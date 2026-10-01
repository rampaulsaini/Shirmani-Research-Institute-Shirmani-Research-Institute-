"""Evidence-first Supreme NLP practitioner control plane.

This module does not claim to detect subjective experience. It converts structured,
measured multimodal signals into auditable natural-language hypotheses while
preserving uncertainty, provenance, and verification boundaries.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Iterable

MODALITIES = {
    "text", "speech", "image", "video", "vibration", "electrical", "thermal",
    "acoustic", "chemical", "environmental", "motion", "other_sensor",
}


def _fingerprint(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def validate_observation(observation: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if observation.get("modality") not in MODALITIES:
        errors.append("unsupported modality")
    if "value" not in observation:
        errors.append("missing value")
    if not observation.get("timestamp"):
        errors.append("missing timestamp")
    if not observation.get("source"):
        errors.append("missing source")
    return errors


def interpret(observations: Iterable[dict[str, Any]], hypothesis: str,
              confidence: float, evidence: list[str] | None = None,
              limitations: list[str] | None = None) -> dict[str, Any]:
    obs = list(observations)
    errors = [e for item in obs for e in validate_observation(item)]
    if errors:
        raise ValueError("; ".join(sorted(set(errors))))
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")

    modalities = sorted({x["modality"] for x in obs})
    result = {
        "status": "unverified",
        "claim_type": "signal_based_hypothesis",
        "hypothesis": hypothesis,
        "observations": obs,
        "modalities": modalities,
        "evidence": evidence or [],
        "confidence": confidence,
        "uncertainty": round(1.0 - confidence, 6),
        "limitations": limitations or [
            "Signal interpretation is not, by itself, proof of subjective experience."
        ],
        "provenance": {
            "observation_fingerprint": _fingerprint(obs),
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        "verification_status": "pending_independent_verification",
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "production_promotion_allowed": False,
        },
    }
    return result


def to_plain_language(result: dict[str, Any]) -> str:
    return (
        f"प्राप्त संकेतों के आधार पर एक संभावित व्याख्या है: {result['hypothesis']}। "
        f"मॉडल confidence {result['confidence']:.2f} है; "
        "यह संकेत-आधारित परिकल्पना है, प्रत्यक्ष व्यक्तिपरक अनुभव का प्रमाण नहीं।"
    )
