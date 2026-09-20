#!/usr/bin/env python3
"""Fail-closed QC and promotion gate for independent verification registry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

ALLOWED_REVIEW = {"PENDING_REVIEW", "IN_REVIEW", "REVIEWED"}
ALLOWED_VERIFY = {"NOT_VERIFIED", "VERIFIED"}

def main():
    queue = OUT / "independent-verification-queue.jsonl"
    registry = OUT / "independent-verification-registry.jsonl"
    if not queue.exists() or not registry.exists():
        raise SystemExit("verification queue or registry is missing")
    task_ids = set()
    for line in queue.read_text(encoding="utf-8").splitlines():
        if line.strip():
            task_ids.add(str(json.loads(line).get("task_id", "")))
    seen = set()
    errors = []
    verified = 0
    records = 0
    for n, line in enumerate(registry.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append({"line": n, "error": "invalid_json:" + str(exc)})
            continue
        tid = str(r.get("task_id", ""))
        if tid in seen:
            errors.append({"line": n, "error": "duplicate_task_id"})
        seen.add(tid)
        if tid not in task_ids:
            errors.append({"line": n, "error": "task_id_not_in_queue"})
        if r.get("review_status") not in ALLOWED_REVIEW:
            errors.append({"line": n, "error": "invalid_review_status"})
        if r.get("verification_status") not in ALLOWED_VERIFY:
            errors.append({"line": n, "error": "invalid_verification_status"})
        if r.get("verification_status") == "VERIFIED":
            verified += 1
            ev = r.get("independent_evidence")
            counter = r.get("countercase_review") or {}
            repro = r.get("reproducibility") or {}
            reviewer = r.get("reviewer") or {}
            audit = r.get("audit") or {}
            if r.get("independent") is not True:
                errors.append({"line": n, "error": "verified_requires_independent_true"})
            if not isinstance(ev, list) or not ev:
                errors.append({"line": n, "error": "verified_requires_independent_evidence"})
            if counter.get("status") != "REVIEWED":
                errors.append({"line": n, "error": "verified_requires_countercase_review"})
            if repro.get("status") not in {"REPRODUCED", "NOT_APPLICABLE"}:
                errors.append({"line": n, "error": "verified_requires_reproducibility"})
            if not reviewer.get("identity") or not reviewer.get("reviewed_at"):
                errors.append({"line": n, "error": "verified_requires_reviewer_audit_identity"})
            if not audit.get("record_id"):
                errors.append({"line": n, "error": "verified_requires_audit_record"})
    if records != len(task_ids):
        errors.append({"error": "registry_queue_count_mismatch", "queue": len(task_ids), "registry": records})
    # A clean registry is not itself proof that claims are verified; it only
    # proves the registry obeys the promotion contract.
    report = {
        "version": 1,
        "records": records,
        "unique_tasks": len(seen),
        "queue_tasks": len(task_ids),
        "verified_records": verified,
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "verification_gate": "CHECK" if not errors and verified == 0 else ("PASS" if not errors else "BLOCK"),
        "note": "PASS means the registry contract is valid; it does not independently validate the claims."
    }
    (OUT / "VERIFICATION-REGISTRY-QC.json").write_text(json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
