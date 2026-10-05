#!/usr/bin/env python3
"""Validate Research Paper verification queue semantics without network access."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
claims=json.loads((root/"generated/research-paper-claims.json").read_text(encoding="utf-8"))["claims"]
queue=root/"generated/research-paper-verification-queue.jsonl"
assert queue.exists()
rows=[json.loads(x) for x in queue.read_text(encoding="utf-8").splitlines() if x.strip()]
assert len(rows)==len(claims)
assert {r["claim_id"] for r in rows}=={c["id"] for c in claims}
for r in rows:
    assert r["status"]=="QUEUED"
    assert r["verification_status"]=="UNVERIFIED"
    assert r["independent"] is False
    assert r["independent_verification_required"] is True
    assert r["promotion_allowed"] is False
print(f"Research Paper verification queue: PASS ({len(rows)} tasks; fail-closed)")
