#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
AG=json.loads((ROOT/'factory/agents.json').read_text(encoding='utf-8'))
status={'generated_at':datetime.now(timezone.utc).isoformat(),'mode':'free-first-orchestration','agents':[{**a,'status':'READY'} for a in AG['agents']],'supervisor':AG['supervisor'],'note':'READY means pipeline stage is registered; it does not claim an external AI model is running continuously.'}
(ROOT/'generated').mkdir(exist_ok=True)
(ROOT/'generated'/'agent-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
