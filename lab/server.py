"""Standard-library HTTP API for search, Script, and Bitcoin Core regtest status."""

from __future__ import annotations

import json
import logging
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict
from urllib.parse import parse_qs, unquote, urlparse

from . import __version__
from .bitcoin_rpc import status as bitcoin_status
from .interpreter import evaluate_script
from .library import SearchIndex, default_library_path


LOGGER = logging.getLogger(__name__)
MAX_REQUEST_BYTES = 1_000_000


class LabHTTPServer(ThreadingHTTPServer):
    index: SearchIndex


class Handler(BaseHTTPRequestHandler):
    server_version = "BitcoinResearchLab/{}".format(__version__)

    def log_message(self, pattern: str, *args: Any) -> None:
        LOGGER.info("%s - %s", self.address_string(), pattern % args)

    def _send(self, status: int, payload: Dict[str, Any]) -> None:
        encoded = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(encoded)

    def _body(self) -> Dict[str, Any]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError as exc:
            raise ValueError("invalid Content-Length") from exc
        if length <= 0 or length > MAX_REQUEST_BYTES:
            raise ValueError("request body must be between 1 and {} bytes".format(MAX_REQUEST_BYTES))
        try:
            value = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("request body must be a JSON object") from exc
        if not isinstance(value, dict):
            raise ValueError("request body must be a JSON object")
        return value

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(HTTPStatus.NO_CONTENT)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/health":
                self._send(
                    HTTPStatus.OK,
                    {
                        "status": "ok",
                        "version": __version__,
                        "indexed_documents": self.server.index.count(),
                        "bitcoin_core": bitcoin_status(),
                    },
                )
                return
            if parsed.path == "/api/v1/bitcoin/status":
                core = bitcoin_status()
                self._send(HTTPStatus.OK if core["reachable"] else HTTPStatus.SERVICE_UNAVAILABLE, core)
                return
            if parsed.path == "/api/v1/search":
                query = parse_qs(parsed.query)
                one = lambda name: query.get(name, [None])[0]
                results = self.server.index.search(
                    query=one("q") or "",
                    collection=one("collection"),
                    source_type=one("source_type"),
                    author=one("author"),
                    tag=one("tag"),
                    year=int(one("year")) if one("year") else None,
                    limit=int(one("limit") or 10),
                )
                self._send(HTTPStatus.OK, {"count": len(results), "results": results})
                return
            prefix = "/api/v1/documents/"
            if parsed.path.startswith(prefix):
                document = self.server.index.get(unquote(parsed.path[len(prefix):]))
                if document is None:
                    self._send(HTTPStatus.NOT_FOUND, {"error": "document not found"})
                else:
                    self._send(HTTPStatus.OK, document)
                return
            self._send(HTTPStatus.NOT_FOUND, {"error": "route not found"})
        except (ValueError, TypeError) as exc:
            self._send(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except Exception as exc:  # defensive API boundary
            LOGGER.exception("GET failed")
            self._send(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        try:
            body = self._body()
            if parsed.path == "/api/v1/script/evaluate":
                result = evaluate_script(str(body.get("unlocking_script", "")), str(body.get("locking_script", "")))
                self._send(HTTPStatus.OK, result)
                return
            if parsed.path == "/api/v1/index/rebuild":
                count = self.server.index.rebuild(default_library_path())
                self._send(HTTPStatus.OK, {"indexed_documents": count})
                return
            self._send(HTTPStatus.NOT_FOUND, {"error": "route not found"})
        except (ValueError, TypeError) as exc:
            self._send(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except RuntimeError as exc:
            self._send(HTTPStatus.BAD_GATEWAY, {"error": str(exc)})
        except Exception as exc:  # defensive API boundary
            LOGGER.exception("POST failed")
            self._send(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})


def serve(host: str, port: int, index: SearchIndex) -> None:
    server = LabHTTPServer((host, port), Handler)
    server.index = index
    LOGGER.info("Bitcoin Research Lab listening on http://%s:%s", host, port)
    server.serve_forever()
