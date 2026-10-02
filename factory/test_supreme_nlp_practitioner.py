import unittest
from supreme_nlp_practitioner import evaluate

class SupremeNLPPractitionerTests(unittest.TestCase):
    def test_missing_provenance_fails_closed(self):
        r = evaluate({"record_id":"t-1","signal":"temperature=31C","pattern":"change",
                      "inference":"possible transition","provenance":[]})
        self.assertEqual(r.status, "BLOCKED")
        self.assertEqual(r.verification_state, "BLOCKED")

    def test_unverified_signal_never_becomes_subjective_claim(self):
        r = evaluate({"record_id":"t-2","signal":"instrument voltage pattern",
                      "pattern":"repeatable oscillation","inference":"pattern class A",
                      "confidence":0.82,"provenance":["instrument://sample-2"],
                      "verification_state":"UNVERIFIED"})
        self.assertEqual(r.verification_state, "UNVERIFIED")
        self.assertIn("not proof of subjective feeling", r.interpretation)

    def test_verified_without_evidence_is_downgraded(self):
        r = evaluate({"record_id":"t-3","signal":"acoustic sequence",
                      "pattern":"sequence cluster","inference":"cluster B",
                      "provenance":["instrument://sample-3"],"verification_state":"VERIFIED"})
        self.assertEqual(r.verification_state, "REVIEW")

if __name__ == "__main__":
    unittest.main()
