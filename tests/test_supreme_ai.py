import unittest
from agents.supreme_nlp import summarize
from agents.ultra_automission import build_plan

class SupremeAITests(unittest.TestCase):
    def test_empty_input_fails_closed(self):
        r=summarize([])
        self.assertEqual(r["status"],"no_observable_signal")
        self.assertIsNone(r["interpretation"])

    def test_confidence_is_bounded(self):
        r=summarize([
            {"modality":"electrical","feature":"x","value":1.0,"quality":0.9,"source":"a"},
            {"modality":"vibration","feature":"x","value":0.8,"quality":0.9,"source":"b"}
        ])
        self.assertGreaterEqual(r["interpretation"]["confidence"],0)
        self.assertLessEqual(r["interpretation"]["confidence"],1)

    def test_automission_never_promotes_verification(self):
        p=build_plan()
        self.assertEqual(p["governance"]["verification_promotion"],"independent_verification_required")
        self.assertFalse(p["governance"]["scheduled_source_mutation"])

if __name__=="__main__":
    unittest.main()
