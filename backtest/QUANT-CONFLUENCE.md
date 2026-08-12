# Quantitative Results III — Confluence (Square of Nine + Gann Angle)

**Date:** 2026-08-12  
**Data:** 499 Daily bars XAUUSD (2024-09-04 → 2026-08-11)

## Goal

Test whether requiring **both** a Square of Nine level **and** a Gann angle (1×1 or 2×1) on the same bar improves reaction quality versus Square of Nine alone.

## Method

- Origins: last 12 swing highs and last 12 swing lows (5-bar fractals)
- Square of Nine levels generated with the practical square-root method
- Gann angles projected with scale = 10 points per daily bar
- A bar is counted as confluence when price trades within 0.4% of both a Sq9 level and an angle
- Reversal definition (strict): after the touch bar, price must move ≥ **40 points** in the expected direction within the next 7 bars

## Results

### From Swing Lows (rising angles expected to act as support)

| Type              | Touches | Reversals ≥40 pts | Success Rate |
|-------------------|---------|-------------------|--------------|
| Pure Square of 9  | 180     | 173               | 96.1%        |
| **Confluence**    | 45      | 43                | 95.6%        |

### From Swing Highs (falling angles expected to act as resistance)

| Type              | Touches | Reversals ≥40 pts | Success Rate |
|-------------------|---------|-------------------|--------------|
| Pure Square of 9  | 223     | 206               | 92.4%        |
| **Confluence**    | 69      | 63                | 91.3%        |

### Combined

| Type              | Touches | Reversals | Success Rate |
|-------------------|---------|-----------|--------------|
| Pure Square of 9  | 403     | 379       | **94.0%**    |
| **Confluence**    | 114     | 106       | **93.0%**    |

## Observations

1. **Confluence events are real and reasonably frequent** (114 events in the sample of 12+12 swings).
2. On Daily timeframe with a 40-point reversal threshold, both pure Sq9 and confluence show very high success rates. This is partly explained by the extreme volatility of Gold in the 2024–2026 sample (range > 3000 points).
3. Confluence does **not** meaningfully *increase* the already high reversal rate on Daily, but it **filters** the number of signals (114 vs 403), which is useful for reducing trade frequency and focusing on higher-conviction areas.
4. The real test of confluence value will come on **H1 / M15**, where a 30–40 point move is a much more selective event and noise is higher.

## Practical Conclusion (so far)

- Square of Nine levels from major swings remain the stronger standalone tool on Daily.
- Adding the Gann angle as a filter reduces the number of candidate levels while preserving high reaction probability.
- Best use of confluence at this stage: treat the overlapping zones as preferred areas for profit targets or for tighter risk placement rather than as a strict entry trigger on Daily.

## Next Steps

- [ ] Repeat the exact confluence test on H1 data (day-trading horizon)
- [ ] Introduce ATR regime split (high vs low volatility)
- [ ] Simulate the v0.1 day-trading rules with R-multiples on H1

---

*Research only. Not trading advice.*
