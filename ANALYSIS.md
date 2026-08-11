# XAUUSD Gann Analysis — Longer-Term Swing Map & Progress

**Last updated:** 2026-08-12

## Data Coverage

- **Daily bars**: 499 (2024-09-03 → 2026-08-10)
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

## Day-Trading Progress

See the companion document:

→ **[BACKTEST-DAY-TRADING.md](BACKTEST-DAY-TRADING.md)**

It contains the concrete day-trading ruleset (v0.1), observations on the recent expansion and reversal days, and the practical scaling used for 1×1 / 2×1 angles on Gold.

## Code Tools Added

A pure-Python helper module is now in the repository:

```
tools/gann_utils.py
```

It provides:

- `square_of_nine_levels(origin, steps=8)` — practical Square of Nine projections
- `gann_angle_price(...)` — project any common Gann angle forward/backward
- Convenience wrappers for rising angles from a low and falling angles from a high

These functions are the foundation for the next quantitative layer (bar-by-bar angle tracking and hit-rate measurement).

## Immediate Next Work

1. Use `gann_utils.py` against the 499 daily bars to measure how often price reacted at projected Square-of-Nine levels and key angles from the major swings listed above.
2. Expand the H1 day-trading sample and compute exact R-multiples for the v0.1 ruleset.
3. Add a simple volatility filter (ATR regime) so angle strategies are not forced to fight expansion days.

---

*Research repository — not trading advice.*
