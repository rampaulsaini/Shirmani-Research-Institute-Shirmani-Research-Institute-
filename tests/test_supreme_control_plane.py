import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agents"))

from supreme_control_plane import Policy, run


class ControlPlaneTests(unittest.TestCase):
    def observations(self):
        return [
            {"modality": "sensor", "feature": "signal", "value": 1.0, "quality": 0.95, "source": "A"},
            {"modality": "sensor", "feature": "signal", "value": 1.01, "quality": 0.95, "source": "B"},
        ] * 5

    def test_fail_closed_without_independent_verification(self):
        record = run(self.observations(), "pattern")
        self.assertEqual(record["decision"], "HOLD_UNVERIFIED")
        self.assertFalse(record["promotion_allowed"])

    def test_weak_evidence_is_not_promoted(self):
        weak = [{"modality": "sensor", "feature": "signal", "value": 1.0, "quality": 0.2, "source": "A"}]
        record = run(weak, "pattern")
        self.assertEqual(record["decision"], "IMPROVEMENT_REQUIRED")
        self.assertFalse(record["promotion_allowed"])

    def test_policy_is_serializable(self):
        policy = Policy()
        self.assertGreaterEqual(policy.min_quality, 0.0)
        self.assertLessEqual(policy.min_quality, 1.0)

    def test_record_is_json_serializable(self):
        record = run(self.observations())
        json.dumps(record, ensure_ascii=False)


if __name__ == "__main__":
    unittest.main()
