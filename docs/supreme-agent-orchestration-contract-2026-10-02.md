# SHIRMANI Supreme Agent Orchestration Contract

## Purpose

Define a bounded multi-agent execution layer for AI, ML, NLP and Automission without confusing orchestration success with model accuracy or scientific verification.

## Canonical agent graph

Intake → Planner → Research → Evidence → NLP Interpreter → ML/Signal → Security → Verification → QC → Publisher → Archive → Telemetry

Agents are peers with explicit contracts. No single agent may promote an unverified claim to VERIFIED.

## Agent responsibilities

| Agent | Responsibility | Required output |
|---|---|---|
| Intake | preserve source and request | source/provenance record |
| Planner | decompose task | deterministic task plan |
| Research | retrieve/prepare evidence | evidence candidates |
| Evidence | bind claims to sources | claim-evidence links |
| NLP Interpreter | translate signals/results | plain-language interpretation |
| ML/Signal | classify/estimate measurable patterns | model/version/result |
| Security | detect unsafe or secret-bearing operations | security gate |
| Verification | independently test required claims | verification state |
| QC | validate schemas/contracts/regressions | PASS/REVIEW/BLOCKED |
| Publisher | publish only permitted artifacts | publication record |
| Archive | preserve immutable trace | archive/provenance record |
| Telemetry | measure execution health | cycle telemetry |

## State machine

REGISTERED → RUNNING → CHECKED → REVIEW → VERIFIED

Failure states:

- BLOCKED — required gate failed.
- UNVERIFIED — execution completed but independent verification is absent.
- REVIEW — evidence or results are materially ambiguous or contradictory.

No workflow-success event may promote UNVERIFIED to VERIFIED.

## Execution contract

Each cycle must carry:

- event_id
- cycle_id
- agent_id
- agent_version
- input_fingerprint
- output_fingerprint
- provenance
- status
- confidence/uncertainty where applicable
- blockers
- timestamp
- parent_event_id when applicable

## Signal-to-language boundary

For living organisms, plants, environments and non-living systems, the platform may process instrumented measurable signals. The NLP layer must state separately:

1. measured signal;
2. detected pattern;
3. model inference;
4. plain-language interpretation;
5. confidence/uncertainty;
6. evidence/provenance;
7. alternative interpretation;
8. unresolved unknowns.

The system must not represent a signal pattern as proven subjective feeling, consciousness or intention without independent evidence specifically supporting that proposition.

## Continuous improvement

A model or agent change is accepted only when:

- the task and evaluation protocol are declared;
- the dataset/version or fingerprint is recorded;
- the baseline is recorded;
- the new result is measured;
- regression checks pass;
- material limitations are recorded;
- verification state remains distinct from workflow status.

## Fail-closed controls

Missing provenance, invalid schema, failed security gate, contradictory critical evidence or missing required contract causes BLOCKED/REVIEW rather than fabricated completion.

High-impact, irreversible, financial, identity, security and external-publication actions require explicit authorization gates.

## Five-minute Automission

The five-minute cycle performs deterministic orchestration-health, contract, schema and regression checks. Expensive training, external data collection and high-impact actions are not implicitly authorized by the five-minute scheduler.

## Quality target

The system optimizes for measurable accuracy, reproducibility, traceability, latency, robustness and safe failure. “Supreme accuracy” is a target requiring benchmark evidence, not a value inserted into the system without measurement.
