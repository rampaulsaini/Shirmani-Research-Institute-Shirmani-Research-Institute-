export const GOVERNANCE_ROLES = Object.freeze({
  family: "LOCAL_HUMAN_CONTEXT",
  community: "COMMUNITY_COUNCIL",
  administration: "ELECTED_EXECUTIVE",
  legislature: "REPRESENTATIVE_LEGISLATURE",
  judiciary: "INDEPENDENT_JUDICIARY",
  oversight: "INDEPENDENT_OVERSIGHT",
  supreme_control: "CONSTITUTIONAL_CONSTRAINT_LAYER",
  ai: "AI_ANALYSIS_AND_ASSISTANCE"
});

export const AI_PROHIBITED_ACTIONS = Object.freeze([
  "irreversible_penalty",
  "rights_removal",
  "election_decision",
  "court_override",
  "final_custody_decision",
  "autonomous_force_authorization",
  "self_verification"
]);

export const HUMAN_REVIEW_REQUIRED = Object.freeze([
  "criminal_or_civil_penalty",
  "rights_or_access_restriction",
  "child_safety_escalation",
  "medical_high_impact_decision",
  "public_benefit_denial",
  "environmental_harm_authorization",
  "election_or_civic_process_action",
  "judicial_or_appeal_outcome"
]);

export function governancePolicy() {
  return {
    status: "ARCHITECTURE",
    roles: GOVERNANCE_ROLES,
    ai: {
      allowed: ["research", "summarization", "translation", "risk_flagging", "evidence_mapping", "simulation"],
      prohibited: AI_PROHIBITED_ACTIONS,
      human_review_required: HUMAN_REVIEW_REQUIRED
    },
    supreme_control: {
      nature: "constitutional_constraints_and_audit",
      personal_absolute_power: false,
      ai_absolute_power: false,
      appeal_required_for_high_impact_actions: true,
      independent_oversight_required: true
    },
    essential_services: {
      objective: ["food", "basic_shelter", "basic_healthcare", "education", "clean_water", "sanitation"],
      implementation_status: "POLICY_OBJECTIVE_REQUIRES_CAPACITY_AND_FINANCING_EVIDENCE"
    },
    environment: {
      protected_domains: ["air", "water", "soil", "forests", "oceans", "biodiversity", "climate", "space_environment"],
      implementation_status: "RESEARCH_AND_POLICY_ARCHITECTURE"
    },
    truth_boundary: {
      architecture_is_not_deployed_government: true,
      ai_output_is_not_independent_verification: true,
      policy_objective_is_not_funding_or_capacity_proof: true
    }
  };
}
