import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "supreme-nlp-signal-to-language-contract-2026-10-02.md"
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-interpretation.schema.json"

TERMS = [
    "Measured signal", "Detected pattern", "Model inference",
    "Plain-language interpretation", "Confidence / uncertainty",
    "Evidence / provenance", "Alternative interpretation",
    "Unresolved unknowns", "subjective feeling", "consciousness",
    "Verification states",
]
REQUIRED = [
    "record_id", "modality", "measured_signal", "detected_pattern",
    "model_inference", "plain_language", "uncertainty",
    "provenance", "verification_state",
]

def main():
    text = DOC.read_text(encoding="utf-8")
    missing = [term for term in TERMS if term not in text]
    if missing:
        raise SystemExit("Signal contract missing: " + ", ".join(missing))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED if key not in schema.get("required", [])]
    if missing:
        raise SystemExit("Signal schema missing required keys: " + ", ".join(missing))
    states = schema.get("properties", {}).get("verification_state", {}).get("enum", [])
    if states != ["REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"]:
        raise SystemExit("Signal verification states are not fail-closed")
    print("SHIRMANI Supreme NLP Signal Contract: PASS")

if __name__ == "__main__":
    main()
