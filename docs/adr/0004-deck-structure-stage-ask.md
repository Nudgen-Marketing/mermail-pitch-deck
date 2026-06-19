# ADR 0004 — Stage, ask, deck structure, and visual reuse

- **Status:** Accepted
- **Date:** 2026-06-19
- **Context:** Final grilling decisions before building the customer-care pitch deck.

## Decisions

### Stage / traction
Show **live product, pre-revenue / early users**. Narrative: "built, now prove demand."
Traction slide shows the product is real + early signal, asking funds to reach revenue.

### The ask
Round and amount left as a **[TBD] placeholder**. Build the use-of-funds slide structure;
the figure is filled in after the founders decide.

### Visual + file scope
**Reuse the existing design system** (dark `#01070d` + cyan `#70eeee`, Inter) and the deck
shell (slide system, nav, animation JS, embedded base64 logo), but write a **new file**
`mermail-cx-deck.html`. The existing `mermail-pitch-deck.html` ("inboxes for agents") is
preserved untouched.

### Slide order (9 slides)
1. Cover — "The inbox that answers itself" + privacy-first agentic support inbox + hero stats
2. Problem — SMB SaaS support email drowning the team
3. Solution — hosted Mermail mailbox → AI triage → draft → human approve → auto-send ramp
4. Privacy — data-path contrast vs incumbents (the moat); own mail server + zero-retention
5. Market — AI customer service software TAM/SAM/SOM
6. Competition — vs Intercom Fin / Zendesk AI / Sierra, privacy data-path column
7. Business model — pricing tiers (self-serve, low ACV)
8. Traction — live product, early users timeline
9. Team + Ask — Nathan Nguyen & Toan Nhu + [TBD] raise + use of funds

Privacy earns a dedicated slide (#4) directly after the solution because it is the headline
differentiator.

## Consequences

- Market/competition numbers must be re-sourced for **AI customer service**, not marketing
  automation (the old deck's TAM is for a different category). Use clearly-labeled,
  defensible public figures; mark any estimate as such.
- Team slide keeps the "Co-founder only" convention from project CLAUDE.md.
- All sources remain clickable `<a target="_blank">` links.
