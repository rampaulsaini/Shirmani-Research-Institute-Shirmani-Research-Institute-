#!/usr/bin/env python3
"""Fast preflight smoke test for the research factory."""
import importlib
import json
from pathlib import Path
import tempfile

AGENTS = [
    "contracts", "source_agent", "corpus_agent", "research_agent",
    "verification_agent", "writing_agent", "book_agent",
    "music_agent", "certificate_agent", "topic_agent",
    "provenance_agent", "qc_agent", "publishing_agent", "orchestrator",
]

def main():
    for name in AGENTS:
        importlib.import_module("agents." + name)

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        corpus = root / "corpus.jsonl"
        out = root / "out"
        corpus.write_text(
            json.dumps({
                "id": 1,
                "source": "smoke-test",
                "text": "निष्पक्ष समझ और स्वतंत्र परीक्षण पर एक परीक्षण वाक्य।"
            }, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        from agents.orchestrator import run
        status = run(str(corpus), str(out), batch_size=1)
        assert status["processed_batch"] == 1
        assert (out / "claims-index.json").exists()
        assert (out / "provenance-index.jsonl").exists()
        assert (out / "factory-status.json").exists()

    print("Factory smoke test OK")

if __name__ == "__main__":
    main()
