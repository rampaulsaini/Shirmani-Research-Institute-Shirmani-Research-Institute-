#!/usr/bin/env python3
"""Build durable human-review records from the independent verification queue.

This creates review slots only. It never fabricates a reviewer, evidence, or
VERIFIED status.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def sha(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def main():
    queue = OUT / "independent-verification-queue.jsonl"
    if not queue.exists():
        raise SystemExit("independent-verification-queue.jsonl is missing")
    now = datetime.now(timezone.utc).isoformat()
    records = []
    for line in queue.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        task_id = str(task["task_id"])
        records.append({
            "review_id": "review:" + sha(task_id)[:24],
            "task_id": task_id,
            "claim_id": str(task["claim_id"]),
            "status": "QUEUED",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "reviewer": None,
            "reviewer_role": None,
            "reviewed_at": None,
            "evidence_references": [],
            "countercase_review": {
                "status": "NOT_REVIEWED",
                "references": []
            },
            "reproduction_or_test": {
                "status": "NOT_RUN",
                "references": []
            },
            "audit": {
                "recorded_at": now,
                "record_hash": sha(json.dumps(task, ensure_ascii=False, sort_keys=True))
            },
            "created_at": now,
            "generator": "factory/verification_registry.py"
        })
    out = OUT / "independent-verification-registry.jsonl"
    out.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in records) +
        ("\n" if records else ""), encoding="utf-8"
    )
    summary = {
        "version": 1,
        "records": len(records),
        "queued": len(records),
        "verified": 0,
        "promotion_gate": "CHECK" if records else "BLOCK",
        "policy": "Review records are durable slots; no reviewer/evidence/verification is invented."
    }
    (OUT / "VERIFICATION-REGISTRY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
