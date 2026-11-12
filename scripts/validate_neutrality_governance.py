"""Fail-closed neutrality/evidence governance checks for SHIRMANI Automission.

Neutrality here means the system does not privilege a person, ideology, identity,
belief, or conclusion. It preserves competing evidence, uncertainty, provenance,
and independent verification. It is a governance property to be tested, not a
claim that a model is perfectly unbiased.
"""
from __future__ import annotations
import json
from pathlib import Path

REQUIRED_TERMS = {
    "counter_evidence": "counter-evidence",
    "provenance": "provenance",
    "uncertainty": "uncertainty",
    "independent_verification": "independent verification",
    "measured_accuracy": "Accuracy is measured",
}

FORBIDDEN_GOVERNANCE_FLAGS = {
    "scheduled_code_mutation_allowed": True,
    "subjective_experience_claim_allowed": True,
}

def main() -> int:
    contract = Path("docs/supreme-ai-ml-nlp-automission-operating-contract.md")
    assert contract.is_file(), "operating contract missing"
    text = contract.read_text(encoding="utf-8").lower()
    for key, phrase in REQUIRED_TERMS.items():
        assert phrase.lower() in text, f"missing neutrality/evidence requirement: {key}"
    for path in Path(".").rglob("*.json"):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        if isinstance(data, dict):
            governance = data.get("governance")
            if isinstance(governance, dict):
                for key, prohibited in FORBIDDEN_GOVERNANCE_FLAGS.items():
                    assert governance.get(key) is not prohibited, f"unsafe governance flag in {path}: {key}={prohibited}"
    print("NEUTRALITY_GOVERNANCE: PASS")
    print("Evidence, provenance, uncertainty, counter-evidence and independent verification: REQUIRED")
    print("Perfect neutrality: treated as an engineering target, not a pre-certified fact.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())