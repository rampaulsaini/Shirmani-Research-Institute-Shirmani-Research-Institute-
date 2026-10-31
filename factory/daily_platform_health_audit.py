#!/usr/bin/env python3
"""Evidence-honest daily audit for key Shirmani public-interface paths.

This checks repository files and static navigation only. It does not verify
external provider APIs, voice identity, rendered media, lip-sync, live Q&A,
authentication, payments, sales, uptime, or revenue.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "artifacts" / "platform-health"
REPORT_PATH = REPORT_DIR / "daily-platform-health.json"
REQUIRED_FILES = [
    "public-interface.html",
    "showroom/voice-to-live-evidence-console.html",
    "showroom/shirmani-supreme-heart-view-preview.html",
    "showroom/heart-view-live-rehearsal-cue-deck.html",
    "showroom/shirmani-supreme-character-studio.html",
    "docs/VOICE_TO_LIVE_ACCEPTANCE_AND_AUTOMATION.md",
]
HEYGEN_REFERENCE = (
    "https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7"
)
CHAIN_TERMS = [
    "Voice-to-Live Evidence Console",
    "Heart-View",
    "Character Studio",
]


def check(name: str, passed: bool, detail: str) -> dict:
    return {"name": name, "passed": bool(passed), "detail": detail}


def main() -> int:
    checks = []
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        checks.append(check(
            f"required-file:{relative}",
            path.is_file(),
            "present" if path.is_file() else "missing",
        ))

    public = ROOT / "public-interface.html"
    content = public.read_text(encoding="utf-8", errors="replace") if public.exists() else ""
    for term in CHAIN_TERMS:
        checks.append(check(
            f"public-interface-entry:{term}",
            term.casefold() in content.casefold(),
            "found in public interface" if term.casefold() in content.casefold()
            else "entry text not found",
        ))
    checks.append(check(
        "existing-heygen-reference",
        HEYGEN_REFERENCE in content
        or (ROOT / "showroom/voice-to-live-evidence-console.html").is_file()
        and HEYGEN_REFERENCE in (ROOT / "showroom/voice-to-live-evidence-console.html").read_text(
            encoding="utf-8", errors="replace"
        ),
        "reference URL retained in public interface or evidence console",
    ))

    # Validate local HTML links in the two primary operator pages. External URLs
    # and fragment-only links are intentionally excluded from this static check.
    pages = [
        ROOT / "public-interface.html",
        ROOT / "showroom/voice-to-live-evidence-console.html",
    ]
    for page in pages:
        if not page.is_file():
            continue
        html = page.read_text(encoding="utf-8", errors="replace")
        for href in re.findall(r"""href\s*=\s*["']([^"'#]+)["']""", html, flags=re.I):
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("//"):
                continue
            target = (page.parent / parsed.path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                checks.append(check(
                    f"local-link:{page.relative_to(ROOT)}:{href}",
                    False, "path escapes repository root",
                ))
                continue
            # Ignore query-only paths; report missing local destinations.
            if not parsed.path:
                continue
            checks.append(check(
                f"local-link:{page.relative_to(ROOT)}:{href}",
                target.exists(),
                "destination exists" if target.exists() else "destination missing",
            ))

    total = len(checks)
    passed = sum(1 for item in checks if item["passed"])
    percent = round((passed / total) * 100, 2) if total else 0
    report = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "audit_type": "repository-static-health",
        "status": "PASS" if passed == total else "ATTENTION_REQUIRED",
        "summary": {
            "checks_total": total,
            "checks_passed": passed,
            "checks_failed": total - passed,
            "static_check_pass_percent": percent,
        },
        "scope_notice": (
            "This is a repository/static-link audit for this workflow run, not "
            "24/7 uptime telemetry or proof of external provider behavior. "
            "It does not verify HeyGen API access, voice match, rendered output, "
            "lip-sync, live Q&A, login/signup, payments, sales, or revenue."
        ),
        "checks": checks,
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))
    print(f"Detailed report: {REPORT_PATH.relative_to(ROOT)}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
