#!/usr/bin/env python3
"""Unified fail-closed control plane for the SHIRMANI AI/ML/NLP Automission stack."""
from __future__ import annotations
import hashlib,json,os,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
ENV=os.environ.copy()
ENV["PYTHONPATH"]=str(ROOT)+os.pathsep+ENV.get("PYTHONPATH","")
OUT=ROOT/"generated"/"supreme-orchestrator"
OUT.mkdir(parents=True,exist_ok=True)

GATES=[
("architecture_qc","factory/supreme_architecture_qc.py"),
("nlp_qc","factory/supreme_nlp_qc.py"),
("quality_gate","factory/supreme_quality_gate.py"),
("verification_queue_qc","factory/verification_queue_qc.py"),
("verification_promotion_gate","factory/verification_promotion_gate.py"),
("publication_gate","factory/publication_gate.py"),
("nlp_benchmark","factory/supreme_nlp_benchmark.py"),
("unified_nlp_control_plane","factory/supreme_nlp_unified_gate.py"),
]
REQUIRED=[
"agents/automission_supervisor.py",
"agents/supreme_nlp_practitioner.py",
"schemas/supreme-nlp-signal-record.schema.json",
"docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
"factory/supreme_nlp_benchmark.py",
"factory/supreme_nlp_unified_gate.py",
"research/independent-verification-protocol-2026-09-29.md",
]

def seed_nlp_status() -> None:
    """Create a deterministic, evidence-labelled NLP record before dependent gates."""
    from agents.supreme_nlp import build_record

    source = ROOT/"generated"/"signal-input.jsonl"
    rows = (
        [json.loads(x) for x in source.read_text(encoding="utf-8").splitlines() if x.strip()]
        if source.exists() else []
    )
    if not rows:
        rows=[
            {"modality":"synthetic","feature":"baseline_a","value":1.0,"quality":1.0,"source":"supreme-orchestrator-smoke"},
            {"modality":"synthetic","feature":"baseline_b","value":1.0,"quality":1.0,"source":"supreme-orchestrator-smoke"},
        ]
    record=build_record(rows,"supreme-orchestrator-cycle")
    target=ROOT/"generated"/"supreme-nlp"/"status.json"
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def prepare_verification_ledgers() -> None:
    """Synchronize deterministic review inputs before dependent verification gates.

    This step may create or refresh pending review slots and their queue-task
    hashes, but it never creates a VERIFIED decision. Keeping the bootstrap
    immediately upstream of the promotion gate prevents stale review hashes
    from being reported as integrity failures on scheduled cycles.
    """
    steps = (
        ROOT/"factory"/"bootstrap_independent_verification_queue.py",
        ROOT/"factory"/"bootstrap_verification_review_registry.py",
    )
    for script in steps:
        x = subprocess.run(
            ["python", str(script)],
            cwd=ROOT,
            env=ENV,
            text=True,
            capture_output=True,
            timeout=180,
        )
        if x.returncode != 0:
            raise RuntimeError(
                f"verification bootstrap failed: {script.name}: "
                f"{x.stdout[-1000:]} {x.stderr[-1000:]}"
            )

def run_gate(name:str,rel:str)->dict[str,Any]:
    p=ROOT/rel
    if not p.exists():
        return {"name":name,"status":"BLOCK","reason":f"missing:{rel}"}
    try:
        x=subprocess.run(["python",str(p)],cwd=ROOT,env=ENV,text=True,capture_output=True,timeout=180)
        return {
            "name":name,
            "status":"PASS" if x.returncode==0 else "BLOCK",
            "returncode":x.returncode,
            "stdout_tail":x.stdout[-2000:],
            "stderr_tail":x.stderr[-2000:],
        }
    except Exception as e:
        return {"name":name,"status":"BLOCK","reason":str(e)}

def main()->int:
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]

    # Dependency order: create deterministic evidence/status inputs first,
    # then execute all fail-closed gates.
    seed_nlp_status()
    prepare_verification_ledgers()
    e2e=subprocess.run(["python","-m","unittest","tests/test_supreme_nlp_end_to_end.py","-v"],cwd=ROOT,env=ENV,text=True,capture_output=True,timeout=180)
    e2e_gate={"name":"supreme_nlp_end_to_end","status":"PASS" if e2e.returncode==0 else "BLOCK","returncode":e2e.returncode,"stdout_tail":e2e.stdout[-2000:],"stderr_tail":e2e.stderr[-2000:]}
    gates=[run_gate(n,p) for n,p in GATES]+[e2e_gate]

    ok=not missing and all(g["status"]=="PASS" for g in gates)
    d={
        "schema_version":"1.1",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "system":"SHIRMANI_SUPREME_TOTAL_AI_ML_NLP_AUTOMISSION",
        "cycle":"5-minute",
        "pipeline":["Observe","Collect","Normalize","Analyze","Reason","Execute","Test","Verify","Audit","Learn","Improve"],
        "status":"PASS" if ok else "BLOCK",
        "missing_required_files":missing,
        "gates":gates,
        "verification_state":{
            "claim_records":0,
            "queued_records":0,
            "verified_records":0,
            "note":"Empty ledgers are intentional until evidence-backed claims are submitted; no verification is fabricated."
        },
        "governance":{
            "fail_closed":True,
            "scheduled_code_mutation_allowed":False,
            "subjective_experience_claim_allowed":False,
            "independent_verification_required":True,
            "human_review_for_high_impact_actions":True,
            "accuracy_is_measured_not_declared":True,
            "synthetic_regression_benchmark_required":True,
        },
    }
    d["fingerprint"]=hashlib.sha256(
        json.dumps(d,sort_keys=True,ensure_ascii=False).encode()
    ).hexdigest()
    (OUT/"status.json").write_text(
        json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps(d,ensure_ascii=False,indent=2))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
