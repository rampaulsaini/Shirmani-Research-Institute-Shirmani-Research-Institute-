# Claim–Evidence–Formulation Protocol

## Purpose

This protocol defines how the Shirmani Research Institute agent should process a statement that asks for truth, proof, comparison, formulation, or computation.

## Output contract

```json
{
  "claim": "...",
  "claim_type": "empirical|mathematical|historical|textual|philosophical|computational",
  "definitions": [],
  "formulation": {"logic": [], "equations": [], "algorithm": []},
  "evidence": [],
  "computation": [],
  "comparison": [],
  "result": {"status": "supported|contradicted|unresolved|hypothesis|not_testable", "reason": "..."},
  "limitations": [],
  "provenance": []
}
```

## Evidence statuses

- **supported** — the supplied evidence and method support the bounded claim.
- **contradicted** — reliable evidence or a valid derivation conflicts with the bounded claim.
- **unresolved** — available evidence is insufficient or conflicting.
- **hypothesis** — a meaningful proposition proposed for testing but not established.
- **not_testable** — the claim is outside the available empirical/formal test method.

## Separation of domains

### Mathematics
Use definitions, axioms, transformations, symbolic derivations, numerical checks, and counterexamples.

### Science
Use operational definitions, measurements, reproducible methods, uncertainty, controls, and independent evidence.

### History/textual research
Separate primary text, translation, commentary, provenance, dating, and later interpretation.

### Philosophy
Preserve philosophical arguments as arguments. Do not silently convert a philosophical proposition into an empirical fact.

### User-authored framework
Terms such as “निष्पक्ष समझ”, “शमीकरण यथार्थ सिद्धांत”, “यथार्थ युग”, “हृदय दृष्टिकोण”, and “मस्तक दृष्टिकोण” may be modeled as explicit concepts/hypotheses. The system can test internal consistency, compare them with other frameworks, formalize definitions, and identify consequences, but must not claim independent scientific validation without appropriate evidence.

## “Quantum / infinity / ultra” rule

Words such as “Quantum”, “Infinity”, “Ultra”, or “Mega” are not proof methods by themselves.

When such a method is requested, the agent must translate the request into a concrete method:
- quantum algorithm or quantum formalism, if genuinely applicable;
- asymptotic/infinite-limit mathematics, if applicable;
- high-precision numerical computation, if applicable;
- otherwise state that the requested label has no defined evidentiary meaning for that claim.

## Comparison rule

Comparisons should expose common definitions, differences, supporting evidence, counter-evidence, assumptions, predictions/consequences, and unresolved questions. No option should be declared superior merely because it matches a preferred framework.

## Reproducibility

Every computation should record input, formula/algorithm, code version or hash, runtime parameters, output, and limitations.

## Core principle

**स्पष्टता > प्रभावशाली भाषा; प्रमाण > दावा; पुनरुत्पादन > अनुमान; तुलना > पूर्वाग्रह; निष्कर्ष की सीमा > अतिनिश्चितता।**
