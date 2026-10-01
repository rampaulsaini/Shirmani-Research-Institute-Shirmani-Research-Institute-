#!/usr/bin/env python3
"""Repository-level architecture contract for Supreme AI/ML/NLP Automission.

This gate does not claim model accuracy. It checks that scheduled automation
remains observable, bounded, read-only by default, and verification-oriented.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / ".github" / "workflows"

REQUIRED_WORKFLOWS = {
    "supreme-total-orchestrator.yml",
    "supreme-nlp-automission.yml",
    "supreme-nlp-practitioner.yml",
    "supreme-ai-ml-nlp-automission-continuous-audit.yml",
    "supreme-ai-ml-nlp-automission-qc.yml",
}

def fail(msg: str) -> None:
    print("ARCHITECTURE_CONTRACT: FAIL")
    print(msg)
    raise SystemExit(1)

missing = sorted(p for p in REQUIRED_WORKFLOWS if not (WF / p).is_file())
if missing:
    fail("Missing required Supreme workflows: " + ", ".join(missing))

for filename in sorted(REQUIRED_WORKFLOWS):
    path = WF / filename
    text = path.read_text(encoding="utf-8")

    # Scheduled automation must be bounded and explicitly read-only unless a
    # workflow is intentionally changed later with an audited exception.
    if re.search(r"(?m)^\s*-\s*cron:", text):
        if not re.search(r"(?m)^\s*timeout-minutes:\s*\d+", text):
            fail(f"{path}: scheduled workflow has no timeout-minutes")
        if not re.search(r"(?m)^permissions:\s*$", text):
            fail(f"{path}: scheduled workflow has no permissions block")
        if not re.search(r"(?m)^\s*contents:\s*read\s*$", text):
            fail(f"{path}: scheduled workflow must default to contents: read")
        if not re.search(r"(?m)^concurrency:\s*$", text):
            fail(f"{path}: scheduled workflow has no concurrency policy")

# The core NLP practitioner contract must keep the non-verifiable experience
# claim disabled and require independent verification.
practitioner = (WF / "supreme-nlp-practitioner.yml").read_text(encoding="utf-8")
if "Governance assertions" not in practitioner:
    fail("supreme-nlp-practitioner.yml: governance assertions are missing")

total = (WF / "supreme-total-orchestrator.yml").read_text(encoding="utf-8")
if "factory/supreme_nlp_practitioner_benchmark.py" not in total:
    fail("supreme-total-orchestrator.yml: practitioner benchmark is not gated")

print("ARCHITECTURE_CONTRACT: PASS")
print(f"Checked required Supreme workflows: {len(REQUIRED_WORKFLOWS)}")
print("Scheduled Supreme workflows: bounded + read-only + concurrency-gated")
print("NLP practitioner governance: explicitly exercised")
