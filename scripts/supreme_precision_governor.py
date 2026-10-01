#!/usr/bin/env python3
"""Supreme Precision Governor: deterministic meta-gate for AI/ML/NLP Automission.

This is a control-plane validator, not a claim of perfect model accuracy.
It converts benchmark, calibration, provenance, abstention, latency and
release-boundary signals into explicit PASS/BLOCK/REVIEW states.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "automission-benchmark-report.json"
OUT = ROOT / "generated" / "supreme-precision-governor.json"

REQUIRED_METRICS = {
    "accuracy", "precision_macro", "recall_macro", "f1_macro",
    "brier_score", "expected_calibration_error", "coverage",
    "selective_risk", "provenance_completeness",
    "latency_p50_ms", "latency_p95_ms", "latency_p99_ms",
}

REQUIRED_CONTRACTS = [
    "docs/yatharth-governance/automission-quality-gate.json",
    "docs/yatharth-governance/automission-benchmark-manifest.json",
    "docs/yatharth-governance/supreme-automission-contract.json",
    "docs/yatharth-governance/automission-accuracy-abstention-contract.json",
    "docs/yatharth-governance/automission-performance-contract.json",
]

def canonical_sha(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()

def main():
    errors = []
    warnings = []
    if not REPORT.exists():
        raise SystemExit("benchmark report missing")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    metrics = report.get("metrics", {})
    missing = sorted(REQUIRED_METRICS - set(metrics))
    if missing:
        errors.append({"code": "MISSING_METRICS", "items": missing})

    for key in ("accuracy", "precision_macro", "recall_macro", "f1_macro", "coverage", "provenance_completeness"):
        if key in metrics and not 0.0 <= float(metrics[key]) <= 1.0:
            errors.append({"code": "METRIC_RANGE", "metric": key, "value": metrics[key]})
    for key in ("brier_score", "expected_calibration_error", "selective_risk"):
        if key in metrics and not 0.0 <= float(metrics[key]) <= 1.0:
            errors.append({"code": "METRIC_RANGE", "metric": key, "value": metrics[key]})

    suite = report.get("suite_metrics", {})
    if not suite:
        errors.append({"code": "NO_SUITE_METRICS"})
    else:
        for name, row in suite.items():
            if float(row.get("coverage", 0)) <= 0:
                errors.append({"code": "ZERO_SUITE_COVERAGE", "suite": name})
            if float(row.get("provenance_completeness", 0)) < 1:
                errors.append({"code": "INCOMPLETE_SUITE_PROVENANCE", "suite": name})
        weakest = min(float(row.get("accuracy", 0)) for row in suite.values())
        if float(report.get("weakest_suite_accuracy", -1)) != round(weakest, 6):
            errors.append({"code": "WEAKEST_SUITE_MISMATCH"})

    boundary = report.get("release_boundary", {})
    if boundary.get("independent_verified_claims") != 0:
        errors.append({"code": "VERIFICATION_BOUNDARY_BREACH"})
    if boundary.get("live_claim") is not False:
        errors.append({"code": "LIVE_CLAIM_BOUNDARY_BREACH"})
    if report.get("status") != "BENCHMARK_ONLY":
        errors.append({"code": "BENCHMARK_STATUS_ESCALATION"})

    for rel in REQUIRED_CONTRACTS:
        p = ROOT / rel
        if not p.exists():
            errors.append({"code": "MISSING_CONTRACT", "path": rel})

    # A governor must never trade safety/evidence for speed.
    if "latency_p95_ms" in metrics and float(metrics["latency_p95_ms"]) > 10000:
        warnings.append({"code": "HIGH_P95_LATENCY", "value": metrics["latency_p95_ms"]})
    if "expected_calibration_error" in metrics and float(metrics["expected_calibration_error"]) > 0.20:
        warnings.append({"code": "CALIBRATION_DRIFT", "value": metrics["expected_calibration_error"]})
    if "abstention_rate" in metrics and float(metrics["abstention_rate"]) == 0:
        warnings.append({"code": "NO_ABSTENTION_SIGNAL", "message": "Review whether uncertainty cases are represented."})

    status = "BLOCK" if errors else ("REVIEW" if warnings else "PASS")
    payload = {
        "schema_version": "1.0.0",
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "metrics_snapshot": metrics,
        "weakest_suite_accuracy": report.get("weakest_suite_accuracy"),
        "benchmark_fixture_sha256": report.get("fixture_sha256"),
        "governor_input_sha256": canonical_sha({"report": report, "contracts": REQUIRED_CONTRACTS}),
        "truth_boundary": {
            "benchmark_is_not_truth_verification": True,
            "confidence_is_not_certainty": True,
            "consensus_is_not_independent_verification": True,
            "independent_verified_claims": 0,
            "live_claim": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if status == "BLOCK":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
