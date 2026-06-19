# ADR 0002 — ICP and the privacy-first mechanism

- **Status:** Accepted
- **Date:** 2026-06-19
- **Context:** Grilling session. We needed to fix who buys Mermail and what "privacy-first"
  concretely means, since both shape the entire deck.

## Decisions

### ICP
Primary buyer is **SMB SaaS support teams** (founder / head of support at 5–50 person SaaS
companies). Motion is self-serve, low ACV, high volume. They drown in support email, have no
dedicated CX tooling budget, and hold customer PII without a compliance team to protect it.

### Privacy-first mechanism
"Privacy-first" means: customer email is processed in a **per-tenant isolated** environment,
on a **zero-retention LLM API**, and is **never used to train models**.

Headline claim: *"Your customers' data is never stored, never trained on."*
Proof points: DPA, zero-retention provider contract, SOC 2 (on roadmap).

This is the wedge against Intercom Fin / Zendesk AI / Sierra, who route customer data through
retained, train-on-your-data pipelines that an SMB cannot easily vet.

## Consequences

- Deck must contrast Mermail's data path vs incumbents' data path explicitly.
- Avoid on-prem/self-hosted framing — it contradicts the self-serve SMB motion.
- "Never trained on / never stored" must be backed by a visible trust/security slide.
