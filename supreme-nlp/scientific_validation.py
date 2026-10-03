"""Scientific validation primitives for Supreme NLP."""
from __future__ import annotations
import hashlib, json
from dataclasses import dataclass
from typing import Any, Iterable

@dataclass(frozen=True)
class ValidationResult:
    status: str
    score: float
    reasons: tuple[str, ...]

def fingerprint(value: Any) -> str:
    raw=json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",",":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def calibration_error(predicted: Iterable[float], observed: Iterable[bool], bins: int=10) -> float:
    p=list(predicted); y=list(observed)
    if not p or len(p)!=len(y): return 1.0
    p=[max(0.0,min(1.0,float(x))) for x in p]
    total=0.0
    for b in range(bins):
        lo=b/bins; hi=(b+1)/bins
        idx=[i for i,x in enumerate(p) if lo <= x < hi or (b==bins-1 and x==hi)]
        if idx:
            total += len(idx)/len(p) * abs(sum(p[i] for i in idx)/len(idx) - sum(bool(y[i]) for i in idx)/len(idx))
    return round(total,6)

def independent_gate(*, repeated_trials:int, independent_sources:int, preregistered:bool,
                     blinded:bool, negative_controls:bool, reproducible:bool,
                     effect_replicated:bool) -> ValidationResult:
    reasons=[]
    checks={
        "pre_registration":preregistered, "blinding":blinded,
        "negative_controls":negative_controls, "reproducibility":reproducible,
        "effect_replication":effect_replicated,
    }
    if repeated_trials < 3: reasons.append("At least 3 repeated trials are required.")
    if independent_sources < 2: reasons.append("At least 2 independent data sources/labs are required.")
    reasons.extend(k for k,v in checks.items() if not v)
    passed=(repeated_trials>=3 and independent_sources>=2 and all(checks.values()))
    return ValidationResult("VERIFIED_CANDIDATE" if passed else "NOT_VERIFIED",
                            1.0 if passed else 0.0, tuple(reasons))

def make_claim_record(observation:dict[str,Any], hypothesis:str, result:ValidationResult)->dict[str,Any]:
    record={"schema_version":"3.0.0","observation":observation,"hypothesis":hypothesis,
            "verification":{"status":result.status,"score":result.score,"reasons":list(result.reasons)},
            "epistemic_boundary":{"observation_is_not_experience":True,
                                  "model_confidence_is_not_proof":True,
                                  "independent_replication_required":True}}
    record["fingerprint"]=fingerprint(record)
    return record
