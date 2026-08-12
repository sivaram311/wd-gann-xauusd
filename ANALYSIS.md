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

## Quantitative Results So Far

1. **Touch rate (Sq9)** → [QUANT-SQ9-RESULTS.md](backtest/QUANT-SQ9-RESULTS.md)  
   ~50.4% of levels touched within 25 bars.

2. **Reversal quality + Angles** → [QUANT-REVERSAL-AND-ANGLES.md](backtest/QUANT-REVERSAL-AND-ANGLES.md)  
   - When a Sq9 level is touched, it reverses ≥30 points in the expected direction **~80.6%** of the time.  
   - First Gann angle hit-rates on Daily (1×1 / 2×1) are lower (7–15%), as expected for a moving target.

## Day-Trading Progress

→ **[BACKTEST-DAY-TRADING.md](BACKTEST-DAY-TRADING.md)** (v0.1 ruleset)

## Code Tools

`tools/gann_utils.py` — Square of Nine + scaled angle projection helpers.

## Status Checklist

- [x] Multi-year daily data pulled
- [x] Major swings mapped
- [x] Core Gann utility functions written
- [x] Sq9 touch-rate baseline
- [x] Reversal-quality scoring
- [x] First Gann angle hit-rate measurement
- [ ] Confluence scoring (Sq9 + Angle)
- [ ] ATR regime filter
- [ ] Full H1 day-trading ruleset backtest with R-multiples

---

*Research repository — not trading advice.*
