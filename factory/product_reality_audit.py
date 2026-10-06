from pathlib import Path
from datetime import datetime,timezone
import json,re
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; CAT=GEN/"1000-digital-products.json"; OUT=GEN/"product-reality-audit.json"; HTML=ROOT/"production-reality-control-center.html"
AI=re.compile(r"(openai|anthropic|gemini|transformers|torch|tensorflow|sklearn|scikit-learn|ollama|huggingface|vertexai|bedrock)",re.I)
NLP=re.compile(r"(spacy|nltk|transformers|tokeniz|language model|nlp)",re.I)
def main():
 d=json.loads(CAT.read_text(encoding="utf-8")); ps=d.get("products",[]); concrete=sum(1 for p in ps if (ROOT/p.get("asset","")).is_file() and (ROOT/p.get("asset","")).stat().st_size>0)
 engines=sorted(set(p.get("engine","") for p in ps)); fam={}; ai=[]; nlp=[]
 for p in ps: fam[p.get("family","unknown")]=fam.get(p.get("family","unknown"),0)+1
 for folder in [ROOT/"factory",ROOT/".github/workflows",ROOT/"scripts",ROOT/"source"]:
  if not folder.exists(): continue
  for f in folder.rglob("*"):
   if f.is_file() and f.suffix.lower() in {".py",".yml",".yaml",".json",".md",".js",".ts",".html"}:
    t=f.read_text(encoding="utf-8",errors="ignore")
    if AI.search(t): ai.append(str(f.relative_to(ROOT)))
    if NLP.search(t): nlp.append(str(f.relative_to(ROOT)))
 r={"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_products":len(ps),"concrete_assets":concrete,"concrete_asset_percent":round(100*concrete/len(ps),2) if ps else 0,"remaining_concrete_assets":len(ps)-concrete,"engine_count":len(engines),"family_count":len(fam),"family_distribution":dict(sorted(fam.items())),"ai_ml_execution_evidence_files":sorted(set(ai)),"nlp_execution_evidence_files":sorted(set(nlp)),"ai_ml_execution_evidence_status":"EVIDENCE_DETECTED" if ai else "NOT_DETECTED","nlp_execution_evidence_status":"EVIDENCE_DETECTED" if nlp else "NOT_DETECTED","truth_rules":{"workflow_run_is_product":False,"catalog_identity_is_product":False,"concrete_asset_is_sale":False,"concrete_asset_is_payment":False,"concrete_asset_is_independent_verification":False,"orchestration_name_is_model_execution":False}}
 GEN.mkdir(exist_ok=True); OUT.write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 if HTML.exists():
  s=HTML.read_text(encoding="utf-8")
  for k,v in {"CATALOG":r["catalog_products"],"CONCRETE":r["concrete_assets"],"PCT":r["concrete_asset_percent"],"ENGINES":r["engine_count"],"AI":r["ai_ml_execution_evidence_status"],"NLP":r["nlp_execution_evidence_status"],"TIME":r["generated_at"]}.items(): s=s.replace("{{"+k+"}}",str(v))
  HTML.write_text(s,encoding="utf-8")
 print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
