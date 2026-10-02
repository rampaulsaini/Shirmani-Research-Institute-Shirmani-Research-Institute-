import unittest
from agents.ultra_mega_infinity_quantum_nlp import interpret

class TestUltraMegaInfinityQuantumNLP(unittest.TestCase):
    def test_deterministic_interpretation(self):
        rows=[{"modality":"plant-signal","feature":"electrical_a","value":1.0,"quality":1.0,"source":"synthetic"},
              {"modality":"plant-signal","feature":"vibration_a","value":1.0,"quality":1.0,"source":"synthetic"}]
        a=interpret(rows,"test-cycle"); b=interpret(rows,"test-cycle")
        self.assertEqual(a["fingerprint"],b["fingerprint"])
        self.assertFalse(a["interpretation"]["subjective_experience_claim"])
    def test_invalid_data_fails_closed(self):
        r=interpret([{"bad":"row"}],"empty")
        self.assertEqual(r["interpretation"]["status"],"NO_DATA")
        self.assertEqual(r["interpretation"]["confidence"],0.0)
    def test_low_quality_does_not_claim_certainty(self):
        r=interpret([{"modality":"sensor","feature":"x","value":100,"quality":0.1,"source":"synthetic"}],"low-quality")
        self.assertLess(r["interpretation"]["confidence"],0.60)
        self.assertFalse(r["governance"]["subjective_experience_claim_allowed"])

if __name__=="__main__":
    unittest.main()
