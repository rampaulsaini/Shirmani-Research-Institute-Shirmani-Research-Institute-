#!/usr/bin/env python3
"""Regression tests for the public production status contract."""
import json
import tempfile
import unittest
from pathlib import Path

from factory.public_production_materializer import materialize_concrete_asset_status


class ConcreteAssetStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "generated").mkdir()
        (self.root / "products" / "production").mkdir(parents=True)
        (self.root / "products" / "production" / "a.html").write_text("A", encoding="utf-8")
        (self.root / "products" / "production" / "b.html").write_text("B", encoding="utf-8")
        catalog = {
            "product_count": 2,
            "products": [
                {"id": "a", "asset": "products/production/a.html"},
                {"id": "b", "asset": "products/production/b.html"},
            ],
        }
        (self.root / "generated" / "1000-digital-products.json").write_text(
            json.dumps(catalog), encoding="utf-8"
        )
        # Reproduce the legacy persisted status that caused the production gate to fail.
        (self.root / "generated" / "concrete-product-asset-status.json").write_text(
            json.dumps({"product_assets": 2, "dispatch": "NO"}), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_refreshes_timestamp_and_counts_real_assets(self):
        timestamp = "2026-10-16T00:00:00+00:00"
        status = materialize_concrete_asset_status(self.root, generated_at=timestamp)
        self.assertEqual(status["generated_at"], timestamp)
        self.assertEqual(status["product_assets"], 2)
        self.assertEqual(status["concrete_product_assets"], 2)
        self.assertEqual(status["catalog_products"], 2)
        self.assertEqual(status["materialization_percent"], 100.0)
        self.assertEqual(status["state"], "READY_FOR_QC")
        self.assertEqual(status["dispatch"], "NO")

    def test_missing_asset_is_not_counted_as_produced(self):
        (self.root / "products" / "production" / "b.html").unlink()
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["product_assets"], 1)
        self.assertEqual(status["materialization_percent"], 50.0)
        self.assertEqual(status["state"], "IN_PROGRESS")

    def test_path_traversal_asset_is_not_counted(self):
        catalog_path = self.root / "generated" / "1000-digital-products.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["products"][0]["asset"] = "../outside.html"
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        status = materialize_concrete_asset_status(self.root, generated_at="2026-10-16T00:00:00+00:00")
        self.assertEqual(status["product_assets"], 1)


if __name__ == "__main__":
    unittest.main()
