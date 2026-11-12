from pathlib import Path
import re

DOC = Path("docs/SUPREME-NISHPaksh-AUTOMISSION-GOVERNANCE.md")
REQUIRED = [
    "OBSERVED -> DERIVED -> INFERRED -> EXPLAINED -> INDEPENDENTLY_VERIFIED -> PUBLISHED",
    "INFERRED != VERIFIED",
    "confidence != probability of truth",
    "counter-evidence",
    "alternative hypotheses",
    "Scheduled production-code mutation: BLOCKED.",
    "Human agency",
]

text = DOC.read_text(encoding="utf-8")
missing = [x for x in REQUIRED if x not in text]
assert not missing, f"Missing governance requirements: {missing}"

# Guard against accidental weakening of the evidence boundary.
assert "subjective feeling, consciousness, intention or pain" in text
assert "fail closed" in text.lower()
assert "rollback path" in text.lower()

print("NISHPakSH_GOVERNANCE_CONTRACT: PASS")
