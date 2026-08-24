import os
import unittest
from unittest.mock import patch

from lab.interpreter import evaluate_script


class ScriptAdapterTests(unittest.TestCase):
    def test_missing_rust_backend_fails_without_python_fallback(self):
        environment = dict(os.environ)
        environment["LAB_SCRIPT_BINARY"] = "/definitely/missing/bitcoin-script-kernel"
        with patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(RuntimeError, "required rust-bitcoinkernel backend"):
                evaluate_script("2 3 OP_ADD", "5 OP_EQUAL")


if __name__ == "__main__":
    unittest.main()
