import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"automission-benchmark-report.json"
MANIFEST=ROOT/"docs/yatharth-governance/automission-benchmark-manifest.json"

def main():
    r=json.loads(REPORT.read_text(encoding="utf-8"))
    m=json.loads(MANIFEST.read_text(encoding="utf-8"))
    required={"accuracy","precision_macro","recall_macro","f1_macro","brier_score","expected_calibration_error",
              "abstention_rate","selective_risk","provenance_completeness","reproducibility",
              "latency_p50_ms","latency_p95_ms","latency_p99_ms","error_rate"}
    metrics=r.get("metrics",{})
    missing=required-set(metrics)
    assert not missing, f"missing metrics: {sorted(missing)}"
    assert r["manifest_id"]==m["manifest_id"]
    assert r["fixture_sha256"].startswith("sha256:") or len(r["fixture_sha256"])==64
    assert r["status"]=="BENCHMARK_ONLY"
    assert r["release_boundary"]["independent_verified_claims"]==0
    assert r["release_boundary"]["live_claim"] is False
    print("Benchmark report contract: PASS")

if __name__=="__main__":
    main()
