"""Supreme NLP Practitioner: deterministic multimodal fusion and language explanation.

Evidence-preserving control plane. It never converts a measured signal into a
claim of subjective experience.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import isfinite, sqrt
from typing import Any, Iterable
import hashlib, json, re

@dataclass(frozen=True)
class Observation:
    modality: str
    feature: str
    value: float
    quality: float = 1.0
    source: str = "unknown"
    unit: str = ""
    timestamp: str = ""

def clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    value = float(x)
    if not isfinite(value):
        return lo
    return max(lo, min(hi, value))

def normalize(raw: dict[str, Any]) -> Observation:
    try:
        value = float(raw.get("value", 0.0))
    except (TypeError, ValueError):
        value = 0.0
    if not isfinite(value):
        value = 0.0
    return Observation(
        modality=str(raw.get("modality", "unknown")).strip().lower() or "unknown",
        feature=str(raw.get("feature", "unknown")).strip().lower() or "unknown",
        value=value,
        quality=clip(raw.get("quality", 1.0)),
        source=str(raw.get("source", "unknown")).strip() or "unknown",
        unit=str(raw.get("unit", "")).strip(),
        timestamp=str(raw.get("timestamp", "")).strip(),
    )

def detect_language(text: str) -> str:
    if re.search(r"[\u0900-\u097F]", text): return "hi"
    if re.search(r"[\u0A00-\u0A7F]", text): return "pa"
    if re.search(r"[\u4E00-\u9FFF]", text): return "zh"
    if re.search(r"[\u3040-\u30FF]", text): return "ja"
    return "en"

def semantic_intent(text: str) -> str:
    t=text.lower()
    if any(k in t for k in ("why","cause","क्यों","कारण")): return "causal_question"
    if any(k in t for k in ("feel","emotion","भाव","अनुभव","एहसास")): return "experience_interpretation"
    if any(k in t for k in ("detect","measure","माप","पहचान")): return "measurement"
    return "general_interpretation"

def robust_stats(rows: list[Observation]) -> dict[str, float]:
    vals=[r.value for r in rows]
    mean=sum(vals)/len(vals)
    variance=sum((v-mean)**2 for v in vals)/len(vals)
    spread=sqrt(variance)
    ordered=sorted(vals)
    median=ordered[len(vals)//2] if len(vals)%2 else (ordered[len(vals)//2-1]+ordered[len(vals)//2])/2
    mad=sum(abs(v-median) for v in vals)/len(vals)
    return {"mean":mean,"spread":spread,"median":median,"mad":mad}

def fuse(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    rows=[normalize(x) for x in observations]
    usable=[x for x in rows if x.quality > 0]
    if not usable:
        return {"status":"insufficient_quality","observations":[asdict(x) for x in rows],"interpretation":None}
    stats=robust_stats(usable)
    modalities=sorted({x.modality for x in usable})
    sources=sorted({x.source for x in usable})
    quality=sum(x.quality for x in usable)/len(usable)
    relative_spread=stats["spread"]/(abs(stats["mean"])+1e-9)
    variability=clip(relative_spread/3.0)
    outlier_ratio=clip(sum(abs(x.value-stats["median"]) > max(3*stats["mad"],1e-9) for x in usable)/len(usable))
    agreement=clip(1.0-0.65*variability-0.35*outlier_ratio)
    diversity=clip(len(modalities)/4)
    replication=clip(len(sources)/4)
    confidence=clip(0.15+0.40*quality+0.25*agreement+0.10*diversity+0.10*replication)
    if variability >= .66: state="high_variability_pattern"
    elif variability >= .33: state="moderate_variability_pattern"
    else: state="stable_pattern"
    limitations=[
        "यह measured/observable signals की computational interpretation है; subjective feeling का direct proof नहीं।",
        "जीव, वनस्पति या निर्जीव वस्तु के अनुभव का दावा करने के लिए operational definition, labelled experiments और independent replication चाहिए।",
        "Confidence calibrated scientific certainty नहीं है; calibration data उपलब्ध होने पर इसे अलग से evaluate करना होगा।",
    ]
    if len(modalities)<2:
        limitations.append("केवल एक modality उपलब्ध है; multimodal corroboration अभी उपलब्ध नहीं।")
    if outlier_ratio>.25:
        limitations.append("कुछ observations robust baseline से अलग हैं; raw data और sensor quality की पुनः जाँच उचित है।")
    return {
        "status":"interpreted","intent":semantic_intent(request),"language":detect_language(request),
        "features":{"mean":stats["mean"],"spread":stats["spread"],"median":stats["median"],"mad":stats["mad"],
                    "variability":variability,"outlier_ratio":outlier_ratio,"agreement":agreement,
                    "quality":quality,"modalities":len(modalities),"sources":len(sources),
                    "diversity":diversity,"replication":replication,"confidence":confidence},
        "interpretation":{"state":state,"evidence":[asdict(x) for x in usable],"limitations":limitations},
        "observations":[asdict(x) for x in rows],
    }

def explain_simple(result: dict[str, Any], language: str = "hi") -> str:
    if result.get("status")!="interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है; इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    f=result["features"]; i=result["interpretation"]
    if language=="en":
        return (f"Observed data shows a {i['state']} pattern. Confidence={f['confidence']:.0%}, "
                f"agreement={f['agreement']:.0%}, modalities={f['modalities']}. "
                "This is signal interpretation, not proof of subjective experience.")
    return (f"प्राप्त संकेतों में '{i['state']}' जैसा पैटर्न है। विश्वास-मान {f['confidence']:.0%}, "
            f"संकेत-सहमति {f['agreement']:.0%}, स्वतंत्र modalities {f['modalities']} हैं। "
            "यह संकेतों की computational व्याख्या है; इसे प्रत्यक्ष भाव/चेतना का प्रमाण नहीं माना जाता।")

def fingerprint(result: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(result,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def build_practitioner_record(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    result=fuse(observations,request)
    return {
        "schema_version":"1.0","generated_at":datetime.now(timezone.utc).isoformat(),
        "pipeline":"observe->normalize->quality->robust-stats->multimodal-fusion->uncertainty->NLP",
        "result":result,"simple_language":explain_simple(result,result.get("language","hi")),
        "fingerprint":fingerprint(result),
        "governance":{"fail_closed":True,"subjective_experience_claim_allowed":False,
                      "code_mutation_allowed":False,"independent_verification_required":True}
    }
