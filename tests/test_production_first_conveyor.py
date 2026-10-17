import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "production_first_conveyor.py"


class ProductionFirstConveyorTests(unittest.TestCase):
    def test_bounded_queue_keeps_catalog_totals_and_writes_valid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts = root / "scripts"
            generated = root / "generated"
            scripts.mkdir()
            generated.mkdir()
            copied_script = scripts / "production_first_conveyor.py"
            shutil.copy2(SCRIPT, copied_script)
            products = [
                {"id": f"PRODUCT-{i:04d}", "name": f"Product {i}", "description": "Fixture"}
                for i in range(300)
            ]
            (generated / "1000-digital-products.json").write_text(
                json.dumps({"product_count": len(products), "products": products}),
                encoding="utf-8",
            )

            subprocess.run(
                [sys.executable, str(copied_script)],
                check=True,
                capture_output=True,
                text=True,
            )

            manifest = json.loads(
                (generated / "production-first-conveyor.json").read_text(encoding="utf-8")
            )
            state = json.loads(
                (generated / "production-first-state.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["catalog_identities"], 300)
            self.assertEqual(manifest["queue_limit"], 250)
            self.assertEqual(manifest["queue_records"], 250)
            self.assertTrue(manifest["queue_truncated"])
            self.assertEqual(len(manifest["queue"]), 250)
            self.assertEqual(manifest["records_with_production_gaps"], 300)
            self.assertEqual(state["catalog_identities"], 300)
            self.assertEqual(state["production_gap_records"], 300)


if __name__ == "__main__":
    unittest.main()
