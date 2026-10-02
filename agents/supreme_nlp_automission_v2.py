"""Evidence-first multimodal-to-NLP control layer."""
from __future__ import annotations
import hashlib, json, math, time
from dataclasses import dataclass, asdict
from typing import Any, Iterable

@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    quality: float
    source: str

def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))

def normalize(rows: Iterable[dict[str, Any]]) -> list[Signal]:
    out=[]
    for r in rows:
        try:
            q=_clip(float(r.get("quality",0))); v=float(r.get("value",0))
        except (TypeError,ValueError): continue
        if not math.isfinite(v): continue
        out.append(Signal(str(r.get("modality","unknown")),str(r.get("feature","unknown")),v,q,str(r.get("source","unspecified"))))
    return out

def infer_observable_state(signals: list[Signal]) -> dict[str, Any]:
    if not signals:
        return {"label":"INSUFFICIENT_DATA","confidence":0.0,"basis":"No usable observable signals.","subjective_experience_inferred":False}
    weighted=sum(abs(s.value)*s.quality for s in signals); quality=sum(s.quality for s in signals)
    confidence=_clip(quality/max(len(signals),1)); magnitude=weighted/max(quality,1e-12)
    label="LOW_ACTIVITY" if magnitude<0.5 else "MODERATE_ACTIVITY" if magnitude<2 else "HIGH_ACTIVITY"
    return {"label":label,"confidence":round(confidence,6),"basis":"Observable signal magnitude and data quality only.","subjective_experience_inferred":False}

def simple_language(state: dict[str,Any]) -> str:
    if state["label"]=="INSUFFICIENT_DATA": return "उपलब्ध संकेत पर्याप्त नहीं हैं; विश्वसनीय निष्कर्ष नहीं बनाया गया।"
    return f"देखे गए संकेतों में {state['label']} जैसा पैटर्न मिला। डेटा-गुणवत्ता आधारित confidence {state['confidence']:.1%} है। इसे प्रत्यक्ष चेतना या भाव-अनुभव का प्रमाण नहीं माना गया है।"

def build_record(rows: Iterable[dict[str,Any]], task_id: str="automission-v2") -> dict[str,Any]:
    signals=normalize(rows); state=infer_observable_state(signals)
    payload={"record_id":task_id,"timestamp":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
      "input":{"signal_count":len(signals)},"signals":[asdict(s) for s in signals],
      "interpretation":{"state":state,"simple_language":simple_language(state)},
      "evidence":[{"source":s.source,"feature":s.feature,"modality":s.modality} for s in signals],
      "governance":{"fail_closed":True,"independent_verification_required":True,"subjective_experience_claim_allowed":False,"accuracy_is_measured_not_declared":True,"scheduled_code_mutation_allowed":False},
      "metrics":{"signal_count":len(signals),"mean_quality":round(sum(s.quality for s in signals)/len(signals),6) if signals else 0.0}}
    canonical=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    payload["fingerprint"]=hashlib.sha256(canonical.encode()).hexdigest()
    return payload
