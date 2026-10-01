#!/usr/bin/env python3
"""Deterministic, fail-closed quality controller for SHIRMANI Automission.

Scope: automation integrity, reproducibility and verification boundaries.
This program does NOT infer scientific truth or model accuracy from workflow
success. Independent verification remains a separate human-review process.
"""
from __future__ import annotations
import hashlib, json, pathlib, re, sys
from collections import Counter

ROOT = pathlib.Path(".")
OUT = ROOT / "generated" / "SUPREME-QUALITY-REPORT.json"
VERIFICATION = ROOT / "generated" / "independent-verification-status-2026-09-29.json"

def load_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))

def sha256(path: pathlib.Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    checks = []
    def check(name, passed, detail):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    workflows = list((ROOT / ".github" / "workflows").glob("*.yml"))
    names = [p.name for p in workflows]
    dup = [n for n,c in Counter(names).items() if c > 1]
    check("workflow_inventory", bool(workflows), f"{len(workflows)} workflow files")
    check("duplicate_filenames", not dup, f"duplicates={dup}")

    # Every scheduled/event-driven workflow must declare bounded permissions and
    # concurrency to reduce accidental privilege and duplicate execution.
    risky = []
    for p in workflows:
        s = p.read_text(encoding="utf-8", errors="replace")
        if "permissions:" not in s:
            risky.append(f"{p}: missing explicit permissions")
        if ("schedule:" in s or "workflow_run" in s) and "concurrency:" not in s:
            risky.append(f"{p}: scheduled/workflow_run workflow lacks concurrency")
    check("automation_hygiene", not risky, "; ".join(risky[:20]) or "permissions/concurrency boundaries present")

    qc_path = ROOT / "generated" / "QC-REPORT.json"
    if qc_path.exists():
        try:
            qc = load_json(qc_path)
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
            required = ("invented_work", "invented_skill", "invented_income",
                        "automatic_employment", "automatic_payment", "human_review_required")
            check("verification_fail_closed",
                  all(rules.get(k) is False for k in required[:-1]) and bool(rules.get(required[-1])),
                  "verification schema keeps invention and human-review boundaries explicit")
        except Exception as e:
            check("verification_fail_closed", False, f"schema unreadable: {e}")
    else:
        check("verification_fail_closed", False, "verification schema missing")

    # Independent verification registry must remain zero until a real independent
    # review decision is recorded. Evidence-supported != independently verified.
    if VERIFICATION.exists():
        try:
            d = load_json(VERIFICATION)
            s = d["verification_summary"]
            records = d["records"]
            ok = (
                s["independently_verified_records"] == 0 and
                s["independent_verified_percent"] == 0 and
                len(records) == s["queue_records"] and
                sum(1 for r in records if r.get("status") == "EVIDENCE-SUPPORTED") == s["evidence_supported_records"] and
                all(str(r.get("status", "")).upper() != "VERIFIED" for r in records)
            )
            check("independent_verification_fail_closed", ok,
                  f"verified={s['independently_verified_records']}, readiness={s['verification_readiness_percent']}%, records={len(records)}")
        except Exception as e:
            check("independent_verification_fail_closed", False, f"invalid registry: {e}")
    else:
        check("independent_verification_fail_closed", False, "independent verification registry missing")

    # Validate JSONL syntax and unique IDs for traceability artifacts when present.
    jsonl_paths = [
        ROOT / "generated" / "claim-evidence.jsonl",
        ROOT / "generated" / "reasoning-manifest.jsonl",
        ROOT / "generated" / "provenance-ledger.jsonl",
        ROOT / "generated" / "independent-verification-registry.jsonl",
    ]
    jsonl_errors = []
    jsonl_counts = {}
    for path in jsonl_paths:
        if not path.exists():
            continue
        seen = set()
        count = 0
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            count += 1
            try:
                r = json.loads(line)
            except Exception as e:
                jsonl_errors.append(f"{path}:{line_no}: invalid JSON: {e}")
                continue
            rid = r.get("id") or r.get("artifact_id")
            if rid is not None:
                if rid in seen:
                    jsonl_errors.append(f"{path}:{line_no}: duplicate id={rid}")
                seen.add(rid)
            vrec = r.get("verification") if isinstance(r.get("verification"), dict) else {}
            if vrec.get("status") == "PASS" or vrec.get("independent") is True:
                jsonl_errors.append(f"{path}:{line_no}: unearned independent verification")
        jsonl_counts[str(path)] = {"records": count, "unique_ids": len(seen), "sha256": sha256(path)}
    check("traceability_jsonl", not jsonl_errors, "; ".join(jsonl_errors[:20]) or json.dumps(jsonl_counts, ensure_ascii=False))

    # Detect the common anti-pattern of claiming VERIFIED without a human gate.
    forbidden = []
    for p in workflows:
        s = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r"VERIFIED\s*[:=].*(true|TRUE|1)", s) and "human" not in s.lower():
            forbidden.append(str(p))
    check("no_unreviewed_verified_promotion", not forbidden, f"suspect workflows={forbidden}")

    passed = sum(c["passed"] for c in checks)
    report = {
        "schema_version": "1.1.0",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "principle": "Measure, verify, then promote; never infer verification.",
        "accuracy_claim": "NOT_ASSERTED",
        "independent_verification_claim": "NOT_ASSERTED",
        "artifacts": {
            "verification_registry_sha256": sha256(VERIFICATION) if VERIFICATION.exists() else None,
            "jsonl": jsonl_counts,
        },
        "checks": checks,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
