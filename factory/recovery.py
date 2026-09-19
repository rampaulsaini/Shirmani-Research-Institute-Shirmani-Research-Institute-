#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; failures=[]
for p in OUT.glob("*report.json"):
    try:
        x=json.loads(p.read_text(encoding="utf-8"))
        if x.get("status")=="FAIL": failures.append(p.name)
    except Exception: pass
state=json.loads((OUT/"recovery-state.json").read_text(encoding="utf-8")) if (OUT/"recovery-state.json").exists() else {}
plan={"generated_at":datetime.now(timezone.utc).isoformat(),"status":"RECOVERED" if state.get("success") and not failures else ("REVIEW_REQUIRED" if failures else "READY"),"failed_reports":failures,"last_stage":state,"rules":["retry transient failures","never fabricate unavailable sources","require QC before publication","research remains draft until independently verified"]}
(OUT/"recovery-plan.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps(plan,ensure_ascii=False))
