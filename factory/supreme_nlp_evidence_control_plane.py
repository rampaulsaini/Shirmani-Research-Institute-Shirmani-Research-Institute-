"""SHIRMANI Supreme NLP Evidence Control Plane."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
from agents.supreme_nlp import build_record
from agents.supreme_nlp_multimodal import analyze
from agents.supreme_nlp_quality import evaluate

INPUT=Path("generated/signal-input.jsonl")
OUT=Path("generated/supreme-nlp")
OUT.mkdir(parents=True,exist_ok=True)

def load_rows():
    if not INPUT.exists(): return []
    rows=[]
    for line in INPUT.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        try: item=json.loads(line)
        except json.JSONDecodeError: continue
        if isinstance(item,dict): rows.append(item)
    return rows

def run():
    rows=load_rows()
    multimodal=analyze(rows,request="automission",source_type="signal-input" if rows else "no-input")
    base=build_record(rows,"supreme-evidence-control-plane")
    f=base["result"].get("features",{})
    base["result"]["features"]={**f,
        "quality":multimodal["metrics"]["quality"],
        "agreement":multimodal["metrics"]["agreement"],
        "independent_sources":len(multimodal["metrics"]["sources"]),
        "sample_count":multimodal["metrics"]["usable_observations"],
        "drift_score":multimodal["metrics"]["baseline_drift"]}
    quality=evaluate(base)
    report={
      "schema_version":"supreme-nlp-evidence-control-plane-v1",
      "generated_at":datetime.now(timezone.utc).isoformat(),
      "pipeline":["observe","normalize","multimodal-fusion","quality-gate","contradiction-check","uncertainty","independent-verification","simple-language","audit"],
      "input":{"path":str(INPUT),"observations":len(rows)},
      "multimodal":multimodal,"base_record":base,"quality_gate":quality,
      "promotion":{"candidate_ready":quality["status"]=="PASS","production_promotion_allowed":False,
                   "reason":"Independent verification remains mandatory; scheduled Automission cannot self-declare VERIFIED."},
      "governance":{"fail_closed":True,"subjective_experience_claim_allowed":False,
                    "scheduled_code_mutation_allowed":False,"independent_verification_required":True,
                    "accuracy_is_measured_not_declared":True,"raw_observations_preserved":True}}
    (OUT/"evidence-control-plane.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return report

if __name__=="__main__":
    d=run()
    print(json.dumps({"status":d["quality_gate"]["status"],"observations":d["input"]["observations"],
                      "promotion_allowed":d["promotion"]["production_promotion_allowed"],
                      "fingerprint":d["quality_gate"]["fingerprint"]},ensure_ascii=False))
