# Yatharth Music AI — Shirmani Hub Integration Contract

## Current verified boundary

The Shirmani public hub already links to the Yatharth Music AI public interface and repository.

The Yatharth Music AI repository provides:
- FastAPI application;
- ACE-Step integration;
- durable task state and recovery;
- health/readiness endpoints;
- retry and provider recovery;
- mobile-first public UI;
- a Colab development/test notebook.

## What is **not** yet 24/7 production integration

A Colab runtime plus a `trycloudflare.com` quick tunnel is temporary development infrastructure. Its URL changes and disappears when the runtime stops.

Therefore:
- temporary public URL ≠ permanent hosting;
- GitHub repository ≠ running GPU service;
- `/api/health` liveness ≠ ACE-Step generation readiness;
- GitHub Actions success ≠ successful public music generation;
- a menu link ≠ completed cross-repository runtime integration.

## Required production chain

`Public Hub → Production Music API → Durable Queue → Persistent GPU/ACE-Step → Object Storage → Monitoring → Recovery → Evidence`

Production should use:
1. persistent GPU hosting;
2. HTTPS/reverse proxy;
3. durable queue/state;
4. object storage for generated audio;
5. authentication and quotas;
6. monitoring and restart policy;
7. secrets outside source code;
8. backup and recovery;
9. abuse/rate controls;
10. real generation smoke tests from the public endpoint.

## Automation policy

The system may automatically:
- inspect health;
- retry transient failures;
- recover durable queued work;
- publish status telemetry;
- prepare content and marketing artifacts.

Production code/model upgrades should remain versioned, tested and release-gated. No silent uncontrolled self-modification is treated as a reliability feature.

## Income boundary

The Hub may promote Music AI, digital products and services, but revenue, sales, ad delivery or audience scale must only be reported from actual platform evidence.

## Current test evidence

The repository notebook explicitly sets `MPLBACKEND=Agg` before ACE-Step startup and waits for the ACE-Step health endpoint before exposing its temporary public link. If a Colab run still shows the `matplotlib_inline` backend error, that run is executing an older notebook state or did not restart from the current notebook.

