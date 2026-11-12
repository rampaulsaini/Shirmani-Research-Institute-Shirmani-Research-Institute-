#!/usr/bin/env python3
"""Fail-closed neutrality gate for SHIRMANI Supreme Automission."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/yatharth-governance/nishpaksh-automission-control-contract.md"
GRAPH = ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
NLP = ROOT / "docs/supreme-nlp-practitioner-contract.md"

REQUIRED = [
    "Preserve → Classify → Evidence → Compare → Test → Verify → Publish",
    "SOURCE_DECLARED",
    "MEASURED",
    "INFERRED",
    "UNVERIFIED",
    "VERIFIED",
    "CONTRADICTED",
    "REVIEW",
    "counter-evidence",
    "Uncalibrated heuristic confidence",
    "Scheduled Automission may not",
    "Five-minute loop",
]

def need(text, term):
    if term not in text:
        raise AssertionError(f"missing:{term}")

def main():
    for p in (CONTRACT, GRAPH, NLP):
        if not p.is_file() or p.stat().st_size == 0:
            raise AssertionError(f"missing_or_empty:{p.relative_to(ROOT)}")

    contract = CONTRACT.read_text(encoding="utf-8")
    graph = GRAPH.read_text(encoding="utf-8")
    nlp = NLP.read_text(encoding="utf-8")

    for term in REQUIRED:
        need(contract, term)

    # Existing architecture must retain the measured-signal boundary.
    for term in (
        "Accuracy is measured, not declared.",
        "A model output is not automatically proof of subjective feeling or consciousness.",
        "Independent verification is distinct from preparation/QC.",
    ):
        need(graph, term)

    for term in (
        "Measured signal",
        "Model inference",
        "Interpretation",
        "Confidence",
        "Unresolved uncertainty",
    ):
        need(nlp, term)

    # Protect against unsupported certainty language entering the new contract.
    forbidden = re.findall(
        r"\b(?:100% accurate|consciousness detected|subjective experience proven)\b",
        contract,
        re.I,
    )
    if forbidden:
        raise AssertionError("unsupported_certainty_language:" + ",".join(sorted(set(forbidden))))

    print("NISHPaksh SUPREME AUTOMISSION NEUTRALITY GATE: PASS")
    print("Evidence states: PASS")
    print("Conflict protocol: PASS")
    print("Signal/inference boundary: PASS")
    print("Accuracy boundary: PASS")
    print("Fail-closed automation boundary: PASS")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"NISHPaksh SUPREME AUTOMISSION NEUTRALITY GATE: BLOCK — {exc}")
        sys.exit(1)
