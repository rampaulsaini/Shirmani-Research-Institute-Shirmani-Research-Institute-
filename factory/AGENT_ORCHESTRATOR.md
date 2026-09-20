# Permanent AI-Agent Orchestration

## Agents
1. Scout Agent — discovers changed source material.
2. Curator Agent — normalizes, deduplicates and records provenance.
3. Research Agent — turns source material into research drafts.
4. Kavya Agent — produces गीत/श्लोक/सूत्र drafts.
5. Granth Agent — assembles digital महाग्रंथ editions.
6. Review Agent — checks duplication, unsupported claims and missing sources.
7. Certificate Agent — creates archival records only.
8. Publisher Agent — publishes approved artifacts to the website.
9. Monitor Agent — records failures and retries safely.

## Operating rule
Automation may generate, validate, archive and publish drafts. It must not silently convert an opinion or philosophical claim into a scientific fact.

## Human-review boundary
Public research claims that require factual or scientific verification remain marked for independent review.

## Permanent operation
GitHub Actions runs scheduled jobs and manual dispatch. Failed jobs can be retried without regenerating successful work.
