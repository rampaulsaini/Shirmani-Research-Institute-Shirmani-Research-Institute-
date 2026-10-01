#!/usr/bin/env python3
"""Deterministic quality gate for AI/ML/NLP/Automission artifacts."""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GENERATED=ROOT/"generated"
EVIDENCE_KEYS=("evidence","sources","citations","references","source_refs")
UNCERTAINTY_KEYS=("uncertainty","confidence","limitations","caveats")

def text_of(x):
    if isinstance(x,str): return x
    if isinstance(x,dict): return " ".join(text_of(v) for v in x.values())
    if isinstance(x,list): return " ".join(text_of(v) for v in x)
    return ""

def load_records():
    for path in (GENERATED/"source-units.jsonl",GENERATED/"research-queue.jsonl"):
        if path.exists():
            rows=[]
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    try: rows.append(json.loads(line))
                    except json.JSONDecodeError: pass
            if rows: return path,rows
    return None,[]

def evaluate(rows):
    if not rows: return 0,{"records":0}
    n=len(rows); unique=set(); complete=evidence=uncertain=traceable=0; contradictions=0
    for r in rows:
        content=text_of(r.get("content","")).strip()
        if str(r.get("id","")).strip() and content: complete+=1
        canonical=re.sub(r"\s+"," ",content.lower()).strip()
        if canonical: unique.add(hashlib.sha256(canonical.encode()).hexdigest())
        if any(r.get(k) for k in EVIDENCE_KEYS): evidence+=1
        if any(r.get(k) is not None for k in UNCERTAINTY_KEYS): uncertain+=1
        if r.get("source") or r.get("source_url") or r.get("provenance"): traceable+=1
        if "contradiction" in canonical: contradictions+=1
    m={
      "records":n,"complete_rate":round(complete/n,4),
      "evidence_rate":round(evidence/n,4),"uncertainty_rate":round(uncertain/n,4),
      "traceability_rate":round(traceable/n,4),"unique_rate":round(len(unique)/n,4),
      "possible_contradiction_markers":contradictions}
    q=sum(m[k]*w for k,w in {
      "complete_rate":.30,"evidence_rate":.25,"uncertainty_rate":.10,
      "traceability_rate":.20,"unique_rate":.15}.items())
    return round(q,4),m

def main():
    path,rows=load_records(); quality,metrics=evaluate(rows)
    result={"gate":"SHIRMANI_SUPREME_QUALITY_GATE",
            "status":"PASS" if quality>=.90 and metrics.get("possible_contradiction_markers",0)==0 else "REVIEW",
            "quality_score":quality,
            "absolute_accuracy_claim":False,
            "interpretation":"Measured artifact quality, not proof of truth.",
            "input":str(path.relative_to(ROOT)) if path else None,"metrics":metrics}
    out=GENERATED/"supreme-quality-gate.json"; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result["status"]=="PASS" else 2

if __name__=="__main__": sys.exit(main())
