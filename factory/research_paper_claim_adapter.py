#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical Research Paper claim bridge."""
from pathlib import Path
exec((Path(__file__).with_name("research_paper_claim_adapter_v2.py")).read_text(encoding="utf-8"), {"__name__": "__main__"})
