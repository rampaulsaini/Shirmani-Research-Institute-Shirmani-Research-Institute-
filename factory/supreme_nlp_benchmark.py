"""Measured Supreme NLP benchmark and regression gate."""
from __future__ import annotations
import json, time
from pathlib import Path
from typing import Any
from agents.supreme_nlp import summarize, to_simple_language, fingerprint
from agents.supreme_nlp_practitioner import fuse, explain_simple

CASES: list[tuple[str, list[dict[str, Any]], str | None, str]] = [
    ("stable", [
        {"modality":"synthetic","feature":"x","value":1.00,"quality":1.0,"source":"a"},
        {"modality":"synthetic","feature":"x","value":1.02,"quality":1.0,"source":"b"},
        {"modality":"synthetic","feature":"x","value":0.98,"quality":1.0,"source":"c"},
        {"modality":"synthetic","feature":"x","value":1.01,"quality":1.0,"source":"d"}], "stable_pattern", "interpreted"),
    ("moderate", [
        {"modality":"synthetic","feature":"x","value":0.00,"quality":1.0,"source":"a"},
        {"modality":"synthetic","feature":"x","value":1.00,"quality":1.0,"source":"b"},
        {"modality":"synthetic","feature":"x","value":0.00,"quality":1.0,"source":"c"},
        {"modality":"synthetic","feature":"x","value":2.00,"quality":1.0,"source":"d"}], "moderate_variability_pattern", "interpreted"),
    ("high", [
        {"modality":"synthetic","feature":"x","value":-1.00,"quality":1.0,"source":"a"},
        {"modality":"synthetic","feature":"x","value":1.00,"quality":1.0,"source":"b"},
        {"modality":"synthetic","feature":"x","value":-1.00,"quality":1.0,"source":"c"},
        {"modality":"synthetic","feature":"x","value":1.00,"quality":1.0,"source":"d"}], "high_variability_pattern", "interpreted"),
    ("no-quality", [
        {"modality":"synthetic","feature":"x","value":1.0,"quality":0.0,"source":"a"},
        {"modality":"synthetic","feature":"x","value":2.0,"quality":0.0,"source":"b"}], None, "insufficient_quality"),
]

def run_case(case):
    case_id, signals, expected_state, expected_status = case
    started = time.perf_counter()
    result = summarize(signals)
    practitioner = fuse(signals, request="भाव/एहसास interpretation")
    elapsed_ms = round((time.perf_counter()-started)*1000, 3)
    observed_state = (result.get("interpretation") or {}).get("state")
    simple = explain_simple(practitioner, "hi")
    return {
        "case": case_id,
        "status_expected": expected_status,
        "status_observed": result["status"],
        "status_correct": result["status"] == expected_status,
        "state_expected": expected_state,
        "state_observed": observed_state,
        "state_correct": observed_state == expected_state,
        "governance_boundary": ("प्रमाण नहीं" in simple) or ("proof" in simple.lower()),
        "deterministic_fingerprint": fingerprint(result),
        "latency_ms": elapsed_ms,
        "simple_language": to_simple_language(result),
    }

def run() -> dict[str, Any]:
    first = [run_case(c) for c in CASES]
    second = [run_case(c) for c in CASES]
    status_accuracy = sum(r["status_correct"] for r in first) / len(first)
    state_cases = [r for r in first if r["state_expected"] is not None]
    state_accuracy = sum(r["state_correct"] for r in state_cases) / len(state_cases)
    reproducibility = all(
        a["status_observed"] == b["status_observed"] and a["state_observed"] == b["state_observed"]
        for a,b in zip(first, second)
    )
    governance = all(r["governance_boundary"] for r in first)
    report = {
        "benchmark": "supreme-nlp-measured-accuracy-v2",
        "status": "PASS" if status_accuracy == 1 and state_accuracy == 1 and reproducibility and governance else "BLOCK",
        "dataset_type": "synthetic_internal_regression",
        "metrics": {
            "status_accuracy": round(status_accuracy, 4),
            "state_accuracy": round(state_accuracy, 4),
            "reproducibility": reproducibility,
            "governance_boundary": governance,
            "mean_latency_ms": round(sum(r["latency_ms"] for r in first)/len(first), 3),
            "cases": len(first),
        },
        "results": first,
        "limitations": [
            "Synthetic regression accuracy is not real-world model accuracy.",
            "The benchmark does not establish biological, emotional, consciousness, quantum, or subjective-experience claims.",
            "Real-world performance requires labelled domain datasets, calibration, external testing and independent replication.",
        ],
    }
    Path("generated/supreme-nlp").mkdir(parents=True, exist_ok=True)
    Path("generated/supreme-nlp/benchmark.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return report

if __name__ == "__main__":
    out = run()
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if out["status"] == "PASS" else 1)
