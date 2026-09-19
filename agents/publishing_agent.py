"""Publishing contract for machine-readable factory status."""
from pathlib import Path
import json

def publish(out,status):
    root=Path(out)
    root.mkdir(parents=True,exist_ok=True)
    payload={**status,"publication":{"status":"generated","research_is_draft":True,
      "verification_required":True,"source_of_truth":"artifact-manifest.jsonl"}}
    (root/"factory-status.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    return payload
