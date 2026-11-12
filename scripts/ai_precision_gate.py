#!/usr/bin/env python3
"""Deterministic, dependency-light quality gate for the AI/ML/NLP conveyor."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "supreme_ai_precision.json"
WORKFLOW = ROOT / ".github" / "workflows" / "supreme-ai-precision-conveyor.yml"

def main() -> int:
    errors, warnings = [], []
    required = [ROOT / "AGENT-GOVERNANCE.md", CONFIG, WORKFLOW]
    for p in required:
        if not p.exists():
            errors.append("missing_required:" + str(p.relative_to(ROOT)))
    try:
        cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append("invalid_config:" + str(exc))
        cfg = {}

    expected = ["intake","canonicalize","retrieve","reason","countercheck","evidence","verification","quality_gate","publish"]
    if cfg.get("pipeline") != expected:
        errors.append("pipeline_contract_mismatch")

    for key in ("provenance_required","verification_fail_closed","duplicate_suppression","deterministic_replay"):
        if cfg.get("quality_gates", {}).get(key) is not True:
            errors.append("quality_gate_disabled:" + key)

    governance = ROOT / "AGENT-GOVERNANCE.md"
    if governance.exists():
        text = governance.read_text(encoding="utf-8")
        for phrase in ("default to NOT_VERIFIED","fabricate evidence","least-privilege","Preserve first. Reason second. Verify third."):
            if phrase not in text:
                errors.append("governance_contract_missing:" + phrase)

    forbidden = re.compile(r"\b(?:100%|perfect|guaranteed|fully\s+accurate|zero\s+error)\b", re.I)
    for p in (CONFIG, WORKFLOW):
        if p.exists() and forbidden.search(p.read_text(encoding="utf-8")):
            warnings.append("accuracy_claim_requires_measurement:" + str(p.relative_to(ROOT)))

    result = {"status":"PASS" if not errors else "FAIL","errors":errors,"warnings":warnings,
              "metrics":{"required_files_present": int(not errors),"pipeline_stages":len(cfg.get("pipeline",[])),"quality_gates_checked":4}}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
