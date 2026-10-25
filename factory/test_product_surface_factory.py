import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

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
        self.assertNotIn('href="../../demos/vip/sp-0001.svg"', rendered)
        self.assertNotIn('href="../../demos/calculator.mp4"', rendered)

    def test_existing_media_links_are_root_relative_from_nested_page(self):
        (self.root / "products/demos/vip").mkdir(parents=True)
        (self.root / "products/demos").mkdir(parents=True, exist_ok=True)
        (self.root / "products/demos/vip/sp-0001.svg").write_text("<svg/>", encoding="utf-8")
        (self.root / "products/demos/calculator.mp4").write_bytes(b"demo")
        rendered = factory.page(self.product, root=self.root)
        self.assertIn('href="../../demos/vip/sp-0001.svg"', rendered)
        self.assertIn('href="../../demos/calculator.mp4"', rendered)
        self.assertNotIn("Demo media is not published", rendered)

    def test_every_emitted_local_href_resolves_from_actual_nested_page(self):
        (self.root / "showroom-public.html").write_text("<html/>", encoding="utf-8")
        (self.root / "product-passport.html").write_text("<html/>", encoding="utf-8")
        (self.root / "products/demos").mkdir(parents=True, exist_ok=True)
        (self.root / "products/demos/calculator.mp4").write_bytes(b"demo")
        rendered = factory.page(self.product, root=self.root)
        page_path = self.root / "products/live/sp-0001/index.html"
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(rendered, encoding="utf-8")

        class Hrefs(HTMLParser):
            def __init__(self):
                super().__init__()
                self.values = []

            def handle_starttag(self, tag, attrs):
                self.values.extend(value for key, value in attrs if key.lower() == "href" and value)

        parser = Hrefs()
        parser.feed(rendered)
        for href in parser.values:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (page_path.parent / unquote(parsed.path)).resolve()
            with self.subTest(href=href):
                target.relative_to(self.root.resolve())
                self.assertTrue(target.exists(), f"{href} resolves to missing target {target}")


if __name__ == "__main__":
    unittest.main()
