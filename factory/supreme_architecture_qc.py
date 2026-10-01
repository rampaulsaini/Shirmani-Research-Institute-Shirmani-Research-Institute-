#!/usr/bin/env python3
"""Deterministic hardening gate for the Supreme AI-ML-NLP-Automission architecture.

This gate validates architecture contracts and evidence boundaries. It does not
claim scientific truth, consciousness detection, or model accuracy by itself.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

GRAPH = ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
GOVERNANCE = ROOT / "docs/yatharth-governance/ai-control-contract.md"
CONTINUITY = ROOT / "PROJECT-CONTINUITY.md"
WORKFLOW = ROOT / ".github/workflows/omniverse-factory.yml"
STATUS = ROOT / "generated/factory-status.json"

REQUIRED_GRAPH_TERMS = [
    "Multimodal Perception",
    "Data Quality + Normalization",
    "Feature / Signal Extraction",
    "ML Models",
    "NLP: Natural Language Processing",
    "Multimodal Fusion",
    "Reasoning + Uncertainty",
    "Planner Agent",
    "Evidence Agent",
    "NLP Interpreter Agent",
    "Security Agent",
    "Verification Agent",
    "Independent Verification",
    "QC / Regression",
    "Fail Closed + Diagnose",
    "Continuous Improvement",
]

REQUIRED_LOOP = [
    "Observe", "Collect", "Normalize", "Analyze", "Reason", "Execute",
    "Test", "Verify", "Audit", "Learn", "Improve"
]

def fail(message):
    raise AssertionError(message)

def require_file(path):
    if not path.is_file() or path.stat().st_size == 0:
        fail(f"missing_or_empty:{path.relative_to(ROOT)}")

def main():
    for path in (GRAPH, GOVERNANCE, CONTINUITY, WORKFLOW, STATUS):
        require_file(path)

    graph = GRAPH.read_text(encoding="utf-8")
    governance = GOVERNANCE.read_text(encoding="utf-8")
    continuity = CONTINUITY.read_text(encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")

    missing = [term for term in REQUIRED_GRAPH_TERMS if term not in graph]
    if missing:
        fail("graph_missing:" + ",".join(missing))

    # Validate the canonical five-minute loop as one exact contract. Searching
    # each word independently is unsafe because the architecture diagram
    # legitimately mentions the same stages in other contexts.
    canonical_loop = "Observe → Collect → Normalize → Analyze → Reason → Execute → Test → Verify → Audit → Learn → Improve"
    if canonical_loop not in graph:
        fail("five_minute_loop_incomplete")
    loop_pos = [canonical_loop.find(term) for term in REQUIRED_LOOP]
    if loop_pos != sorted(loop_pos):
        fail("five_minute_loop_order_changed")

    for term in (
        "Accuracy is measured, not declared.",
        "Independent verification is distinct from preparation/QC.",
        "Human review remains required for high-impact actions.",
        "A model output is not automatically proof of subjective feeling or consciousness.",
    ):
        if term not in graph:
            fail("accuracy_boundary_missing:" + term)

    governance_lower = governance.casefold()
    for term in (
        "fabricate sources",
        "turn a prediction into fact",
        "make irreversible high-impact decisions without the required human/legal gate",
        "Human override",
        "Collect only necessary data",
    ):
        if term.casefold() not in governance_lower:
            fail("governance_boundary_missing:" + term)

    if 'cron: "*/5 * * * *"' not in workflow:
        fail("five_minute_schedule_missing")

    for step in (
        "factory/agent_governance_qc.py",
        "factory/quality_control.py",
        "factory/verification_queue_qc.py",
        "factory/verification_promotion_gate.py",
        "factory/publication_gate.py",
        "factory/continuity_manifest.py",
    ):
        if step not in workflow:
            fail("workflow_gate_missing:" + step)

    status = json.loads(STATUS.read_text(encoding="utf-8"))
    if status.get("publication", {}).get("research_is_draft") is not True:
        fail("generated_status_must_remain_research_draft")
    if status.get("publication", {}).get("verification_required") is not True:
        fail("generated_status_must_require_verification")

    # Explicitly guard against unsafe language being introduced into the
    # canonical graph. This is a text-integrity check, not a scientific test.
    unsafe = re.findall(r"\b(?:proved|proven|100% accurate|consciousness detected)\b", graph, re.I)
    if unsafe:
        fail("unsupported_certainty_language_in_graph:" + ",".join(sorted(set(unsafe))))

    result = {
        "version": 2,
        "gate": "SUPREME_AI_ML_NLP_AUTOMISSION_HARDENING",
        "status": "PASS",
        "checks": {
            "canonical_graph": "PASS",
            "five_minute_loop": "PASS",
            "evidence_boundaries": "PASS",
            "governance_boundaries": "PASS",
            "workflow_gates": "PASS",
            "draft_and_verification_status": "PASS",
            "unsupported_certainty_scan": "PASS",
        },
        "scientific_truth_claim": False,
        "independent_verification": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "BLOCK", "error": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)
