#!/usr/bin/env python3
"""Build a fail-closed independent-review readiness queue.

This tool may prepare records for an independent reviewer.
It never changes reviewer decisions and never declares VERIFIED.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/independent-review-readiness.json"
TARGET = 100200
REQUIRED = ("id", "claim", "evidence", "independent_test", "reproducibility",
            "counter_evidence", "audit", "reviewer_decision")

def main() -> int:
    if not SOURCE.exists():
        raise SystemExit("Missing independent verification registry")
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    records = data.get("records")
    if not isinstance(records, list):
        raise SystemExit("records must be a list")

    ready, blocked = [], []
    for r in records:
        missing = [k for k in REQUIRED if k not in r]
        sources = r.get("evidence", {}).get("sources", [])
        evidence_hash = r.get("evidence", {}).get("evidence_hash")
        reviewer = r.get("reviewer_decision", {}).get("decision")
        if missing:
            blocked.append({"id": r.get("id"), "reason": "MISSING_FIELDS", "fields": missing})
        elif not sources or evidence_hash in (None, "", "PENDING_EVIDENCE_HASH"):
            blocked.append({"id": r["id"], "reason": "EVIDENCE_NOT_READY"})
        elif reviewer != "PENDING":
            blocked.append({"id": r["id"], "reason": "REVIEW_STATE_NOT_PENDING"})
        else:
            ready.append({
                "id": r["id"],
                "claim": r["claim"],
                "evidence_sources": sources,
                "evidence_hash": evidence_hash,
                "independent_test_protocol": r["independent_test"].get("protocol"),
                "required_reviewer_outputs": [
                    "independent_test_result", "counter_evidence_review",
                    "reproducibility_result", "reviewer_provenance",
                    "timestamp", "audit_id"
                ]
            })

    if len(ready) + len(blocked) != len(records):
        raise SystemExit("READINESS_PARTITION_MISMATCH")

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": "fail-closed readiness partition from authoritative registry",
        "target": TARGET,
        "registry_records": len(records),
        "review_ready": len(ready),
        "blocked": len(blocked),
        "independently_verified": sum(
            1 for r in records
            if r.get("reviewer_decision", {}).get("decision") == "VERIFIED"
            and r.get("status") == "VERIFIED"
        ),
        "automation_state": {
            "may_prepare_review_queue": True,
            "may_declare_verified": False,
            "independent_reviewer_required": True
        },
        "review_ready_records": ready,
        "blocked_records": blocked
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
