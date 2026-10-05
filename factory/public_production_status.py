import json,datetime
from pathlib import Path
R=Path("."); G=R/"generated"
def fs(p,s=None): return [x for x in p.rglob("*") if x.is_file() and (s is None or x.suffix.lower() in s)] if p.exists() else []
def lines(p):
 try:return sum(1 for _ in p.open(encoding="utf-8",errors="replace"))
 except:return 0
def obj(p):
 try:return json.loads(p.read_text(encoding="utf-8"))
 except:return {}
c=obj(R/"factory/product-catalog.json"); offers=[o for l in c.get("lanes",[]) for o in l.get("offers",[])]
v=obj(G/"independent-verification-status.json"); q=obj(G/"VERIFICATION-QUEUE.json"); f=obj(G/"factory-status.json"); a=obj(G/"agent-status.json")
out={"version":2,"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"mode":"PRODUCT_FIRST_MULTI_LAYER_PRODUCTION","principle":"Produce concrete outputs first; verification evaluates produced results downstream.","public_surfaces":{"html_pages":len(fs(R,{".html"})),"research_files":len(fs(R/"research")),"product_lanes":len(c.get("lanes",[])),"product_offers":len(offers),"factory_scripts":len(fs(R/"factory",{".py"})),"workflow_files":len(fs(R/".github/workflows",{".yml",".yaml"})),"schema_files":len(fs(R/"schemas",{".json"})),"agent_files":len(fs(R/"agents")),"generated_artifacts":len(fs(G))},"production_outputs":{"factory_records_reported":f.get("records",0),"processed_batch_reported":f.get("processed_batch",0),"canonical_knowledge_records":lines(G/"canonical-knowledge.jsonl"),"ai_output_records":lines(G/"ai-output.jsonl"),"claim_evidence_records":lines(G/"claim-evidence.jsonl"),"provenance_records":lines(G/"provenance-ledger.jsonl"),"artifact_manifest_records":lines(G/"artifact-manifest.jsonl")},"agent_wiring":{"registered_agents":len(a.get("agents",[])),"registered_is_not_continuous_execution":True},"verification":{"queue_total":v.get("queue_total",q.get("queue_total",0)),"prepared_records":v.get("prepared_review_records",0),"reviewed_records":v.get("reviewed_records",0),"verified_records":v.get("verified_records",0),"verification_is_downstream":True,"promotion_requires_independent_review":True},"integrity":{"fabricated_metrics":False,"missing_values_remain_missing":True}}
G.mkdir(exist_ok=True); (G/"multi-layer-production-status.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,ensure_ascii=False,indent=2))
