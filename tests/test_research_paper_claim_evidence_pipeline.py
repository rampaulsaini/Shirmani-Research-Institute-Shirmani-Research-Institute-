#!/usr/bin/env python3
"""Regression test: Research Paper claims enter the canonical claim/evidence pipeline."""
import importlib.util
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("reasoning_pipeline", root / "factory" / "reasoning_pipeline.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

registry = json.loads((root / "generated" / "research-paper-claims.json").read_text(encoding="utf-8"))
rows = mod.research_paper_records()

expected = {f"claim:research-paper:{c['id']}" for c in registry["claims"]}
actual = {r["id"] for r in rows}
assert actual == expected
assert len(rows) == len(registry["claims"])

for row in rows:
    assert row["verification"]["status"] == "NOT_VERIFIED"
    assert row["verification"]["independent"] is False
    assert row["source_traceability"]["resolved"] is True
    assert row["evidence"][0]["kind"] == "AUTHOR_PROPOSITION"
    assert row["evidence"][0]["status"] == "NOT_VERIFIED"
    assert row["conclusion"].startswith("No independently verified")

print(f"Research Paper claim/evidence adapter: PASS ({len(rows)} claims)")
