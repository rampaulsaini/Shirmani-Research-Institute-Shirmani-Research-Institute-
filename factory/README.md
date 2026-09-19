# Omniverse Research Factory

यह folder केंद्रीय Hub की मशीनरी है।

## Execution order
1. source-registry.py — सभी configured repositories का canonical registry
2. build_factory.py — source collection और traceable corpus
3. agent_runner.py — registered agent stages का runtime state
4. agent_supervisor.py — supervisor/status
5. GitHub Actions — scheduled/triggered execution

## Design rule
Generated products कभी canonical source corpus के input नहीं बनते। हर research draft में source provenance और independent verification requirement रहती है।

## Free-first
यह base orchestration किसी paid API पर निर्भर नहीं है। वास्तविक semantic AI के लिए बाद में local/open model adapters जोड़े जा सकते हैं।
