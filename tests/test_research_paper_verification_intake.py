#!/usr/bin/env python3
"""Regression test for deterministic Research Paper verification intake."""
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run(
    ["python3", "factory/research_paper_verification_intake.py"],
    cwd=root, check=True
)
rows = [
    json.loads(x) for x in
    (root / "generated/research-paper-verification-intake.jsonl")
    .read_text(encoding="utf-8").splitlines() if x.strip()
]
assert len(rows) == 5
assert [r["task_id"] for r in rows] == sorted(r["task_id"] for r in rows)
for row in rows:
    assert row["status"] == "QUEUED_FOR_INDEPENDENT_VERIFICATION"
    assert row["verification_status"] == "UNVERIFIED"
    assert row["independent"] is True
    assert row["promotion_allowed"] is False
    assert len(row["task_hash"]) == 64
print("Research Paper verification intake: PASS (5 fail-closed tasks)")
