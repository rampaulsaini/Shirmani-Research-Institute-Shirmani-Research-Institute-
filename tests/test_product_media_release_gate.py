#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "factory" / "product_media_release_gate.py"
SPEC = importlib.util.spec_from_file_location("product_media_release_gate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProductMediaReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "assets").mkdir()
        (self.root / "docs").mkdir()
        # Minimal recognizable file signatures are sufficient for deterministic gate tests.
        (self.root / "assets" / "shot.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"test")
        (self.root / "assets" / "demo.mp4").write_bytes(b"\x00\x00\x00\x18ftypmp42" + b"test")
        (self.root / "docs" / "guide.md").write_text("How to use this product.\n", encoding="utf-8")
        self.product = {
            "product_id": "SRI-ABC-001",
            "version": "1.0.0",
            "short_description": "A product-specific plain-language demo.",
            "passport_url": "https://example.org/passports/SRI-ABC-001",
            "qr_target_url": "https://example.org/passports/SRI-ABC-001",
            "screenshot_path": "assets/shot.png",
            "screenshot_kind": "REAL_BROWSER_SCREENSHOT",
            "demo_video_path": "assets/demo.mp4",
            "demo_status": "RECORDED",
            "usage_guide_path": "docs/guide.md",
            "qr_scan_test": "PASS",
            "photo_asset_status": "VERIFIED",
        }

    def tearDown(self):
        self.temp.cleanup()

    def validate(self, products=None):
        return MODULE.validate_manifest({"products": products or [self.product]}, self.root)

    def test_complete_product_passes_contract(self):
        result = self.validate()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["passed_count"], 1)

    def test_missing_demo_is_blocked(self):
        product = dict(self.product, demo_status="STORYBOARD — NOT RECORDED")
        result = self.validate([product])
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any("not recorded" in e for e in result["errors"]))

    def test_mockup_cannot_pass_as_real_screenshot(self):
        product = dict(self.product, screenshot_kind="ILLUSTRATIVE MOCK-UP")
        self.assertEqual(self.validate([product])["status"], "BLOCKED")

    def test_wrong_qr_destination_is_blocked(self):
        product = dict(self.product, qr_target_url="https://example.org/other")
        self.assertEqual(self.validate([product])["status"], "BLOCKED")

    def test_shared_qr_destination_is_blocked(self):
        second = dict(self.product, product_id="SRI-ABC-002")
        self.assertEqual(self.validate([self.product, second])["status"], "BLOCKED")

    def test_missing_photo_authorization_is_blocked(self):
        product = dict(self.product, photo_asset_status="NOT_VERIFIED")
        self.assertEqual(self.validate([product])["status"], "BLOCKED")

    def test_duplicate_id_and_version_is_blocked(self):
        self.assertEqual(self.validate([self.product, dict(self.product)])["status"], "BLOCKED")

    def test_bad_video_signature_is_blocked(self):
        (self.root / "assets" / "demo.mp4").write_bytes(b"not a video")
        self.assertEqual(self.validate()["status"], "BLOCKED")

    def test_empty_manifest_is_blocked(self):
        result = MODULE.validate_manifest({"products": []}, self.root)
        self.assertEqual(result["status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
