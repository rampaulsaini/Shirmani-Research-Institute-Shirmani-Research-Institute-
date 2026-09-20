#!/usr/bin/env python3
"""Unify factory safety/QC reports into one fail-closed publication decision.

A publication PASS means required deterministic gates passed and no gate
reported BLOCK. It does not mean that claims are scientifically or
independently verified.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REPORTS = {
    "deterministic_qc": "QC-REPORT.json",
    "formulation_qc": "FORMULATION-QC.json",
    "verification_queue_qc": "VERIFICATION-QUEUE-QC.json",
    "verification_promotion_qc": "VERIFICATION-PROMOTION-QC.json",
}

def load(name):
    path = OUT / name
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_load_error": str(exc)}

def main():
    reports = {key: load(filename) for key, filename in REPORTS.items()}
    missing = [key for key, value in reports.items() if value is None]
    invalid = [key for key, value in reports.items()
               if isinstance(value, dict) and "_load_error" in value]
    blocked = [key for key, value in reports.items()
               if isinstance(value, dict) and value.get("publication_gate") == "BLOCK"]
    queue_unready = (
        reports["verification_queue_qc"] is not None
        and reports["verification_queue_qc"].get("publication_gate") != "PASS"
    )
    formulation_unready = (
        reports["formulation_qc"] is not None
        and reports["formulation_qc"].get("publication_gate") != "PASS"
    )
    if missing or invalid or blocked or queue_unready or formulation_unready:
        decision = "BLOCK"
    elif all(isinstance(reports[key], dict)
             and reports[key].get("publication_gate") in {"PASS", "CHECK"}
             for key in REPORTS):
        decision = "PASS"
    else:
        decision = "CHECK"
    result = {
        "version": 1,
        "publication_gate": decision,
        "required_reports": REPORTS,
        "missing_reports": missing,
        "invalid_reports": invalid,
        "blocked_reports": blocked,
        "verification_is_independent": False,
        "policy": "Publication safety is fail-closed. Provenance, generated reasoning and queue records never count as independent proof. VERIFIED requires the separate human/audit promotion gate.",
        "reports": reports,
    }
    (OUT / "PUBLICATION-GATE.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"publication_gate": decision, "missing": len(missing),
                      "invalid": len(invalid), "blocked": len(blocked)}, ensure_ascii=False))
    if decision == "BLOCK":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
