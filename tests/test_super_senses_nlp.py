import unittest
from agents.super_senses_nlp import fuse

class SuperSensesTests(unittest.TestCase):
    def test_multimodal_candidate(self):
        r=fuse([
          {"modality":"electrical","feature":"signal","value":1.00,"quality":1,"source":"a"},
          {"modality":"audio","feature":"signal","value":1.01,"quality":1,"source":"b"},
          {"modality":"thermal","feature":"signal","value":1.00,"quality":1,"source":"c"}])
        self.assertEqual(r["status"],"CANDIDATE")
        self.assertEqual(r["verification"]["status"],"UNVERIFIED")
        self.assertTrue(r["governance"]["fail_closed"])
        self.assertFalse(r["governance"]["subjective_experience_claim_allowed"])
        self.assertEqual(len(r["fingerprint"]),64)

    def test_conflict_blocks(self):
        r=fuse([
          {"modality":"electrical","feature":"signal","value":1,"quality":1,"source":"a"},
          {"modality":"audio","feature":"signal","value":100,"quality":1,"source":"b"}])
        self.assertEqual(r["status"],"BLOCKED")
        self.assertFalse(r["verification"]["promotion_allowed"])

    def test_no_data(self):
        r=fuse([])
        self.assertEqual(r["status"],"NO_CLAIM")
        self.assertEqual(r["metrics"]["confidence"],0.0)

if __name__=="__main__":
    unittest.main()
