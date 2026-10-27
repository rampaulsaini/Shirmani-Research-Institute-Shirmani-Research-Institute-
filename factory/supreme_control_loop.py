#!/usr/bin/env python3
"""Fail-closed, provider-free control loop for AI/ML/NLP artifacts.

This is a verification harness, not a claim of perfect intelligence.
It checks evidence, provenance, confidence bounds, and verification status.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

def iter_jsonl(path: Path):
    if not path.exists():
        return
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            yield line_no, json.loads(line)
        except Exception as exc:
            yield line_no, {"__parse_error__": str(exc)}

def inspect_nlp_records(report):
    candidates = [
        GENERATED / "nlp-results.jsonl",
        GENERATED / "nlp-manifest.jsonl",
        GENERATED / "reasoning-manifest.jsonl",
        GENERATED / "claim-evidence.jsonl",
    ]
    seen = 0
    violations = 0
    for path in candidates:
        for line_no, record in iter_jsonl(path) or []:
            seen += 1
            if "__parse_error__" in record:
                report["blocking_errors"].append(f"{path.relative_to(ROOT)}:{line_no}:invalid_json")
                violations += 1
                continue
            confidence = record.get("confidence")
            if confidence is not None:
                try:
                    c = float(confidence)
                    if not 0.0 <= c <= 1.0:
                        raise ValueError
                except Exception:
                    report["blocking_errors"].append(f"{path.relative_to(ROOT)}:{line_no}:invalid_confidence")
                    violations += 1
            status = record.get("verification_status") or record.get("evidence_status")
            if status in {"VERIFIED", "independently_verified"} and record.get("independent") is not True:
                report["blocking_errors"].append(f"{path.relative_to(ROOT)}:{line_no}:unearned_verification")
                violations += 1
            if ("reasoning" in record or "claim" in record) and record.get("human_review_required") is not True:
                report["blocking_errors"].append(f"{path.relative_to(ROOT)}:{line_no}:human_review_gate_missing")
                violations += 1
            if ("reasoning" in record or "claim" in record) and not record.get("source_ids"):
                report["blocking_errors"].append(f"{path.relative_to(ROOT)}:{line_no}:missing_source_ids")
                violations += 1
    return seen, violations

def main():
    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "gate": "PASS",
        "checks_total": 0,
        "checks_passed": 0,
        "verification_violations": 0,
        "nlp_records_inspected": 0,
        "blocking_errors": [],
    }
    def check(name, fn):
        report["checks_total"] += 1
        try:
            ok = bool(fn())
        except Exception as exc:
            ok = False
            report["blocking_errors"].append(f"{name}:exception:{exc}")
        if ok:
            report["checks_passed"] += 1
        elif not any(x.startswith(name + ":") for x in report["blocking_errors"]):
            report["blocking_errors"].append(f"{name}:FAIL")
        return ok
    check("repository_layout", lambda: (ROOT / ".github" / "workflows").exists() and (ROOT / "agents").exists() and (ROOT / "factory").exists())
    check("framework_contract", lambda: (lambda d: isinstance(d, dict) and bool(d.get("framework_id")))(load_json(ROOT / "factory" / "shirmani-framework.json")))
    def qc_check():
        p = GENERATED / "QC-REPORT.json"
        if not p.exists():
            return True
        d = load_json(p)
        return isinstance(d, dict) and d.get("publication_gate") in {"PASS", "BLOCK"} and isinstance(d.get("blocking_error_count"), int)
    check("qc_report_contract", qc_check)
    seen, violations = inspect_nlp_records(report)
    report["nlp_records_inspected"] = seen
    report["verification_violations"] = violations
    check("verification_safety_gate", lambda: violations == 0)
    if report["blocking_errors"]:
        report["gate"] = "BLOCK"
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "supreme-control-loop-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    raise SystemExit(1 if report["gate"] == "BLOCK" else 0)

if __name__ == "__main__":
    main()
