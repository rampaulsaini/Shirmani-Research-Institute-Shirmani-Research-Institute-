#!/usr/bin/env python3
"""Guarded AI code improvement agent. Creates a patch only; never merges or deploys."""
import json, os, re, subprocess, sys, urllib.request, urllib.error

API_KEY = os.environ.get("OPENAI_API_KEY", "")
MODEL = os.environ.get("OPENAI_CODE_AGENT_MODEL", "gpt-5-codex")
if not API_KEY:
    print("SKIP: OPENAI_API_KEY repository secret is not configured; no files changed.")
    sys.exit(0)

def run(args, **kwargs):
    return subprocess.run(args, check=True, text=True, capture_output=True, **kwargs)

# Keep the agent scoped to the current Node API and its tests.
paths = run(["git", "ls-files", "server/src/index.js", "server/test"]).stdout.splitlines()
paths = [p for p in paths if p == "server/src/index.js" or re.fullmatch(r"server/test/[A-Za-z0-9._-]+\.test\.js", p)]
if not paths:
    print("SKIP: no allowlisted API source/test files found.")
    sys.exit(0)
context = []
for path in paths:
    try:
        data = open(path, encoding="utf-8").read()
    except (OSError, UnicodeError):
        continue
    context.append(f"\n--- FILE: {path} ---\n{data[:24000]}")
source = "\n".join(context)
if len(source) > 100000:
    source = source[:100000]

instructions = """You are a cautious senior Node.js maintainer for this repository.
Inspect the supplied source and tests. Identify at most ONE clearly evidenced, high-value correctness, security, reliability, or customer-enquiry/income-readiness defect that can be fixed safely in this small change.
If no clear defect exists, return an empty patch. Do not invent issues or make cosmetic churn.
Return ONLY valid JSON: {"summary":"short evidence-based summary","patch":"unified diff"}.
Patch constraints:
- Only modify server/src/index.js or existing/new server/test/*.test.js files.
- No deletions, renames, binaries, dependency changes, workflow changes, secret changes, migrations, schema changes, provider activation, payment acceptance, external network calls, or production data changes.
- Preserve /api/health as liveness-only; /api/ready as readiness; paid_orders as canonical income evidence ledger; payment webhook fail-closed until signed provider verification and idempotency exist.
- Never fabricate customers, orders, payments, dispatch, delivery, or revenue.
- Add/adjust regression tests for any behavior change. Do not claim tests passed.
- Avoid broad refactors. Unified diff must apply cleanly to current checkout.
"""

payload = {
    "model": MODEL,
    "instructions": instructions,
    "input": "Repository source and tests follow.\n" + source,
    "max_output_tokens": 6000
}
req = urllib.request.Request(
    "https://api.openai.com/v1/responses",
    data=json.dumps(payload).encode(),
    headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=120) as response:
        result = json.loads(response.read().decode())
except urllib.error.HTTPError as exc:
    detail = exc.read().decode(errors="replace")[:1000]
    print(f"Agent API error HTTP {exc.code}: {detail}", file=sys.stderr)
    sys.exit(1)

text = result.get("output_text")
if not text:
    pieces = []
    for item in result.get("output", []):
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                pieces.append(part.get("text", ""))
    text = "\n".join(pieces)
try:
    answer = json.loads(text)
except Exception:
    print("Agent returned invalid JSON; refusing to apply any patch.", file=sys.stderr)
    sys.exit(1)
patch = answer.get("patch", "")
summary = str(answer.get("summary", "No summary supplied"))[:500]
if not patch.strip():
    print("NO_CHANGE: " + summary)
    sys.exit(0)
if "GIT binary patch" in patch or re.search(r"^deleted file mode|^rename (from|to)", patch, re.M):
    print("BLOCKED: patch contains deletion, rename, or binary content.", file=sys.stderr)
    sys.exit(1)
changed = re.findall(r"^\+\+\+ b/(.+)$", patch, re.M)
if not changed or any(not (p == "server/src/index.js" or re.fullmatch(r"server/test/[A-Za-z0-9._-]+\.test\.js", p)) for p in changed):
    print("BLOCKED: patch touches paths outside the strict allowlist: " + repr(changed), file=sys.stderr)
    sys.exit(1)
patch_file = "/tmp/guarded-agent.patch"
open(patch_file, "w", encoding="utf-8").write(patch)
run(["git", "apply", "--check", patch_file])
run(["git", "apply", patch_file])
print("PATCH_APPLIED: " + summary)
print("Changed files: " + ", ".join(changed))
