"""Deterministic, evidence-first multimodal signal-to-language contract.

This module is deliberately model-agnostic. A future ML/NLP model can be plugged
into the interpretation stage without weakening the evidence and uncertainty
boundary.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class SignalRecord:
    signal_id: str
    observation: str
    interpretation: str
    confidence: float
    evidence: Sequence[str]
    limitations: Sequence[str]
    provenance: Mapping[str, Any]
    status: str = "UNVERIFIED"

    def validate(self) -> None:
        if not self.signal_id.strip():
            raise ValueError("signal_id is required")
        if not self.observation.strip():
            raise ValueError("observation is required")
        if not self.interpretation.strip():
            raise ValueError("interpretation is required")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if not self.provenance:
            raise ValueError("provenance is required")
        if self.status not in {"OBSERVED", "INFERRED", "UNVERIFIED", "REJECTED"}:
            raise ValueError("invalid status")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)


def stable_signal_id(source: str, payload: str) -> str:
    """Create a reproducible identifier without storing sensitive raw data."""
    return sha256(f"{source}\n{payload}".encode("utf-8")).hexdigest()[:24]


def translate_signal(
    *,
    source: str,
    observation: str,
    model_interpretation: str | None = None,
    confidence: float = 0.0,
    evidence: Sequence[str] = (),
    limitations: Sequence[str] = (),
    provenance: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Produce a simple-language result with an explicit epistemic boundary."""
    has_evidence = bool(evidence)
    status = "INFERRED" if model_interpretation and has_evidence else "UNVERIFIED"
    interpretation = model_interpretation or (
        "उपलब्ध संकेत दर्ज हुए हैं, लेकिन इनके अर्थ के लिए पर्याप्त सत्यापन-साक्ष्य उपलब्ध नहीं है।"
    )
    record = SignalRecord(
        signal_id=stable_signal_id(source, observation),
        observation=observation,
        interpretation=interpretation,
        confidence=float(confidence),
        evidence=list(evidence),
        limitations=list(limitations) or [
            "यह आउटपुट observable signal की व्याख्या है; इसे अपने-आप subjective feeling का प्रमाण नहीं माना जाता।"
        ],
        provenance=dict(provenance or {"source": source}),
        status=status,
    )
    return record.to_dict()
