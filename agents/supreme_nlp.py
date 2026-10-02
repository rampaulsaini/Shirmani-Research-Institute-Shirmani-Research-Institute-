"""Supreme NLP v3: evidence-first, modality-aware signal interpretation."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import sqrt, isfinite
from collections import defaultdict
from typing import Any, Dict, Iterable
import hashlib, json

VERSION = "supreme-nlp-v3"

@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    unit: str = ""
    quality: float = 1.0
    source: str = "unknown"
    timestamp: str = ""
    baseline_mean: float | None = None
    baseline_std: float | None = None

def _clip(x: Any, lo=0.0, hi=1.0) -> float:
    try:
        v=float(x)
        return lo if not isfinite(v) else max(lo,min(hi,v))
    except (TypeError,ValueError):
        return lo

def _num(x, default=0.0):
    try:
        v=float(x)
        return v if isfinite(v) else default
    except (TypeError,ValueError):
        return default

def normalize_signal(raw: Dict[str,Any]) -> Signal:
    def opt(name):
        try:
            v=raw.get(name)
            if v is None: return None
            v=float(v)
            return v if isfinite(v) else None
        except (TypeError,ValueError):
            return None
    return Signal(
        modality=str(raw.get("modality","unknown")).strip().lower() or "unknown",
        feature=str(raw.get("feature","unknown")).strip() or "unknown",
        value=_num(raw.get("value",0.0)),
        unit=str(raw.get("unit","")).strip(),
        quality=_clip(raw.get("quality",1.0)),
        source=str(raw.get("source","unknown")).strip() or "unknown",
        timestamp=str(raw.get("timestamp","")),
        baseline_mean=opt("baseline_mean"),
        baseline_std=opt("baseline_std"))

def _key(s): return (s.modality,s.feature,s.unit)

def _z(s):
    if s.baseline_mean is None or s.baseline_std is None or s.baseline_std<=0: return None
    return (s.value-s.baseline_mean)/s.baseline_std

def _drift(rows):
    z=[min(1.0,abs(v)/3.0) for s in rows if (v:=_z(s)) is not None]
    return sum(z)/len(z) if z else 0.0

def _groups(rows):
    groups=defaultdict(list)
    for s in rows: groups[_key(s)].append(s)
    out=[]
    for (modality,feature,unit),vals in sorted(groups.items()):
        numbers=[s.value for s in vals]
        mean=sum(numbers)/len(numbers)
        spread=sqrt(sum((v-mean)**2 for v in numbers)/len(numbers))
        scale=max(abs(mean)*0.05,1e-12)
        dispersion=min(1.0,spread/(3*scale))
        sources=sorted({s.source for s in vals if s.source!="unknown"})
        out.append({"modality":modality,"feature":feature,"unit":unit,
                    "sample_count":len(vals),"mean":round(mean,8),
                    "spread":round(spread,8),"dispersion":round(dispersion,6),
                    "agreement":round(1-dispersion,6),"sources":sources})
    return out

def _grade(count,quality,groups,sources):
    score=.30*_clip(count/20)+.30*quality+.20*_clip(groups/4)+.20*_clip(sources/3)
    return "A" if score>=.85 else "B" if score>=.70 else "C" if score>=.50 else "D"

def summarize(signals: Iterable[Dict[str,Any]]) -> Dict[str,Any]:
    rows=[normalize_signal(x) for x in signals]
    if not rows: return {"status":"no_data","interpretation":None,"signals":[]}
    usable=[s for s in rows if s.quality>0]
    if not usable:
        return {"status":"insufficient_quality","interpretation":None,
                "signals":[asdict(s) for s in rows]}
    groups=_groups(usable)
    agreement=sum(g["agreement"] for g in groups)/len(groups)
    quality=sum(s.quality for s in usable)/len(usable)
    modalities=sorted({s.modality for s in usable})
    sources=sorted({s.source for s in usable if s.source!="unknown"})
    # Different physical units/modalities are never combined into one raw mean.
    confidence=round(_clip(.10+.35*quality+.25*agreement+
                            .15*_clip(len(usable)/20)+
                            .10*_clip(len(modalities)/4)+.05*_clip(len(sources)/3)),4)
    max_disp=max((g["dispersion"] for g in groups),default=1.0)
    state=("high_within_group_variability" if max_disp>=.66 else
           "moderate_within_group_variability" if max_disp>=.33 else
           "relatively_stable_within_group")
    evidence=[f"{s.modality}:{s.feature}={s.value}{s.unit} "
              f"(quality={s.quality:.2f}; source={s.source})" for s in usable]
    limitations=[
      "यह observable/measurable signals की model-based interpretation है; subjective feeling, consciousness या intention का direct proof नहीं।",
      "अलग modalities/units को raw mean में नहीं मिलाया गया; agreement केवल compatible groups में मापा गया है।",
      "Confidence UNCALIBRATED है जब तक task-specific labelled evaluation data से calibration स्थापित न हो।",
      "Sensor artefacts, confounding variables और alternative explanations के लिए independent controls आवश्यक हैं।"]
    return {
      "status":"interpreted","claim_type":"MEASURABLE_SIGNAL_INTERPRETATION",
      "interpretation":{"state":state,"confidence":confidence,
        "confidence_status":"UNCALIBRATED","evidence":evidence,"limitations":limitations},
      "features":{
        "mean":round(sum(g["mean"] for g in groups)/len(groups),8),
        "spread":round(sum(g["spread"] for g in groups)/len(groups),8),
        "anomaly_score":round(1-agreement,4),"agreement":round(agreement,4),
        "quality":round(quality,4),"modalities":len(modalities),
        "modality_names":modalities,"independent_sources":len(sources),
        "source_names":sources,"sample_count":len(usable),
        "drift_score":round(_drift(usable),4),"compatible_groups":len(groups),
        "group_summaries":groups,
        "evidence_grade":_grade(len(usable),quality,len(groups),len(sources))},
      "verification":{"status":"UNVERIFIED","independent_required":True,
                      "replication_required":True,"promotion_allowed":False},
      "signals":[asdict(s) for s in rows]}

def to_simple_language(result):
    if result.get("status")!="interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है, इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i,f=result["interpretation"],result["features"]
    return (f"मापे गए संकेतों में '{i['state']}' जैसा pattern दिखाई देता है। "
            f"प्रारंभिक, uncalibrated confidence {i['confidence']:.0%} और evidence grade "
            f"{f['evidence_grade']} है। अलग-अलग signal प्रकारों को compatible श्रेणियों "
            "में अलग रखकर तुलना की गई है। यह measurable signal interpretation है; "
            "इसे किसी जीव के प्रत्यक्ष भाव, चेतना या subjective experience का प्रमाण नहीं माना जा सकता।")

def fingerprint(result):
    return hashlib.sha256(json.dumps(result,sort_keys=True,ensure_ascii=False,
                                     separators=(",",":")).encode()).hexdigest()

def build_record(signals,task_id):
    result=summarize(signals)
    return {"schema_version":VERSION,"task_id":task_id,
            "generated_at":datetime.now(timezone.utc).isoformat(),
            "pipeline":"observe->normalize->quality->compatible-grouping->feature->multimodal-evidence-fusion->interpret->NLP->confidence->independent-verification->audit",
            "result":result,"simple_language":to_simple_language(result),
            "fingerprint":fingerprint(result),
            "provenance":{"generator":"agents/supreme_nlp.py",
                          "contract":"observable-signal-only",
                          "verification_status":"UNVERIFIED",
                          "confidence_status":result.get("interpretation",{}).get("confidence_status","NOT_AVAILABLE")}}
