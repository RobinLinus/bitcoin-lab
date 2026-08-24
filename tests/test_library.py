import tempfile
import unittest
from pathlib import Path

from lab.library import SearchIndex, load_documents, validate_manifests


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "library"


class LibraryTests(unittest.TestCase):
    def test_sample_library_has_all_collections(self):
        documents = load_documents(LIBRARY)
        expected = {
            "papers", "delving-bitcoin", "mailing-lists", "robinlinus", "fairgate",
            "alpen", "babylon", "bitcoin-scripts", "bitvm-opcodes",
            "robinlinus-gists", "citrea-docs",
        }
        self.assertTrue(expected.issubset({document.metadata["collection"] for document in documents}))
        self.assertGreaterEqual(len(documents), 54)
        self.assertGreaterEqual(len(validate_manifests(LIBRARY)), 11)

    def test_full_text_and_metadata_search(self):
        with tempfile.TemporaryDirectory() as directory:
            index = SearchIndex(Path(directory) / "test.db")
            self.assertGreaterEqual(index.rebuild(LIBRARY), 54)
            full_text = index.search("package relay fee bumping")
            self.assertEqual("delving-package-relay-fixture", full_text[0]["id"])
            metadata = index.search(collection="mailing-lists", tag="rbf")
            self.assertEqual(["mailing-list-pinning-fixture"], [item["id"] for item in metadata])

            for collection in ("bitcoin-scripts", "bitvm-opcodes", "robinlinus-gists", "citrea-docs"):
                self.assertTrue(index.search(collection=collection), collection)


if __name__ == "__main__":
    unittest.main()
