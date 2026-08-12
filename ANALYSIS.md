# XAUUSD Gann Analysis — Longer-Term Swing Map & Progress

**Last updated:** 2026-08-12

## Data Coverage

- **Daily bars**: 499 (2024-09-04 → 2026-08-11)
- **Price range in sample**: 2471.82 – 5597.60
- **H1 bars** (recent window): ~500 bars (mid-July → 11 Aug 2026)

## Major Swing Highs (last 8 identified)

| Date       | Price   |
|------------|---------|
| 2026-02-11 | 5119.04 |
| 2026-03-02 | 5419.13 |
| 2026-04-17 | 4890.37 |
| 2026-05-12 | 4773.86 |
| 2026-05-29 | 4595.18 |
| 2026-06-17 | 4382.44 |
| 2026-07-06 | 4203.29 |
| 2026-07-22 | 4165.99 |

## Major Swing Lows (last 8 identified)

| Date       | Price   |
|------------|---------|
| 2026-03-03 | 4996.05 |
| 2026-03-23 | 4097.87 |
| 2026-05-04 | 4500.49 |
| 2026-05-28 | 4366.29 |
| 2026-06-11 | 4023.68 |
| 2026-06-30 | 3942.22 |
| 2026-07-17 | 3959.50 |
| 2026-07-29 | 3995.71 |

These pivots are the primary origins for longer-term Gann fans and Square of Nine work.

## First Quantitative Result (Square of Nine)

A formal touch-rate study has been completed:

→ **[backtest/QUANT-SQ9-RESULTS.md](backtest/QUANT-SQ9-RESULTS.md)**

**Headline number:** 50.4% of generated Square-of-Nine levels (within a practical distance band) were touched by price inside the following 25 daily bars.

This is a baseline only. Next measurements will focus on *reversal quality*, confluence with angles, and regime filters.

## Day-Trading Progress

See the companion document:

→ **[BACKTEST-DAY-TRADING.md](BACKTEST-DAY-TRADING.md)**

It contains the concrete day-trading ruleset (v0.1), observations on the recent expansion and reversal days, and the practical scaling used for 1×1 / 2×1 angles on Gold.

## Code Tools

```
tools/gann_utils.py
```

Provides:
- `square_of_nine_levels(origin, steps=8)`
- `gann_angle_price(...)`
- Rising / falling angle helpers

## Current Status & Next Work

- [x] Multi-year daily data pulled
- [x] Major swings mapped
- [x] Core Gann utility functions written
- [x] First quantitative Sq9 touch-rate baseline
- [ ] Reversal-quality scoring (not just touch)
- [ ] Gann angle hit-rate measurement
- [ ] ATR regime filter
- [ ] Full H1 day-trading ruleset backtest with R-multiples

---

*Research repository — not trading advice.*
