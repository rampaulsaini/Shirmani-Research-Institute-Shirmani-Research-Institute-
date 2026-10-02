#!/usr/bin/env python3
"""Repository-level architecture contract for Supreme AI/ML/NLP Automission."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
WF=ROOT/".github"/"workflows"
REQUIRED_WORKFLOWS={
 "supreme-total-orchestrator.yml","supreme-nlp-automission.yml",
 "supreme-nlp-practitioner.yml","supreme-ai-ml-nlp-automission-continuous-audit.yml",
 "supreme-neutrality-audit.yml",
}
def fail(msg:str)->None:
 print("ARCHITECTURE_CONTRACT: FAIL"); print(msg); raise SystemExit(1)
missing=sorted(p for p in REQUIRED_WORKFLOWS if not (WF/p).is_file())
if missing: fail("Missing required Supreme workflows: "+", ".join(missing))
for filename in sorted(REQUIRED_WORKFLOWS):
 path=WF/filename; text=path.read_text(encoding="utf-8")
 if re.search(r"(?m)^\s*-\s*cron:",text):
  if not re.search(r"(?m)^\s*timeout-minutes:\s*\d+",text): fail(f"{path}: no timeout-minutes")
  if not re.search(r"(?m)^permissions:\s*$",text): fail(f"{path}: no permissions block")
  if not re.search(r"(?m)^\s*contents:\s*read\s*$",text): fail(f"{path}: contents must be read-only")
  if not re.search(r"(?m)^concurrency:\s*$",text): fail(f"{path}: no concurrency policy")
practitioner=(WF/"supreme-nlp-practitioner.yml").read_text(encoding="utf-8")
if "Governance assertions" not in practitioner: fail("NLP practitioner governance assertions missing")
if not (ROOT/"scripts"/"validate_neutrality_contract.py").is_file(): fail("neutrality validator missing")
if not (ROOT/"schemas"/"neutrality-evidence-record.schema.json").is_file(): fail("neutrality schema missing")
print("ARCHITECTURE_CONTRACT: PASS")
print(f"Checked required Supreme workflows: {len(REQUIRED_WORKFLOWS)}")
print("Scheduled automation: bounded + read-only + concurrency-gated")
print("Neutrality/evidence contract: required")
