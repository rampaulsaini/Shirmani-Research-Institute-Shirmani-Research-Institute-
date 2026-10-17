import json
import tempfile
import unittest
from pathlib import Path

from scripts.ensure_product_catalog import ensure_catalog


class EnsureProductCatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.catalog = self.root / "generated" / "1000-digital-products.json"
        self.registry = self.root / "generated" / "production-registry.json"
        self.catalog.parent.mkdir(parents=True)
        self.rows = [{"id": "SP-0001", "name": "Starter"}, {"id": "SP-0002", "name": "Calculator"}]

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def test_empty_catalog_recovers_from_valid_registry(self):
        self.catalog.write_text("", encoding="utf-8")
        self.write_json(self.registry, {"schema_version": 2, "product_count": 2, "products": self.rows})

        result = ensure_catalog(self.catalog, self.registry)

        self.assertEqual(result, {"action": "restored-from-registry", "product_count": 2})
        recovered = json.loads(self.catalog.read_text(encoding="utf-8"))
        self.assertEqual(recovered["schema_version"], 2)
        self.assertEqual(recovered["products"], self.rows)

    def test_valid_catalog_is_preserved_byte_for_byte(self):
        original = '{ "schema_version": 2, "products": [{"id":"KEEP-1","name":"Keep"}] }\n'
        self.catalog.write_text(original, encoding="utf-8")
        self.write_json(self.registry, {"products": self.rows})

        result = ensure_catalog(self.catalog, self.registry)

        self.assertEqual(result, {"action": "kept-existing", "product_count": 1})
        self.assertEqual(self.catalog.read_text(encoding="utf-8"), original)

    def test_missing_or_empty_registry_fails_closed(self):
        self.catalog.write_text("", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "refusing to produce"):
            ensure_catalog(self.catalog, self.registry)
        self.write_json(self.registry, {"products": []})
        with self.assertRaisesRegex(ValueError, "refusing to produce"):
            ensure_catalog(self.catalog, self.registry)
        self.assertEqual(self.catalog.read_text(encoding="utf-8"), "")

    def test_duplicate_or_missing_ids_fail_closed(self):
        for bad_rows in (
            [{"id": "DUP"}, {"id": "DUP"}],
            [{"id": "OK"}, {"name": "missing ID"}],
            [{"id": "OK"}, None],
        ):
            with self.subTest(bad_rows=bad_rows):
                self.catalog.write_text("", encoding="utf-8")
                self.write_json(self.registry, {"products": bad_rows})
                with self.assertRaises(ValueError):
                    ensure_catalog(self.catalog, self.registry)
                self.assertEqual(self.catalog.read_text(encoding="utf-8"), "")

    def test_invalid_catalog_recovers_but_nonempty_invalid_rows_fail_closed(self):
        self.catalog.write_text("{invalid json", encoding="utf-8")
        self.write_json(self.registry, {"products": self.rows})
        result = ensure_catalog(self.catalog, self.registry)
        self.assertEqual(result["action"], "restored-from-registry")

        self.write_json(self.catalog, {"products": [{"name": "no ID"}]})
        before = self.catalog.read_text(encoding="utf-8")
        with self.assertRaises(ValueError):
            ensure_catalog(self.catalog, self.registry)
        self.assertEqual(self.catalog.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
