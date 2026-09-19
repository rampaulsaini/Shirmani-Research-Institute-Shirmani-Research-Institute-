#!/usr/bin/env python3
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"factory/repos.json").read_text(encoding="utf-8"))
WORK=ROOT/"factory/_sources"
managed=[]; external=[]
for full in CFG["repositories"]:
    if full == CFG.get("hub_repository"): continue
    if not full.startswith("rampaulsaini/"):
        external.append({"repository":full,"kind":"external-source","status":"SOURCE_ONLY"}); continue
    name=full.split("/",1)[1]; dest=WORK/name
    meta=dest/"factory-agent.json"; manifest=dest/"agent-output"/"manifest.json"
    item={"repository":full,"kind":"managed-agent","status":"MISSING","agent_manifest":meta.exists(),"output_manifest":manifest.exists()}
    if meta.exists():
        try:
            data=json.loads(meta.read_text(encoding="utf-8")); item["agent_id"]=data.get("agent_id") or data.get("id"); item["role"]=data.get("role")
        except Exception as exc: item["agent_manifest_error"]=str(exc)
    if manifest.exists(): item["output_sha256"]=hashlib.sha256(manifest.read_bytes()).hexdigest()
    item["status"]="READY" if item["agent_manifest"] and item["output_manifest"] else "PARTIAL"
    managed.append(item)
ready=sum(x["status"]=="READY" for x in managed)
out={"generated_at":datetime.now(timezone.utc).isoformat(),"hub":CFG.get("hub_repository"),"managed_agent_count":len(managed),"ready_agent_count":ready,"partial_agent_count":sum(x["status"]=="PARTIAL" for x in managed),"external_source_count":len(external),"automation_mode":"event-and-schedule driven; not a continuously running external AI service","managed_agents":managed,"external_sources":external}
(ROOT/"generated").mkdir(exist_ok=True)
(ROOT/"generated"/"federation-status.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"managed_agents":len(managed),"ready":ready,"partial":out["partial_agent_count"],"external_sources":len(external)}))
