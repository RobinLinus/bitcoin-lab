#!/usr/bin/env python3
"""Incrementally ingest bounded public-source snapshots into the research library.

The registry is data, not code: it defines source limits, allowed hosts, rights
notes, immutable Git commits, and discovery strategies. HTTP crawling is denied
unless robots.txt explicitly permits the URL (a missing/404 robots file follows
the standard allow-all convention). GitHub Git/API sources use their published
interfaces and terms rather than scraping GitHub web pages.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import mimetypes
import os
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = ROOT / "library"
FETCHER_VERSION = "1.0.0"
MAX_RESPONSE_BYTES = 24 * 1024 * 1024
MAX_TEXT_FILE_BYTES = 2 * 1024 * 1024


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_from(value: Optional[str], fallback: str) -> str:
    if value:
        match = re.search(r"\b(20\d\d-[01]\d-[0-3]\d)\b", value)
        if match:
            return match.group(1)
    return fallback[:10]


def slug(value: str, limit: int = 62) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (cleaned or "document")[:limit].rstrip("-")


def unique(values: Iterable[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        value = value.strip()
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def json_read(path: Path) -> Dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("{} must contain a JSON object".format(path))
    return value


def json_write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


class VisibleHTML(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title_parts: List[str] = []
        self.text_parts: List[str] = []
        self.links: List[str] = []
        self.meta: Dict[str, str] = {}
        self.canonical: Optional[str] = None
        self._skip = 0
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: Sequence[Tuple[str, Optional[str]]]) -> None:
        attributes = {name.lower(): (value or "") for name, value in attrs}
        if tag in {"script", "style", "svg", "template"}:
            self._skip += 1
        if tag == "title":
            self._in_title = True
        if tag == "a" and attributes.get("href"):
            self.links.append(urllib.parse.urljoin(self.base_url, attributes["href"]))
        if tag == "link" and "canonical" in attributes.get("rel", "").lower():
            candidate = urllib.parse.urljoin(self.base_url, attributes.get("href", ""))
            if candidate:
                self.canonical = candidate
        if tag == "meta":
            key = (attributes.get("property") or attributes.get("name") or "").lower()
            content = attributes.get("content", "").strip()
            if key and content:
                self.meta[key] = content

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "template"} and self._skip:
            self._skip -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._skip:
            return
        normalized = " ".join(data.split())
        if not normalized:
            return
        if self._in_title:
            self.title_parts.append(normalized)
        else:
            self.text_parts.append(normalized)

    @property
    def title(self) -> str:
        return " ".join(self.title_parts).strip()

    @property
    def text(self) -> str:
        return "\n\n".join(self.text_parts).strip()


@dataclass
class Response:
    url: str
    status: int
    headers: Dict[str, str]
    body: bytes

    @property
    def content_type(self) -> str:
        return self.headers.get("content-type", "application/octet-stream").split(";", 1)[0].lower()


class PublicFetcher:
    def __init__(self, user_agent: str, delay: float, timeout: int):
        self.user_agent = user_agent
        self.delay = delay
        self.timeout = timeout
        self.last_request: Dict[str, float] = {}
        self.robots: Dict[str, Tuple[str, Optional[urllib.robotparser.RobotFileParser]]] = {}

    def _pace(self, host: str) -> None:
        elapsed = time.monotonic() - self.last_request.get(host, 0.0)
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

    def _request(self, url: str, accept: str) -> Response:
        host = (urllib.parse.urlparse(url).hostname or "").lower()
        self._pace(host)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": self.user_agent, "Accept": accept},
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as handle:
                body = handle.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise ValueError("response exceeds {} bytes".format(MAX_RESPONSE_BYTES))
                return Response(
                    url=handle.geturl(),
                    status=int(handle.status),
                    headers={key.lower(): value for key, value in handle.headers.items()},
                    body=body,
                )
        finally:
            self.last_request[host] = time.monotonic()

    def _robots_policy(self, source: Dict[str, Any], url: str) -> Tuple[str, Optional[urllib.robotparser.RobotFileParser]]:
        host = (urllib.parse.urlparse(url).hostname or "").lower()
        if host in self.robots:
            return self.robots[host]
        configured = source.get("robots_url")
        configured_host = (urllib.parse.urlparse(configured).hostname or "").lower() if configured else ""
        robots_url = configured if configured_host == host else "https://{}/robots.txt".format(host)
        try:
            response = self._request(str(robots_url), "text/plain,*/*;q=0.1")
            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(str(robots_url))
            parser.parse(response.body.decode("utf-8", errors="replace").splitlines())
            policy = ("loaded:{}".format(response.status), parser)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                policy = ("missing:404-allow", None)
            else:
                policy = ("denied:http-{}".format(exc.code), False)  # type: ignore[assignment]
        except Exception as exc:
            policy = ("denied:{}".format(type(exc).__name__), False)  # type: ignore[assignment]
        self.robots[host] = policy
        return policy

    def fetch_http(self, source: Dict[str, Any], url: str, accept: str = "*/*") -> Response:
        host = (urllib.parse.urlparse(url).hostname or "").lower()
        if host not in {item.lower() for item in source.get("allowed_hosts", [])}:
            raise PermissionError("host not in source allowlist: {}".format(host))
        status, parser = self._robots_policy(source, url)
        if parser is False or (parser is not None and not parser.can_fetch(self.user_agent, url)):
            raise PermissionError("robots denied {} ({})".format(url, status))
        return self._request(url, accept)

    def fetch_api(self, url: str) -> Response:
        return self._request(url, "application/vnd.github+json")


def normalized_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, ""))


def allowed_candidate(source: Dict[str, Any], url: str) -> bool:
    url = normalized_url(url)
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    if host not in {item.lower() for item in source.get("allowed_hosts", [])}:
        return False
    include = source.get("include_pattern")
    exclude = source.get("exclude_pattern")
    return (not include or re.search(include, url) is not None) and (not exclude or re.search(exclude, url) is None)


def decode_response(response: Response) -> str:
    match = re.search(r"charset=([^; ]+)", response.headers.get("content-type", ""), re.I)
    encoding = match.group(1).strip('"\'') if match else "utf-8"
    try:
        return response.body.decode(encoding, errors="replace")
    except LookupError:
        return response.body.decode("utf-8", errors="replace")


def discover_http(source: Dict[str, Any], fetcher: PublicFetcher) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    response = fetcher.fetch_http(source, source["discovery_url"], "application/json,text/html,*/*;q=0.1")
    details: Dict[str, Any] = {
        "discovery_status": response.status,
        "discovery_content_type": response.content_type,
    }
    candidates: List[Dict[str, str]] = []
    if source["strategy"] == "discourse-latest":
        payload = json.loads(response.body.decode("utf-8"))
        topics = payload.get("topic_list", {}).get("topics", [])
        for topic in topics:
            topic_id = int(topic["id"])
            topic_slug = str(topic.get("slug") or topic_id)
            canonical = "https://delvingbitcoin.org/t/{}/{}".format(topic_slug, topic_id)
            candidates.append({"fetch_url": canonical + ".json", "canonical_url": canonical})
    else:
        page = VisibleHTML(response.url)
        page.feed(decode_response(response))
        details["discovery_links"] = len(page.links)
        for url in source.get("seed_urls", []):
            if allowed_candidate(source, url):
                candidates.append({"fetch_url": normalized_url(url), "canonical_url": normalized_url(url)})
        for url in page.links:
            if allowed_candidate(source, url):
                candidates.append({"fetch_url": normalized_url(url), "canonical_url": normalized_url(url)})
    deduplicated: List[Dict[str, str]] = []
    seen = set()
    for item in candidates:
        key = item["canonical_url"]
        if key not in seen:
            seen.add(key)
            deduplicated.append(item)
    return deduplicated, details


def raw_extension(response: Response, url: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix and len(suffix) <= 8:
        return suffix
    guessed = mimetypes.guess_extension(response.content_type) or ".bin"
    return ".html" if response.content_type == "text/html" else guessed


def pdf_text(raw_path: Path) -> Tuple[str, str]:
    executable = shutil.which("pdftotext")
    if not executable:
        return "", "pdftotext was not installed; the PDF is retained and indexed by title/provenance only."
    with tempfile.TemporaryDirectory(prefix="bitcoin-lab-pdf-") as directory:
        output = Path(directory) / "document.txt"
        completed = subprocess.run(
            [executable, "-layout", str(raw_path), str(output)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90,
        )
        if completed.returncode or not output.exists():
            return "", "pdftotext failed: {}".format(completed.stderr.strip()[:240])
        return output.read_text(encoding="utf-8", errors="replace").strip(), "PDF text extracted with pdftotext."


def markdown_document(title: str, canonical: str, retrieved: str, body: str, note: str = "") -> str:
    header = "# {}\n\nSource: {}\n\nRetrieved: {}\n".format(title.strip(), canonical, retrieved)
    if note:
        header += "\nExtraction note: {}\n".format(note)
    return header + "\n---\n\n" + body.strip() + "\n"


def save_document(
    library: Path,
    source: Dict[str, Any],
    canonical: str,
    title: str,
    authors: List[str],
    published: str,
    source_type: str,
    body: str,
    raw_bytes: bytes,
    raw_suffix: str,
    retrieval: Dict[str, Any],
    abstract_hint: str = "",
) -> Dict[str, Any]:
    digest = hashlib.sha256(raw_bytes).hexdigest()
    identifier = "{}-{}-{}".format(source["id"], slug(title), hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:10])
    collection = source["collection"]
    document_dir = library / "documents" / collection
    raw_dir = library / "raw" / source["id"]
    document_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_name = identifier + raw_suffix
    raw_path = raw_dir / raw_name
    content_name = identifier + ".md"
    metadata_name = identifier + ".metadata.json"
    raw_path.write_bytes(raw_bytes)
    (document_dir / content_name).write_text(body, encoding="utf-8")
    normalized_abstract = " ".join((abstract_hint or re.sub(r"[#>`*_\[\]()]", " ", body)).split())
    if not normalized_abstract:
        normalized_abstract = "Public source snapshot from {}.".format(source["source_name"])
    retrieved = retrieval["retrieved_at"]
    retrieval = dict(retrieval)
    retrieval.update(
        {
            "sha256": digest,
            "raw_file": raw_path.relative_to(library).as_posix(),
            "fetcher_version": FETCHER_VERSION,
        }
    )
    metadata = {
        "schema_version": "1.0.0",
        "id": identifier,
        "title": title.strip() or identifier,
        "authors": unique(authors) or [source["source_name"]],
        "published_at": date_from(published, retrieved),
        "source_type": source_type,
        "collection": collection,
        "canonical_url": canonical,
        "content_file": content_name,
        "license": source["rights_policy"],
        "retrieved_at": retrieved[:10],
        "abstract": normalized_abstract[:600],
        "tags": unique(source.get("tags", []) + ["public-source", "ingested"]),
        "bitcoin_topics": unique(source.get("bitcoin_topics", [])),
        "source_manifest": source["manifest"],
        "provenance": {
            "content_kind": "source-text",
            "is_sample": False,
            "notes": "Incremental bounded ingestion; see library/source-registry.json and library/ingestion/latest-report.json.",
            "source_license": source["rights_policy"],
        },
        "retrieval": retrieval,
    }
    json_write(document_dir / metadata_name, metadata)
    entry = {
        "id": identifier,
        "canonical_url": canonical,
        "local_metadata_file": (document_dir / metadata_name).relative_to(library).as_posix(),
        "enabled": True,
        "retrieved_at": retrieved,
        "sha256": digest,
        "raw_file": raw_path.relative_to(library).as_posix(),
        "managed_by": "scripts/ingest_sources.py",
    }
    for name in ("repository", "commit", "revision", "path"):
        if retrieval.get(name):
            entry[name] = retrieval[name]
    return entry


def ingest_http_item(
    library: Path,
    source: Dict[str, Any],
    candidate: Dict[str, str],
    fetcher: PublicFetcher,
    retrieved: str,
) -> Dict[str, Any]:
    response = fetcher.fetch_http(source, candidate["fetch_url"], "application/json,text/html,application/pdf,*/*;q=0.1")
    canonical = candidate["canonical_url"]
    title = Path(urllib.parse.urlparse(canonical).path).name or source["source_name"]
    authors = [source["source_name"]]
    published = retrieved
    abstract_hint = ""
    suffix = raw_extension(response, response.url)
    extraction_note = ""
    if response.content_type == "application/json" and source["strategy"] == "discourse-latest":
        payload = json.loads(response.body.decode("utf-8"))
        title = str(payload.get("title") or title)
        posts = payload.get("post_stream", {}).get("posts", [])
        pieces = []
        authors = []
        for post in posts:
            author = str(post.get("name") or post.get("username") or source["source_name"])
            authors.append(author)
            fragment = VisibleHTML(canonical)
            fragment.feed(str(post.get("cooked") or ""))
            pieces.append("## {}\n\n{}".format(author, fragment.text))
        published = str(posts[0].get("created_at") or retrieved) if posts else retrieved
        body_text = "\n\n".join(pieces)
        abstract_hint = str(payload.get("fancy_title") or title)
    elif response.content_type == "text/html" or suffix in {".html", ".htm"}:
        page = VisibleHTML(response.url)
        page.feed(decode_response(response))
        title = page.meta.get("og:title") or page.title or title
        authors = [page.meta.get("author") or page.meta.get("article:author") or source["source_name"]]
        published = page.meta.get("article:published_time") or page.meta.get("date") or retrieved
        abstract_hint = page.meta.get("description") or page.meta.get("og:description") or ""
        if page.canonical and allowed_candidate(source, page.canonical):
            canonical = normalized_url(page.canonical)
        body_text = page.text
    elif response.content_type == "application/pdf" or suffix == ".pdf":
        temporary_raw = library / "raw" / source["id"] / ("extract-" + hashlib.sha256(canonical.encode()).hexdigest()[:10] + ".pdf")
        temporary_raw.parent.mkdir(parents=True, exist_ok=True)
        temporary_raw.write_bytes(response.body)
        body_text, extraction_note = pdf_text(temporary_raw)
        temporary_raw.unlink(missing_ok=True)
        title = urllib.parse.unquote(Path(urllib.parse.urlparse(canonical).path).stem).replace("_", " ").replace("-", " ")
        source_type = "paper"
        body = markdown_document(title, canonical, retrieved, body_text or "PDF retained in the raw source directory.", extraction_note)
        return save_document(
            library,
            source,
            canonical,
            title,
            authors,
            published,
            source_type,
            body,
            response.body,
            ".pdf",
            {
                "method": "public-http",
                "fetched_url": response.url,
                "retrieved_at": retrieved,
                "http_status": response.status,
                "content_type": response.content_type,
            },
            abstract_hint,
        )
    else:
        body_text = decode_response(response)
    body = markdown_document(title, canonical, retrieved, body_text, extraction_note)
    return save_document(
        library,
        source,
        canonical,
        title,
        authors,
        published,
        source["source_type"],
        body,
        response.body,
        suffix,
        {
            "method": "public-http",
            "fetched_url": response.url,
            "retrieved_at": retrieved,
            "http_status": response.status,
            "content_type": response.content_type,
        },
        abstract_hint,
    )


def run_git(arguments: Sequence[str], cwd: Path, timeout: int = 120) -> str:
    completed = subprocess.run(
        list(arguments),
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
    )
    if completed.returncode:
        raise RuntimeError("{}: {}".format(" ".join(arguments), completed.stderr.strip()[:500]))
    return completed.stdout.strip()


def ingest_git_source(library: Path, source: Dict[str, Any], retrieved: str, limit: int) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    commit = source["pinned_commit"]
    repository = source["repository"]
    pattern = re.compile(source["include_pattern"])
    entries: List[Dict[str, Any]] = []
    detail: Dict[str, Any] = {"pinned_commit": commit, "repository": repository}
    with tempfile.TemporaryDirectory(prefix="bitcoin-lab-git-") as directory:
        checkout = Path(directory)
        run_git(["git", "init", "--quiet"], checkout)
        run_git(["git", "fetch", "--quiet", "--depth=1", repository, commit], checkout)
        run_git(["git", "checkout", "--quiet", "--detach", "FETCH_HEAD"], checkout)
        actual = run_git(["git", "rev-parse", "HEAD"], checkout)
        if actual != commit:
            raise RuntimeError("pinned commit mismatch: expected {}, got {}".format(commit, actual))
        authored = run_git(["git", "show", "-s", "--format=%aI", commit], checkout)
        files = run_git(["git", "ls-tree", "-r", "--name-only", commit], checkout).splitlines()
        candidates = [path for path in files if pattern.search(path)]
        detail["matched_files"] = len(candidates)
        detail["license_files"] = [path for path in files if re.search(r"(^|/)(LICENSE|COPYING)(\..*)?$", path, re.I)][:10]
        web_repository = repository.removesuffix(".git")
        for path_string in candidates[:limit]:
            path = checkout / path_string
            raw = path.read_bytes()
            if len(raw) > MAX_TEXT_FILE_BYTES:
                detail.setdefault("skips", []).append({"path": path_string, "reason": "file-too-large"})
                continue
            if b"\x00" in raw:
                detail.setdefault("skips", []).append({"path": path_string, "reason": "binary"})
                continue
            text = raw.decode("utf-8", errors="replace")
            canonical = "{}/blob/{}/{}".format(web_repository, commit, urllib.parse.quote(path_string))
            language = Path(path_string).suffix.lstrip(".")
            body = markdown_document(
                path_string,
                canonical,
                retrieved,
                "````{}\n{}\n````".format(language, text.rstrip()),
                "Exact text file from immutable Git commit {}.".format(commit),
            )
            raw_suffix = Path(path_string).suffix or ".txt"
            entry = save_document(
                library,
                source,
                canonical,
                path_string,
                [source["source_name"]],
                authored,
                source["source_type"],
                body,
                raw,
                raw_suffix,
                {
                    "method": "public-git",
                    "repository": repository,
                    "commit": commit,
                    "path": path_string,
                    "retrieved_at": retrieved,
                    "content_type": "text/plain",
                },
                "{} at pinned commit {}.".format(path_string, commit),
            )
            entries.append(entry)
    return entries, detail


def gist_anchor(filename: str) -> str:
    return "file-" + re.sub(r"[^a-z0-9]+", "-", filename.lower()).strip("-")


def ingest_gists(
    library: Path,
    source: Dict[str, Any],
    fetcher: PublicFetcher,
    retrieved: str,
    limit: int,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    listing = fetcher.fetch_api(source["discovery_url"])
    summaries = json.loads(listing.body.decode("utf-8"))
    if not isinstance(summaries, list):
        raise ValueError("GitHub gists listing was not an array")
    max_gists = min(int(source.get("max_gists", 10)), len(summaries))
    detail: Dict[str, Any] = {
        "discovered_gists": len(summaries),
        "selected_gists": max_gists,
        "github_rate_limit_remaining": listing.headers.get("x-ratelimit-remaining", "unknown"),
    }
    entries: List[Dict[str, Any]] = []
    for summary in summaries[:max_gists]:
        if len(entries) >= limit:
            break
        response = fetcher.fetch_api(summary["url"])
        gist = json.loads(response.body.decode("utf-8"))
        history = gist.get("history") or []
        revision = str(history[0].get("version")) if history else str(gist.get("updated_at") or "unknown")
        for filename, file_value in (gist.get("files") or {}).items():
            if len(entries) >= limit:
                break
            raw: Optional[bytes] = None
            content = file_value.get("content")
            if content is not None and not file_value.get("truncated"):
                raw = str(content).encode("utf-8")
            elif file_value.get("raw_url"):
                raw_source = dict(source)
                raw_source["allowed_hosts"] = unique(source.get("allowed_hosts", []) + ["gist.githubusercontent.com"])
                raw_response = fetcher.fetch_http(raw_source, file_value["raw_url"], "text/plain")
                raw = raw_response.body
            if raw is None:
                detail.setdefault("skips", []).append({"gist": gist.get("id"), "file": filename, "reason": "no-public-content"})
                continue
            if len(raw) > MAX_TEXT_FILE_BYTES or b"\x00" in raw:
                detail.setdefault("skips", []).append({"gist": gist.get("id"), "file": filename, "reason": "large-or-binary"})
                continue
            canonical = "{}#{}".format(gist["html_url"], gist_anchor(filename))
            text = raw.decode("utf-8", errors="replace")
            language = str(file_value.get("language") or Path(filename).suffix.lstrip(".") or "text").lower()
            body = markdown_document(
                "{} / {}".format(gist.get("description") or gist["id"], filename),
                canonical,
                retrieved,
                "````{}\n{}\n````".format(language, text.rstrip()),
                "Current public gist file at revision {}.".format(revision),
            )
            entry = save_document(
                library,
                source,
                canonical,
                "{} / {}".format(gist.get("description") or gist["id"], filename),
                [str((gist.get("owner") or {}).get("login") or "robinLinus")],
                str(gist.get("created_at") or retrieved),
                source["source_type"],
                body,
                raw,
                Path(filename).suffix or ".txt",
                {
                    "method": "public-api",
                    "fetched_url": summary["url"],
                    "revision": revision,
                    "path": filename,
                    "retrieved_at": retrieved,
                    "http_status": response.status,
                    "content_type": str(file_value.get("type") or "text/plain"),
                },
                str(gist.get("description") or "Public gist file {}".format(filename)),
            )
            entries.append(entry)
    return entries, detail


def update_manifest(library: Path, source: Dict[str, Any], new_entries: List[Dict[str, Any]]) -> None:
    path = library / source["manifest"]
    manifest = json_read(path)
    existing = {entry["id"]: entry for entry in manifest.get("entries", [])}
    for entry in new_entries:
        existing[entry["id"]] = entry
    manifest["entries"] = sorted(existing.values(), key=lambda entry: entry["id"])
    if new_entries:
        manifest["ingestion"]["mode"] = "registry-fetcher"
        manifest["ingestion"]["status"] = "ingested"
        manifest["ingestion"]["notes"] = "Incremental snapshot managed by scripts/ingest_sources.py; see library/ingestion/latest-report.json."
    json_write(path, manifest)


def ingest_source(
    library: Path,
    source: Dict[str, Any],
    fetcher: PublicFetcher,
    override_limit: Optional[int],
    dry_run: bool,
) -> Dict[str, Any]:
    retrieved = utc_now()
    limit = min(int(source.get("max_items", 10)), override_limit) if override_limit else int(source.get("max_items", 10))
    report: Dict[str, Any] = {
        "id": source["id"],
        "strategy": source["strategy"],
        "started_at": retrieved,
        "cap": limit,
        "boundary": source["boundary"],
        "rights_policy": source["rights_policy"],
        "status": "running",
        "fetched": 0,
        "skipped": [],
        "errors": [],
    }
    entries: List[Dict[str, Any]] = []
    try:
        if source["strategy"] == "git-repository":
            entries, details = ingest_git_source(library, source, retrieved, limit)
            report.update(details)
            report["discovered"] = details.get("matched_files", len(entries))
        elif source["strategy"] == "github-gists":
            entries, details = ingest_gists(library, source, fetcher, retrieved, limit)
            report.update(details)
            report["discovered"] = details.get("discovered_gists", 0)
        else:
            candidates, details = discover_http(source, fetcher)
            report.update(details)
            report["discovered"] = len(candidates)
            for candidate in candidates[:limit]:
                try:
                    entries.append(ingest_http_item(library, source, candidate, fetcher, retrieved))
                except Exception as exc:
                    report["skipped"].append(
                        {"url": candidate["fetch_url"], "reason": "{}: {}".format(type(exc).__name__, str(exc)[:400])}
                    )
        report["fetched"] = len(entries)
        report["status"] = "ok" if entries else "no-items"
        if not dry_run:
            update_manifest(library, source, entries)
    except Exception as exc:
        report["status"] = "failed"
        report["errors"].append("{}: {}".format(type(exc).__name__, str(exc)[:800]))
    report["finished_at"] = utc_now()
    report["robots"] = {
        host: status for host, (status, _) in sorted(fetcher.robots.items())
        if host in {item.lower() for item in source.get("allowed_hosts", [])}
    }
    return report


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    parser.add_argument("--registry", type=Path)
    parser.add_argument("--source", action="append", help="source ID to ingest; may be repeated")
    parser.add_argument("--max-items", type=int, help="lower every per-source cap for this run")
    parser.add_argument("--dry-run", action="store_true", help="fetch and report without updating manifests/report")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    library = arguments.library.resolve()
    registry_path = (arguments.registry or library / "source-registry.json").resolve()
    registry = json_read(registry_path)
    defaults = registry["defaults"]
    fetcher = PublicFetcher(
        registry["user_agent"],
        float(defaults["delay_seconds"]),
        int(defaults["timeout_seconds"]),
    )
    selected = set(arguments.source or [])
    sources = [source for source in registry["sources"] if not selected or source["id"] in selected]
    unknown = selected.difference(source["id"] for source in sources)
    if unknown:
        raise SystemExit("unknown source(s): {}".format(", ".join(sorted(unknown))))
    started = utc_now()
    reports = [ingest_source(library, source, fetcher, arguments.max_items, arguments.dry_run) for source in sources]
    result = {
        "schema_version": "1.0.0",
        "fetcher_version": FETCHER_VERSION,
        "started_at": started,
        "finished_at": utc_now(),
        "registry": registry_path.relative_to(ROOT).as_posix() if registry_path.is_relative_to(ROOT) else str(registry_path),
        "source_count": len(reports),
        "fetched_documents": sum(item["fetched"] for item in reports),
        "failed_sources": [item["id"] for item in reports if item["status"] == "failed"],
        "no_item_sources": [item["id"] for item in reports if item["status"] == "no-items"],
        "sources": reports,
    }
    if not arguments.dry_run:
        json_write(library / "ingestion" / "latest-report.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["failed_sources"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
