#!/usr/bin/env python3
"""Verify Research Paper claims enter the independent-verification queue."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry=json.loads((ROOT/"generated/research-paper-claims.json").read_text(encoding="utf-8"))
queue=ROOT/"generated/independent-verification-queue.jsonl"
assert queue.exists() and queue.stat().st_size > 0
rows=[json.loads(x) for x in queue.read_text(encoding="utf-8").splitlines() if x.strip()]
expected={f"claim:research-paper:{c['id']}" for c in registry["claims"]}
actual={str(r.get("claim_id")) for r in rows}
assert expected <= actual
for r in rows:
    if r["claim_id"] in expected:
        assert r["status"] == "QUEUED"
        assert r["verification_status"] == "NOT_VERIFIED"
        assert r["independent"] is False
        assert r["required_evidence"]
print(f"Research Paper verification queue: PASS ({len(expected)} claims queued fail-closed)")
