import json
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "unique-tool-automission.yml"


def validation_script():
    workflow = WORKFLOW.read_text(encoding="utf-8")
    match = re.search(r"(?ms)^        run: \|\n(?P<block>.*?^          PY\s*$)", workflow)
    if not match:
        raise AssertionError("Could not locate the unique-tool validation run block")
    lines = textwrap.dedent(match.group("block")).splitlines()
    if len(lines) < 3 or lines[0] != "python - <<'PY'" or lines[-1] != "PY":
        raise AssertionError("Unexpected unique-tool validation script wrapper")
    return "\n".join(lines[1:-1]) + "\n"


class UniqueToolManifestNoopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        (self.project / "factory").mkdir()
        (self.project / "tools").mkdir()
        self.catalog_path = self.project / "factory" / "unique-tool-catalog.json"
        self.tool_path = self.project / "tools" / "demo.html"
        self.manifest_path = self.project / "generated" / "unique-tool-production-manifest.json"
        self.catalog_path.write_text(
            json.dumps({"tools": [{"id": "SRI-TEST-001", "name": "Test tool", "path": "tools/demo.html"}]}),
            encoding="utf-8",
        )
        self.tool_path.write_text("<!doctype html>\n" + ("<!-- test asset -->\n" * 40), encoding="utf-8")
        self.script = validation_script()

    def run_validation(self):
        return subprocess.run(
            [sys.executable, "-c", self.script],
            cwd=self.project,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_unchanged_inventory_preserves_manifest_byte_for_byte(self):
        first = self.run_validation()
        self.assertEqual(first.returncode, 0, first.stderr)
        original = self.manifest_path.read_bytes()

        second = self.run_validation()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("avoiding timestamp-only publication", second.stdout)
        self.assertEqual(self.manifest_path.read_bytes(), original)

    def test_changed_tool_hash_refreshes_manifest(self):
        first = self.run_validation()
        self.assertEqual(first.returncode, 0, first.stderr)
        original = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self.tool_path.write_text("<!doctype html>\n" + ("<!-- changed asset -->\n" * 40), encoding="utf-8")

        changed = self.run_validation()
        self.assertEqual(changed.returncode, 0, changed.stderr)
        updated = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self.assertNotEqual(updated["tools"][0]["sha256"], original["tools"][0]["sha256"])
        self.assertNotIn("avoiding timestamp-only publication", changed.stdout)

    def test_empty_catalog_fails_closed_and_preserves_existing_manifest(self):
        first = self.run_validation()
        self.assertEqual(first.returncode, 0, first.stderr)
        original = self.manifest_path.read_bytes()
        self.catalog_path.write_text(json.dumps({"tools": []}), encoding="utf-8")

        failed = self.run_validation()
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("catalog is empty", failed.stderr + failed.stdout)
        self.assertEqual(self.manifest_path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
