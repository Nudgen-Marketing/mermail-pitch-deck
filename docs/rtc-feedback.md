# RTC pitch deck

Source: [Pitching with Josip, 30 September 2026](https://app.notion.com/p/Pitching-with-Josip-3eb6fc4a184d80f49ba8f7f0322b0db5?source=copy_link).

The RTC variant lives in `rtc/index.html`. It is independent of the existing decks.

## Feedback applied

- Use “Inbox and wallet for agents” and explain email confirmations, verification, and receipts early.
- Remove the tiny gray cover tagline, redundant slide labels, and staccato sales copy.
- Replace the unreadable embedded video with a large shopping → email → payment flow, limited to supported services.
- Compare annual web-visit growth on one scale: Google Search −1.41% and the top 10 AI chatbots +80.92%, April 2024–March 2025 versus the prior year. Do not imply that AI has more absolute traffic or that the comparison proves displacement.
- Put payment volume before transaction count. Label the figures as x402 ecosystem activity, separate from Mermail traction.
- Remove email totals and total signups from the traction story. Focus on the reported GTM workflow and the pilot outcomes to measure.
- Remove the broad $3–5 trillion market forecast. Explain the buyer and revenue model instead.
- Lead team evidence with the existing Nimbus/LP Agent $100K ARR outcome, explicitly a prior business. Explain Tiki for an international audience. Keep both founders titled “Co-founder”.
- Make the ask concrete and remove the motivational closing slogan.

## Evidence boundaries

The meeting's 30% email-confirmation example and suggested team achievements are not verified statistics. They are not used as facts.

The [Solana Foundation article, 5 August 2026](https://solana.com/news/webinar-recap-agentic-payments) reports roughly 200 million x402 transactions and $50 billion in volume. These are rounded ecosystem figures, not Mermail volume or activity “since August”.

Slide 5 now reproduces the selected channels from https://chatgpt-vs-google.com/ using its exact embedded `dataView.chart` arrays, retrieved 2026-10-01. The reproducible snapshot is `rtc/traffic-data.json`. All series cover June 2025–September 2026 on a shared zero-based 0–600M monthly visitor scale. Direct uses `directVisitors`, Google uses `googleVisitors` alone (the original chart's Search sums Google, Bing and DuckDuckGo), and AI sums `chatgptVisitors`, `perplexityVisitors`, and `geminiVisitors` as in the original channel chart. These are traffic sources to sites measured by Ahrefs Web Analytics, not global visits to the AI/search platforms. The page's 74,752 fixed-cohort statement applies explicitly to the separate total-traffic trend; the channel chart is therefore described only as the Ahrefs sample. Latest legend values are September 2026.

The repository does not establish current paying-customer, deployed-agent, completed-payment, or repeat-usage counts. Older wallet-user snapshots differ, so they are not promoted to current traction. Pilot measures are goals, not achieved results. Nathan's quantitative career outcomes remain unprovided. The prior-business ARR claim is company-reported in the existing deck, not independently audited.

## Build and publication

- Run `python3 scripts/check-rtc.py` for dependency-free release checks.
- `deploy-mermail-pitch-deck.yml` checks pull requests and relevant pushes to `main`, supports manual runs, uploads an `rtc-pitch-deck` preview artifact containing `rtc/` and `assets/`, and includes `rtc/` in the complete Pages artifact while running the same checks. It remains the single publisher, preserving `/`, `/colosseum/`, `/ds2s/`, the original deck, and the one-pager.
- After an approved push to `main` and successful Pages deployment, the deck is served at `https://pitching.mermail.app/rtc` (Pages redirects to `/rtc/`).
- To preview locally, serve the repository root with `python3 -m http.server 8765` and open `http://localhost:8765/rtc/`.
