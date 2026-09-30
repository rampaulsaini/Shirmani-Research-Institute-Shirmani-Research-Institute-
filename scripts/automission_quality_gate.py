#!/usr/bin/env python3
"""Deterministic, model-agnostic Automission quality gate.

This gate does not claim perfect AI accuracy. It verifies engineering contracts:
- workflow YAML is structurally plausible
- retry loops are bounded
- explicit permissions are present
- concurrency is declared for automation workflows
- verification/abstention language is preserved
- a small deterministic NLP normalization/routing benchmark remains stable
"""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / ".github" / "workflows"
OUT = ROOT / "automation" / "quality" / "latest-quality-report.json"

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def norm(s: str) -> str:
    s = s.casefold().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def nlp_benchmark():
    cases = [
        ("  Automission   Accuracy  ", "automission accuracy"),
        ("AI/ML/NLP Verification", "ai/ml/nlp verification"),
        ("  Yatharth  सत्य  ", "yatharth सत्य"),
        ("Abstain when evidence is insufficient", "abstain when evidence is insufficient"),
    ]
    results = [{"input": a, "expected": b, "actual": norm(a), "pass": norm(a) == b} for a,b in cases]
    return results

def workflow_audit():
    files = sorted(list(WF.glob("*.yml")) + list(WF.glob("*.yaml")))
    results = []
    names = {}
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"(?m)^name:\s*(.+?)\s*$", text)
        name = m.group(1).strip() if m else p.name
        names.setdefault(name, []).append(p.name)
        checks = {
            "has_name": bool(m),
            "has_permissions": bool(re.search(r"(?m)^permissions:\s*$", text)),
            "has_concurrency": bool(re.search(r"(?m)^concurrency:\s*$", text)),
            "has_timeout": bool(re.search(r"(?m)^\s+timeout-minutes:\s*\d+", text)),
            "no_unbounded_sleep_loop": not bool(re.search(r"while\s+true|for\s*\(\s*;\s*;\s*\)", text)),
            "retry_is_bounded": not bool(re.search(r"rerun[^\n]*failed", text, re.I)) or bool(re.search(r"attempt|run_attempt|limit|bounded|once|one", text, re.I)),
            "verification_boundary_present": bool(re.search(r"verification|abstention|provenance|integrity", text, re.I)),
        }
        results.append({"file": p.relative_to(ROOT).as_posix(), "name": name, "checks": checks})
    duplicate_names = {k:v for k,v in names.items() if len(v) > 1}
    return files, results, duplicate_names

def main():
    files, audits, duplicate_names = workflow_audit()
    benchmark = nlp_benchmark()
    failures = []
    for item in audits:
        for check, ok in item["checks"].items():
            if not ok:
                failures.append(f"{item['file']}: {check}")
    failures += [f"duplicate workflow name: {k} -> {v}" for k,v in duplicate_names.items()]
    failures += [f"NLP benchmark mismatch: {x['input']!r}" for x in benchmark if not x["pass"]]
    report = {
        "schema": "shirmani.automission.quality.v1",
        "workflow_count": len(files),
        "workflow_audits": audits,
        "deterministic_nlp_benchmark": benchmark,
        "failure_count": len(failures),
        "failures": failures,
        "verification_policy": {
            "independent_verification_is_not_inferred_from_ci_pass": True,
            "abstain_on_insufficient_evidence": True,
            "provenance_required_for_released_results": True,
        },
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, ensure_ascii=False))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "workflow_count": len(files),
        "failure_count": len(failures),
        "report": OUT.as_posix(),
        "report_sha256": report["report_sha256"],
    }, indent=2))
    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
