"""Observable-signal -> plain-language interpreter for SHIRMANI NLP.

This module deliberately distinguishes measurable/observed signals from claims
about consciousness or literal feelings. It can describe affect-like states
from supplied measurements for living systems, plants, machines, environments,
or other entities, while preserving evidence, uncertainty and provenance.
It is deterministic and dependency-free so Automission can use it as a
bounded normalization layer before probabilistic models are introduced.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Any, Iterable


SCHEMA_VERSION = "1.0"

STATE_RULES = (
    ("calm", 0.0, 0.25),
    ("mild", 0.25, 0.50),
    ("elevated", 0.50, 0.75),
    ("high", 0.75, 1.01),
)


@dataclass(frozen=True)
class Signal:
    name: str
    value: float
    unit: str = ""
    source: str = "unknown"
    observed_at: str | None = None
    quality: float = 1.0
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Interpretation:
    entity_id: str
    entity_type: str
    state: str
    plain_language: str
    confidence: float
    uncertainty: float
    evidence_ids: tuple[str, ...]
    signals_used: tuple[str, ...]
    consciousness_claim: str = "not_inferred"

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _clip(value: float) -> float:
    if not isfinite(value):
        raise ValueError("signal values must be finite")
    return max(0.0, min(1.0, float(value)))


def normalize_signals(signals: Iterable[Signal | dict[str, Any]]) -> list[Signal]:
    result: list[Signal] = []
    for raw in signals:
        if isinstance(raw, Signal):
            s = raw
        else:
            s = Signal(
                name=str(raw.get("name", "")).strip(),
                value=float(raw.get("value", 0.0)),
                unit=str(raw.get("unit", "")),
                source=str(raw.get("source", "unknown")),
                observed_at=raw.get("observed_at"),
                quality=float(raw.get("quality", 1.0)),
                evidence_ids=tuple(str(x) for x in raw.get("evidence_ids", ())),
            )
        if not s.name:
            raise ValueError("every signal needs a name")
        result.append(
            Signal(
                name=s.name,
                value=_clip(s.value),
                unit=s.unit,
                source=s.source,
                observed_at=s.observed_at,
                quality=_clip(s.quality),
                evidence_ids=tuple(s.evidence_ids),
            )
        )
    return result


def _state(score: float) -> str:
    for name, low, high in STATE_RULES:
        if low <= score < high:
            return name
    return "high"


def _confidence(signals: list[Signal]) -> tuple[float, float]:
    if not signals:
        return 0.0, 1.0
    quality = sum(s.quality for s in signals) / len(signals)
    source_count = len({s.source for s in signals if s.source})
    evidence_count = len({e for s in signals for e in s.evidence_ids})
    diversity = min(1.0, source_count / 3.0)
    evidence = min(1.0, evidence_count / 3.0)
    confidence = _clip(0.55 * quality + 0.25 * diversity + 0.20 * evidence)
    return round(confidence, 6), round(1.0 - confidence, 6)


def interpret(
    entity_id: str,
    entity_type: str,
    signals: Iterable[Signal | dict[str, Any]],
) -> Interpretation:
    normalized = normalize_signals(signals)
    if not normalized:
        return Interpretation(
            entity_id=str(entity_id),
            entity_type=str(entity_type),
            state="unknown",
            plain_language="No observable signal was supplied, so no state can be inferred.",
            confidence=0.0,
            uncertainty=1.0,
            evidence_ids=(),
            signals_used=(),
        )

    # The score is a normalized descriptive signal index, not a measurement
    # of subjective experience. Equal weighting is intentional and auditable.
    score = sum(s.value * s.quality for s in normalized) / max(
        1e-12, sum(s.quality for s in normalized)
    )
    state = _state(score)
    confidence, uncertainty = _confidence(normalized)
    evidence_ids = tuple(
        sorted({e for s in normalized for e in s.evidence_ids})
    )
    names = tuple(s.name for s in normalized)

    language = (
        f"Observable signals indicate a {state} level of the measured "
        f"state for this {entity_type}. This describes recorded signals, "
        f"not a proof of subjective feeling or consciousness."
    )
    return Interpretation(
        entity_id=str(entity_id),
        entity_type=str(entity_type),
        state=state,
        plain_language=language,
        confidence=confidence,
        uncertainty=uncertainty,
        evidence_ids=evidence_ids,
        signals_used=names,
    )


def interpret_batch(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for record in records:
        result = interpret(
            entity_id=str(record.get("entity_id", "unknown")),
            entity_type=str(record.get("entity_type", "entity")),
            signals=record.get("signals", ()),
        )
        out.append({"schema_version": SCHEMA_VERSION, **result.as_dict()})
    return out
