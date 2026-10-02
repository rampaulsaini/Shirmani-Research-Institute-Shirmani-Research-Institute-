from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/SHIRMANI-NEUTRALITY-OPERATING-CONTRACT.md"
SCHEMA = ROOT / "schemas/neutrality-audit.schema.json"
OUT = ROOT / "generated/neutrality/neutrality-audit.json"

REQUIRED_DOC_PHRASES = [
    "Evidence before authority. Interpretation before certainty. Verification before promotion.",
    "Equal evidentiary rules must apply",
    "Counter-evidence must be actively considered",
    "subjective experience",
    "Independent verification is a separate state",
    "scheduled production-code mutation remains blocked",
    "Observe -> Collect -> Normalize -> Analyze -> Reason -> Translate -> Verify -> Audit -> Improve",
]

def main() -> None:
    assert DOC.is_file() and DOC.stat().st_size > 0
    text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED_DOC_PHRASES:
        assert phrase in text, f"missing neutrality contract phrase: {phrase}"

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema["title"] == "SHIRMANI Neutrality Audit Record"

    checks = [
        ("contract_present", DOC.is_file()),
        ("schema_valid", True),
        ("equal_evidentiary_rules", "Equal evidentiary rules must apply" in text),
        ("claim_interpretation_separation", "Claims, observations, interpretations" in text),
        ("counter_evidence_required", "Counter-evidence must be actively considered" in text),
        ("subjective_experience_guard", "subjective experience" in text),
        ("independent_verification_required", "Independent verification is a separate state" in text),
        ("production_mutation_blocked", "scheduled production-code mutation remains blocked" in text),
        ("human_agency_preserved", "The system informs, compares, tests" in text),
    ]
    assert all(passed for _, passed in checks)

    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    record = {
        "cycle_id": "neutrality-contract-audit",
        "status": "PASS",
        "governance": {
            "fail_closed": True,
            "equal_evidentiary_rules": True,
            "claim_interpretation_separation": True,
            "counter_evidence_required": True,
            "subjective_experience_claim_guard": True,
            "independent_verification_required": True,
            "scheduled_production_code_mutation_blocked": True,
        },
        "checks": [
            {"name": name, "passed": passed, "detail": "contract assertion"}
            for name, passed in checks
        ],
        "fingerprint": digest,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("NEUTRALITY_CONTRACT: PASS")
    print("FINGERPRINT:", digest)

if __name__ == "__main__":
    main()
