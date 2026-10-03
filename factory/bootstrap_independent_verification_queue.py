#!/usr/bin/env python3
"""Bootstrap a deterministic independent-verification queue from the authoritative record registry.

This creates review tasks only. It never creates a VERIFIED decision.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/independent-verification-queue.jsonl"

def sha256_obj(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    records = data.get("records", [])
    # Preserve task timestamps and hashes across five-minute cycles so an
    # existing review remains bound to the same immutable task.
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                task = json.loads(line)
                existing[str(task.get("task_id", ""))] = task

    now = datetime.now(timezone.utc).isoformat()
    rows = []
    for r in records:
        rid = str(r["id"])
        task_id = f"{rid}-independent-review-v1"
        sources = list((r.get("evidence") or {}).get("sources") or [])
        source_status = str(r.get("source_status") or r.get("status") or "UNKNOWN")
        if task_id in existing:
            # Reconcile routing metadata while preserving any human review state.
            task = dict(existing[task_id])
            if task.get("status") not in {"REVIEWED", "VERIFIED"}:
                task["source_ids"] = sources
                task["source_status"] = source_status
                task["required_evidence"] = [
                    "precise claim text",
                    "operational definition",
                    "independent source or reproducible test",
                    "counter-evidence review",
                    "reviewer identity and role",
                    "timestamp",
                    "explicit decision"
                ]
            rows.append(task)
            continue
        task = {
            "task_id": task_id,
            "claim_id": rid,
            "source_ids": sources,
            "source_status": source_status,
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
    OUT.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows), encoding="utf-8")
    print(json.dumps({"queue_records": len(rows), "verified_records": 0, "fail_closed": True}, ensure_ascii=False))

if __name__ == "__main__":
    main()
