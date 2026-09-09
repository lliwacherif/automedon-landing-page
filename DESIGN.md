# Automedon Design System

## 1. Overview

**Brand:** Automedon — fleet operating system for Tunisian car-rental agencies.  
**Direction:** Cobalt Instrument (brand palette lock).  
**Philosophy:** Imperial Blue structure, True Cobalt action, Bright Snow / White Smoke paper. Product UI is the hero. No sand/amber, no extra hues.

Tone is formal but local: precise, trustworthy, built for operators.

## 2. Colors

Brand primitives (hex is source of truth):

| Token | Hex | OKLCH | Role |
|---|---|---|---|
| `--true-cobalt` | `#293385` | `oklch(0.366 0.137 272)` | Primary CTA, labels, accent |
| `--imperial-blue` | `#132571` | `oklch(0.307 0.133 267)` | Text, hero/footer bands, hover |
| `--bright-snow` | `#f8f8f8` | `oklch(0.979 0 0)` | Page, text on dark, button label |
| `--white-smoke` | `#f4f4f4` | `oklch(0.967 0 0)` | Cards, fields, alternate bands |

Semantic mapping:

- `--color-bg` → Bright Snow  
- `--color-surface` → White Smoke  
- `--color-fg` → Imperial Blue  
- `--color-muted` → True Cobalt mixed with Snow (~78%)  
- `--color-primary` → True Cobalt  
- `--color-primary-hover` → Imperial Blue  
- `--color-accent` → True Cobalt  
- `--color-on-primary` → Bright Snow  
- `--color-inverse` → Imperial Blue (hero, why, CTA, footer)  
- `--color-inverse-fg` → Bright Snow  
- `--color-ring` → True Cobalt  
- `--color-border` → Imperial Blue at 16% on Snow  

Do not introduce sand, green, purple, or off-palette neutrals. Browser chrome traffic-light dots on screenshots are the only exception (OS metaphor). Form errors use Imperial Blue + message text (not a fifth hue).

Contrast: Imperial Blue on Bright Snow and Snow on Imperial Blue both exceed AA. Muted mixes stay 16px+.

## 3. Typography

- **Display:** Fraunces (`opsz` 9–144, weights 500–700)  
- **Body:** Source Sans 3 (400–700)  
- **Arabic:** IBM Plex Sans Arabic for both roles when `dir="rtl"`

Fluid scale:

- `--text-xs`: `clamp(0.75rem, 0.7rem + 0.25vw, 0.8125rem)`  
- `--text-sm`: `clamp(0.8125rem, 0.775rem + 0.2vw, 0.875rem)`  
- `--text-base`: `clamp(0.9375rem, 0.9rem + 0.2vw, 1rem)`  
- `--text-lg`: `clamp(1.0625rem, 1rem + 0.3vw, 1.125rem)`  
- `--text-xl`: `clamp(1.1875rem, 1.1rem + 0.45vw, 1.35rem)`  
- `--text-2xl`: `clamp(1.5rem, 1.25rem + 1vw, 1.85rem)`  
- `--text-3xl`: `clamp(1.75rem, 1.45rem + 1.4vw, 2.4rem)`  
- `--text-4xl`: `clamp(2.2rem, 1.7rem + 2.4vw, 3.6rem)`

Line-height: 1.15 display / 1.6 body. Letter-spacing: −0.02em on display.

## 4. Layout

- Base unit: **4px**. Public scale: 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96.  
- Content width: **1120px**. Media/carousel: up to 1280px.  
- Section padding: `--space-section` = `clamp(4rem, 8vw, 7rem)`.  
- Header rhythm: label 8 → title 12 → description 48 → content.  
- Device scroll: side-by-side ≥900px; stacked below. Max ~110vh stage on mobile.

## 5. Elevation & Depth

- Level 0: Bright Snow page  
- Level 1: White Smoke panel + Imperial Blue 16% border  
- Level 2: dropdown / lightbox on Imperial overlay  
- Shadows: `0 24px 48px color-mix(in srgb, var(--imperial-blue) 18%, transparent)`

## 6. Shapes

- `--radius-sm`: 6px  
- `--radius-md`: 10px  
- `--radius-lg`: 16px  
- `--radius-xl`: 20px  
- `--radius-pill`: 999px  
- Buttons: pill. Cards/panels: `--radius-lg`. Fields: `--radius-md`.

## 7. Components

- **Button primary:** True Cobalt fill, Bright Snow text, Imperial hover.  
- **Button secondary:** transparent, Imperial/Cobalt border.  
- **Card:** White Smoke, hairline border, no glass.  
- **Plan featured:** True Cobalt hairline + Imperial badge (Snow text), **no scale**.  
- **Field:** Bright Snow fill, Imperial text, Cobalt ring on `:focus-visible`.  
- **Nav:** fixed; Snow text over Imperial hero; Bright Snow bar after scroll. Collapse ≤900px.  
- **Hero / Why / CTA / Footer:** Imperial inverse bands, Bright Snow type.

## 8. Do's and Don'ts

**Do:** use the four brand tokens; mix only those four for muted/border/overlay; keep product screenshots sharp; honor `prefers-reduced-motion`; preserve Formspree fields.  
**Don't:** sand/amber; purple glow; Inter/Space Grotesk; plan prices; extra greys or greens; raw hex in new CSS except the four primitives.

## 9. Motion

- `--duration-fast`: 150ms  
- `--duration-normal`: 250ms  
- `--ease-out`: `cubic-bezier(.22, 1, .36, 1)`  
- Keep iMac/MacBook/iPhone device family scroll + Swiper + lightbox.  
- Reduce looping video opacity; disable zoom animation when reduced-motion.

## 10. Responsive

- 320–479: 1 col, overlapping device cluster, icon nav CTA  
- 480–767: same, larger type  
- 768–899: 2-col features/pricing; tighter device cluster  
- 900+: iMac/MacBook/iPhone overlapping family  
- 1024+: full nav (collapse still at 768 if 5+ links overflow — prefer 768)

## 11. Dark Mode Strategy

Light paper site with Imperial inverse bands (hero, why, CTA, footer). Semantic tokens live on `:root`. Do not add a separate dark theme.

## 12. Agent Prompt Guide

When editing UI: read this file first; map every color/spacing/type to tokens; keep `#contact` Formspree actions and `name` attributes; keep FR/EN/AR + RTL; do not restore prices on plan cards.
