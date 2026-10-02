#!/usr/bin/env python3
"""Unified fail-closed gate for the SHIRMANI Supreme NLP control plane.

This gate does not claim model accuracy or subjective experience. It verifies
that practitioner and multimodal interpreters agree on governance boundaries,
produce deterministic machine-readable outputs, and remain independently
unverified until evidence-backed promotion occurs.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from agents.supreme_nlp_multimodal import analyze, to_simple_language
from agents.supreme_nlp_practitioner import build_practitioner_record

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
    multimodal = analyze(ROWS, request="multimodal signal interpretation", source_type="synthetic")
    multimodal["simple_language"] = to_simple_language(multimodal)

    pg = practitioner["governance"]
    checks = {
        "practitioner_fail_closed": pg["fail_closed"] is True,
        "practitioner_no_subjective_claim": pg["subjective_experience_claim_allowed"] is False,
        "practitioner_no_code_mutation": pg["code_mutation_allowed"] is False,
        "practitioner_independent_verification": pg["independent_verification_required"] is True,
        "multimodal_unverified": multimodal["verification"]["status"] == "UNVERIFIED",
        "multimodal_promotion_blocked": multimodal["verification"]["promotion_allowed"] is False,
        "multimodal_status_bounded": multimodal["status"] in {"CANDIDATE", "NO_CLAIM", "BLOCKED"},
        "confidence_bounded": 0 <= multimodal["confidence"] <= 1,
        "simple_language_present": bool(multimodal["simple_language"].strip()),
    }
    passed = all(checks.values())

    report = {
        "schema_version": "1.0",
        "status": "PASS" if passed else "BLOCK",
        "promotion_allowed": False,
        "checks": checks,
        "practitioner": {
            "status": practitioner["result"]["status"],
            "confidence": practitioner["result"]["features"].get("confidence"),
            "fingerprint": practitioner["fingerprint"],
        },
        "multimodal": {
            "status": multimodal["status"],
            "confidence": multimodal["confidence"],
            "verification": multimodal["verification"],
            "simple_language": multimodal["simple_language"],
        },
        "governance": {
            "fail_closed": True,
            "accuracy_is_measured_not_declared": True,
            "subjective_experience_claim_allowed": False,
            "independent_verification_required": True,
            "production_code_mutation_allowed": False,
        },
    }
    report["fingerprint"] = canonical_hash(report)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
