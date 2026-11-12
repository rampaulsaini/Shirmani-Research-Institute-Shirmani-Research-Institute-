import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-claim-evidence.schema.json"

REQUIRED = [
    "claim_id",
    "source_text",
    "operational_definition",
    "comparison_scope",
    "evidence",
    "counter_evidence",
    "testability",
    "limitations",
    "verification_state",
]

ALLOWED_STATES = ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"]

def main():
    if not SCHEMA.is_file():
        raise SystemExit("BLOCKED: evidence schema missing")

    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"BLOCKED: invalid evidence schema: {exc}")

    missing = [k for k in REQUIRED if k not in schema.get("required", [])]
    if missing:
        raise SystemExit("BLOCKED: schema missing required keys: " + ", ".join(missing))

    props = schema.get("properties", {})
    states = props.get("verification_state", {}).get("enum")
    if states != ALLOWED_STATES:
        raise SystemExit("BLOCKED: verification states are not fail-closed")

    if props.get("evidence", {}).get("type") != "array":
        raise SystemExit("BLOCKED: evidence must be an array")
    if props.get("counter_evidence", {}).get("type") != "array":
        raise SystemExit("BLOCKED: counter_evidence must be an array")

    if props.get("confidence", {}).get("minimum") != 0 or props.get("confidence", {}).get("maximum") != 1:
        raise SystemExit("BLOCKED: confidence bounds must be 0..1")

    contract = ROOT / "docs" / "supreme-nlp-evidence-comparison-gate.md"
    text = contract.read_text(encoding="utf-8") if contract.is_file() else ""
    for term in [
        "Author wording",
        "operational definition",
        "counter-evidence",
        "Four-Yuga comparison protocol",
        "Fail-closed rules",
        "subjective feeling",
        "universal accuracy"
    ]:
        if term not in text:
            raise SystemExit("BLOCKED: contract missing required control: " + term)

    print("SHIRMANI Supreme NLP Evidence & Comparative Reasoning Gate: PASS")

if __name__ == "__main__":
    main()
