#!/usr/bin/env python3
"""Lightweight public-surface audit. Heuristic only; not a penetration test."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXTS = {".html", ".htm", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".py", ".yml", ".yaml", ".json"}
SKIP = {".git", "node_modules", ".venv", "venv", "dist", "build"}
RULES = [
    ("HIGH", "possible hard-coded credential", re.compile(r"""(?i)(api[_-]?key|secret|access[_-]?token|password)\s*[:=]\s*['"][A-Za-z0-9_./+=-]{16,}['"]""")),
    ("MEDIUM", "unsafe DOM HTML sink (review context)", re.compile(r"\b(?:innerHTML|outerHTML|insertAdjacentHTML)\s*=")),
    ("MEDIUM", "new-window link (check rel=noopener noreferrer)", re.compile(r"""target\s*=\s*['_"]_blank['_"]""", re.I)),
    ("MEDIUM", "dynamic code execution sink (review context)", re.compile(r"\b(?:eval\s*\(|new\s+Function\s*\()")),
]

def main():
    findings = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTS:
            continue
        if any(part in SKIP for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, 1):
            for severity, label, pattern in RULES:
                if pattern.search(line):
                    # Never print source lines: a match could contain a credential.
                    findings.append({
                        "severity": severity,
                        "rule": label,
                        "path": str(path.relative_to(ROOT)),
                        "line": line_no,
                    })
    output = ROOT / "generated" / "security-public-surface-audit.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "schema_version": 1,
        "audit_type": "heuristic_static_review",
        "not_a_penetration_test": True,
        "findings_count": len(findings),
        "findings": findings,
    }
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    high = sum(item["severity"] == "HIGH" for item in findings)
    medium = sum(item["severity"] == "MEDIUM" for item in findings)
    print(f"Public-surface heuristic audit: {len(findings)} finding(s); HIGH={high} MEDIUM={medium}")
    print(f"Report: {output.relative_to(ROOT)}")
    print("Review findings manually; false positives are possible and a clean report does not prove security.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
