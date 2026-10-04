#!/usr/bin/env python3
"""Fail-closed checks for the Nishpaksh/Yatharth research framework."""
import json
from pathlib import Path

spec=json.loads(Path("docs/NISHPAKSH-YATHARTH-GOVERNANCE-RESEARCH-FRAMEWORK-2026-10-04.json").read_text(encoding="utf-8"))
matrix=json.loads(Path("docs/NISHPAKSH-COMPARATIVE-RESEARCH-MATRIX-2026-10-04.json").read_text(encoding="utf-8"))

assert spec["status"]=="AUTHOR_PROPOSED_FRAMEWORK"
assert spec["verification_status"]=="UNVERIFIED"
assert "author-reported material" in spec["author_statement_boundary"]
assert spec["verification_gate"]["outcomes"] == ["UNVERIFIED","SUPPORTED","CONTESTED","VERIFIED"]
assert "Author declaration" in spec["verification_gate"]["rule"]
assert len(spec["system_layers"]) >= 4
assert len(spec["research_questions"]) >= 4
assert len(matrix["comparisons"]) >= 5
assert "does not pre-assign superiority" in matrix["policy"]

print(f"Nishpaksh framework: PASS ({len(spec['core_principles'])} principles, {len(matrix['comparisons'])} comparison targets)")
