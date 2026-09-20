"""Second-generation orchestration with provenance, language routing and artifact manifests."""
from pathlib import Path
from datetime import datetime, timezone
import json
from .research_agent import question
from .verification_agent import classify
from .topic_agent import enrich
from .provenance_agent import record, validate
from .language_agents import detect, route as language_route
from .artifact_agent import manifest_record, append
from .qc_agent import run as qc
from .publishing_agent import publish
from .contract_bridge import source_record, concept_records, claim_record, verification_report

def run(corpus, out, topic_path=None, batch_size=1000):
    rows=[json.loads(x) for x in Path(corpus).read_text(encoding="utf-8").splitlines() if x.strip()]
    Path(out).mkdir(parents=True, exist_ok=True)
    if topic_path:
        rows=enrich(rows, topic_path)
    claims=[]; products=[]; contract_sources=[]; contract_concepts=[]; contract_claims=[]; verification_reports=[]
    artifact_path=Path(out)/"artifact-manifest.jsonl"
    artifact_path.write_text("",encoding="utf-8")
    queue_dir=Path(out)/"queues"; queue_dir.mkdir(exist_ok=True)
    for r in rows[:batch_size]:
        language=detect(r.get("text",""))
        verification=classify(r["text"],r.get("source"))
        contract_row={**r,"topics":r.get("topics",["general"])}
        src=source_record(contract_row)
        contract_sources.append(src)
        contract_concepts.extend(concept_records(contract_row))
        claims.append({
            "id":r["id"], "topics":r.get("topics",["general"]),
            "research":question(r["text"]), "verification":verification,
            "language":language, "language_route":language_route(language)
        })
        cp=claim_record(contract_row, "UNVERIFIED", r.get("source") or r.get("repository") or "unknown")
        contract_claims.append(cp)
        verification_reports.append(verification_report(cp, "NOT_VERIFIED"))
        p=record("claim",r.get("source","unknown"),r["text"],str(r["id"]),verification["status"],r.get("topics",[]))
        if validate(p):
            products.append(p)
            append(artifact_path,manifest_record("claim",language,r["text"],[r["id"]],"orchestrator","draft",
                {"source":r.get("source","unknown"),"verification_status":verification["status"]}))
            q=queue_dir/f"language.{language}.jsonl"
            with q.open("a",encoding="utf-8") as f:
                f.write(json.dumps({"job_id":f"claim-{r['id']}","artifact_id":p["id"],"language":language,
                                    "agent":language_route(language)["agent"],"status":"pending","attempts":0},
                                   ensure_ascii=False)+"\n")
    Path(out,"claims-index.json").write_text(json.dumps(claims,ensure_ascii=False,indent=2),encoding="utf-8")
    contract_dir=Path(out)/"contracts"; contract_dir.mkdir(exist_ok=True)
    for name, records in (("source-records.jsonl",contract_sources),("concept-records.jsonl",contract_concepts),("claim-records.jsonl",contract_claims),("verification-reports.jsonl",verification_reports)):
        (contract_dir/name).write_text("\\n".join(json.dumps(x,ensure_ascii=False) for x in records)+("\\n" if records else ""),encoding="utf-8")
    Path(out,"provenance-index.jsonl").write_text(
        "\n".join(json.dumps(x,ensure_ascii=False) for x in products)+"\n",encoding="utf-8")
    status={
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "agents":["source","corpus","topic","router","nvidia-or-fallback","research","verification","provenance","language.hi","language.pa","language.en","writing","book","certificate","music","qc","publishing"],
        "records":len(rows),"processed_batch":min(len(rows),batch_size),
        "artifact_manifest":str(artifact_path.relative_to(Path(out))),
        "language_queues":sorted(str(p.relative_to(queue_dir)) for p in queue_dir.glob("*.jsonl")),
        "qc":qc(out)
    }
    publish(out,status)
    return status
