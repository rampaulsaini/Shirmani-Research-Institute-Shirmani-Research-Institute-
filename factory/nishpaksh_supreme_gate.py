"""Deterministic integrity gate for Nishpaksh Supreme NLP outputs.

This gate validates architecture-level invariants. It does not claim that
a model is scientifically correct merely because the gate passes.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "nishpaksh-supreme-automission-v2.md"
SCHEMA = ROOT / "schemas" / "nishpaksh-nlp-result.schema.json"
GOV = ROOT / "schemas" / "agent-governance.json"

REQUIRED_CONTRACT_MARKERS = [
    "evidence-first",
    "fail-closed",
    "counter-evidence",
    "independent verification",
    "FAIL_CLOSED",
    "subjective feeling",
    "Supreme accuracy",
]

def main() -> None:
    contract = CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in REQUIRED_CONTRACT_MARKERS if x not in contract]
    if missing:
        raise SystemExit("Contract gate failed; missing: " + ", ".join(missing))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    expected = {
        "event_id", "status", "claim_type", "measured_signal",
        "model_inference", "interpretation", "confidence",
        "provenance", "counter_evidence", "verification"
    }
    if required != expected:
        raise SystemExit("NLP result schema required fields are incomplete")

    governance = json.loads(GOV.read_text(encoding="utf-8"))
    hard_requirements = {
        "fail_closed": True,
        "provenance_required_for_claims": True,
        "fabrication_prohibited": True,
    }
    for key, value in hard_requirements.items():
        if governance.get(key) is not value:
            raise SystemExit(f"Governance gate failed: {key} must be {value}")

    print("NISHPAKSH SUPREME NLP GATE: PASS")
    print("Architecture integrity verified; scientific truth is NOT inferred from this gate.")

if __name__ == "__main__":
    main()
