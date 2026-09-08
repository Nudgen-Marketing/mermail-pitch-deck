# Mermail — Investor Pitch Deck

Investor pitch deck and brand design assets for [Mermail](https://mermail.app) — email identity and controlled payments for AI agents.

## Contents

| File / Folder | Description |
| :--- | :--- |
| [`mermail-pitch-deck.html`](file:///Users/mac/Projects/mermail-pitch-deck/mermail-pitch-deck.html) | Single-file, self-contained interactive investor pitch deck. |
| [`DESIGN-SYSTEM-MERMAIL.md`](file:///Users/mac/Projects/mermail-pitch-deck/DESIGN-SYSTEM-MERMAIL.md) | Mermail brand and UI design system token reference. |
| [`assets/`](file:///Users/mac/Projects/mermail-pitch-deck/assets) | Canonical landing-page logo and mark, founder headshots, avatars, and OpenGraph sharing images. |

## Interactive Pitch Deck

The investor pitch deck (`mermail-pitch-deck.html`) is fully self-contained with no external local dependencies. The canonical Mermail landing-page logo and image assets are embedded as base64 data, and fonts are loaded dynamically from the Google Fonts CDN. You can open it in any modern web browser without a local web server.

### Slide Structure (9 Slides)

1. **Cover** — “Give your AI a way to act” as infrastructure for AiFi.
2. **The Web Is No Longer Human-First** — From searching the web, to asking AI, to delegating outcomes to agents.
3. **The Product** — One Mermail account combines identity, payment, an audit trail, and instant revocation.
4. **Sales Outreach Use Case** — An agent finds prospects, buys enrichment, sends personalized outreach from its own inbox, and returns warm leads.
5. **Why Now** — MCP, network payment programs, and the arrival of live agentic-commerce rails.
6. **Traction** — Identity is live; the next proof is repeat jobs, own-money top-ups, and paid accounts.
7. **Go-to-Market** — Reach AI power users, embed in their existing tools, drive real transactions, and turn completed tasks into growth.
8. **Funding Allocation** — $250K pre-seed, eight-month runway, six allocation buckets, and proof milestones.
9. **Team & Connect** — Infrastructure builders for AiFi, co-founders Nathan Nguyen and Toan Nhu, and a QR code to try Mermail.

## Borneo Demo Day

[`borneo-demo-day/index.html`](borneo-demo-day/index.html) is the event deck, served at `/borneo-demo-day/` after deployment. Its ten slides cover the product, problem, demo, timing, traction, competition and moat thesis, go-to-market, team, and a closing ask for angel investor introductions, design partners, and ecosystem connections. It omits the fundraising amount and allocation; the main investor deck remains separate. Slide 4 embeds the YouTube product demo and requests 1.5× playback through the IFrame API. Serve the deck over HTTP(S) for video playback; the embedded demo requires internet access and pauses when leaving the slide.

## About Mermail

Mermail gives an AI agent its own email inbox and a user-controlled Agent Wallet. Through MCP, agents can register, verify, buy, book, manage billing, and preserve confirmations without borrowing the user's inbox or handing reusable payment credentials to the agent.

- **Website:** [mermail.app](https://mermail.app)
- **Founders:** Nathan Nguyen & Toan Nhu (Co-founders)
- **Design Language:** HSL tailored dark neutrals with emerald/cyan accent (`#70eeee`).
