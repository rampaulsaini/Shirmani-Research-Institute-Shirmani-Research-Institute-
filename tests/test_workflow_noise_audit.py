import tempfile
import unittest
from pathlib import Path

from scripts.workflow_noise_audit import build_report


class WorkflowNoiseAuditTests(unittest.TestCase):
    def test_read_only_and_manual_only_is_review_not_delete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "manual.yml").write_text(
                "name: Manual fallback\non:\n  workflow_dispatch:\npermissions:\n  contents: read\n",
                encoding="utf-8",
            )
            report = build_report(root)
            self.assertEqual(report["workflow_count"], 1)
            self.assertFalse(report["deletion_performed"])
            self.assertEqual(report["mode"], "read-only")
            self.assertTrue(any("manual-dispatch-only" in x["reason"] for x in report["review_candidates"]))

    def test_exact_duplicates_are_reported_without_removal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            content = "name: Read only\non:\n  push:\npermissions:\n  contents: read\n"
            (workflow_dir / "a.yml").write_text(content, encoding="utf-8")
            (workflow_dir / "b.yaml").write_text(content, encoding="utf-8")
            report = build_report(root)
            self.assertEqual(report["exact_duplicate_groups"], 1)
            self.assertFalse(report["deletion_performed"])
            self.assertTrue(any(x["type"] == "exact-content-duplicate-review" for x in report["review_candidates"]))

    def test_high_frequency_schedule_is_flagged_without_modification(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "frequent.yml").write_text(
                'name: Frequent worker\\non:\\n  schedule:\\n    - cron: "*/5 * * * *"\\n'
                '  workflow_dispatch:\\npermissions:\\n  contents: read\\n',
                encoding="utf-8",
            )
            report = build_report(root)
            workflow = report["workflows"][0]
            self.assertEqual(workflow["schedule_crons"], ["*/5 * * * *"])
            self.assertTrue(any("high-frequency-schedule" in reason for reason in workflow["review_reasons"]))
            self.assertFalse(report["deletion_performed"])

    def test_write_permissions_and_cancel_are_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "risky.yml").write_text(
                "name: Critical writer\non:\n  push:\npermissions:\n  contents: write\n"
                "concurrency:\n  group: shared\n  cancel-in-progress: true\n",
                encoding="utf-8",
            )
            report = build_report(root)
            reasons = report["workflows"][0]["review_reasons"]
            self.assertTrue(any("write-permission" in x for x in reasons))
            self.assertTrue(any("cancels-in-progress" in x for x in reasons))


if __name__ == "__main__":
    unittest.main()
