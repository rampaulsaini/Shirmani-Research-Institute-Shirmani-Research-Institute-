"""Continuous architecture and epistemic-safety audit for SHIRMANI Automission."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
CONTRACT = ROOT / "factory" / "multimodal-signal-contract.json"
REGISTRY = ROOT / "factory" / "agent-registry.json"

REQUIRED_FILES = [
    "factory/supreme_ai_ml_nlp_engine.py",
    "factory/supreme_quality_controller.py",
    "factory/verification_promotion_gate.py",
    "factory/verification_registry.py",
    "factory/verification_queue.py",
    ".github/workflows/shirmani-supreme-ai-ml-nlp-quality.yml",
    ".github/workflows/shirmani-multi-automation-supervisor.yml",
    ".github/workflows/shirmani-inter-repository-automission.yml",
]

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    failures = []
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        failures.append({"check": "required_architecture", "missing": missing})

    try:
        contract = load(CONTRACT)
        if contract.get("schema_version") != "1.0":
            failures.append({"check": "signal_contract_version"})
        if len(contract.get("signal_modalities", [])) < 5:
            failures.append({"check": "signal_modalities"})
        required = set(contract.get("required_fields", []))
        if not {"signal_id", "timestamp", "modality", "measurement", "model_version",
                "interpretation", "confidence", "evidence", "uncertainty"}.issubset(required):
            failures.append({"check": "signal_required_fields"})
        if not contract.get("language_output", {}).get("must_separate_observation_from_inference"):
            failures.append({"check": "epistemic_separation"})
    except Exception as exc:
        failures.append({"check": "signal_contract_parse", "error": str(exc)})

    try:
        registry = load(REGISTRY)
        policy = registry.get("policy", {})
        required_policy = {
            "source_first": True,
            "generated_output_is_not_source": True,
            "research_requires_independent_verification": True,
            "no_claim_of_scientific_validation": True,
            "human_agency_preserved": True,
            "provenance_required": True,
        }
        for key, expected in required_policy.items():
            if policy.get(key) is not expected:
                failures.append({"check": "agent_governance", "field": key})
    except Exception as exc:
        failures.append({"check": "agent_registry_parse", "error": str(exc)})

    report = {
        "schema_version": "1.0",
        "mode": "continuous-improvement-architecture-audit",
        "required_components": len(REQUIRED_FILES),
        "missing_components": len(missing),
        "failures": failures,
        "next_action": "CONTINUE_AUTOMISSION" if not failures else "STOP_AND_REPAIR",
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "continuous-improvement-audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))
    if failures:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
