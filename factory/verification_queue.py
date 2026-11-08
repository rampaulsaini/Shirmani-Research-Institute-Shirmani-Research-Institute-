#!/usr/bin/env python3
"""Build a deterministic independent-verification queue from its authoritative registry.

The queue creates review tasks only for records in
`generated/independent-verification-records.json`. It never marks a claim
verified and never treats provenance or source traceability as proof.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"


def build():
    source = OUT / "independent-verification-records.json"
    if not source.is_file():
        raise SystemExit("independent-verification-records.json is missing")
    data = json.loads(source.read_text(encoding="utf-8"))
    records = data.get("records") if isinstance(data, dict) else None
    if not isinstance(records, list) or not records:
        raise SystemExit("authoritative independent-verification records are empty or invalid")

    tasks = []
    now = datetime.now(timezone.utc).isoformat()
    seen = set()
    for line_no, record in enumerate(records, 1):
        if not isinstance(record, dict):
            raise SystemExit(f"authoritative record {line_no} is not an object")
        claim_id = str(record.get("id", "")).strip()
        if not claim_id or claim_id in seen:
            raise SystemExit(f"authoritative record {line_no} has a missing or duplicate id")
        seen.add(claim_id)

        evidence = record.get("evidence") or {}
        sources = evidence.get("sources") if isinstance(evidence, dict) else None
        if not isinstance(sources, list) or not all(isinstance(x, str) and x.strip() for x in sources):
            raise SystemExit(f"authoritative record {claim_id} has invalid evidence.sources")
        source_ids = sources
        source_status = str(record.get("source_status") or record.get("status") or "UNKNOWN")
        questions = record.get("verification_questions") or [
            "Can the claim be independently supported by an appropriate primary or authoritative source?",
            "Can an independent reviewer reproduce the stated formulation or test?",
            "Are there credible counterexamples or contradictory sources?"
        ]
        task = {
            "task_id": f"{claim_id}-independent-review-v1",
            "claim_id": claim_id,
            "source_ids": source_ids,
            "source_status": source_status,
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
            "generator": "factory/verification_queue.py"
        }
        tasks.append(task)

    out = OUT / "independent-verification-queue.jsonl"
    out.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in tasks) +
        ("\n" if tasks else ""), encoding="utf-8"
    )
    summary = {
        "version": 2,
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
