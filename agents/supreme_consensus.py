"""Fail-closed multi-agent consensus and evidence gate."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
from typing import Iterable

@dataclass(frozen=True)
class AgentJudgment:
    agent: str
    label: str
    confidence: float
    evidence_ids: tuple[str, ...] = ()
    def normalized(self):
        return AgentJudgment(self.agent.strip() or "unknown", self.label.strip().upper() or "UNKNOWN",
                             max(0.0,min(1.0,float(self.confidence))),
                             tuple(sorted(set(str(x) for x in self.evidence_ids if x))))

def _weighted_vote(judgments: Iterable[AgentJudgment]):
    scores={}
    for raw in judgments:
        j=raw.normalized()
        scores[j.label]=scores.get(j.label,0.0)+j.confidence
    if not scores: return "UNKNOWN",0.0
    label,total=max(scores.items(),key=lambda x:(x[1],x[0]))
    denom=sum(scores.values())
    return label,(total/denom if denom else 0.0)

def evaluate(claim, judgments, *, required_evidence=(), min_consensus=0.80, min_agents=3):
    js=[j.normalized() for j in judgments]
    label,consensus=_weighted_vote(js)
    evidence=sorted(set(str(x) for x in required_evidence if x))
    supplied=sorted(set(e for j in js for e in j.evidence_ids))
    evidence_ok=all(e in supplied for e in evidence)
    unique_agents=len({j.agent for j in js})
    safe=bool(str(claim).strip()) and unique_agents>=min_agents and consensus>=min_consensus and evidence_ok and label=="SUPPORTED"
    return {
        "schema":"supreme-consensus/v1",
        "claim_sha256":sha256(str(claim).strip().encode()).hexdigest(),
        "agents":[asdict(j) for j in js],
        "consensus_label":label,"consensus_score":round(consensus,6),
        "unique_agents":unique_agents,"required_evidence":evidence,
        "evidence_complete":evidence_ok,"decision":"VERIFIED" if safe else "HOLD",
        "fail_closed":not safe
    }
