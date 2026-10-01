#!/usr/bin/env python3
"""Fail-closed quality controller for the SHIRMANI automation factory.

This controller measures integrity; it never promotes records to VERIFIED.
"""
from __future__ import annotations
import json, pathlib, re, sys
from collections import Counter

ROOT = pathlib.Path(".")
OUT = ROOT / "generated" / "SUPREME-QUALITY-REPORT.json"

def load_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    checks = []
    def check(name, passed, detail):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    workflows = list((ROOT / ".github" / "workflows").glob("*.yml"))
    heart = [p for p in workflows if p.name.startswith(("heart-view-review-", "shirmani-heart-view-review-"))]
    names = [p.name for p in workflows]
    dup = [n for n,c in Counter(names).items() if c > 1]

    check("workflow_inventory", bool(workflows), f"{len(workflows)} workflow files")
    check("duplicate_filenames", not dup, f"duplicates={dup}")

    for rel in ["generated/QC-REPORT.json"]:
        p = ROOT / rel
        if p.exists():
            try:
                qc = load_json(p)
                check("factory_qc", qc.get("publication_gate") == "PASS" and qc.get("blocking_error_count", 0) == 0,
                      f"gate={qc.get('publication_gate')}, blocking={qc.get('blocking_error_count')}")
            except Exception as e:
                check("factory_qc", False, f"invalid JSON: {e}")
        else:
            check("factory_qc", False, "QC report missing")

    v = ROOT / "federation" / "verified-work.schema.json"
    if v.exists():
        try:
            spec = load_json(v)
            rules = spec.get("rules", {})
            check("verification_fail_closed",
                  rules.get("invented_work") is False and
                  rules.get("invented_skill") is False and
                  rules.get("invented_income") is False and
                  rules.get("automatic_employment") is False and
                  rules.get("automatic_payment") is False and
                  rules.get("human_review_required"),
                  "verification schema keeps human gates explicit")
        except Exception as e:
            check("verification_fail_closed", False, f"schema unreadable: {e}")
    else:
        check("verification_fail_closed", False, "verification schema missing")

    # Lightweight static safety checks on automation definitions.
    risky = []
    for p in workflows:
        s = p.read_text(encoding="utf-8", errors="replace")
        if "permissions:" not in s:
            risky.append(f"{p}: missing explicit permissions")
        if "concurrency:" not in s and ("schedule:" in s or "workflow_run" in s):
            risky.append(f"{p}: scheduled/workflow_run workflow lacks concurrency")
    check("automation_hygiene", not risky, "; ".join(risky[:12]) or "explicit permissions/concurrency present")

    # Detect the common anti-pattern of claiming VERIFIED without a human gate.
    forbidden = []
    for p in workflows:
        s = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r"VERIFIED\s*[:=].*(true|TRUE|1)", s) and "human" not in s.lower():
            forbidden.append(str(p))
    check("no_unreviewed_verified_promotion", not forbidden,
          f"suspect workflows={forbidden}")

    passed = sum(c["passed"] for c in checks)
    report = {
        "schema_version": "1.0.0",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "heart_view_workflows": len(heart),
        "principle": "Measure, verify, then promote; never infer verification.",
        "checks": checks,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
