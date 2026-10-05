#!/usr/bin/env python3
"""Self-healing production dispatcher.

Creates a bounded, source-bound work queue when the generated dispatcher queue
is missing or empty. This is production continuity, not verification.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"production-work-queue.jsonl"
MAX_TASKS=500
SKIP={".git","__pycache__","_sources","generated"}
ALLOWED={".html",".md",".yml",".yaml",".py",".json",".jsonl"}
LANES={
 "research":("research","paper","evidence","knowledge","archive"),
 "ai-ml-nlp":("ai","ml","nlp","automission","agent","model"),
 "content":("content","audio","video","music","podcast","media"),
 "platform":("platform","dashboard","hub","portal","social"),
 "economic":("income","employment","market","store","product","economic","value"),
 "social-media":("social","youtube","facebook","blog","media"),
 "federation":("federation","repository","network"),
 "security-quality":("security","quality","qc","verification","audit","governance"),
 "automation":("workflow","factory","automation","orchestrator","worker"),
}
def lane(path,text):
    hay=(path+" "+text[:1500]).lower()
    for name,keys in LANES.items():
        if any(k in hay for k in keys): return name
    return "platform"
def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    existing=[x for x in OUT.read_text(encoding="utf-8",errors="ignore").splitlines() if x.strip()] if OUT.exists() else []
    if existing:
        print(json.dumps({"source":"existing_queue","tasks":len(existing)})); return
    candidates=[]
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in ALLOWED: continue
        if any(part in SKIP for part in p.parts): continue
        text=p.read_text(encoding="utf-8",errors="ignore")
        candidates.append((str(p.relative_to(ROOT)),text))
    candidates.sort()
    cycle=int(datetime.now(timezone.utc).timestamp()//300)
    rows=[]
    for slot,(path,text) in enumerate(candidates[:MAX_TASKS],1):
        task_id="AUTO-"+hashlib.sha256(f"{cycle}|{path}|{slot}".encode()).hexdigest()[:24]
        rows.append({"task_id":task_id,"cycle":cycle,"slot":slot,"lane":lane(path,text),
                     "module":path,"module_kind":Path(path).suffix.lstrip("."),
                     "objective":f"Produce a concrete source-bound output for {path}",
                     "source_bound":True,"verification_status":"PENDING"})
    OUT.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows),encoding="utf-8")
    print(json.dumps({"source":"self_heal_discovery","tasks":len(rows),"cycle":cycle},ensure_ascii=False))
if __name__=="__main__": main()
