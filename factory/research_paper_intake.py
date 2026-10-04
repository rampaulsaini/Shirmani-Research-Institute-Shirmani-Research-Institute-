#!/usr/bin/env python3
"""Convert registered Research Paper claims into fail-closed verification tasks.

This is an intake adapter, not a verifier. It creates review work only.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / "federation/research-paper-source-intake.json").read_text(encoding="utf-8"))
claims = json.loads((ROOT / source["claim_registry"]).read_text(encoding="utf-8"))

if source["verification_status"] != "UNVERIFIED":
    raise SystemExit("Research Paper intake must remain UNVERIFIED")

rows = []
for claim in claims["claims"]:
    if claim["verification_status"] != "UNVERIFIED":
        raise SystemExit(f"claim {claim['id']} is not UNVERIFIED")
    rows.append({
        "task_id": "SRP-VERIFY-" + claim["id"],
        "claim_id": claim["id"],
        "source_id": source["source_id"],
        "repository": source["repository"],
        "verification_status": "UNVERIFIED",
        "status": "QUEUED",
        "independent_verification_required": True,
        "evidence_required": claim["evidence_required"],
        "promotion_allowed": False,
        "policy": "Queueing a task is not verification and does not establish truth."
    })

out = ROOT / "generated/research-paper-verification-queue.jsonl"
out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
print(f"Research Paper verification queue: {len(rows)} tasks")
