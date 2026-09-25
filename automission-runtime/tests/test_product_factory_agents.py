import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from product_catalog import ProductCatalog
from product_agents import build_product_spec, validate_agent_plan
from product_packaging import build_manifest
from product_factory import DigitalProductFactory

class ProductFactoryAgentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "factory.db"
        self.catalog = ProductCatalog(self.db)
        self.factory = DigitalProductFactory(self.catalog)

    def tearDown(self):
        self.tmp.cleanup()

    def test_blueprint_is_deterministic_and_has_agent_plan(self):
        product_id, spec = self.factory.create_blueprint(
            "Yatharth AI Toolkit", "ai_tool",
            "A digital AI toolkit", ["en", "hi"]
        )
        self.assertTrue(product_id)
        self.assertIn("software", spec["agents"])
        self.assertTrue(spec["spec_hash"])
        validate_agent_plan(spec)

    def test_packaging_manifest_is_hashed(self):
        spec = build_product_spec("Book", "book", "Digital book")
        manifest = build_manifest(
            {**spec, "version": "1.0.0"},
            ["cover.png", "book.pdf"],
        )
        self.assertEqual(manifest["files"], ["book.pdf", "cover.png"])
        self.assertTrue(manifest["manifest_hash"])

    def test_invalid_agent_plan_rejected(self):
        with self.assertRaises(ValueError):
            validate_agent_plan({"agents": ["unknown-agent"]})

if __name__ == "__main__":
    unittest.main()
