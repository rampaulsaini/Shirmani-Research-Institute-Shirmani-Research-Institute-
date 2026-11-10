import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from factory import bootstrap_independent_verification_queue as bootstrap


class VerificationQueueBootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.generated = self.root / "generated"
        self.generated.mkdir()
        self.source = self.generated / "independent-verification-records.json"
        self.queue = self.generated / "independent-verification-queue.jsonl"
        self.source.write_text(json.dumps({
            "records": [{
                "id": "IV-BOOTSTRAP-001",
                "status": "EVIDENCE-SUPPORTED",
                "evidence": {"sources": ["https://example.org/evidence"]},
            }]
        }), encoding="utf-8")
        self.patches = (
            patch.object(bootstrap, "SRC", self.source),
            patch.object(bootstrap, "OUT", self.queue),
        )
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()
        self.tmp.cleanup()

    def run_bootstrap(self):
        with contextlib.redirect_stdout(io.StringIO()):
            bootstrap.main()

    def test_summary_is_written_next_to_jsonl_queue(self):
        self.run_bootstrap()
        summary = self.generated / "VERIFICATION-QUEUE.json"
        self.assertTrue(self.queue.is_file())
        self.assertTrue(summary.is_file())
        self.assertFalse((self.queue / "VERIFICATION-QUEUE.json").exists())
        payload = json.loads(summary.read_text(encoding="utf-8"))
        self.assertEqual(payload["records"], 1)
        self.assertEqual(payload["queued"], 1)
        self.assertEqual(payload["verified"], 0)

    def test_existing_review_state_and_timestamp_survive_repeated_cycle(self):
        self.run_bootstrap()
        task = json.loads(self.queue.read_text(encoding="utf-8").splitlines()[0])
        original_created_at = task["created_at"]
        task["status"] = "REVIEWED"
        self.queue.write_text(json.dumps(task) + "\n", encoding="utf-8")

        self.run_bootstrap()
        persisted = json.loads(self.queue.read_text(encoding="utf-8").splitlines()[0])
        summary = json.loads((self.generated / "VERIFICATION-QUEUE.json").read_text(encoding="utf-8"))
        self.assertEqual(persisted["status"], "REVIEWED")
        self.assertEqual(persisted["created_at"], original_created_at)
        self.assertEqual(summary["reviewed"], 1)
        self.assertEqual(summary["queued"], 0)
        self.assertEqual(summary["verified"], 0)


if __name__ == "__main__":
    unittest.main()
