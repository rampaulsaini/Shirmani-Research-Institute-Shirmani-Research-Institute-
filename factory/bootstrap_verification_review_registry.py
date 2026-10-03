#!/usr/bin/env python3
"""Create pending review slots bound to the exact current verification queue.

Pending review slots are not verification decisions.
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

def main():
    # Preserve existing review decisions. The five-minute automation cycle may
    # add missing review slots, but it must never erase an independent review
    # that has already been recorded.
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            task_id = str(record.get("task_id", ""))
            if task_id:
                existing[task_id] = record

    rows = []
    now = datetime.now(timezone.utc).isoformat()
    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = str(task["task_id"])
        if task_id in existing:
            record = existing[task_id]
            record.setdefault("audit", {})["record_hash"] = task_hash(task)
            rows.append(record)
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
    print(json.dumps({"review_slots": len(rows), "verified_records": 0, "fail_closed": True}, ensure_ascii=False))

if __name__ == "__main__":
    main()
