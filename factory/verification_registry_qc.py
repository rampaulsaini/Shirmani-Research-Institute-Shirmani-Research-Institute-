#!/usr/bin/env python3
"""Fail-closed structural QC for independent verification review records.

The registry is durable state. QUEUED records are the initial fail-closed state;
REVIEWED/VERIFIED records are allowed only when the corresponding human-review
fields are internally coherent. This validator never creates verification data.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def task_hash(task):
    return hashlib.sha256(
        json.dumps(task, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()

def main():
    queue = OUT / "independent-verification-queue.jsonl"
    registry = OUT / "independent-verification-registry.jsonl"
    if not queue.exists() or not registry.exists():
        raise SystemExit("verification queue or registry is missing")

    queue_records = {}
    errors = []
    for n, line in enumerate(queue.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            task = json.loads(line)
        except Exception as exc:
            errors.append({"source": "queue", "line": n, "error": "invalid_json:" + str(exc)})
            continue
        task_id = str(task.get("task_id", ""))
        if not task_id or task_id in queue_records:
            errors.append({"source": "queue", "line": n, "error": "missing_or_duplicate_task_id"})
            continue
        queue_records[task_id] = task

    seen = set()
    count = 0
    state_counts = {"QUEUED": 0, "REVIEWED": 0, "OTHER": 0}
    required = (
        "review_id","task_id","claim_id","status","verification_status","independent",
        "reviewer","reviewer_role","reviewed_at","evidence_references",
        "countercase_review","reproduction_or_test","audit","created_at","generator"
    )

    for n, line in enumerate(registry.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        count += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append({"source": "registry", "line": n, "error": "invalid_json:" + str(exc)})
            continue

        for key in required:
            if key not in r:
                errors.append({"line": n, "error": "missing:" + key})

        rid = r.get("review_id")
        if not rid or rid in seen:
            errors.append({"line": n, "error": "missing_or_duplicate_review_id"})
        seen.add(rid)

        task_id = str(r.get("task_id", ""))
        task = queue_records.get(task_id)
        if task is None:
            errors.append({"line": n, "error": "task_not_in_queue"})
            continue

        if str(r.get("claim_id", "")) != str(task.get("claim_id", "")):
            errors.append({"line": n, "error": "claim_id_mismatch"})

        audit = r.get("audit") or {}
        if audit.get("record_hash") != task_hash(task):
            errors.append({"line": n, "error": "task_hash_mismatch"})
        if not audit.get("recorded_at"):
            errors.append({"line": n, "error": "audit_metadata_missing_recorded_at"})

        status = r.get("status")
        verification = r.get("verification_status")

        if status == "QUEUED":
            state_counts["QUEUED"] += 1
            if verification != "NOT_VERIFIED":
                errors.append({"line": n, "error": "queued_record_must_be_not_verified"})
            if r.get("independent") is not False:
                errors.append({"line": n, "error": "queued_record_must_not_be_independent"})
            if any(r.get(k) is not None for k in ("reviewer","reviewer_role","reviewed_at")):
                errors.append({"line": n, "error": "queued_record_contains_reviewer_metadata"})
            if r.get("evidence_references") != []:
                errors.append({"line": n, "error": "queued_record_contains_evidence"})
            if (r.get("countercase_review") or {}).get("status") != "NOT_REVIEWED":
                errors.append({"line": n, "error": "queued_countercase_not_fail_closed"})
            if (r.get("reproduction_or_test") or {}).get("status") != "NOT_RUN":
                errors.append({"line": n, "error": "queued_reproduction_not_fail_closed"})

        elif status == "REVIEWED":
            state_counts["REVIEWED"] += 1
            if verification not in {"NOT_VERIFIED", "VERIFIED"}:
                errors.append({"line": n, "error": "invalid_reviewed_verification_status"})
            if not isinstance(r.get("reviewer"), str) or not r["reviewer"].strip():
                errors.append({"line": n, "error": "reviewed_record_missing_reviewer"})
            if not isinstance(r.get("reviewer_role"), str) or not r["reviewer_role"].strip():
                errors.append({"line": n, "error": "reviewed_record_missing_reviewer_role"})
            if not r.get("reviewed_at"):
                errors.append({"line": n, "error": "reviewed_record_missing_reviewed_at"})
            if r.get("independent") is not True:
                errors.append({"line": n, "error": "reviewed_record_must_be_independent"})
            if not isinstance(r.get("evidence_references"), list) or not r["evidence_references"]:
                errors.append({"line": n, "error": "reviewed_record_missing_evidence"})
            cc = r.get("countercase_review") or {}
            if cc.get("status") != "REVIEWED" or not isinstance(cc.get("references"), list) or not cc["references"]:
                errors.append({"line": n, "error": "reviewed_record_missing_countercase_review"})
            rt = r.get("reproduction_or_test") or {}
            if rt.get("status") not in {"PASSED", "SUPPORTED", "NOT_APPLICABLE_WITH_REASON"}:
                errors.append({"line": n, "error": "reviewed_record_missing_test_state"})
            if not isinstance(rt.get("references"), list) or not rt["references"]:
                errors.append({"line": n, "error": "reviewed_record_missing_test_references"})

        else:
            state_counts["OTHER"] += 1
            errors.append({"line": n, "error": "unsupported_review_status:" + str(status)})

        if verification == "VERIFIED" and status != "REVIEWED":
            errors.append({"line": n, "error": "verified_requires_reviewed_status"})

    registry_task_ids = set()
    for line in registry.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                registry_task_ids.add(str(json.loads(line).get("task_id", "")))
            except Exception:
                pass
    orphan_count = len(set(queue_records) - registry_task_ids)
    if count != len(queue_records):
        errors.append({"error":"registry_queue_count_mismatch","queue":len(queue_records),"registry":count})

    report = {
        "version": 2,
        "records": count,
        "unique_reviews": len(seen),
        "queue_records": len(queue_records),
        "orphan_queue_tasks": orphan_count,
        "state_counts": state_counts,
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "policy": "Registry QC validates durable review state without creating reviewer, evidence, test, or verification data. Promotion remains fail-closed.",
        "errors": errors,
    }
    (OUT / "VERIFICATION-REGISTRY-QC.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
