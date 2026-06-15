# Pitch Deck Project

## Project
Mermail (mermail.app) — AI-powered retention email workflow platform for SMB SaaS.

## Primary File
`mermail-pitch-deck.html` — single self-contained HTML pitch deck (logo base64-embedded, no external asset dependencies except Google Fonts CDN).

## Design System
Dark neutral + emerald accent. Tokens defined in `:root`:
- Background: `#01070d`, Foreground: `#ffffff`
- Accent: `#70eeee` (success), `#70eeee` (success-strong)
- Surfaces: `#06111f`, `#081629`, `#102a3b`
- Fonts: Inter (headings and body)
- Global scale: `html { font-size: 120%; }`

Full design system doc: `DESIGN-SYSTEM-MERMAIL.md`

## Slides (9 total)
1. Cover — one-liner + hero stats
2. Problem — churn pain points
3. Solution — 3-step workflow (Integrate → Detect → Automate)
4. Market — animated Venn diagram (TAM/SAM/SOM)
5. Traction — timeline (problem validation → MVP beta)
6. Competition — comparison table
7. Business Model — pricing tiers + unit economics
8. Team — Nathan Nguyen & Toan Nhu (Co-founders)
9. Ask — raise amount + use of funds

## Founders
- **Nathan Nguyen** — Co-founder. Data Scientist at Webjet.com.au.
- **Toan Nhu** — Co-founder. Principal Software Engineer at VinGroup, ex Senior Data Engineer at Tiki.

## Market Numbers (verified)
- TAM: $6.65B — Grand View Research, Marketing Automation Software Market, 2025
- SAM: $1.2B — IMARC Group, Email Marketing Software Market, 2024
- CAGR: 15.3%

## Key Conventions
- No CEO/CTO titles — both listed as "Co-founder" only
- All sources are clickable `<a target="_blank">` links
- Animations respect `prefers-reduced-motion`
- Logo is embedded as base64 — do not revert to file path references
