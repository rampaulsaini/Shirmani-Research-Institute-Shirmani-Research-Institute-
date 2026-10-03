#!/usr/bin/env python3
"""Create/preserve review slots bound to the exact current verification queue.

Pending slots are created only for new tasks. Existing review records are
preserved when their task binding is still valid, so a completed independent
review is not erased by the five-minute automation cycle.
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

def main():
    now = datetime.now(timezone.utc).isoformat()
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            task_id = str(row.get("task_id", ""))
            if task_id:
                existing[task_id] = row

    rows, preserved, created = [], 0, 0
    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = str(task["task_id"])
        expected_hash = task_hash(task)
        prior = existing.get(task_id)
        if prior and (prior.get("audit") or {}).get("record_hash") == expected_hash:
            rows.append(prior)
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
            "audit": {"recorded_at": "", "record_hash": expected_hash},
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
        "preserved_reviews": preserved,
        "new_pending_reviews": created,
        "verified_records": sum(1 for x in rows if x.get("verification_status") == "VERIFIED"),
        "fail_closed": True
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
