import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "docs" / "supreme-nlp-practitioner-contract.md",
    ROOT / "docs" / "supreme-nlp-evaluation-gate.md",
    ROOT / "schemas" / "supreme-nlp-evaluation.schema.json",
    ROOT / "schemas" / "supreme-nlp-signal-translation.schema.json",
    ROOT / "schemas" / "agent-governance.json",
    ROOT / "factory" / "supreme_nlp_contract_qc.py",
    ROOT / "factory" / "supreme_nlp_evaluation_qc.py",
]

EXPECTED_VERIFICATION_STATES = [
    "REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"
]

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"BLOCKED: invalid JSON in {path.relative_to(ROOT)}: {exc}")

def main():
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    if missing:
        raise SystemExit("BLOCKED: missing required artifacts: " + ", ".join(missing))

    governance = load_json(ROOT / "schemas" / "agent-governance.json")
    evaluation = load_json(ROOT / "schemas" / "supreme-nlp-evaluation.schema.json")
    signal = load_json(ROOT / "schemas" / "supreme-nlp-signal-translation.schema.json")

    signal_required = {
        "record_id", "source_modality", "measurement", "detected_pattern",
        "model_inference", "plain_language_interpretation", "confidence",
        "provenance", "verification_state", "unknowns"
    }
    signal_properties = signal.get("properties", {})
    signal_checks = {
        "signal_schema_type_object": signal.get("type") == "object",
        "signal_required_fields_complete": set(signal.get("required", [])) == signal_required,
        "signal_additional_properties_blocked": signal.get("additionalProperties") is False,
        "signal_verification_states_fail_closed":
            signal_properties.get("verification_state", {}).get("enum") == EXPECTED_VERIFICATION_STATES,
        "signal_provenance_array":
            signal_properties.get("provenance", {}).get("type") == "array",
        "signal_unknowns_array":
            signal_properties.get("unknowns", {}).get("type") == "array",
        "signal_alternatives_array":
            signal_properties.get("alternative_interpretations", {}).get("type") == "array",
    }

    checks = {
        "fail_closed": governance.get("fail_closed") is True,
        "provenance_required": governance.get("provenance_required_for_claims") is True,
        "fabrication_prohibited": governance.get("fabrication_prohibited") is True,
        "verification_states_fail_closed":
            evaluation.get("properties", {}).get("verification_state", {}).get("enum")
            == EXPECTED_VERIFICATION_STATES,
        "baseline_numeric":
            evaluation.get("properties", {}).get("baseline", {}).get("type") == "number",
        "result_numeric":
            evaluation.get("properties", {}).get("result", {}).get("type") == "number",
        **signal_checks,
    }

    status = "PASS" if all(checks.values()) else "BLOCKED"
    telemetry = {
        "schema_version": "1.1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "checks": checks,
        "accuracy_claim_policy": "measured_benchmark_only",
        "biological_signal_policy":
            "signal_inference_is_not_proof_of_subjective_feeling",
        "verification_policy":
            "workflow_pass_does_not_promote_unverified_to_verified",
    }

    out = ROOT / "generated" / "supreme-nlp-operational-health.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(telemetry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if status != "PASS":
        failed = [name for name, ok in checks.items() if not ok]
        raise SystemExit("Operational health gate BLOCKED: " + ", ".join(failed))
    print("SHIRMANI Supreme NLP Operational Health: PASS")

if __name__ == "__main__":
    main()
