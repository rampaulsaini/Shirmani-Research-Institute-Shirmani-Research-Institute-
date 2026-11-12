"""Deduplicated failure-memory ledger for Automission."""
from __future__ import annotations
import json
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
def fingerprint(stage,error,context=None):
    raw=json.dumps({"stage":stage,"error":error,"context":context or {}},ensure_ascii=False,sort_keys=True)
    return sha256(raw.encode()).hexdigest()
def record(path,stage,error,context=None):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    fp=fingerprint(stage,error,context); rows=[]
    if p.exists(): rows=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    hit=next((r for r in rows if r.get("fingerprint")==fp),None)
    if hit:
        hit["count"]=int(hit.get("count",0))+1; hit["last_seen"]=datetime.now(timezone.utc).isoformat()
    else:
        hit={"fingerprint":fp,"stage":stage,"error":str(error),"context":context or {},
             "first_seen":datetime.now(timezone.utc).isoformat(),"count":1,"status":"OPEN"}
        rows.append(hit)
    p.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")
    return hit
