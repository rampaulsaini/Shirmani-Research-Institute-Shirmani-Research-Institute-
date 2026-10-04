#!/usr/bin/env python3
"""Regression test for Research Paper entries emitted by the reasoning pipeline."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "generated" / "research-paper-claims.json").read_text(encoding="utf-8"))
manifest = ROOT / "generated" / "reasoning-manifest.jsonl"
claims = ROOT / "generated" / "claim-evidence.jsonl"

assert manifest.exists(), "reasoning-manifest.jsonl is missing"
assert claims.exists(), "claim-evidence.jsonl is missing"

rows = [json.loads(x) for x in manifest.read_text(encoding="utf-8").splitlines() if x.strip()]
claim_rows = [json.loads(x) for x in claims.read_text(encoding="utf-8").splitlines() if x.strip()]
expected = {f"research-paper:{c['id']}" for c in registry["claims"]}

actual = {str(r.get("artifact_id")) for r in rows if str(r.get("kind")) == "research-paper"}
assert expected <= actual

for r in rows:
    if str(r.get("artifact_id")) not in expected:
        continue
    assert r.get("verification", {}).get("status") == "NOT_VERIFIED"
    assert r.get("verification", {}).get("independent") is False
    assert r.get("evidence_status") in {"SOURCE_TRACE", "NOT_VERIFIED", "UNVERIFIED"} or r.get("evidence_status") is not None

ce_ids = {str(r.get("id")) for r in claim_rows}
for claim_id in expected:
    assert f"claim:{claim_id}" in ce_ids

print(f"Research Paper reasoning pipeline: PASS ({len(expected)} claims integrated)")
