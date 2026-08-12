# H1 Day-Trading Gann Backtest (v0.1 Ruleset)

**Date:** 2026-08-12  
**Data:** 799 H1 bars of XAUUSD (2026-06-24 → 2026-08-12) — 36 trading days  
**Trades generated:** 27 (one proxy signal per day maximum)

---

## Rules Implemented (Proxy)

Taken from the framework in `BACKTEST-DAY-TRADING.md`:

- **Origins each day:** Previous Day High (PDH), Previous Day Low (PDL), Previous Day Close (PDC)
- **Angles:** Rising 1×1 & 2×1 from PDL, Falling 1×1 & 2×1 from PDH  
  Scale = **2.5 points per H1 bar**
- **Signal (simplified):**  
  - Long: price low interacts with a rising angle + bullish close  
  - Short: price high interacts with a falling angle + bearish close  
- First valid signal after the first 2 hours of the day is taken  
- Risk distance derived from the angle (minimum 5 pts, typical ~12 pts)  
- Outcome measured over the next 5 H1 bars

This is still a **proxy**, not a full tick-by-tick engine with order-block style rejection or time-cycle filters. It is the first quantitative measurement of the angle-based day-trading idea.

---

## Results

| Metric                    | Value      |
|---------------------------|------------|
| Number of trades          | 27         |
| Win rate                  | **37.0%** (10/27) |
| Average R (all trades)    | **0.89**   |
| Average R on winners      | 1.78       |
| Average R on losers       | 0.37       |
| **Expectancy**            | **+0.89 R** |

Even with a sub-40% win rate the system shows positive expectancy because the average winner is substantially larger than the average loser.

---

## Sample Trades

| Date       | Side  | Entry  | R     | Win?  | Max Favourable | Max Adverse |
|------------|-------|--------|-------|-------|----------------|-------------|
| 2026-06-25 | Long  | 3982.9 | 1.07  | Yes   | 18.2           | 16.7        |
| 2026-06-26 | Short | 3990.7 | 0.09  | No    | 4.2            | 49.0        |
| 2026-07-06 | Short | 4179.6 | 2.55  | Yes   | 35.1           | 23.6        |
| 2026-07-08 | Long  | 4111.5 | 1.29  | Yes   | 22.4           | 15.2        |
| 2026-08-07 | Long  | 4256.7 | 1.45  | Yes   | 42.0           | 9.8         |
| 2026-08-10 | Short | 4341.2 | 4.00  | Yes   | 24.6           | 10.9        |
| 2026-08-11 | Short | 4366.2 | 0.82  | No    | 9.8            | 26.7        |

---

## Interpretation

- The core idea (reacting at Gann angles projected from the previous day’s extremes) produces a **positive expectancy** sample on recent H1 data.
- Win rate is modest; edge comes from reward-to-risk asymmetry.
- Several large adverse excursions on losing trades suggest the need for:
  1. A tighter or volatility-adjusted stop method
  2. Time-cycle filter (avoid signals late in the session)
  3. Higher-timeframe bias filter (only take longs above a rising Daily angle, etc.)

---

## Limitations of this first pass

- Only ~5–6 weeks of H1 data
- One trade per day maximum (conservative)
- No Square-of-Nine confluence filter applied yet
- No explicit 90/144/180-minute time window filter
- Rejection logic is simplified (bullish/bearish close only)

---

## Recommended Next Improvements

1. Add Sq9 confluence as a required filter and re-measure expectancy
2. Add time-cycle windows (only take signals inside 90–180 min from open)
3. Expand to 3–6 months of H1 data when available
4. Test ATR-based position sizing / stop distance
5. Separate London vs New York session performance

---

*Research only. Not trading advice. Past positive expectancy on a small sample does not guarantee future results.*
