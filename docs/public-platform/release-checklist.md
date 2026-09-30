# Public Platform Release Checklist

## Engineering
- [ ] Server syntax check passes
- [ ] API contract tests pass
- [ ] Smoke tests pass
- [ ] Database migration reviewed
- [ ] Backups and restore test completed
- [ ] Monitoring and alerts active
- [ ] Rollback tested

## Security and privacy
- [ ] Production HTTPS configured
- [ ] Secrets are external to source control
- [ ] Authentication and authorization tested
- [ ] Rate limiting and abuse controls active
- [ ] Privacy export/deletion/correction tested
- [ ] Sensitive data exposure checks completed
- [ ] Audit logging active

## Product modules
- [ ] Account/profile
- [ ] Social publishing
- [ ] Media
- [ ] Digital Store
- [ ] Freelancing
- [ ] Employment
- [ ] Education
- [ ] Research
- [ ] Yatharth AI / AI Music
- [ ] Trust, complaints and appeals
- [ ] Marketplace orders and support

A checked module means the release gate was tested for that release; it does not automatically mean the module is globally available.

## Payments
- [ ] Provider configuration is active
- [ ] Signed webhook verification works
- [ ] Refund/cancellation behavior tested
- [ ] Payout controls tested
- [ ] Fraud/chargeback handling documented

## AI / Automission
- [ ] Agent identities and scopes are registered
- [ ] Task events are auditable
- [ ] Retry/cancel behavior is bounded
- [ ] High-impact actions have human review
- [ ] Model/provider failure recovery tested
- [ ] AI output provenance is retained

## Research truth boundary
- [ ] Author source is preserved
- [ ] Claims are separated from evidence
- [ ] Counter-evidence is represented where applicable
- [ ] Independent review status is explicit
- [ ] No CI/workflow result is presented as independent verification

## Release decision

Only after the applicable checks are satisfied may an authorized maintainer perform the real deployment. A successful GitHub check is a validation signal, not proof of production availability or independent verification.
