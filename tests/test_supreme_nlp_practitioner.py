import unittest
from agents.supreme_nlp_practitioner import interpret, plain_language

class SupremeNLPPractitionerTests(unittest.TestCase):
    def test_empty_is_fail_closed(self):
        r=interpret([], "empty")
        self.assertEqual(r["result"]["status"], "no_data")
        self.assertIn("कोई", plain_language(r))

    def test_low_quality_is_not_interpreted(self):
        r=interpret([
            {"modality":"plant","feature":"voltage","value":1,"quality":0.2},
            {"modality":"plant","feature":"voltage","value":2,"quality":0.3}
        ], "lowq")
        self.assertEqual(r["result"]["status"], "insufficient_quality")

    def test_cross_modal_conflict_is_explicit(self):
        r=interpret([
            {"modality":"electrical","feature":"signal","value":1,"quality":1,"calibration":"calibrated"},
            {"modality":"audio","feature":"signal","value":100,"quality":1,"calibration":"calibrated"}
        ], "conflict")
        self.assertEqual(r["result"]["status"], "conflict")
        self.assertLess(r["result"]["features"]["agreement"], 0.45)

    def test_deterministic_fingerprint(self):
        rows=[
            {"modality":"electrical","feature":"signal","value":1,"quality":1,"calibration":"calibrated"},
            {"modality":"audio","feature":"signal","value":1.1,"quality":1,"calibration":"calibrated"}
        ]
        a=interpret(rows,"same"); b=interpret(rows,"same")
        self.assertEqual(a["fingerprint"], b["fingerprint"])

if __name__=="__main__":
    unittest.main()
