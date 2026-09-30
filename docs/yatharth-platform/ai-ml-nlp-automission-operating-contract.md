# AI/ML/NLP/Automission Operating Contract

## Objective
Provide a fail-closed operating model for a highly automated Yatharth platform.

## Agent layers
- L0 Platform Safety and Policy Gate
- L1 Identity/Account Intake
- L2 Content Intake and NLP normalization
- L3 Semantic classification and entity linking
- L4 Search, retrieval and recommendation
- L5 Creator, education and research assistants
- L6 Commerce, freelancing and service matching
- L7 Trust, abuse, fraud and quality detection
- L8 Verification and evidence mapping
- L9 Customer support and dispute triage
- L10 Automission Supervisor
- L11 Federation and integration agents
- L12 Continuous audit, resilience and recovery

## Required operating properties
1. Every consequential automated action has an auditable event.
2. Agents use least-privilege credentials and scoped tools.
3. Sensitive secrets never enter prompts, logs, issues or public content.
4. Automation cannot mark a claim independently verified merely because an AI model, workflow or CI check succeeded.
5. Models may recommend; policy gates enforce allowed actions.
6. Users receive understandable reasons and appeal routes for consequential moderation decisions.
7. Financial and legal actions are subject to applicable law and appropriate human oversight.
8. Model outputs are treated as fallible and can be challenged.
9. Failures are quarantined rather than silently propagated.
10. Continuous audit can stop or degrade automation when safety or integrity contracts fail.

## Status vocabulary
PLANNED -> BUILT -> TESTED -> STAGED -> LIVE -> AUTONOMOUS

A module must not be represented as LIVE or AUTONOMOUS without deployment evidence.

## Core loop
Observe -> classify -> reason -> act within policy -> record -> evaluate -> recover -> learn from approved feedback.

## Human agency
The platform is designed to increase access, knowledge, opportunity and user control. It must not intentionally exploit attention, conceal material risks, or make irreversible high-impact decisions without an appropriate review path.

This is an architecture and governance contract, not evidence that the complete system is currently deployed.
