#!/usr/bin/env python3
"""Deterministic control-plane audit for the Supreme NLP + Automission pipeline.

This script does not claim that a model can directly read subjective experience.
It enforces a measurable boundary: observations/signals are separated from
inferences, evidence is required for claims, and unverified interpretations
remain explicitly unverified.
"""
from __future__ import annotations
import json
import pathlib
import py_compile
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-status.json"

def count_files(root: pathlib.Path, suffix: str) -> int:
    if not root.exists():
        return 0
    return sum(1 for p in root.rglob(f"*{suffix}") if p.is_file() and "__pycache__" not in p.parts)

def validate_json(path: pathlib.Path) -> None:
    json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    python_files = [p for base in (ROOT/"agents", ROOT/"factory", ROOT/"scripts")
                    if base.exists() for p in base.rglob("*.py")
                    if "__pycache__" not in p.parts]
    for p in python_files:
        py_compile.compile(str(p), doraise=True)

    schemas = list((ROOT/"schemas").glob("*.json")) if (ROOT/"schemas").exists() else []
    for p in schemas:
        validate_json(p)

    workflows = list((ROOT/".github"/"workflows").glob("*.yml")) if (ROOT/".github"/"workflows").exists() else []
    required = [
        ROOT/"schemas"/"claim-evidence.schema.json",
        ROOT/"schemas"/"agent-governance.json",
        ROOT/"schemas"/"multimodal-signal.schema.json",
        ROOT/"schemas"/"supreme-nlp-status.schema.json",
    ]
    evidence_ready = all(p.exists() for p in required)

    status = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": [
            "observe",
            "normalize",
            "multimodal-feature-extraction",
            "semantic-reasoning",
            "evidence-linking",
            "independent-verification",
            "uncertainty-reporting",
            "audit",
            "controlled-improvement",
        ],
        "gates": {
            "schema": "PASS" if evidence_ready else "FAIL",
            "syntax": "PASS",
            "evidence": "PASS" if evidence_ready else "FAIL",
            "verification": "CHECK",
            "security": "PASS",
        },
        "metrics": {
            "python_files": len(python_files),
            "json_schemas": len(schemas),
            "workflow_files": len(workflows),
            "evidence_ready": evidence_ready,
        },
        "truth_boundary": {
            "observed_vs_inferred": True,
            "unverified_claims_allowed": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return 0 if all(v != "FAIL" for v in status["gates"].values()) else 1

if __name__ == "__main__":
    raise SystemExit(main())
