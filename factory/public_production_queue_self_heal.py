#!/usr/bin/env python3
"""Self-healing, rotating production dispatcher.

Each 5-minute cycle selects a deterministic slice of repository modules so
production work rotates across the full module inventory instead of repeatedly
processing the same first batch. This is production continuity, not verification.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"production-work-queue.jsonl"
MAX_TASKS=1000
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
        if any(k in hay for k in keys):
            return name
    return "platform"

def discover():
    candidates=[]
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in ALLOWED:
            continue
        if any(part in SKIP for part in p.parts):
            continue
        text=p.read_text(encoding="utf-8",errors="ignore")
        candidates.append((str(p.relative_to(ROOT)),text))
    candidates.sort(key=lambda x:x[0])
    return candidates

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    candidates=discover()
    total=len(candidates)
    if not total:
        OUT.write_text("",encoding="utf-8")
        print(json.dumps({"source":"empty_repository","tasks":0}))
        return

    # Five-minute cycle cursor: deterministic rotation across the complete inventory.
    cycle=int(datetime.now(timezone.utc).timestamp()//300)
    offset=(cycle*MAX_TASKS)%total
    selected=[candidates[(offset+i)%total] for i in range(min(MAX_TASKS,total))]

    rows=[]
    for slot,(path,text) in enumerate(selected,1):
        task_id="AUTO-"+hashlib.sha256(
            f"{cycle}|{offset}|{path}|{slot}".encode()
        ).hexdigest()[:24]
        rows.append({
            "task_id":task_id,
            "cycle":cycle,
            "slot":slot,
            "queue_offset":offset,
            "inventory_total":total,
            "lane":lane(path,text),
            "module":path,
            "module_kind":Path(path).suffix.lstrip("."),
            "objective":f"Produce a concrete source-bound output for {path}",
            "source_bound":True,
            "verification_status":"PENDING"
        })

    OUT.write_text(
        "".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows),
        encoding="utf-8"
    )
    print(json.dumps({
        "source":"rotating_inventory",
        "tasks":len(rows),
        "cycle":cycle,
        "offset":offset,
        "inventory_total":total,
        "coverage_window":"rotates across full repository inventory"
    },ensure_ascii=False))

if __name__=="__main__":
    main()
