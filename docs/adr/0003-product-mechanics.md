# ADR 0003 — Product mechanics: hosted mail server + human-in-loop autonomy

- **Status:** Accepted
- **Date:** 2026-06-19
- **Context:** Grilling session. Needed to fix how Mermail connects to support email and how
  autonomously it replies, since the demo/how-it-works slide is the heart of a CX-AI deck.

## Decisions

### Mermail runs its own mail server
Mermail provides a **hosted mailbox on its own domain** that the customer uses as their
customer-support mailbox. It does **not** connect to / sit on top of Gmail or Microsoft 365.
This means support email never touches Google/Microsoft infrastructure — strengthening the
"data never leaves" privacy claim at the transport layer, not just the LLM layer.
(Custom-domain support is a likely later step, not the launch story.)

### Autonomy: draft → human approve → ramp to auto
At launch the AI **drafts** every reply and a **human approves** before send. Trusted
categories unlock **auto-send** over time as confidence is earned. Human-in-the-loop control
is framed as a feature ("automation earns trust"), not a limitation.

## Consequences

- The privacy slide can claim end-to-end data custody (own mail server + zero-retention LLM +
  per-tenant isolation + never trained on).
- The how-it-works flow: Get a Mermail support mailbox → AI triages + drafts → human approves
  → auto-send unlocks per category.
- Demo should show the draft/approve loop and the privacy data path.
- Onboarding friction = adopting a new support address; the deck should acknowledge/handle it.
