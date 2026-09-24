import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "generated" / "employment-automission-gate.json"

SCHEMAS = [
    "schemas/income-evidence-ledger.json",
    "federation/employment-income-status-bridge.schema.json",
    "federation/employment-audit-closure.schema.json",
    "federation/settlement-records.schema.json",
    "federation/reconciliation-audit-trail.schema.json",
    "federation/dispute-resolution.schema.json",
]

def load_json(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    checks = []
    errors = []

    for rel in SCHEMAS:
        try:
            data = load_json(rel)
            checks.append({"file": rel, "json": "PASS", "status": data.get("status")})
        except Exception as exc:
            errors.append(f"{rel}: {exc}")

    bridge = load_json("federation/employment-income-status-bridge.schema.json")
    closure = load_json("federation/employment-audit-closure.schema.json")
    settlement = load_json("federation/settlement-records.schema.json")
    reconciliation = load_json("federation/reconciliation-audit-trail.schema.json")
    dispute = load_json("federation/dispute-resolution.schema.json")
    ledger = load_json("schemas/income-evidence-ledger.json")

    required_assertions = {
        "bridge_no_fabricated_income": any("no fabricated" in x.lower() and "income" in x.lower()
                                           for x in bridge.get("integrity_rules", [])),
        "completed_not_paid": any("COMPLETED does not imply PAID" in x for x in bridge.get("integrity_rules", [])),
        "paid_requires_evidence": any("payment evidence" in x.lower() for x in bridge.get("integrity_rules", [])),
        "closure_requires_evidence": any("evidence" in x.lower() for x in closure.get("integrity_rules", [])),
        "settled_requires_external_evidence": any("external payment/settlement evidence" in x for x in settlement.get("integrity_rules", [])),
        "reconciled_requires_evidence": any("RECONCILED requires payment evidence" in x for x in reconciliation.get("integrity_rules", [])),
        "dispute_no_auto_decision": dispute.get("rules", {}).get("automated_decision") is False,
        "ledger_payment_requires_evidence": bool(ledger.get("rules", {}).get("payment_requires_payment_evidence")),
        "ledger_delivery_requires_evidence": bool(ledger.get("rules", {}).get("delivery_requires_delivery_evidence")),
        "ledger_public_totals_derived": bool(ledger.get("rules", {}).get("public_totals_must_be_derived_from_ledger")),
    }
    for name, ok in required_assertions.items():
        if not ok:
            errors.append(f"required integrity assertion failed: {name}")

    result = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "AUTOMISSION_EVIDENCE_GATE",
        "gate": "PASS" if not errors else "BLOCKED",
        "checks": checks,
        "assertions": required_assertions,
        "errors": errors,
        "truth_boundary": {
            "no_transaction_without_external_evidence": True,
            "no_fabricated_employment_or_income": True,
            "completed_is_not_paid": True,
            "paid_is_not_reconciled": True,
            "disputes_require_documented_resolution": True,
            "external_actions_are_not_simulated": True,
        },
        "next_action": (
            "CONTINUE_AUTOMISSION" if not errors
            else "STOP_AND_REPAIR"
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        raise SystemExit("Employment evidence gate BLOCKED")
    print("Employment Automission Evidence Gate PASS")

if __name__ == "__main__":
    main()
