from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
p = root / "factory" / "continuous_supervisor.py"
subprocess.run([sys.executable, str(p)], check=True, cwd=root)
r = json.loads((root / "generated" / "continuous-supervisor-status.json").read_text(encoding="utf-8"))
assert r["truth_claim"] is False
assert "gate" in r and "checks" in r
print("continuous supervisor smoke test: OK")
