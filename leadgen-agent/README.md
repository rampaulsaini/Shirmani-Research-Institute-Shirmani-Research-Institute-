# Shirmani Local Lead Agent

A local-first, human-approved prospect CRM. Python + SQLite are the durable core; Ollama is an optional local drafting/enrichment engine.

## Safety defaults
- No web scraping, unsolicited bulk messaging, WhatsApp automation, or outbound send capability.
- Import only business contacts obtained from appropriate public/consented sources.
- AI scores are advisory and explainable; review before acting.
- Message generation creates drafts only. A human must approve the exact recipient and text in the UI/CRM before any separately configured sender is used.
- Opt-outs suppress follow-ups. Never store passwords, API tokens, payment-card data, or unnecessary personal data.

## Run locally
1. Install Python 3.10+ and Ollama from https://ollama.com.
2. In a terminal: `ollama pull llama3.2:3b`
3. Start Ollama: `ollama serve` (if it is not already running).
4. From this folder: `python lead_agent.py init`
5. Import a CSV: `python lead_agent.py import-csv prospects.csv`
6. Score records: `python lead_agent.py score`
7. Draft for a lead: `python lead_agent.py draft LEAD_ID`
8. Review: `python lead_agent.py list`

CSV columns: `business_name,website,niche,country,contact_name,email,phone,source_url,need_evidence,contact_basis`.

The database is created at `data/leads.sqlite3`. It is local and should not be committed or placed in a public web root.

## Docker
`docker compose up --build` starts the CLI container. To use Ollama installed on the host, set `OLLAMA_BASE_URL=http://host.docker.internal:11434`. The compose file includes host-gateway support. Pull the model on the host with `ollama pull llama3.2:3b`.

## WhatsApp boundary
This starter does not clone or run an unofficial WhatsApp Web client. Connect only the official WhatsApp Business Platform/Cloud API after business verification, approved templates where required, explicit opt-in, webhook signature validation, and rate-limit review. Incoming webhook messages should be stored only with the relevant consent/context; replies remain drafts until a human approves them. No WhatsApp credentials are required for local tests.

## Lead scoring
A transparent 0–100 heuristic considers niche fit, evidence of a current need, an official website/source, a usable business contact route, and a documented contact basis. Missing facts reduce the score; Ollama does not invent them.

## Tests
`python -m unittest discover -s tests -v`
