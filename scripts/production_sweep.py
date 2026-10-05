#!/usr/bin/env python3
"""Supreme multi-lane production sweep: production first, verification downstream."""
from __future__ import annotations
import json, subprocess, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"production"; OUT.mkdir(parents=True,exist_ok=True)

def run(cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    return {"command":" ".join(cmd),"returncode":p.returncode,"status":"PASS" if p.returncode==0 else "FAIL","stdout":p.stdout[-4000:],"stderr":p.stderr[-4000:]}

def load_json(path):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return None

files=[p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
counts=Counter(p.suffix.lower() for p in files)
lanes={"research_knowledge":[".md",".jsonl"],"public_modules":[".html"],"ai_ml_nlp":[".py",".js"],"automation":[".yml",".yaml",".trigger"],"data_schema":[".json"],"media_archive":[".jpg",".png",".mp3",".wav",".mp4",".pdf"]}
lane_counts={k:sum(counts[e] for e in v) for k,v in lanes.items()}

agents_payload=load_json(ROOT/"factory"/"agents.json") or {}
factory_agents=agents_payload.get("agents",[])
queue_payload=load_json(ROOT/"automation"/"queue"/"tasks.json") or {}
tasks=queue_payload.get("tasks",[])

runs=[run([sys.executable,"factory/agent_runner.py"]),run([sys.executable,"factory/agent_supervisor.py"]),run([sys.executable,"factory/agent_governance_qc.py"])]

json_failures=[]; json_checked=0
for p in ROOT.rglob("*.json"):
    if ".git" in p.parts: continue
    json_checked+=1
    if load_json(p) is None: json_failures.append(str(p.relative_to(ROOT)))

workflow_dir=ROOT/".github"/"workflows"
workflow_count=len(list(workflow_dir.glob("*.yml")))+len(list(workflow_dir.glob("*.yaml"))) if workflow_dir.exists() else 0

status={"generated_at":datetime.now(timezone.utc).isoformat(),"mode":"production-first-multi-lane-automission","repository":"rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-","inventory":{"total_files":len(files),"workflows":workflow_count,"factory_agents":len(factory_agents),"queue_tasks":len(tasks),"json_checked":json_checked,"json_failures":len(json_failures)},"lanes":lane_counts,"production_policy":{"primary_goal":"produce traceable outputs across many lanes","verification_role":"downstream quality/evidence state","fail_closed_for":["fabrication","secrets","irreversible external actions","verification promotion"],"quantum_mode":"quantum-inspired prioritization; no claim of physical quantum compute"},"factory_agents":[{"id":a.get("id"),"role":a.get("role"),"status":"READY_FOR_SWEEP"} for a in factory_agents],"queue":[{"id":t.get("id"),"type":t.get("type"),"priority":t.get("priority"),"safe":t.get("safe")} for t in tasks],"deterministic_runs":runs,"json_failures":json_failures[:100],"result_semantics":{"READY_FOR_SWEEP":"registered production lane/stage","PASS":"deterministic execution or syntax check passed","FAIL":"deterministic execution needs repair","VERIFIED":"reserved for independently supported evidence; never auto-promoted by this sweep"}}
(OUT/"production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

md=["# ꙰ Supreme Production Mission","","Generated: "+status["generated_at"],"","Production is primary. Verification is downstream evidence/quality state.","","## Production map"]
md += ["- **"+k+"**: "+str(v)+" discoverable files/modules" for k,v in lane_counts.items()]
md += ["","## Runtime inventory","- Total files: **"+str(len(files))+"**","- GitHub workflows: **"+str(workflow_count)+"**","- Factory agents: **"+str(len(factory_agents))+"**","- Queue tasks: **"+str(len(tasks))+"**","- JSON files checked: **"+str(json_checked)+"**","- JSON syntax failures: **"+str(len(json_failures))+"**","","## Execution rule","Every cycle should create or update traceable artifacts where a lane has work. A successful workflow is not itself an independent verification claim."]
(OUT/"production-report.md").write_text("\n".join(md)+"\n",encoding="utf-8")
print("production sweep complete:",len(files),"files,",len(factory_agents),"factory agents,",len(tasks),"queue tasks")
