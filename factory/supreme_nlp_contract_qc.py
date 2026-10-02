import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "supreme-nlp-practitioner-contract.md"
GRAPH = ROOT / "docs" / "supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
NISHPAKSH = ROOT / "docs" / "nishpaksh-ai-operating-contract.md"
GOV = ROOT / "schemas" / "agent-governance.json"

required_contract_terms = [
    "Measured signal","Model inference","Interpretation","Confidence",
    "Unresolved uncertainty","Accuracy is measured","Fail-closed rules",
    "Independent verification","Continuous improvement",
]

def main():
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [x for x in required_contract_terms if x not in text]
    if missing: raise SystemExit("NLP contract missing: " + ", ".join(missing))

    graph = GRAPH.read_text(encoding="utf-8")
    for term in ["Multimodal Perception","NLP","Independent Verification","Continuous Improvement"]:
        if term not in graph: raise SystemExit(f"Total graph missing required stage: {term}")

    ntext=NISHPAKSH.read_text(encoding="utf-8")
    for term in ["Nishpaksh rules","counter-evidence","FAIL-CLOSED","Supreme accuracy rule"]:
        if term not in ntext: raise SystemExit(f"Nishpaksh contract missing: {term}")

    gov=json.loads(GOV.read_text(encoding="utf-8"))
    if gov.get("fail_closed") is not True: raise SystemExit("Agent governance is not fail-closed")
    if gov.get("provenance_required_for_claims") is not True: raise SystemExit("Claim provenance requirement is missing")
    if gov.get("fabrication_prohibited") is not True: raise SystemExit("Fabrication prohibition is missing")
    n=gov.get("neutrality_contract",{})
    for k in ("enabled","counter_evidence_required","uncertainty_required","source_provenance_required"):
        if n.get(k) is not True: raise SystemExit(f"Nishpaksh neutrality requirement missing: {k}")

    print("SHIRMANI Supreme NLP + Nishpaksh Contract: PASS")

if __name__ == "__main__":
    main()
