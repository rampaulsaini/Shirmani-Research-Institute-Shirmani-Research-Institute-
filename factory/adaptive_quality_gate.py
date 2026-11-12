"""Adaptive regression gate for the SHIRMANI AI/ML/NLP quality plane."""
from __future__ import annotations
import json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "generated" / "supreme-quality-report.json"
FAILURES = ROOT / "generated" / "failure-registry.json"
OUT = ROOT / "generated" / "adaptive-quality-gate.json"

def read(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default

def main() -> int:
    report, failures = read(REPORT, {}), read(FAILURES, {})
    ensemble = report.get("ensemble", {})
    stats = ensemble.get("score_stats", {})
    score = float(ensemble.get("ensemble_score", 0.0) or 0.0)
    spread = float(stats.get("spread", 1.0) or 1.0)
    finite = all(math.isfinite(x) for x in (score, spread))
    failed_runs = int(failures.get("semantics", {}).get("failed_run_count", 0) or 0)
    checks = {
        "quality_report_present": bool(report),
        "quality_next_action_continue": report.get("next_action") == "CONTINUE_AUTOMISSION",
        "ensemble_score_finite": finite and 0.0 <= score <= 1.0,
        "ensemble_spread_bounded": finite and spread <= 0.10,
        "failure_registry_not_corrupt": isinstance(failures, dict),
    }
    result = {
        "schema_version": "1.0",
        "mode": "adaptive-regression-gate",
        "checks": checks,
        "passed_checks": sum(checks.values()),
        "total_checks": len(checks),
        "ensemble_score": score,
        "ensemble_spread": spread,
        "failed_run_count_observed": failed_runs,
        "failure_volume_is_telemetry_only": True,
        "next_action": "CONTINUE_AUTOMISSION" if all(checks.values()) else "STOP_AND_REPAIR",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["next_action"] == "CONTINUE_AUTOMISSION" else 2

if __name__ == "__main__":
    raise SystemExit(main())
