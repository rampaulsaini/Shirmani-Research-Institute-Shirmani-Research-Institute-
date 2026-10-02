"""Deterministic Supreme NLP Automission policy layer.

Produces measurable signal summaries and improvement actions. It never claims
subjective experience from a signal and never mutates production code.
"""
from __future__ import annotations
import math
from typing import Any

def clip(x: float) -> float:
    return max(0.0, min(1.0, float(x)))

def inspect(signals: list[dict[str,Any]]) -> dict[str,Any]:
    usable=[]
    for row in signals:
        try:
            value=float(row.get("value",0)); quality=clip(float(row.get("quality",0)))
        except (TypeError,ValueError):
            continue
        if math.isfinite(value): usable.append((value,quality))
    actions=[]
    if not usable: actions.append("collect usable signals before interpretation")
    mean_quality=sum(q for _,q in usable)/len(usable) if usable else 0.0
    if mean_quality < .70: actions.append("improve signal quality and sensor validation")
    if len(usable) < 10: actions.append("increase evaluation sample size before stronger claims")
    if not actions: actions.append("continue regression, calibration and independent verification")
    return {
      "state":"IMPROVEMENT_REQUIRED" if len(actions)>1 else "MONITOR",
      "signal_count":len(usable),"mean_quality":round(mean_quality,6),
      "actions":actions,
      "governance":{"fail_closed":True,"independent_verification_required":True,
                    "subjective_experience_claim_allowed":False,
                    "scheduled_code_mutation_allowed":False,
                    "accuracy_is_measured_not_declared":True}
    }
