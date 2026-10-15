#!/usr/bin/env python3
"""Regression tests for old product-media manifests missing optional fields."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "scripts" / "product_media_factory.py"
SPEC = importlib.util.spec_from_file_location("product_media_factory", MODULE)
FACTORY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FACTORY)


class LegacyMediaManifestTests(unittest.TestCase):
    def test_missing_vip_screenshot_is_migrated(self):
        rows = FACTORY.normalize_manifest_rows({
            "products": [{"product_id": "SP-0001", "video_asset": "products/demos/sp-0001.mp4"}]
        })
        self.assertEqual(rows["SP-0001"]["vip_screenshot"], "products/vip-screenshots/sp-0001.png")

    def test_legacy_id_alias_is_supported(self):
        rows = FACTORY.normalize_manifest_rows({"products": [{"id": "SP-0002"}]})
        self.assertEqual(rows["SP-0002"]["product_id"], "SP-0002")
        self.assertEqual(rows["SP-0002"]["video_asset"], "products/demos/sp-0002.mp4")

    def test_unidentifiable_or_malformed_rows_are_skipped(self):
        rows = FACTORY.normalize_manifest_rows({
            "products": [None, {"video_asset": "orphan.mp4"}, {"id": "SP-0003"}]
        })
        self.assertEqual(list(rows), ["SP-0003"])

    def test_non_list_products_is_safe(self):
        self.assertEqual(FACTORY.normalize_manifest_rows({"products": None}), {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
