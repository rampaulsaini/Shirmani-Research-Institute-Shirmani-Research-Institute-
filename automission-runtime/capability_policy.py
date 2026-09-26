import json
from pathlib import Path


DEFAULT_MATRIX = Path(__file__).resolve().parent.parent / "income" / "capability-permission-matrix.json"


class CapabilityPolicy:
    def __init__(self, matrix_path=None):
        path = Path(matrix_path or DEFAULT_MATRIX)
        self.data = json.loads(path.read_text(encoding="utf-8"))

    def capability(self, action):
        return self.data.get("capabilities", {}).get(action)

    def allows_execution(self, action):
        rule = self.capability(action)
        return bool(rule and rule.get("execution") is True)

    def requires_authorization(self, action):
        rule = self.capability(action)
        return bool(rule and rule.get("authorization_required") is True)

    def allows_planning(self, action):
        rule = self.capability(action)
        return bool(rule and rule.get("planning") is True)
