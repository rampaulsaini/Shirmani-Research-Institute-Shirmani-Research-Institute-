#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical Research Paper verification intake.

Queueing a task is not verification. Every queued record remains UNVERIFIED,
and independent records whether independent verification has already occurred.
"""
from pathlib import Path
exec((Path(__file__).with_name("research_paper_intake.py")).read_text(encoding="utf-8"), {"__name__": "__main__"})
