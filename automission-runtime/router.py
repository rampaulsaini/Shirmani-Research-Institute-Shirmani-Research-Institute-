from queue import QueueStore

IRREVERSIBLE = {"apply", "submit", "accept_contract", "publish", "payment"}

def route(store, item):
    action = item.get("action", "review")
    if action in IRREVERSIBLE:
        return {"status":"APPROVAL_REQUIRED","action":action,"opportunity_id":item["id"]}
    return {"status":"QUEUED","action":action,"opportunity_id":item["id"]}

def route_pending(store, limit=25):
    routed = []
    for item in store.pending(limit):
        result = route(store, item)
        routed.append(result)
    return routed
