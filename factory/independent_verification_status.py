#!/usr/bin/env python3
"""Build fail-closed independent-verification telemetry.

Preparation, packet creation, and workflow success are never verification.
A record counts as VERIFIED only when its registry status is REVIEWED, its
verification_status is VERIFIED, and independent is explicitly true.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

RANGE_RE = re.compile(r"^verification-review-packet-(\d{6})-(\d{6})\.json$")
VERIFIED_LABELS = {"VERIFIED", "INDEPENDENTLY_VERIFIED"}
REVIEW_LABELS = {"REVIEW", "UNDER_REVIEW", "CHECKED"}
UNVERIFIED_LABELS = {
    "UNVERIFIED", "NOT_VERIFIED", "PENDING", "READY_FOR_HUMAN_REVIEW"
}


def read_jsonl_gz(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at {path.name}:{line_number}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"non-object record at {path.name}:{line_number}")
            yield record


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_status(generated: Path) -> dict:
    queue_path = generated / "independent-verification-queue.jsonl.gz"
    registry_path = generated / "independent-verification-registry.jsonl.gz"
    if not queue_path.is_file() or not registry_path.is_file():
        raise ValueError("independent verification queue/registry is missing")

    queue_ids = []
    for record in read_jsonl_gz(queue_path):
        task_id = str(record.get("task_id", "")).strip()
        if not task_id:
            raise ValueError("verification queue contains a missing task_id")
        queue_ids.append(task_id)
    if len(queue_ids) != len(set(queue_ids)):
        raise ValueError("verification queue contains duplicate task_id values")

    registry_ids = []
    verified = review = unverified = blocked = other = 0
    for record in read_jsonl_gz(registry_path):
        task_id = str(record.get("task_id", "")).strip()
        if not task_id:
            raise ValueError("verification registry contains a missing task_id")
        registry_ids.append(task_id)
        verification_status = str(record.get("verification_status", "")).strip().upper()
        record_status = str(record.get("status", "")).strip().upper()
        is_verified = (
            record_status == "REVIEWED"
            and verification_status == "VERIFIED"
            and record.get("independent") is True
        )
        if record_status == "REVIEWED" or verification_status in REVIEW_LABELS:
            review += 1
        if is_verified:
            verified += 1
        elif verification_status in UNVERIFIED_LABELS or verification_status in VERIFIED_LABELS:
            # A VERIFIED label without the required review/independence fields
            # is deliberately kept unverified.
            unverified += 1
        elif verification_status == "BLOCKED":
            blocked += 1
        else:
            other += 1

    if len(registry_ids) != len(set(registry_ids)):
        raise ValueError("verification registry contains duplicate task_id values")
    if set(queue_ids) != set(registry_ids):
        raise ValueError("verification queue and registry task_id sets do not match")
    if verified > review:
        raise ValueError("verified records cannot exceed reviewed records")

    prepared_ranges = []
    for path in generated.glob("verification-review-packet-*.json"):
        match = RANGE_RE.fullmatch(path.name)
        if not match:
            continue
        start, end = map(int, match.groups())
        if start < 1 or end < start or end > len(queue_ids):
            raise ValueError(f"review packet range is outside queue bounds: {path.name}")
        try:
            packet = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"invalid review packet {path.name}: {exc}") from exc
        if not isinstance(packet, dict):
            raise ValueError(f"review packet must be a JSON object: {path.name}")
        if packet.get("status") == "READY_FOR_HUMAN_REVIEW":
            prepared_ranges.append([start, end])

    prepared_ranges.sort()
    prepared_records = 0
    previous_end = 0
    for start, end in prepared_ranges:
        if start <= previous_end:
            raise ValueError("prepared review packet ranges overlap")
        prepared_records += end - start + 1
        previous_end = end
    queue_total = len(queue_ids)
    if prepared_records > queue_total:
        raise ValueError("prepared review records exceed queue total")

    status = {
        "version": 2,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generated_from": {
            "queue": "generated/independent-verification-queue.jsonl.gz",
            "registry": "generated/independent-verification-registry.jsonl.gz",
        },
        "queue_total": queue_total,
        "registry_total": len(registry_ids),
        "prepared_review_records": prepared_records,
        "verified_records": verified,
        "review_records": review,
        "unverified_records": unverified,
        "blocked_records": blocked,
        "other_registry_status_records": other,
        "verification_policy": "FAIL_CLOSED",
        "workflow_success_is_not_independent_verification": True,
        "human_review_required_for_verified_promotion": True,
        "prepared_ranges": prepared_ranges,
        "integrity": {
            "queue_registry_task_ids_match": True,
            "queue_sha256": sha256_file(queue_path),
            "registry_sha256": sha256_file(registry_path),
            "verified_requires_reviewed_and_independent_true": True,
        },
    }
    status["prepared_percent"] = round(prepared_records / queue_total * 100, 2) if queue_total else 0.0
    status["verified_percent_of_queue"] = round(verified / queue_total * 100, 2) if queue_total else 0.0
    status["state"] = "VERIFIED_PROGRESS_AVAILABLE" if verified else "READY_FOR_REVIEW"
    return status


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    status = build_status(root / "generated")
    output = root / "generated" / "independent-verification-status.json"
    output.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))


if __name__ == "__main__":
    main()
