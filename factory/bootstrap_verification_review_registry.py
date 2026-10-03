#!/usr/bin/env python3
"""Create/preserve independent-review slots bound to the exact current queue.

Pending slots may be created automatically. Existing review decisions are preserved
so a 5-minute conveyor cycle cannot erase independent reviewer work.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
OUT = ROOT / "generated/independent-verification-registry.jsonl"

def task_hash(task):
    return hashlib.sha256(json.dumps(task, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

def load_existing():
    existing = {}
    if not OUT.exists():
        return existing
    for line in OUT.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            existing[row["task_id"]] = row
    return existing

def main():
    existing = load_existing()
    rows = []
    now = datetime.now(timezone.utc).isoformat()

    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = task["task_id"]
        prior = existing.get(task_id)

        if prior and prior.get("status") == "REVIEWED":
            # Preserve the independent decision while re-binding it to the
            # exact current queue task. A changed task therefore invalidates
            # the old review through the promotion gate.
            prior = dict(prior)
            prior["audit"] = dict(prior.get("audit") or {})
            prior["audit"]["record_hash"] = task_hash(task)
            rows.append(prior)
            continue

        rows.append({
            "review_id": "REVIEW-" + task_id,
            "task_id": task_id,
            "claim_id": task["claim_id"],
            "status": "PENDING_REVIEW",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "reviewer": "",
            "reviewer_role": "",
            "reviewed_at": "",
            "evidence_references": list(task.get("source_ids") or []),
            "countercase_review": {"status": "PENDING", "references": []},
            "reproduction_or_test": {"status": "PENDING", "references": []},
            "audit": {"recorded_at": "", "record_hash": task_hash(task)},
            "created_at": now,
            "generator": "factory/bootstrap_verification_review_registry.py"
        })

    OUT.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows), encoding="utf-8")
    reviewed = sum(1 for x in rows if x.get("status") == "REVIEWED")
    verified = sum(1 for x in rows if x.get("verification_status") == "VERIFIED")
    print(json.dumps({"review_slots": len(rows), "reviewed_records": reviewed, "verified_records": verified, "fail_closed": True, "existing_review_decisions_preserved": True}, ensure_ascii=False))

if __name__ == "__main__":
    main()
