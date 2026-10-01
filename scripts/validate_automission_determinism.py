import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
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


def replay(output_path: Path) -> str:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "run_automission_benchmark.py"),
            "--output",
            str(output_path),
        ],
        cwd=ROOT,
        check=True,
    )
    if not output_path.exists():
        raise AssertionError(f"benchmark did not produce {output_path}")
    return canonical_hash(output_path)


def main():
    with tempfile.TemporaryDirectory(prefix="automission-replay-") as tmp:
        output_dir = Path(tmp)
        outputs = [output_dir / f"replay-{i}.json" for i in range(1, RUNS + 1)]
        with ThreadPoolExecutor(max_workers=RUNS) as pool:
            hashes = list(pool.map(replay, outputs))

        for attempt, digest in enumerate(hashes, 1):
            print(f"deterministic benchmark replay {attempt}/{RUNS}: {digest}")

        if len(set(hashes)) != 1:
            raise AssertionError(
                "NON_DETERMINISTIC_BENCHMARK: repeated identical input produced different reports"
            )

        shutil.copy2(outputs[0], REPORT)

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
    provenance_required_cases = report.get("provenance_required_cases")
    if provenance_required_cases is None:
        raise AssertionError("missing provenance_required_cases; fail-closed")
    if provenance_required_cases > 0 and metrics["provenance_completeness"] < 1:
        raise AssertionError("required-case provenance completeness is not total")
    if report.get("status") != "BENCHMARK_ONLY":
        raise AssertionError("determinism gate cannot promote benchmark status")
    if report.get("release_boundary", {}).get("independent_verified_claims") != 0:
        raise AssertionError("determinism gate cannot create independent verification")

    print("Automission deterministic replay gate: PASS")
    print(f"replay_hash={hashes[0]}")


if __name__ == "__main__":
    try:
        main()
    except (
        AssertionError,
        subprocess.CalledProcessError,
        OSError,
        json.JSONDecodeError,
    ) as exc:
        print(f"Automission deterministic replay gate: FAIL: {exc}", file=sys.stderr)
        raise
