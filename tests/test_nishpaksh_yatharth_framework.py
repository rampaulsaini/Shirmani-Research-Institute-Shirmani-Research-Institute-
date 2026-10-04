#!/usr/bin/env python3
import json
from pathlib import Path

claims=json.loads(Path("generated/research-paper-claims.json").read_text(encoding="utf-8"))
html=Path("index.html").read_text(encoding="utf-8")

ids={c["id"] for c in claims["claims"]}
for expected in ["SRP-C001","SRP-C002","SRP-C003","SRP-C004","SRP-C005","SRP-C006","SRP-C007","SRP-C008"]:
    assert expected in ids
assert 'id="nishpaksh-yatharth-framework"' in html
assert "श्रेष्ठता Verification Gate" in html
assert "Research Boundary" in html
assert all(c["verification_status"] == "UNVERIFIED" for c in claims["claims"])
print(f"Nishpaksh Yatharth framework: PASS ({len(claims['claims'])} unverified propositions)")
