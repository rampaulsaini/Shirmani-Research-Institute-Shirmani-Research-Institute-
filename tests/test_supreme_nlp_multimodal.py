import unittest
from agents.supreme_nlp_multimodal import analyze, fingerprint, to_simple_language

class SupremeNlpMultimodalTests(unittest.TestCase):
    def test_deterministic_structure(self):
        rows=[
          {"modality":"electrical","feature":"x","value":1.0,"quality":1.0,"source":"a"},
          {"modality":"audio","feature":"x","value":1.01,"quality":1.0,"source":"b"}]
        a=analyze(rows); b=analyze(rows)
        self.assertEqual(a["evidence_class"],b["evidence_class"])
        self.assertEqual(a["metrics"],b["metrics"])
        self.assertEqual(a["confidence"],b["confidence"])
        self.assertEqual(a["provenance"]["fingerprint"],fingerprint(a))

    def test_empty_input_abstains(self):
        r=analyze([])
        self.assertEqual(r["status"],"NO_CLAIM")
        self.assertEqual(r["evidence_class"],"UNKNOWN")
        self.assertIn("पर्याप्त",to_simple_language(r))

    def test_low_quality_not_promoted(self):
        r=analyze([{"modality":"sensor","feature":"x","value":1,"quality":0,"source":"bad"}])
        self.assertEqual(r["status"],"NO_CLAIM")
        self.assertFalse(r["verification"]["promotion_allowed"])

    def test_experience_request_remains_bounded(self):
        r=analyze([
          {"modality":"electrical","feature":"x","value":1,"quality":1,"source":"a"},
          {"modality":"audio","feature":"x","value":1.01,"quality":1,"source":"b"}],
          request="क्या यह जीव महसूस कर रहा है?")
        self.assertEqual(r["evidence_class"],"INFERRED")
        self.assertFalse(r["verification"]["promotion_allowed"])

if __name__=="__main__":
    unittest.main()
