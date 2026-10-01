"""Evidence-first translation of observable signals into plain-language summaries."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Mapping, Sequence
import math
SCHEMA_VERSION = "1.0"
@dataclass(frozen=True)
class SignalObservation:
    modality: str
    metric: str
    value: float
    baseline: float
    unit: str = ""
    direction: str = "unknown"
    source: str = "unspecified"
@dataclass(frozen=True)
class SignalInterpretation:
    observation: str
    possible_state: str
    confidence: float
    evidence: tuple[str, ...]
    limitations: tuple[str, ...]
    status: str = "MODEL_INFERENCE_NOT_PROOF"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, float(value)))
def standardized_deviation(value: float, baseline: float, scale: float | None = None) -> float:
    if not all(math.isfinite(float(x)) for x in (value, baseline)): raise ValueError("value and baseline must be finite")
    if scale is None: scale = max(abs(float(baseline)) * 0.10, 1e-9)
    if not math.isfinite(float(scale)) or float(scale) <= 0: raise ValueError("scale must be a positive finite number")
    return (float(value) - float(baseline)) / float(scale)
def summarize_signal(observations: Sequence[SignalObservation], *, state_labels: Mapping[str, str] | None = None) -> SignalInterpretation:
    if not observations:
        return SignalInterpretation("No measurable signal was supplied.","INSUFFICIENT_DATA",0.0,(),("No observation was available for interpretation.",))
    deviations, evidence = [], []
    for item in observations:
        z=standardized_deviation(item.value,item.baseline); deviations.append(abs(z))
        direction=item.direction if item.direction!="unknown" else ("above" if z>0 else "below" if z<0 else "near")
        evidence.append(f"{item.modality}:{item.metric}={item.value:g}{item.unit} (baseline {item.baseline:g}{item.unit}; {direction})")
    strength=sum(min(d,3.0) for d in deviations)/(3.0*len(deviations))
    confidence=_clamp(0.50+0.45*strength)
    label=state_labels.get("default","observable change from baseline") if state_labels else "observable change from baseline"
    return SignalInterpretation(f"Measured data show {label}.",label,round(confidence,4),tuple(evidence),("This is an inference from measured signals, not proof of subjective feeling.","Domain-specific biological interpretation requires validated training data and independent testing."))
