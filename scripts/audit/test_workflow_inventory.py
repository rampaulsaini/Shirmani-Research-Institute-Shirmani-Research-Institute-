import tempfile
import unittest
from pathlib import Path

from workflow_inventory import build_inventory, inspect_workflow


SAMPLE = """name: Example deploy
on:
  push:
    branches: [main]
  schedule:
    - cron: "*/15 * * * *"
permissions:
  contents: read
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo ok
"""


class WorkflowInventoryTests(unittest.TestCase):
    def test_extracts_review_metadata_without_deletion_recommendation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            path = workflow_dir / "example.yml"
            path.write_text(SAMPLE, encoding="utf-8")
            record = inspect_workflow(path, root=root)
            self.assertEqual(record["name"], "Example deploy")
            self.assertIn("push", record["triggers"])
            self.assertIn("schedule", record["triggers"])
            self.assertEqual(record["schedule_crons"], ["*/15 * * * *"])
            self.assertTrue(record["permissions_declared"])
            self.assertTrue(record["concurrency_declared"])
            self.assertEqual(record["job_ids"], ["test"])
            self.assertFalse(record["deletion_candidate"])
            self.assertEqual(record["triage_status"], "UNKNOWN")

    def test_duplicate_names_are_signals_not_deletion_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            for filename in ("one.yml", "two.yaml"):
                (workflow_dir / filename).write_text(SAMPLE, encoding="utf-8")
            report = build_inventory(workflow_dir=workflow_dir, root=root)
            self.assertEqual(report["workflow_file_count"], 2)
            self.assertEqual(report["triage_status_counts"]["UNKNOWN"], 2)
            self.assertTrue(all(item["duplicate_name_is_not_removal_evidence"] for item in report["workflows"]))
            self.assertTrue(all(item["deletion_candidate"] is False for item in report["workflows"]))


if __name__ == "__main__":
    unittest.main()
