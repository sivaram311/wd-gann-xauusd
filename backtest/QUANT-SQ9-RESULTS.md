# Quantitative Square of Nine Study — XAUUSD Daily

**Date:** 2026-08-12  
**Data:** 499 Daily bars (2024-09-04 → 2026-08-11)  
**Method:** 5-bar swing highs/lows → generate Square of Nine levels → measure whether price later traded within 0.4% of the level inside the next 25 bars.

## Test Design

- Swings identified with a classic 5-bar fractal.
- Square of Nine levels generated with the practical square-root method (`tools/gann_utils.py`).
- Only levels between ~0.6% and 12% away from the origin swing were tested (too close = noise, too far = irrelevant for intermediate horizon).
- Tolerance for a “hit”: price high/low/close came within **0.4%** of the projected level.
- Look-ahead window: **25 trading days**.

## Results (last 15 swing highs + last 15 swing lows)

| Origin Type       | Levels Tested | Levels Touched | Hit Rate |
|-------------------|---------------|----------------|----------|
| Swing Highs       | 347           | 179            | **51.6%** |
| Swing Lows        | 338           | 166            | **49.1%** |
| **Combined**      | **685**       | **345**        | **50.4%** |

### Interpretation

A raw touch rate of ~50% is close to what one would expect from random levels in a trending/volatile market when the tolerance band is 0.4% and the window is 25 days.  
This does **not** yet prove edge. It does establish a baseline.

What matters more for trading is:
1. **Reaction quality** (rejection / reversal vs mere touch),
2. **Confluence** (Square of Nine + Gann angle + time cycle),
3. **Regime filter** (the same level behaves differently in expansion vs consolidation).

These refinements are the next measurement layer.

## Sample Recent Reactions

**From swing highs**
- 2026-07-22 high @ 4166 → multiple Sq9 levels (4214, 4231, 4247, 4263, 4296, 4329, 4362, 4428) were later traded.

**From swing lows**
- 2026-07-29 low @ 3996 → levels 4043, 4059, 4075, 4091, 4123, 4253, 4318, 4384 were later traded.

## Next Quantitative Steps

1. Measure **reversal rate** (not just touch) — did price reverse at least X points after touching the level?
2. Add Gann angle hit-rate using the same swing origins and the functions in `tools/gann_utils.py`.
3. Introduce an ATR regime filter and re-score the levels.
4. Move to H1 / M15 for the day-trading ruleset already defined in `BACKTEST-DAY-TRADING.md`.

---

*Baseline established. Edge measurement continues.*
