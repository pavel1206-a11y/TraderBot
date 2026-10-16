# 30-minute ORB runner (big wins, small losses; paper only)

Owner request 2026-10-16: find a strategy with big wins and only small losses.

## Rules

1. **Opening range** = high and low of 9:30–10:00 (first six 5-min candles).
2. **Entry** (10:00 AM–12:30 PM ET, first signal of the day only): a 5-min candle
   **closes beyond the opening range**, and on the same candle:
   - SPY is on the breakout side of VWAP (above for calls, below for puts);
   - QQQ is on the same side of its own VWAP;
   - volume is ≥ 1.2× the average of the prior 10 candles.
3. **Stop:** $0.05 beyond the extreme of the breakout candle and the candle
   before it (the lower low for calls, the higher high for puts). Skip if that
   is more than $1.50 away.
4. **At +1R, move the stop to break-even.**
5. **No profit target:** hold until 3:30 PM (or the break-even stop). Exiting on a
   5-min close back through VWAP gave almost the same results.

## Results (SPY 5-min bars, 2/3–10/15/2026, $0.02 per trade cost)

Settings chosen on Feb–Jun; Jul–Oct was not seen by the search.

| Period | Trades | Wins | Scratches (break-even) | Full losses | Avg win | Avg full loss | Net per SPY share |
|---|---|---|---|---|---|---|---|
| Feb–Jun | 45 | 11 | 17 | 17 | **+$3.54** | **−$0.97** | +$22.19 |
| **Jul–Oct (unseen)** | **50** | **12** | **19** | **19** | **+$2.27** | **−$0.92** | **+$9.38** |
| All | 95 | 23 (24%) | 36 (38%) | 36 (38%) | +$2.88 | −$0.94 | +$31.57 |

- Wins are about 3× the size of losses, and over a third of trades end flat at break-even.
- The **win rate is low (24%)**: the longest run without a win was 9 trades. It
  only works if every signal is taken and the runner is never cut early.
- Biggest wins: 6/5 put +$9.42, 9/21 call +$5.06, 5/13 call +$5.00, 3/26 put +$4.13.
- Calls carried the result (54 trades, +75.9R; puts 41 trades, +2.3R). SPY rose from
  ~$650 to ~$770 over this period, so the put side may just be weaker in an up market.
- Raising the minimum stop distance to $0.30 or $0.50 kept both halves positive.

## Search log

About 20,000 variants across 4 families (ORB, PDH/PDL breakout, flush + VWAP reclaim,
squeeze breakout) × 7 exit styles (fixed 2/3/4R, VWAP-close exit, trailing stop,
hold to close) with and without a break-even stop. Discovery filter: ≥ 25 trades,
avg win ≥ 2.5× avg loss, ≥ +0.15R per trade, profit factor ≥ 1.4. 1,692 passed in
discovery; 404 also passed on the unseen months. The top ones were nearly all
this ORB runner. Code: `tools/pdh_pdl/s3.py`, `search3.py`, `detail.py`.
