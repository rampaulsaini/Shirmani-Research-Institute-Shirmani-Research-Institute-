"""Shared provenance contract."""
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
