# Shirmani Social API

Production-backend foundation for the Yatharth public-platform surfaces.

## Setup
1. Copy `.env.example` to `.env`.
2. Configure `DATABASE_URL` and a long random `JWT_SECRET`.
3. Apply `sql/schema.sql` to PostgreSQL.
4. Run `npm install` and `npm start`.

The schema provides the current API tables plus extensible primitives for social interactions, notifications, media metadata, learning, work fulfilment, disputes and independent-review records.

## Readiness
This repository contains an API foundation and database contract. It does **not** claim that payments, object storage, employment, dispute decisions, AI workers, or independent verification are live. Those require provider integration, deployment evidence and/or qualified independent review.

## Safety
Never place credentials, payment secrets, API keys or private user data in Git commits, issues or chat. High-impact moderation, financial, dispute and verification decisions require appropriate human oversight and appeal.
