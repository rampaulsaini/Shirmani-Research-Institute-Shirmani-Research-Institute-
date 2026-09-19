"""Source -> corpus -> research -> verification -> QC -> publishing."""
from pathlib import Path
from datetime import datetime,timezone
import json
from .research_agent import question
from .verification_agent import classify
from .qc_agent import run as qc
from .publishing_agent import publish
def run(corpus,out):
    rows=[json.loads(x) for x in Path(corpus).read_text(encoding='utf-8').splitlines() if x.strip()]
    Path(out).mkdir(parents=True,exist_ok=True)
    claims=[{'id':r['id'],'research':question(r['text']),'verification':classify(r['text'],r.get('source'))} for r in rows[:1000]]
    Path(out,'claims-index.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2),encoding='utf-8')
    status={'generated_at':datetime.now(timezone.utc).isoformat(),'agents':['source','corpus','research','verification','writing','book','certificate','qc','publishing'],'records':len(rows),'qc':qc(out)}
    publish(out,status); return status
