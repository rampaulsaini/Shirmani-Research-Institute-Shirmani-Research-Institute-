"""Contract tests for result-first multi-layer orchestration.

These tests enforce that the orchestrator measures concrete result production
without turning queue/workflow activity into independent verification.
"""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

from factory import result_first_orchestrator as rfo


class ResultFirstOrchestratorTests(unittest.TestCase):
    def test_empty_inputs_do_not_look_like_result_production(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            plan = out / "plan.json"
            with patch.object(rfo, "OUT", out), patch.object(rfo, "PLAN", plan):
                rfo.main()
            data = json.loads(plan.read_text(encoding="utf-8"))

        self.assertFalse(data["dimensions"]["result_production"])
        self.assertTrue(data["fail_closed"])
        self.assertEqual(data["result_metrics"]["verification_queue_records"], 0)
        self.assertEqual(data["result_metrics"]["verification_registry_records"], 0)

    def test_verification_activity_never_becomes_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "independent-verification-status-1.json").write_text(
                json.dumps(
                    {
                        "verification_summary": {
                            "independently_verified_records": 1,
                            "independent_verified_percent": 100,
                            "verification_readiness_percent": 100,
                        },
                        "records": [{"status": "VERIFIED"}],
                    }
                ),
                encoding="utf-8",
            )
            plan = out / "plan.json"
            with patch.object(rfo, "OUT", out), patch.object(rfo, "PLAN", plan):
                rfo.main()
            data = json.loads(plan.read_text(encoding="utf-8"))

        self.assertFalse(data["dimensions"]["verification_boundary"])
        self.assertEqual(data["result_metrics"]["independently_verified_records"], 1)
        self.assertTrue(data["fail_closed"])

    def test_integrity_hash_is_stable_for_same_plan_content(self):
        payload = {"b": 2, "a": 1}
        first = rfo.sha256_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        )
        second = rfo.sha256_text(
            json.dumps({"a": 1, "b": 2}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        )
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
