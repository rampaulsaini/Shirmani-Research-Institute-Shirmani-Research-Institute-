#!/usr/bin/env python3
"""Deterministic readiness gate for the SHIRMANI second-version presentation layer.

This intentionally does not call HeyGen. External connection state must be evidenced
by an authorized integration before the repository can label the subsystem connected.
"""

from __future__ import annotations

import json
from pathlib import Path

CONTRACT = Path("docs/heygen-second-version-contract.md")
OUT = Path("generated/heygen-second-version-readiness.json")

REQUIRED = [
    "Voice → authorized voice integration",
    "accurate lip synchronization",
    "coherent voice/face timing",
    "source-linked answers when evidence exists",
    "अभी पर्याप्त प्रमाण उपलब्ध नहीं है。",
    "separation of philosophical/identity statements from independently verified scientific claims",
    "Reality gate",
]

def main() -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    checks = {item: item in text for item in REQUIRED}
    result = {
        "system": "SHIRMANI_SECOND_VERSION_PRESENTATION",
        "external_provider": "HeyGen",
        "contract_present": CONTRACT.exists(),
        "contract_checks": checks,
        "contract_complete": all(checks.values()),
        "external_connection": "NOT_EVIDENCED",
        "production_state": "SPEC_READY_EXTERNAL_INTEGRATION_PENDING",
        "truth_rule": "Never claim an external HeyGen operation succeeded without evidence.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["contract_complete"]:
        raise SystemExit("Second-version contract is incomplete")

if __name__ == "__main__":
    main()
