"""Deterministic Automission supervisor for continuous quality improvement."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

def inspect(status_path="generated/supreme-nlp/status.json"):
    p=Path(status_path)
    if not p.exists():
        return {"state":"NO_STATUS","actions":["generate a status record"]}
    d=json.loads(p.read_text(encoding="utf-8"))
    r=d.get("result", {})
    f=r.get("features", {})
    actions=[]
    if r.get("status") != "interpreted": actions.append("collect higher-quality signals")
    if f.get("evidence_grade") in {"C","D"}: actions.append("increase evidence quality and independent validation")
    if f.get("agreement",1) < .5: actions.append("investigate cross-signal disagreement")
    if f.get("modalities",0) < 2: actions.append("add an independent modality where scientifically appropriate")
    if not actions: actions.append("continue scheduled monitoring and regression tests")
    return {
        "state":"IMPROVEMENT_REQUIRED" if len(actions)>1 else "MONITOR",
        "actions":actions,
        "source_fingerprint":d.get("fingerprint"),
        "generated_at":datetime.now(timezone.utc).isoformat()
    }

if __name__=="__main__":
    out=inspect()
    Path("generated/supreme-nlp").mkdir(parents=True,exist_ok=True)
    Path("generated/supreme-nlp/automission-plan.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
    print(out)
