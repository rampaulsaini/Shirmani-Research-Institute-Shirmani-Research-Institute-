import tempfile
import unittest
from pathlib import Path

from scripts.workflow_noise_audit import build_report


class WorkflowNoiseAuditTests(unittest.TestCase):
    def _root(self, tmp):
        root = Path(tmp)
        (root / ".github" / "workflows").mkdir(parents=True)
        return root

    def test_read_only_and_manual_only_is_review_not_delete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._root(tmp)
            (root / ".github/workflows/manual.yml").write_text(
                "name: Manual fallback\non:\n  workflow_dispatch:\n"
                "permissions:\n  contents: read\njobs:\n  check:\n"
                "    runs-on: ubuntu-latest\n    timeout-minutes: 5\n",
                encoding="utf-8",
            )
            report = build_report(root)
            self.assertEqual(report["workflow_count"], 1)
            self.assertFalse(report["deletion_performed"])
            self.assertFalse(report["changes_performed"])
            self.assertEqual(report["mode"], "read-only")
            self.assertTrue(any(
                "manual-dispatch-only" in x["reason"]
                for x in report["review_candidates"]
            ))

    def test_exact_duplicates_are_reported_without_removal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._root(tmp)
            content = (
                "name: Read only\non:\n  push:\npermissions:\n"
                "  contents: read\njobs:\n  check:\n"
                "    runs-on: ubuntu-latest\n    timeout-minutes: 5\n"
            )
            (root / ".github/workflows/a.yml").write_text(content, encoding="utf-8")
            (root / ".github/workflows/b.yaml").write_text(content, encoding="utf-8")
            report = build_report(root)
            self.assertEqual(report["exact_duplicate_groups"], 1)
            self.assertFalse(report["deletion_performed"])
            self.assertTrue(any(
                x["type"] == "exact-content-duplicate-review"
                for x in report["review_candidates"]
            ))

    def test_write_permissions_and_cancel_are_flagged_as_risk_not_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._root(tmp)
            (root / ".github/workflows/risky.yml").write_text(
                "name: Critical production writer\non:\n  push:\n"
                "permissions:\n  contents: write\n"
                "concurrency:\n  group: production-writer\n"
                "  cancel-in-progress: true\njobs:\n  build:\n"
                "    runs-on: ubuntu-latest\n    timeout-minutes: 10\n",
                encoding="utf-8",
            )
            report = build_report(root)
            item = report["workflows"][0]
            self.assertTrue(item["write_permissions"])
            self.assertEqual(item["concurrency_group"], "production-writer")
            self.assertTrue(item["cancel_in_progress"])
            self.assertEqual(item["timeout_minutes"], [10])
            reasons = item["review_reasons"]
            self.assertTrue(any("write-permission" in x for x in reasons))
            self.assertTrue(any("cancels-in-progress" in x for x in reasons))
            self.assertTrue(any("critical-work-cancellation-risk" in x for x in reasons))
            self.assertFalse(report["deletion_performed"])

    def test_event_signatures_are_inventory_only_not_delete_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._root(tmp)
            content = (
                "name: A check\non:\n  push:\n  pull_request:\n"
                "jobs:\n  test:\n    runs-on: ubuntu-latest\n"
                "    timeout-minutes: 5\n"
            )
            (root / ".github/workflows/a.yml").write_text(content, encoding="utf-8")
            (root / ".github/workflows/b.yml").write_text(content.replace("name: A check", "name: B check"), encoding="utf-8")
            report = build_report(root)
            self.assertEqual(report["same_event_signature_groups"], 1)
            self.assertEqual(report["event_counts"], {"pull_request": 2, "push": 2})
            self.assertFalse(any(
                x["type"] == "same-event-signature-delete"
                for x in report["review_candidates"]
            ))
            self.assertIn(
                "Matching event signatures are not proof of duplicate behavior.",
                report["policy"],
            )

    def test_missing_timeout_is_a_review_hint_not_a_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._root(tmp)
            (root / ".github/workflows/no-timeout.yml").write_text(
                "name: Check\non:\n  push:\njobs:\n  test:\n"
                "    runs-on: ubuntu-latest\n",
                encoding="utf-8",
            )
            report = build_report(root)
            self.assertTrue(any(
                "no-static-timeout-minutes-found" in reason
                for reason in report["workflows"][0]["review_reasons"]
            ))
            self.assertEqual(report["mode"], "read-only")


if __name__ == "__main__":
    unittest.main()
