"""Deterministic governance checks for the SHIRMANI Automission stack.

This module is intentionally evidence-first. It does not decide whether a
subjective experience exists; it checks whether a record is allowed to claim
that it has been established.
"""
from __future__ import annotations
from typing import Any

FORBIDDEN_VERIFIED_PATTERNS = (
    "direct proof of subjective experience",
    "proof of consciousness",
    "भाव का प्रत्यक्ष प्रमाण",
    "चेतना का प्रत्यक्ष प्रमाण",
    "100% certainty",
    "पूर्णतः सिद्ध",
)

REQUIRED_FIELDS = (
    "source", "timestamp", "input_fingerprint", "method",
    "observations", "interpretation", "limitations",
    "counter_evidence", "alternative_explanations",
    "verification_status",
)

ALLOWED_STATES = {
    "RAW", "OBSERVED", "INTERPRETED",
    "EVIDENCE-SUPPORTED", "INDEPENDENTLY-VERIFIED",
}

def audit_record(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    missing = [k for k in REQUIRED_FIELDS if k not in record]
    if missing:
        errors.append("missing_required_fields:" + ",".join(missing))

    state = str(record.get("verification_status", "RAW"))
    if state not in ALLOWED_STATES:
        errors.append("invalid_verification_status:" + state)

    text = str(record.get("interpretation", "")).lower()
    for phrase in FORBIDDEN_VERIFIED_PATTERNS:
        if phrase.lower() in text and state != "INDEPENDENTLY-VERIFIED":
            errors.append("unsupported_claim:" + phrase)

    if not record.get("counter_evidence"):
        warnings.append("counter_evidence_missing")
    if not record.get("alternative_explanations"):
        warnings.append("alternative_explanations_missing")
    if not record.get("limitations"):
        errors.append("limitations_missing")

    return {
        "status": "PASS" if not errors else "FAIL",
        "fail_closed": bool(errors),
        "errors": errors,
        "warnings": warnings,
    }
