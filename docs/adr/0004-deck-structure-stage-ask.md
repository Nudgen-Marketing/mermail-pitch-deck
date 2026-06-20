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

## Update — 2026-06-19 (post-build iteration)

Founder revisions after reviewing the live deck:
- **Slide 4 is now "Built to Scale"** (agent inboxes scale, human email inboxes don't), not
  the privacy contrast. Privacy now lives on the cover stat ("Zero data stored/trained on")
  and the competition table's data-path rows. Consider reinstating a dedicated privacy slide
  if the deck has room.
- **Slide 1 (Problem)** drills into CX staffing economics: $10K–$20K & 60–90 days to train an
  agent, 30–45% attrition, linear scaling, ~4–5 FTEs for 24/7 (sourced: Plivo/McKinsey, JustCall).
- **Slide 3 (Solution)** trimmed to step titles only; step 4 = "Auto-send & track metrics".
- **Slide 5 (Market)** SOM raised from $20M to **$70M** (~5% of SAM, 5-year), with a larger ring.
- **Slide 7 (Business model)** shows a **subscription model with three tiers but no prices**.
- **Slide 8 (Traction)** dates corrected: Apr started → May building → Jun live → Q3 first revenue.
- **The ask is now $200K** (was [TBD]).
- **Competition slide dropped** — deck is now 8 slides (cover + 7), renumbered to /08. Note:
  privacy now appears **only as the cover stat** ("Zero data stored/trained on"); the dedicated
  privacy slide and the competition data-path rows are both gone. Reinstate a privacy slide if
  the "privacy-first" tagline needs on-slide support.

## Consequences

- Market/competition numbers must be re-sourced for **AI customer service**, not marketing
  automation (the old deck's TAM is for a different category). Use clearly-labeled,
  defensible public figures; mark any estimate as such.
- Team slide keeps the "Co-founder only" convention from project CLAUDE.md.
- All sources remain clickable `<a target="_blank">` links.
