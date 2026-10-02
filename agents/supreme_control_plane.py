"""Supreme Evidence Control Plane.

Deterministic orchestration layer for NLP/ML/Agent outputs.
It preserves evidence boundaries, fails closed on weak evidence, and emits
machine-readable audit records. It does not claim subjective experience.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Iterable

from supreme_nlp_practitioner import build_practitioner_record
from supreme_nlp_quality import QualityThresholds, evaluate


VERSION = "supreme-control-plane-v1"


@dataclass(frozen=True)
class Policy:
    min_quality: float = 0.70
    min_agreement: float = 0.70
    min_sources: int = 2
    min_samples: int = 10
    max_drift: float = 0.30
    require_independent_verification: bool = True
    allow_subjective_experience_claims: bool = False
    allow_code_mutation: bool = False


def _sha256(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _quality_record(observations: list[dict[str, Any]], practitioner: dict[str, Any]) -> dict[str, Any]:
    result = practitioner.get("result", {})
    features = result.get("features", {})
    normalized = {
        "result": {
            "status": result.get("status", "unknown"),
            "features": {
                "quality": features.get("quality", 0.0),
                "agreement": features.get("agreement", 0.0),
                "sources": features.get("sources", 0),
                "sample_count": len(result.get("observations", observations)),
                "drift_score": 0.0,
            },
            "interpretation": {
                "confidence": features.get("confidence", 0.0)
            },
        },
        "signals": observations,
        "fingerprint": practitioner.get("fingerprint", ""),
        "verification": {"status": "UNVERIFIED"},
    }
    return normalized


def run(
    observations: Iterable[dict[str, Any]],
    request: str = "",
    policy: Policy | None = None,
) -> dict[str, Any]:
    p = policy or Policy()
    rows = list(observations)

    practitioner = build_practitioner_record(rows, request)
    quality_input = _quality_record(rows, practitioner)
    thresholds = QualityThresholds(
        min_quality=p.min_quality,
        min_agreement=p.min_agreement,
        min_sources=p.min_sources,
        min_samples=p.min_samples,
        max_drift=p.max_drift,
    )
    quality = evaluate(quality_input, thresholds=thresholds)

    promoted = (
        quality["status"] == "PASS"
        and not p.require_independent_verification
        and not quality["governance"]["scheduled_code_mutation_allowed"]
    )

    decision = "HOLD_UNVERIFIED"
    if quality["status"] == "BLOCKED":
        decision = "BLOCKED"
    elif quality["status"] == "IMPROVEMENT_REQUIRED":
        decision = "IMPROVEMENT_REQUIRED"
    elif promoted:
        decision = "PROMOTABLE"

    record = {
        "schema_version": VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": [
            "observe",
            "normalize",
            "multimodal-fusion",
            "uncertainty",
            "quality-gate",
            "independent-verification-gate",
        ],
        "decision": decision,
        "promotion_allowed": promoted,
        "practitioner": practitioner,
        "quality_gate": quality,
        "governance": {
            "fail_closed": True,
            "require_independent_verification": p.require_independent_verification,
            "allow_subjective_experience_claims": p.allow_subjective_experience_claims,
            "allow_code_mutation": p.allow_code_mutation,
            "accuracy_is_measured_not_declared": True,
        },
    }
    record["fingerprint"] = _sha256(record)
    return record


def self_test() -> dict[str, Any]:
    observations = [
        {"modality": "sensor", "feature": "signal", "value": 1.00, "quality": 0.95, "source": "A"},
        {"modality": "sensor", "feature": "signal", "value": 1.02, "quality": 0.95, "source": "B"},
    ] * 5
    record = run(observations, "क्या संकेतों में कोई pattern है?")
    assert record["decision"] == "HOLD_UNVERIFIED"
    assert record["governance"]["fail_closed"] is True
    assert record["governance"]["allow_subjective_experience_claims"] is False
    assert len(record["fingerprint"]) == 64
    return {
        "status": "PASS",
        "version": VERSION,
        "decision": record["decision"],
        "fingerprint": record["fingerprint"],
    }


if __name__ == "__main__":
    print(json.dumps(self_test(), ensure_ascii=False, indent=2))
