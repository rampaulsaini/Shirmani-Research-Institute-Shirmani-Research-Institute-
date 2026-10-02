"""Supreme NLP orchestration core: evidence-first, fail-closed, dependency-free."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
MIN_SOURCES=2; MIN_SAMPLES=10; MIN_SCORE=0.70
def fingerprint(x: Any) -> str:
    raw=json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
def clamp(x: float) -> float: return max(0.0,min(1.0,float(x)))
def analyze(o: dict[str,Any]) -> dict[str,Any]:
    s=o.get("signals") or []
    mods=sorted({str(x.get("modality","")).strip() for x in s if x.get("modality")})
    src=sorted({str(x.get("source_id")) for x in s if x.get("source_id")})
    q=[float(x.get("quality",0.0)) for x in s if isinstance(x.get("quality",0.0),(int,float))]
    mq=sum(q)/len(q) if q else 0.0
    score=clamp(.35*mq+.25*min(len(mods)/2,1)+.20*min(len(src)/MIN_SOURCES,1)+.20*min(len(s)/MIN_SAMPLES,1))
    grade="A" if score>=.85 else "B" if score>=.70 else "C" if score>=.50 else "D"
    return {"observation_id":o.get("observation_id"),"status":"interpretable" if score>=MIN_SCORE else "insufficient_evidence",
      "evidence":{"score":round(score,4),"grade":grade,"modalities":mods,"independent_sources":src,"sample_count":len(s)},
      "translation_boundary":{"allowed":True,"meaning":"Translate measured patterns into plain language with uncertainty.","subjective_experience_claim":"not established by this pipeline"},
      "provenance":{"observation_fingerprint":fingerprint(o),"generated_at":datetime.now(timezone.utc).isoformat()}}
def plan(r: dict[str,Any]) -> dict[str,Any]:
    e=r["evidence"]; a=[]
    if e["sample_count"]<MIN_SAMPLES: a.append("increase repeated observations")
    if len(e["modalities"])<2: a.append("add an independent modality where scientifically appropriate")
    if len(e["independent_sources"])<MIN_SOURCES: a.append("obtain an independent source or replication")
    if e["score"]<MIN_SCORE: a.append("abstain from stronger interpretation")
    if not a: a.append("run independent verification and regression tests")
    return {"state":"IMPROVEMENT_REQUIRED" if len(a)>1 else "VERIFY","actions":a,"fail_closed":True,"promotion_allowed":False,"generated_at":datetime.now(timezone.utc).isoformat()}
def run(inp="generated/supreme-nlp/observation.json",outdir="generated/supreme-nlp"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True); p=Path(inp)
    if not p.exists(): payload={"status":"NO_OBSERVATION","fail_closed":True,"message":"No observation supplied; no interpretation or promotion is permitted."}
    else:
        o=json.loads(p.read_text(encoding="utf-8")); r=analyze(o); payload={"result":r,"automission":plan(r)}
    (out/"result.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); return payload
if __name__=="__main__": print(json.dumps(run(),ensure_ascii=False,indent=2))
