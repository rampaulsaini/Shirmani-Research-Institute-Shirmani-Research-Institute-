import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "automission-benchmark-report.json"
RUNS = 3


def canonical_hash(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    canonical = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def main():
    hashes = []
    for attempt in range(1, RUNS + 1):
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "run_automission_benchmark.py")],
            cwd=ROOT,
            check=True,
        )
        if not REPORT.exists():
            raise AssertionError("benchmark did not produce its report")
        digest = canonical_hash(REPORT)
        hashes.append(digest)
        print(f"deterministic benchmark replay {attempt}/{RUNS}: {digest}")

    if len(set(hashes)) != 1:
        raise AssertionError(
            "NON_DETERMINISTIC_BENCHMARK: repeated identical input produced different reports"
        )

    report = json.loads(REPORT.read_text(encoding="utf-8"))
    metrics = report["metrics"]
    required_metrics = {
        "accuracy",
        "precision_macro",
        "recall_macro",
        "f1_macro",
        "brier_score",
        "expected_calibration_error",
        "coverage",
        "selective_risk",
        "provenance_completeness",
        "latency_p50_ms",
        "latency_p95_ms",
        "latency_p99_ms",
    }
    missing = required_metrics - set(metrics)
    if missing:
        raise AssertionError(f"benchmark report missing metrics: {sorted(missing)}")

    if metrics["selective_risk"] < 0 or metrics["selective_risk"] > 1:
        raise AssertionError("selective risk outside [0,1]")
    if metrics["coverage"] <= 0:
        raise AssertionError("zero useful coverage")
    if metrics["provenance_completeness"] < 1:
        raise AssertionError("provenance completeness is not total")

    print("Automission deterministic replay gate: PASS")
    print(f"replay_hash={hashes[0]}")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, subprocess.CalledProcessError, OSError, json.JSONDecodeError) as exc:
        print(f"Automission deterministic replay gate: FAIL: {exc}", file=sys.stderr)
        raise
