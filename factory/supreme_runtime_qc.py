#!/usr/bin/env python3
"""Supreme runtime contract QC.

Deterministic, provider-free guardrail for the AI/ML/NLP/Automission architecture.
It validates the canonical layers and fail-closed boundaries without claiming
scientific verification or executing autonomous external side effects.
"""
from __future__ import annotations
import json, py_compile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=[
"schemas/agent-governance.json",
"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
"factory/agent_governance_qc.py","factory/quality_control.py",
"factory/reasoning_pipeline.py","factory/verification_queue.py",
"factory/verification_promotion_gate.py",
]
LAYERS={"intake_source","reasoning","evidence","verification","product","marketing",
"economic_transaction","security_audit","publishing","continuity"}
def block(msg): raise SystemExit("SUPREME-RUNTIME-QC: BLOCK: "+msg)
def main():
    missing=[p for p in REQUIRED_FILES if not (ROOT/p).is_file()]
    if missing: block("missing required architecture files: "+", ".join(missing))
    policy=json.loads((ROOT/"schemas/agent-governance.json").read_text(encoding="utf-8"))
    if policy.get("fail_closed") is not True: block("fail_closed is not true")
    if policy.get("default_status")!="unverified": block("default_status is not unverified")
    if set(policy.get("agent_layers",[]))!=LAYERS: block("agent layer contract mismatch")
    auth=policy.get("authorization",{})
    if auth.get("irreversible_actions")!="owner_authorization_required": block("irreversible action boundary missing")
    if auth.get("verification_promotion")!="independent_verification_required": block("verification promotion boundary missing")
    if policy.get("provenance_required_for_claims") is not True: block("provenance requirement missing")
    if policy.get("fabrication_prohibited") is not True: block("fabrication prohibition missing")
    if policy.get("secret_handling")!="secret_store_only": block("secret handling contract mismatch")
    if policy.get("public_surface_may_expose_secrets") is not False: block("public secret exposure boundary mismatch")
    graph=(ROOT/"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md").read_text(encoding="utf-8").lower()
    for phrase in ["multimodal perception","ml models","nlp: natural language processing",
        "multimodal fusion","context + ontology + knowledge graph","reasoning + uncertainty",
        "planner agent","evidence agent","verification agent","security agent","fail closed",
        "continuous improvement","measured signal","model inference","confidence","unresolved uncertainty"]:
        if phrase not in graph: block("canonical graph missing: "+phrase)
    errors=[]
    for path in sorted((ROOT/"factory").glob("*.py"))+sorted((ROOT/"agents").glob("*.py")):
        try: py_compile.compile(str(path),doraise=True)
        except Exception as exc: errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if errors: block("python compile errors: "+" | ".join(errors))
    report={"status":"PASS","contract":"supreme-ai-ml-nlp-automission",
      "scientific_verification":"not_claimed",
      "signal_interpretation_boundary":"measured_signal != subjective_feeling_proof",
      "checked_required_files":len(REQUIRED_FILES),"python_compile":"PASS"}
    out=ROOT/"generated/supreme-runtime-qc.json"; out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("SUPREME-RUNTIME-QC: PASS")
if __name__=="__main__": main()
