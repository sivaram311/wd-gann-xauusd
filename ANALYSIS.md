# XAUUSD Gann Analysis — Progress Dashboard

**Last updated:** 2026-08-12

## Quantitative Results Summary

| Study | File | Key Finding |
|-------|------|-------------|
| Sq9 Touch Rate | [QUANT-SQ9-RESULTS.md](backtest/QUANT-SQ9-RESULTS.md) | ~50% of levels touched within 25 days |
| Reversal Quality + Angles | [QUANT-REVERSAL-AND-ANGLES.md](backtest/QUANT-REVERSAL-AND-ANGLES.md) | ~80% of touched Sq9 levels reversed ≥30 pts |
| Confluence (Sq9+Angle) | [QUANT-CONFLUENCE.md](backtest/QUANT-CONFLUENCE.md) | Filters signals while preserving high reaction rate |
| **H1 Day-Trading Backtest** | [H1-DAYTRADING-BACKTEST.md](backtest/H1-DAYTRADING-BACKTEST.md) | **27 trades, 37% win rate, +0.89 R expectancy** |

## Day-Trading Ruleset

→ [BACKTEST-DAY-TRADING.md](BACKTEST-DAY-TRADING.md)

## Code

`tools/gann_utils.py`

## Status Checklist

- [x] Multi-year daily data + major swings
- [x] Core Gann utility functions
- [x] Sq9 touch-rate baseline
- [x] Reversal-quality scoring
- [x] Gann angle hit-rate (Daily)
- [x] Confluence scoring
- [x] **First H1 day-trading quantitative backtest**
- [ ] Sq9 + time-cycle filters on the H1 ruleset
- [ ] ATR regime filter
- [ ] Longer H1 history + out-of-sample test

---

*Research repository — not trading advice.*
