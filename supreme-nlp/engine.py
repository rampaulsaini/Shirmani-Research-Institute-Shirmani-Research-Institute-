"""Deterministic evidence-first Supreme NLP core."""
from __future__ import annotations
import hashlib, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

GRADE_WEIGHT={"A":1.0,"B":.8,"C":.5,"D":.2}

def fingerprint(obj:Any)->str:
    raw=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    return hashlib.sha256(raw.encode()).hexdigest()

def normalize(records:Iterable[dict[str,Any]])->list[dict[str,Any]]:
    out=[]
    for r in records:
        if not isinstance(r,dict): continue
        out.append({
            "source_id":str(r.get("source_id","unknown")).strip() or "unknown",
            "modality":str(r.get("modality","unknown")).strip().lower() or "unknown",
            "timestamp":r.get("timestamp"),
            "features":r.get("features") if isinstance(r.get("features"),dict) else {},
            "provenance":r.get("provenance") if isinstance(r.get("provenance"),dict) else {}
        })
    return out

def agreement(rows:list[dict[str,Any]])->float:
    labels=[str(r["features"]["state"]) for r in rows if "state" in r["features"]]
    if len(labels)<2:return 0.0
    return max(Counter(labels).values())/len(labels)

def grade(n:int,sources:int,modalities:int,agree:float)->str:
    if n>=30 and sources>=3 and modalities>=3 and agree>=.85:return "A"
    if n>=10 and sources>=2 and modalities>=2 and agree>=.70:return "B"
    if n>=5 and sources>=1:return "C"
    return "D"

def interpret(records:Iterable[dict[str,Any]])->dict[str,Any]:
    rows=normalize(records)
    modalities={r["modality"] for r in rows if r["modality"]!="unknown"}
    sources={r["source_id"] for r in rows if r["source_id"]!="unknown"}
    agree=agreement(rows); g=grade(len(rows),len(sources),len(modalities),agree)
    limitations=[
      "Measured signal patterns are observations, not direct proof of subjective experience.",
      "Interpretation depends on calibration, sampling quality, model validity and context.",
      "Independent replication is required before VERIFIED status."
    ]
    if not rows:
        status="insufficient_data"; text="No valid multimodal observations were supplied."; confidence=0.0
    else:
        status="interpreted"
        text=(f"Observed {len(rows)} records across {len(modalities)} modalities. "
              f"Cross-signal agreement is {agree:.2f}; evidence grade is {g}. "
              "The system can describe measurable patterns but does not infer subjective experience from them.")
        confidence=min(.95,.20+.20*min(len(rows)/30,1)+.20*min(len(sources)/3,1)+.25*agree+.15*GRADE_WEIGHT[g])
    result={"schema_version":"1.0.0","status":status,
      "features":{"modalities":len(modalities),"independent_sources":len(sources),"sample_count":len(rows),
                  "agreement":round(agree,4),"evidence_grade":g,"drift_score":0.0},
      "interpretation":{"text":text,"confidence":round(confidence,4),"limitations":limitations},
      "governance":{"fail_closed":True,"independent_verification_required":True,"subjective_experience_claim_allowed":False}}
    result["fingerprint"]=fingerprint(result)
    result["generated_at"]=datetime.now(timezone.utc).isoformat()
    return result

def run(input_path="generated/supreme-nlp/input.jsonl",output_path="generated/supreme-nlp/status.json"):
    p=Path(input_path); records=[]
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try: records.append(json.loads(line))
                except json.JSONDecodeError: pass
    result=interpret(records)
    out=Path(output_path); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return result

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
