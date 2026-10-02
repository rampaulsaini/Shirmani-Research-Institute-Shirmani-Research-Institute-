import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/yatharth-governance/nishpaksh-ai-automission-v2.md"
GOV = ROOT / "schemas/agent-governance.json"

REQUIRED = [
    "Preserve every source faithfully", "privilege no source automatically", "HYPOTHESIS",
    "UNVERIFIED", "COUNTER-EVIDENCE", "Measured signal", "model inference", "confidence",
    "fail closed", "self-verification presented as independent verification",
    "HUMAN_REVIEW_REQUIRED", "reproducible evidence",
]

def main():
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [term for term in REQUIRED if term.lower() not in text.lower()]
    if missing:
        raise SystemExit("Nishpaksh Automission v2 contract missing: " + ", ".join(missing))
    gov = json.loads(GOV.read_text(encoding="utf-8"))
    checks = {
        "fail_closed": gov.get("fail_closed") is True,
        "provenance_required_for_claims": gov.get("provenance_required_for_claims") is True,
        "fabrication_prohibited": gov.get("fabrication_prohibited") is True,
        "default_status": gov.get("default_status") == "unverified",
    }
    failed = [k for k, ok in checks.items() if not ok]
    if failed:
        raise SystemExit("Governance baseline failed: " + ", ".join(failed))
    print("Nishpaksh AI–ML–NLP–Automission v2 QC: PASS")

if __name__ == "__main__":
    main()