import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_product_media", ROOT / "scripts" / "validate_product_media.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def record(pid="SRI-001", name="Sample", **overrides):
    data = {
        "product_id": pid, "name": name, "version": "0.1.0",
        "short_description": "Short description",
        "passport_url": "https://example.org/passport/" + pid,
        "qr_asset_path": "assets/qr/" + pid + ".png",
        "vip_screenshot_path": "assets/screenshots/" + pid + ".png",
        "demo_video_path": "assets/demos/" + pid + ".mp4",
        "usage_guide_url": "https://example.org/guide/" + pid,
        "original_logo_asset_path": "assets/identity/original-photo.png",
        "evidence_state": "SOURCE-BASED", "release_state": "TESTING"
    }
    data.update(overrides)
    return data


class ProductMediaGateTests(unittest.TestCase):
    def test_complete_testing_record_passes_structure(self):
        self.assertEqual(MODULE.validate([record()]), [])

    def test_duplicate_product_id_fails(self):
        errors = MODULE.validate([record(), record(name="Different")])
        self.assertTrue(any("duplicate product_id" in e for e in errors))

    def test_qr_reuse_fails(self):
        a, b = record(), record("SRI-002", "Other", qr_asset_path="assets/qr/SRI-001.png")
        self.assertTrue(any("QR asset reused" in e for e in MODULE.validate([a, b])))

    def test_demo_reuse_fails(self):
        a, b = record(), record("SRI-002", "Other", demo_video_path="assets/demos/SRI-001.mp4")
        self.assertTrue(any("demo video reused" in e for e in MODULE.validate([a, b])))

    def test_verified_record_with_missing_media_fails(self):
        item = record(release_state="VERIFIED", demo_video_path="")
        self.assertTrue(any("cannot be VERIFIED" in e for e in MODULE.validate([item])))

    def test_invalid_evidence_state_fails(self):
        self.assertTrue(any("invalid evidence_state" in e
                            for e in MODULE.validate([record(evidence_state="CERTAIN")])))

    def test_missing_required_field_fails(self):
        item = record()
        del item["short_description"]
        self.assertTrue(any("missing fields" in e for e in MODULE.validate([item])))


if __name__ == "__main__":
    unittest.main()
