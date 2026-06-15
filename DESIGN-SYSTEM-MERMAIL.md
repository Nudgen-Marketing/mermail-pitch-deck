# Mermail Design System

## 1) Design Principles

- Clarity first: every screen should help users complete a workflow quickly.
- Trust through consistency: keep spacing, typography, and controls predictable.
- Practical warmth: modern SaaS UI with calm neutrals and neon cyan action accents.
- Low-friction speed: minimize visual noise and reduce decision fatigue.

## 2) Brand Personality

- Tone: confident, helpful, direct.
- Visual feel: clean, lightweight, product-focused.
- Experience goal: users should feel guided, not overwhelmed.

## 3) Color System

Use semantic tokens over hardcoded colors.

### Core Tokens

| Token | Light | Dark | Usage |
| --- | --- | --- | --- |
| `--background` | `#ffffff` | `#01070d` | App/page background |
| `--foreground` | `#171717` | `#ffffff` | Primary text/icons |
| `--success` | `#70eeee` | `#70eeee` | Positive actions, success states |
| `--success-strong` | `#70eeee` | `#70eeee` | Highlights, emphasis, toasts |

### Supporting Palette

- Neutral UI: Tailwind slate/zinc/blue ramps for borders, muted text, and surfaces.
- Status colors:
- `Success`: neon cyan range (`neon cyan-500` to `neon cyan-700`)
- `Warning`: amber range
- `Info`: blue range
- `Error`: red range

## 4) Typography

- Primary stack: `var(--font-inter), system-ui, -apple-system, "Segoe UI", Arial, sans-serif`
- Headings: Inter emphasis (clean, modern, product-forward).
- Body/UI: Inter for readability and dense interface text.
- Hierarchy:
- `H1`: page purpose/value
- `H2`: section grouping
- `H3`: sub-section and card titles
- Body: concise supporting content

## 5) Spacing & Layout

- Base unit: 4px scale.
- Recommended rhythm:
- `4, 8, 12, 16, 24, 32, 40, 48, 64`
- Layout behavior:
- Avoid horizontal overflow on mobile.
- Keep strong vertical grouping and clear section separation.
- Prefer card-based chunking for complex workflows.

## 6) Shape, Borders, and Shadows

- Border radius:
- Inputs/buttons: `8px` to `10px`
- Cards/panels: `12px` to `16px`
- Borders:
- Use subtle neutral borders for structure, not decoration.
- Shadows:
- Prefer soft depth (`shadow-sm`/`shadow-md`) over heavy elevation.

## 7) Motion

Motion should communicate state changes, never distract.

- Standard transition window: `150ms` to `300ms`.
- Existing patterns to keep:
- `fadeInUp`, `fadeSlideUp`, `tiltIn` for content reveal
- Gentle floating/pulse for selected decorative accents
- Accessibility:
- Respect `prefers-reduced-motion`.
- Avoid layout-shifting hover animations.

## 8) Component Guidance

### Buttons

- Primary CTA: high contrast (`bg-foreground text-background`) or neon cyan success when action is positive.
- Secondary actions: outline/ghost variants with clear hover + focus states.
- Loading state: spinner + disabled interaction.

### Inputs

- Consistent height and radius.
- Clear focus ring (`focus-visible`) with accessible contrast.
- Error/validation states must be explicit and text-supported.

### Cards and Panels

- Use for grouping campaign, analytics, and settings sections.
- Keep header + content + action zones visually distinct.

### Status Chips/Badges

- Use semantic colors consistently:
- draft (neutral), scheduled (amber), running/info (blue), sent/success (neon cyan), stopped/error (red).

## 9) Accessibility Rules

- Minimum text contrast: WCAG AA (4.5:1 for normal text).
- Keyboard-first support:
- Visible focus states on all interactive controls.
- Logical tab order in forms, dialogs, and dashboards.
- Avoid color-only meaning; pair with label/icon/text.

## 10) Content & UX Tone

- Write short, action-oriented UI copy.
- Prefer verbs in CTAs: `Create`, `Launch`, `Save`, `Send`.
- Error copy should explain:
- what happened
- why it matters
- the next action

## 11) Implementation Baseline

Use centralized tokens and avoid local one-off styles:

```css
:root {
  --background: #ffffff;
  --foreground: #171717;
  --success: #70eeee;
  --success-strong: #70eeee;
}

.dark {
  --background: #01070d;
  --foreground: #ffffff;
}
```

## 12) Definition of Done (Design)

- Uses semantic color tokens, not arbitrary hex values.
- Typography and spacing follow this system.
- Focus/hover/loading/disabled states are present.
- Mobile layout has no horizontal overflow.
- Motion is subtle and reduced-motion safe.
- Contrast and readability are validated before shipping.
