# ADR 0001 — Product positioning: Mermail is the AI that works the inbox

- **Status:** Accepted
- **Date:** 2026-06-19
- **Context:** Grilling session for a new pitch deck. The live deck positioned Mermail as
  "real inboxes for agents" (mailbox infrastructure so third-party bots can receive OTPs,
  receipts, audit trails). The new brief asks for a "privacy-first agentic inbox for AI"
  aimed at a customer-care use case.

## Decision

Mermail **is** the agent. It is an autonomous AI inbox that reads, triages, drafts, and
resolves customer-care email/messages on a company's behalf. The customer-care use case is
the **headline product**, not one downstream example. Privacy-first is a core differentiator,
not a footnote.

This is a deliberate pivot away from the "infrastructure mailbox for third-party bots"
narrative of the previous deck.

## Consequences

- The buyer/user is a support/CX team (SMB SaaS), not a developer building agents.
- Value props center on ticket deflection, instant replies, and privacy-safe handling.
- The existing deck's slides (OTP/verification infra) are largely replaced, not edited.
- "Privacy-first" must be substantiated, not asserted (see later ADRs).
