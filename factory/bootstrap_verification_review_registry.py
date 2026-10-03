#!/usr/bin/env python3
"""Maintain pending review slots without destroying completed independent reviews.

Pending review slots are not verification decisions. Existing review records are
preserved verbatim so an independent review can survive every 5-minute conveyor cycle.
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
        json.dumps(task, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

def load_jsonl(path):
    if not path.exists():
        return []
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            rows.append(json.loads(line))
    return rows

def main():
    queue = load_jsonl(QUEUE)
    existing = {str(r.get("task_id")): r for r in load_jsonl(OUT) if r.get("task_id")}
    rows = []
    now = datetime.now(timezone.utc).isoformat()

    for task in queue:
        task_id = str(task["task_id"])
        current = existing.get(task_id)

        # Preserve an existing review exactly when its task is unchanged.
        if current and current.get("audit", {}).get("record_hash") == task_hash(task):
            rows.append(current)
            continue

        # A changed task gets a fresh pending slot; old review data must not
        # silently transfer to a different task definition.
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

    OUT.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows),
        encoding="utf-8"
    )
    verified = sum(1 for r in rows if r.get("verification_status") == "VERIFIED")
    print(json.dumps({
        "review_slots": len(rows),
        "preserved_reviews": sum(1 for r in rows if r.get("status") == "REVIEWED"),
        "verified_records": verified,
        "fail_closed": True
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
