#!/usr/bin/env python3
"""Read-only repository security baseline; never prints matched secret values."""
from pathlib import Path
import json, os, re, sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
MAX_BYTES = 2_000_000
PATTERNS = [
    ("GitHub classic token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("AWS access key ID", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Private-key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
]
TEXT_SUFFIXES = {".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".html", ".htm", ".css", ".json", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".env", ".md", ".txt", ".sh", ".ps1", ".xml", ".sql", ".tf"}
findings, workflow_warnings, files_scanned, oversized_skipped = [], [], 0, 0
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for name in files:
        path = Path(base) / name
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() not in TEXT_SUFFIXES and name not in {".env", ".gitignore"}:
            continue
        try:
            if path.stat().st_size > MAX_BYTES:
                oversized_skipped += 1
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        files_scanned += 1
        for label, pattern in PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append({"type": label, "path": rel, "line": line})
        if rel.startswith(".github/workflows/") and name.endswith((".yml", ".yaml")):
            if not re.search(r"(?m)^permissions\s*:", text):
                workflow_warnings.append({"type": "workflow missing explicit permissions block", "path": rel})
            for line_no, line in enumerate(text.splitlines(), 1):
                if re.search(r"(?m)^\s*-?\s*uses:\s*[^\s@]+@(v\d+|main|master|latest)\s*(?:#.*)?$", line):
                    workflow_warnings.append({"type": "action reference is tag-based; consider pinning a reviewed full commit SHA", "path": rel, "line": line_no})

report = {
    "schema_version": 1,
    "scope": "read-only local repository text scan; not a penetration test or full security audit",
    "files_scanned": files_scanned,
    "oversized_files_skipped": oversized_skipped,
    "high_confidence_secret_findings": findings,
    "workflow_hardening_warnings": workflow_warnings,
    "status": "BLOCKED_HIGH_CONFIDENCE_FINDINGS" if findings else "BASELINE_SCAN_COMPLETE_WITH_REVIEW_WARNINGS" if workflow_warnings else "BASELINE_SCAN_COMPLETE",
}
print(json.dumps(report, ensure_ascii=False, indent=2))
summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as out:
        out.write("# Repository Security Baseline\n\n")
        out.write(f"- Text files scanned: **{files_scanned}**\n- Oversized files skipped: **{oversized_skipped}**\n")
        out.write(f"- High-confidence credential-pattern findings: **{len(findings)}**\n- Workflow hardening warnings: **{len(workflow_warnings)}**\n\n")
        out.write("> This is a static baseline scan, not a penetration test or guarantee of security. Matched secret values are never printed. Review warnings and confirm findings before remediation.\n\n")
        for item in findings:
            out.write(f"- **BLOCKER** {item['type']} — `{item['path']}:{item['line']}`\n")
        for item in workflow_warnings[:250]:
            out.write(f"- **REVIEW** {item['type']} — `{item['path']}" + (f":{item['line']}" if "line" in item else "") + "`\n")
if findings:
    sys.exit(1)
