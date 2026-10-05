#!/usr/bin/env python3
"""Result-first review gate.

This layer verifies the integrity and completeness of a *produced result
artifact* before routing it to independent review. It never promotes a result
to VERIFIED and never treats workflow success as verification.

The intended lifecycle is:
INPUTS -> MODEL/PROCESS -> RESULT ARTIFACT -> RESULT INTEGRITY CHECK
-> INDEPENDENT REVIEW -> DECISION.

A result can therefore be operationally review-ready without being scientifically
verified.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
from pathlib import Path
from typing import Any


ALLOWED_RESULT_STATUSES = {
    "interpreted",
    "insufficient_quality",
    "completed",
    "failed",
    "abstained",
}
REQUIRED_FIELDS = ("result_id", "task_id", "result_status", "result")
FORBIDDEN_VERIFICATION_FLAGS = {
    "verified",
    "independently_verified",
    "scientific_verification_granted",
}
REQUIRED_PROVENANCE_FIELDS = (
    "generator",
    "verification_status",
    "independent_replication_verified",
)


def has_true_verification_flag(value: Any) -> bool:
    """Reject verification shortcuts at any nesting depth."""
    if isinstance(value, dict):
        return any(
            (key in FORBIDDEN_VERIFICATION_FLAGS and value[key] is True)
            or has_true_verification_flag(child)
            for key, child in value.items()
        )
    if isinstance(value, list):
        return any(has_true_verification_flag(item) for item in value)
    return False


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def integrity_payload(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "result_id": record["result_id"],
        "task_id": record["task_id"],
        "result_status": record["result_status"],
        "result": record["result"],
        "provenance": record["provenance"],
    }


def verify_integrity(record: dict[str, Any]) -> bool:
    fingerprint = record.get("fingerprint")
    if not isinstance(fingerprint, str) or not fingerprint:
        return False
    try:
        expected = canonical_sha256(integrity_payload(record))
    except (KeyError, TypeError, ValueError):
        return False
    return hmac.compare_digest(fingerprint, expected)


def validate_result(record: dict[str, Any]) -> dict[str, Any]:
    checks: dict[str, bool] = {}
    checks["required_fields"] = (
        all(non_empty_string(record.get(k)) for k in ("result_id", "task_id", "result_status"))
        and isinstance(record.get("result"), dict)
    )
    checks["result_status_allowed"] = str(record.get("result_status", "")) in ALLOWED_RESULT_STATUSES
    checks["result_object_present"] = isinstance(record.get("result"), dict)
    provenance = record.get("provenance")
    checks["provenance_present"] = (
        isinstance(provenance, dict)
        and non_empty_string(provenance.get("generator"))
        and non_empty_string(provenance.get("verification_status"))
        and isinstance(provenance.get("independent_replication_verified"), bool)
    )
    checks["integrity"] = verify_integrity(record)

    # Explicitly reject attempts to turn this post-result gate into a direct
    # verification shortcut.
    checks["no_direct_verification_shortcut"] = not has_true_verification_flag(record)
    if isinstance(provenance, dict):
        checks["provenance_not_verified"] = (
            provenance.get("verification_status") == "UNVERIFIED"
            and provenance.get("independent_replication_verified") is False
        )
    else:
        checks["provenance_not_verified"] = False

    passed = all(checks.values())
    return {
        "status": "READY_FOR_INDEPENDENT_REVIEW" if passed else "FAIL",
        "checks": checks,
        "scientific_verification_granted": False,
        "next_step": (
            "Route the concrete result artifact to an independent reviewer."
            if passed
            else "Repair the result artifact before independent review."
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", required=True)
    args = ap.parse_args()

    path = Path(args.result)
    if not path.is_file():
        raise SystemExit(f"RESULT_REVIEW_GATE_FAIL: missing result artifact {path}")

    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"RESULT_REVIEW_GATE_FAIL: invalid JSON: {exc}") from exc

    if not isinstance(record, dict):
        raise SystemExit("RESULT_REVIEW_GATE_FAIL: result artifact must be an object")

    report = validate_result(record)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if report["status"] != "READY_FOR_INDEPENDENT_REVIEW":
        raise SystemExit("RESULT_REVIEW_GATE_FAIL: result is not review-ready")


if __name__ == "__main__":
    main()
