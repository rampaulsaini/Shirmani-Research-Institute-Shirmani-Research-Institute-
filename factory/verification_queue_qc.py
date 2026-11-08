#!/usr/bin/env python3
"""Fail-closed QC for the dedicated independent-verification queue.

This queue is bootstrapped from generated/independent-verification-records.json.
It is a separate ledger from the large claim-evidence.jsonl production pipeline.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"


def validate(records_path: Path, queue_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    errors: list[dict[str, Any]] = []
    if not records_path.is_file():
        return ({"version": 2, "records": 0, "queue_records": 0,
                 "error_count": 1, "publication_gate": "BLOCK"},
                [{"error": "authoritative_verification_records_missing"}])
    if not queue_path.is_file():
        return ({"version": 2, "records": 0, "queue_records": 0,
                 "error_count": 1, "publication_gate": "BLOCK"},
                [{"error": "verification_queue_missing"}])

    try:
        source = json.loads(records_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return ({"version": 2, "records": 0, "queue_records": 0,
                 "error_count": 1, "publication_gate": "BLOCK"},
                [{"error": "invalid_authoritative_records_json:" + str(exc)}])

    source_rows = source.get("records") if isinstance(source, dict) else None
    if not isinstance(source_rows, list) or not source_rows:
        errors.append({"error": "authoritative_records_empty_or_invalid"})
        source_rows = []

    expected: dict[str, dict[str, Any]] = {}
    for n, row in enumerate(source_rows, 1):
        if not isinstance(row, dict):
            errors.append({"line": n, "error": "source_record_not_object"})
            continue
        claim_id = str(row.get("id", "")).strip()
        if not claim_id:
            errors.append({"line": n, "error": "source_record_missing_id"})
            continue
        if claim_id in expected:
            errors.append({"line": n, "error": "duplicate_source_claim_id"})
            continue
        evidence = row.get("evidence") or {}
        sources = evidence.get("sources") if isinstance(evidence, dict) else None
        if not isinstance(sources, list) or not all(isinstance(x, str) and x.strip() for x in sources):
            errors.append({"line": n, "error": "source_evidence_sources_invalid"})
            sources = []
        expected[claim_id] = {
            "source_ids": sources,
            "source_status": str(row.get("source_status") or row.get("status") or "UNKNOWN"),
        }

    seen_tasks: set[str] = set()
    seen_claims: set[str] = set()
    queue_records = 0
    try:
        lines = queue_path.read_text(encoding="utf-8").splitlines()
    except Exception as exc:
        lines = []
        errors.append({"error": "verification_queue_read_failed:" + str(exc)})

    required = (
        "task_id", "claim_id", "source_ids", "verification_questions",
        "required_evidence", "status", "verification_status", "independent",
        "created_at", "generator",
    )
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        queue_records += 1
        try:
            task = json.loads(line)
        except Exception as exc:
            errors.append({"line": n, "error": "invalid_queue_json:" + str(exc)})
            continue
        if not isinstance(task, dict):
            errors.append({"line": n, "error": "queue_record_not_object"})
            continue

        for key in required:
            if key not in task:
                errors.append({"line": n, "error": "missing:" + key})

        claim_id = str(task.get("claim_id", "")).strip()
        task_id = str(task.get("task_id", "")).strip()
        if not task_id:
            errors.append({"line": n, "error": "missing_task_id"})
        elif task_id in seen_tasks:
            errors.append({"line": n, "error": "duplicate_task_id"})
        seen_tasks.add(task_id)

        if not claim_id:
            errors.append({"line": n, "error": "missing_claim_id"})
        elif claim_id in seen_claims:
            errors.append({"line": n, "error": "duplicate_claim_id"})
        seen_claims.add(claim_id)

        source_record = expected.get(claim_id)
        if source_record is None:
            errors.append({"line": n, "error": "claim_id_not_in_authoritative_records"})
        else:
            if task_id != f"{claim_id}-independent-review-v1":
                errors.append({"line": n, "error": "task_id_claim_binding_mismatch"})
            if task.get("source_ids") != source_record["source_ids"]:
                errors.append({"line": n, "error": "source_ids_do_not_match_authoritative_record"})
            if task.get("source_status") != source_record["source_status"]:
                errors.append({"line": n, "error": "source_status_mismatch"})

        status = task.get("status")
        verification_status = task.get("verification_status")
        independent = task.get("independent")
        if status not in {"QUEUED", "REVIEWED", "VERIFIED"}:
            errors.append({"line": n, "error": "invalid_queue_status"})
        if verification_status not in {"NOT_VERIFIED", "VERIFIED"}:
            errors.append({"line": n, "error": "invalid_verification_status"})
        if status == "QUEUED" and (verification_status != "NOT_VERIFIED" or independent is not False):
            errors.append({"line": n, "error": "queued_task_must_remain_unverified_and_not_independent"})
        if verification_status == "VERIFIED" and (status not in {"REVIEWED", "VERIFIED"} or independent is not True):
            errors.append({"line": n, "error": "verified_task_missing_independent_review_state"})
        if status == "VERIFIED" and verification_status != "VERIFIED":
            errors.append({"line": n, "error": "verified_queue_status_without_verified_decision"})
        if not isinstance(task.get("source_ids"), list):
            errors.append({"line": n, "error": "source_ids_not_list"})
        if not isinstance(task.get("verification_questions"), list) or not task.get("verification_questions"):
            errors.append({"line": n, "error": "missing_verification_questions"})
        if not isinstance(task.get("required_evidence"), list) or not task.get("required_evidence"):
            errors.append({"line": n, "error": "missing_required_evidence"})
        if not task.get("created_at") or not task.get("generator"):
            errors.append({"line": n, "error": "queue_provenance_missing"})

    missing_claims = sorted(set(expected) - seen_claims)
    if missing_claims:
        errors.append({"error": "authoritative_claims_missing_from_queue",
                       "count": len(missing_claims), "claim_ids": missing_claims})
    unexpected_claims = sorted(seen_claims - set(expected))
    if unexpected_claims:
        errors.append({"error": "unexpected_queue_claims",
                       "count": len(unexpected_claims), "claim_ids": unexpected_claims})

    report = {
        "version": 2,
        "records": len(expected),
        "queue_records": queue_records,
        "unique_tasks": len(seen_tasks),
        "unique_claims": len(seen_claims),
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "verification_policy": "Queue structure and provenance are checked against authoritative records; VERIFIED queue states require independent review markers and remain subject to the separate promotion gate.",
    }
    return report, errors


def main() -> None:
    report, errors = validate(
        OUT / "independent-verification-records.json",
        OUT / "independent-verification-queue.jsonl",
    )
    (OUT / "VERIFICATION-QUEUE-QC.json").write_text(
        json.dumps({**report, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
