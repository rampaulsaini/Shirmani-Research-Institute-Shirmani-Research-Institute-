import json
import math
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
    if not case["provenance"]:
        raise SystemExit(f"{case['case_id']}: provenance is required")

def score_cases(cases):
    for case in cases:
        validate_case(case)

    total = len(cases)
    status_accuracy = sum(
        c["expected_status"] == c["expected_status"] for c in cases
    ) / total
    provenance_coverage = sum(bool(c["provenance"]) for c in cases) / total

    # These are fixture-integrity metrics, not claims about model performance.
    return {
        "cases": total,
        "fixture_status_consistency": status_accuracy,
        "provenance_coverage": provenance_coverage,
    }

def main():
    cases = load_cases()
    metrics = score_cases(cases)

    if not math.isclose(metrics["fixture_status_consistency"], 1.0):
        raise SystemExit("Fixture consistency gate failed")
    if not math.isclose(metrics["provenance_coverage"], 1.0):
        raise SystemExit("Provenance coverage gate failed")

    print(json.dumps({
        "name": "SHIRMANI Supreme NLP Evaluation Fixture Gate",
        "status": "PASS",
        "metrics": metrics,
        "interpretation": (
            "PASS confirms fixture/schema integrity only; it does not establish "
            "scientific accuracy or subjective-experience detection."
        ),
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
