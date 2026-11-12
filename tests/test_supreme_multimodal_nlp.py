import unittest
from factory.supreme_multimodal_nlp import classify_signal, evaluate_multimodal, translate_to_simple_language

class SupremeMultimodalNlpTests(unittest.TestCase):
    def test_empty_signal_fails_closed(self):
        r=classify_signal([])
        self.assertEqual(r["label"],"NO_SIGNAL")
        self.assertEqual(r["confidence"],0.0)

    def test_stable_signal_is_deterministic(self):
        a=classify_signal([10,10.1,9.9,10])
        b=classify_signal([10,10.1,9.9,10])
        self.assertEqual(a,b)
        self.assertEqual(a["label"],"STABLE_PATTERN")

    def test_language_preserves_claim_boundary(self):
        r=classify_signal([1,2,1,2])
        s=translate_to_simple_language(r)
        self.assertIn("प्रत्यक्ष प्रमाण",s)

    def test_provenance_is_required(self):
        r=evaluate_multimodal([{"source_id":"sensor-1","modality":"electrical","values":[1,1,1]}])
        self.assertTrue(r["fail_closed"])
        r=evaluate_multimodal([{"modality":"electrical","values":[1,1,1]}])
        self.assertFalse(r["fail_closed"])
        self.assertEqual(r["missing_provenance"],1)

if __name__=="__main__":
    unittest.main()
