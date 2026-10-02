#!/usr/bin/env python3
"""Evidence-preserving Supreme NLP runtime contract.

The contract converts validated multimodal observations into conservative,
human-readable output. It never treats fluent inference as proof of subjective
experience or as independent verification.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping
import hashlib
import json
from datetime import datetime, timezone

EVIDENCE_CLASSES = {"OBSERVED", "INFERRED", "CORRELATED", "HYPOTHESIS", "UNKNOWN"}
STATUSES = {"NO_CLAIM", "CANDIDATE", "VERIFIED", "BLOCKED"}


@dataclass(frozen=True)
class Observation:
    source: str
    modality: str
    value: Any
    timestamp: str
    quality: float
    preprocessing_version: str
    model_version: str
    provenance_fingerprint: str


def fingerprint_observation(obs: Mapping[str, Any]) -> str:
    raw = json.dumps(dict(obs), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def validate_observation(obs: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    required = (
        "source", "modality", "value", "timestamp", "quality",
        "preprocessing_version", "model_version", "provenance_fingerprint",
    )
    for key in required:
        if key not in obs:
            errors.append(f"MISSING:{key}")
    if "quality" in obs:
        try:
            quality = float(obs["quality"])
            if not 0 <= quality <= 1:
                errors.append("QUALITY_OUT_OF_RANGE")
        except (TypeError, ValueError):
            errors.append("QUALITY_NOT_NUMERIC")
    if obs.get("provenance_fingerprint") and len(str(obs["provenance_fingerprint"])) < 16:
        errors.append("PROVENANCE_FINGERPRINT_TOO_SHORT")
    return errors


def fuse_observations(observations: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    rows = [dict(x) for x in observations]
    errors: list[str] = []
    for row in rows:
        errors.extend(validate_observation(row))
    if errors:
        return {"status": "BLOCKED", "evidence_class": "UNKNOWN", "errors": sorted(set(errors))}
    qualities = [float(x["quality"]) for x in rows]
    signatures = {
        json.dumps(x["value"], ensure_ascii=False, sort_keys=True) for x in rows
    }
    return {
        "status": "CANDIDATE" if rows else "NO_CLAIM",
        "evidence_class": "OBSERVED" if rows else "UNKNOWN",
        "observation_count": len(rows),
        "mean_quality": sum(qualities) / len(qualities) if qualities else 0.0,
        "modalities": sorted({str(x["modality"]) for x in rows}),
        "disagreement_present": len(signatures) > 1,
        "provenance_fingerprints": [str(x["provenance_fingerprint"]) for x in rows],
    }


def render_simple_language(
    *,
    evidence_class: str,
    status: str,
    measured: str,
    pattern: str,
    interpretation: str,
    unknown: str,
    confidence: float,
) -> str:
    if evidence_class not in EVIDENCE_CLASSES:
        raise ValueError("invalid evidence_class")
    if status not in STATUSES:
        raise ValueError("invalid status")
    confidence = max(0.0, min(1.0, float(confidence)))
    if status == "NO_CLAIM" or evidence_class == "UNKNOWN":
        interpretation = "उपलब्ध प्रमाण पर्याप्त नहीं हैं; इसलिए कोई निश्चित दावा नहीं किया जा रहा है।"
    return (
        f"क्या मापा गया: {measured}\n"
        f"क्या pattern मिला: {pattern}\n"
        f"प्रमाण-आधारित व्याख्या: {interpretation}\n"
        f"क्या अभी अज्ञात है: {unknown}\n"
        f"Evidence class: {evidence_class}; status: {status}; confidence: {confidence:.3f}"
    )


def build_record(
    *,
    evidence_class: str,
    status: str,
    observations: list[Mapping[str, Any]],
    claims: list[str],
    limitations: list[str],
    confidence: float,
) -> dict[str, Any]:
    fused = fuse_observations(observations)
    if fused["status"] == "BLOCKED":
        status = "BLOCKED"
        evidence_class = "UNKNOWN"
    return {
        "evidence_class": evidence_class,
        "status": status,
        "provenance": {
            "source": "multimodal-runtime",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fingerprint": hashlib.sha256(
                json.dumps(fused, sort_keys=True, ensure_ascii=False).encode("utf-8")
            ).hexdigest(),
        },
        "confidence": max(0.0, min(1.0, float(confidence))),
        "claims": claims,
        "limitations": limitations,
        "fusion": fused,
    }


if __name__ == "__main__":
    demo = build_record(
        evidence_class="OBSERVED",
        status="CANDIDATE",
        observations=[{
            "source": "demo-sensor",
            "modality": "time-series",
            "value": {"signal": "sample"},
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "quality": 1.0,
            "preprocessing_version": "v1",
            "model_version": "contract-only",
            "provenance_fingerprint": "demo-provenance-00000001",
        }],
        claims=["A measurable signal was received."],
        limitations=["This contract does not establish subjective experience."],
        confidence=0.5,
    )
    print(json.dumps(demo, ensure_ascii=False, indent=2))
