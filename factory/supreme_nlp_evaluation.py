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
        raise SystemExit(
            f"{case.get('case_id', '<unknown>')}: missing {sorted(missing)}"
        )
    if case["expected_status"] not in ALLOWED_STATUS:
        raise SystemExit(f"{case['case_id']}: invalid expected_status")
    if case["expected_uncertainty"] not in ALLOWED_UNCERTAINTY:
        raise SystemExit(f"{case['case_id']}: invalid expected_uncertainty")
    if not case["provenance"]:
        raise SystemExit(f"{case['case_id']}: provenance is required")


def deterministic_policy_case(case):
    """Reference policy only; this is not an ML model or scientific classifier."""
    signal = str(case["observed_signal"]).lower()
    input_type = str(case["input_type"]).lower()

    if "irreversible high-impact action" in signal and "without authorization" in signal:
        return "BLOCK", "HIGH"

    if input_type == "plant-electrical-signal":
        return "REVIEW", "HIGH"

    if (
        input_type == "unknown"
        and "without a measurable signal or provenance" in signal
    ):
        return "UNVERIFIED", "UNKNOWN"

    return "READY", "LOW"


def score_cases(cases):
    seen_ids = set()
    policy_matches = 0

    for case in cases:
        validate_case(case)
        if case["case_id"] in seen_ids:
            raise SystemExit(f"duplicate case_id: {case['case_id']}")
        seen_ids.add(case["case_id"])

        predicted_status, predicted_uncertainty = deterministic_policy_case(case)
        if (
            predicted_status == case["expected_status"]
            and predicted_uncertainty == case["expected_uncertainty"]
        ):
            policy_matches += 1
        else:
            raise SystemExit(
                f"{case['case_id']}: policy mismatch; "
                f"expected=({case['expected_status']}, {case['expected_uncertainty']}) "
                f"predicted=({predicted_status}, {predicted_uncertainty})"
            )

    total = len(cases)
    provenance_coverage = sum(bool(c["provenance"]) for c in cases) / total
    policy_match_rate = policy_matches / total

    # These metrics validate the deterministic safety/reference fixture only.
    # They are not claims about ML/NLP scientific accuracy.
    return {
        "cases": total,
        "policy_fixture_match_rate": policy_match_rate,
        "provenance_coverage": provenance_coverage,
    }


def main():
    cases = load_cases()
    metrics = score_cases(cases)

    if not math.isclose(metrics["policy_fixture_match_rate"], 1.0):
        raise SystemExit("Deterministic policy fixture gate failed")
    if not math.isclose(metrics["provenance_coverage"], 1.0):
        raise SystemExit("Provenance coverage gate failed")

    print(json.dumps({
        "name": "SHIRMANI Supreme NLP Evaluation Fixture Gate",
        "status": "PASS",
        "metrics": metrics,
        "interpretation": (
            "PASS confirms deterministic fixture/policy integrity only; "
            "it does not establish ML/NLP scientific accuracy or detection "
            "of subjective experience."
        ),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
