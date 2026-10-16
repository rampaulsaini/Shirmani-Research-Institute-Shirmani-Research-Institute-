#!/usr/bin/env python3
"""Regression test: the production reality gate must remain valid Python syntax."""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "factory" / "production_reality_gate.py"


class ProductionRealityGateSyntaxTests(unittest.TestCase):
    def test_gate_source_parses(self):
        source = SOURCE.read_text(encoding="utf-8")
        ast.parse(source, filename=str(SOURCE))


if __name__ == "__main__":
    unittest.main()
