"""Deterministic integrity checks for the SHIRMANI Supreme NLP contract.

This is a contract/architecture benchmark, not a claim of model accuracy.
It verifies that required epistemic boundaries and fail-closed language remain
present before an automated cycle can be considered healthy.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "supreme-nlp-practitioner-contract.md"
GRAPH = ROOT / "docs" / "supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"

REQUIRED = (
    "Measured signal",
    "Model inference",
    "Interpretation",
    "Confidence",
    "Unresolved uncertainty",
    "Accuracy is measured",
    "Missing provenance → UNVERIFIED.",
    "Missing evaluation evidence → UNVERIFIED.",
    "Contradictory evidence → REVIEW.",
    "Failed safety/integrity check → BLOCK.",
    "Independent verification is never inferred from workflow success.",
)

def main() -> None:
    contract = CONTRACT.read_text(encoding="utf-8")
    graph = GRAPH.read_text(encoding="utf-8")
    missing = [term for term in REQUIRED if term not in contract]
    if missing:
        raise SystemExit("INTEGRITY BENCHMARK FAIL: " + "; ".join(missing))
    for term in ("Independent Verification", "Continuous Improvement", "Multimodal Perception"):
        if term not in graph:
            raise SystemExit(f"INTEGRITY BENCHMARK FAIL: graph missing {term}")
    print("SHIRMANI Supreme NLP integrity benchmark: PASS")
    print("Scope: deterministic contract/architecture integrity; model accuracy is not inferred.")

if __name__ == "__main__":
    main()
