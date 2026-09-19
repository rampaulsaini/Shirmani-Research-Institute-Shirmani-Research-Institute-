"""Durable JSONL queue primitives with retry/dead-letter tracking."""
import json
from pathlib import Path
from datetime import datetime,timezone
from agents.language_agents import route as language_route

def enqueue(path, jobs):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("a",encoding="utf-8") as f:
        for j in jobs:
            j.setdefault("status","pending"); j.setdefault("attempts",0); j.setdefault("created_at",datetime.now(timezone.utc).isoformat())
            f.write(json.dumps(j,ensure_ascii=False)+"\n")

def claim(path,limit=100):
    p=Path(path)
    if not p.exists(): return []
    rows=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    claimed=[]
    for j in rows:
        if j.get("status")=="pending" and len(claimed)<limit:
            j["status"]="running"; j["started_at"]=datetime.now(timezone.utc).isoformat(); claimed.append(j)
    p.write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+"\n",encoding="utf-8")
    return claimed

def finish(path,job_id,ok,error=""):
    p=Path(path); rows=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    for j in rows:
        if j.get("job_id")==job_id:
            j["attempts"]=int(j.get("attempts",0))+1
            if ok: j["status"]="succeeded"
            elif j["attempts"]<3: j["status"]="retrying"; j["retry_after_seconds"]=[30,120,300][min(j["attempts"],3)-1]
            else: j["status"]="failed"; j["error"]=error; j["dead_letter"]=True
            j["finished_at"]=datetime.now(timezone.utc).isoformat()
    p.write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+"\n",encoding="utf-8")

def language_job(job_id,text,language):
    r=language_route(language)
    return {"job_id":job_id,"language":language,"agent":r["agent"],"queue":r["queue"],"text":text,"status":"pending","attempts":0}
