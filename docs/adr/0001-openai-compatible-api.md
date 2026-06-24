# ADR-0001: OpenAI-Compatible API Surface

**Status:** Accepted
**Date:** 2026-06-24

## Context

Synapse needs an interface clients can adopt with near-zero friction. Two
options dominate: define a Synapse-native API, or implement OpenAI's
`/v1/chat/completions` contract.

## Options considered

- **A. Native API.** Clean schema designed around our routing primitives.
  Cost: every adopter writes a new client.
- **B. OpenAI-compatible.** Existing SDKs (`openai-python`, LangChain,
  LlamaIndex) work via a base-URL change. Cost: we inherit OpenAI's quirks and
  must track their API as it evolves.
- **C. Both.** Native API plus a translation shim.

## Decision

We chose **B**. OpenAI-compatible primary surface. Routing hints live in a
`synapse` sub-object inside the request body and in `X-Synapse-*` headers. The
`model` field accepts either `synapse-auto` (routing on) or an explicit backend
name (routing off, for testing).

## Consequences

Adoption is effectively free for anyone already using the OpenAI SDK. We must
keep up with OpenAI's schema changes, mitigated by versioning at the path
(`/v1/`) and pinning to a known-good snapshot. Streaming responses must match
OpenAI's SSE format exactly, which we verify against `openai-python` in CI.