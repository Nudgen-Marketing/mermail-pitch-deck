# Mermail — Investor Pitch Deck

Investor pitch deck and brand design assets for [Mermail](https://mermail.app) — email identity and controlled payments for AI agents.

## Contents

| File / Folder | Description |
| :--- | :--- |
| [`mermail-pitch-deck.html`](file:///Users/mac/Projects/mermail-pitch-deck/mermail-pitch-deck.html) | Single-file, self-contained interactive investor pitch deck. |
| [`one-pager.html`](one-pager.html) | Responsive investor one-pager based on the Colosseum deck, with a single-sheet print layout. |
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

## UII SIP & SHARE

[`uii-sip-share/index.html`](uii-sip-share/index.html) is a six-slide Vietnamese deck for UII SIP & SHARE #4 (1 October 2026), “Building Your Startup Moat in the Age of AI.” It covers Mermail’s product, a sales workflow, its moat thesis, pilot measures, and the Team slide from the public pitch deck.

The GitHub Pages workflow validates and packages a preview on pull requests, relevant `main` pushes, or manual dispatch, including `/uii-sip-share/` alongside the existing routes. After deployment, open [pitching.mermail.app/uii-sip-share](https://pitching.mermail.app/uii-sip-share). Validate locally with `python3 scripts/check-uii-sip-share.py`. Use arrow keys, Page Up/Down, swipe, or the on-screen buttons; print for a six-page landscape handout.

## RTC

[`rtc/index.html`](rtc/index.html) is the pitch revised from Josip’s 30 September 2026 feedback: a clear email-and-wallet explanation, readable emoji flow, sourced ecosystem context, focused pilot validation, and outcome-oriented team evidence. See [feedback and evidence notes](docs/rtc-feedback.md).

The GitHub Pages workflow validates the deck and uploads a preview artifact on pull requests, relevant `main` pushes, or manual dispatch. It publishes the deck at [pitching.mermail.app/rtc](https://pitching.mermail.app/rtc) after deployment while preserving the existing routes. Run `python3 scripts/check-rtc.py` locally before publishing.

## DS2S

[`ds2s/index.html`](ds2s/index.html) is the 12-slide DS2S deck based on Colosseum, with B2B/B2C customer segments and updated acquisition channels on the GTM slide. The Ask follows Team and covers brand awareness, community, user-generated content, and customer research. It is served at `/ds2s/` after deployment.

## Colosseum

[`colosseum/index.html`](colosseum/index.html) is the default deck, served at `/` and `/colosseum/` after deployment. Its ten slides cover the product, problem, demo, timing, traction, competition and moat thesis, go-to-market, team, and a closing ask for angel investor introductions, design partners, and ecosystem connections. It omits the fundraising amount and allocation; the original investor deck remains available at `/mermail-pitch-deck.html`. Slide 4 embeds the YouTube product demo and requests 1.5× playback through the IFrame API. Serve the deck over HTTP(S) for video playback; the embedded demo requires internet access and pauses when leaving the slide.

## Investor One-Pager

Open [`one-pager.html`](one-pager.html) directly in a browser. It uses an embedded logo and system font fallbacks; Google Fonts enhances typography when online. Print or save to PDF using A4 paper, 100% scale, and browser headers/footers disabled for a single-sheet overview.

The content follows the Colosseum deck: traction is a company-reported first-25-days snapshot, and the ask is for investor introductions, pilot users, and community builders. The market forecast is commerce volume, not a Mermail revenue estimate. The one-pager does not import the main deck’s fundraising amount.

The GitHub Pages workflow triggers when this HTML changes on `main` and includes it in the deployed artifact at `/one-pager.html`. It also remains available through the workflow’s manual trigger.

## About Mermail

Mermail gives an AI agent its own email inbox and a user-controlled Agent Wallet. Through MCP, agents can register, verify, buy, book, manage billing, and preserve confirmations without borrowing the user's inbox or handing reusable payment credentials to the agent.

- **Website:** [mermail.app](https://mermail.app)
- **Founders:** Nathan Nguyen & Toan Nhu (Co-founders)
- **Design Language:** HSL tailored dark neutrals with emerald/cyan accent (`#70eeee`).

## Arc

[`arc/index.html`](arc/index.html) is the 13-slide October 2, 2026 Vietnam Office Hours deck. It covers Agent Stack Wallets, CCTP funding, Agent Marketplace discovery, and the proposed MPP inbox-purchase flow on Arc. Existing implementation notes support Arc x402 and Base MPP; Arc MPP and directory acceptance are presented as milestones. The Pages build includes `/arc/`.
