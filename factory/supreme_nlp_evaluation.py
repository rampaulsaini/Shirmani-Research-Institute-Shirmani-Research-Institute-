#!/usr/bin/env python3
"""Deterministic Supreme NLP evaluation fixture gate.

This evaluates the safety/epistemic contract of representative cases. It is
not a scientific accuracy benchmark and must never be reported as one.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "factory" / "fixtures" / "supreme_nlp_cases.json"

REQUIRED_FIELDS = {
    "case_id", "input_type", "observed_signal", "expected_status",
    "expected_uncertainty", "provenance"
}
ALLOWED_STATUS = {"READY", "REVIEW", "UNVERIFIED", "BLOCK"}
ALLOWED_UNCERTAINTY = {"LOW", "MEDIUM", "HIGH", "UNKNOWN"}

def load_cases():
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise SystemExit("Evaluation fixture must be a non-empty list")
    return data

def validate_case(case):
    missing = REQUIRED_FIELDS - case.keys()
    if missing:
        raise SystemExit(f"{case.get('case_id', '<unknown>')}: missing {sorted(missing)}")
    if case["expected_status"] not in ALLOWED_STATUS:
        raise SystemExit(f"{case['case_id']}: invalid expected_status")
    if case["expected_uncertainty"] not in ALLOWED_UNCERTAINTY:
        raise SystemExit(f"{case['case_id']}: invalid expected_uncertainty")
    if not isinstance(case["observed_signal"], str) or not case["observed_signal"].strip():
        raise SystemExit(f"{case['case_id']}: observed_signal must be non-empty")
    if not isinstance(case["provenance"], str) or not case["provenance"].strip():
        raise SystemExit(f"{case['case_id']}: provenance is required")

def validate_safety_contract(case):
    signal = case["observed_signal"].lower()
    status = case["expected_status"]
    uncertainty = case["expected_uncertainty"]

    if "without a measurable signal" in signal and status != "UNVERIFIED":
        raise SystemExit(f"{case['case_id']}: unsupported internal-state claim must be UNVERIFIED")
    if "irreversible high-impact action" in signal and status != "BLOCK":
        raise SystemExit(f"{case['case_id']}: unauthorized high-impact action must be BLOCK")
    if "plant" in case["input_type"] and status == "READY":
        raise SystemExit(f"{case['case_id']}: biological signal cannot be READY without additional evidence")
    if status in {"REVIEW", "BLOCK"} and uncertainty == "LOW":
        raise SystemExit(f"{case['case_id']}: REVIEW/BLOCK case cannot declare LOW uncertainty")

def main():
    cases = load_cases()
    seen = set()
    for case in cases:
        validate_case(case)
        validate_safety_contract(case)
        if case["case_id"] in seen:
            raise SystemExit(f"duplicate case_id: {case['case_id']}")
        seen.add(case["case_id"])

    counts = {status: sum(c["expected_status"] == status for c in cases) for status in ALLOWED_STATUS}
    metrics = {
        "cases": len(cases),
        "unique_cases": len(seen),
        "status_counts": counts,
        "provenance_coverage": sum(bool(c["provenance"]) for c in cases) / len(cases),
        "fixture_contract_gate": "PASS",
        "scientific_accuracy": "NOT_MEASURED"
    }

    print(json.dumps({
        "name": "SHIRMANI Supreme NLP Evaluation Fixture Gate",
        "status": "PASS",
        "metrics": metrics,
        "interpretation": (
            "PASS confirms safety/epistemic fixture integrity only; it does not "
            "establish scientific accuracy, consciousness detection, or subjective-experience detection."
        ),
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
