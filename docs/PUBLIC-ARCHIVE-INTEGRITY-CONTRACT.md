# Public Archive Integrity Contract

## Purpose

The Shirmani Research Institute public page presents a large digital archive, research material, external collections, and Omniverse tools. This contract keeps the public presentation useful without turning declared collection metadata into scientific verification.

## Status semantics

| Public label | Meaning | What it does not mean |
| --- | --- | --- |
| DECLARED | A collection count, title, link, or description supplied by the archive owner | Independently audited quantity or scientific proof |
| LINKED | A public destination is provided | The destination's contents have been independently verified |
| ACCESSIBLE | A destination was successfully checked by an automated/public availability check | The underlying material is authentic, complete, or scientifically validated |
| PREPARED | A verification/review packet has been assembled under the repository contract | Human/independent review has occurred |
| REVIEWED | A concrete record has passed the repository's defined review step | Universal truth or scientific consensus |
| VERIFIED | Only a record satisfying the repository's explicit independent-verification contract | Mere workflow success, queue coverage, automation, or generated output |

## Archive-count rule

Displayed quantities such as `10,000 Audios`, `4,000 Photos`, or `495 Docs` are **archive-declared collection metadata** unless an explicit evidence record says otherwise.

The interface must not silently convert:

- collection size → evidence count;
- queue size → review coverage;
- prepared packets → reviewed records;
- workflow success → scientific verification;
- generated output → independent replication.

## Research / AI rule

NLP, multimodal, sensor, or AI-generated interpretations are model outputs about observable inputs. They must retain:

1. provenance;
2. data-quality information;
3. calibration status;
4. abstention/disagreement state;
5. integrity information;
6. explicit verification status.

A model interpretation must remain `UNVERIFIED` unless the repository's independent-verification contract is actually satisfied.

## External collection rule

Google Drive, Google Photos, YouTube, Facebook, marketplace, and other external destinations should be represented as linked resources. Their presence on the public page is not itself evidence that the destination is complete, authentic, independently reviewed, or scientifically validated.

## Omniverse tools rule

Client-side AI tools must clearly distinguish:

- local UI functionality;
- external API availability;
- generated text;
- stored credentials;
- server-side processing.

An API-key notice must never imply that an AI output is independently verified.

## Accessibility and trust

Public archive cards should expose, where available:

- descriptive title;
- collection type;
- declared quantity;
- destination;
- status label;
- last checked timestamp;
- provenance/source note.

Status labels should be understandable without relying only on color.

## Operational gate

Any future automation that updates public verification status must be fail-closed:

> No packet, queue, workflow run, generated page, fingerprint, or automation success may by itself create an independent scientific `VERIFIED` state.

## Current integration target

The public interface should consume the same distinction already used by the repository's evidence and verification layers: **declared → prepared → reviewed → verified**.

This document is a presentation/governance contract. It does not assert that any archive quantity or scientific claim has been independently verified.