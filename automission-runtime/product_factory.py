from product_agents import build_product_spec, validate_agent_plan
from product_packaging import build_manifest
from product_pipeline import (
    run_quality_gate,
    prepare_for_publishing,
    request_publish_approval,
)
from product_dashboard import snapshot
from product_learning import capture_product_intelligence, prioritize_product, capture_fulfillment_signal, prioritize_with_fulfillment


class DigitalProductFactory:
    def __init__(self, catalog):
        self.catalog = catalog

    def create_blueprint(self, title, product_type, description="", languages=None):
        spec = build_product_spec(title, product_type, description, languages)
        validate_agent_plan(spec)
        product_id = self.catalog.create(
            title,
            product_type,
            description,
            payload={
                "agent_plan": spec["agents"],
                "languages": spec["languages"],
                "spec_hash": spec["spec_hash"],
            },
        )
        return product_id, spec

    def package(self, product_id, spec, files=(), version="1.0.0"):
        manifest = build_manifest(
            {**spec, "version": version},
            files=files,
            version=version,
        )
        return manifest

    def qc_and_price(
        self,
        product_id,
        quality_score,
        quality_evidence,
        price,
        currency,
    ):
        run_quality_gate(
            self.catalog,
            product_id,
            quality_score,
            quality_evidence,
        )
        return prepare_for_publishing(
            self.catalog,
            product_id,
            price,
            currency,
        )

    def request_publication(self, product_id):
        return request_publish_approval(self.catalog, product_id)

    def intelligence(self):
        return capture_product_intelligence(self.catalog.db_path)

    def dashboard(self):
        return snapshot(self.catalog.db_path)

    def score_next_product(self, base_score, product_type, currency, product_id=None, fulfillment_db=None):
        intelligence = self.intelligence()
        score = prioritize_product(base_score, product_type, currency, intelligence)
        if product_id is not None and fulfillment_db is not None:
            signal = capture_fulfillment_signal(fulfillment_db)
            score = prioritize_with_fulfillment(score, product_id, signal)
        return score
