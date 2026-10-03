# Personal Claim / Provenance Verification Gate — v1

This gate separates authorship/provenance, provenance of user-supplied media, and independent verification of broader philosophical, experiential, or empirical claims.

## Safety and integrity boundary

Personal photographs, eyes, face appearance, voice, conversation style, handwriting, or other personal material may be preserved as user-supplied provenance evidence, but automation must not infer identity from biometric characteristics or create biometric templates.

A photograph matching a person does not by itself prove that the person authored every proposition associated with the photograph.

## Claim classes

- AUTHORSHIP_PROVENANCE
- USER_SUPPLIED_MEDIA_PROVENANCE
- IDENTITY_CLAIM
- PHILOSOPHICAL_OR_EXPERIENTIAL_CLAIM
- EMPIRICAL_CLAIM

## Fail-closed rules

- Repository ownership is provenance evidence, not absolute proof of a person's offline identity.
- User-supplied face/eye/voice material is provenance evidence only; it must not be converted into a biometric identity score.
- A statement such as “मैं शिरोमणि हूँ” is not independently verified merely because it appears in the author's source.
- Philosophical, spiritual, metaphysical, or experiential claims require their own operational definitions and independent tests.
- Automation may classify evidence and detect missing requirements, but it must not manufacture an independent identity or truth decision.

## Intended result

The gate produces one of: PROVENANCE-SUPPORTED, PENDING_INDEPENDENT_REVIEW, NOT_VERIFIED, or CONTRADICTED.

It must never silently convert a personal claim into universal truth.
