#!/usr/bin/env python3
"""Deterministic, fail-closed quality gate for AI/ML/NLP/Automission artifacts."""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GENERATED=ROOT/"generated"
EVIDENCE_KEYS=("evidence","sources","citations","references","source_refs")
UNCERTAINTY_KEYS=("uncertainty","confidence","limitations","caveats")
PROVENANCE_KEYS=("source","source_url","provenance","trace_id","retrieved_at")
REQUIRED_FIELDS=("id","content")
def text_of(x):
    if isinstance(x,str): return x
    if isinstance(x,dict): return " ".join(text_of(v) for v in x.values())
    if isinstance(x,list): return " ".join(text_of(v) for v in x)
    return ""
def load_records():
    for path in (GENERATED/"source-units.jsonl",GENERATED/"research-queue.jsonl"):
        if path.exists():
            rows=[]; invalid=0
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip(): continue
                try: rows.append(json.loads(line))
                except json.JSONDecodeError: invalid+=1
            if rows or invalid: return path,rows,invalid
    return None,[],0
def has_value(r, keys): return any(r.get(k) not in (None,"",[],{}) for k in keys)
def contradiction_signal(content):
    t=re.sub(r"\s+"," ",content.lower())
    return any(x in t for x in ("contradiction","conflicts with","inconsistent with","cannot be reconciled"))
def evaluate(rows, invalid_lines):
    if not rows: return 0.0,{"records":0,"invalid_json_lines":invalid_lines,"status_reason":"no_valid_records"}
    n=len(rows); unique=set(); complete=evidence=uncertain=traceable=contradictions=duplicates=missing=0
    for r in rows:
        content=text_of(r.get("content","")).strip()
        if all(str(r.get(k,"")).strip() for k in REQUIRED_FIELDS) and content: complete+=1
        else: missing+=1
        canonical=re.sub(r"\s+"," ",content.lower()).strip()
        if canonical:
            d=hashlib.sha256(canonical.encode()).hexdigest()
            if d in unique: duplicates+=1
            unique.add(d)
        if has_value(r,EVIDENCE_KEYS): evidence+=1
        if has_value(r,UNCERTAINTY_KEYS): uncertain+=1
        if has_value(r,PROVENANCE_KEYS): traceable+=1
        if contradiction_signal(content): contradictions+=1
    m={"records":n,"invalid_json_lines":invalid_lines,"complete_rate":round(complete/n,4),
       "evidence_rate":round(evidence/n,4),"uncertainty_rate":round(uncertain/n,4),
       "traceability_rate":round(traceable/n,4),"unique_rate":round(len(unique)/n,4),
       "duplicate_records":duplicates,"missing_required_fields":missing,
       "possible_contradiction_markers":contradictions}
    q=sum(m[k]*w for k,w in {"complete_rate":.30,"evidence_rate":.25,"uncertainty_rate":.10,
      "traceability_rate":.20,"unique_rate":.15}.items())
    return round(q,4),m
def main():
    path,rows,invalid=load_records(); quality,metrics=evaluate(rows,invalid)
    hard_fail=(not rows or invalid>0 or metrics.get("missing_required_fields",0)>0 or
               metrics.get("possible_contradiction_markers",0)>0)
    status="PASS" if quality>=.90 and not hard_fail else "REVIEW"
    result={"gate":"SHIRMANI_SUPREME_QUALITY_GATE","status":status,"quality_score":quality,
      "accuracy_claim":"No absolute-accuracy claim; measures evidence-backed artifact quality.",
      "input":str(path.relative_to(ROOT)) if path else None,"metrics":metrics,
      "decision_policy":{"threshold":0.90,"fail_closed":True,"independent_verification_required":True}}
    out=GENERATED/"supreme-quality-gate.json"; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if status=="PASS" else 2
if __name__=="__main__": sys.exit(main())
