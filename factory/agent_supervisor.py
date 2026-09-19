#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
AG=json.loads((ROOT/'factory/agents.json').read_text(encoding='utf-8'))
runtime={}
p=ROOT/'generated'/'agent-runtime.json'
if p.exists(): runtime=json.loads(p.read_text(encoding='utf-8'))
status=[]
for a in AG['agents']:
    status.append({**a,'status':'REGISTERED','execution':next((x['execution'] for x in runtime.get('agents',[]) if x.get('id')==a['id']),'pipeline-stage')})
out={'generated_at':datetime.now(timezone.utc).isoformat(),'mode':'free-first-orchestration','agents':status,'supervisor':AG['supervisor'],'note':'REGISTERED means the stage is wired into the factory pipeline; it does not claim a continuously running external AI model.'}
(ROOT/'generated').mkdir(exist_ok=True)
(ROOT/'generated'/'agent-status.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
