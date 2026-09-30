# Yatharth Public Platform — Completion Gate

यह gate यह सुनिश्चित करता है कि किसी capability को केवल दस्तावेज़, workflow run या AI output के आधार पर LIVE न घोषित किया जाए।

## Required lifecycle

`ARCHITECTURE → IMPLEMENTED → TESTED → SECURITY_REVIEWED → MONITORED → LIVE`

Research या high-impact modules के लिए अतिरिक्त:

`REVIEW_REQUIRED → QUALIFIED_HUMAN_REVIEW → STATUS_DECISION`

## Evidence recorded for completion

हर capability के लिए जहाँ लागू हो:

- implementation path
- automated tests
- security/privacy controls
- monitoring/observability
- rollback or disable mechanism
- user-facing status
- owner/responsibility
- known limitations
- human-review and appeal path for high-impact actions

## Fail-closed rules

- Missing evidence never becomes `LIVE`.
- AI output never becomes independent verification.
- Workflow success never becomes scientific verification.
- Architecture never becomes deployment automatically.
- A broken dependency may move a capability back to a safer status.
- Independent verification remains a separate evidence-and-human-review process.

## Current verification boundary

The public registry records `independent_verified_claims` separately from platform completion. It must remain unchanged unless a qualifying independent human review record exists.

## Continuity principle

**देखें → समझें → अलग करें → छोटा अगला कदम → करें → परिणाम दर्ज करें → सीखें → सुधारें → दोहराएँ।**

इससे “संपूर्ण संतुष्टि की निरंतरता” को पूर्णता के दावे के बजाय सत्यनिष्ठ निरीक्षण, उपयोगी कार्य और लगातार सुधार की operational discipline बनाया जाता है।
