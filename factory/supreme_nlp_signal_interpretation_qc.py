import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/supreme-nlp-multimodal-signal-language-contract.md"
SCHEMA = ROOT / "schemas/supreme-nlp-signal-interpretation.schema.json"

REQUIRED_CONTRACT_TERMS = [
    "Canonical pipeline",
    "Interpretation boundary",
    "Required interpretation record",
    "Fail-closed rules",
    "Accuracy",
    "Automission",
]

REQUIRED_SCHEMA_KEYS = [
    "record_id","timestamp","signal_modality","source_provenance",
    "acquisition_context","quality_status","detected_pattern","model",
    "task_scope","inference","uncertainty","evidence",
    "alternative_interpretations","unresolved_questions","verification_state",
]

def main():
    if not CONTRACT.is_file():
        raise SystemExit("Multimodal signal contract is missing")
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in REQUIRED_CONTRACT_TERMS if x not in text]
    if missing:
        raise SystemExit("Contract missing: " + ", ".join(missing))

    if not SCHEMA.is_file():
        raise SystemExit("Signal interpretation schema is missing")
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    missing = [x for x in REQUIRED_SCHEMA_KEYS if x not in schema.get("required", [])]
    if missing:
        raise SystemExit("Schema missing required keys: " + ", ".join(missing))

    states = schema.get("properties", {}).get("verification_state", {}).get("enum", [])
    if states != ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"]:
        raise SystemExit("Verification states are not fail-closed")

    modalities = schema.get("properties", {}).get("signal_modality", {}).get("enum", [])
    if "biopotential" not in modalities or "multimodal" not in modalities:
        raise SystemExit("Required multimodal/biopotential modalities are missing")

    quality = schema.get("properties", {}).get("quality_status", {}).get("enum", [])
    if quality != ["PASS","REVIEW","BLOCKED"]:
        raise SystemExit("Quality states are invalid")

    print("SHIRMANI Supreme NLP Multimodal Signal-to-Language Gate: PASS")

if __name__ == "__main__":
    main()
