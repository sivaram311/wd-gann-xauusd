# Quantitative Results II — Reversal Quality & Gann Angles

**Date:** 2026-08-12  
**Data:** 499 Daily bars XAUUSD (2024-09-04 → 2026-08-11)

---

## 1. Square of Nine — Reversal Quality (Key Upgrade)

Previous study only measured *touches*. This study asks a harder question:

> After price touches a Square of Nine level, does it reverse by at least **30 points** in the expected direction within the next ~8 bars?

**Parameters**
- Last 15 swing highs + last 15 swing lows
- Levels between 0.6% – 12% from origin
- Touch tolerance: 0.4%
- Look-ahead for touch: 25 bars
- Reversal requirement: ≥ 30 points in the logical direction (resistance after high-origin levels, support after low-origin levels)

### Results

| Origin Type     | Levels Tested | Touched | Reversed ≥30 pts | % of Touches that Reversed | % of All Levels |
|-----------------|---------------|---------|------------------|----------------------------|-----------------|
| Swing Highs     | 347           | 179     | 142              | **79.3%**                  | 40.9%           |
| Swing Lows      | 338           | 166     | 136              | **81.9%**                  | 40.2%           |
| **Combined**    | **685**       | **345** | **278**          | **~80.6%**                 | **~40.6%**      |

### Interpretation

Once price actually reaches a Square of Nine level generated from a major swing, the probability of a meaningful 30-point reaction in the expected direction is high (~80%).  
This is a much more useful statistic than the raw 50% touch rate. It suggests the levels have real magnetic / reaction properties when tested.

---

## 2. Gann Angles — First Hit-Rate Pass (Daily)

Rising angles projected from swing lows and falling angles from swing highs.

**Scale tested:** 10 points per daily bar (and a tighter 6-point scale) for the 1×1.  
Tolerance: 0.5%.

| Test                              | 1×1 Hit Rate | 2×1 Hit Rate |
|-----------------------------------|--------------|--------------|
| Rising from Lows (scale=10)       | 8.3%         | 11.0%        |
| Falling from Highs (scale=10)     | 9.9%         | 15.1%        |
| Rising from Lows (scale=6)        | 11.0%        | 8.6%         |
| Falling from Highs (scale=6)      | 7.2%         | 11.2%        |

### Interpretation

Angle hit rates are lower than Square of Nine levels because an angle is a *moving* target. The 2×1 shows slightly more interaction than the 1×1 on the wider scale.  
These numbers are only a first baseline; angle performance is expected to improve when:
- Measured on H1/M15 (day-trading timeframe)
- Combined with Square of Nine confluence
- Filtered by volatility regime

---

## 3. Practical Takeaway for Day / Swing Trading

1. **Square of Nine levels from major swings** are worth watching. When price arrives at them, the odds of a usable reaction are favourable (~80% for a 30-point move in this sample).
2. **Gann angles** alone (on Daily) are weaker as standalone signals but remain useful as dynamic structure, especially the 2×1.
3. The highest-probability setups will almost certainly come from **confluence**: price arriving at a Square of Nine level that also sits on a Gann angle, preferably inside a known time cycle window.

---

## 4. Next Measurements

- [ ] Confluence scoring (Sq9 + Angle on the same bar)
- [ ] ATR / volatility regime split (expansion vs compression)
- [ ] Same reversal test on H1 data for the day-trading ruleset
- [ ] R-multiple simulation of the v0.1 day-trading rules

---

*Research only. Not trading advice.*
