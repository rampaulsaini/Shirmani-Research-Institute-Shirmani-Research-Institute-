#!/usr/bin/env python3
"""Unified fail-closed gate for the SHIRMANI Supreme NLP control plane.

The unified gate consumes the current v3 validation contract instead of an
obsolete multimodal module name. It checks governance boundaries, deterministic
output shape, explicit abstention/verification state, and the non-promotion
boundary. A passing gate is operational evidence only; it is not independent
scientific verification.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from agents.supreme_nlp_practitioner import build_practitioner_record
from agents.supreme_nlp_v3 import build_record

OUT = Path("generated/supreme-nlp/unified-control-plane.json")

ROWS = [
    {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "synthetic-a"},
    {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 1.0, "source": "synthetic-b"},
    {"modality": "thermal", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "synthetic-c"},
]


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> int:
    practitioner = build_practitioner_record(ROWS, "unified-control-plane")
    v3_record = build_record(ROWS, "unified-control-plane-v3")
    v3 = v3_record["result"]
    interpretation = v3.get("interpretation") or {}

    pg = practitioner["governance"]
    # Promotion must be derived from the record itself, never hard-coded.
    verification_status = interpretation.get("verification_status")
    independent_replication_verified = v3_record["provenance"].get("independent_replication_verified")
    promotion_blocked = not (
        verification_status == "VERIFIED"
        and independent_replication_verified is True
    )

    checks = {
        "practitioner_fail_closed": pg["fail_closed"] is True,
        "practitioner_no_subjective_claim": pg["subjective_experience_claim_allowed"] is False,
        "practitioner_no_code_mutation": pg["code_mutation_allowed"] is False,
        "practitioner_independent_verification": pg["independent_verification_required"] is True,
        "v3_status_interpreted": v3["status"] == "interpreted",
        "v3_unverified": interpretation["verification_status"] == "UNVERIFIED",
        "v3_confidence_uncalibrated": interpretation["confidence_status"] == "UNCALIBRATED",
        "v3_calibration_required": interpretation["calibration_required"] is True,
        "v3_experiment_provenance_declared": v3["features"].get("experiment_provenance_status") in {"DECLARED_IDENTIFIERS_ONLY", "MISSING_EXPERIMENT_IDENTIFIERS"},
        "v3_independent_replication_unverified": v3_record["provenance"].get("independent_replication_verified") is False,
        "v3_promotion_blocked": promotion_blocked,
        "simple_language_present": bool(v3_record["simple_language"].strip()),
        "fingerprint_present": bool(v3_record["fingerprint"].strip()),
    }
    passed = all(checks.values())

    report = {
        "schema_version": "2.0",
        "status": "PASS" if passed else "BLOCK",
        "promotion_allowed": False,
        "checks": checks,
        "practitioner": {
            "status": practitioner["result"]["status"],
            "confidence": practitioner["result"]["features"].get("confidence"),
            "fingerprint": practitioner["fingerprint"],
        },
        "v3": {
            "schema_version": v3_record["schema_version"],
            "status": v3["status"],
            "confidence": interpretation.get("confidence"),
            "confidence_status": interpretation.get("confidence_status"),
            "verification_status": interpretation.get("verification_status"),
            "abstention": interpretation.get("abstention"),
            "calibration_required": interpretation.get("calibration_required"),
            "experiment_provenance_status": v3["features"].get("experiment_provenance_status"),
            "independent_experiment_count": v3["features"].get("independent_experiment_count"),
            "independent_replication_verified": v3_record["provenance"].get("independent_replication_verified"),
            "fingerprint": v3_record["fingerprint"],
            "simple_language": v3_record["simple_language"],
        },
        "governance": {
            "fail_closed": True,
            "accuracy_is_measured_not_declared": True,
            "subjective_experience_claim_allowed": False,
            "independent_verification_required": True,
            "production_code_mutation_allowed": False,
            "promotion_requires_independent_evidence": True,
            "declared_experiment_identifiers_are_not_replication": True,
        },
    }
    report["fingerprint"] = canonical_hash(report)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
