import json
import tempfile
import unittest
from pathlib import Path
from factory.supreme_nlp_signal_contract import NLPInterpretation, SignalObservation, observation_to_language, write_contract_report

class SupremeNLPSignalContractTests(unittest.TestCase):
    def test_signal_translation_is_deterministic_and_conservative(self):
        obs = SignalObservation(source="plant-signal", features={"electrical_signal": 0.8, "vibration": 0.2})
        result = observation_to_language(obs, "obs-0001", baseline={"electrical_signal": 0.5, "vibration": 0.2})
        self.assertIn("electrical_signal increased", result.plain_language)
        self.assertEqual(result.experience_claim, "not_established")
        self.assertGreaterEqual(result.confidence, 0.5)
        self.assertLessEqual(result.confidence, 1.0)

    def test_non_finite_signal_is_rejected(self):
        with self.assertRaises(ValueError):
            SignalObservation(source="sensor", features={"x": float("nan")}).validate()

    def test_invalid_confidence_is_rejected(self):
        with self.assertRaises(ValueError):
            NLPInterpretation("x", "x", (), 1.1, "x").validate()

    def test_machine_readable_report_is_written(self):
        obs = SignalObservation(source="sensor", features={"x": 1.0})
        with tempfile.TemporaryDirectory() as directory:
            target = str(Path(directory) / "report.json")
            report = write_contract_report([obs], target)
            loaded = json.loads(Path(target).read_text(encoding="utf-8"))
            self.assertTrue(report["fail_closed"])
            self.assertTrue(loaded["measured_signals_are_not_subjective-experience_proof"])
            self.assertEqual(len(loaded["observations"]), 1)

if __name__ == "__main__":
    unittest.main()
