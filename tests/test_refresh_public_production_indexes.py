import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "factory" / "refresh_public_production_indexes.py"
SPEC = importlib.util.spec_from_file_location("refresh_public_production_indexes", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RefreshPublicProductionIndexesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        generated = self.root / "generated"
        lanes = generated / "public-production"
        lanes.mkdir(parents=True)
        self.queue = generated / "production-work-queue.jsonl"
        self.results = generated / "production-results.jsonl"
        self.catalog = generated / "public-production-catalog.json"
        self.archive = lanes / "archive"
        self.archive_index = self.archive / "index.json"
        self.lane_file = lanes / "test-lane.jsonl"

        queued = {
            "task_id": "task-001",
            "cycle": 12,
            "slot": 1,
            "lane": "test-lane",
            "module": "factory/example.py",
        }
        self.queue.write_text(json.dumps(queued) + "\n", encoding="utf-8")
        self.queued = queued

        MODULE.ROOT = self.root
        MODULE.GEN = generated
        MODULE.QUEUE = self.queue
        MODULE.RESULTS = self.results
        MODULE.LANES = lanes
        MODULE.ARCHIVE = self.archive
        MODULE.CATALOG = self.catalog
        MODULE.ARCHIVE_INDEX = self.archive_index

    def tearDown(self):
        self.temp.cleanup()

    def write_lane(self, produced_at):
        row = {
            "task_id": "task-001",
            "cycle": 12,
            "slot": 1,
            "lane": "test-lane",
            "module": "factory/example.py",
            "status": "PRODUCED",
            "produced_at": produced_at,
            "integrity": {"source_bound": True},
        }
        self.lane_file.write_text(json.dumps(row) + "\n", encoding="utf-8")

    def test_fresh_lane_record_builds_indexes_with_source_time(self):
        produced_at = (datetime.now(timezone.utc) - timedelta(seconds=30)).isoformat()
        self.write_lane(produced_at)
        original_lane = self.lane_file.read_text(encoding="utf-8")

        MODULE.main()

        catalog = json.loads(self.catalog.read_text(encoding="utf-8"))
        archive = json.loads(self.archive_index.read_text(encoding="utf-8"))
        self.assertEqual(catalog["source_cycle"], 12)
        self.assertEqual(archive["source_cycle"], 12)
        self.assertEqual(catalog["source_produced_at"], produced_at)
        self.assertEqual(archive["source_produced_at"], produced_at)
        self.assertEqual(self.lane_file.read_text(encoding="utf-8"), original_lane)
        self.assertEqual(len(self.results.read_text(encoding="utf-8").splitlines()), 1)


    def test_malformed_archive_filename_is_excluded_but_preserved(self):
        produced_at = (datetime.now(timezone.utc) - timedelta(seconds=30)).isoformat()
        self.write_lane(produced_at)
        self.archive.mkdir(parents=True, exist_ok=True)
        malformed = self.archive / "production-cycle-5970968.jsonl"
        malformed.write_text('{"legacy": true}\\n', encoding="utf-8")

        MODULE.main()

        archive = json.loads(self.archive_index.read_text(encoding="utf-8"))
        self.assertNotIn(malformed.name, archive["files"])
        self.assertIn(malformed.name, archive["ignored_malformed_archive_files"])
        self.assertTrue(malformed.is_file())
        self.assertTrue(archive["integrity"]["archive_index_excludes_malformed_shard_names"])

    def test_stale_lane_record_cannot_be_relabelled_fresh(self):
        produced_at = (datetime.now(timezone.utc) - timedelta(seconds=1900)).isoformat()
        self.write_lane(produced_at)

        with self.assertRaisesRegex(SystemExit, "stale or future-dated"):
            MODULE.main()

        self.assertFalse(self.results.exists())
        self.assertFalse(self.catalog.exists())
        self.assertFalse(self.archive_index.exists())


if __name__ == "__main__":
    unittest.main()
