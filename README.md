# Synapse

> Cost-aware LLM router. Routes each request to the right open-source model based on query complexity, SLA tier, and budget.


## At a glance

| Metric | Synapse | Always-Best Baseline | Improvement |
|---|---|---|---|
| Cost / 1k requests (USD) | _TBD_ | _TBD_ | _TBD_ |
| p95 latency (interactive) | _TBD_ | _TBD_ | _TBD_ |
| Mean judge quality (1-5) | _TBD_ | _TBD_ | _TBD_ |
| Sustained QPS | _TBD_ | _TBD_ | _TBD_ |

_Numbers populated at v0.7. See [docs/benchmarks/results.md](docs/benchmarks/results.md) for methodology._

## How it works

Synapse sits in front of a fleet of open-source LLMs (Phi-3-mini, Mistral-7B, Llama-3-70B). Each incoming request is scored for complexity by a lightweight hybrid classifier, then routed to the smallest model that can answer it under the caller's SLA and budget constraints.

![Architecture](docs/images/architecture.png)

## Quickstart

```bash
git clone https://github.com/minurasam/synapse-router && cd synapse-router
cp .env.example .env
docker compose up --build
```

Then point any OpenAI-compatible client at `http://localhost:8000/v1`:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Authorization: Bearer dev-key-replace-me" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "synapse-auto",
    "messages": [{"role": "user", "content": "What is 2+2?"}]
  }'
```

The response includes `X-Synapse-Routed-Model` and `X-Synapse-Complexity-Score` headers showing the routing decision.

## Documentation

- [Architecture](docs/architecture.md)
- [Routing algorithm](docs/routing.md)
- [Classifier design](docs/classifier.md)
- [API reference](docs/api.md)
- [Deployment](docs/deployment.md)
- [Architecture Decision Records](docs/adr/)
- [Benchmarks](docs/benchmarks/results.md)

## Status

Under active development. See [ROADMAP.md](ROADMAP.md) for milestones.

## License

MIT