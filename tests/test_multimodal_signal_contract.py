import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class MultimodalSignalContractTests(unittest.TestCase):
    def test_schema_is_valid_json(self):
        p = ROOT / "schemas" / "multimodal-signal-interpretation.schema.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        self.assertEqual(data["properties"]["schema_version"]["const"], "1.0")
        self.assertIn("signals", data["required"])

    def test_contract_separates_observation_from_interpretation(self):
        text = (ROOT / "docs" / "supreme-multimodal-signal-to-language-contract-2026-10-01.md").read_text(encoding="utf-8")
        self.assertIn("Signal ≠ भावना ≠ चेतना ≠ सत्यापित निष्कर्ष", text)
        self.assertIn("measured signal", text)
        self.assertIn("model inference", text)
        self.assertIn("verification status", text)

if __name__ == "__main__":
    unittest.main()
