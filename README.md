# W.D. Gann Analysis on XAUUSD

**Public research repository** applying classical W.D. Gann geometric and time-based methods to Gold (XAUUSD).

## Core Ideology

William D. Gann taught that price and time are geometrically related. Markets move in measurable proportions (angles, squares, cycles). The goal of this project is **not** discretionary chart reading, but systematic extraction and historical validation of Gann constructs on XAUUSD.

### Key Gann Concepts Applied

1. **Gann Angles / Fans**  
   1×1 (45°), 2×1, 1×2, 3×1, 1×3, 4×1, 1×4 drawn from major swing highs and lows. These act as dynamic support/resistance.

2. **Square of Nine**  
   Spiral number wheel used to project price levels that are geometrically related to significant highs/lows (cardinal cross, ordinal cross, etc.).

3. **Price–Time Squares**  
   When the number of price units moved equals the number of time units (days/bars) elapsed from a major pivot, a turning point is expected.

4. **Time Cycles**  
   Natural cycles (30, 45, 60, 90, 144, 180, 360 calendar or trading days) measured from major tops and bottoms.

5. **Law of Vibration & Natural Levels**  
   Emphasis on whole numbers, halves, quarters, and Gann’s preferred price increments for Gold.

## Methodology: “Backtest Coming Backwards”

Traditional forward backtesting optimizes on past data and hopes the future behaves the same.  
**Coming backwards** means:

1. Start from the most recent significant swing high/low on XAUUSD.
2. Work **backward** through history, identifying the major pivots that “should” have been important according to Gann geometry.
3. Measure how often the Gann angles, Square-of-Nine levels, and time cycles actually contained price or produced measurable reactions.
4. Only after the historical map is complete do we freeze the rules and examine whether the same geometric relationships continue to appear in more recent (or unseen) data.

This approach reduces look-ahead bias in the discovery phase and forces the analyst to respect the geometry that was already present in the past.

## Planned Contents of this Repository

- `ANALYSIS.md` — Detailed historical Gann map of major XAUUSD swings (to be expanded with real data).
- `methodology/` — Precise definitions of how angles, Square of Nine, and cycles are calculated for Gold.
- `data/` — Notes on data sources (MT5 / broker continuous contracts) and cleaning rules.
- `backtest/` — Results of the backward validation and any quantitative metrics (hit rate of angles, average reaction size, etc.).
- Scripts (Python) for generating Gann fans and Square-of-Nine levels from OHLC data (future).

## Current Status

Repository initialized and methodology documented.  
Next steps:
1. Pull multi-year daily / H4 XAUUSD history via MT5.
2. Identify major swing points.
3. Construct Gann fans and Square-of-Nine projections.
4. Document findings in markdown and quantify the historical reliability of the geometry.

---

*This is a research project, not financial advice. Gann methods are geometric tools; they do not guarantee future results.*
