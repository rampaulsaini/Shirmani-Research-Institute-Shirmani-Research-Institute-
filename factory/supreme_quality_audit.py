"""Deterministic replay and structural audit for the SHIRMANI quality controller."""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "generated" / "supreme-quality-report.json"


def load_report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def canonical(report: dict) -> str:
    data = json.loads(json.dumps(report))
    data.pop("generated_at", None)
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate_shape(r: dict) -> None:
    required = {
        "schema_version", "mode", "checks", "passed_checks", "total_checks",
        "corpus", "verification", "worker", "ensemble", "hard_failures",
        "next_action",
    }
    missing = required - set(r)
    if missing:
        raise AssertionError(f"missing report fields: {sorted(missing)}")
    if r["mode"] != "fail-closed-deterministic-ai-ml-nlp-quality-control":
        raise AssertionError("unexpected controller mode")
    if r["next_action"] != "CONTINUE_AUTOMISSION":
        raise AssertionError("controller is not in CONTINUE_AUTOMISSION state")
    if not r["verification"].get("fail_closed"):
        raise AssertionError("verification boundary is not fail-closed")
    if not r["worker"].get("worker_observable"):
        raise AssertionError("worker is not observable")
    ensemble = r["ensemble"]
    if not ensemble.get("consensus_pass"):
        raise AssertionError("ensemble consensus failed")
    stats = ensemble.get("score_stats", {})
    if stats.get("spread", 1.0) > 0.10:
        raise AssertionError("ensemble score spread exceeds 0.10")
    for name, agent in ensemble.get("agents", {}).items():
        score = agent.get("score")
        if not isinstance(score, (int, float)) or not 0.0 <= float(score) <= 1.0:
            raise AssertionError(f"invalid score for {name}: {score!r}")


def main() -> None:
    start = time.monotonic()
    subprocess.run(
        [sys.executable, str(ROOT / "factory" / "supreme_quality_controller.py")],
        cwd=ROOT,
        check=True,
        timeout=60,
    )
    first = load_report()
    validate_shape(first)

    subprocess.run(
        [sys.executable, str(ROOT / "factory" / "supreme_quality_controller.py")],
        cwd=ROOT,
        check=True,
        timeout=60,
    )
    second = load_report()
    validate_shape(second)

    if canonical(first) != canonical(second):
        raise AssertionError("deterministic replay mismatch")

    elapsed = time.monotonic() - start
    if elapsed > 120:
        raise AssertionError(f"quality controller replay exceeded 120s: {elapsed:.3f}s")

    print("SUPREME QUALITY AUDIT: PASS")
    print(f"deterministic_replay=PASS elapsed_seconds={elapsed:.3f}")
    print(f"ensemble_score={second['ensemble']['ensemble_score']}")
    print(f"checks={second['passed_checks']}/{second['total_checks']}")


if __name__ == "__main__":
    main()
