#!/usr/bin/env python3
"""Deterministic repository health gate for the SHIRMANI platform.

The script reports measurable repository state; it never converts an author
claim into a scientific fact and never treats workflow success as independent
verification.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
REPORT = ROOT / "generated" / "platform-health-report.json"


def run(*cmd: str) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False)
    return p.returncode, (p.stdout + p.stderr).strip()


def workflow_health() -> dict:
    files = sorted(WORKFLOWS.glob("*.y*ml"))
    names: list[str] = []
    yaml_errors: list[str] = []
    for path in files:
        try:
            import yaml  # type: ignore
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or not data.get("jobs"):
                yaml_errors.append(f"{path.relative_to(ROOT)}: missing jobs")
            name = data.get("name") if isinstance(data, dict) else None
            names.append(str(name or path.name))
        except Exception as exc:
            yaml_errors.append(f"{path.relative_to(ROOT)}: {exc}")
    duplicate_names = sorted(
        name for name, count in Counter(names).items() if count > 1
    )
    stale_triggers = sorted(p.name for p in ROOT.glob("CONTINUE-*.trigger"))
    return {
        "workflow_files": len(files),
        "duplicate_workflow_names": duplicate_names,
        "yaml_errors": yaml_errors,
        "stale_root_trigger_files": stale_triggers,
    }


def python_health() -> dict:
    code, output = run(
        sys.executable, "-m", "compileall", "-q", "agents", "factory", "scripts"
    )
    return {"compileall_pass": code == 0, "compileall_output": output[-2000:]}


def test_health() -> dict:
    code, output = run(
        sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"
    )
    return {"unit_tests_pass": code == 0, "unit_test_output": output[-5000:]}


def public_surface_health() -> dict:
    required = [
        "index.html",
        "public-identity.html",
        "platform-charter.md",
        "AGENT-GOVERNANCE.md",
        "docs/public-platform/deployment-runbook.md",
        "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    return {"required_surfaces": len(required), "missing": missing}


def main() -> int:
    workflow = workflow_health()
    py = python_health()
    tests = test_health()
    public = public_surface_health()
    checks = {
        "workflow_yaml": not workflow["yaml_errors"],
        "unique_workflow_names": not workflow["duplicate_workflow_names"],
        "no_stale_root_triggers": not workflow["stale_root_trigger_files"],
        "python_compile": py["compileall_pass"],
        "unit_tests": tests["unit_tests_pass"],
        "public_surfaces": not public["missing"],
    }
    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "deterministic-platform-health-gate",
        "claim_policy": (
            "Repository health is measured mechanically; scientific truth "
            "and perfect accuracy are not inferred."
        ),
        "checks": checks,
        "passed_checks": sum(checks.values()),
        "total_checks": len(checks),
        "workflow": workflow,
        "python": py,
        "tests": tests,
        "public_surface": public,
        "next_action": (
            "CONTINUE_AUTOMISSION" if all(checks.values()) else "STOP_AND_REPAIR"
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
