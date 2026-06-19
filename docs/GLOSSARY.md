# Mermail Pitch Deck — Glossary

Shared vocabulary for the customer-care pitch deck. Keep terms consistent across all slides.

- **Agentic inbox** — Mermail itself: an autonomous AI that reads, triages, drafts, and
  resolves customer-care messages on a company's behalf. The AI *works* the inbox; it is not
  a mailbox provisioned *for* third-party bots. (See [ADR 0001](adr/0001-product-positioning.md).)
- **ICP** — SMB SaaS support teams (5–50 person companies), founder/head-of-support buyer,
  self-serve, low ACV. (See [ADR 0002](adr/0002-icp-and-privacy.md).)
- **Privacy-first** — Per-tenant isolation + zero-retention LLM API + never trained on
  customer data. Claim: "Your customers' data is never stored, never trained on."
- **Ticket deflection** — Share of inbound support messages resolved without a human touching
  them; Mermail's primary value metric.
- **Zero-retention** — LLM provider contract where prompts/outputs are not stored after the
  request completes.
- **Incumbents** — Intercom Fin, Zendesk AI, Sierra, Decagon: AI CX tools Mermail is measured
  against. Mermail's wedge vs them is the privacy data path.
