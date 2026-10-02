import unittest
from agents.supreme_nlp_quality import (
    brier_score, contradiction_index, expected_calibration_error,
    evaluate, stable_fingerprint,
)

class SupremeNLPQualityTests(unittest.TestCase):
    def test_calibration_metrics(self):
        self.assertEqual(brier_score([0.0,1.0],[0,1]),0.0)
        self.assertEqual(expected_calibration_error([0.0,1.0],[0,1]),0.0)

    def test_contradiction_detected(self):
        rows=[{"feature":"x","value":1},{"feature":"x","value":100}]
        self.assertGreater(contradiction_index(rows),0.9)

    def test_fail_closed_even_when_quality_passes(self):
        record={
          "status":"CANDIDATE",
          "fingerprint":"a"*64,
          "result":{"features":{"quality":1,"agreement":1,"independent_sources":3,
                                "sample_count":20,"drift_score":0},
                    "interpretation":{"confidence":0.9},
                    "verification":{"status":"UNVERIFIED"}},
          "signals":[{"feature":"x","value":1},{"feature":"x","value":1.01}]
        }
        report=evaluate(record)
        self.assertEqual(report["status"],"PASS")
        self.assertFalse(report["promotion_allowed"])
        self.assertTrue(report["governance"]["independent_verification_required"])

    def test_fingerprint_deterministic(self):
        x={"b":2,"a":"क"}
        self.assertEqual(stable_fingerprint(x),stable_fingerprint({"a":"क","b":2}))

if __name__=="__main__":
    unittest.main()
