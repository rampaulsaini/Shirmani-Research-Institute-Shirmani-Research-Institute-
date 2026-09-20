#!/usr/bin/env python3
"""Fast preflight smoke test for the research factory."""
import importlib
import json
from pathlib import Path
import tempfile
import sys

AGENTS = [
    "contracts", "source_agent", "corpus_agent", "research_agent",
    "verification_agent", "writing_agent", "book_agent",
    "music_agent", "certificate_agent", "topic_agent",
    "provenance_agent", "qc_agent", "publishing_agent", "orchestrator",
    "language_agents", "artifact_agent", "deep_learning_agent",
]

def _read_jsonl(path):
    """Strictly read JSONL and report the exact bad line for fast diagnosis."""
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError as exc:
            raise AssertionError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc

def main():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
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
        assert (out / "artifact-manifest.jsonl").exists()
        assert (out / "queues").exists()

        contracts = out / "contracts"
        for name in (
            "source-records.jsonl",
            "concept-records.jsonl",
            "claim-records.jsonl",
            "verification-reports.jsonl",
        ):
            path = contracts / name
            assert path.exists(), f"missing contract file: {path}"
            rows = list(_read_jsonl(path))
            assert rows, f"empty contract file: {path}"
            for row in rows:
                assert row.get("id") or row.get("record_id")

    # Provenance regression: generated paper drafts place the source value
    # on the line after "## Source"; the parser must resolve that value.
    from factory.reasoning_pipeline import source_ids_from_text
    resolved = source_ids_from_text(
        "## Source\nrepo/example:path.md\n",
        {"repo/example:path.md": "42"},
    )
    assert resolved == ["42"], f"paper source provenance regression: {resolved}"

    print("Factory smoke test OK")

if __name__ == "__main__":
    main()
