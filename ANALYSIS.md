# XAUUSD Gann Analysis — Longer-Term Swing Map & Progress

**Last updated:** 2026-08-12

## Data Coverage

- **Daily bars**: 499 (2024-09-04 → 2026-08-11)
- **Price range in sample**: 2471.82 – 5597.60
- **H1 bars** (recent window): ~500 bars (mid-July → 11 Aug 2026)

## Quantitative Results So Far

| Study | File | Key Finding |
|-------|------|-------------|
| Sq9 Touch Rate | [QUANT-SQ9-RESULTS.md](backtest/QUANT-SQ9-RESULTS.md) | ~50% of levels touched within 25 bars |
| Reversal Quality + Angles | [QUANT-REVERSAL-AND-ANGLES.md](backtest/QUANT-REVERSAL-AND-ANGLES.md) | ~80% of touched Sq9 levels reversed ≥30 pts |
| **Confluence** | [QUANT-CONFLUENCE.md](backtest/QUANT-CONFLUENCE.md) | 114 confluence events; high reversal rate preserved while filtering signal count |

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
- [x] Confluence scoring (Sq9 + Angle)
- [ ] ATR regime filter
- [ ] Full H1 day-trading ruleset backtest with R-multiples

---

*Research repository — not trading advice.*
