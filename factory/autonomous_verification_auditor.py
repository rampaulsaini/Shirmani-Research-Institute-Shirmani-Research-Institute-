#!/usr/bin/env python3
"""Autonomous verification auditor. Never promotes records to VERIFIED."""
from __future__ import annotations
import hashlib, json, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
QUEUE=OUT/"independent-verification-queue.jsonl"
REG=OUT/"independent-verification-registry.jsonl"

def load(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def fetch(url):
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"SHIRMANI-Autonomous-Verification-Auditor/1.0"})
        with urllib.request.urlopen(req,timeout=12) as r:
            data=r.read(200000)
            return {"ok":200 <= r.status < 400,"status":r.status,"bytes":len(data),
                    "sha256":hashlib.sha256(data).hexdigest()}
    except Exception as e:
        return {"ok":False,"error":type(e).__name__+":"+str(e)[:180]}

def main():
    queue=load(QUEUE); registry=load(REG)
    by_task={r.get("task_id"):r for r in registry}
    rows=[]
    for q in queue:
        task=q.get("task_id","")
        r=by_task.get(task,{})
        refs=[x for x in q.get("source_ids",[]) if isinstance(x,str) and x.startswith(("http://","https://"))]
        source_checks=[{"url":u,**fetch(u)} for u in refs]
        external_ok=sum(x.get("ok",False) for x in source_checks)
        has_counter=(r.get("countercase_review") or {}).get("status")=="REVIEWED"
        has_test=(r.get("reproduction_or_test") or {}).get("status") in {"PASSED","SUPPORTED"}
        has_reviewer=bool(str(r.get("reviewer","")).strip()) and bool(str(r.get("reviewer_role","")).strip())
        machine_ready=bool(refs) and external_ok==len(refs) and has_test and has_counter
        rows.append({
            "claim_id":q.get("claim_id"),"task_id":task,
            "source_count":len(refs),"reachable_source_count":external_ok,
            "source_checks":source_checks,
            "reproduction_ready":has_test,"counterevidence_reviewed":has_counter,
            "reviewer_present":has_reviewer,
            "machine_verification_candidate":machine_ready,
            "human_independent_verification":(
                r.get("verification_status")=="VERIFIED" and r.get("independent") is True
            )
        })
    report={
        "schema_version":"1.0.0","generated_at":datetime.now(timezone.utc).isoformat(),
        "purpose":"autonomous verification while author is absent",
        "queue_records":len(queue),
        "machine_verification_candidates":sum(x["machine_verification_candidate"] for x in rows),
        "human_independent_verified":sum(x["human_independent_verification"] for x in rows),
        "policy":{
            "runs_without_author":True,
            "workflow_success_is_not_verification":True,
            "machine_candidate_is_not_VERIFIED":True,
            "human_independent_decision_required_for_VERIFIED":True
        },
        "records":rows
    }
    (OUT/"AUTONOMOUS-VERIFICATION-AUDIT.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="records"},ensure_ascii=False))

if __name__=="__main__":
    main()
