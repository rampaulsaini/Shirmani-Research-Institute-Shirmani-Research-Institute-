import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "supreme-nlp-practitioner-contract.md"
SIGNAL_CONTRACT = ROOT / "docs" / "supreme-nlp-signal-to-language-contract-2026-10-02.md"
GRAPH = ROOT / "docs" / "supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
GOV = ROOT / "schemas" / "agent-governance.json"

required_contract_terms = [
    "Measured signal", "Model inference", "Interpretation", "Confidence",
    "Unresolved uncertainty", "Accuracy is measured", "Fail-closed rules",
    "Independent verification", "Continuous improvement",
]
required_signal_terms = [
    "Canonical pipeline", "Detected pattern", "Plain-language interpretation",
    "Feeling boundary", "Accuracy", "Automission role",
]

def main():
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in required_contract_terms if x not in text]
    if missing:
        raise SystemExit("NLP contract missing: " + ", ".join(missing))

    signal = SIGNAL_CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in required_signal_terms if x not in signal]
    if missing:
        raise SystemExit("Signal-to-language contract missing: " + ", ".join(missing))

    graph = GRAPH.read_text(encoding="utf-8")
    for term in ["Multimodal Perception", "NLP", "Independent Verification", "Continuous Improvement"]:
        if term not in graph:
            raise SystemExit(f"Total graph missing required stage: {term}")

    gov = json.loads(GOV.read_text(encoding="utf-8"))
    for key in ["fail_closed", "provenance_required_for_claims", "fabrication_prohibited"]:
        if gov.get(key) is not True:
            raise SystemExit(f"Agent governance requirement missing: {key}")

    print("SHIRMANI Supreme NLP Practitioner Contract: PASS")

if __name__ == "__main__":
    main()
