from product_agents import build_product_spec, validate_agent_plan
from product_packaging import build_manifest
from product_pipeline import run_quality_gate, prepare_for_publishing, request_publish_approval\nfrom product_dashboard import snapshot\nfrom product_learning import capture_product_intelligence, prioritize_product

class DigitalProductFactory:
    def __init__(self, catalog):
        self.catalog = catalog

    def create_blueprint(self, title, product_type, description="", languages=None):
        spec = build_product_spec(title, product_type, description, languages)
        validate_agent_plan(spec)
        product_id = self.catalog.create(
            title, product_type, description,
            payload={"agent_plan": spec["agents"], "languages": spec["languages"],
                     "spec_hash": spec["spec_hash"]},
        )
        return product_id, spec

    def package(self, product_id, spec, files=(), version="1.0.0"):
        manifest = build_manifest(
            {**spec, "version": version},
            files=files,
            version=version,
        )
        return manifest

    def qc_and_price(self, product_id, quality_score, quality_evidence,
                     price, currency):
        run_quality_gate(self.catalog, product_id, quality_score, quality_evidence)
        return prepare_for_publishing(self.catalog, product_id, price, currency)

    def request_publication(self, product_id):
        return request_publish_approval(self.catalog, product_id)
