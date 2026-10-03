#!/usr/bin/env python3
"""Build a fail-closed independent-verification progress map.

This report measures queue/review/verification state only. It never promotes
records and never treats workflow success, QC PASS, packet creation, or source
traceability as independent verification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

TARGET = 100_200

def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON at {path}:{line_no}: {exc}")
    return rows

def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pct(n: int, d: int) -> float:
    return round((100.0 * n / d), 6) if d else 0.0

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", required=True)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    queue_path = Path(args.queue)
    registry_path = Path(args.registry)
    queue = load_jsonl(queue_path)
    registry = load_jsonl(registry_path)

    queue_ids = [str(r.get("task_id", "")) for r in queue]
    registry_ids = [str(r.get("task_id", "")) for r in registry]
    if not all(queue_ids) or len(queue_ids) != len(set(queue_ids)):
        raise SystemExit("verification queue IDs are missing or duplicated")
    if not all(registry_ids) or len(registry_ids) != len(set(registry_ids)):
        raise SystemExit("verification registry IDs are missing or duplicated")
    if set(queue_ids) != set(registry_ids):
        raise SystemExit("queue and registry task sets do not match")

    verification = Counter(
        str(r.get("verification_status", "UNKNOWN")).upper() for r in registry
    )
    status = Counter(str(r.get("status", "UNKNOWN")).upper() for r in registry)
    reviewed = sum(r.get("status") == "REVIEWED" for r in registry)
    verified = sum(
        r.get("status") == "REVIEWED"
        and r.get("verification_status") == "VERIFIED"
        and r.get("independent") is True
        for r in registry
    )

    report = {
        "schema_version": 2,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_records": TARGET,
        "queue_total": len(queue),
        "registry_total": len(registry),
        "reviewed_records": reviewed,
        "independent_verified_records": verified,
        "remaining_review_records": max(len(queue) - reviewed, 0),
        "remaining_verification_records": max(len(queue) - verified, 0),
        "review_completion_pct": pct(reviewed, len(queue)),
        "verification_completion_pct": pct(verified, len(queue)),
        "target_completion_pct": pct(verified, TARGET),
        "verification_status_counts": dict(sorted(verification.items())),
        "registry_status_counts": dict(sorted(status.items())),
        "queue_registry_task_id_match": True,
        "automation_state": "READY_FOR_HUMAN_REVIEW" if queue else "NO_QUEUE",
        "verification_state": (
            "INDEPENDENT_VERIFICATION_PENDING" if verified == 0
            else "PARTIALLY_VERIFIED"
        ),
        "promotion_policy": "FAIL_CLOSED",
        "workflow_success_is_not_verification": True,
        "promotion_allowed_by_this_report": False,
        "human_review_inferred": False,
        "integrity": {
            "queue_sha256": sha256_file(queue_path),
            "registry_sha256": sha256_file(registry_path),
        },
        "policy": (
            "Only the existing independent verification promotion gate may "
            "recognize VERIFIED records. This progress report is telemetry."
        ),
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
