#!/usr/bin/env python3
"""Bootstrap a deterministic independent-verification queue.

Existing tasks are preserved when their claim_id/task_id remains present.
New claims receive a task once. This prevents scheduled bootstrapping from
invalidating prior review/audit hashes. This tool never creates VERIFIED.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/independent-verification-queue.jsonl"

def sha256_obj(obj):
    return hashlib.sha256(
        json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def load_existing():
    if not OUT.exists():
        return {}
    existing = {}
    for line in OUT.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        existing[str(row.get("claim_id") or row.get("task_id"))] = row
    return existing

def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    records = data.get("records", [])
    existing = load_existing()
    now = datetime.now(timezone.utc).isoformat()
    rows = []
    new_tasks = 0

    for r in records:
        rid = str(r["id"])
        task_id = f"{rid}-independent-review-v1"
        old = existing.get(rid)
        if old and old.get("task_id") == task_id:
            rows.append(old)
            continue

        sources = list((r.get("evidence") or {}).get("sources") or [])
        task = {
            "task_id": task_id,
            "claim_id": rid,
            "source_ids": sources,
            "verification_questions": [
                "What observation would falsify or materially weaken this claim?",
                "Can an independent reviewer reproduce the stated result from the cited evidence or test?",
                "What credible counter-evidence must be considered before a decision?"
            ],
            "required_evidence": [
                "precise operational definition",
                "independent source or reproducible test",
                "reproducible result and artifacts",
                "counter-evidence review",
                "reviewer identity and role",
                "review timestamp and audit hash"
            ],
            "status": "QUEUED",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "created_at": now,
            "generator": "factory/bootstrap_independent_verification_queue.py"
        }
        task["task_sha256"] = sha256_obj(task)
        rows.append(task)
        new_tasks += 1

    OUT.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows),
        encoding="utf-8"
    )
    print(json.dumps({
        "queue_records": len(rows),
        "new_tasks": new_tasks,
        "verified_records": 0,
        "fail_closed": True
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
