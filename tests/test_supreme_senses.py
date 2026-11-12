import unittest
from agents.supreme_senses import analyze, to_simple_language

class SuperSensesTests(unittest.TestCase):
    def test_empty_abstains(self):
        r=analyze([])
        self.assertEqual(r["status"],"ABSTAIN")
        self.assertTrue(r["governance"]["fail_closed"])

    def test_conflict_abstains(self):
        r=analyze([
          {"modality":"audio","feature":"x","value":1,"quality":1,"source":"a"},
          {"modality":"electrical","feature":"x","value":100,"quality":1,"source":"b"}])
        self.assertEqual(r["status"],"ABSTAIN")
        self.assertEqual(r["uncertainty"]["reason"],"CROSS_MODAL_CONFLICT")

    def test_candidate_is_bounded(self):
        r=analyze([
          {"modality":"audio","feature":"x","value":1.00,"quality":1,"source":"a","timestamp":"t1"},
          {"modality":"electrical","feature":"x","value":1.01,"quality":1,"source":"b","timestamp":"t2"},
          {"modality":"thermal","feature":"x","value":0.99,"quality":1,"source":"c","timestamp":"t3"}])
        self.assertEqual(r["status"],"CANDIDATE")
        self.assertGreaterEqual(r["confidence"],0.55)
        self.assertLessEqual(r["confidence"],1)
        self.assertFalse(r["governance"]["subjective_experience_claim_allowed"])
        self.assertTrue(r["governance"]["independent_verification_required"])
        self.assertIn("observable",to_simple_language(r))

if __name__=="__main__":
    unittest.main()
