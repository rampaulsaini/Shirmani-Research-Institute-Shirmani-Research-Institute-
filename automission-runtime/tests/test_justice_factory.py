import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from justice_factory import build_case_plan, validate_case_plan

class JusticeFactoryTests(unittest.TestCase):
    def test_case_plan_is_source_and_human_review_oriented(self):
        plan = build_case_plan(
            "Civil property dispute",
            "India",
            "legal_research",
            "hi",
        )
        self.assertEqual(plan["ai_role"], "decision_support_only")
        self.assertFalse(plan["binding_judgment"])
        self.assertIn("citation_verification", plan["workflow"])
        self.assertTrue(validate_case_plan(plan))

    def test_invalid_service_rejected(self):
        with self.assertRaises(ValueError):
            build_case_plan("X", "India", "final_judgment")

if __name__ == "__main__":
    unittest.main()
