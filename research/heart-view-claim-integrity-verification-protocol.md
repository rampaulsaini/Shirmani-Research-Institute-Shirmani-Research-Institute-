# SHIRMANI Heart-View Claim Integrity & Verification Protocol

## Purpose

This protocol adds a fail-closed verification boundary for any person who makes a claim such as:

> "I am Shiromani."

The system must distinguish a person's self-description from an independently verified claim. It must never convert confidence, intelligence, eloquence, popularity, appearance, spiritual language, or workflow success into proof of a universal or metaphysical claim.

## Core principle

A person may state an identity or experience in their own words. The system records that statement faithfully, but does not declare a metaphysical identity as objectively proven.

The gate evaluates only operationally testable dimensions:

1. provenance of the statement;
2. clarity of the claim and its operational meaning;
3. consistency across time and media;
4. evidence that can be independently inspected;
5. counter-evidence and disconfirming observations;
6. reproducibility of testable observations;
7. absence of coercive or authority-based promotion;
8. reviewer independence and provenance;
9. uncertainty and abstention when evidence is insufficient;
10. distinction between personal experience and universal claim.

## Heart-View test boundary

The project may preserve and evaluate the user's stated Heart-View/Yatharth terminology, but the gate must not silently transform that terminology into an externally established scientific fact.

For claims concerning "संपूर्ण संतुष्टि की निरंतरता", universal human welfare, or a transition from a "मन/मस्तक/बुद्धि" viewpoint to a "हृदय के दृष्टिकोण", the gate asks:

- What exactly is being claimed?
- What observable behavior or outcome would count as evidence?
- What evidence could show the claim is wrong or incomplete?
- Can an independent reviewer reproduce the relevant observation?
- Are contrary observations disclosed rather than suppressed?
- Is the claim being presented as a personal realization, a philosophical framework, or an externally testable universal proposition?

## Anti-deception boundary

The following are NOT sufficient for VERIFIED status:

- saying "I am Shiromani";
- intelligence, cleverness, rhetoric, charisma or popularity;
- a photograph, facial appearance, eyes, clothing or perceived expression;
- a voice or speaking style by itself;
- number of followers;
- number of GitHub workflow runs;
- AI-generated agreement;
- self-authored certificates;
- absence of criticism;
- a model's confidence.

The system must not infer moral character, spiritual attainment, or universal truth from appearance.

## Personal multimodal provenance

Where the claimant voluntarily provides photographs, video, audio, or transcripts, these may be attached as provenance records to establish what the claimant actually said or presented.

They are evidence of the media/source and context—not proof of a metaphysical status.

For every personal media item, record:

- consent/status of authorization;
- source and capture context when available;
- timestamp when available;
- cryptographic hash;
- transcript or description;
- what proposition the media actually supports;
- uncertainty/limitations.

## Private-question layer

Questions intended to distinguish a Heart-View practical orientation from a purely self-serving or authority-seeking interpretation should be explicit and reproducible. They should not be designed to force a desired conclusion.

Examples:

1. Does the claimant allow their own central claim to be questioned?
2. What evidence would change or weaken the claimant's conclusion?
3. How are people who disagree treated?
4. Is personal benefit being confused with universal benefit?
5. Does the claimant distinguish experience from externally testable fact?
6. Are counter-examples preserved?
7. Can another person independently inspect the relevant evidence?
8. Does the framework permit abstention where evidence is insufficient?
9. Does the claimant claim authority over others, or invite independent examination?
10. Are statements about humanity's history presented as hypotheses, interpretations, or documented facts?

## Decision states

- SELF_DECLARED: the person made the claim.
- PROVENANCE_CONFIRMED: the source/media is sufficiently attributable.
- EVIDENCE-SUPPORTED: specified evidence supports one or more operational propositions.
- PENDING_INDEPENDENT_REVIEW: the claim has not yet received independent review.
- VERIFIED: reserved for an operationally defined claim that satisfies the project's independent verification protocol and explicit independent reviewer decision.
- NOT_VERIFIED: evidence does not currently satisfy the gate.
- CONTRADICTED: reliable evidence conflicts with the operational proposition.
- INCONCLUSIVE: evidence is insufficient or materially ambiguous.

## Fail-closed rule

No automation may declare a metaphysical or universal identity "verified" merely because a workflow passed.

workflow success != independent verification

A VERIFIED decision requires explicit reviewer provenance and the complete evidence/test/counter-evidence/audit chain already required by the repository's independent-verification protocol.

## Preservation rule

The claimant's original wording may be preserved verbatim as source material. Interpretation, operationalization, testing and verification must be stored separately so that the original statement is not silently rewritten.
