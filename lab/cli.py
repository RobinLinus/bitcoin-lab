"""Command-line entrypoint for the Bitcoin Research Lab."""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

from .bitcoin_rpc import status as bitcoin_status
from .interpreter import evaluate_script
from .library import SearchIndex, default_index_path, default_library_path, load_documents, validate_manifests
from .server import serve


def _json(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--index-path", type=Path, default=default_index_path())
    commands = root.add_subparsers(dest="command", required=True)

    commands.add_parser("validate", help="validate manifests and document metadata")
    commands.add_parser("index", help="rebuild the full-text index")

    search = commands.add_parser("search", help="search document text and metadata")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--collection")
    search.add_argument("--source-type")
    search.add_argument("--author")
    search.add_argument("--tag")
    search.add_argument("--year", type=int)
    search.add_argument("--limit", type=int, default=10)

    script = commands.add_parser("script", help="evaluate a Script pair")
    script.add_argument("--unlocking", default="")
    script.add_argument("--locking", required=True)

    commands.add_parser("bitcoin-status", help="query the configured Bitcoin Core RPC")

    server = commands.add_parser("serve", help="index the library and start the HTTP service")
    server.add_argument("--host", default="127.0.0.1")
    server.add_argument("--port", type=int, default=8080)
    return root


def main() -> None:
    arguments = parser().parse_args()
    index = SearchIndex(arguments.index_path)
    if arguments.command == "validate":
        documents = load_documents(default_library_path())
        manifests = validate_manifests(default_library_path())
        _json({"documents": len(documents), "manifests": len(manifests), "status": "valid"})
    elif arguments.command == "index":
        _json({"indexed_documents": index.rebuild(default_library_path()), "index_path": str(index.path)})
    elif arguments.command == "search":
        if not index.count():
            index.rebuild(default_library_path())
        _json(
            index.search(
                arguments.query,
                collection=arguments.collection,
                source_type=arguments.source_type,
                author=arguments.author,
                tag=arguments.tag,
                year=arguments.year,
                limit=arguments.limit,
            )
        )
    elif arguments.command == "script":
        _json(evaluate_script(arguments.unlocking, arguments.locking))
    elif arguments.command == "bitcoin-status":
        _json(bitcoin_status())
    elif arguments.command == "serve":
        index.rebuild(default_library_path())
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
        serve(arguments.host, arguments.port, index)


if __name__ == "__main__":
    main()
