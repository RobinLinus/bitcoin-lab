"""Required subprocess adapter for the pinned rust-bitcoinkernel backend."""

from __future__ import annotations

import json
import os
import subprocess
from typing import Any, Dict


EXPECTED_BACKEND = "rust-bitcoinkernel"
EXPECTED_REVISION = "691a90cc0c20761cc9b35a783e0e84c77245d555"


def evaluate_script(unlocking_script: str, locking_script: str) -> Dict[str, Any]:
    binary = os.environ.get("LAB_SCRIPT_BINARY", "/usr/local/bin/bitcoin-script-kernel")
    payload = json.dumps({"unlocking_script": unlocking_script, "locking_script": locking_script})
    try:
        process = subprocess.run(
            [binary],
            input=payload,
            text=True,
            capture_output=True,
            timeout=15,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError("required rust-bitcoinkernel backend failed to start: {}".format(exc)) from exc
    if process.returncode != 0:
        raise RuntimeError(
            "required rust-bitcoinkernel backend exited {}: {}".format(
                process.returncode, process.stderr.strip()
            )
        )
    try:
        result = json.loads(process.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("required rust-bitcoinkernel backend returned invalid JSON") from exc
    if not isinstance(result, dict) or result.get("backend") != EXPECTED_BACKEND:
        raise RuntimeError("Script response did not come from rust-bitcoinkernel")
    if result.get("backend_revision") != EXPECTED_REVISION:
        raise RuntimeError("rust-bitcoinkernel backend revision mismatch")
    return result
