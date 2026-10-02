"""Evidence-first multimodal signal -> simple-language NLP adapter."""
from __future__ import annotations
import hashlib,json
from statistics import mean
from typing import Any
ALLOWED_MODALITIES={"audio","electrical","vibration","temperature","light","motion","chemical","text","image","environmental"}
def analyze(observations:list[dict[str,Any]],request:str="signal interpretation")->dict[str,Any]:
    clean=[]
    for row in observations:
        modality=str(row.get("modality","unknown"))
        try:value=float(row.get("value",0))
        except (TypeError,ValueError):value=0.0
        try:quality=max(0.0,min(1.0,float(row.get("quality",0))))
        except (TypeError,ValueError):quality=0.0
        clean.append({"modality":modality,"feature":str(row.get("feature","signal")),"value":value,"quality":quality,"source":str(row.get("source","unknown"))})
    usable=[r for r in clean if r["modality"] in ALLOWED_MODALITIES and r["quality"]>0]
    quality=mean([r["quality"] for r in usable]) if usable else 0.0
    fp=hashlib.sha256(json.dumps(clean,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return {"status":"CANDIDATE" if usable else "NO_CLAIM","request":request,"observations":clean,
      "summary":{"usable_observations":len(usable),"mean_quality":round(quality,6)},
      "interpretation":{"type":"measurable-signal-hypothesis","subjective_experience_proven":False},
      "confidence":round(quality,6),
      "verification":{"status":"UNVERIFIED","promotion_allowed":False,"independent_verification_required":True},
      "governance":{"fail_closed":True,"accuracy_is_measured_not_declared":True,"subjective_experience_claim_allowed":False,"scheduled_code_mutation_allowed":False},
      "fingerprint":fp}
def to_simple_language(record:dict[str,Any])->str:
    s=record["summary"]
    if not s["usable_observations"]: return "पर्याप्त विश्वसनीय मापनीय संकेत उपलब्ध नहीं हैं; इसलिए कोई निष्कर्ष नहीं दिया गया।"
    return f"प्रणाली ने {s['usable_observations']} उपयोगी मापनीय संकेत देखे। औसत डेटा-गुणवत्ता {s['mean_quality']:.1%} है। इन संकेतों से केवल एक परीक्षणयोग्य परिकल्पना बनाई जा सकती है; किसी व्यक्तिपरक अनुभव का प्रत्यक्ष प्रमाण अभी स्थापित नहीं है।"
