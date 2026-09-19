#!/usr/bin/env python3
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"factory/repos.json").read_text(encoding="utf-8"))
WORK=ROOT/"factory/_sources"
managed=[]; external=[]

for full in CFG["repositories"]:
    if full == CFG.get("hub_repository"):
        continue
    if not full.startswith("rampaulsaini/"):
        external.append({"repository":full,"kind":"external-source","status":"SOURCE_ONLY"})
        continue
    name=full.split("/",1)[1]
    dest=WORK/name
    meta=dest/"factory-agent.json"
    runner=dest/"factory-agent.py"
    workflows=dest/".github/workflows"
    workflow=any(workflows.glob("factory-agent*.yml")) if workflows.exists() else False
    item={
        "repository":full,"kind":"managed-agent","status":"MISSING",
        "agent_manifest":meta.exists(),"agent_runner":runner.exists(),
        "workflow":workflow
    }
    if meta.exists():
        try:
            data=json.loads(meta.read_text(encoding="utf-8"))
            item["agent_id"]=data.get("agent_id") or data.get("id")
            item["role"]=data.get("role")
        except Exception as exc:
            item["agent_manifest_error"]=str(exc)
    item["status"]="READY" if all((item["agent_manifest"],item["agent_runner"],item["workflow"])) else (
        "PARTIAL" if any((item["agent_manifest"],item["agent_runner"],item["workflow"])) else "MISSING"
    )
    managed.append(item)

ready=sum(x["status"]=="READY" for x in managed)
partial=sum(x["status"]=="PARTIAL" for x in managed)
missing=sum(x["status"]=="MISSING" for x in managed)
out={
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "hub":CFG.get("hub_repository"),
    "managed_agent_count":len(managed),
    "ready_agent_count":ready,
    "partial_agent_count":partial,
    "missing_agent_count":missing,
    "external_source_count":len(external),
    "automation_mode":"event-and-schedule driven; not a continuously running external AI service",
    "managed_agents":managed,
    "external_sources":external
}
(ROOT/"generated").mkdir(exist_ok=True)
(ROOT/"generated"/"federation-status.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"managed_agents":len(managed),"ready":ready,"partial":partial,"missing":missing,"external_sources":len(external)}))
