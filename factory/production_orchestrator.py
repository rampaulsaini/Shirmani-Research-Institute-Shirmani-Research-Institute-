#!/usr/bin/env python3
"""Multi-layer production orchestrator: production first, verification downstream."""
from __future__ import annotations
import json, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
OUT.mkdir(exist_ok=True)
STAMP = lambda: datetime.now(timezone.utc).isoformat()

LANES = [
    ("source-and-federation", "factory/build_factory.py"),
    ("product-generation", "factory/generate_products.py"),
    ("multilingual-production", "factory/multilingual.py"),
    ("research-evidence-production", "factory/research_evidence_graph.py"),
    ("quality-production", "factory/quality_control.py"),
    ("publication-indexing", "factory/publish_index.py"),
    ("factory-reporting", "factory/run_report.py"),
]

def run_lane(name: str, script: str) -> dict:
    started = STAMP(); t0 = time.time()
    p = subprocess.run([sys.executable, script], cwd=ROOT, text=True,
                       capture_output=True, check=False)
    return {
        "lane": name, "script": script,
        "status": "SUCCEEDED" if p.returncode == 0 else "FAILED",
        "returncode": p.returncode, "started_at": started, "finished_at": STAMP(),
        "duration_seconds": round(time.time() - t0, 3),
        "stdout_tail": p.stdout[-2000:], "stderr_tail": p.stderr[-2000:],
    }

def count_lines(path: Path) -> int:
    if not path.exists(): return 0
    with path.open(encoding="utf-8", errors="ignore") as f:
        return sum(1 for x in f if x.strip())

def main() -> int:
    results = [run_lane(name, script) for name, script in LANES]
    generated = {
        "generated/ai-output.jsonl": count_lines(OUT / "ai-output.jsonl"),
        "generated/audio-prompts.jsonl": count_lines(OUT / "audio-prompts.jsonl"),
        "generated/verse-corpus.jsonl": count_lines(OUT / "verse-corpus.jsonl"),
        "generated/source-units.jsonl": count_lines(OUT / "source-units.jsonl"),
        "generated/research-queue.jsonl": count_lines(OUT / "research-queue.jsonl"),
        "generated/product-queue.jsonl": count_lines(OUT / "product-queue.jsonl"),
    }
    status = {
        "schema_version": 1, "generated_at": STAMP(),
        "mode": "MULTI_LAYER_PRODUCTION",
        "priority": "production-first; verification-downstream",
        "orchestration": "multi-level / multi-lane / deterministic bounded fan-out",
        "quantum_label": "quantum-inspired orchestration only; no quantum hardware claim",
        "lanes": results, "production_outputs": generated,
        "lane_count": len(LANES),
        "successful_lanes": sum(x["status"] == "SUCCEEDED" for x in results),
        "failed_lanes": sum(x["status"] == "FAILED" for x in results),
        "verification_note": "Verification is a downstream state for produced artifacts; this cycle does not treat verification as the production objective.",
        "truth_policy": "Generated material remains draft/unverified unless an explicit evidence and verification state says otherwise.",
    }
    (OUT / "production-cycle.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))
    return 0 if status["failed_lanes"] == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
