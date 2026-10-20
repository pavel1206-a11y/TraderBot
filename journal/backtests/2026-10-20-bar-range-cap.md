# Bar-range cap on E lines: backtest (2026-10-20)

Question: the armed E lines skip a trigger bar whose high–low range is over $1.00. The owner asked to raise that limit (10/19 EOD). Before changing it, a replay of the E rules as armed today.

Rules simulated (SPY 5-min, 2026-01-02 to 10-15, 198 sessions): fresh close through a key level (prior-day H/L/C, pivots R1/R2/S1/S2, opening range, day high/low) within the close band; SPY and QQQ on the trade's side of VWAP; volume ≥ 1.0× the prior 10 bars, or ≥ 0.7× with QQQ breaking its 45-min edge the same bar; stop ±$0.40; target 1.5R; room ≥ 1.5R to the next level; 30-min time stop; ≤ 3 trades and ≤ 2 losses a day. Script: `tools/pdh_pdl/rangecap.py`.

| Close band | Cap $1.00 | $1.25 | $1.50 | $2.00 | No cap |
|---|---|---|---|---|---|
| $0.10 (current) | 114 tr, **+10.8R** | 125, +9.8R | 130, +7.3R | 134, +3.3R | 136, +1.3R |
| $0.30 | 212, **+18.2R** | 237, +17.6R | 250, +14.6R | 262, +12.5R | |
| $0.50 | 227, **+21.6R** | 256, +20.0R | 270, +16.0R | 281, +10.0R | |

- Every step up in the cap lowers the total. At the current band, the 22 trades that only exist without a cap won 5 times for −9.5R. Big trigger bars tend to reverse inside the $0.40 stop.
- The close band is what costs trades: $0.30 nearly doubles the trades and adds +7.4R with the $1.00 cap kept; both halves of the year are positive (Jan–Jun +5.1R, Jul–Oct +13.1R). $0.50 is higher in total but weaker in Jul–Oct (+9.6R).
- Caveats: simplified simulator (fixed 30-min block after each entry, approximate QQQ clause), SPY points not option prices, data ends 10/15 (10/16 and 10/19 not included).

Recommendation: keep the $1.00 cap; widen the close band to $0.30 (proposal 1, revised). Owner decides.
