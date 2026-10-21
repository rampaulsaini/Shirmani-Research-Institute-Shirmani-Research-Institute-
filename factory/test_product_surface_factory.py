import tempfile
import unittest
from pathlib import Path

from factory import product_surface_factory as factory


class ProductSurfaceFactoryTests(unittest.TestCase):
    def setUp(self):
        self.product = {
            "id": "SP-0001",
            "name": "Starter Math",
            "family": "Education",
            "engine": "calculator",
            "short_description": "A test listing",
            "offer_price_inr": 79,
        }
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_root_navigation_and_contact_ctas_use_correct_relative_depth(self):
        rendered = factory.page(self.product, root=self.root)
        self.assertIn('href="../../../product-passport.html?id=SP-0001"', rendered)
        self.assertIn('href="../../../showroom-public.html"', rendered)
        self.assertIn("wa.me/918082935186", rendered)
        self.assertIn("mailto:sainirampaul60@gmail.com", rendered)

    def test_missing_demo_is_not_misrepresented_as_runnable(self):
        rendered = factory.page(self.product, root=self.root)
        self.assertIn("Demo media is not published", rendered)
        self.assertIn("not proof of a runnable product demo", rendered)
        self.assertNotIn('href="../../../demos/vip/sp-0001.svg"', rendered)
        self.assertNotIn('href="../../../demos/products/sp-0001.mp4"', rendered)

    def test_existing_media_links_are_root_relative_from_nested_page(self):
        (self.root / "demos/vip").mkdir(parents=True)
        (self.root / "demos/products").mkdir(parents=True)
        (self.root / "demos/vip/sp-0001.svg").write_text("<svg/>", encoding="utf-8")
        (self.root / "demos/products/sp-0001.mp4").write_bytes(b"demo")
        rendered = factory.page(self.product, root=self.root)
        self.assertIn('href="../../../demos/vip/sp-0001.svg"', rendered)
        self.assertIn('href="../../../demos/products/sp-0001.mp4"', rendered)
        self.assertNotIn("Demo media is not published", rendered)


if __name__ == "__main__":
    unittest.main()
