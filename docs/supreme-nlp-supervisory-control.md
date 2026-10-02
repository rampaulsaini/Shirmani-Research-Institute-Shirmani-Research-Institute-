# SHIRMANI Supreme NLP Supervisory Control

## Purpose
Provide one deterministic supervisory gate above the existing Supreme NLP health, benchmark and Ultra Mega Infinity Quantum Automission controllers.

The supervisor does not replace those controls. It reconciles their results and exposes a single fail-closed operational state.

## Control graph
Health → Benchmark Contract → Orchestrator → Supervisor → Telemetry

The supervisor must never convert workflow success into model accuracy, confidence into truth, UNVERIFIED evidence into VERIFIED, or bypass governance/provenance/regression gates. Production self-modification and irreversible, financial or high-impact actions remain authorization-gated.

## State rule
- BLOCKED: a required controller fails or a required artifact is missing.
- REVIEW: controllers run but a material review condition is reported.
- UNVERIFIED: deterministic controls pass, but independent verification evidence is absent.
- VERIFIED: only permitted when every required verification input explicitly reports VERIFIED and independent verification evidence is present.

The normal Automission operating state is therefore UNVERIFIED, not falsely VERIFIED.

## Five-minute role
Every cycle executes the existing deterministic health controller, benchmark/self-improvement policy and architecture orchestrator; reconciles their exit codes and declared states; emits machine-readable telemetry; and fails closed on missing evidence or controller failure.

Expensive training, external data acquisition and high-impact actions remain separately authorized.

## Signal-language boundary
Instrumented biological, plant, environmental or non-living signals can be transformed into model patterns and plain-language descriptions. The supervisor preserves the boundary between measured signal, detected pattern, inference, interpretation, confidence, provenance, alternatives and unknowns. It does not treat a signal as proof of subjective feeling or consciousness.
