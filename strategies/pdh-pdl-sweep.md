# PDH/PDL sweep + VWAP reclaim (candidate setup G, paper only)

Requested by the owner on 2026-10-15: find a SPY strategy built on the previous
day's high (PDH) and low (PDL) that wins more often than it loses, looking back
90 days. Not in the playbook yet; proposed for the Friday review.

## Rules (as backtested)

1. Mark PDH and PDL (regular session 9:30–4:00). The pre-market brief posts them.
2. **Sweep:** price trades at least **$0.10 beyond** the level (above PDH / below PDL).
3. **Reclaim (entry candle):** within **60 minutes** of the sweep, a 5-min candle
   closes back inside the level, **on the right side of VWAP**, and in the
   reversal color:
   - PDH sweep → **put**: the candle closes below PDH, below VWAP, red.
   - PDL sweep → **call**: the candle closes above PDL, above VWAP, green.
4. Entry at that candle's close, no earlier than 9:45 and no later than 2:25.
5. **Stop:** $0.25 beyond the entry candle's high (puts) or low (calls).
6. **Target: 1R** (the same distance as the stop). Out by 3:30 at the latest.
7. Skip if the stop is under $0.15 or over $2.50 away. One trade per level per day.

## Results (SPY 5-min bars, R = SPY risk per trade)

| Period | Trades | Wins | Win rate | Net |
|---|---|---|---|---|
| Last 90 days (7/17–10/15), both sides | 19 | 11 | 58% | +3.0R |
| **PDH sweep → puts only** | **14** | **9** | **64%** | **+4.0R** |
| PDL sweep → calls only | 5 | 2 | 40% | −1.0R |
| Earlier holdout (6/16–7/16), puts | 4 | 3 | 75% | +2.0R |
| Earlier holdout, calls | 3 | 1 | 33% | −1.0R |

- The put side (fading a sweep of yesterday's high) is the edge; the call side
  is not proven. In a market that drifted up, PDH got swept often and failed.
- Many entries come right at 9:45–10:00, the first bar the 0DTE rules allow.
- Frequency: about 1–2 a week.

## Caveats

- 756 rule variants were tested. Settings were chosen on 7/17–8/31 and checked
  on 9/1–10/15 and 6/16–7/16; neighbouring settings were also positive in all
  three periods. Still a small sample (14 put trades): paper-trade it before
  real money.
- R is measured on SPY. A 0DTE option at the $100 cap moves less than 1:1
  (delta ≈ 0.3–0.5), and spreads and decay cut into a 1R target.
- Raising the target to 1.5R drops the win rate under 50% (the owner asked for
  more wins than losses), though some 1.5R variants made more R in total.

Backtest code: `tools/pdh_pdl/` (eng.py loads bars, strat.py has the three
strategy families: sweep+VWAP, breakout-retest, rejection fade; grid.py and g2.py
run the searches).
