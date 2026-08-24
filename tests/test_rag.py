import tempfile
import unittest
from pathlib import Path

from lab.library import SearchIndex
from lab.rag import answer


ROOT = Path(__file__).resolve().parents[1]


class RagTests(unittest.TestCase):
    def test_retrieval_answer_is_grounded_without_a_model(self):
        with tempfile.TemporaryDirectory() as directory:
            index = SearchIndex(Path(directory) / "test.db")
            index.rebuild(ROOT / "library")
            result = answer("How does package relay help fee bumping?", index, top_k=2)
            self.assertTrue(result["grounded"])
            self.assertEqual("local-extractive", result["mode"])
            self.assertIsNone(result["model"])
            self.assertEqual("delving-package-relay-fixture", result["citations"][0]["id"])


if __name__ == "__main__":
    unittest.main()

