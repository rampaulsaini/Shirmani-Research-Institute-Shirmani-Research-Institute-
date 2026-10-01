#!/usr/bin/env python3
"""Dependency-light deterministic quality gate for the SHIRMANI agent/factory stack."""
from __future__ import annotations
import ast, json, pathlib, re, sys, time
ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORT = ROOT / "generated" / "supreme-quality-report.json"
REQUIRED = [
    "agents/orchestrator.py","agents/qc_agent.py","agents/provenance_agent.py",
    "agents/language_agents.py","agents/deep_learning_agent.py",
    "factory/verification_queue.py","factory/verification_promotion_gate.py",
    "factory/verification_registry.py","scripts/validate_json.py",
    ".github/workflows/shirmani-multi-automation-supervisor.yml",
    ".github/workflows/shirmani-inter-repository-automission.yml",
    ".github/workflows/shirmani-continuous-audit.yml",
]
def read(p): return p.read_text(encoding="utf-8", errors="strict")
def main():
    started=time.time(); checks=[]; critical=[]
    def check(name, passed, detail, is_critical=True):
        item={"name":name,"passed":bool(passed),"critical":is_critical,"detail":detail}
        checks.append(item)
        if is_critical and not passed: critical.append(item)
    for rel in REQUIRED:
        p=ROOT/rel; check("required_file:"+rel,p.is_file(),"present" if p.is_file() else "missing")
    py_files=[p for base in ("agents","factory","scripts") for p in (ROOT/base).rglob("*.py")]
    py_errors=[]
    for p in py_files:
        try: ast.parse(read(p),filename=str(p))
        except SyntaxError as e: py_errors.append(f"{p.relative_to(ROOT)}:{e.lineno}:{e.offset} {e.msg}")
    check("python_ast",not py_errors,f"{len(py_files)} Python files parsed; errors={len(py_errors)}")
    json_files=[p for base in ("factory","schemas","generated") for p in (ROOT/base).rglob("*.json")]
    json_errors=[]
    for p in json_files:
        try: json.loads(read(p))
        except Exception as e: json_errors.append(f"{p.relative_to(ROOT)}: {e}")
    check("json_integrity",not json_errors,f"{len(json_files)} JSON files parsed; errors={len(json_errors)}")
    wfdir=ROOT/".github"/"workflows"; workflows=sorted(wfdir.glob("*.y*ml")); names={}; structural=[]
    for p in workflows:
        t=read(p); m=re.search(r"^name:\s*(.+?)\s*$",t,re.M); n=m.group(1).strip().strip("'\\"") if m else p.name
        names.setdefault(n,[]).append(p.name)
        if not re.search(r"^on:\s*(?:$|.*)",t,re.M): structural.append(f"{p.name}: missing on")
        if not re.search(r"^jobs:\s*$",t,re.M): structural.append(f"{p.name}: missing jobs")
    dup={k:v for k,v in names.items() if len(v)>1}
    check("workflow_structure",not structural,f"{len(workflows)} workflows inspected; structural_errors={len(structural)}")
    check("workflow_name_uniqueness",not dup,f"duplicate_names={len(dup)}",False)
    sup=ROOT/".github/workflows/shirmani-multi-automation-supervisor.yml"
    if sup.is_file():
        t=read(sup)
        check("five_minute_supervision",'cron: "*/5 * * * *"' in t,"5-minute schedule present")
        check("safe_retry_boundary",'r.get("event") not in {"schedule","workflow_dispatch"}' in t,"push-triggered failures excluded")
    fed=ROOT/".github/workflows/shirmani-inter-repository-automission.yml"
    if fed.is_file():
        t=read(fed)
        check("downstream_receipt_gate","independent_verification_claim" in t and "receipt.status != 'RECEIVED'" in t,"receiver receipt required")
        check("credential_fail_closed","Federation dispatch skipped safely" in t,"credential failure fails closed")
    keywords={"agents/qc_agent.py":["def"],"agents/provenance_agent.py":["def"],"factory/verification_promotion_gate.py":["verify","promotion"]}
    for rel,ks in keywords.items():
        p=ROOT/rel; c=read(p).lower() if p.is_file() else ""; missing=[k for k in ks if k not in c]
        check("control_surface:"+rel,not missing,"keywords checked")
    report={"status":"PASS" if not critical else "FAIL","gate":"SHIRMANI Supreme Quality Gate",
      "principle":"engineering evidence before promotion; no claim of perfect model accuracy",
      "timestamp_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"duration_seconds":round(time.time()-started,3),
      "workflow_count":len(workflows),"python_file_count":len(py_files),"json_file_count":len(json_files),
      "critical_failure_count":len(critical),"checks":checks,
      "details":{"python_errors":py_errors[:20],"json_errors":json_errors[:20],"workflow_errors":structural[:20]}}
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); return 0 if not critical else 1
if __name__=="__main__": raise SystemExit(main())
