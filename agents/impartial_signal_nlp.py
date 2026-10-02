"""Deterministic evidence-first signal-to-language engine."""
from __future__ import annotations
import hashlib, json
from typing import Any

def _fingerprint(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def build_record(rows: list[dict[str, Any]], cycle: str) -> dict[str, Any]:
    clean=[]
    for row in rows:
        if isinstance(row,dict) and "feature" in row and "value" in row:
            clean.append({"name":str(row["feature"]),"value":row["value"],
                          "quality":float(row.get("quality",0.0)),
                          "source":str(row.get("source","unspecified"))})
    if not clean:
        observation={"modality":"unknown","features":[],"quality":0.0,"provenance":"no-observation"}
        interpretation={"status":"NO_DATA","pattern":"No usable signal record",
          "statement":"कोई पर्याप्त signal उपलब्ध नहीं है।","confidence":0.0,
          "uncertainty":"No observation was available.","evidence_status":"INSUFFICIENT_EVIDENCE"}
    else:
        q=sum(x["quality"] for x in clean)/len(clean)
        observation={"modality":"multimodal-signal",
          "features":[{"name":x["name"],"value":x["value"]} for x in clean],
          "quality":max(0.0,min(1.0,q)),
          "provenance":";".join(sorted(set(x["source"] for x in clean)))}
        if q < 0.70:
            status="INSUFFICIENT_EVIDENCE"
            statement="Signal मिला है, लेकिन quality पर्याप्त नहीं है कि विश्वसनीय interpretation दी जा सके।"
            evidence="INSUFFICIENT_EVIDENCE"
        else:
            status="INTERPRETED"
            statement="Observable signal में measurable pattern मिला है; इसे निजी भाव या subjective experience का प्रमाण नहीं माना गया है।"
            evidence="OBSERVATIONAL"
        interpretation={"status":status,
          "pattern":f"{len(clean)} observable feature(s); mean quality={q:.3f}",
          "statement":statement,"confidence":round(max(0.0,min(1.0,q)),6),
          "uncertainty":"Pattern interpretation depends on sensor quality, training data, context, and independent validation.",
          "evidence_status":evidence}
    body={"record_id":f"signal-{cycle}","cycle":cycle,"observation":observation,
      "interpretation":interpretation,
      "governance":{"impartiality":True,"fail_closed":True,
        "subjective_experience_claim_allowed":False,"self_verification_allowed":False},
      "simple_language":interpretation["statement"],
      "limitations":["Observable signals are not by themselves proof of subjective experience.",
                     "Confidence is not evidence.","Independent verification remains a separate gate."]}
    body["fingerprint"]=_fingerprint(body)
    return body
