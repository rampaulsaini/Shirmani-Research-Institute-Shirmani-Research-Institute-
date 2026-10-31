from __future__ import annotations

import gzip
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import importlib.util

spec = importlib.util.spec_from_file_location(
    "independent_verification_status", ROOT / "factory" / "independent_verification_status.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
build_status = module.build_status


class IndependentVerificationStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.generated = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write_gzip(self, name, rows):
        path = self.generated / name
        with gzip.open(path, "wt", encoding="utf-8") as stream:
            for row in rows:
                stream.write(json.dumps(row) + "\n")

    def seed(self, queue, registry):
        self.write_gzip("independent-verification-queue.jsonl.gz", queue)
        self.write_gzip("independent-verification-registry.jsonl.gz", registry)

    def test_verified_requires_reviewed_status_and_independent_true(self):
        queue = [{"task_id": "a"}, {"task_id": "b"}, {"task_id": "c"}]
        registry = [
            {"task_id": "a", "status": "REVIEWED", "verification_status": "VERIFIED", "independent": True},
            {"task_id": "b", "status": "REVIEWED", "verification_status": "VERIFIED", "independent": False},
            {"task_id": "c", "status": "PENDING", "verification_status": "PENDING"},
        ]
        self.seed(queue, registry)
        (self.generated / "verification-review-packet-000001-000002.json").write_text(
            json.dumps({"status": "READY_FOR_HUMAN_REVIEW"}), encoding="utf-8"
        )

        result = build_status(self.generated)

        self.assertEqual(result["queue_total"], 3)
        self.assertEqual(result["registry_total"], 3)
        self.assertEqual(result["verified_records"], 1)
        self.assertEqual(result["review_records"], 2)
        self.assertEqual(result["unverified_records"], 2)
        self.assertEqual(result["prepared_review_records"], 2)
        self.assertTrue(result["integrity"]["queue_registry_task_ids_match"])
        self.assertTrue(result["generated_at"])

    def test_queue_registry_mismatch_fails_closed(self):
        self.seed([{"task_id": "a"}], [{"task_id": "b"}])
        with self.assertRaisesRegex(ValueError, "task_id sets do not match"):
            build_status(self.generated)

    def test_duplicate_queue_ids_fail_closed(self):
        self.seed([{"task_id": "a"}, {"task_id": "a"}], [{"task_id": "a"}])
        with self.assertRaisesRegex(ValueError, "duplicate task_id"):
            build_status(self.generated)

    def test_overlapping_prepared_ranges_fail_closed(self):
        queue = [{"task_id": str(i)} for i in range(1, 5)]
        self.seed(queue, queue)
        for name in (
            "verification-review-packet-000001-000003.json",
            "verification-review-packet-000003-000004.json",
        ):
            (self.generated / name).write_text(
                json.dumps({"status": "READY_FOR_HUMAN_REVIEW"}), encoding="utf-8"
            )
        with self.assertRaisesRegex(ValueError, "ranges overlap"):
            build_status(self.generated)


if __name__ == "__main__":
    unittest.main()
