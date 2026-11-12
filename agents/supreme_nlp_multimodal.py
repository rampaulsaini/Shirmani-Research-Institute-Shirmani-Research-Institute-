"""Evidence-preserving multimodal control plane for SHIRMANI Supreme NLP."""
from __future__ import annotations
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib, json, math
from typing import Any, Iterable

VERSION = "supreme-nlp-multimodal-v2"

@dataclass(frozen=True)
class Observation:
    modality: str
    feature: str
    value: float
    quality: float
    source: str
    timestamp: str
    unit: str = ""
    baseline_mean: float | None = None
    baseline_std: float | None = None

def _num(v: Any, default=0.0) -> float:
    try: x=float(v)
    except (TypeError, ValueError): return default
    return x if math.isfinite(x) else default

def _clip(v: Any) -> float:
    return max(0.0, min(1.0, _num(v)))

def normalize(raw: dict[str, Any]) -> Observation:
    def opt(name):
        return None if raw.get(name) is None else _num(raw.get(name))
    return Observation(
        modality=str(raw.get("modality","unknown")).strip().lower() or "unknown",
        feature=str(raw.get("feature","unknown")).strip().lower() or "unknown",
        value=_num(raw.get("value")),
        quality=_clip(raw.get("quality",1.0)),
        source=str(raw.get("source","unknown")).strip() or "unknown",
        timestamp=str(raw.get("timestamp","")).strip(),
        unit=str(raw.get("unit","")).strip(),
        baseline_mean=opt("baseline_mean"),
        baseline_std=None if opt("baseline_std") is None else max(0.0,opt("baseline_std")),
    )

def _stable(v: Any) -> str:
    return json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(",",":"))

def fingerprint(record: dict[str, Any]) -> str:
    x=dict(record)
    x.pop("fingerprint",None)
    provenance=dict(x.get("provenance") or {})
    provenance.pop("fingerprint",None)
    x["provenance"]=provenance
    return hashlib.sha256(_stable(x).encode()).hexdigest()

def _agreement(rows: list[Observation]) -> float:
    # Compare only like-for-like measurements. Different units are not
    # numerically comparable without an explicit conversion contract.
    groups=defaultdict(list)
    for r in rows: groups[(r.feature, r.unit)].append(r.value)
    scores=[]
    for vals in groups.values():
        if len(vals)<2: continue
        mean=sum(vals)/len(vals)
        spread=math.sqrt(sum((v-mean)**2 for v in vals)/len(vals))
        scores.append(max(0.0,1.0-min(1.0,spread/(3*(abs(mean)+1e-9)))))
    return sum(scores)/len(scores) if scores else 0.0

def _drift(rows: list[Observation]) -> float:
    scores=[]
    for r in rows:
        if r.baseline_mean is None: continue
        scale=max(r.baseline_std or 0.0,abs(r.baseline_mean)*0.05,1e-9)
        scores.append(min(1.0,abs(r.value-r.baseline_mean)/(3*scale)))
    return sum(scores)/len(scores) if scores else 0.0

def analyze(observations: Iterable[dict[str,Any]], request="", source_type="unknown") -> dict[str,Any]:
    rows=[normalize(x) for x in observations]
    usable=[r for r in rows if r.quality>0]
    modalities=sorted({r.modality for r in usable})
    sources=sorted({r.source for r in usable if r.source!="unknown"})
    quality=sum(r.quality for r in usable)/len(usable) if usable else 0.0
    agreement=_agreement(usable)
    drift=_drift(usable)
    calibrated=sum(r.baseline_mean is not None and r.baseline_std is not None for r in usable)
    calibration=("NOT_APPLICABLE" if not usable else
                 "BASELINE_PRESENT" if calibrated==len(usable) else
                 "PARTIAL_BASELINE" if calibrated else "UNCALIBRATED")
    confidence=round(max(0,min(1,
        .20*quality+.25*agreement+.15*min(1,len(modalities)/3)+
        .15*min(1,len(sources)/3)+.15*(1-drift)+
        .10*(calibration=="BASELINE_PRESENT"))),4)

    if not usable:
        evidence_class,status,state,reason="UNKNOWN","NO_CLAIM","UNKNOWN","NO_USABLE_SIGNAL"
    elif len(usable)>=2 and agreement<.25:
        evidence_class,status,state,reason="UNKNOWN","BLOCKED","CONFLICTING","CONFLICTING_OBSERVATIONS"
    else:
        evidence_class,status="INFERRED","CANDIDATE"
        state="STABLE_PATTERN" if agreement>=.67 else "MODERATE_VARIABILITY_PATTERN" if agreement>=.34 else "HIGH_VARIABILITY_PATTERN"
        reason="MODEL_SUPPORTED_SIGNAL_PATTERN"

    limitations=[
        "यह observable signal data की computational interpretation है।",
        "Signal interpretation अपने-आप subjective experience, consciousness या feeling का प्रमाण नहीं है।",
        "Confidence bounded heuristic है; calibrated scientific probability नहीं।",
        "Scientific performance claims के लिए labelled datasets और independent replication आवश्यक हैं।",
    ]
    if len(modalities)<2: limitations.append("Multimodal corroboration उपलब्ध नहीं है।")
    comparable_groups=len({(r.feature,r.unit) for r in usable if r.unit})
    if comparable_groups == 0: limitations.append("Measurement units declared नहीं हैं; cross-unit numerical agreement का दावा नहीं किया गया।")
    if calibration=="UNCALIBRATED": limitations.append("Baseline calibration उपलब्ध नहीं है।")

    record={
      "schema_version":VERSION,
      "generated_at":datetime.now(timezone.utc).isoformat(),
      "source_type":source_type,
      "evidence_class":evidence_class,
      "status":status,
      "claims":[f"Observed {len(usable)} usable observations across {len(modalities)} modalities.",
                f"Detected computational state: {state}."] ,
      "provenance":{"source":"agents/supreme_nlp_multimodal.py","timestamp":datetime.now(timezone.utc).isoformat(),"fingerprint":""},
      "metrics":{"observations":len(rows),"usable_observations":len(usable),"modalities":modalities,
                 "sources":sources,"quality":round(quality,4),"agreement":round(agreement,4),
                 "comparable_measurement_groups":comparable_groups,
                 "baseline_drift":round(drift,4),"calibration_status":calibration},
      "confidence":confidence,
      "uncertainty":{"status":"EXPLICIT","reason":reason,"abstention_available":True},
      "limitations":limitations,
      "verification":{"status":"UNVERIFIED","independent_required":True,"promotion_allowed":False},
      "observations":[asdict(r) for r in rows],
    }
    record["provenance"]["fingerprint"]=fingerprint(record)
    return record

def to_simple_language(record, language="hi"):
    if record["status"]=="NO_CLAIM":
        return "पर्याप्त उपयोगी संकेत नहीं मिले; इसलिए कोई निष्कर्ष नहीं दिया गया।"
    if record["status"]=="BLOCKED":
        return "प्राप्त संकेतों में पर्याप्त असहमति है; इसलिए निष्कर्ष रोक दिया गया है।"
    state=record["claims"][1].split(": ",1)[-1]
    if language=="en":
        return f"Observed {record['metrics']['usable_observations']} usable signals. Detected {state}; bounded confidence {record['confidence']:.0%}. This is signal interpretation, not proof of subjective experience."
    return f"{record['metrics']['usable_observations']} उपयोगी संकेतों में '{state}' जैसा computational पैटर्न मिला। bounded confidence {record['confidence']:.0%} है। यह संकेतों की व्याख्या है, प्रत्यक्ष भाव या चेतना का प्रमाण नहीं।"
