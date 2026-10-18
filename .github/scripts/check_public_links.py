#!/usr/bin/env python3
"""Check newly added local HTML links in a pull request.

Only links introduced on added diff lines are checked, so legacy broken links
do not suddenly block unrelated changes. External URLs and app-only schemes
are intentionally skipped.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ATTR = re.compile(r"""\b(?:href|src|poster|action)\s*=\s*["']([^"']+)["']""", re.I)
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data", "blob", "sms"}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, stderr=subprocess.STDOUT)


def is_local_target(page: Path, raw: str) -> tuple[Path | None, str | None]:
    value = raw.strip()
    if not value or value.startswith("#"):
        return None, None
    parsed = urlsplit(value)
    if parsed.scheme.lower() in SKIP_SCHEMES or parsed.netloc:
        return None, None
    path = unquote(parsed.path)
    if not path:
        return None, None
    # A leading slash is interpreted as repository-root-relative for this check.
    candidate = Path(path.lstrip("/")) if path.startswith("/") else page.parent / path
    candidate = Path(__import__("os").path.normpath(str(candidate)))
    if candidate.is_dir():
        candidate = candidate / "index.html"
    if candidate.exists():
        return candidate, None
    # Extensionless links may intentionally resolve to a directory index.
    if not candidate.suffix and (candidate / "index.html").exists():
        return candidate / "index.html", None
    return candidate, f"{page.as_posix()} -> {raw} (expected {candidate.as_posix()})"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_public_links.py <base-sha>")
        return 2
    base = sys.argv[1]
    changed = git("diff", "--name-only", f"{base}...HEAD", "--", "*.html", "*.htm").splitlines()
    failures: list[str] = []
    checked = 0
    for name in changed:
        page = Path(name)
        if not page.is_file():
            continue
        diff = git("diff", "--unified=0", f"{base}...HEAD", "--", name)
        for line in diff.splitlines():
            if not line.startswith("+") or line.startswith("+++"):
                continue
            for match in ATTR.finditer(line[1:]):
                raw = match.group(1)
                target, error = is_local_target(page, raw)
                if target is None and error is None:
                    continue
                checked += 1
                if error:
                    failures.append(error)
    print(f"Public link integrity: checked {checked} newly added local link(s) across {len(changed)} changed HTML file(s).")
    if failures:
        print("\nBroken or unresolved local targets:")
        for failure in sorted(set(failures)):
            print(f"  - {failure}")
        print("\nFix the target or document why the link is generated externally before merging.")
        return 1
    print("PASS: all newly added local HTML targets resolve to repository files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
