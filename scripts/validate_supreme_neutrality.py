"""Deterministic validator for the SHIRMANI Supreme Neutrality Contract."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/SHIRMANI-SUPREME-NEUTRALITY-CONTRACT.md"

REQUIRED = [
    "Neutrality is a system property.",
    "Source ≠ evidence.",
    "Inference must be labeled.",
    "Counter-evidence is mandatory for verification.",
    "Subjective-experience boundary.",
    "Fail closed.",
    "No scheduled production-code mutation.",
    "Equal treatment.",
    "Observe → Collect → Normalize → Quality Check → Extract Features → Model → Compare Alternatives → Quantify Uncertainty → Translate → Preserve Provenance → Verify",
]

def main():
    text = DOC.read_text(encoding="utf-8")
    missing = [x for x in REQUIRED if x not in text]
    if missing:
        raise SystemExit("NEUTRALITY_CONTRACT_FAIL: " + " | ".join(missing))
    print("NEUTRALITY_CONTRACT: PASS")
    print("RULES:", len(REQUIRED))

if __name__ == "__main__":
    main()
