import unittest
from factory.supreme_signal_nlp_contract import validate_output, validate_signal

class SupremeSignalNLPContractTests(unittest.TestCase):
    def test_valid_signal(self):
        signal={"signal_id":"t1","source_type":"sensor","timestamp":"2026-10-01T00:00:00Z",
                "features":{"x":1},"context":{"baseline":"b"}}
        self.assertEqual(validate_signal(signal),[])
    def test_confidence_must_be_bounded(self):
        output={"observation":"Measured change.","interpretation":"Compatible with a changed state.",
                "confidence":1.4,"evidence":["sensor"],"limitations":["not proof of subjective experience"],"provenance":["t1"]}
        self.assertTrue(any("confidence" in e for e in validate_output(output)))
    def test_no_direct_subjective_claims(self):
        output={"observation":"The system is proven to feel pain.","interpretation":"Directly feels pain.",
                "confidence":0.9,"evidence":["signal"],"limitations":["none"],"provenance":["t1"]}
        self.assertTrue(validate_output(output))

if __name__=="__main__":
    unittest.main()
