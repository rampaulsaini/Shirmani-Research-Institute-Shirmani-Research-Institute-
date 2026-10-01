"""Evidence-aware signal -> language translation layer.

Turns observable structured signals into simple language while preserving the
distinction between observation, inference, and unknown state.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Mapping

@dataclass(frozen=True)
class SignalObservation:
    entity_id: str
    entity_type: str
    signal: str
    value: float
    unit: str = ""
    source: str = ""
    observed_at: str = ""

@dataclass(frozen=True)
class LanguageInterpretation:
    entity_id: str
    statement: str
    epistemic_status: str
    confidence: float
    evidence: dict[str, Any]

def _clip(value: float) -> float:
    return max(0.0, min(1.0, float(value)))

def _label(signal: str, value: float) -> str:
    s = signal.casefold()
    if any(k in s for k in ("temperature", "heat")):
        return "temperature is elevated" if value > 0.7 else "temperature is not elevated"
    if any(k in s for k in ("moisture", "humidity", "water")):
        return "moisture/water level is high" if value > 0.7 else "moisture/water level is not high"
    if any(k in s for k in ("light", "lux")):
        return "light exposure is high" if value > 0.7 else "light exposure is low"
    if any(k in s for k in ("stress", "strain", "pressure")):
        return "stress/strain signal is high" if value > 0.7 else "stress/strain signal is low"
    if any(k in s for k in ("activity", "movement", "motion")):
        return "activity/movement is high" if value > 0.7 else "activity/movement is low"
    return f"{signal} signal is {value:.3f}"

def translate_signal(obs: SignalObservation, model_confidence: float | None = None) -> LanguageInterpretation:
    value = _clip(obs.value)
    model = _clip(model_confidence) if model_confidence is not None else 0.0
    source_ok = bool(obs.source.strip())
    confidence = round(0.65 * value + 0.25 * model + 0.10 * float(source_ok), 4)
    statement = f"{obs.entity_type} '{obs.entity_id}': {_label(obs.signal, value)}."
    if source_ok:
        status = "OBSERVED_SIGNAL_WITH_MODEL_SUPPORT" if model_confidence is not None else "OBSERVED_SIGNAL"
    else:
        status = "OBSERVED_SIGNAL_WITHOUT_SOURCE"
    return LanguageInterpretation(
        entity_id=obs.entity_id,
        statement=statement,
        epistemic_status=status,
        confidence=confidence,
        evidence={"signal": obs.signal, "value": obs.value, "unit": obs.unit, "source": obs.source,
                  "observed_at": obs.observed_at, "model_confidence": model_confidence},
    )

def translate_batch(records: list[Mapping[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in records:
        obs = SignalObservation(
            entity_id=str(row.get("entity_id", "")),
            entity_type=str(row.get("entity_type", "entity")),
            signal=str(row.get("signal", "unknown")),
            value=float(row.get("value", 0.0)),
            unit=str(row.get("unit", "")),
            source=str(row.get("source", "")),
            observed_at=str(row.get("observed_at", "")),
        )
        result = translate_signal(obs, row.get("model_confidence"))
        out.append(asdict(result))
    return out
