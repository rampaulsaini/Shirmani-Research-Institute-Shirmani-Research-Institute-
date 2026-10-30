import sqlite3

import pytest

from adapter_registry import AdapterRegistry


def test_adapter_registration_never_implies_readiness(tmp_path):
    registry = AdapterRegistry(tmp_path / "adapters.db")
    key = registry.register("digital-store", "publish", ["publish"])
    assert registry.can_execute(key) is False
    assert registry.snapshot() == {"DISCOVERED": 1}


def test_ready_requires_authorization_flag(tmp_path):
    registry = AdapterRegistry(tmp_path / "adapters.db")
    key = registry.register("freelance-platform", "submit", ["submit"])
    registry.set_state(key, "CONFIGURED")
    registry.set_state(key, "HEALTH_CHECKED", {"ok": True})
    registry.set_state(key, "AUTHORIZED", {"approved": True})
    registry.set_state(key, "READY", {"ok": True})
    assert registry.can_execute(key) is True
