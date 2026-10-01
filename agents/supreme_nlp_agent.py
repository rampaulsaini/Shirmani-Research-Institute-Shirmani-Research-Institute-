"""Evidence-first multimodal-to-NLP control layer."""
from __future__ import annotations
import hashlib, json, math, re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "supreme-nlp-v1"

def _sha(obj: Any) -> str:
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()

def signal_summary(signals: list[dict[str, Any]]) -> dict[str, Any]:
    kinds, numeric = {}, []
    for s in signals:
        k = str(s.get("type", "unknown"))
        kinds[k] = kinds.get(k, 0) + 1
        if isinstance(s.get("value"), (int, float)) and math.isfinite(float(s["value"])):
            numeric.append(float(s["value"]))
    return {"signal_count":len(signals),"signal_types":kinds,
            "numeric_observations":len(numeric),
            "numeric_mean":sum(numeric)/len(numeric) if numeric else None}

def interpret(observation: dict[str, Any]) -> dict[str, Any]:
    signals = observation.get("signals") or []
    result = {
        "schema_version": VERSION,
        "status": "UNVERIFIED",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_sha256": _sha(observation),
        "observation": {"context":normalize_text(observation.get("context","")),
                        "summary":signal_summary(signals)},
        "natural_language": (
            "Observable signals show a measurable pattern that may be associated "
            "with a contextual state; this is not direct proof of subjective emotion "
            "or consciousness."
        ),
        "evidence_boundary":"observable_signal_only",
        "confidence":0.0,
        "verification":{"required":True,"independent_reviewer_required":True},
        "next_actions":["collect repeated observations",
                        "compare with labeled/control data",
                        "test alternative explanations",
                        "record counter-evidence",
                        "independently verify before promotion"]
    }
    return result

def save(observation: dict[str, Any], path: str) -> dict[str, Any]:
    result=interpret(observation)
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    return result

if __name__ == "__main__":
    print(json.dumps(interpret({"context":"baseline","signals":[]}),ensure_ascii=False,indent=2))
