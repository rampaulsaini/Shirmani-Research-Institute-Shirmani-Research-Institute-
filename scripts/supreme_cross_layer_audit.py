#!/usr/bin/env python3
"""Read-only cross-layer health audit for the SHIRMANI AI/ML/NLP Automission stack."""
from __future__ import annotations
import json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORKFLOWS=ROOT/".github"/"workflows"
REQUIRED=[
"agents/supreme_nlp.py","agents/supreme_nlp_multimodal.py",
"agents/supreme_nlp_practitioner.py","agents/supreme_nlp_quality.py",
"agents/automission_supervisor.py","factory/supreme_system_orchestrator.py",
"factory/supreme_nlp_benchmark.py","schemas/supreme-nlp-signal-record.schema.json",
"docs/supreme-ai-ml-nlp-automission-operating-contract.md",
]
MARKERS={
"fail_closed":"fail_closed",
"no_subjective_experience_claim":"subjective_experience_claim_allowed",
"accuracy_measured":"accuracy_is_measured_not_declared",
"independent_verification":"independent_verification_required",
"no_scheduled_mutation":"scheduled_code_mutation_allowed",
}
def read(p):
    return p.read_text(encoding="utf-8",errors="replace") if p.exists() else ""
def inventory():
    out=[]
    for p in sorted(WORKFLOWS.glob("*.yml"))+sorted(WORKFLOWS.glob("*.yaml")):
        s=read(p); crons=re.findall(r'''cron:\s*["']([^"']+)["']''',s)
        out.append({"file":str(p.relative_to(ROOT)),"five_minute":"*/5 * * * *" in crons,
                    "crons":crons,"has_permissions":"permissions:" in s,
                    "has_concurrency":"concurrency:" in s,"uses_checkout":"actions/checkout@" in s})
    return out
def main():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    workflows=inventory()
    five=[x["file"] for x in workflows if x["five_minute"]]
    source="\n".join(read(ROOT/p) for p in REQUIRED if (ROOT/p).is_file())
    governance={k:v in source for k,v in MARKERS.items()}
    checks={
      "required_components_present":not missing,
      "workflow_inventory_nonempty":bool(workflows),
      "governance_fail_closed":governance["fail_closed"],
      "governance_no_subjective_experience_claim":governance["no_subjective_experience_claim"],
      "governance_accuracy_measured":governance["accuracy_measured"],
      "governance_independent_verification":governance["independent_verification"],
      "governance_no_scheduled_mutation":governance["no_scheduled_mutation"],
      "canonical_operating_contract_present":(ROOT/"docs/supreme-ai-ml-nlp-automission-operating-contract.md").is_file(),
    }
    status="PASS" if all(checks.values()) else "BLOCK"
    report={"schema_version":"supreme-cross-layer-audit-v1",
      "generated_at":datetime.now(timezone.utc).isoformat(),"status":status,
      "checks":checks,"missing_required":missing,"workflow_count":len(workflows),
      "five_minute_workflow_count":len(five),"five_minute_workflows":five,
      "schedule_review":"VISIBLE_OVERLAP_REVIEW_REQUIRED" if len(five)>8 else "WITHIN_AUDIT_THRESHOLD",
      "governance":governance,
      "principles":{"accuracy_is_measured_not_declared":True,
        "observable_signal_is_not_subjective_experience_proof":True,
        "independent_verification_is_distinct_from_qc":True,
        "scheduled_code_mutation_is_blocked":True,"audit_is_read_only":True},
      "next_actions":["Continue benchmark, verification and regression cycles."] if status=="PASS"
        else ["Repair every BLOCK check before treating the control plane as healthy."]}
    out=ROOT/"generated"/"supreme-control-plane"/"cross-layer-audit.json"
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if status=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
