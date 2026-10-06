"""Supreme NLP v3 validation layer.

Observable-signal interpretation only. No fluent output is treated as proof of
subjective experience. The layer is deterministic and exposes abstention,
disagreement, provenance, calibration and drift diagnostics.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import sqrt, isfinite
from typing import Any, Iterable
import hashlib, hmac, json

VERSION = "supreme-nlp-v3"

@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    quality: float = 1.0
    source: str = "unknown"
    experiment_id: str = ""
    unit: str = ""
    baseline_mean: float | None = None
    baseline_std: float | None = None

def clip(x: float, lo=0.0, hi=1.0) -> float:
    try:
        value = float(x)
        if not isfinite(value):
            return lo
        return max(lo, min(hi, value))
    except (TypeError, ValueError):
        return lo

def normalize(raw: dict[str, Any]) -> Signal:
    if not isinstance(raw, dict):
        raise ValueError("each signal must be a mapping")
    def num(k):
        try:
            v = raw.get(k)
            if v is None:
                return None
            value = float(v)
            return value if isfinite(value) else None
        except (TypeError, ValueError):
            return None
    invalid_value = False
    try:
        value=float(raw.get("value", 0.0))
    except (TypeError, ValueError):
        value=0.0
        invalid_value = "value" in raw
    if not isfinite(value):
        value=0.0
        invalid_value = True
    quality=clip(raw.get("quality",1.0))
    # Invalid observed values are never allowed to become trusted zero-valued
    # signals. Preserve the finite normalized value for auditability, but mark
    # the signal unusable so downstream summaries fail closed.
    if invalid_value:
        quality=0.0
    return Signal(
        modality=str(raw.get("modality","unknown")),
        feature=str(raw.get("feature","unknown")),
        value=value,
        quality=quality,
        source=str(raw.get("source","unknown")),
        experiment_id=str(raw.get("experiment_id","")),
        unit=str(raw.get("unit","")),
        baseline_mean=num("baseline_mean"),
        baseline_std=num("baseline_std"),
    )

def _zscores(rows):
    out=[]
    for s in rows:
        if s.baseline_mean is None: continue
        sd=abs(s.baseline_std or 0.0)
        if sd <= 1e-12: sd=max(abs(s.baseline_mean),1.0)
        out.append((s.value-s.baseline_mean)/sd)
    return out

def _anomaly(rows):
    """Estimate variability only within feature/unit-compatible groups."""
    groups={}
    comparable_group_count=0
    for s in rows:
        # Missing units cannot establish a safe comparability group.
        if not s.unit.strip():
            continue
        groups.setdefault((s.feature, s.unit), []).append(s)
    scores=[]
    for values in groups.values():
        if len(values)<2:
            continue
        comparable_group_count += 1
        mean=sum(s.value for s in values)/len(values)
        spread=sqrt(sum((s.value-mean)**2 for s in values)/len(values))
        scores.append(clip((spread/(abs(mean)+1e-9))/3.0))
    if scores:
        return max(scores), False
    return 0.0, len(rows)>1 and comparable_group_count==0

def _disagreement(rows):
    """Compare only compatible feature/unit groups in standardized space."""
    groups={}
    for s in rows:
        if s.baseline_mean is None:
            continue
        # A missing unit cannot establish compatibility across modalities.
        # Keep such rows out of disagreement rather than comparing raw scales.
        if not s.unit.strip():
            continue
        key=(s.feature, s.unit)
        groups.setdefault(key, {}).setdefault(s.modality, []).append(s)
    scores=[]
    for modality_groups in groups.values():
        if len(modality_groups)<2:
            continue
        means=[]
        for values in modality_groups.values():
            zs=[]
            for s in values:
                sd=abs(s.baseline_std or 0.0)
                if sd <= 1e-12:
                    sd=max(abs(s.baseline_mean or 0.0),1.0)
                zs.append((s.value-s.baseline_mean)/sd)
            means.append(sum(zs)/len(zs))
        center=sum(means)/len(means)
        scale=max(sum(abs(x) for x in means)/len(means),1.0)
        scores.append(sqrt(sum((x-center)**2 for x in means)/len(means))/scale)
    return clip(sum(scores)/len(scores)) if scores else 0.0

def summarize(signals: Iterable[dict[str,Any]]) -> dict[str,Any]:
    rows=[normalize(x) for x in signals]
    usable=[x for x in rows if x.quality>0]
    if not usable:
        return {"status":"insufficient_quality","signals":[asdict(x) for x in rows]}
    comparable_keys={(x.feature, x.unit) for x in usable if x.unit.strip()}
    aggregate_comparable = len(comparable_keys) == 1 and len(comparable_keys) == len({(x.feature, x.unit) for x in usable})
    if aggregate_comparable:
        mean=sum(x.value for x in usable)/len(usable)
        spread=sqrt(sum((x.value-mean)**2 for x in usable)/len(usable))
        aggregate_status="COMPARABLE_GROUP"
    else:
        # Never publish a pooled mean/spread across heterogeneous feature/unit
        # groups. The record remains interpretable, but the aggregate is
        # explicitly unavailable rather than numerically misleading.
        mean=None
        spread=None
        aggregate_status="INSUFFICIENT_EVIDENCE"
    quality=sum(x.quality for x in usable)/len(usable)
    modalities=len({x.modality for x in usable})
    sources=len({x.source for x in usable if x.source!="unknown"})
    experiments=len({x.experiment_id for x in usable if x.experiment_id.strip()})
    anomaly, comparability_insufficient=_anomaly(usable)
    z=_zscores(usable)
    disagreement=_disagreement(usable)
    abstain=quality<.50 or comparability_insufficient or anomaly>=.90 or disagreement>=.85
    confidence=clip(.15+.30*quality+.18*(1-anomaly)+.15*clip(len(usable)/20)+.10*clip(modalities/4)+.05*clip(sources/3)+.07*(1-disagreement))
    if abstain: confidence=min(confidence,.25)
    state="high_variability_pattern" if anomaly>=.66 else "moderate_variability_pattern" if anomaly>=.33 else "stable_pattern"
    return {
        "status":"interpreted",
        "interpretation":{
            "state":state,
            "confidence":round(confidence,4),
            "confidence_status":"UNCALIBRATED",
            "abstention":abstain,
            "calibration_required":True,
            "verification_status":"UNVERIFIED",
            "limitations":[
                "यह observable signals की model-based interpretation है, subjective feeling का direct proof नहीं।",
                "Biological/physical claims के लिए labelled data, domain calibration और independent replication आवश्यक हैं।",
                "Alternative explanations और sensor artefacts को नियंत्रित परीक्षणों से अलग करना आवश्यक है।"
            ]
        },
        "features":{
            "mean":mean,"spread":spread,
            "aggregate_comparability_status":aggregate_status,
            "anomaly_score":anomaly,
            "anomaly_comparability_status":"INSUFFICIENT_EVIDENCE" if comparability_insufficient else "COMPARABLE_GROUPS",
            "quality":quality,"modalities":modalities,"source_count":sources,
            "declared_unique_experiment_count":experiments,
            "experiment_provenance_status":"DECLARED_IDENTIFIERS_ONLY" if experiments else "MISSING_EXPERIMENT_IDENTIFIERS",
            "independence_status":"NOT_ESTABLISHED",
            "sample_count":len(usable),
            "baseline_z_score_mean":round(sum(z)/len(z),4) if z else None,
            "baseline_z_score_max_abs":round(max((abs(x) for x in z),default=0.0),4),
            "cross_modal_disagreement":round(disagreement,4)
        },
        "signals":[asdict(x) for x in rows]
    }

def simple_language(result):
    if result.get("status")!="interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है; इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i=result["interpretation"]
    if i["abstention"]:
        return "संकेतों में पर्याप्त अनिश्चितता या modality disagreement है; प्रणाली ने सुरक्षित रूप से निष्कर्ष से विराम लिया है।"
    return f"मिले संकेतों में '{i['state']}' जैसा observable pattern है। प्रारंभिक uncalibrated confidence {i['confidence']:.0%} है। यह किसी जीव के प्रत्यक्ष भाव या चेतना का प्रमाण नहीं है।"

def sha256(value) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def record_integrity_payload(record: dict[str, Any]) -> dict[str, Any]:
    """Return immutable record fields covered by the fingerprint."""
    return {
        "schema_version": record["schema_version"],
        "task_id": record["task_id"],
        "generated_at": record["generated_at"],
        "result": record["result"],
        "simple_language": record["simple_language"],
        "provenance": record["provenance"],
    }

def verify_record_integrity(record: dict[str, Any]) -> bool:
    """Verify a v3 record fingerprint without treating it as scientific proof."""
    try:
        expected = record.get("fingerprint", "")
        if not isinstance(expected, str) or not expected:
            return False
        actual = sha256(record_integrity_payload(record))
        return hmac.compare_digest(expected, actual)
    except (KeyError, TypeError, ValueError):
        return False

def validate_result_boundary(record: dict[str, Any]) -> dict[str, Any]:
    """Validate a produced result artifact without granting scientific verification.

    This is a post-result integrity/contract gate: it checks required fields,
    fingerprint integrity, and fail-closed verification semantics. It never
    promotes UNVERIFIED records to VERIFIED.
    """
    result = record.get("result")
    interpretation = result.get("interpretation") if isinstance(result, dict) else None
    provenance = record.get("provenance")
    checks = {
        "record_integrity": verify_record_integrity(record),
        "schema_present": record.get("schema_version") == VERSION,
        "task_id_present": isinstance(record.get("task_id"), str) and bool(record.get("task_id").strip()),
        # Verification is evaluated only after a concrete result artifact exists.
        # A direct verification flag, workflow success, or generated packet cannot
        # substitute for a result-level record and its fail-closed provenance.
        "result_artifact_present": (
            isinstance(result, dict)
            and result.get("status") in {"interpreted", "insufficient_quality"}
            and isinstance(interpretation, dict)
        ),
        "verification_fail_closed": (
            isinstance(interpretation, dict)
            and interpretation.get("verification_status") == "UNVERIFIED"
            and isinstance(provenance, dict)
            and provenance.get("verification_status") == "UNVERIFIED"
            and provenance.get("independent_replication_verified") is False
        ),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "scientific_verification_granted": False,
    }

def build_record(signals, task_id):
    result=summarize(signals)
    record = {
        "schema_version":VERSION,
        "task_id":task_id,
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "result":result,
        "simple_language":simple_language(result),
        "provenance":{"generator":"agents/supreme_nlp_v3.py","verification_status":"UNVERIFIED","calibration_status":"REQUIRED","experiment_provenance_status":result.get("features",{}).get("experiment_provenance_status","MISSING_EXPERIMENT_IDENTIFIERS"),"independent_replication_verified":False},
    }
    record["fingerprint"] = sha256(record_integrity_payload(record))
    return record

def calibration_report(probabilities, labels, bins=10):
    """Return Brier score and ECE for labelled evaluation data."""
    if len(probabilities)!=len(labels) or not probabilities:
        raise ValueError("probabilities and labels must have equal non-zero length")
    if not isinstance(bins, int) or isinstance(bins, bool) or bins <= 0:
        raise ValueError("bins must be a positive integer")
    try:
        raw_p=[float(x) for x in probabilities]
    except (TypeError, ValueError) as exc:
        raise ValueError("probabilities must be numeric") from exc
    if not all(isfinite(x) for x in raw_p):
        raise ValueError("probabilities must be finite")
    if any(x < 0.0 or x > 1.0 for x in raw_p):
        raise ValueError("probabilities must be within [0, 1]")
    p=raw_p
    y=[_binary_label(x) for x in labels]
    brier=sum((a-b)**2 for a,b in zip(p,y))/len(p)
    ece=0.0
    for k in range(bins):
        lo=k/bins; hi=(k+1)/bins
        idx=[i for i,x in enumerate(p) if (lo<=x<hi) or (k==bins-1 and x==hi)]
        if idx:
            acc=sum(y[i] for i in idx)/len(idx)
            conf=sum(p[i] for i in idx)/len(idx)
            ece += len(idx)/len(p)*abs(acc-conf)
    return {"brier_score":round(brier,6),"expected_calibration_error":round(ece,6),"sample_count":len(p),"status":"CALIBRATED_EVALUATION"}

def _binary_label(value: Any) -> int:
    """Accept only explicit binary labels; reject truthy strings and other ambiguity."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int) and value in (0, 1):
        return value
    if isinstance(value, float) and isfinite(value) and value in (0.0, 1.0):
        return int(value)
    raise ValueError("labels and predictions must be explicit binary values (0/1 or bool)")

def _boolean_flag(value: Any) -> bool:
    """Accept only explicit boolean abstention flags; reject truthy strings."""
    if isinstance(value, bool):
        return value
    raise ValueError("abstentions must be explicit boolean values")

def classification_report(predictions, labels):
    """Compute deterministic binary precision/recall/F1 and confusion counts."""
    if len(predictions) != len(labels) or not predictions:
        raise ValueError("predictions and labels must have equal non-zero length")
    p=[_binary_label(x) for x in predictions]
    y=[_binary_label(x) for x in labels]
    tp=sum(a==1 and b==1 for a,b in zip(p,y))
    fp=sum(a==1 and b==0 for a,b in zip(p,y))
    fn=sum(a==0 and b==1 for a,b in zip(p,y))
    tn=sum(a==0 and b==0 for a,b in zip(p,y))
    precision=tp/(tp+fp) if tp+fp else 0.0
    recall=tp/(tp+fn) if tp+fn else 0.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    accuracy=(tp+tn)/len(y)
    return {"precision":round(precision,6),"recall":round(recall,6),"f1":round(f1,6),"accuracy":round(accuracy,6),"tp":tp,"fp":fp,"fn":fn,"tn":tn,"sample_count":len(y)}

def selective_risk(predictions, labels, abstentions):
    """Measure error only on accepted predictions and expose coverage/abstention."""
    if not (len(predictions)==len(labels)==len(abstentions)) or not predictions:
        raise ValueError("predictions, labels and abstentions must have equal non-zero length")
    p=[_binary_label(x) for x in predictions]
    y=[_binary_label(x) for x in labels]
    a=[_boolean_flag(x) for x in abstentions]
    accepted=[i for i,x in enumerate(a) if not x]
    errors=sum(p[i] != y[i] for i in accepted)
    total=len(y)
    coverage=len(accepted)/total
    return {"selective_risk":round(errors/len(accepted),6) if accepted else 1.0,"coverage":round(coverage,6),"abstention_rate":round(1-coverage,6),"accepted_count":len(accepted),"sample_count":total}

def drift_report(reference, current, threshold=2.0):
    """Screen feature drift using absolute standardized mean shifts.

    This is a screening diagnostic, not proof of distributional change. Missing
    feature groups fail closed as INSUFFICIENT_EVIDENCE.
    """
    try:
        threshold_value=float(threshold)
    except (TypeError, ValueError) as exc:
        raise ValueError("threshold must be a positive finite number") from exc
    if not isfinite(threshold_value) or threshold_value <= 0:
        raise ValueError("threshold must be a positive finite number")
    # Drift diagnostics must never consume normalize()'s audit-friendly zero
    # fallback for malformed observations. Validate the raw observed values
    # first so NaN/Inf/non-numeric data becomes explicit insufficient evidence.
    def _valid_drift_input(rows):
        for raw in rows:
            if not isinstance(raw, dict):
                return False
            try:
                value = float(raw.get("value"))
            except (TypeError, ValueError):
                return False
            if not isfinite(value):
                return False
        return True
    if not _valid_drift_input(reference) or not _valid_drift_input(current):
        return {
            "status": "INSUFFICIENT_EVIDENCE",
            "drift_detected": False,
            "insufficient_evidence": True,
            "threshold": threshold_value,
            "features": {},
        }
    ref=[normalize(x) for x in reference]
    cur=[normalize(x) for x in current]
    ref_groups={}
    cur_groups={}
    for row in ref:
        # Missing units cannot establish a safe feature comparison. Keep them
        # as explicit fail-closed groups instead of treating "" as a unit.
        if not row.unit.strip():
            ref_groups.setdefault((row.feature,"<MISSING_UNIT>"),[]).append(row.value)
            continue
        ref_groups.setdefault((row.feature,row.unit),[]).append(row.value)
    for row in cur:
        if not row.unit.strip():
            cur_groups.setdefault((row.feature,"<MISSING_UNIT>"),[]).append(row.value)
            continue
        cur_groups.setdefault((row.feature,row.unit),[]).append(row.value)
    keys=sorted(set(ref_groups)|set(cur_groups))
    if not keys:
        return {"status":"INSUFFICIENT_EVIDENCE","drift_detected":False,"features":{}}
    features={}
    drift=False
    insufficient_evidence=False
    for key in keys:
        rv=ref_groups.get(key,[]); cv=cur_groups.get(key,[])
        # A one-sample population cannot support a variance-based standardized
        # shift. Do not turn a zero/undefined reference variance into an
        # artificially enormous drift score.
        if len(rv) < 2 or len(cv) < 2:
            features["|".join(key)]={"status":"INSUFFICIENT_EVIDENCE"}
            insufficient_evidence=True
            continue
        rm=sum(rv)/len(rv); cm=sum(cv)/len(cv)
        rs=sqrt(sum((x-rm)**2 for x in rv)/len(rv))
        if rs <= 1e-12:
            features["|".join(key)]={"status":"INSUFFICIENT_EVIDENCE"}
            insufficient_evidence=True
            continue
        shift=abs(cm-rm)/rs
        flagged=shift>=threshold_value
        drift=drift or flagged
        features["|".join(key)]={"reference_mean":rm,"current_mean":cm,"standardized_shift":round(shift,6),"drift":flagged}
    if drift:
        status="DRIFT_DETECTED"
    elif insufficient_evidence:
        status="INSUFFICIENT_EVIDENCE"
    else:
        status="NO_DRIFT_DETECTED"
    return {"status":status,"drift_detected":drift,"insufficient_evidence":insufficient_evidence,"threshold":threshold_value,"features":features}
