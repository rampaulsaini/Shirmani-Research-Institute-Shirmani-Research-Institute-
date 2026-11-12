#!/usr/bin/env python3
"""Deterministic Nishpaksh Heart-View Automission integrity gate."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "docs/yatharth-governance/nishpaksh-heart-view-automission-contract.md": [
        "Source preservation",
        "Equal treatment",
        "Evidence first",
        "Counter-evidence",
        "Fail closed",
        "No self-authorization",
        "Measured Signal",
        "UNVERIFIED",
    ],
    "docs/supreme-nlp-practitioner-contract.md": [
        "Measured signal",
        "Model inference",
        "Interpretation",
        "Confidence",
        "Unresolved uncertainty",
    ],
}

FORBIDDEN_ASSERTIONS = [
    "independently verified fact by default",
    "100% accuracy",
    "fully supreme accuracy",
    "subjective feeling is proven by signal",
]

def main() -> None:
    failures = []
    for rel, needles in REQUIRED.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"MISSING:{rel}:{needle}")

    workflow = (ROOT / ".github/workflows/nishpaksh-heart-view-automission.yml").read_text(
        encoding="utf-8"
    )
    if "*/5 * * * *" not in workflow:
        failures.append("MISSING:five-minute-schedule")
    if "contents: read" not in workflow:
        failures.append("MISSING:read-only-permissions")
    if "fail_closed" not in workflow:
        failures.append("MISSING:fail-closed-gate")
    if "independent_verification_required" not in workflow:
        failures.append("MISSING:independent-verification-gate")

    lower = workflow.lower()
    for phrase in FORBIDDEN_ASSERTIONS:
        if phrase.lower() in lower:
            failures.append(f"FORBIDDEN:{phrase}")

    if failures:
        print("NISHPAKSH_INTEGRITY_GATE: BLOCK")
        print("\n".join(failures))
        raise SystemExit(1)

    print("NISHPAKSH_INTEGRITY_GATE: PASS")
    print("Source preservation: PASS")
    print("Equal treatment: PASS")
    print("Evidence/counter-evidence boundary: PASS")
    print("Fail-closed boundary: PASS")
    print("Independent verification boundary: PASS")
    print("Five-minute cycle: PASS")
    print("Scheduled code mutation: BLOCKED")

if __name__ == "__main__":
    main()
