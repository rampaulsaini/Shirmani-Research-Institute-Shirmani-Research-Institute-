#!/usr/bin/env python3
from pathlib import Path
p = Path("factory/research_evidence_graph.py")
c = p.read_text(encoding="utf-8")
assert "research-paper-source-intake.json" in c
assert '"source:" + source_id' in c
assert 'intake.get("repository")' in c
assert 'intake.get("verification_status")' in c
print("Research Paper graph source anchor: PASS")
