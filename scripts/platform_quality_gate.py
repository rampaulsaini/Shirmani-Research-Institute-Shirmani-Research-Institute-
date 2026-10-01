#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; WF=ROOT/".github"/"workflows"; FAILURES=[]; WARNINGS=[]
for p in ROOT.rglob("*.json"):
    if any(x in {".git","node_modules"} for x in p.parts): continue
    try: json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: FAILURES.append(f"invalid JSON: {p.relative_to(ROOT)}: {e}")
for p in sorted(WF.glob("*.y*ml")):
    t=p.read_text(encoding="utf-8")
    if "uses: docker://" in t and ":latest" in t: FAILURES.append(f"unpinned container action: {p.relative_to(ROOT)}")
    if "schedule:" in t and "concurrency:" not in t: FAILURES.append(f"scheduled workflow lacks concurrency control: {p.relative_to(ROOT)}")
    if "runs-on:" in t and "timeout-minutes:" not in t: WARNINGS.append(f"workflow has no explicit timeout: {p.relative_to(ROOT)}")
required=["AGENT-GOVERNANCE.md","SECURITY.md","README.md","factory/signal_to_language.py","tests/test_signal_to_language.py","docs/yatharth-governance/signal-to-language.md"]
for x in required:
    if not (ROOT/x).is_file(): FAILURES.append(f"required platform file missing: {x}")
g=(ROOT/"AGENT-GOVERNANCE.md").read_text(encoding="utf-8").lower()
for x in ("fail-closed","independent verification","fabricate evidence"):
    if x not in g: FAILURES.append(f"agent governance missing required boundary: {x}")
report={"schema_version":"1.0","status":"PASS" if not FAILURES else "FAIL","failures":FAILURES,"warnings":WARNINGS,"workflow_count":len(list(WF.glob("*.y*ml")))}
out=ROOT/"generated"/"platform-quality-gate.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2)); sys.exit(1 if FAILURES else 0)
