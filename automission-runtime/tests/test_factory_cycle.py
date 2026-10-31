import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from product_catalog import ProductCatalog
from factory_cycle import run_factory_cycle, load_requests

class FactoryCycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "factory.db"
        self.catalog = ProductCatalog(self.db)

    def tearDown(self):
        self.tmp.cleanup()

    def test_cycle_creates_blueprint_without_publishing(self):
        result = run_factory_cycle(self.catalog, [{
            "title": "Yatharth Website Kit",
            "product_type": "website",
            "description": "Reusable website package",
            "languages": ["en", "hi"],
            "files": ["README.md", "template.zip"],
        }])
        self.assertEqual(result[0]["status"], "BLUEPRINT_READY")
        self.assertEqual(self.catalog.get(result[0]["product_id"])["stage"], "IDEA")

    def test_invalid_request_is_rejected(self):
        result = run_factory_cycle(self.catalog, [{"product_type": "book"}])
        self.assertEqual(result[0]["status"], "REJECTED")

    def test_request_file_must_be_list(self):
        path = Path(self.tmp.name) / "requests.json"
        path.write_text('{"title":"bad"}')
        with self.assertRaises(ValueError):
            load_requests(path)

if __name__ == "__main__":
    unittest.main()
