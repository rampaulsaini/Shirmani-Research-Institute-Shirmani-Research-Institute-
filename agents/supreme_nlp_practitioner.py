"""High-integrity multimodal NLP practitioner.

Converts observable multimodal signals into plain language without claiming
unmeasured subjective experience. Designed for deterministic Automission,
provenance, calibration, and fail-closed interpretation.
"""
from __future__ import annotations
import hashlib, json, math
from collections import defaultdict
from datetime import datetime, timezone
from statistics import mean, pstdev
from typing import Any, Iterable

ALLOWED_STATUS={"no_data","insufficient_quality","interpreted","conflict"}
MIN_QUALITY=0.50
MIN_SIGNALS=2

def _clip(x: float, lo=0.0, hi=1.0) -> float:
    return max(lo, min(hi, float(x)))

def normalize(rows: Iterable[dict[str,Any]]) -> list[dict[str,Any]]:
    out=[]
    for r in rows:
        try: value=float(r.get("value",0.0))
        except (TypeError,ValueError): continue
        out.append({
            "modality":str(r.get("modality","unknown")),
            "feature":str(r.get("feature","unknown")),
            "value":value,
            "unit":str(r.get("unit","")),
            "quality":_clip(r.get("quality",1.0)),
            "source":str(r.get("source","unknown")),
            "timestamp":str(r.get("timestamp","")),
            "calibration":str(r.get("calibration","unknown")),
        })
    return out

def _agreement(groups: list[float]) -> float:
    if len(groups)<2: return 1.0
    m=mean(groups)
    if abs(m)<1e-12:
        return 1.0 if max(abs(x) for x in groups)<1e-12 else 0.0
    return _clip(1.0-pstdev(groups)/(abs(m)+1e-12))

def interpret(rows: Iterable[dict[str,Any]], task_id: str) -> dict[str,Any]:
    signals=normalize(rows)
    if not signals:
        result={"status":"no_data","signals":[],"interpretation":None}
    else:
        usable=[s for s in signals if s["quality"]>=MIN_QUALITY]
        if len(usable)<MIN_SIGNALS:
            result={"status":"insufficient_quality","signals":signals,"interpretation":None}
        else:
            by_modality=defaultdict(list)
            for s in usable: by_modality[s["modality"]].append(s["value"])
            modality_means=[mean(v) for v in by_modality.values()]
            overall=mean([s["value"] for s in usable])
            spread=pstdev([s["value"] for s in usable]) if len(usable)>1 else 0.0
            normalized_spread=_clip(spread/(abs(overall)+1e-12))
            agreement=_agreement(modality_means)
            quality=mean(s["quality"] for s in usable)
            calibration=mean(1.0 if s["calibration"] not in {"","unknown","uncalibrated"} else 0.5 for s in usable)
            confidence=_clip(0.20+0.30*quality+0.20*agreement+0.15*calibration+0.15*_clip(len(usable)/10))
            conflict=agreement<0.45
            state=("cross_modal_conflict" if conflict else
                   "high_variability_pattern" if normalized_spread>=0.66 else
                   "moderate_variability_pattern" if normalized_spread>=0.33 else
                   "stable_pattern")
            limitations=[
                "यह observable signals की model-based interpretation है; subjective feeling या consciousness का direct proof नहीं।",
                "Biological/plant/physical interpretation के लिए domain-labelled datasets, calibration और independent replication आवश्यक हैं।",
                "Confidence evidence quality और model agreement को दर्शाता है; scientific certainty नहीं।",
            ]
            result={
                "status":"conflict" if conflict else "interpreted",
                "signals":signals,
                "features":{
                    "overall_mean":overall,"spread":spread,
                    "normalized_spread":normalized_spread,
                    "agreement":agreement,"quality":quality,
                    "calibration_coverage":calibration,
                    "modalities":len(by_modality),
                    "signal_count":len(usable),
                },
                "interpretation":{
                    "state":state,"confidence":round(confidence,4),
                    "evidence":[f'{s["modality"]}:{s["feature"]}={s["value"]}{s["unit"]}; q={s["quality"]:.2f}' for s in usable],
                    "limitations":limitations,
                },
            }
    payload={"schema_version":"2.0","task_id":task_id,"pipeline":"observe->normalize->quality->calibration->cross-modal-agreement->interpret->plain-NLP->audit","result":result}
    payload["fingerprint"]=hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return payload

def plain_language(record: dict[str,Any]) -> str:
    r=record["result"]
    if r["status"]=="no_data": return "अभी कोई पर्याप्त observable signal उपलब्ध नहीं है।"
    if r["status"]=="insufficient_quality": return "संकेत उपलब्ध हैं, लेकिन उनकी गुणवत्ता/मात्रा विश्वसनीय व्याख्या के लिए पर्याप्त नहीं है।"
    i=r["interpretation"]; f=r["features"]
    if r["status"]=="conflict":
        return f"अलग-अलग संकेतों में स्पष्ट असहमति दिखाई देती है। Cross-modal agreement {f['agreement']:.0%} है; इसलिए निष्कर्ष रोककर अतिरिक्त स्वतंत्र माप लेना उचित है।"
    return f"मिले हुए observable संकेतों में '{i['state']}' जैसा pattern दिखाई देता है। Confidence {i['confidence']:.0%} है और {f['modalities']} modality उपलब्ध हैं। यह संकेतों की व्याख्या है, प्रत्यक्ष भाव/चेतना का प्रमाण नहीं।"
