"""Continuous AI/ML/NLP supervisor.

Measures engineering reliability, provenance, verification readiness, duplicate pressure,
schema integrity, and execution latency. It never upgrades an unverified claim to truth.
"""
from __future__ import annotations
import ast, json, re, time
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"
FACTORY = ROOT / "factory"
WORKFLOWS = ROOT / ".github" / "workflows"
OUT = ROOT / "generated" / "continuous-supervisor-status.json"

REQUIRED_AGENTS = {
    "orchestrator.py", "verification_agent.py", "qc_agent.py",
    "provenance_agent.py", "source_agent.py", "research_agent.py",
    "writing_agent.py", "publishing_agent.py",
}

def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def _compile_python():
    errors = []
    count = 0
    for root in (AGENTS, FACTORY):
        for p in root.rglob("*.py"):
            if "__pycache__" in p.parts:
                continue
            count += 1
            try:
                ast.parse(p.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"{p.relative_to(ROOT)}:{exc}")
    return count, errors

def _workflow_health():
    rows = []
    for p in WORKFLOWS.glob("*.yml"):
        text = p.read_text(encoding="utf-8", errors="strict")
        rows.append({
            "file": str(p.relative_to(ROOT)),
            "has_schedule": "schedule:" in text,
            "has_dispatch": "workflow_dispatch:" in text,
            "has_timeout": "timeout-minutes:" in text,
            "has_concurrency": "concurrency:" in text,
        })
    return rows

def _artifact_health():
    manifest = ROOT / "generated" / "agent-run" / "artifact-manifest.jsonl"
    if not manifest.exists():
        return {"records": 0, "errors": ["artifact-manifest-missing"], "source_coverage": 0.0}
    errors, ids, hashes = [], set(), set()
    with_source = 0
    records = 0
    for n, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append(f"invalid-json:{n}:{exc}")
            continue
        for k in ("artifact_id", "kind", "language", "status", "sha256", "provenance", "created_at"):
            if not r.get(k):
                errors.append(f"missing:{k}:{n}")
        if r.get("artifact_id") in ids:
            errors.append(f"duplicate-id:{r.get('artifact_id')}")
        ids.add(r.get("artifact_id"))
        hashes.add(r.get("sha256"))
        provenance = r.get("provenance")
        if r.get("source") or (isinstance(provenance, dict) and provenance.get("source")):
            with_source += 1
    return {
        "records": records,
        "errors": errors[:100],
        "source_coverage": round(with_source / records, 4) if records else 0.0,
        "unique_hashes": len(hashes),
    }

def evaluate():
    started = time.perf_counter()
    compile_count, compile_errors = _compile_python()
    missing_agents = sorted(REQUIRED_AGENTS - {p.name for p in AGENTS.glob("*.py")})
    workflows = _workflow_health()
    artifacts = _artifact_health()

    # Conservative gate: engineering health is measurable; truth is not inferred.
    checks = {
        "python_parse": not compile_errors,
        "required_agents": not missing_agents,
        "artifact_manifest": "artifact-manifest-missing" not in artifacts["errors"],
        "source_coverage": artifacts["records"] == 0 or artifacts["source_coverage"] >= 0.95,
        "workflow_scheduling": any(x["has_schedule"] for x in workflows),
        "workflow_timeout_controls": all(x["has_timeout"] for x in workflows if x["has_schedule"]),
    }
    passed = sum(bool(v) for v in checks.values())
    score = round(100 * passed / len(checks), 2)

    result = {
        "schema_version": "3.0",
        "mode": "continuous-supreme-reliability-supervisor",
        "truth_claim": False,
        "accuracy_policy": "No heuristic, model score, or source presence is treated as proof of truth.",
        "gate": "PASS" if all(checks.values()) else "HOLD",
        "engineering_reliability_score": score,
        "checks": checks,
        "python_files_checked": compile_count,
        "python_parse_errors": compile_errors[:100],
        "missing_required_agents": missing_agents,
        "workflow_health": workflows,
        "artifact_health": artifacts,
        "latency_ms": round((time.perf_counter() - started) * 1000, 2),
        "next_actions": (
            ["continue independent verification", "monitor drift", "preserve provenance", "abstain on insufficient evidence"]
            if all(checks.values()) else
            ["repair failed engineering checks", "re-run supervisor", "keep affected outputs on HOLD"]
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result

if __name__ == "__main__":
    print(json.dumps(evaluate(), ensure_ascii=False, indent=2))
