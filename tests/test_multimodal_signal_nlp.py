import unittest
from factory.multimodal_signal_nlp import SCHEMA_VERSION, classify_signal, interpret, normalize_observation, plain_language

class MultimodalSignalNlpTests(unittest.TestCase):
    def test_schema(self): self.assertEqual(SCHEMA_VERSION,"1.0")
    def test_classification(self):
        o=normalize_observation({"name":"electrical_activity","value":12,"unit":"mV","baseline":10,"tolerance":1})
        self.assertEqual(classify_signal(o),"strong deviation from baseline")
    def test_claim_boundary(self):
        r=interpret([{"name":"temperature","value":32,"unit":"C","baseline":25,"tolerance":2}],context="plant environment")
        self.assertIn("measured signal patterns",plain_language(r))
        self.assertIn("does not prove",plain_language(r))
    def test_empty_is_fail_closed(self):
        r=interpret([]); self.assertEqual(r["status"],"NO_SIGNAL"); self.assertEqual(r["confidence"],0.0)
    def test_invalid_quality(self):
        with self.assertRaises(ValueError):
            interpret([{"name":"x","value":1,"unit":"u","baseline":0,"tolerance":1}],source_quality=2)

if __name__=="__main__": unittest.main()
