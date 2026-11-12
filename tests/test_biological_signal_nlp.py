import unittest

from factory.biological_signal_nlp import (
    SignalObservation,
    interpret_batch,
    interpret_signal,
)


class BiologicalSignalNLPTests(unittest.TestCase):
    def test_plant_signal_is_not_mislabeled_as_feeling(self):
        result = interpret_signal(SignalObservation(
            subject_type="plant",
            signal="moisture",
            value=20,
            unit="%",
            baseline=40,
            source="sensor-1",
        ))
        self.assertEqual(result.state, "HYDRATION_STRESS_ASSOCIATED")
        self.assertFalse(result.subjective_feeling_claim)
        self.assertIn("does not prove a feeling", result.simple_language)

    def test_nonliving_object_reports_physical_change(self):
        result = interpret_signal(SignalObservation(
            subject_type="nonliving",
            signal="temperature",
            value=60,
            unit="C",
            baseline=30,
            source="sensor-2",
        ))
        self.assertEqual(result.state, "PHYSICAL_CHANGE")
        self.assertFalse(result.subjective_feeling_claim)

    def test_missing_context_stays_conservative(self):
        result = interpret_signal(SignalObservation(
            subject_type="plant",
            signal="electrical_potential",
            value=2.0,
            unit="mV",
        ))
        self.assertEqual(result.state, "PHYSIOLOGICAL_OR_BEHAVIORAL_SIGNAL")
        self.assertLess(result.confidence, 0.95)

    def test_batch_contract_never_claims_subjective_feelings(self):
        result = interpret_batch([
            SignalObservation("plant", "growth_rate", 12, "mm/day", 8, source="study"),
            SignalObservation("nonliving", "temperature", 40, "C", 20, source="sensor"),
        ])
        self.assertFalse(result["truth_claim"])
        self.assertEqual(result["subjective_feeling_claims"], 0)


if __name__ == "__main__":
    unittest.main()
