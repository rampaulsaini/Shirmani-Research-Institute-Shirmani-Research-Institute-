"""Deterministic signal-to-language contract for the Supreme NLP layer."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from math import isfinite
from typing import Mapping, Sequence
import json
from pathlib import Path

@dataclass(frozen=True)
class SignalObservation:
    source: str
    features: Mapping[str, float]
    timestamp: str | None = None
    unit: str | None = None

    def validate(self) -> None:
        if not self.source.strip():
            raise ValueError("source is required")
        for key, value in self.features.items():
            if not str(key).strip():
                raise ValueError("feature name cannot be empty")
            if not isinstance(value, (int, float)) or not isfinite(float(value)):
                raise ValueError(f"feature {key!r} must be a finite number")

@dataclass(frozen=True)
class NLPInterpretation:
    observation_id: str
    plain_language: str
    evidence: tuple[str, ...]
    confidence: float
    uncertainty: str
    experience_claim: str = "not_established"

    def validate(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.experience_claim not in {"not_established", "supported", "unknown"}:
            raise ValueError("invalid experience_claim")

def observation_to_language(observation: SignalObservation, observation_id: str, *, baseline: Mapping[str, float] | None = None) -> NLPInterpretation:
    observation.validate()
    baseline = baseline or {}
    evidence: list[str] = []
    changes: list[float] = []
    for key, value in observation.features.items():
        if key not in baseline:
            evidence.append(f"{key}={float(value):.6g}")
            continue
        delta = float(value) - float(baseline[key])
        changes.append(abs(delta))
        direction = "increased" if delta > 0 else "decreased" if delta < 0 else "unchanged"
        evidence.append(f"{key} {direction} by {abs(delta):.6g}")
    magnitude = sum(changes) / len(changes) if changes else 0.0
    confidence = min(0.99, 0.50 + min(magnitude, 1.0) * 0.40) if changes else 0.50
    uncertainty = (
        "measured change detected; interpretation is signal-level, not a proof of subjective experience"
        if changes else
        "no baseline comparison; interpretation is limited to the observed measurements"
    )
    plain = f"Observed measurable signals from {observation.source}. " + (
        "; ".join(evidence) if evidence else "No usable features were supplied."
    ) + "."
    result = NLPInterpretation(
        observation_id=observation_id,
        plain_language=plain,
        evidence=tuple(evidence),
        confidence=round(confidence, 4),
        uncertainty=uncertainty,
    )
    result.validate()
    return result

def write_contract_report(observations: Sequence[SignalObservation], output_path: str = "generated/supreme-nlp-signal-contract.json") -> dict:
    results = [asdict(observation_to_language(o, f"obs-{i:04d}")) for i, o in enumerate(observations, 1)]
    report = {
        "contract": "supreme-nlp-signal-contract-v1",
        "fail_closed": True,
        "measured_signals_are_not_subjective-experience_proof": True,
        "observations": results,
    }
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report

if __name__ == "__main__":
    report = write_contract_report([
        SignalObservation(source="example-sensor", features={"electrical_signal": 0.82, "vibration": 0.31}, unit="normalized")
    ])
    print(json.dumps(report, ensure_ascii=False, indent=2))
