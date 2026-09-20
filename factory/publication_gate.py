#!/usr/bin/env python3
"""Unify factory safety/QC reports into one fail-closed publication decision."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "generated"
REPORTS = {
    "deterministic_qc": "QC-REPORT.json",
    "formulation_qc": "FORMULATION-QC.json",
    "verification_queue_qc": "VERIFICATION-QUEUE-QC.json",
    "verification_promotion_qc": "VERIFICATION-PROMOTION-QC.json",
}

def read_report(filename):
    path = OUT / filename
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_load_error": str(exc)}

def main():
    reports = {k: read_report(v) for k, v in REPORTS.items()}
    missing = [k for k,v in reports.items() if v is None]
    invalid = [k for k,v in reports.items() if isinstance(v,dict) and "_load_error" in v]
    blocked = [k for k,v in reports.items() if isinstance(v,dict) and v.get("publication_gate")=="BLOCK"]
    queue_ok = isinstance(reports["verification_queue_qc"],dict) and reports["verification_queue_qc"].get("publication_gate")=="PASS"
    formulation_ok = isinstance(reports["formulation_qc"],dict) and reports["formulation_qc"].get("publication_gate")=="PASS"
    decision = "BLOCK" if (missing or invalid or blocked or not queue_ok or not formulation_ok) else (
        "PASS" if all(isinstance(v,dict) and v.get("publication_gate") in {"PASS","CHECK"} for v in reports.values())
        else "CHECK")
    result = {
        "version": 1,
        "publication_gate": decision,
        "required_reports": REPORTS,
        "missing_reports": missing,
        "invalid_reports": invalid,
        "blocked_reports": blocked,
        "verification_is_independent": False,
        "policy": "Provenance, generated reasoning, and verification queues are not independent proof. VERIFIED requires the separate human/audit promotion gate.",
        "reports": reports,
    }
    (OUT/"PUBLICATION-GATE.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"publication_gate":decision,"missing":len(missing),"invalid":len(invalid),"blocked":len(blocked)},ensure_ascii=False))
    if decision=="BLOCK":
        raise SystemExit(1)

if __name__=="__main__":
    main()
