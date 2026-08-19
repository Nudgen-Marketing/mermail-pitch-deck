# ADR 0005 — Agent identity and Agent Wallet

- **Status:** Accepted
- **Date:** 2026-08-04
- **Source:** Mermail Notion page “01 — Product”

## Decision

The investor deck positions Mermail as MCP infrastructure that gives AI agents:

- a dedicated email identity and mailbox;
- email tools inside the agent client;
- a user-controlled Agent Wallet for permissioned payments.

The core promise is: **Give your AI a way to act.** The initial audience is B2C AI
operators, with AI builders as the secondary audience and team workflows as an
expansion path.

## Payment narrative

The deck presents the planned Agent Wallet as autonomy without custody:

1. the user chooses Always Ask for per-action approval or bounded autonomy under a human-approved policy;
2. the agent can prepare an action, while cards and wallet keys remain outside its context;
3. Always Ask approvals expire after one action, while autonomous actions must stay inside the active policy and policy changes require human re-approval;
4. the payment completes and the confirmation returns to the agent's inbox.

Do not lead with crypto or protocol implementation details while the compliance and rail
structure remain unresolved. The underlying provider is an implementation detail and is
not named in investor materials. Do not claim controls beyond those implemented or documented.

## Consequences

- This supersedes the customer-care positioning in ADR 0001 for the primary investor deck.
- The Sui/Harbor/zkLogin/MemWal technology story is removed from the primary deck.
- Subscription remains the core business model; transaction revenue is labeled as planned
  upside subject to processor and network economics.
- Traction reporting must distinguish built email/MCP foundations from Agent Wallet adoption
  and from the policy-controlled payment flow still being completed. See ADR 0006 for the
  current traction, GTM, and funding slide decisions.
