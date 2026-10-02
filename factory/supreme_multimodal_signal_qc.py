import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/supreme-multimodal-signal-to-language-contract.md"
SCHEMA = ROOT / "schemas/supreme-multimodal-signal-record.schema.json"

TERMS = [
    "Signal -> Quality -> Features -> Pattern -> Model Inference -> Evidence",
    "Plain Language",
    "Confidence",
    "verification_state",
    "subjective feeling",
    "Fail-closed",
]

def main():
    if not CONTRACT.is_file() or not SCHEMA.is_file():
        raise SystemExit("Multimodal signal contract/schema missing")
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [term for term in TERMS if term.lower() not in text.lower()]
    if missing:
        raise SystemExit("Contract missing: " + ", ".join(missing))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    expected = {
        "source_id","timestamp","modality","signal_fingerprint","preprocessing",
        "features","pattern","model","inference","confidence","provenance",
        "alternatives","unknowns","verification_state"
    }
    if set(schema.get("required", [])) != expected:
        raise SystemExit("Signal schema required keys mismatch")
    if schema.get("additionalProperties") is not False:
        raise SystemExit("Signal schema must be fail-closed")
    print("SHIRMANI Supreme Multimodal Signal QC: PASS")

if __name__ == "__main__":
    main()
