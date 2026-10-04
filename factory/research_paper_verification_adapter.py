#!/usr/bin/env python3
"""Create deterministic verification tasks for registered Research Paper claims.

This adapter creates review work, not proof. Every task remains UNVERIFIED until
an independent verification record satisfies the existing promotion boundary.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
claims = json.loads((ROOT/"generated/research-paper-claims.json").read_text(encoding="utf-8"))["claims"]
out = ROOT/"generated/research-paper-verification-queue.jsonl"
rows = []
for c in claims:
    rows.append({
        "task_id": f"VRF-{c['id']}",
        "claim_id": c["id"],
        "source_repository": "rampaulsaini/Shirmani-Research-Paper",
        "status": "QUEUED",
        "verification_status": "UNVERIFIED",
        "independent": True,
        "evidence_required": c["evidence_required"],
        "promotion_blocked": True,
        "policy": "Queueing a verification task is not verification."
    })
out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in rows), encoding="utf-8")
print(f"Research Paper verification tasks: {len(rows)}")
