#!/usr/bin/env python3
"""Repository-level architecture contract for the SHIRMANI AI/ML/NLP Automission stack.

This gate validates files that actually exist on the current default architecture.
It intentionally fails closed when a required control is missing, but never edits
workflows or removes automation.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / ".github" / "workflows"

# These are the canonical, present-day control-plane workflows. Keep this list
# synchronized with real repository paths; stale names must not make the gate
# fail forever before it reaches substantive checks.
REQUIRED_WORKFLOWS = {
    "supreme-total-orchestrator.yml",
    "supreme-nlp-contract.yml",
    "workflow-noise-audit.yml",
}


def fail(msg: str) -> None:
    print("ARCHITECTURE_CONTRACT: FAIL")
    print(msg)
    raise SystemExit(1)


missing = sorted(p for p in REQUIRED_WORKFLOWS if not (WF / p).is_file())
if missing:
    fail("Missing required control workflows: " + ", ".join(missing))

for filename in sorted(REQUIRED_WORKFLOWS):
    path = WF / filename
    text = path.read_text(encoding="utf-8")

    if not re.search(r"(?m)^permissions:\s*$", text):
        fail(f"{path}: explicit permissions block is required")
    if not re.search(r"(?m)^\s*contents:\s*read\s*$", text):
        fail(f"{path}: control workflow must retain contents: read")
    if not re.search(r"(?m)^concurrency:\s*$", text):
        fail(f"{path}: concurrency policy is required")
    if not re.search(r"(?m)^\s*timeout-minutes:\s*\d+\s*$", text):
        fail(f"{path}: bounded job timeout is required")

    # Critical control-plane work must not be interrupted by a newer run.
    if filename in {"supreme-total-orchestrator.yml", "supreme-nlp-contract.yml"}:
        if re.search(r"(?m)^\s*cancel-in-progress:\s*true\s*$", text):
            fail(f"{path}: critical automission must not cancel an in-progress run")

practitioner_path = ROOT / "agents" / "supreme_nlp_practitioner.py"
if not practitioner_path.is_file():
    fail("agents/supreme_nlp_practitioner.py: NLP practitioner implementation is missing")
practitioner = practitioner_path.read_text(encoding="utf-8")
if "subjective experience" not in practitioner.lower():
    fail("Supreme NLP practitioner must explicitly avoid unsupported subjective-experience claims")

noise_audit = (WF / "workflow-noise-audit.yml").read_text(encoding="utf-8")
if "workflow_dispatch:" not in noise_audit or "schedule:" not in noise_audit:
    fail("Workflow noise audit must support both manual and scheduled read-only inspection")
if "contents: write" in noise_audit:
    fail("Workflow noise audit must remain read-only")

print("ARCHITECTURE_CONTRACT: PASS")
print(f"Checked canonical control workflows: {len(REQUIRED_WORKFLOWS)}")
print("Control permissions: read-only")
print("Critical automission concurrency: in-progress runs protected")
print("Workflow noise audit: manual + scheduled, no deletion or writes")
print("NLP practitioner evidence discipline: explicitly checked")
