"""Evidence-first translation of multimodal observations into plain-language NLP.
No claim of subjective consciousness is made from sensor data alone.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any

@dataclass
class NLPInterpretation:
    statement: str
    confidence: float
    evidence_level: str
    alternative_explanations: list[str]
    evidence_refs: list[str]

def interpret_signal(record: dict[str, Any]) -> dict[str, Any]:
    observations = record.get("observations", [])
    quality = [float(x["quality"]) for x in observations if isinstance(x.get("quality"), (int,float))]
    q = sum(quality) / len(quality) if quality else 0.5
    if not observations:
        return asdict(NLPInterpretation(
            "कोई पर्याप्त observable signal उपलब्ध नहीं है।",
            0.0, "unverified", ["डेटा अपर्याप्त है"], []
        ))
    features = ", ".join(str(x.get("feature")) for x in observations[:5])
    statement = (
        f"प्राप्त डेटा में {features} जैसे observable संकेत मिले हैं। "
        "इन संकेतों से एक संभावित अवस्था का अनुमान लगाया जा सकता है, "
        "लेकिन इसे सीधे subjective भावना या चेतना का प्रमाण नहीं माना जा सकता।"
    )
    return asdict(NLPInterpretation(
        statement=statement,
        confidence=round(max(0.0, min(1.0, q)), 4),
        evidence_level="inferred",
        alternative_explanations=[
            "measurement noise या उपकरणीय artifact",
            "पर्यावरणीय परिवर्तन",
            "अज्ञात confounding factor"
        ],
        evidence_refs=[record.get("record_id","")]
    ))

def make_record(source_type: str, observations: list[dict[str, Any]], record_id: str="auto") -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    r={"record_id":record_id,"source_type":source_type,"timestamp":now,
       "observations":observations,"interpretation":{}}
    r["interpretation"]=interpret_signal(r)
    return r
