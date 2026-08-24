"""Minimal read-only JSON-RPC client for the Compose Bitcoin Core regtest node."""

from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict


def status() -> Dict[str, Any]:
    url = os.environ.get("BITCOIN_RPC_URL", "http://bitcoin-core:18443")
    user = os.environ.get("BITCOIN_RPC_USER", "lab")
    password = os.environ.get("BITCOIN_RPC_PASSWORD", "lab-regtest-only")
    payload = json.dumps({"jsonrpc": "2.0", "id": "lab", "method": "getblockchaininfo", "params": []}).encode("utf-8")
    credentials = base64.b64encode("{}:{}".format(user, password).encode("utf-8")).decode("ascii")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json", "Authorization": "Basic " + credentials},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=3) as response:
            value = json.loads(response.read().decode("utf-8"))
        result = value.get("result") or {}
        return {
            "reachable": True,
            "chain": result.get("chain"),
            "blocks": result.get("blocks"),
            "headers": result.get("headers"),
            "initialblockdownload": result.get("initialblockdownload"),
        }
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
        return {"reachable": False, "error": str(exc)}

