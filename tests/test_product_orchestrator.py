#!/usr/bin/env python3
"""Regression gate for the Product-First multi-layer factory.

This test validates the real orchestrator contract without treating workflow
activity, catalog presence, or generated output as independent verification.
"""

import json
import tempfile
from pathlib import Path

import factory.product_orchestrator as orchestrator


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        out = root / "generated"
        out.mkdir()

        # Provide representative existing assets so the orchestrator must
        # measure concrete artifacts rather than merely declaring products.
        (out / "book-001.md").write_text("# book\n", encoding="utf-8")
        (out / "research-paper-draft-001.md").write_text("# paper\n", encoding="utf-8")
        (out / "verse-corpus.jsonl").write_text('{"id":"v1"}\n{"id":"v2"}\n', encoding="utf-8")
        (out / "audio-prompts.jsonl").write_text('{"id":"a1"}\n', encoding="utf-8")
        certs = out / "certificates"
        certs.mkdir()
        (certs / "certificate-001.md").write_text("# certificate\n", encoding="utf-8")
        (out / "research-evidence-graph.json").write_text("{}\n", encoding="utf-8")
        (out / "repository-intelligence.json").write_text("{}\n", encoding="utf-8")

        original_root = orchestrator.ROOT
        original_out = orchestrator.OUT
        try:
            orchestrator.ROOT = root
            orchestrator.OUT = out
            # Reuse the checked-in product target configuration while pointing
            # generated artifacts at the isolated test directory.
            orchestrator.CFG = {
                "products": {
                    "digital_books": 100,
                    "research_papers": 100,
                    "verses": 100000,
                    "audio_prompts": 10000,
                    "certificates": 1000,
                }
            }
            orchestrator.main()
        finally:
            orchestrator.ROOT = original_root
            orchestrator.OUT = original_out

        catalog = json.loads((out / "PRODUCT-CATALOG.json").read_text(encoding="utf-8"))
        assert catalog["strategy"] == "PRODUCT_FIRST"
        assert catalog["product_count"] == 7
        assert catalog["available_units"] > 0
        assert catalog["target_units"] > catalog["available_units"]
        assert 0 < catalog["completion_pct"] < 100

        for line in catalog["lines"]:
            assert line["verification_state"] == "UNVERIFIED"
            assert line["independent_verification_required"] is True
            assert line["commercial_state"] == "NOT_CONFIGURED"

        pipeline = (out / "PRODUCT-PIPELINE.md").read_text(encoding="utf-8")
        assert "Asset → Product Record → Packaging" not in pipeline
        assert "Product creation and packaging proceed independently of verification" in pipeline
        assert "quantum-inspired" in pipeline
        assert "financial transactions and irreversible commercial actions remain disabled" in pipeline


if __name__ == "__main__":
    main()
