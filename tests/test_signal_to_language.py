import unittest
from factory.signal_to_language import SignalObservation, standardized_deviation, summarize_signal
class SignalToLanguageTests(unittest.TestCase):
    def test_baseline_is_zero(self): self.assertEqual(standardized_deviation(10,10,2),0.0)
    def test_nonfinite_input_is_rejected(self):
        with self.assertRaises(ValueError): standardized_deviation(float("nan"),10,2)
    def test_translation_is_evidence_first(self):
        result=summarize_signal([SignalObservation("plant-electric","amplitude",14,10,"mV")])
        self.assertIn("Measured data",result.observation); self.assertEqual(result.status,"MODEL_INFERENCE_NOT_PROOF"); self.assertGreater(result.confidence,0); self.assertTrue(any("plant-electric" in x for x in result.evidence)); self.assertTrue(any("not proof" in x.lower() for x in result.limitations))
    def test_empty_input_fails_closed(self):
        result=summarize_signal([]); self.assertEqual(result.possible_state,"INSUFFICIENT_DATA"); self.assertEqual(result.confidence,0.0)
if __name__=="__main__": unittest.main()
