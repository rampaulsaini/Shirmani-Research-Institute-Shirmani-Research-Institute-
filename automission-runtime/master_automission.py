from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List

@dataclass(frozen=True)
class AgentTask:
    task_id: str
    domain: str
    role: str
    action: str
    reversible: bool = True

class MasterAutomission:
    """Deterministic control-plane planner; external irreversible actions stay gated."""
    DOMAINS = (
        "research", "education", "software", "products", "music",
        "books", "animation", "film", "design", "marketing",
        "seo", "localization", "publishing", "qc", "support",
    )

    def __init__(self):
        self.tasks: List[AgentTask] = []

    def register(self, task_id: str, domain: str, role: str, action: str,
                 reversible: bool = True):
        if domain not in self.DOMAINS:
            raise ValueError("unknown_domain")
        if not all(str(x).strip() for x in (task_id, role, action)):
            raise ValueError("task_fields_required")
        task = AgentTask(task_id, domain, role, action, reversible)
        self.tasks.append(task)
        return task

    def plan(self) -> Dict:
        return {
            "status": "PLANNED",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "task_count": len(self.tasks),
            "tasks": [t.__dict__ for t in self.tasks],
            "authorization_required_for": [
                "publish", "payment", "submit", "accept_contract"
            ],
        }

    def route(self) -> List[Dict]:
        return [
            {
                "task_id": t.task_id,
                "domain": t.domain,
                "role": t.role,
                "action": t.action,
                "status": "QUEUED" if t.reversible else "APPROVAL_REQUIRED",
            }
            for t in self.tasks
        ]
