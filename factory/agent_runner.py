#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
agents=json.loads((ROOT/"factory/agents.json").read_text(encoding="utf-8"))["agents"]
out=ROOT/"generated"; out.mkdir(exist_ok=True)
state={
 "generated_at":datetime.now(timezone.utc).isoformat(),
 "mode":"free-first deterministic orchestration",
 "agents":[{"id":a["id"],"role":a["role"],"status":"READY","execution":"pipeline-stage"} for a in agents],
 "note":"READY means registered and executable as a pipeline stage; it does not claim a continuously running external AI model."
}
(out/"agent-runtime.json").write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding="utf-8")
print("agent stages registered:",len(agents))
