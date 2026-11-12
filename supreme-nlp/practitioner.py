"""Supreme NLP practitioner orchestrator."""
from __future__ import annotations
import json
from pathlib import Path
from signal_to_language import interpret as signal_interpret, load_jsonl
from engine import interpret as evidence_interpret
from quality_gate import gate

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated/supreme-nlp/signal-input.jsonl"
OUTPUT=ROOT/"generated/supreme-nlp/practitioner-status.json"

def run(input_path:Path=INPUT)->dict:
    rows=load_jsonl(input_path)
    signal=signal_interpret(rows)
    evidence=evidence_interpret(rows)
    quality=gate(signal)
    result={"schema_version":"2.0.0",
      "pipeline":["ingest","normalize","multimodal-describe","evidence-interpret","quality-gate"],
      "signal_to_language":signal,"evidence_interpretation":evidence,
      "quality_gate":quality,
      "automission":{"mode":"observe-evaluate-report","production_mutation":False,
                     "verification_promotion":"disabled",
                     "human_review_required_for_verified":True}}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return result

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
