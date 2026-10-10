"""Regression tests for the product-specific VIP visual factory (stdlib only)."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = spec_from_file_location("vip_screenshot_factory", ROOT / "factory" / "vip_screenshot_factory.py")
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VipScreenshotFactoryTests(unittest.TestCase):
    def test_visual_has_4k_16_9_canvas_and_unique_product_identity(self):
        svg = MODULE.make_svg({
            "id": "SRI-TEST-4K",
            "name": "Test Product",
            "category": "Research",
            "engine": "browser",
            "short_description": "A focused demo product.",
            "price_inr": 499,
        })
        self.assertIn('width="3840" height="2160"', svg)
        self.assertIn('viewBox="0 0 2560 1440"', svg)
        self.assertIn("SRI-TEST-4K", svg)
        self.assertIn("Test Product", svg)
        self.assertIn("A focused demo product.", svg)
        self.assertIn("Shiromani Rampal Saini", svg)
        self.assertIn("product-passport.html?id=SRI-TEST-4K", svg)
        self.assertIn("product-demo.html?id=SRI-TEST-4K", svg)

    def test_untrusted_product_text_is_html_escaped(self):
        svg = MODULE.make_svg({
            "id": "SRI-ESCAPE",
            "name": "<script>alert(1)</script>",
            "short_description": "Safe & clear",
        })
        self.assertNotIn("<script>alert(1)</script>", svg)
        self.assertIn("&lt;script&gt;", svg)
        self.assertIn("Safe &amp; clear", svg)


if __name__ == "__main__":
    unittest.main()
