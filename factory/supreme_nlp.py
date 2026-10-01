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
    "event_id",
    "source_type",
    "observations",
    "interpretation",
    "confidence",
    "evidence",
    "verification",
    "provenance",
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

    if not isinstance(observations, list) or not observations:
        raise ValueError("observations must be a non-empty list")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError("evidence must be a non-empty list")
    if not isinstance(verification, dict):
        raise ValueError("verification must be an object")
    if not isinstance(provenance, dict):
        raise ValueError("provenance must be an object")
    if not isinstance(interpretation, dict):
        raise ValueError("interpretation must be an object")

    independent_check = verification.get("independent_check")
    if not isinstance(independent_check, bool):
        raise ValueError("verification.independent_check must be boolean")

    claim_type = interpretation.get("claim_type", "data_interpretation")
    if claim_type not in {
        "observation",
        "data_interpretation",
        "hypothesis",
        "scientific_claim",
    }:
        raise ValueError("unsupported interpretation.claim_type")

    return {
        "event_id": str(record["event_id"]),
        "status": "verified" if independent_check else "unverified",
        "confidence": confidence,
        "observation_count": len(observations),
        "evidence_count": len(evidence),
        "independent_check": independent_check,
        "claim_type": claim_type,
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
        "provenance": {
            "source": "self_test",
            "timestamp": "synthetic",
        },
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

    if not confidence_guard or not verification_guard:
        raise AssertionError("negative validation guards failed")

    return {
        "ok": True,
        "record": result,
        "guards": {
            "confidence_bounds": confidence_guard,
            "verification_type": verification_guard,
        },
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
