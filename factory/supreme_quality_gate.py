"""Deterministic fail-closed quality gate for Supreme Continuous Improvement."""
from __future__ import annotations

import json
import pathlib
import sys

REQUIRED = {
    "schema_version",
    "generated_at",
    "pipeline",
    "simple_language",
    "fingerprint",
    "result",
    "governance",
}
REQUIRED_FEATURES = {
    "confidence",
    "agreement",
    "quality",
    "modalities",
    "sources",
}


def validate(path="generated/supreme-nlp/status.json"):
    p = pathlib.Path(path)
    if not p.exists():
        return False, ["STATUS_MISSING"]

    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return False, [f"INVALID_JSON:{exc}"]

    errors = [f"MISSING:{k}" for k in REQUIRED - d.keys()]
    if d.get("schema_version") != "1.0":
        errors.append("SCHEMA_VERSION_INVALID")

    fingerprint = d.get("fingerprint", "")
    if not isinstance(fingerprint, str) or len(fingerprint) != 64:
        errors.append("FINGERPRINT_INVALID")

    result = d.get("result") or {}
    if result.get("status") not in {"insufficient_quality", "interpreted"}:
        errors.append("RESULT_STATUS_INVALID")

    features = result.get("features") or {}
    errors.extend(f"FEATURE_MISSING:{k}" for k in REQUIRED_FEATURES - features.keys())

    for key in ("confidence", "agreement", "quality"):
        try:
            value = float(features.get(key, -1))
        except (TypeError, ValueError):
            value = -1
        if not 0 <= value <= 1:
            errors.append(f"{key.upper()}_OUT_OF_RANGE")

    for key in ("modalities", "sources"):
        try:
            value = int(features.get(key, -1))
        except (TypeError, ValueError):
            value = -1
        if value < 0:
            errors.append(f"{key.upper()}_INVALID")

    interpretation = d.get("interpretation") or {}
    if not interpretation.get("limitations"):
        errors.append("LIMITATIONS_MISSING")
    if not d.get("provenance"):
        errors.append("PROVENANCE_MISSING")

    governance = d.get("governance") or {}
    required_governance = {
        "fail_closed": True,
        "subjective_experience_claim_allowed": False,
        "code_mutation_allowed": False,
        "independent_verification_required": True,
    }
    for key, expected in required_governance.items():
        if governance.get(key) is not expected:
            errors.append(f"GOVERNANCE_BOUNDARY:{key}")

    # A signal interpretation is never allowed to become a claim of subjective
    # experience merely because confidence is high.
    if "subjective experience" not in " ".join(interpretation.get("limitations", [])):
        errors.append("SUBJECTIVE_EXPERIENCE_LIMITATION_MISSING")

    return not errors, errors


if __name__ == "__main__":
    ok, errors = validate()
    print("SUPREME_QUALITY_GATE", "PASS" if ok else "FAIL", errors)
    sys.exit(0 if ok else 1)
