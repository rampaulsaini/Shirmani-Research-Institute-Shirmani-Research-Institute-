"""Fail-closed integrity gate for source-based comparison claims."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "yatharth-comparison.schema.json"
MATRIX = ROOT / "research" / "yatharth-comparison-matrix-2026-09-29.md"

REQUIRED_SCHEMA = {"claim_id", "author_claim", "definition", "comparands", "evidence", "status"}
STATUSES = {"AUTHOR-DEFINED", "AUTHOR-PROPOSED", "NEEDS OPERATIONALIZATION", "UNVERIFIED", "EVIDENCE-SUPPORTED", "VERIFIED"}

def main() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    missing = REQUIRED_SCHEMA - set(schema.get("required", []))
    if missing:
        raise SystemExit("Comparison schema missing: " + ", ".join(sorted(missing)))
    enum = set(schema.get("properties", {}).get("status", {}).get("enum", []))
    if enum != STATUSES:
        raise SystemExit("Comparison status enum drift detected")

    text = MATRIX.read_text(encoding="utf-8")
    for phrase in ["AUTHOR CLAIM", "OPERATIONAL DEFINITION", "EVIDENCE", "COUNTER-EVIDENCE", "TESTABILITY", "LIMITATION", "UNVERIFIED", "Integrity rule"]:
        if phrase not in text:
            raise SystemExit(f"Comparison matrix missing integrity term: {phrase}")

    # Guard against accidental universalization of comparative/accuracy claims.
    for pattern in [r"खरबों गुणा अधिक.*सिद्ध", r"खरबों गुणा.*scientifically proven", r"fully supreme accuracy"]:
        if re.search(pattern, text, flags=re.IGNORECASE):
            raise SystemExit("Unqualified comparative/accuracy claim detected")

    if "लेखक का “खरबों गुणा अधिक ऊंचा/सच्चा/सर्वश्रेष्ठ” एक **AUTHOR CLAIM** है" not in text:
        raise SystemExit("Author-claim boundary missing")

    print("SHIRMANI Supreme Claim Integrity QC: PASS")

if __name__ == "__main__":
    main()
