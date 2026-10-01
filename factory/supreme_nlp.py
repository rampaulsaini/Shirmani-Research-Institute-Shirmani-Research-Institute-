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
from typing import Any, Iterable


SUBJECT_TYPES = frozenset(
    {"HUMAN", "ANIMAL", "PLANT", "MATERIAL", "ENVIRONMENT", "DEVICE", "OTHER"}
)
MODALITIES = frozenset(
    {
        "TEXT", "AUDIO", "IMAGE", "VIDEO", "VIBRATION", "ELECTRICAL",
        "TEMPERATURE", "LIGHT", "CHEMICAL", "MOTION", "MULTIMODAL", "OTHER",
    }
)
EVIDENCE_LEVELS = frozenset(
    {"observational", "correlational", "validated", "unknown"}
)
VERIFICATION_STATUSES = frozenset(
    {"UNVERIFIED", "INDEPENDENTLY_VERIFIED", "REJECTED"}
)


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
    """Return a stable SHA-256 fingerprint for JSON-compatible evidence."""
    payload = json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    )
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


def observe(
    record_id: str,
    subject_type: str,
    modality: str,
    values: dict[str, float],
    unit: str | None,
    source: str,
    context: dict[str, Any] | None = None,
) -> SignalObservation:
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
        "record_id": record_id,
        "subject_type": subject_type,
        "modality": modality,
        "values": values,
        "unit": unit,
        "source": source,
        "captured_at": captured_at,
        "context": context or {},
    }
    return SignalObservation(**raw, evidence_hash=canonical_hash(raw))


def interpret(
    obs: SignalObservation,
    statement: str,
    hypotheses: Iterable[str],
    confidence: float,
    evidence_level: str = "observational",
    limitations: Iterable[str] = (),
    verification_status: str = "UNVERIFIED",
) -> Interpretation:
    _require_text("statement", statement)
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if evidence_level not in EVIDENCE_LEVELS:
        raise ValueError("unsupported evidence level")
    if verification_status not in VERIFICATION_STATUSES:
        raise ValueError("unsupported verification_status")

    hypothesis_list = list(hypotheses)
    limitation_list = list(limitations)
    if not all(isinstance(item, str) and item.strip() for item in hypothesis_list):
        raise ValueError("hypotheses must contain non-empty strings")
    if not all(isinstance(item, str) and item.strip() for item in limitation_list):
        raise ValueError("limitations must contain non-empty strings")

    return Interpretation(
        record_id=obs.record_id,
        observation_hash=obs.evidence_hash,
        statement=statement,
        hypotheses=hypothesis_list,
        confidence=confidence,
        evidence_level=evidence_level,
        limitations=limitation_list,
        verification_status=verification_status,
        generated_at=datetime.now(timezone.utc).isoformat(),
    )


def to_json(record: SignalObservation | Interpretation) -> str:
    return json.dumps(asdict(record), ensure_ascii=False, sort_keys=True)
