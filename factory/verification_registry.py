#!/usr/bin/env python3
"""Build a fail-closed durable registry for independent verification reviews.

Queue membership is not verification. This registry records review state and
only permits promotion when explicit independent evidence, countercase review,
reviewer/audit metadata, and reproducible checks are present.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def task_id_for(claim_id):
    return "verify:" + hashlib.sha256(claim_id.encode("utf-8")).hexdigest()[:24]

def build():
    queue = OUT / "independent-verification-queue.jsonl"
    if not queue.exists():
        raise SystemExit("independent-verification-queue.jsonl is missing")
    records = []
    now = datetime.now(timezone.utc).isoformat()
    for line in queue.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        task = json.loads(line)
        records.append({
            "task_id": task["task_id"],
            "claim_id": task["claim_id"],
            "review_status": "PENDING_REVIEW",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "independent_evidence": [],
            "countercase_review": {
                "status": "NOT_REVIEWED",
                "findings": []
            },
            "reproducibility": {
                "status": "NOT_TESTED",
                "test_reference": None
            },
            "reviewer": {
                "identity": None,
                "role": None,
                "reviewed_at": None
            },
            "audit": {
                "record_id": None,
                "review_notes": None
            },
            "created_at": now,
            "promotion_policy": "VERIFIED requires explicit independent evidence, countercase review, reproducibility where applicable, reviewer identity/audit record, and an explicit promotion decision."
        })
    out = OUT / "independent-verification-registry.jsonl"
    out.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in records) + ("\n" if records else ""), encoding="utf-8")
    summary = {
        "version": 1,
        "records": len(records),
        "pending_review": len(records),
        "verified": 0,
        "publication_gate": "CHECK" if records else "BLOCK",
        "auto_promotion": False,
        "verification_policy": "Queue and registry records never constitute verification."
    }
    (OUT / "VERIFICATION-REGISTRY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    build()
