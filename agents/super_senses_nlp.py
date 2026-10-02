"""SHIRMANI Super-Senses NLP fusion layer.
Sensor-agnostic, deterministic multimodal control plane. It translates
observable signal patterns into simple language while preserving provenance,
disagreement, uncertainty and fail-closed governance.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Iterable
import hashlib, json, math

VERSION = "super-senses-nlp-v1"

@dataclass(frozen=True)
class Sense:
    modality: str
    feature: str
    value: float
    quality: float = 1.0
    source: str = "unknown"
    timestamp: str = ""
    unit: str = ""
    baseline_mean: float | None = None
    baseline_std: float | None = None

def _num(v: Any, default: float = 0.0) -> float:
    try: x = float(v)
    except (TypeError, ValueError): return default
    return x if math.isfinite(x) else default

def _clip(v: Any) -> float:
    return max(0.0, min(1.0, _num(v)))

def normalize(raw: dict[str, Any]) -> Sense:
    return Sense(
        modality=str(raw.get("modality","unknown")).strip().lower() or "unknown",
        feature=str(raw.get("feature","unknown")).strip().lower() or "unknown",
        value=_num(raw.get("value")),
        quality=_clip(raw.get("quality",1.0)),
        source=str(raw.get("source","unknown")).strip() or "unknown",
        timestamp=str(raw.get("timestamp","")).strip(),
        unit=str(raw.get("unit","")).strip(),
        baseline_mean=None if raw.get("baseline_mean") is None else _num(raw.get("baseline_mean")),
        baseline_std=None if raw.get("baseline_std") is None else max(0.0,_num(raw.get("baseline_std"))),
    )

def _fp(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def _agreement(rows: list[Sense]) -> float:
    groups: dict[str,list[float]] = {}
    for r in rows: groups.setdefault(r.feature,[]).append(r.value)
    scores=[]
    for vals in groups.values():
        if len(vals)<2: continue
        mean=sum(vals)/len(vals)
        spread=math.sqrt(sum((x-mean)**2 for x in vals)/len(vals))
        scores.append(max(0.0,1.0-min(1.0,spread/(3*max(abs(mean)*0.05,1e-9)))))
    return round(sum(scores)/len(scores),4) if scores else 0.0

def _drift(rows: list[Sense]) -> float:
    scores=[]
    for r in rows:
        if r.baseline_mean is None: continue
        scale=max(r.baseline_std or 0.0,abs(r.baseline_mean)*0.05,1e-9)
        scores.append(min(1.0,abs(r.value-r.baseline_mean)/(3*scale)))
    return round(sum(scores)/len(scores),4) if scores else 0.0

def fuse(observations: Iterable[dict[str,Any]], request: str = "", feature_adapter: str = "none") -> dict[str,Any]:
    rows=[normalize(x) for x in observations]
    usable=[r for r in rows if r.quality>0]
    modalities=sorted({r.modality for r in usable})
    sources=sorted({r.source for r in usable if r.source!="unknown"})
    quality=round(sum(r.quality for r in usable)/len(usable),4) if usable else 0.0
    agreement=_agreement(usable)
    drift=_drift(usable)
    if not usable: status,evidence_class,state="NO_CLAIM","UNKNOWN","UNKNOWN"
    elif agreement < .25: status,evidence_class,state="BLOCKED","CONFLICTED","CONFLICTING_SIGNALS"
    elif drift >= .66: status,evidence_class,state="CANDIDATE","INFERRED","STRONG_BASELINE_DEVIATION"
    elif agreement < .50: status,evidence_class,state="CANDIDATE","INFERRED","HIGH_VARIABILITY_PATTERN"
    elif drift >= .33: status,evidence_class,state="CANDIDATE","INFERRED","MODERATE_BASELINE_DEVIATION"
    else: status,evidence_class,state="CANDIDATE","INFERRED","STABLE_PATTERN"
    diversity=min(1.0,len(modalities)/4)
    replication=min(1.0,len(sources)/3)
    confidence=round(max(0.0,min(1.0,
        .30*quality+.30*agreement+.15*diversity+.15*replication+.10*(1-drift))),4) if usable else 0.0
    record={
      "schema_version":VERSION,"generated_at":datetime.now(timezone.utc).isoformat(),
      "request":request,"status":status,"evidence_class":evidence_class,"state":state,
      "metrics":{"observations":len(rows),"usable_observations":len(usable),"modalities":modalities,
                 "sources":sources,"quality":quality,"agreement":agreement,"baseline_drift":drift,
                 "diversity":round(diversity,4),"replication":round(replication,4),"confidence":confidence},
      "translation":{
        "hi":("पर्याप्त उपयोगी संकेत नहीं मिले; निष्कर्ष रोक दिया गया।" if status=="NO_CLAIM"
              else "अलग-अलग संकेतों में पर्याप्त असहमति है; इसलिए निष्कर्ष रोक दिया गया है।" if status=="BLOCKED"
              else f"प्राप्त {len(usable)} उपयोगी संकेतों में '{state}' जैसा computational पैटर्न मिला। सीमित confidence {confidence:.0%} है."),
        "en":("Insufficient usable signals; no claim is produced." if status=="NO_CLAIM"
              else "Signals disagree materially; interpretation is blocked." if status=="BLOCKED"
              else f"{len(usable)} usable observations show a {state.lower()} pattern; bounded confidence is {confidence:.0%}.")},
      "evidence":{"observations":[asdict(r) for r in rows],"feature_adapter":feature_adapter},
      "uncertainty":{"explicit":True,"calibration":"NOT_ESTABLISHED","subjective_experience_inference":False,
                     "alternative_explanations_required":True},
      "verification":{"status":"UNVERIFIED","independent_required":True,"promotion_allowed":False},
      "governance":{"fail_closed":True,"accuracy_is_measured_not_declared":True,
                    "scheduled_code_mutation_allowed":False,"subjective_experience_claim_allowed":False},
    }
    record["fingerprint"]=_fp(record)
    return record

def build_record(observations: Iterable[dict[str,Any]], request: str = "", feature_adapter: str = "none") -> dict[str,Any]:
    return fuse(observations,request,feature_adapter)
