# Shirmani Social API

This service is the production-backend foundation for the global social-platform frontend.

## Run
1. Copy `.env.example` to `.env`.
2. Set `DATABASE_URL` and a long random `JWT_SECRET`.
3. Apply `schema.sql` to PostgreSQL.
4. Run `npm install` and `npm start`.

## API
- `GET /health`
- `POST /v1/auth/register`
- `POST /v1/auth/login`
- `GET /v1/profile/:id`
- `GET /v1/feed`
- `POST /v1/posts` (Bearer token)
- `POST /v1/self-interviews` (Bearer token)

## Production gate
The repository does not claim that this backend is deployed. Before public exposure, configure HTTPS/TLS, secret management, backups, database migrations, monitoring, abuse/moderation workflows, account recovery, email verification, privacy/deletion workflows, object storage/media processing, and security testing.

The API deliberately does not create or claim followers, views, payments, income, employment, testimonials or real-world verification without evidence.
