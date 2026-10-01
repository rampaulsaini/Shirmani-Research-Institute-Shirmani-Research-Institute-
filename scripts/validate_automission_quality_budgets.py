import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/yatharth-governance/supreme-automission-contract.json"
REPORT = ROOT / "automission-benchmark-report.json"

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    budgets = contract["performance"]["quality_budgets"]
    metrics = report["metrics"]
    cases = report.get("counts", {}).get("cases", 0)
    calibration_target = budgets.get("target_expected_calibration_error", budgets["max_expected_calibration_error"])
    strict_calibration = cases >= 20
    routing = report.get("routing", {})
    route_counts = routing.get("route_counts", {})
    checks = {
        "p95_latency": metrics["latency_p95_ms"] <= budgets["max_p95_latency_ms"],
        "p99_latency": metrics["latency_p99_ms"] <= budgets["max_p99_latency_ms"],
        "error_rate": metrics["error_rate"] <= budgets["max_error_rate"],
        "calibration_error": metrics["expected_calibration_error"] <= budgets["max_expected_calibration_error"],
        "strict_calibration_target_when_sample_sufficient": (
            not strict_calibration or metrics["expected_calibration_error"] <= calibration_target
        ),
        "selective_risk": metrics["selective_risk"] <= budgets["max_selective_risk"],
        "provenance": metrics["provenance_completeness"] >= budgets["min_provenance_completeness"],
        "coverage": metrics["coverage"] >= budgets["min_coverage"],
        "status_boundary": report.get("status") == "BENCHMARK_ONLY",
        "independent_verified_claims": report.get("release_boundary", {}).get("independent_verified_claims") == 0,
        "adaptive_routing_present": routing.get("policy") == "deterministic_first_then_escalate_on_uncertainty_or_missing_evidence",
        "routing_counts_consistent": sum(route_counts.values()) == cases,
    }
    print(json.dumps({"budgets": budgets, "metrics": metrics, "checks": checks}, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise AssertionError("QUALITY_BUDGET_BREACH: fail-closed; output must abstain and require review")
    print("Automission quality budget gate: PASS")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Automission quality budget gate: FAIL: {exc}", file=sys.stderr)
        raise
