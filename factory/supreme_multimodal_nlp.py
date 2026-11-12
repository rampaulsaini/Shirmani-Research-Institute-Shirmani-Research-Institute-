"""Evidence-aware multimodal signal -> language translation layer.

This is a deterministic contract layer: it does not claim that a sensor signal
is a subjective feeling. It converts measured features into bounded semantic
descriptions, preserves provenance, and exposes uncertainty explicitly.
"""
from __future__ import annotations
import math
import statistics
from typing import Any

SCHEMA_VERSION="1.0"

def _finite(x: Any) -> bool:
    return isinstance(x,(int,float)) and math.isfinite(float(x))

def normalize_signal(values: list[float]) -> dict[str,float]:
    xs=[float(x) for x in values if _finite(x)]
    if not xs:
        return {"n":0.0,"mean":0.0,"std":0.0,"min":0.0,"max":0.0,"range":0.0}
    mean=statistics.fmean(xs)
    std=statistics.pstdev(xs) if len(xs)>1 else 0.0
    return {"n":float(len(xs)),"mean":mean,"std":std,"min":min(xs),"max":max(xs),"range":max(xs)-min(xs)}

def classify_signal(values: list[float], context: dict[str,Any]|None=None) -> dict[str,Any]:
    context=context or {}
    s=normalize_signal(values)
    if s["n"]==0:
        return {"label":"NO_SIGNAL","confidence":0.0,"evidence":["no finite measurements"],"interpretation":"कोई वैध माप उपलब्ध नहीं है।"}
    cv=s["std"]/abs(s["mean"]) if s["mean"] else s["std"]
    if cv < 0.05:
        label="STABLE_PATTERN"
        interpretation="माप में अपेक्षाकृत स्थिर पैटर्न दिखाई देता है।"
    elif cv < 0.20:
        label="MODERATE_VARIATION"
        interpretation="माप में मध्यम परिवर्तनशीलता दिखाई देती है।"
    else:
        label="HIGH_VARIATION"
        interpretation="माप में अपेक्षाकृत अधिक परिवर्तनशीलता दिखाई देती है।"
    # Confidence reflects signal quality, not probability of an inner mental state.
    quality=min(1.0, math.log1p(s["n"])/math.log(101))
    if context.get("calibrated") is True:
        quality=min(1.0,quality+0.10)
    return {
        "label":label,
        "confidence":round(quality,6),
        "signal_statistics":{k:round(v,6) for k,v in s.items()},
        "evidence":["finite sensor measurements","dispersion analysis"],
        "interpretation":interpretation,
        "claim_boundary":"Observed signal pattern only; no subjective feeling is asserted.",
    }

def translate_to_simple_language(result: dict[str,Any]) -> str:
    label=result.get("label","UNKNOWN")
    c=float(result.get("confidence",0.0))
    text=result.get("interpretation","डेटा का पर्याप्त अर्थ नहीं निकाला जा सका।")
    return f"{text} संकेत-गुणवत्ता confidence {c:.0%} है। निष्कर्ष केवल उपलब्ध मापों पर आधारित है; इसे स्वयं अनुभव/भावना का प्रत्यक्ष प्रमाण नहीं माना गया है।"

def evaluate_multimodal(records: list[dict[str,Any]]) -> dict[str,Any]:
    outputs=[]
    missing_provenance=0
    for row in records:
        source=row.get("source_id")
        if not source: missing_provenance+=1
        result=classify_signal(row.get("values",[]),row.get("context",{}))
        result["source_id"]=source
        result["modality"]=row.get("modality","unknown")
        result["simple_language"]=translate_to_simple_language(result)
        outputs.append(result)
    return {
        "schema_version":SCHEMA_VERSION,
        "records":len(records),
        "missing_provenance":missing_provenance,
        "outputs":outputs,
        "fail_closed":missing_provenance==0,
        "claim_policy":"Signals are translated into bounded observations; subjective experience is never inferred as established fact.",
    }
