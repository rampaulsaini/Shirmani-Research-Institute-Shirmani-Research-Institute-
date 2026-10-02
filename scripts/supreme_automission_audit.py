#!/usr/bin/env python3
"""Deterministic, dependency-free audit for the Supreme Neutral Automission layer."""

from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "supreme_nlp.json"
OUT = ROOT / "automation" / "reports" / "supreme-neutral-audit.json"

CERTAINTY_PATTERNS = [
    r"\b100%\s*(accuracy|accurate|proof|proved|certain)\b",
    r"\b(infallible|always correct|fully supreme accuracy)\b",
    r"\b(scientifically proven|quantum proven|proved by quantum)\b",
]

def load_config() -> dict:
    with CONFIG.open("r", encoding="utf-8") as f:
        return json.load(f)

def scan_text() -> list[dict]:
    findings = []
    extensions = {".md", ".txt", ".json", ".yml", ".yaml", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in extensions:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in CERTAINTY_PATTERNS:
            for match in re.finditer(pattern, text, flags=re.I):
                line = text.count("\n", 0, match.start()) + 1
                findings.append({
                    "file": str(path.relative_to(ROOT)),
                    "line": line,
                    "type": "unsupported_certainty_language",
                    "text": match.group(0),
                    "action": "REVIEW: attach evidence, confidence, or limitation before presenting as factual."
                })
    return findings

def main() -> int:
    cfg = load_config()
    required = [
        "neutrality", "evidence_first", "fact_inference_separation",
        "uncertainty_required", "independent_verification",
        "human_review_for_high_impact",
    ]
    missing = [k for k in required if cfg["principles"].get(k) is not True]
    findings = scan_text()
    report = {
        "system": cfg["system_name"],
        "version": cfg["version"],
        "status": "PASS" if not missing else "FAIL",
        "principle_gaps": missing,
        "review_findings": findings,
        "finding_count": len(findings),
        "note": "Review findings are non-blocking; they identify claims that require evidence or qualification."
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if missing else 0

if __name__ == "__main__":
    raise SystemExit(main())
