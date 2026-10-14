#!/usr/bin/env python3
"""Unit tests for product-media manifest metadata integrity."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_product_media_manifest.py"
spec = importlib.util.spec_from_file_location("validate_product_media_manifest", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def product(product_id="SRI-001", suffix="001", status="DRAFT"):
    return {
        "product_id": product_id,
        "version": "1.0.0",
        "short_description": "A concise, accurate product summary.",
        "passport_url": f"https://example.org/passport/{suffix}",
        "qr_url": f"https://example.org/qr/{suffix}",
        "screenshot": f"https://example.org/screenshots/{suffix}.png",
        "demo_video": f"https://example.org/demos/{suffix}.mp4",
        "usage_guide": f"https://example.org/guides/{suffix}",
        "status": status,
    }


class ProductMediaManifestTests(unittest.TestCase):
    def test_valid_draft_manifest_passes(self):
        self.assertEqual(validator.validate_manifest({"release_status": "DRAFT", "products": [product()]}), [])

    def test_duplicate_product_id_is_rejected(self):
        errors = validator.validate_manifest({"products": [product(), product(suffix="002")]})
        self.assertTrue(any("duplicate product_id" in error for error in errors))

    def test_reused_qr_or_demo_is_rejected(self):
        first = product()
        second = product(product_id="SRI-002", suffix="002")
        second["qr_url"] = first["qr_url"]
        second["demo_video"] = first["demo_video"]
        errors = validator.validate_manifest({"products": [first, second]})
        self.assertTrue(any("reused qr_url" in error for error in errors))
        self.assertTrue(any("reused demo_video" in error for error in errors))

    def test_missing_asset_is_rejected(self):
        item = product()
        item["demo_video"] = ""
        errors = validator.validate_manifest({"products": [item]})
        self.assertTrue(any("demo_video is required" in error for error in errors))

    def test_placeholders_block_published_release(self):
        item = product(status="PUBLISHED")
        item["demo_video"] = "STORYBOARD — NOT RECORDED"
        errors = validator.validate_manifest({"release_status": "PUBLISHED", "products": [item]})
        self.assertTrue(any("placeholder and cannot be published" in error for error in errors))

    def test_unverified_product_blocks_published_release(self):
        errors = validator.validate_manifest({"release_status": "PUBLISHED", "products": [product(status="DRAFT")]})
        self.assertTrue(any("status must be VERIFIED or PUBLISHED" in error for error in errors))

    def test_non_object_and_missing_products_are_rejected(self):
        self.assertTrue(validator.validate_manifest([]))
        self.assertTrue(validator.validate_manifest({}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
