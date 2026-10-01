"""Evidence-first multimodal signal -> language control plane.

The control plane translates observable signals into traceable language while
preserving provenance, uncertainty, competing hypotheses, and verification state.
It does not infer subjective experience from a sensor pattern by itself.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
from typing import Any, Iterable, Mapping


SUBJECT_TYPES = frozenset({"HUMAN", "ANIMAL", "PLANT", "MATERIAL", "ENVIRONMENT", "DEVICE", "OTHER"})
MODALITIES = frozenset({"TEXT", "AUDIO", "IMAGE", "VIDEO", "VIBRATION", "ELECTRICAL", "TEMPERATURE", "LIGHT", "CHEMICAL", "MOTION", "MULTIMODAL", "OTHER"})
EVIDENCE_LEVELS = frozenset({"observational", "correlational", "validated", "unknown"})
VERIFICATION_STATUSES = frozenset({"UNVERIFIED", "INDEPENDENTLY_VERIFIED", "REJECTED"})


@dataclass(frozen=True)
class SignalObservation:
    record_id: str
    subject_type: str
    modality: str
    values: dict[str, float]
    unit: str | None
    source: str
    captured_at: str
    context: dict[str, Any]
    evidence_hash: str


@dataclass(frozen=True)
class Interpretation:
    record_id: str
    observation_hash: str
    statement: str
    hypotheses: list[str]
    confidence: float
    evidence_level: str
    limitations: list[str]
    verification_status: str
    generated_at: str


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _require_text(name: str, value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")


def _validate_values(values: dict[str, float]) -> None:
    if not isinstance(values, dict) or not values:
        raise ValueError("values must be a non-empty object")
    for key, value in values.items():
        _require_text("value key", key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("signal values must be numeric")
        if not math.isfinite(float(value)):
            raise ValueError("signal values must be finite")


def observe(record_id: str, subject_type: str, modality: str, values: dict[str, float],
            unit: str | None, source: str, context: dict[str, Any] | None = None) -> SignalObservation:
    _require_text("record_id", record_id)
    _require_text("source", source)
    if subject_type not in SUBJECT_TYPES:
        raise ValueError("unsupported subject_type")
    if modality not in MODALITIES:
        raise ValueError("unsupported modality")
    if unit is not None:
        _require_text("unit", unit)
    if context is not None and not isinstance(context, dict):
        raise TypeError("context must be an object")
    _validate_values(values)
    captured_at = datetime.now(timezone.utc).isoformat()
    raw = {
        "record_id": record_id, "subject_type": subject_type, "modality": modality,
        "values": values, "unit": unit, "source": source, "captured_at": captured_at,
        "context": context or {},
    }
    return SignalObservation(**raw, evidence_hash=canonical_hash(raw))


def interpret(obs: SignalObservation, statement: str, hypotheses: Iterable[str],
               confidence: float, evidence_level: str = "observational",
               limitations: Iterable[str] = (), verification_status: str = "UNVERIFIED") -> Interpretation:
    _require_text("statement", statement)
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if evidence_level not in EVIDENCE_LEVELS:
        raise ValueError("unsupported evidence level")
    if verification_status != "UNVERIFIED":
        raise ValueError("interpret() only creates UNVERIFIED records")
    hypothesis_list, limitation_list = list(hypotheses), list(limitations)
    if not all(isinstance(x, str) and x.strip() for x in hypothesis_list):
        raise ValueError("hypotheses must contain non-empty strings")
    if not all(isinstance(x, str) and x.strip() for x in limitation_list):
        raise ValueError("limitations must contain non-empty strings")
    return Interpretation(obs.record_id, obs.evidence_hash, statement, hypothesis_list,
                          confidence, evidence_level, limitation_list, "UNVERIFIED",
                          datetime.now(timezone.utc).isoformat())


def independent_verify(interpretation: Interpretation,
                       attestations: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Fail-closed promotion gate; attestations must come from distinct verifiers."""
    records = [a for a in attestations if isinstance(a, Mapping)]
    verifier_ids = {str(a.get("verifier_id", "")).strip() for a in records if str(a.get("verifier_id", "")).strip()}
    matching = [a for a in records
                if a.get("observation_hash") == interpretation.observation_hash
                and a.get("decision") == "PASS"
                and str(a.get("verifier_id", "")).strip()]
    matching_ids = {str(a["verifier_id"]).strip() for a in matching}
    if interpretation.verification_status != "UNVERIFIED":
        return {"status": interpretation.verification_status, "reason": "not_promotable"}
    if interpretation.evidence_level != "validated":
        return {"status": "UNVERIFIED", "reason": "evidence_not_validated"}
    if len(matching_ids) < 2:
        return {"status": "UNVERIFIED", "reason": "two_distinct_pass_attestations_required"}
    return {
        "status": "INDEPENDENTLY_VERIFIED",
        "reason": "two_distinct_verifier_attestations_match_observation",
        "verifier_count": len(matching_ids),
    }


def to_json(record: SignalObservation | Interpretation) -> str:
    return json.dumps(asdict(record), ensure_ascii=False, sort_keys=True)
