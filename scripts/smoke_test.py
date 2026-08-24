#!/usr/bin/env python3
"""End-to-end HTTP smoke check for the running Compose stack."""

import json
import os
import urllib.request


BASE = os.environ.get("LAB_URL", "http://127.0.0.1:8080").rstrip("/")


def request(path, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"Content-Type": "application/json"} if data else {}
    method = "POST" if data else "GET"
    call = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    with urllib.request.urlopen(call, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    health = request("/health")
    assert health["status"] == "ok"
    assert health["indexed_documents"] >= 3
    assert health["bitcoin_core"]["reachable"] is True

    search = request("/api/v1/search?q=package%20relay%20fee%20bumping&collection=delving-bitcoin")
    assert search["count"] >= 1
    assert search["results"][0]["id"] == "delving-package-relay-fixture"

    script = request("/api/v1/script/evaluate", {"unlocking_script": "2 3 OP_ADD", "locking_script": "5 OP_EQUAL"})
    assert script["success"] is True
    assert script["backend"] == "rust-bitcoinkernel"
    assert script["backend_revision"] == "691a90cc0c20761cc9b35a783e0e84c77245d555"
    assert script["consensus_engine"] == "Bitcoin Core libbitcoinkernel"
    assert script["consensus_compatible"] is True
    assert len(script["trace"]) >= 5

    bitcoin = request("/api/v1/bitcoin/status")
    assert bitcoin["reachable"] is True
    assert bitcoin["chain"] == "regtest"

    print(json.dumps({
        "status": "ok",
        "indexed_documents": health["indexed_documents"],
        "search_top_id": search["results"][0]["id"],
        "script_backend": script["backend"],
        "script_backend_revision": script["backend_revision"],
        "script_trace_frames": len(script["trace"]),
        "bitcoin_core": bitcoin,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
