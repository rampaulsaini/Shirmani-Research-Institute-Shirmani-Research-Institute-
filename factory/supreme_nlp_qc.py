#!/usr/bin/env python3
"""Deterministic QC for the Supreme NLP evidence-first contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "schemas" / "supreme-nlp-contract.json"

REQUIRED_PIPELINE = {
    "ingest", "quality_control", "feature_extraction", "multimodal_fusion",
    "inference", "calibration", "evidence_binding", "plain_language_translation",
    "independent_verification", "audit",
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    pipeline = set(contract.get("required_pipeline", []))
    if pipeline != REQUIRED_PIPELINE:
        raise SystemExit("SUPREME-NLP-QC: BLOCK: incomplete pipeline contract")
    if contract.get("confidence_policy", {}).get("no_automatic_100_percent_claims") is not True:
        raise SystemExit("SUPREME-NLP-QC: BLOCK: unsafe confidence policy")
    exp = contract.get("experience_claim_policy", {})
    if exp.get("direct_subjective_experience_inference") != "prohibited_without_independent_empirical_evidence":
        raise SystemExit("SUPREME-NLP-QC: BLOCK: experience boundary missing")
    auto = contract.get("automission_policy", {})
    if auto.get("fail_closed") is not True:
        raise SystemExit("SUPREME-NLP-QC: BLOCK: Automission is not fail-closed")
    if auto.get("production_promotion") != "independent_verification_required":
        raise SystemExit("SUPREME-NLP-QC: BLOCK: promotion boundary missing")
    print("SUPREME-NLP-QC: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
