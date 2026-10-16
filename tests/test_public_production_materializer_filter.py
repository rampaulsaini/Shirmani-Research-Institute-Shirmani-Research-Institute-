import tempfile
import unittest
from pathlib import Path

from factory.public_production_materializer import load_source


class LoadSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_reads_non_empty_repository_source(self):
        (self.root / "module.py").write_text("print('useful')\n", encoding="utf-8")
        source, reason = load_source("module.py", self.root)
        self.assertEqual(source, "print('useful')\n")
        self.assertIsNone(reason)

    def test_skips_missing_source(self):
        source, reason = load_source("missing.py", self.root)
        self.assertIsNone(source)
        self.assertEqual(reason, "missing_source")

    def test_skips_empty_source(self):
        (self.root / "empty.py").write_text("  \n", encoding="utf-8")
        source, reason = load_source("empty.py", self.root)
        self.assertIsNone(source)
        self.assertEqual(reason, "empty_source")

    def test_rejects_path_traversal_outside_repository(self):
        outside = self.root.parent / "outside.py"
        source, reason = load_source("../outside.py", self.root)
        self.assertIsNone(source)
        self.assertEqual(reason, "outside_repository")

    def test_rejects_empty_or_invalid_module_path(self):
        for module in ("", None, 12):
            source, reason = load_source(module, self.root)
            self.assertIsNone(source)
            self.assertEqual(reason, "invalid_module_path")


if __name__ == "__main__":
    unittest.main()
