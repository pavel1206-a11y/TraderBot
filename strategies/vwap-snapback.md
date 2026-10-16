# VWAP snap-back (80%+ win-rate candidate, paper only)

Owner request 2026-10-16: keep testing strategies on history until one wins 80%
of the time, ignoring the premium cap for the test. Real-money rules in
CLAUDE.md (including the cap) are unchanged.

## Rules

1. Calls only (long). Entries 9:45 AM–12:00 PM ET.
2. **Stretch:** a 5-min candle's low is at least **$1.00 below VWAP**.
3. **Snap-back candle:** the next candle is green and **closes above the
   stretched candle's high**. Enter at its close.
4. **Stop:** $0.50 below the lower of the two candles' lows.
5. **Target:** **halfway back to VWAP** (measured from the entry close).
6. Exit by 3:30 if neither is hit. First signal of the day only. Skip if the
   target is under $0.10 away or the stop is over $3.00 away.

## Results (SPY 5-min bars, $0.02 per trade cost)

Settings chosen on 2/3–6/30, then tested on 7/1–10/15, which the search never saw.

| Period | Trades | Wins | Win rate |
|---|---|---|---|
| Discovery 2/3–6/30 | 52 | 46 | 88% |
| **Held-out 7/1–10/15** | **51** | **43** | **84%** |
| All | 103 | 89 | 86% |

**The catch: wins are small and losses are big.** Average win +$0.40 per SPY
share; average loss −$1.86. One loss erases about 4–5 wins. Net over 103 trades:
+$9.60 per share (about $0.09 a trade). 3 of 8 full months were flat or
negative (April, July, August). The edge shrinks to about zero if slippage reaches
about $0.10 per trade, and a 0DTE option makes a $0.40 SPY move worth very
little after the spread.

Aiming the target fully at VWAP makes more per win but drops the win rate to
65–74%. That is the usual trade-off: a higher win rate costs size per win.

## Search log

Over 10,000 rule variants across four families (PDH/PDL sweep + VWAP reclaim,
gap fade, VWAP snap-back, PDH/PDL breakout-retest), on 198 sessions
(1/2–10/15/2026). 59 variants hit ≥ 80% with ≥ 20 trades in discovery; 12 held
≥ 80% on the held-out months, all of them VWAP snap-back longs. No PDH/PDL
variant held 80% out of sample. Code: `tools/pdh_pdl/` (s2.py, search.py, val.py).
