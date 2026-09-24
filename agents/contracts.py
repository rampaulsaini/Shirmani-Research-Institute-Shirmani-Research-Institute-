"""Shared provenance and agent-output contract."""
from dataclasses import dataclass, asdict
from typing import Literal
Status=Literal['source-backed','user-authored','hypothesis','unverified','verified']
@dataclass(frozen=True)
class Provenance:
    source_repository:str
    source_path:str
    source_sha256:str
    generated_at:str
    status:Status='unverified'
    notes:str=''
    def to_dict(self): return asdict(self)


AgentLayer = Literal['intake_source', 'reasoning', 'evidence', 'verification', 'product', 'marketing', 'economic_transaction', 'security_audit', 'publishing', 'continuity']

@dataclass(frozen=True)
class AgentOutput:
    agent_id: str
    agent_layer: AgentLayer
    output_id: str
    status: Status = 'unverified'
    provenance: Provenance | None = None
    requires_human_authorization: bool = False
    external_side_effects: bool = False
    notes: str = ''

    def to_dict(self):
        return asdict(self)


def publication_eligible(output: AgentOutput) -> bool:
    """Fail closed: verified status and provenance are both required."""
    return output.status == 'verified' and output.provenance is not None
