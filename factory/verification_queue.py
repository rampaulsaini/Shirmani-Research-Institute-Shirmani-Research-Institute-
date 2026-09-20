#!/usr/bin/env python3
"""Build a deterministic independent-verification queue.

The queue creates review tasks from claim/evidence records. It never marks a
claim verified and never treats provenance or source traceability as proof.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def sha(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def build():
    source = OUT / "claim-evidence.jsonl"
    if not source.exists():
        raise SystemExit("claim-evidence.jsonl is missing")
    tasks = []
    now = datetime.now(timezone.utc).isoformat()
    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        claim_id = str(record.get("id", ""))
        verification = record.get("verification") or {}
        questions = record.get("verification_questions") or [
            "Can the claim be independently supported by an appropriate primary or authoritative source?",
            "Can an independent reviewer reproduce the stated formulation or test?",
            "Are there credible counterexamples or contradictory sources?"
        ]
        source_ids = [str(x) for x in (record.get("source_traceability") or {}).get("source_ids", [])]
        task = {
            "task_id": "verify:" + sha(claim_id)[:24],
            "claim_id": claim_id,
            "source_ids": source_ids,
            "verification_questions": questions,
            "required_evidence": [
                "independent_source_or_reproducible_test",
                "explicit_countercase_review",
                "reviewer_identity_or_audit_record"
            ],
            "status": "QUEUED",
            "verification_status": "NOT_VERIFIED",
            "independent": False,
            "created_at": now,
            "generator": "factory/verification_queue.py",
            "claim_verification_status": verification.get("status", "NOT_VERIFIED")
        }
        tasks.append(task)
    out = OUT / "independent-verification-queue.jsonl"
    out.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in tasks) +
        ("\n" if tasks else ""), encoding="utf-8"
    )
    summary = {
        "version": 1,
        "records": len(tasks),
        "queued": len(tasks),
        "publication_gate": "CHECK" if tasks else "BLOCK",
        "verification_policy": "No task may be auto-promoted to verified by this factory."
    }
    (OUT / "VERIFICATION-QUEUE.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    build()
