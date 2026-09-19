"""Source -> corpus -> topic -> research -> verification -> provenance -> QC -> publishing."""
from pathlib import Path
from datetime import datetime, timezone
import json
from .research_agent import question
from .verification_agent import classify
from .topic_agent import enrich
from .provenance_agent import record, validate
from .qc_agent import run as qc
from .publishing_agent import publish

def run(corpus, out, topic_path=None, batch_size=1000):
    rows=[json.loads(x) for x in Path(corpus).read_text(encoding="utf-8").splitlines() if x.strip()]
    Path(out).mkdir(parents=True, exist_ok=True)
    if topic_path:
        rows=enrich(rows, topic_path)
    claims=[]
    products=[]
    for r in rows[:batch_size]:
        claims.append({
            "id":r["id"],
            "topics":r.get("topics",["general"]),
            "research":question(r["text"]),
            "verification":classify(r["text"],r.get("source"))
        })
        p=record("claim",r.get("source","unknown"),r["text"],str(r["id"]),
                 classify(r["text"],r.get("source")),r.get("topics",[]))
        if validate(p):
            products.append(p)
    Path(out,"claims-index.json").write_text(json.dumps(claims,ensure_ascii=False,indent=2),encoding="utf-8")
    Path(out,"provenance-index.jsonl").write_text(
        "\n".join(json.dumps(x,ensure_ascii=False) for x in products)+"\n",encoding="utf-8")
    status={
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "agents":["source","corpus","topic","research","verification","provenance","writing","book","certificate","music","qc","publishing"],
        "records":len(rows),"processed_batch":min(len(rows),batch_size),
        "qc":qc(out)
    }
    publish(out,status)
    return status
