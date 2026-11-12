import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "fusion", Path(__file__).resolve().parents[1] / "factory/supreme_evidence_fusion.py"
)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class SupremeEvidenceFusionTests(unittest.TestCase):
    def test_missing_claims_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "generated").mkdir()
            report = MOD.audit(root)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertEqual(report["decision"]["automission_action"], "HOLD_AND_REVIEW")

    def test_generated_verified_state_is_never_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            g = Path(d) / "generated"
            g.mkdir()
            claim = {
                "id":"claim:verse:1","claim":"x","definitions":["x"],"source":[{"source_id":"s1"}],
                "evidence":[{"status":"SUPPORTED"}],"formulation":{},"countercases":["x"],
                "verification":{"status":"VERIFIED","independent":True},"conclusion":"x",
                "provenance":{"generator":"x","created_at":"2026-01-01T00:00:00+00:00","content_hash":"h"},
                "source_traceability":{"status":"PASS","resolved":True,"source_ids":["s1"]}
            }
            (g/"claim-evidence.jsonl").write_text(json.dumps(claim)+"\n")
            (g/"reasoning-manifest.jsonl").write_text(json.dumps({"kind":"verse","artifact_id":"1"})+"\n")
            (g/"provenance-ledger.jsonl").write_text(json.dumps({
                "artifact_id":"1","source_ids":["s1"],"content_sha256":"h",
                "created_at":"2026-01-01T00:00:00+00:00","generator":"x",
                "verification_status":"NOT_VERIFIED","independent":False})+"\n")
            (g/"source-units.jsonl").write_text(json.dumps({"id":"s1"})+"\n")
            report = MOD.audit(root)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertEqual(report["hard_fail_metrics"]["unsafe_verified_states"], 0)
            self.assertGreater(report["hard_fail_metrics"]["bad_verification_states"], 0)

if __name__ == "__main__":
    unittest.main()
