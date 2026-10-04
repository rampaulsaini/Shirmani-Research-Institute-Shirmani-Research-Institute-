import json
from pathlib import Path
p=Path("generated/claim-evidence.jsonl")
rows=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
srp=[x for x in rows if str(x.get("id","")).startswith("claim:research-paper-claim:")]
assert srp
assert all((x.get("verification") or {}).get("status")=="NOT_VERIFIED" for x in srp)
assert all((x.get("verification") or {}).get("independent") is False for x in srp)
print("Research Paper evidence intake: PASS")
