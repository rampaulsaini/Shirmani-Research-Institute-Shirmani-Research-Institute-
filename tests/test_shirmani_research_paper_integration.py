#!/usr/bin/env python3
"""Regression checks for the Shirmani Research Paper federation entry."""
from __future__ import annotations

import json
from pathlib import Path

REGISTRY = Path("automation/repository-network-registry-2026-10-01.json")
INDEX = Path("index.html")


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    integration = registry.get("research_paper_integration", {})
    assert integration.get("repository") == "rampaulsaini/Shirmani-Research-Paper"
    assert integration.get("role") == "PRIMARY_RESEARCH_PAPER"
    assert integration.get("connection_status") == "CONNECTED"
    assert integration.get("verification_status") == "UNVERIFIED"
    assert integration.get("public_entrypoint", "").startswith("https://")
    assert "main platform public menu entry" in integration.get("connection_basis", [])

    html = INDEX.read_text(encoding="utf-8")
    assert "Shirmani Research Paper — प्रमुख शोध" in html
    assert 'id="shirmani-research-paper"' in html
    assert "https://github.com/rampaulsaini/Shirmani-Research-Paper" in html
    assert "Independent Verification" in html
    print("Shirmani Research Paper integration: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
