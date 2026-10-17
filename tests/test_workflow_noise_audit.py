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

    def test_write_permissions_and_cancel_are_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "risky.yml").write_text(
                "name: Production Critical Writer\non:\n  push:\npermissions:\n  contents: write\n"
                "concurrency:\n  group: shared\n  cancel-in-progress: true\n",
                encoding="utf-8",
            )
            report = build_report(root)
            item = report["workflows"][0]
            self.assertTrue(item["write_permissions"])
            self.assertEqual(item["concurrency_group"], "shared")
            self.assertTrue(item["cancel_in_progress"])
            self.assertEqual(item["criticality"], "critical-review")
            self.assertTrue(any("write-permission" in x for x in item["review_reasons"]))
            self.assertTrue(any("critical-workflow-cancellation-risk" in x for x in item["review_reasons"]))

    def test_workflow_run_dependencies_are_mapped_and_unresolved_refs_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "build.yml").write_text(
                "name: Build Product\non:\n  push:\n",
                encoding="utf-8",
            )
            (workflow_dir / "downstream.yml").write_text(
                'name: Downstream Consumer\non:\n  workflow_run:\n    workflows:\n      - "Build Product"\n      - "Missing Upstream"\n    types: [completed]\n',
                encoding="utf-8",
            )
            report = build_report(root)
            deps = report["workflow_run_dependencies"]
            self.assertTrue(any(d["upstream_workflow_name"] == "Build Product" and d["resolution"] == "matched" for d in deps))
            self.assertTrue(any(d["upstream_workflow_name"] == "Missing Upstream" and d["resolution"] == "unresolved-name-review" for d in deps))
            self.assertTrue(any(c["type"] == "unresolved-workflow-run-reference" for c in report["review_candidates"]))
            self.assertFalse(report["deletion_performed"])


if __name__ == "__main__":
    unittest.main()
