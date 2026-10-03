#!/usr/bin/env python3
"""Bootstrap pending review slots without overwriting completed review records.

Pending slots may be created automatically; independent verification decisions
must remain durable and are never auto-created by this script.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "generated/independent-verification-queue.jsonl"
OUT = ROOT / "generated/independent-verification-registry.jsonl"

def task_hash(task):
    return hashlib.sha256(
        json.dumps(task, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()

def load_existing():
    if not OUT.exists():
        return {}
    existing = {}
    for line in OUT.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        task_id = str(row.get("task_id", ""))
        if task_id:
            existing[task_id] = row
    return existing

def main():
    existing = load_existing()
    now = datetime.now(timezone.utc).isoformat()
    rows = []
    preserved = 0
    created = 0

    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = str(task["task_id"])

        if task_id in existing:
            rows.append(existing[task_id])
            preserved += 1
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
        created += 1

    OUT.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows),
        encoding="utf-8"
    )
    print(json.dumps({
        "review_slots": len(rows),
        "created_pending_slots": created,
        "preserved_review_records": preserved,
        "verified_records": sum(
            1 for x in rows if x.get("verification_status") == "VERIFIED"
        ),
        "fail_closed": True
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
