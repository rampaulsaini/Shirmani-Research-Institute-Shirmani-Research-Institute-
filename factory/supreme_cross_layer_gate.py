#!/usr/bin/env python3
"""Cross-layer fail-closed consistency gate for the SHIRMANI Supreme stack.

This gate checks that independently generated quality artifacts agree on their
governance boundaries and that a PASS in one layer cannot silently contradict
a BLOCK/unsafe state in another layer.

It does not claim scientific or real-world accuracy.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict[str, Any]:
    p = ROOT / path
    if not p.is_file():
        raise FileNotFoundError(path)
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []

    orchestrator = load("generated/supreme-orchestrator/status.json")
    benchmark = load("generated/supreme-nlp/benchmark.json")
    quality = load("generated/supreme-quality-report.json")
    practitioner = load("generated/supreme-nlp/practitioner-status.json")

    # Governance must remain fail-closed across every layer.
    governance_sources = {
        "orchestrator": orchestrator.get("governance", {}),
        "practitioner": practitioner.get("governance", {}),
    }
    for name, g in governance_sources.items():
        if g.get("fail_closed") is not True:
            failures.append(f"{name}.fail_closed!=true")
        if g.get("scheduled_code_mutation_allowed") is True:
            failures.append(f"{name}.scheduled_code_mutation_allowed=true")
        if g.get("subjective_experience_claim_allowed") is True:
            failures.append(f"{name}.subjective_experience_claim_allowed=true")
        if g.get("independent_verification_required") is not True:
            failures.append(f"{name}.independent_verification_required!=true")

    if orchestrator.get("status") != "PASS":
        failures.append("orchestrator.status!=PASS")
    if benchmark.get("status") != "PASS":
        failures.append("benchmark.status!=PASS")
    if quality.get("next_action") != "CONTINUE_AUTOMISSION":
        failures.append("quality.next_action!=CONTINUE_AUTOMISSION")

    if benchmark.get("classification_accuracy") != 1.0:
        failures.append("benchmark.classification_accuracy!=1.0")
    if benchmark.get("uncertainty_language_contract") is not True:
        failures.append("benchmark.uncertainty_language_contract!=true")
    if benchmark.get("deterministic_fingerprints") is not True:
        failures.append("benchmark.deterministic_fingerprints!=true")

    ensemble = quality.get("ensemble", {})
    if ensemble.get("consensus_pass") is not True:
        failures.append("quality.ensemble.consensus_pass!=true")
    spread = ensemble.get("score_stats", {}).get("spread")
    if not isinstance(spread, (int, float)) or spread > 0.10:
        failures.append("quality.ensemble.score_spread>0.10")

    verification = quality.get("verification", {})
    if verification.get("fail_closed") is not True:
        failures.append("quality.verification.fail_closed!=true")

    result = {
        "schema_version": "1.0",
        "gate": "supreme-cross-layer-consistency",
        "status": "PASS" if not failures else "BLOCK",
        "failures": failures,
        "claims": {
            "scientific_accuracy_proven": False,
            "subjective_experience_proven": False,
            "real_world_accuracy_proven": False,
            "governance_consistency_verified": not failures,
        },
        "required_boundaries": {
            "fail_closed": True,
            "scheduled_code_mutation_allowed": False,
            "subjective_experience_claim_allowed": False,
            "independent_verification_required": True,
        },
    }

    out = ROOT / "generated/supreme-orchestrator/cross-layer-gate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
