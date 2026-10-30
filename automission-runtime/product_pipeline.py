from product_catalog import ProductCatalog

def run_quality_gate(catalog, product_id, quality_score, evidence_url=None):
    catalog.set_quality(product_id, quality_score, evidence_url)
    catalog.transition(product_id, "QC_PASSED", notes="quality gate passed")
    return catalog.get(product_id)

def prepare_for_publishing(catalog, product_id, price, currency):
    product = catalog.get(product_id)
    if not product:
        raise KeyError(product_id)
    if product["stage"] != "QC_PASSED":
        raise ValueError("product must pass QC first")
    catalog.transition(product_id, "PACKAGED", notes="digital package validated")
    catalog.set_price(product_id, price, currency)
    catalog.transition(product_id, "PRICED", notes="price set")
    catalog.transition(product_id, "READY_TO_PUBLISH", notes="ready for channel adapters")
    return catalog.get(product_id)

def request_publish_approval(catalog, product_id):
    product = catalog.get(product_id)
    if not product:
        raise KeyError(product_id)
    if product["stage"] != "READY_TO_PUBLISH":
        raise ValueError("product is not ready to publish")
    return catalog.transition(product_id, "PUBLISH_APPROVAL_REQUIRED",
                              notes="external publication requires authorization")

def publish_after_approval(catalog, product_id, approver="human"):
    return catalog.approve_publish(product_id, actor=approver)
