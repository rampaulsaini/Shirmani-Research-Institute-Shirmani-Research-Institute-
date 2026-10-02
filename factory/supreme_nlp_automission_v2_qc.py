import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "supreme-nlp-automission-operating-contract-v2.md"
SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-record.schema.json"
GOV = ROOT / "schemas" / "agent-governance.json"
LEGACY = ROOT / "factory" / "supreme_nlp_contract_qc.py"

MARKERS = [
    "निष्पक्षता contract","Signal → Language contract","Supreme accuracy gate",
    "Fail-closed states","Five-minute Automission policy",
    "Biological / plant / environmental interpretation",
    "Security and privacy","Improvement objective"
]

def main():
    for p in (CONTRACT, SCHEMA, GOV, LEGACY):
        if not p.exists():
            raise SystemExit(f"BLOCK: missing required artifact: {p}")

    text = CONTRACT.read_text(encoding="utf-8")
    missing = [m for m in MARKERS if m not in text]
    if missing:
        raise SystemExit("BLOCK: missing contract markers: " + ", ".join(missing))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema["required"])
    expected = {
        "record_id","observed_at","source_type","observed_signal",
        "inference","confidence","uncertainty","verification_status"
    }
    if required != expected:
        raise SystemExit("BLOCK: required signal fields changed unexpectedly")

    gov = json.loads(GOV.read_text(encoding="utf-8"))
    required_flags = ("fail_closed","provenance_required_for_claims","fabrication_prohibited")
    for key in required_flags:
        if gov.get(key) is not True:
            raise SystemExit(f"BLOCK: governance flag {key} is not true")

    print("SHIRMANI Supreme NLP + Automission v2 QC: PASS")
    print("ACCURACY_STATUS=BENCHMARK_REQUIRED")
    print("VERIFICATION_STATUS=INDEPENDENT_VERIFICATION_REQUIRED")
    print("AUTONOMY_STATUS=BOUNDED_FAIL_CLOSED")
    print("BIOLOGICAL_SUBJECTIVE_FEELING=NOT_INFERRED_FROM_SIGNAL_ALONE")

if __name__ == "__main__":
    main()
