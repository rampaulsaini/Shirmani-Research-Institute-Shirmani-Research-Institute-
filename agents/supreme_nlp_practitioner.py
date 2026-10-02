"""Supreme NLP Practitioner: evidence-first multimodal fusion and plain-language explanation.

v1.1 strengthens measurement integrity: observations are never pooled across
incompatible feature/unit groups, source independence is not inferred from
source count, contradictions are surfaced, and confidence is explicitly
heuristic/uncalibrated until benchmark calibration data exists.
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
    try: value = float(x)
    except (TypeError, ValueError): return lo
    if not isfinite(value): return lo
    return max(lo, min(hi, value))

def normalize(raw: dict[str, Any]) -> Observation:
    try: value = float(raw.get("value", 0.0))
    except (TypeError, ValueError): value = 0.0
    if not isfinite(value): value = 0.0
    return Observation(
        modality=str(raw.get("modality", "unknown")).strip().lower() or "unknown",
        feature=str(raw.get("feature", "unknown")).strip().lower() or "unknown",
        value=value, quality=clip(raw.get("quality", 1.0)),
        source=str(raw.get("source", "unknown")).strip() or "unknown",
        unit=str(raw.get("unit", "")).strip(),
        timestamp=str(raw.get("timestamp", "")).strip(),
    )

def detect_language(text: str) -> str:
    if re.search(r"[\u3040-\u30FF]", text): return "ja"
    if re.search(r"[\u0900-\u097F]", text): return "hi"
    if re.search(r"[\u0A00-\u0A7F]", text): return "pa"
    if re.search(r"[\u4E00-\u9FFF]", text): return "zh"
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

def group_key(row: Observation) -> str:
    # Values are pooled only when they describe the same named feature and unit.
    # This prevents invalid arithmetic across unrelated measurements.
    return f"{row.feature}|{row.unit or 'unitless'}"

def _group_summary(rows: list[Observation]) -> dict[str, Any]:
    groups: dict[str,list[Observation]]={}
    for row in rows: groups.setdefault(group_key(row),[]).append(row)
    summaries={}
    for key, items in sorted(groups.items()):
        s=robust_stats(items)
        summaries[key]={
            **s, "sample_count":len(items),
            "modalities":sorted({x.modality for x in items}),
            "sources":sorted({x.source for x in items}),
            "quality":sum(x.quality for x in items)/len(items),
        }
    return summaries

def _contradiction(rows: list[Observation]) -> bool:
    # A contradiction is raised only when the same feature/unit group contains
    # materially opposing directions around its median.
    groups: dict[str,list[Observation]]={}
    for row in rows: groups.setdefault(group_key(row),[]).append(row)
    for items in groups.values():
        if len(items)<3: continue
        s=robust_stats(items)
        scale=max(s["mad"],abs(s["mean"])*0.05,1e-9)
        signs={1 if x.value>s["median"]+scale else -1 if x.value<s["median"]-scale else 0 for x in items}
        if 1 in signs and -1 in signs: return True
    return False

def fuse(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    rows=[normalize(x) for x in observations]
    usable=[x for x in rows if x.quality > 0]
    if not usable:
        return {"status":"insufficient_quality","observations":[asdict(x) for x in rows],"interpretation":None}

    groups=_group_summary(usable)
    modalities=sorted({x.modality for x in usable})
    sources=sorted({x.source for x in usable})
    quality=sum(x.quality for x in usable)/len(usable)
    # Source count is a replication signal, not proof of independence.
    source_diversity=clip(len(sources)/4)
    modality_diversity=clip(len(modalities)/4)
    group_agreement=[]
    outlier_ratios=[]
    for key, s in groups.items():
        spread=float(s["spread"]); mean=float(s["mean"])
        variability=clip((spread/(abs(mean)+1e-9))/3.0)
        group_agreement.append(clip(1.0-variability))
        vals=[x.value for x in usable if group_key(x)==key]
        median=float(s["median"]); mad=float(s["mad"])
        outlier_ratios.append(clip(sum(abs(v-median)>max(3*mad,1e-9) for v in vals)/len(vals)))
    agreement=sum(group_agreement)/len(group_agreement)
    outlier_ratio=sum(outlier_ratios)/len(outlier_ratios)
    contradiction=_contradiction(usable)
    confidence=clip(0.15+0.40*quality+0.20*agreement+0.10*modality_diversity+0.15*source_diversity-(0.20 if contradiction else 0))
    state="contradictory_pattern" if contradiction else (
        "multi_group_pattern" if len(groups)>1 else "single_group_pattern"
    )
    limitations=[
        "यह measured/observable signals की computational interpretation है; subjective feeling का direct proof नहीं।",
        "अलग feature/unit groups को raw values के रूप में आपस में नहीं मिलाया जाता।",
        "Source count independence का प्रमाण नहीं है; independent replication अलग experimental control से स्थापित करनी होगी।",
        "Confidence heuristic और uncalibrated है; labelled benchmark data मिलने पर calibration अलग से आवश्यक है।",
    ]
    if len(modalities)<2: limitations.append("केवल एक modality उपलब्ध है; multimodal corroboration अभी सीमित है।")
    if contradiction: limitations.append("एक ही feature/unit group में विरोधी patterns मिले; interpretation review में रहनी चाहिए।")
    return {
        "status":"interpreted","intent":semantic_intent(request),"language":detect_language(request),
        "features":{
            "confidence":confidence,"confidence_type":"heuristic_uncalibrated",
            "agreement":agreement,"quality":quality,"modalities":len(modalities),
            "sources":len(sources),"source_diversity":source_diversity,
            "groups":len(groups),"outlier_ratio":outlier_ratio,
            "contradiction_detected":contradiction,"group_summaries":groups,
        },
        "interpretation":{
            "state":state,"evidence":[asdict(x) for x in usable],
            "limitations":limitations,"independence_established":False,
        },
        "observations":[asdict(x) for x in rows],
    }

def explain_simple(result: dict[str, Any], language: str = "hi") -> str:
    if result.get("status")!="interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है; इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    f=result["features"]; i=result["interpretation"]
    if language=="en":
        return (f"Observed data shows a {i['state']} pattern across {f['groups']} compatible "
                f"measurement group(s). Heuristic confidence={f['confidence']:.0%}. "
                "This is signal interpretation, not proof of subjective experience.")
    return (f"प्राप्त संकेतों में {f['groups']} संगत measurement group(s) के आधार पर "
            f"'{i['state']}' पैटर्न मिला। heuristic confidence {f['confidence']:.0%} है। "
            "यह मापनीय संकेतों की computational व्याख्या है; इसे प्रत्यक्ष भाव या चेतना का प्रमाण नहीं माना जाता।")

def fingerprint(result: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(result,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def build_practitioner_record(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    result=fuse(observations,request)
    return {
        "schema_version":"1.1","generated_at":datetime.now(timezone.utc).isoformat(),
        "pipeline":"observe->normalize->quality->compatible-grouping->robust-stats->multimodal-fusion->uncertainty->NLP",
        "result":result,"simple_language":explain_simple(result,result.get("language","hi")),
        "fingerprint":fingerprint(result),
        "governance":{
            "fail_closed":True,"subjective_experience_claim_allowed":False,
            "code_mutation_allowed":False,"independent_verification_required":True,
            "confidence_calibration_required":True,
        }
    }
