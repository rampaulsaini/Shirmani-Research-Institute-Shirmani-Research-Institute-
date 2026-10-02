import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/supreme-agent-orchestration-contract-2026-10-02.md"
SCHEMA = ROOT / "schemas/supreme-agent-cycle.schema.json"
GOV = ROOT / "schemas/agent-governance.json"

REQUIRED_CONTRACT_TERMS = [
    "Canonical agent graph",
    "State machine",
    "Signal-to-language boundary",
    "Continuous improvement",
    "Fail-closed controls",
    "Five-minute Automission",
]

REQUIRED_AGENT_LAYERS = [
    "intake_source",
    "reasoning",
    "evidence",
    "verification",
    "security_audit",
    "publishing",
]

def main():
    if not CONTRACT.is_file():
        raise SystemExit("Agent orchestration contract missing")
    if not SCHEMA.is_file():
        raise SystemExit("Agent cycle schema missing")
    if not GOV.is_file():
        raise SystemExit("Agent governance missing")

    text = CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in REQUIRED_CONTRACT_TERMS if x not in text]
    if missing:
        raise SystemExit("Agent contract missing: " + ", ".join(missing))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    expected = {
        "event_id","cycle_id","agent_id","agent_version",
        "input_fingerprint","output_fingerprint","provenance",
        "status","timestamp"
    }
    if not expected.issubset(required):
        raise SystemExit("Agent cycle schema is incomplete")

    gov = json.loads(GOV.read_text(encoding="utf-8"))
    layers = set(gov.get("agent_layers", []))
    missing_layers = [x for x in REQUIRED_AGENT_LAYERS if x not in layers]
    if missing_layers:
        raise SystemExit("Agent governance layers missing: " + ", ".join(missing_layers))

    for key in ["fail_closed","provenance_required_for_claims","fabrication_prohibited"]:
        if gov.get(key) is not True:
            raise SystemExit("Governance control is not enabled: " + key)

    print("SHIRMANI Supreme Agent Orchestration QC: PASS")

if __name__ == "__main__":
    main()
