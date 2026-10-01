"""Supreme NLP quality and verification gate.

Dependency-free control-plane validation for multimodal signal -> language
pipelines. Observations, interpretations, evidence, provenance and
verification are deliberately separated so model output cannot masquerade as
scientific proof.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

REQUIRED_FIELDS = {
    "event_id", "source_type", "observations", "interpretation",
    "confidence", "evidence", "verification", "provenance",
}

CLAIM_TYPES = {
    "observation", "data_interpretation", "hypothesis", "scientific_claim",
}


def _bounded_confidence(value: Any) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    return value


def validate_record(record: Dict[str, Any]) -> Dict[str, Any]:
    missing = sorted(REQUIRED_FIELDS - record.keys())
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    confidence = _bounded_confidence(record["confidence"])
    observations = record["observations"]
    evidence = record["evidence"]
    verification = record["verification"]
    provenance = record["provenance"]
    interpretation = record["interpretation"]

    if not isinstance(record["event_id"], str) or not record["event_id"].strip():
        raise ValueError("event_id must be a non-empty string")
    if not isinstance(record["source_type"], str) or not record["source_type"].strip():
        raise ValueError("source_type must be a non-empty string")
    if not isinstance(observations, list) or not observations:
        raise ValueError("observations must be a non-empty list")
    if not all(isinstance(item, dict) for item in observations):
        raise ValueError("each observation must be an object")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError("evidence must be a non-empty list")
    if not all(isinstance(item, dict) for item in evidence):
        raise ValueError("each evidence item must be an object")
    if not all(isinstance(item.get("id"), str) and item["id"].strip() for item in evidence):
        raise ValueError("each evidence item must have a non-empty id")
    if not all(isinstance(item.get("type"), str) and item["type"].strip() for item in evidence):
        raise ValueError("each evidence item must have a non-empty type")
    if not isinstance(verification, dict):
        raise ValueError("verification must be an object")
    if not isinstance(provenance, dict):
        raise ValueError("provenance must be an object")
    if not isinstance(provenance.get("source"), str) or not provenance["source"].strip():
        raise ValueError("provenance.source must be a non-empty string")
    if not isinstance(interpretation, dict):
        raise ValueError("interpretation must be an object")
    if not isinstance(interpretation.get("plain_language"), str) or not interpretation["plain_language"].strip():
        raise ValueError("interpretation.plain_language must be a non-empty string")

    independent_check = verification.get("independent_check")
    if not isinstance(independent_check, bool):
        raise ValueError("verification.independent_check must be boolean")

    claim_type = interpretation.get("claim_type", "data_interpretation")
    if claim_type not in CLAIM_TYPES:
        raise ValueError("unsupported interpretation.claim_type")
    if claim_type == "scientific_claim" and not independent_check:
        raise ValueError("scientific_claim requires an independent verification check")
    if claim_type == "scientific_claim" and len(evidence) < 2:
        raise ValueError("scientific_claim requires at least two evidence items")
    if claim_type == "scientific_claim":
        evaluator_count = verification.get("independent_evaluator_count", 0)
        if not isinstance(evaluator_count, int) or evaluator_count < 2:
            raise ValueError("scientific_claim requires at least two independent evaluators")
        if verification.get("confidence_calibrated") is not True:
            raise ValueError("scientific_claim requires calibrated confidence")
        if len({item["id"] for item in evidence}) < 2:
            raise ValueError("scientific_claim requires distinct evidence identities")
        if len({item["type"] for item in evidence}) < 2:
            raise ValueError("scientific_claim requires diverse evidence types")

    return {
        "event_id": str(record["event_id"]),
        "status": "verified" if independent_check else "unverified",
        "confidence": confidence,
        "observation_count": len(observations),
        "evidence_count": len(evidence),
        "independent_check": independent_check,
        "claim_type": claim_type,
        "quality_dimensions": {
            "schema_complete": True,
            "typed_observations": True,
            "evidence_present": True,
            "independent_verification": independent_check,
            "claim_strength_guard": True,
            "evidence_identity_guard": True,
            "evaluator_independence_guard": (claim_type != "scientific_claim" or verification.get("independent_evaluator_count", 0) >= 2),
            "confidence_calibration_guard": (claim_type != "scientific_claim" or verification.get("confidence_calibrated") is True),
        },
    }


def run_self_test() -> Dict[str, Any]:
    sample = {
        "event_id": "synthetic-self-test-001",
        "source_type": "synthetic_multimodal",
        "observations": [
            {"modality": "signal", "feature": "pattern_A", "value": 0.72},
            {"modality": "environment", "feature": "temperature", "value": 24.1},
        ],
        "interpretation": {
            "plain_language": "A measurable signal pattern was detected.",
            "claim_type": "data_interpretation",
        },
        "confidence": 0.72,
        "evidence": [{"id": "synthetic_fixture", "type": "fixture"}],
        "verification": {
            "independent_check": True,
            "method": "deterministic_fixture",
        },
        "provenance": {"source": "self_test", "timestamp": "synthetic"},
    }
    result = validate_record(sample)

    negative = dict(sample)
    negative["confidence"] = 1.01
    try:
        validate_record(negative)
    except ValueError:
        confidence_guard = True
    else:
        confidence_guard = False

    negative = dict(sample)
    negative["verification"] = {"independent_check": "yes"}
    try:
        validate_record(negative)
    except ValueError:
        verification_guard = True
    else:
        verification_guard = False

    negative = dict(sample)
    negative["interpretation"] = dict(sample["interpretation"], claim_type="scientific_claim")
    negative["verification"] = {"independent_check": False}
    try:
        validate_record(negative)
    except ValueError:
        claim_strength_guard = True
    else:
        claim_strength_guard = False

    negative = dict(sample)
    negative["evidence"] = ["not-an-object"]
    try:
        validate_record(negative)
    except ValueError:
        evidence_shape_guard = True
    else:
        evidence_shape_guard = False

    guards = {
        "confidence_bounds": confidence_guard,
        "verification_type": verification_guard,
        "claim_strength": claim_strength_guard,
        "evidence_shape": evidence_shape_guard,
    }
    if not all(guards.values()):
        raise AssertionError("negative validation guards failed")

    return {
        "ok": True,
        "record": result,
        "guards": guards,
        "quality_score": sum(guards.values()) / len(guards),
    }


def main() -> None:
    result = run_self_test()
    result["generated_at"] = datetime.now(timezone.utc).isoformat()
    result["engine_hash"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = Path("generated/supreme-nlp-status.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
