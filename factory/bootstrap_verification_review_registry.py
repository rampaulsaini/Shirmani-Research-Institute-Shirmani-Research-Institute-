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
    stable = {k: v for k, v in task.items() if k not in {"created_at", "task_sha256"}}
    return hashlib.sha256(json.dumps(stable, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

def main():
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("task_id"):
                    existing[str(row["task_id"])] = row

    rows = []
    now = datetime.now(timezone.utc).isoformat()
    preserved = 0
    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        tid = str(task["task_id"])
        old = existing.get(tid)
        if old and old.get("audit", {}).get("record_hash") == task_hash(task):
            row = old
            preserved += 1
        else:
            row = {
                "review_id": "REVIEW-" + tid,
                "task_id": tid,
                "claim_id": task["claim_id"],
                "stage": "PENDING_REVIEW",
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
                "created_at": old.get("created_at", now) if old else now,
                "generator": "factory/bootstrap_verification_review_registry.py"
            }
        row.setdefault("audit", {})["record_hash"] = task_hash(task)
        rows.append(row)
    OUT.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows), encoding="utf-8")
    print(json.dumps({"review_slots": len(rows), "verified_records": sum(1 for r in rows if str(r.get("verification_status","")).upper() in {"VERIFIED","INDEPENDENT_VERIFIED"}), "fail_closed": True, "preserved_reviews": preserved}, ensure_ascii=False))

if __name__ == "__main__":
    main()
