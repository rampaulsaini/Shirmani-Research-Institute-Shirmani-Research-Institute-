"""Deterministic observable-signal -> plain-language interpretation layer.

Translates measured signals into bounded hypotheses with explicit uncertainty.
It does not claim to detect subjective experience, emotion, consciousness, or intent.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, asdict
from typing import Any, Mapping

SCHEMA_VERSION = "1.0"

@dataclass(frozen=True)
class SignalObservation:
    name: str
    value: float
    unit: str
    baseline: float
    tolerance: float
    direction: str = "two-sided"

def _finite(x: Any) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(float(x))

def normalize_observation(raw: Mapping[str, Any]) -> SignalObservation:
    required = ("name","value","unit","baseline","tolerance")
    missing = [k for k in required if k not in raw]
    if missing: raise ValueError("missing signal fields: " + ",".join(missing))
    if not all(_finite(raw[k]) for k in ("value","baseline","tolerance")):
        raise ValueError("numeric signal fields must be finite")
    tolerance = float(raw["tolerance"])
    if tolerance <= 0: raise ValueError("tolerance must be > 0")
    direction = str(raw.get("direction","two-sided"))
    if direction not in {"two-sided","higher-is-signal","lower-is-signal"}:
        raise ValueError("unsupported direction")
    return SignalObservation(str(raw["name"]),float(raw["value"]),str(raw["unit"]),
                             float(raw["baseline"]),tolerance,direction)

def standardized_deviation(obs: SignalObservation) -> float:
    return (obs.value - obs.baseline) / obs.tolerance

def signal_strength(obs: SignalObservation) -> float:
    z = standardized_deviation(obs)
    magnitude = max(0.0, z) if obs.direction=="higher-is-signal" else max(0.0,-z) if obs.direction=="lower-is-signal" else abs(z)
    return min(1.0, magnitude/3.0)

def classify_signal(obs: SignalObservation) -> str:
    z=standardized_deviation(obs)
    if obs.direction=="higher-is-signal":
        return "strong upward deviation" if z>=2 else "moderate upward deviation" if z>=1 else "near baseline"
    if obs.direction=="lower-is-signal":
        return "strong downward deviation" if z<=-2 else "moderate downward deviation" if z<=-1 else "near baseline"
    return "strong deviation from baseline" if abs(z)>=2 else "moderate deviation from baseline" if abs(z)>=1 else "near baseline"

def interpret(observations: list[Mapping[str,Any]], *, context="unspecified system", source_quality=1.0) -> dict[str,Any]:
    if not observations:
        return {"schema_version":SCHEMA_VERSION,"context":context,"status":"NO_SIGNAL","interpretation":"No observable signal was supplied.","confidence":0.0,"observations":[],"claim_boundary":"No subjective state is inferred without validated evidence."}
    if not _finite(source_quality) or not 0<=float(source_quality)<=1: raise ValueError("source_quality must be between 0 and 1")
    obs=[normalize_observation(x) for x in observations]
    strengths=[signal_strength(x) for x in obs]
    labels=[classify_signal(x) for x in obs]
    lead=obs[max(range(len(obs)),key=lambda i: strengths[i])]
    confidence=round(min(1.0,0.25+0.5*float(source_quality)+0.25*min(1.0,len(obs)/3.0))*(0.5+0.5*max(strengths)),6)
    return {"schema_version":SCHEMA_VERSION,"context":context,"status":"INTERPRETED",
            "interpretation":f"{lead.name} is {labels[strengths.index(max(strengths))]} relative to its supplied baseline ({lead.value:g} {lead.unit} vs {lead.baseline:g} {lead.unit}).",
            "confidence":confidence,
            "observations":[{**asdict(o),"standardized_deviation":round(standardized_deviation(o),6),"signal_strength":round(signal_strength(o),6),"classification":l} for o,l in zip(obs,labels)],
            "claim_boundary":"This output describes measured signal patterns. It does not prove consciousness, emotion, subjective experience, or intent."}

def plain_language(result: Mapping[str,Any]) -> str:
    if result.get("status")=="NO_SIGNAL": return str(result["interpretation"])
    return f"{result['interpretation']} Model confidence for this signal interpretation: {float(result['confidence']):.0%}. {result['claim_boundary']}"
