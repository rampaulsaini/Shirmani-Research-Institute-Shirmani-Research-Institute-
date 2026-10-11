#!/usr/bin/env python3
"""Small, dependency-free security smoke check for changed public HTML files.

This is a regression guard, not a full security audit or penetration test.
It fails on executable javascript: URLs and reports common risky DOM sinks
for human review rather than assuming every occurrence is exploitable.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

HTML_SUFFIXES = {".html", ".htm"}
JAVASCRIPT_URL = re.compile(
    r"""\b(?:href|src|action|formaction)\s*=\s*(['"])\s*javascript\s*:""",
    re.IGNORECASE,
)
RISKY_SINKS = (
    ("innerHTML assignment", re.compile(r"\.innerHTML\s*\+?=")),
    ("document.write", re.compile(r"\bdocument\s*\.\s*write\s*\(")),
    ("inline event handler", re.compile(r"""\bon[a-z]+\s*=\s*(['"])""", re.IGNORECASE)),
)
TARGET_BLANK = re.compile(r"""\btarget\s*=\s*(['"])_blank\1""", re.IGNORECASE)
REL_NOOPENER = re.compile(r"""\brel\s*=\s*(['"])[^'"]*\bnoopener\b[^'"]*\1""", re.IGNORECASE)

def main() -> int:
    paths = [Path(arg) for arg in sys.argv[1:]]
    html_files = [p for p in paths if p.suffix.lower() in HTML_SUFFIXES and p.is_file()]
    if not html_files:
        print("Security smoke gate: no changed HTML files to inspect.")
        return 0

    errors = 0
    warnings = 0
    for path in html_files:
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"ERROR {path}: cannot read file: {exc}")
            errors += 1
            continue

        if JAVASCRIPT_URL.search(content):
            print(f"FAIL  {path}: executable javascript: URL found in href/src/action")
            errors += 1

        for label, pattern in RISKY_SINKS:
            matches = list(pattern.finditer(content))
            if matches:
                print(f"WARN  {path}: {label} appears {len(matches)} time(s); review data flow and sanitization.")
                warnings += len(matches)

        # A simple whole-file heuristic: warn if _blank exists but no noopener
        # token appears anywhere. Review manually because attributes may be built dynamically.
        if TARGET_BLANK.search(content) and not REL_NOOPENER.search(content):
            print(f"WARN  {path}: target=_blank found without a static rel=noopener token.")
            warnings += 1

    print(f"Security smoke gate summary: files={len(html_files)}, hard_failures={errors}, review_warnings={warnings}.")
    print("Warnings require human review; this check does not prove a page safe or certify the platform.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
