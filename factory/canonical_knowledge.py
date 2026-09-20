#!/usr/bin/env python3
"""Build a stable, incremental canonical knowledge layer from source-units."""
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"
SRC=GEN/"source-units.jsonl"; OUT=GEN/"canonical-knowledge.jsonl"; MAN=GEN/"canonical-knowledge-manifest.json"

def stable_id(row):
    key="|".join([row.get("repository",""),row.get("branch") or "",row.get("path",""),row.get("source_hash","")])
    return "ck_"+hashlib.sha256(key.encode("utf-8")).hexdigest()[:24]

def load_previous():
    prev={}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r=json.loads(line); prev[r["id"]]=r
    return prev

def main():
    if not SRC.exists(): raise SystemExit("Missing generated/source-units.jsonl")
    previous=load_previous(); current={}; now=datetime.now(timezone.utc).isoformat()
    for line in SRC.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        r=json.loads(line); rid=stable_id(r)
        current[rid]={"id":rid,"repository":r["repository"],"branch":r.get("branch"),
            "path":r["path"],"source_hash":r["source_hash"],"text":r["text"],
            "source_type":r.get("source_type","other"),"collected_at":r.get("collected_at"),
            "first_seen_at":previous.get(rid,{}).get("first_seen_at",now),"last_seen_at":now,"active":True}
    for rid,old in previous.items():
        if rid not in current:
            old=dict(old); old["active"]=False; old["last_seen_at"]=now; current[rid]=old
    rows=sorted(current.values(),key=lambda x:x["id"])
    OUT.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")
    active=[r for r in rows if r.get("active")]
    manifest={"version":1,"generated_at":now,"record_count":len(rows),
      "active_record_count":len(active),"inactive_record_count":len(rows)-len(active),
      "new_record_count":sum(1 for r in active if r["id"] not in previous),
      "retained_record_count":sum(1 for r in active if r["id"] in previous),
      "stable_id_basis":"repository|branch|path|source_hash","source":"generated/source-units.jsonl",
      "generated_output_is_not_source":True}
    MAN.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False))
if __name__=="__main__": main()
