#!/usr/bin/env python3
"""Create deterministic verification-intake tasks from Research Paper claims.

This adapter does not verify claims and never promotes them. It produces
review tasks for the existing independent-verification pipeline to consume.
"""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
claims_path = ROOT / "generated" / "research-paper-claims.json"
out_path = ROOT / "generated" / "research-paper-verification-intake.jsonl"

data = json.loads(claims_path.read_text(encoding="utf-8"))
rows = []

for claim in data["claims"]:
    if claim.get("verification_status") != "UNVERIFIED":
        raise SystemExit(f"fail-closed: claim {claim.get('id')} is not UNVERIFIED")
    if claim.get("status") != "AUTHOR_PROPOSITION":
        raise SystemExit(f"fail-closed: claim {claim.get('id')} is not AUTHOR_PROPOSITION")

    canonical = json.dumps(
        {"claim_id": claim["id"], "evidence_required": claim["evidence_required"]},
        ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    task_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    rows.append({
        "task_id": "SRP-VTASK-" + claim["id"],
        "claim_id": claim["id"],
        "source_repository": data["source_repository"],
        "task_hash": task_hash,
        "status": "QUEUED_FOR_INDEPENDENT_VERIFICATION",
        "verification_status": "UNVERIFIED",
        "independent": True,
        "promotion_allowed": False,
        "evidence_required": claim["evidence_required"],
        "policy": "Task creation is operational traceability only; it is not verification."
    })

rows.sort(key=lambda r: r["task_id"])
out_path.write_text(
    "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in rows) + "\n",
    encoding="utf-8"
)
print(f"Research Paper verification intake: {len(rows)} tasks")
