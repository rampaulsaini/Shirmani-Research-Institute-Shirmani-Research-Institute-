import sys
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1] / "automission-runtime"
sys.path.insert(0, str(RUNTIME))

from master_automission import MasterAutomission


def _master():
    master = MasterAutomission()
    master.register("research-cycle", "research", "research-orchestrator", "research")
    master.register("product-cycle", "products", "product-orchestrator", "create_blueprint")
    return master


def test_unverified_or_missing_fulfillment_does_not_boost_product_priority():
    master = _master()
    base = master.plan({"fulfillment_learning": {"verified_deliveries_by_product": {}}})
    assert base["tasks"][0]["priority"] == 0.50
    assert base["tasks"][1]["priority"] == 0.50


def test_verified_fulfillment_boosts_only_product_domain():
    master = _master()
    intelligence = {
        "fulfillment_learning": {
            "verified_deliveries_by_product": {
                "product-a": {"verified_deliveries": 7},
                "product-b": {"verified_deliveries": 3},
            }
        }
    }
    plan = master.plan(intelligence)
    priorities = {task["task_id"]: task["priority"] for task in plan["tasks"]}
    assert priorities["product-cycle"] == 0.51
    assert priorities["research-cycle"] == 0.50


def test_fulfillment_priority_boost_is_strictly_bounded():
    master = _master()
    intelligence = {
        "fulfillment_learning": {
            "verified_deliveries_by_product": {
                "product-a": {"verified_deliveries": 100000},
                "product-b": {"verified_deliveries": 100000},
            }
        }
    }
    plan = master.plan(intelligence)
    priorities = {task["task_id"]: task["priority"] for task in plan["tasks"]}
    assert priorities["product-cycle"] == 0.60
    assert priorities["product-cycle"] - priorities["research-cycle"] <= master.MAX_LEARNED_PRIORITY_BOOST


def test_route_preserves_authorization_gate_for_irreversible_tasks():
    master = MasterAutomission()
    master.register("publish-cycle", "publishing", "publisher", "publish", reversible=False)
    intelligence = {
        "fulfillment_learning": {
            "verified_deliveries_by_product": {"product-a": {"verified_deliveries": 100}}
        }
    }
    routed = master.route(intelligence)
    assert routed[0]["status"] == "APPROVAL_REQUIRED"
    assert routed[0]["priority"] == 0.50
