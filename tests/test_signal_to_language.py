import unittest
from factory.signal_to_language import SignalObservation, translate_signal, translate_batch

class SignalToLanguageTests(unittest.TestCase):
    def test_observation_is_translated_without_claiming_subjective_feeling(self):
        result = translate_signal(SignalObservation("plant-1","plant","moisture",0.9,"ratio","sensor-A"))
        self.assertIn("moisture/water level is high", result.statement)
        self.assertEqual(result.epistemic_status, "OBSERVED_SIGNAL")

    def test_model_support_is_explicit(self):
        result = translate_signal(SignalObservation("tree-1","plant","stress",0.8,source="sensor-A"), 0.91)
        self.assertEqual(result.epistemic_status, "OBSERVED_SIGNAL_WITH_MODEL_SUPPORT")
        self.assertGreater(result.confidence, 0.7)

    def test_missing_source_does_not_disappear(self):
        result = translate_signal(SignalObservation("x","entity","activity",0.5))
        self.assertEqual(result.epistemic_status, "OBSERVED_SIGNAL_WITHOUT_SOURCE")

    def test_batch_is_deterministic(self):
        rows=[{"entity_id":"a","entity_type":"plant","signal":"light","value":0.2,"source":"s"}]
        self.assertEqual(translate_batch(rows), translate_batch(rows))

if __name__ == "__main__":
    unittest.main()
