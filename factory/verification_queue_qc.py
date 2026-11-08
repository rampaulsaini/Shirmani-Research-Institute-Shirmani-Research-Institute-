#!/usr/bin/env python3
"""Fail-closed QC for the independent verification queue."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def main():
    claims = OUT / "claim-evidence.jsonl"
    queue = OUT / "independent-verification-queue.jsonl"
    if not claims.exists() or not queue.exists():
        raise SystemExit("claim-evidence or verification queue is missing")
    claim_ids = set()
    for line in claims.read_text(encoding="utf-8").splitlines():
        if line.strip():
            claim_ids.add(str(json.loads(line).get("id", "")))
    seen = set()
    errors = []
    records = 0
    for n, line in enumerate(queue.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append({"line": n, "error": "invalid_json:" + str(exc)})
            continue
        for key in ("task_id","claim_id","source_ids","verification_questions",
                    "required_evidence","status","verification_status",
                    "independent","created_at","generator"):
            if key not in r:
                errors.append({"line": n, "error": "missing:" + key})
        tid = r.get("task_id")
        cid = str(r.get("claim_id",""))
        if tid in seen:
            errors.append({"line": n, "error": "duplicate_task_id"})
        seen.add(tid)
        if cid not in claim_ids:
            errors.append({"line": n, "error": "claim_id_not_in_claim_evidence"})
        if r.get("status") != "QUEUED":
            errors.append({"line": n, "error": "invalid_queue_status"})
        if r.get("verification_status") != "NOT_VERIFIED":
            errors.append({"line": n, "error": "verification_not_fail_closed"})
        if r.get("independent") is not False:
            errors.append({"line": n, "error": "independent_must_be_false"})
        if not isinstance(r.get("source_ids"), list):
            errors.append({"line": n, "error": "source_ids_not_list"})
        if not isinstance(r.get("verification_questions"), list) or not r.get("verification_questions"):
            errors.append({"line": n, "error": "missing_verification_questions"})
        if not isinstance(r.get("required_evidence"), list) or not r.get("required_evidence"):
            errors.append({"line": n, "error": "missing_required_evidence"})
    if records != len(claim_ids):
        errors.append({"error": "queue_claim_count_mismatch", "claims": len(claim_ids), "queue": records})
    report = {
        "version": 1,
        "records": records,
        "unique_tasks": len(seen),
        "claim_records": len(claim_ids),
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK"
    }
    (OUT / "VERIFICATION-QUEUE-QC.json").write_text(
        json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
