# Independent Verification Review Packets

The repository keeps deterministic generation separate from human/audit verification.

## Purpose

`factory/verification_review_packet.py` creates a small, deterministic review packet from:

- `generated/independent-verification-queue.jsonl`
- `generated/independent-verification-registry.jsonl`

Each packet item contains the exact `task_id`, source IDs, verification questions, and a SHA-256 hash of the current queue task. The packet also contains an empty review template.

## Usage

From the repository root:

```bash
python3 factory/verification_review_packet.py --batch-size 25 --offset 0
```

The first packet covers queue positions 1–25. The next packet can be generated with:

```bash
python3 factory/verification_review_packet.py --batch-size 25 --offset 25
```

## Safety boundary

Packet generation is **not verification**.

It must never:

- invent a reviewer;
- invent evidence or quotations;
- invent a countercase;
- invent a reproduction/test result;
- change `QUEUED` to `REVIEWED`;
- change `NOT_VERIFIED` to `VERIFIED`.

The existing promotion gate remains authoritative. A record can become `VERIFIED` only after the repository's complete independent-review requirements are actually satisfied.

## Continuity

This layer is deliberately non-destructive. It does not modify the protected user-source record and does not rewrite existing review records.
