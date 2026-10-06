#!/usr/bin/env python3
"""Production-first multi-layer loop.

Institute -> Factory -> public production. QC/release remains downstream.
"""
from __future__ import annotations
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"production-first-loop-status.json"
COMMANDS=[
    ("institute_factory","factory/real_product_factory.py"),
    ("concrete_modules","factory/concrete_product_modules.py"),
    ("production_dashboard","factory/production_dashboard.py"),
    ("public_materializer","factory/public_production_materializer.py"),
]
results=[]
for lane, script_path in COMMANDS:
    p=subprocess.run([sys.executable,str(ROOT/script_path)],cwd=ROOT,text=True,capture_output=True)
    results.append({
        "lane":lane,"script":script_path,"returncode":p.returncode,
        "status":"PASS" if p.returncode==0 else "FAIL",
        "stdout_tail":p.stdout[-2000:],"stderr_tail":p.stderr[-2000:]
    })
    if p.returncode:
        break

payload={
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "mode":"production-first",
    "pipeline":["INSTITUTE","FACTORY","QC/GATE","PUBLIC SHOWROOM/SALE"],
    "completed_lanes":[x["lane"] for x in results if x["status"]=="PASS"],
    "results":results,
    "production_is_primary":True,
    "verification_is_downstream":True,
    "dispatch_policy":"NO until explicit downstream release",
    "no_quantum_execution_claim":True,
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(payload,ensure_ascii=False,indent=2))
if any(x["status"]=="FAIL" for x in results):
    raise SystemExit(1)
