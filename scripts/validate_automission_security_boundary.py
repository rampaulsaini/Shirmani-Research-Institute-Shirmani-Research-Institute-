import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gate = json.loads((ROOT / "docs/yatharth-governance/automission-quality-gate.json").read_text())
workflow_dir = ROOT / ".github/workflows"

assert gate["non_negotiable"]["secret_exposure"] is False

# Inspect every tracked workflow textually for dangerous broad write permissions.
for path in workflow_dir.glob("*.yml"):
    text = path.read_text(errors="replace")
    lower = text.lower()
    if "permissions:" in lower:
        # A workflow may grant explicit write scopes, but must not grant all permissions.
        assert "permissions: write-all" not in lower
        assert "permissions: read-all" not in lower
        assert "contents: write" not in lower or "pull_request" in lower
    assert "secrets: *" not in lower

# The new boundary gate itself must remain read-only.
this = (workflow_dir / "automission-security-boundary-gate.yml").read_text()
assert "contents: read" in this
assert "write-all" not in this.lower()
assert "secret_exposure" not in this.lower() or "automission-quality-gate" in this.lower()

print("Automission Security Boundary Gate: PASS")
