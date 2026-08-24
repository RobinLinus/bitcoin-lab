"""Document loading, validation, and SQLite full-text indexing."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


COLLECTIONS = {
    "papers",
    "delving-bitcoin",
    "mailing-lists",
    "robinlinus",
    "fairgate",
    "alpen",
    "babylon",
    "bitcoin-scripts",
    "bitvm-opcodes",
    "robinlinus-gists",
    "citrea-docs",
}
SOURCE_TYPES = {"paper", "article", "mailing-list-thread", "source-code"}
QUERY_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "could", "did", "do",
    "does", "explain", "for", "from", "help", "helps", "how", "in", "is", "it", "of",
    "on", "or", "should", "the", "this", "to", "was", "what", "when", "where", "which",
    "who", "why", "with", "would",
}
REQUIRED_FIELDS = {
    "schema_version",
    "id",
    "title",
    "authors",
    "published_at",
    "source_type",
    "collection",
    "canonical_url",
    "content_file",
    "license",
    "retrieved_at",
    "abstract",
    "tags",
    "bitcoin_topics",
    "source_manifest",
    "provenance",
}


class LibraryError(ValueError):
    """Raised when a library document is invalid."""


@dataclass(frozen=True)
class LibraryDocument:
    metadata: Dict[str, Any]
    body: str
    metadata_path: Path
    content_path: Path
    checksum: str

    @property
    def id(self) -> str:
        return str(self.metadata["id"])


def default_library_path() -> Path:
    return Path(os.environ.get("LAB_LIBRARY_PATH", Path(__file__).resolve().parents[1] / "library"))


def default_index_path() -> Path:
    configured = os.environ.get("LAB_INDEX_PATH")
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parents[1] / "data" / "library.db"


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LibraryError("{}: cannot read JSON: {}".format(path, exc)) from exc
    if not isinstance(value, dict):
        raise LibraryError("{}: expected a JSON object".format(path))
    return value


def validate_metadata(metadata: Dict[str, Any], metadata_path: Path, library_path: Path) -> Path:
    missing = sorted(REQUIRED_FIELDS.difference(metadata))
    if missing:
        raise LibraryError("{}: missing fields: {}".format(metadata_path, ", ".join(missing)))

    identifier = metadata.get("id")
    if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._-]{2,127}", identifier):
        raise LibraryError("{}: id must be a stable lowercase slug".format(metadata_path))
    if metadata.get("collection") not in COLLECTIONS:
        raise LibraryError("{}: unsupported collection".format(metadata_path))
    if metadata.get("source_type") not in SOURCE_TYPES:
        raise LibraryError("{}: unsupported source_type".format(metadata_path))
    for name in ("authors", "tags", "bitcoin_topics"):
        if not isinstance(metadata.get(name), list) or not all(isinstance(item, str) for item in metadata[name]):
            raise LibraryError("{}: {} must be an array of strings".format(metadata_path, name))
    if not isinstance(metadata.get("provenance"), dict):
        raise LibraryError("{}: provenance must be an object".format(metadata_path))

    content_path = (metadata_path.parent / str(metadata["content_file"])).resolve()
    documents_root = (library_path / "documents").resolve()
    try:
        content_path.relative_to(documents_root)
    except ValueError as exc:
        raise LibraryError("{}: content_file escapes the documents directory".format(metadata_path)) from exc
    if not content_path.is_file():
        raise LibraryError("{}: content file does not exist: {}".format(metadata_path, content_path))

    manifest_path = (library_path / str(metadata["source_manifest"])).resolve()
    try:
        manifest_path.relative_to(library_path.resolve())
    except ValueError as exc:
        raise LibraryError("{}: source_manifest escapes the library".format(metadata_path)) from exc
    if not manifest_path.is_file():
        raise LibraryError("{}: source manifest does not exist".format(metadata_path))
    return content_path


def load_documents(library_path: Optional[Path] = None) -> List[LibraryDocument]:
    library_path = (library_path or default_library_path()).resolve()
    document_root = library_path / "documents"
    if not document_root.is_dir():
        raise LibraryError("document directory does not exist: {}".format(document_root))

    documents: List[LibraryDocument] = []
    seen = set()
    for metadata_path in sorted(document_root.rglob("*.metadata.json")):
        metadata = _read_json(metadata_path)
        content_path = validate_metadata(metadata, metadata_path, library_path)
        if metadata["id"] in seen:
            raise LibraryError("duplicate document id: {}".format(metadata["id"]))
        seen.add(metadata["id"])
        body = content_path.read_text(encoding="utf-8")
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        documents.append(LibraryDocument(metadata, body, metadata_path, content_path, digest))
    if not documents:
        raise LibraryError("no metadata documents found under {}".format(document_root))
    return documents


def validate_manifests(library_path: Optional[Path] = None) -> List[Path]:
    library_path = (library_path or default_library_path()).resolve()
    paths = sorted((library_path / "manifests").glob("*.json"))
    if not paths:
        raise LibraryError("no source manifests found")
    for path in paths:
        manifest = _read_json(path)
        for field in ("schema_version", "id", "collection", "source_name", "homepage", "ingestion", "entries"):
            if field not in manifest:
                raise LibraryError("{}: missing manifest field {}".format(path, field))
        if manifest["collection"] not in COLLECTIONS:
            raise LibraryError("{}: unsupported collection".format(path))
        if not isinstance(manifest["entries"], list):
            raise LibraryError("{}: entries must be an array".format(path))
    return paths


class SearchIndex:
    """Small SQLite FTS5 index rebuilt atomically from versioned documents."""

    def __init__(self, path: Optional[Path] = None):
        self.path = Path(path or default_index_path())

    def _connect(self) -> sqlite3.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(str(self.path), timeout=10)
        connection.row_factory = sqlite3.Row
        return connection

    def rebuild(self, library_path: Optional[Path] = None) -> int:
        documents = load_documents(library_path)
        with self._connect() as connection:
            connection.executescript(
                """
                DROP TABLE IF EXISTS documents;
                DROP TABLE IF EXISTS documents_fts;
                CREATE TABLE documents (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    abstract TEXT NOT NULL,
                    authors TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    bitcoin_topics TEXT NOT NULL,
                    published_at TEXT NOT NULL,
                    source_type TEXT NOT NULL,
                    collection TEXT NOT NULL,
                    canonical_url TEXT NOT NULL,
                    license TEXT NOT NULL,
                    content_path TEXT NOT NULL,
                    checksum TEXT NOT NULL,
                    body TEXT NOT NULL,
                    metadata TEXT NOT NULL
                );
                CREATE VIRTUAL TABLE documents_fts USING fts5(
                    id UNINDEXED, title, abstract, body, authors, tags,
                    tokenize='unicode61 remove_diacritics 2'
                );
                """
            )
            for document in documents:
                metadata = document.metadata
                fields = (
                    document.id,
                    metadata["title"],
                    metadata["abstract"],
                    json.dumps(metadata["authors"]),
                    json.dumps(metadata["tags"]),
                    json.dumps(metadata["bitcoin_topics"]),
                    metadata["published_at"],
                    metadata["source_type"],
                    metadata["collection"],
                    metadata["canonical_url"],
                    metadata["license"],
                    str(document.content_path),
                    document.checksum,
                    document.body,
                    json.dumps(metadata, sort_keys=True),
                )
                connection.execute("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", fields)
                connection.execute(
                    "INSERT INTO documents_fts VALUES (?,?,?,?,?,?)",
                    (
                        document.id,
                        metadata["title"],
                        metadata["abstract"],
                        document.body,
                        " ".join(metadata["authors"]),
                        " ".join(metadata["tags"] + metadata["bitcoin_topics"]),
                    ),
                )
        return len(documents)

    def count(self) -> int:
        if not self.path.exists():
            return 0
        with self._connect() as connection:
            row = connection.execute("SELECT count(*) AS count FROM documents").fetchone()
            return int(row["count"])

    @staticmethod
    def _fts_query(query: str) -> str:
        all_terms = re.findall(r"[\w-]+", query.lower(), re.UNICODE)
        terms = [term for term in all_terms if term not in QUERY_STOPWORDS]
        if not terms:
            terms = all_terms
        if not terms:
            return ""
        return " AND ".join('"{}"'.format(term.replace('"', '""')) for term in terms[:24])

    @staticmethod
    def _result(row: sqlite3.Row) -> Dict[str, Any]:
        metadata = json.loads(row["metadata"])
        return {
            "id": row["id"],
            "title": row["title"],
            "abstract": row["abstract"],
            "authors": json.loads(row["authors"]),
            "tags": json.loads(row["tags"]),
            "bitcoin_topics": json.loads(row["bitcoin_topics"]),
            "published_at": row["published_at"],
            "source_type": row["source_type"],
            "collection": row["collection"],
            "canonical_url": row["canonical_url"],
            "license": row["license"],
            "checksum": row["checksum"],
            "snippet": row["snippet"] if "snippet" in row.keys() else row["abstract"],
            "score": row["score"] if "score" in row.keys() else 0.0,
            "metadata": metadata,
        }

    def search(
        self,
        query: str = "",
        collection: Optional[str] = None,
        source_type: Optional[str] = None,
        author: Optional[str] = None,
        tag: Optional[str] = None,
        year: Optional[int] = None,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        limit = max(1, min(int(limit), 50))
        where = []
        parameters: List[Any] = []
        if collection:
            where.append("d.collection = ?")
            parameters.append(collection)
        if source_type:
            where.append("d.source_type = ?")
            parameters.append(source_type)
        if author:
            where.append("lower(d.authors) LIKE ?")
            parameters.append("%{}%".format(author.lower()))
        if tag:
            where.append("(lower(d.tags) LIKE ? OR lower(d.bitcoin_topics) LIKE ?)")
            parameters.extend(["%{}%".format(tag.lower())] * 2)
        if year:
            where.append("substr(d.published_at, 1, 4) = ?")
            parameters.append(str(year))

        fts_query = self._fts_query(query)
        if fts_query:
            where.insert(0, "documents_fts MATCH ?")
            parameters.insert(0, fts_query)
            sql = """
                SELECT d.*, bm25(documents_fts, 0.0, 8.0, 4.0, 1.0, 2.0, 3.0) AS score,
                       snippet(documents_fts, 3, '', '', ' … ', 32) AS snippet
                FROM documents_fts
                JOIN documents d ON d.id = documents_fts.id
            """
            order = " ORDER BY score, d.published_at DESC"
        else:
            sql = "SELECT d.*, 0.0 AS score, d.abstract AS snippet FROM documents d"
            order = " ORDER BY d.published_at DESC, d.id"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += order + " LIMIT ?"
        parameters.append(limit)
        with self._connect() as connection:
            return [self._result(row) for row in connection.execute(sql, parameters).fetchall()]

    def get(self, document_id: str) -> Optional[Dict[str, Any]]:
        with self._connect() as connection:
            row = connection.execute("SELECT *, abstract AS snippet, 0.0 AS score FROM documents WHERE id = ?", (document_id,)).fetchone()
            if row is None:
                return None
            result = self._result(row)
            result["body"] = row["body"]
            return result
