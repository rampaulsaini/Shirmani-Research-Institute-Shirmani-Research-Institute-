"""Super-Senses evidence layer for SHIRMANI Supreme NLP."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib, json, math
from statistics import median
from typing import Any, Iterable

VERSION = "super-senses-v1"

@dataclass(frozen=True)
class Observation:
    modality: str
    feature: str
    value: float
    quality: float
    source: str
    timestamp: str = ""
    unit: str = ""
    baseline: float | None = None
    tolerance: float | None = None

def _finite(v: Any, default=0.0) -> float:
    try:
        x=float(v)
        return x if math.isfinite(x) else default
    except (TypeError, ValueError):
        return default

def _clip(v: Any) -> float:
    return max(0.0, min(1.0, _finite(v)))

def normalize(x: dict[str, Any]) -> Observation:
    b=None if x.get("baseline") is None else _finite(x.get("baseline"))
    t=None if x.get("tolerance") is None else max(1e-12, _finite(x.get("tolerance")))
    return Observation(
        modality=str(x.get("modality","unknown")).strip().lower() or "unknown",
        feature=str(x.get("feature","unknown")).strip().lower() or "unknown",
        value=_finite(x.get("value")),
        quality=_clip(x.get("quality",1.0)),
        source=str(x.get("source","unknown")).strip() or "unknown",
        timestamp=str(x.get("timestamp","")).strip(),
        unit=str(x.get("unit","")).strip(),
        baseline=b, tolerance=t)

def _hash(payload: Any) -> str:
    return hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def _agreement(rows: list[Observation]) -> float:
    groups={}
    for r in rows:
        groups.setdefault(r.feature,[]).append(r.value)
    scores=[]
    for vals in groups.values():
        if len(vals)<2: continue
        m=median(vals)
        spread=math.sqrt(sum((v-m)**2 for v in vals)/len(vals))
        scores.append(max(0.0,1.0-spread/(3*max(abs(m),1e-9))))
    return sum(scores)/len(scores) if scores else 0.0

def _anomaly(rows: list[Observation]) -> float:
    scores=[]
    for r in rows:
        if r.baseline is None: continue
        tol=r.tolerance or max(abs(r.baseline)*0.05,1e-9)
        scores.append(min(1.0,abs(r.value-r.baseline)/(3*tol)))
    return sum(scores)/len(scores) if scores else 0.0

def analyze(observations: Iterable[dict[str,Any]], request: str = "") -> dict[str,Any]:
    raw=[normalize(x) for x in observations]
    usable=[x for x in raw if x.quality>0]
    modalities=sorted({x.modality for x in usable})
    sources=sorted({x.source for x in usable if x.source!="unknown"})
    quality=sum(x.quality for x in usable)/len(usable) if usable else 0.0
    agreement=_agreement(usable)
    anomaly=_anomaly(usable)
    completeness=(sum(bool(x.timestamp) for x in usable)/len(usable)) if usable else 0.0
    corroboration=0.5*min(1.0,len(modalities)/4)+0.5*min(1.0,len(sources)/4)
    confidence=round(max(0.0,min(1.0,
        .30*quality+.25*agreement+.20*corroboration+
        .15*(1-anomaly)+.10*completeness)),4)

    if not usable:
        status,evidence,reason="ABSTAIN","UNRESOLVED","NO_USABLE_SIGNAL"
    elif len(usable)>=2 and agreement<.25:
        status,evidence,reason="ABSTAIN","UNRESOLVED","CROSS_MODAL_CONFLICT"
    elif confidence<.55:
        status,evidence,reason="ABSTAIN","HYPOTHESIS","LOW_CONFIDENCE"
    else:
        status,evidence,reason="CANDIDATE","INFERRED","OBSERVABLE_PATTERN"

    summary=("पर्याप्त विश्वसनीय observable signal नहीं मिला; प्रणाली निष्कर्ष रोक रही है."
      if status=="ABSTAIN" else
      f"{len(usable)} उपयोगी संकेतों और {len(modalities)} modalities से एक computational pattern मिला है। "
      "इसे observable-signal interpretation के रूप में पढ़ना चाहिए, प्रत्यक्ष subjective experience के प्रमाण के रूप में नहीं।")
    record={
      "schema_version":VERSION,
      "created_at":datetime.now(timezone.utc).isoformat(),
      "request":request,"status":status,"evidence_class":evidence,"summary":summary,
      "metrics":{"observations":len(raw),"usable":len(usable),"modalities":modalities,
        "sources":sources,"quality":round(quality,4),"cross_modal_agreement":round(agreement,4),
        "anomaly_score":round(anomaly,4),"timestamp_completeness":round(completeness,4)},
      "confidence":confidence,"uncertainty":{"reason":reason,"abstention":True},
      "governance":{"fail_closed":True,"subjective_experience_claim_allowed":False,
        "production_code_mutation_allowed":False,"independent_verification_required":True,
        "accuracy_is_measured_not_declared":True},
      "limitations":[
        "Observable signals की computational interpretation subjective experience को सीधे सिद्ध नहीं करती।",
        "Confidence calibrated scientific probability नहीं है जब तक labelled validation न हो।",
        "Independent datasets, replication और domain-specific sensors आवश्यक हैं।"],
      "observations":[asdict(x) for x in raw]}
    record["fingerprint"]=_hash(record)
    return record

def to_simple_language(record: dict[str,Any]) -> str:
    return record["summary"] + f" Confidence: {record['confidence']:.0%}."

if __name__=="__main__":
    print(json.dumps(analyze([
      {"modality":"audio","feature":"signal","value":1.0,"quality":1,"source":"demo-a"},
      {"modality":"electrical","feature":"signal","value":1.01,"quality":1,"source":"demo-b"}]),
      ensure_ascii=False,indent=2))
