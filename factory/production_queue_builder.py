#!/usr/bin/env python3
"""Production-first multi-layer work queue builder."""
from __future__ import annotations
import hashlib, json, os
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; QUEUE=GEN/"production-work-queue.jsonl"
SKIP={".git",".github","generated","node_modules","__pycache__",".venv","dist","build"}
EXT={".html",".md",".py",".json",".yml",".yaml"}
BATCH=int(os.environ.get("PRODUCTION_BATCH_SIZE","120"))

def cycle(): return int(datetime.now(timezone.utc).timestamp()//300)

def lane(p):
    s=str(p).lower()
    if any(x in s for x in ("security","quality","qc","schema")): return "security-quality"
    if any(x in s for x in ("social","media","youtube","facebook")): return "social-media"
    if any(x in s for x in ("income","employment","economic","store","market")): return "economic"
    if any(x in s for x in ("federation","repository","integration")): return "federation"
    if any(x in s for x in ("nlp","ml","ai-","automission","agent")): return "ai-ml-nlp"
    if any(x in s for x in ("research","paper","evidence")): return "research"
    if p.suffix.lower() in {".html",".md"}: return "content"
    return "platform"

def main():
    GEN.mkdir(parents=True,exist_ok=True)
    modules=[]
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXT and not any(x in SKIP for x in p.parts):
            rel=p.relative_to(ROOT).as_posix()
            if rel!="factory/production_queue_builder.py":
                modules.append((hashlib.sha256(rel.encode()).hexdigest(),rel,p.suffix.lower().lstrip(".")))
    modules.sort()
    c=cycle(); start=(c*BATCH)%len(modules) if modules else 0
    chosen=[modules[(start+i)%len(modules)] for i in range(min(BATCH,len(modules)))]
    objectives={
      "research":"Produce a concrete source-bound research work artifact.",
      "ai-ml-nlp":"Produce a concrete AI/ML/NLP work artifact.",
      "content":"Produce a concrete public content artifact.",
      "platform":"Produce a concrete platform/module artifact.",
      "economic":"Produce a lawful product/service/livelihood artifact.",
      "social-media":"Produce a public distribution/content artifact.",
      "federation":"Produce a cross-module integration artifact.",
      "security-quality":"Produce a quality/provenance/resilience artifact."
    }
    counts={}
    with QUEUE.open("w",encoding="utf-8") as f:
        for slot,(_,rel,kind) in enumerate(chosen,1):
            ln=lane(Path(rel)); counts[ln]=counts.get(ln,0)+1
            task={"task_id":hashlib.sha256(f"{c}|{slot}|{rel}".encode()).hexdigest()[:24],
                  "cycle":c,"slot":slot,"lane":ln,"module":rel,"module_kind":kind,
                  "objective":objectives[ln],"production_mode":"CONTINUOUS_MULTI_LAYER",
                  "verification":"DOWNSTREAM"}
            f.write(json.dumps(task,ensure_ascii=False)+"\n")
    status={"generated_at":datetime.now(timezone.utc).isoformat(),"cycle":c,
            "discovered_modules":len(modules),"selected_tasks":len(chosen),"batch_size":BATCH,
            "lanes":counts,"principle":"Production first; verification downstream.",
            "integrity":{"source_bound":True,"independent_verification_claim":False}}
    (GEN/"production-queue-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))
if __name__=="__main__": main()
