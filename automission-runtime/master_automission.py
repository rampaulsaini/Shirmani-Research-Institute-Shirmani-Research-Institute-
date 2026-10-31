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
    DEFAULT_PRIORITY = 0.50
    MAX_LEARNED_PRIORITY_BOOST = 0.10
    MAX_FULFILLMENT_SIGNAL = 100

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

    @classmethod
    def _fulfillment_priority_boost(cls, intelligence, domain):
        """Use verified delivery evidence only; never infer revenue or demand."""
        if domain != "products" or not isinstance(intelligence, dict):
            return 0.0
        fulfillment = intelligence.get("fulfillment_learning", {})
        by_product = fulfillment.get("verified_deliveries_by_product", {})
        if not isinstance(by_product, dict):
            return 0.0
        verified = 0
        for value in by_product.values():
            if isinstance(value, dict):
                value = value.get("verified_deliveries", 0)
            try:
                verified += max(0, int(value or 0))
            except (TypeError, ValueError):
                continue
        verified = min(verified, cls.MAX_FULFILLMENT_SIGNAL)
        return min(verified * 0.001, cls.MAX_LEARNED_PRIORITY_BOOST)

    def _priority(self, task, intelligence=None):
        return min(
            1.0,
            self.DEFAULT_PRIORITY + self._fulfillment_priority_boost(intelligence, task.domain),
        )

    def plan(self, intelligence=None) -> Dict:
        tasks = [
            {**t.__dict__, "priority": self._priority(t, intelligence)}
            for t in self.tasks
        ]
        tasks.sort(key=lambda item: (-item["priority"], item["task_id"]))
        return {
            "status": "PLANNED",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "task_count": len(tasks),
            "tasks": tasks,
            "priority_policy": {
                "source": "verified_fulfillment_only",
                "max_boost": self.MAX_LEARNED_PRIORITY_BOOST,
                "revenue_inference": False,
            },
            "authorization_required_for": [
                "publish", "payment", "submit", "accept_contract"
            ],
        }

    def route(self, intelligence=None) -> List[Dict]:
        routed = []
        for t in self.tasks:
            routed.append({
                "task_id": t.task_id,
                "domain": t.domain,
                "role": t.role,
                "action": t.action,
                "priority": self._priority(t, intelligence),
                "status": "QUEUED" if t.reversible else "APPROVAL_REQUIRED",
            })
        return sorted(routed, key=lambda item: (-item["priority"], item["task_id"]))
