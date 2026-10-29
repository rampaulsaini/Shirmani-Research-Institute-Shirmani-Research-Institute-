import unittest

from factory.public_production_materializer import readable_excerpt, title


class PublicProductionTemplateSourceTests(unittest.TestCase):
    def test_python_source_with_embedded_html_template_is_not_parsed_as_rendered_html(self):
        source = '''PAGE = f"""<!doctype html><html><head><title>{name} — SHIRMANI Production</title></head><body>{name}</body></html>"""'''
        self.assertEqual(title(source, "factory/example.py"), "factory/example.py")
        self.assertTrue(readable_excerpt(source).startswith("PAGE = f"))

    def test_actual_html_document_still_uses_its_title_and_readable_text(self):
        source = "<!doctype html><html><head><title>Actual Product</title></head><body><h1>Working demo</h1></body></html>"
        self.assertEqual(title(source, "fallback"), "Actual Product")
        excerpt = readable_excerpt(source)
        self.assertIn("Actual Product", excerpt)
        self.assertIn("Working demo", excerpt)


if __name__ == "__main__":
    unittest.main()
