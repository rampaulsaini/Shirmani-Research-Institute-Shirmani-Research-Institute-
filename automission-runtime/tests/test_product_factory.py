import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from product_catalog import ProductCatalog
from product_pipeline import (run_quality_gate, prepare_for_publishing,
                               request_publish_approval, publish_after_approval)

class ProductFactoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "products.db"
        self.catalog = ProductCatalog(self.db)
        self.product = self.catalog.create(
            "Yatharth AI Toolkit", "ai_tool", "Digital AI toolkit",
            payload={"origin": "automission"}
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_lifecycle_requires_quality_and_approval(self):
        with self.assertRaises(ValueError):
            prepare_for_publishing(self.catalog, self.product, 10, "USD")
        run_quality_gate(self.catalog, self.product, 92, "https://evidence.example/qc")
        prepare_for_publishing(self.catalog, self.product, 10, "USD")
        request_publish_approval(self.catalog, self.product)
        self.assertEqual(self.catalog.get(self.product)["stage"], "PUBLISH_APPROVAL_REQUIRED")
        publish_after_approval(self.catalog, self.product)
        self.assertEqual(self.catalog.get(self.product)["stage"], "PUBLISHED")

    def test_publish_cannot_bypass_approval(self):
        run_quality_gate(self.catalog, self.product, 90)
        prepare_for_publishing(self.catalog, self.product, 10, "USD")
        with self.assertRaises(PermissionError):
            self.catalog.transition(self.product, "PUBLISHED")

    def test_sales_require_real_evidence(self):
        run_quality_gate(self.catalog, self.product, 90)
        prepare_for_publishing(self.catalog, self.product, 10, "USD")
        request_publish_approval(self.catalog, self.product)
        publish_after_approval(self.catalog, self.product)
        with self.assertRaises(ValueError):
            self.catalog.record_sale(self.product, 10, "USD", "", "own_store")
        self.catalog.record_sale(self.product, 10, "USD",
                                 "https://evidence.example/order/1", "own_store")
        self.assertEqual(self.catalog.get(self.product)["stage"], "VERIFIED_SALE")
        self.assertEqual(len(self.catalog.verified_sales()), 1)

    def test_invalid_quality_is_rejected(self):
        with self.assertRaises(ValueError):
            self.catalog.set_quality(self.product, 79)

if __name__ == "__main__":
    unittest.main()
