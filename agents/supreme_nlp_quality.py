"""Supreme NLP Quality Gate: calibration, contradiction, reproducibility and abstention.

Dependency-light, deterministic controls. It evaluates a candidate record; it does
not convert model confidence into scientific truth and never performs code mutation.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
import hashlib, json
from typing import Any, Iterable

VERSION = "supreme-nlp-quality-v1"

@dataclass(frozen=True)
class QualityThresholds:
    min_quality: float = 0.70
    min_agreement: float = 0.70
    min_sources: int = 2
    min_samples: int = 10
    max_drift: float = 0.30
    max_ece: float = 0.10

def _clip(x: Any) -> float:
    try: x=float(x)
    except (TypeError, ValueError): return 0.0
    if not isfinite(x): return 0.0
    return max(0.0, min(1.0, x))

def stable_fingerprint(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()

def expected_calibration_error(predictions: Iterable[float], labels: Iterable[int], bins: int = 10) -> float:
    pairs=[(_clip(p), 1 if int(y) else 0) for p,y in zip(predictions,labels)]
    if not pairs: return 0.0
    total=len(pairs); ece=0.0
    for b in range(bins):
        lo=b/bins; hi=(b+1)/bins
        bucket=[pair for pair in pairs if (lo <= pair[0] < hi) or (b == bins-1 and pair[0] == hi)]
        if not bucket: continue
        avg_p=sum(p for p,_ in bucket)/len(bucket)
        avg_y=sum(y for _,y in bucket)/len(bucket)
        ece += len(bucket)/total * abs(avg_p-avg_y)
    return round(ece,6)

def brier_score(predictions: Iterable[float], labels: Iterable[int]) -> float | None:
    pairs=[(_clip(p), 1 if int(y) else 0) for p,y in zip(predictions,labels)]
    if not pairs: return None
    return round(sum((p-y)**2 for p,y in pairs)/len(pairs),6)

def contradiction_index(observations: list[dict[str,Any]]) -> float:
    groups: dict[str,list[float]]={}
    for x in observations:
        feature=str(x.get("feature","unknown"))
        try: value=float(x.get("value",0))
        except (TypeError,ValueError): continue
        if isfinite(value): groups.setdefault(feature,[]).append(value)
    scores=[]
    for vals in groups.values():
        if len(vals)<2: continue
        mean=sum(vals)/len(vals)
        scale=max(abs(mean)*0.05,1e-9)
        spread=(sum((v-mean)**2 for v in vals)/len(vals))**0.5
        scores.append(min(1.0,spread/(3*scale)))
    return round(sum(scores)/len(scores),6) if scores else 0.0

def evaluate(record: dict[str,Any], labels: dict[str,Any]|None=None,
             thresholds: QualityThresholds|None=None) -> dict[str,Any]:
    t=thresholds or QualityThresholds()
    result=record.get("result") or {}
    features=result.get("features") or {}
    interpretation=result.get("interpretation") or {}
    observations=result.get("signals") or result.get("observations") or []
    quality=_clip(features.get("quality"))
    agreement=_clip(features.get("agreement"))
    sources=int(features.get("independent_sources",features.get("sources",0)) or 0)
    samples=int(features.get("sample_count",features.get("usable_observations",len(observations))) or 0)
    drift=_clip(features.get("drift_score",features.get("baseline_drift",0)))
    confidence=_clip(interpretation.get("confidence",record.get("confidence",0)))
    contradiction=contradiction_index(observations)

    checks={
      "quality": quality >= t.min_quality,
      "agreement": agreement >= t.min_agreement,
      "independent_sources": sources >= t.min_sources,
      "sample_count": samples >= t.min_samples,
      "drift": drift <= t.max_drift,
      "contradiction": contradiction <= (1-t.min_agreement),
      "confidence_bounded": 0 <= confidence <= 1,
      "fingerprint_present": bool(record.get("fingerprint") or (record.get("provenance") or {}).get("fingerprint")),
      "unverified_by_default": (record.get("verification",{}).get("status","UNVERIFIED")=="UNVERIFIED"
          or result.get("verification",{}).get("status","UNVERIFIED")=="UNVERIFIED"),
    }

    calibration={"status":"NOT_PROVIDED","ece":None,"brier":None}
    if labels and isinstance(labels.get("predictions"),list) and isinstance(labels.get("labels"),list):
        calibration["ece"]=expected_calibration_error(labels["predictions"],labels["labels"])
        calibration["brier"]=brier_score(labels["predictions"],labels["labels"])
        calibration["status"]="PASS" if calibration["ece"] <= t.max_ece else "FAIL"
        checks["calibration"]=calibration["status"]=="PASS"

    failed=[k for k,v in checks.items() if not v]
    promotion_allowed=False
    status="PASS" if not failed else "IMPROVEMENT_REQUIRED"
    if record.get("status")=="BLOCKED" or result.get("status")=="BLOCKED":
        status="BLOCKED"

    report={
      "schema_version":VERSION,
      "generated_at":datetime.now(timezone.utc).isoformat(),
      "status":status,
      "promotion_allowed":promotion_allowed,
      "checks":checks,
      "failed_checks":failed,
      "metrics":{
        "quality":quality,"agreement":agreement,"independent_sources":sources,
        "sample_count":samples,"drift":drift,"contradiction_index":contradiction,
        "confidence":confidence,
      },
      "calibration":calibration,
      "governance":{
        "fail_closed":True,
        "subjective_experience_claim_allowed":False,
        "scheduled_code_mutation_allowed":False,
        "independent_verification_required":True,
        "accuracy_is_measured_not_declared":True,
      },
      "next_actions":(
        ["continue monitoring and regression tests"] if not failed else
        [f"address:{x}" for x in failed]
      ),
    }
    report["fingerprint"]=stable_fingerprint(report)
    return report

if __name__=="__main__":
    sample={"result":{"status":"interpreted","features":{"quality":1,"agreement":1,"independent_sources":2,"sample_count":10,"drift_score":0},
              "interpretation":{"confidence":0.5}},"signals":[],"fingerprint":"synthetic"}
    print(json.dumps(evaluate(sample),ensure_ascii=False,indent=2))
