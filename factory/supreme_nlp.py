"""Evidence-first multimodal signal -> language control plane.

This module does not claim direct access to subjective experience. It converts
observable measurements into traceable natural-language interpretations while
preserving provenance, uncertainty, and alternative hypotheses.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Iterable

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
    generated_at: str

def canonical_hash(value: Any) -> str:
    payload=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def observe(record_id: str, subject_type: str, modality: str,
            values: dict[str, float], unit: str | None, source: str,
            context: dict[str, Any] | None = None) -> SignalObservation:
    captured_at=datetime.now(timezone.utc).isoformat()
    raw={"record_id":record_id,"subject_type":subject_type,"modality":modality,
         "values":values,"unit":unit,"source":source,"captured_at":captured_at,
         "context":context or {}}
    return SignalObservation(**raw, evidence_hash=canonical_hash(raw))

def interpret(obs: SignalObservation, statement: str,
              hypotheses: Iterable[str], confidence: float,
              evidence_level: str="observational",
              limitations: Iterable[str]=()) -> Interpretation:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if evidence_level not in {"observational","correlational","validated","unknown"}:
        raise ValueError("unsupported evidence level")
    return Interpretation(
        record_id=obs.record_id,
        observation_hash=obs.evidence_hash,
        statement=statement,
        hypotheses=list(hypotheses),
        confidence=confidence,
        evidence_level=evidence_level,
        limitations=list(limitations),
        generated_at=datetime.now(timezone.utc).isoformat(),
    )

def to_json(record: SignalObservation | Interpretation) -> str:
    return json.dumps(asdict(record),ensure_ascii=False,sort_keys=True)
