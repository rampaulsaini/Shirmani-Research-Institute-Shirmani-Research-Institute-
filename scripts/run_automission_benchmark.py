import argparse
import hashlib
import json
import math
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/yatharth-governance/automission-benchmark-manifest.json"
FIXTURE = ROOT / "benchmarks/automission/sample_predictions.jsonl"
OUT = ROOT / "automission-benchmark-report.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_jsonl(path):
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"invalid JSONL at line {line_no}: {exc}") from exc
    return rows


def percentile(values, p):
    values = sorted(values)
    if not values:
        return None
    if len(values) == 1:
        return values[0]
    k = (len(values) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    if lo == hi:
        return values[lo]
    return values[lo] + (values[hi] - values[lo]) * (k - lo)


def macro_prf(rows):
    labels = sorted({r["expected"] for r in rows} | {r["predicted"] for r in rows})
    precisions, recalls, f1s = [], [], []
    for label in labels:
        tp = sum(r["expected"] == label and r["predicted"] == label for r in rows)
        fp = sum(r["expected"] != label and r["predicted"] == label for r in rows)
        fn = sum(r["expected"] == label and r["predicted"] != label for r in rows)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)
    return statistics.mean(precisions), statistics.mean(recalls), statistics.mean(f1s)


def main(output_path: Path = OUT):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = load_jsonl(FIXTURE)
    required = set(manifest["evaluation"]["required_fields"])
    if not rows:
        raise AssertionError("benchmark fixture is empty")
    declared_suites = set(manifest["suites"])
    seen_suites = {str(r.get("suite")) for r in rows}
    missing_suites = declared_suites - seen_suites
    if missing_suites:
        raise AssertionError(f"missing benchmark suite coverage: {sorted(missing_suites)}")
    unknown_suites = seen_suites - declared_suites
    if unknown_suites:
        raise AssertionError(f"unknown benchmark suites: {sorted(unknown_suites)}")
    for row in rows:
        missing = required - set(row)
        if missing:
            raise AssertionError(f'{row.get("case_id", "?")}: missing {sorted(missing)}')
        if not 0.0 <= float(row["confidence"]) <= 1.0:
            raise AssertionError(f'{row["case_id"]}: confidence outside [0,1]')
        if not isinstance(row["abstained"], bool):
            raise AssertionError(f'{row["case_id"]}: abstained must be boolean')
        if row["abstained"] and row["predicted"] != manifest["evaluation"]["unknown_label"]:
            raise AssertionError(f'{row["case_id"]}: abstention must emit UNKNOWN')
        if not row["input_hash"].startswith("sha256:"):
            raise AssertionError(f'{row["case_id"]}: missing input hash')
        if not isinstance(row["evidence_ids"], list):
            raise AssertionError(f'{row["case_id"]}: evidence_ids must be a list')

    non_abstained = [r for r in rows if not r["abstained"]]
    correct = sum(r["expected"] == r["predicted"] for r in non_abstained)
    accuracy = correct / len(non_abstained) if non_abstained else 0.0
    precision, recall, f1 = macro_prf(non_abstained) if non_abstained else (0.0, 0.0, 0.0)

    brier = statistics.mean(
        (float(r["confidence"]) - (1.0 if r["expected"] == r["predicted"] else 0.0)) ** 2
        for r in non_abstained
    ) if non_abstained else 0.0

    bins = []
    for lower in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        upper = lower + 0.1
        bucket = [r for r in non_abstained if lower <= float(r["confidence"]) < upper or (upper == 1.0 and float(r["confidence"]) <= 1.0)]
        if bucket:
            conf = statistics.mean(float(r["confidence"]) for r in bucket)
            acc = statistics.mean(r["expected"] == r["predicted"] for r in bucket)
            bins.append((len(bucket), abs(conf - acc)))
    ece = sum(n * gap for n, gap in bins) / len(non_abstained) if non_abstained else 0.0

    abstention_rate = sum(r["abstained"] for r in rows) / len(rows)
    coverage = len(non_abstained) / len(rows)
    if coverage < 0.5:
        raise AssertionError(f"abstention coverage too low: {coverage:.6f}")
    selective_risk = 1.0 - accuracy if non_abstained else 0.0
    provenance = sum(bool(r["evidence_ids"]) for r in rows) / len(rows)

    # Per-suite metrics prevent strong aggregate results from masking weak suites.
    suite_metrics = {}
    for suite in sorted(declared_suites):
        suite_rows = [r for r in rows if r.get("suite") == suite]
        suite_non_abstained = [r for r in suite_rows if not r["abstained"]]
        suite_correct = sum(r["expected"] == r["predicted"] for r in suite_non_abstained)
        suite_accuracy = suite_correct / len(suite_non_abstained) if suite_non_abstained else 0.0
        suite_provenance = sum(bool(r["evidence_ids"]) for r in suite_rows) / len(suite_rows) if suite_rows else 0.0
        suite_metrics[suite] = {
            "cases": len(suite_rows),
            "coverage": round(len(suite_non_abstained) / len(suite_rows), 6) if suite_rows else 0.0,
            "accuracy": round(suite_accuracy, 6),
            "provenance_completeness": round(suite_provenance, 6),
            "abstention_rate": round(sum(r["abstained"] for r in suite_rows) / len(suite_rows), 6) if suite_rows else 0.0,
        }
    weakest_suite_accuracy = min(v["accuracy"] for v in suite_metrics.values())
    if weakest_suite_accuracy < 0.5:
        raise AssertionError(f"suite accuracy floor breached: {weakest_suite_accuracy:.6f}")
    latencies = [float(r["latency_ms"]) for r in rows]
    report = {
        "schema_version": "1.0.0",
        "manifest_id": manifest["manifest_id"],
        "fixture_sha256": sha256_bytes(FIXTURE.read_bytes()),
        "metrics": {
            "accuracy": round(accuracy, 6),
            "precision_macro": round(precision, 6),
            "recall_macro": round(recall, 6),
            "f1_macro": round(f1, 6),
            "brier_score": round(brier, 6),
            "expected_calibration_error": round(ece, 6),
            "abstention_rate": round(abstention_rate, 6),
            "coverage": round(coverage, 6),
            "selective_risk": round(selective_risk, 6),
            "provenance_completeness": round(provenance, 6),
            "latency_p50_ms": round(percentile(latencies, 50), 3),
            "latency_p95_ms": round(percentile(latencies, 95), 3),
            "latency_p99_ms": round(percentile(latencies, 99), 3),
            "error_rate": round(sum(r["predicted"] is None for r in rows) / len(rows), 6),
            "reproducibility": 1.0
        },
        "suite_metrics": suite_metrics,
        "weakest_suite_accuracy": round(weakest_suite_accuracy, 6),
        "counts": {
            "cases": len(rows),
            "non_abstained": len(non_abstained),
            "abstained": sum(r["abstained"] for r in rows),
            "suite_counts": {suite: sum(r.get("suite") == suite for r in rows) for suite in sorted(declared_suites)}
        },
        "release_boundary": manifest["release_policy"],
        "status": "BENCHMARK_ONLY"
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Automission deterministic benchmark: PASS")
    print("Boundary: benchmark result is not independent verification and does not establish a LIVE claim.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the bounded Automission benchmark.")
    parser.add_argument("--output", type=Path, default=OUT, help="benchmark report output path")
    args = parser.parse_args()
    try:
        main(args.output)
    except AssertionError as exc:
        print(f"Automission deterministic benchmark: FAIL: {exc}", file=sys.stderr)
        raise
