#!/usr/bin/env python3
"""Build a fail-closed independent-verification progress status.

This reports preparation and registry state only. It never promotes a record
to VERIFIED and never treats workflow success as independent verification.
"""
from __future__ import annotations
import gzip, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
RANGE_RE = re.compile(r"^verification-review-packet-(\d{6})-(\d{6})\.json$")

def read_jsonl_gz(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def main() -> None:
    queue_path = GENERATED / "independent-verification-queue.jsonl.gz"
    registry_path = GENERATED / "independent-verification-registry.jsonl.gz"
    if not queue_path.exists() or not registry_path.exists():
        raise SystemExit("independent verification queue/registry is missing")

    queue_total = sum(1 for _ in read_jsonl_gz(queue_path))
    registry_total = 0
    verified = review = unverified = blocked = other = 0
    # Accept the legacy registry label and the canonical schema label as the same
    # independently verified state. Do not treat workflow/QC success as VERIFIED.
    verified_statuses = {"VERIFIED", "INDEPENDENTLY_VERIFIED"}
    for record in read_jsonl_gz(registry_path):
        registry_total += 1
        value = str(record.get("verification_status", "")).strip().upper()
        if value in verified_statuses: verified += 1
        elif value in {"REVIEW", "UNDER_REVIEW", "CHECKED"}: review += 1
        elif value in {"UNVERIFIED", "NOT_VERIFIED", "PENDING", "READY_FOR_HUMAN_REVIEW"}: unverified += 1
        elif value == "BLOCKED": blocked += 1
        else: other += 1

    prepared_ranges, prepared_records = [], 0
    for path in GENERATED.glob("verification-review-packet-*.json"):
        match = RANGE_RE.match(path.name)
        if not match: continue
        start, end = map(int, match.groups())
        try: packet = json.loads(path.read_text(encoding="utf-8"))
        except Exception: continue
        if packet.get("status") == "READY_FOR_HUMAN_REVIEW":
            prepared_ranges.append([start, end])
            prepared_records += max(0, end - start + 1)

    status = {
        "version": 1,
        "generated_from": {
            "queue": "generated/independent-verification-queue.jsonl.gz",
            "registry": "generated/independent-verification-registry.jsonl.gz",
        },
        "queue_total": queue_total,
        "registry_total": registry_total,
        "prepared_review_records": prepared_records,
        "verified_records": verified,
        "review_records": review,
        "unverified_records": unverified,
        "blocked_records": blocked,
        "other_registry_status_records": other,
        "verification_policy": "FAIL_CLOSED",
        "workflow_success_is_not_independent_verification": True,
        "human_review_required_for_verified_promotion": True,
        "prepared_ranges": sorted(prepared_ranges),
    }
    status["prepared_percent"] = round(prepared_records / queue_total * 100, 2) if queue_total else 0.0
    status["verified_percent_of_queue"] = round(verified / queue_total * 100, 2) if queue_total else 0.0
    status["state"] = "VERIFIED_PROGRESS_AVAILABLE" if verified else "READY_FOR_REVIEW"

    (GENERATED / "independent-verification-status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    main()
