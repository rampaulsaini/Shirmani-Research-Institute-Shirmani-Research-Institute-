import json
import tempfile
import unittest
from pathlib import Path

from scripts.production_first_cycle import write_if_changed


class ProductionOperationsNoOpTests(unittest.TestCase):
    def test_identical_semantic_payload_preserves_file_and_timestamp(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            original = {"generated_at": "2026-10-01T00:00:00Z", "count": 3, "rows": [{"id": "p1"}]}
            path.write_text(json.dumps(original) + "\n", encoding="utf-8")
            before = path.read_bytes()

            changed = write_if_changed(path, {
                "generated_at": "2026-10-17T00:00:00Z",
                "count": 3,
                "rows": [{"id": "p1"}],
            })

            self.assertFalse(changed)
            self.assertEqual(path.read_bytes(), before)

    def test_semantic_change_updates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            path.write_text(json.dumps({"generated_at": "old", "count": 3}) + "\n", encoding="utf-8")

            changed = write_if_changed(path, {"generated_at": "new", "count": 4})

            self.assertTrue(changed)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["count"], 4)

    def test_missing_file_is_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "status.json"

            changed = write_if_changed(path, {"generated_at": "now", "count": 1})

            self.assertTrue(changed)
            self.assertTrue(path.is_file())


if __name__ == "__main__":
    unittest.main()
