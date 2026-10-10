#!/usr/bin/env python3
"""Read-only static baseline checks for GitHub Actions workflow files.

Guardrail only—not a penetration test or security certification. It never prints
secret values and never modifies source files.
"""
from pathlib import Path
import json, re, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"
checks = []
def add(level, path, rule, detail):
    checks.append({"level": level, "path": str(path.relative_to(ROOT)), "rule": rule, "detail": detail})

files = sorted(WORKFLOWS.glob("*.yml")) + sorted(WORKFLOWS.glob("*.yaml")) if WORKFLOWS.exists() else []
if not files:
    add("WARN", WORKFLOWS, "workflow_files_present", "No workflow YAML files were found.")
for path in files:
    source = path.read_text(encoding="utf-8", errors="replace")
    if re.search(r"(?i)curl[^\n|]*\|\s*(?:sudo\s+)?(?:bash|sh)", source):
        add("FAIL", path, "pipe_remote_script", "Remote content appears to be piped directly to a shell.")
    if re.search(r"(?m)^\s*pull_request_target\s*:", source):
        add("WARN", path, "pull_request_target", "Review untrusted pull-request code paths and secret exposure.")
    if re.search(r"(?i)(?:echo|printf)[^\n]*(?:secrets\.[A-Za-z_]+|\$\{\{\s*secrets\.)", source):
        add("FAIL", path, "possible_secret_logging", "Possible secret interpolation in output; inspect without printing secret values.")
    uses = re.findall(r"(?m)^\s*uses:\s*([^\s#]+)", source)
    floating = [ref for ref in uses if not re.search(r"@[0-9a-fA-F]{40}$", ref)]
    if floating:
        add("WARN", path, "unpinned_actions", f"{len(floating)} action reference(s) use a tag/non-SHA ref; consider full commit-SHA pinning.")
    if not re.search(r"(?m)^\s*permissions\s*:", source):
        add("WARN", path, "explicit_permissions", "No explicit permissions block detected; define least privilege.")

report = {
    "schema_version": "1.0",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "static review of .github/workflows/*.yml and *.yaml",
    "files_scanned": len(files),
    "fail_count": sum(c["level"] == "FAIL" for c in checks),
    "warning_count": sum(c["level"] == "WARN" for c in checks),
    "checks": checks,
    "limitations": [
        "Not a penetration test, dependency scan, secret-history scan, or security certification.",
        "Regex-based checks can produce false positives and false negatives.",
        "Does not inspect account settings, repository secrets, branch protection, external services, or deployed runtime."
    ]
}
out = ROOT / "security" / "reports" / "workflow-static-baseline.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Workflow static baseline: {len(files)} files; {report['fail_count']} FAIL; {report['warning_count']} WARN.")
for item in checks:
    print(f"{item['level']} {item['path']} [{item['rule']}]: {item['detail']}")
print(f"Report written: {out.relative_to(ROOT)}")
sys.exit(1 if report["fail_count"] else 0)
