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
    stable = {k: v for k, v in obj.items() if k not in {"created_at", "task_sha256"}}
    return hashlib.sha256(json.dumps(stable, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    records = data.get("records", [])
    now = datetime.now(timezone.utc).isoformat()
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("task_id"):
                    existing[str(row["task_id"])] = row

    rows = []
    for r in records:
        rid = str(r["id"])
        sources = list((r.get("evidence") or {}).get("sources") or [])
        task = {
            "task_id": f"{rid}-independent-review-v1",
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
        old = existing.get(str(task["task_id"]))
        task["created_at"] = old.get("created_at", now) if old else now
        task["task_sha256"] = sha256_obj(task)
        rows.append(task)
    OUT.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows), encoding="utf-8")
    print(json.dumps({"queue_records": len(rows), "verified_records": 0, "fail_closed": True, "preserved_queue_entries": sum(1 for r in rows if r["task_id"] in existing)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
