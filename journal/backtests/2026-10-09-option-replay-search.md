# Option-priced replay and parameter search, setup F (10/9)

Owner asked (10/9): "Replay over and over until you get it right and in positive."

## Protocol (so a lucky fit can't pass as an edge)
- **TRAIN** 2026-03-23..07-15 (79 days): every variant is ranked here only.
- **VALIDATION** 07-16..10-08 (60 days): the top TRAIN variants are checked here. Caveat: F was designed from late-September moves, which sit inside this window.
- **LOCKBOX** 2026-02-23..03-20 (19 days, `data/LOCKBOX_spy_qqq_5min.csv`): never looked at, opened once for the single pre-chosen rule set. (Robinhood keeps real 5-min bars only back to ~2/23; earlier bars come back interpolated.)
- **Option P&L** (`optbt.py`): Robinhood keeps 5-min option bars for only about 3–4 weeks, so prices are modeled with Black-Scholes. IV = 2.3 × realized 5-min vol, calibrated on real 0DTE quotes from 10/6 and 10/8. Checked against real bars (10/6 780P, 10/5 774C): close, slightly conservative on wins. One near-the-money 0DTE contract, $100 premium cap, $0.02 slippage each side.

## Results
- **Grid search:** 576 combinations of exit (1.0/1.5/2.0R), strike (ATM, 1–2 OTM), last entry time, squeeze length and width, entry band, volume rule and start time.
  - Only **65 of 576 were positive on TRAIN**, about what luck alone would produce.
  - The best TRAIN result with ≥ 25 trades was **+$0.30 per contract per trade**.
- **Current F rules in option dollars:**

| Data | Trades | Win rate | Avg per trade | Total |
|---|---|---|---|---|
| TRAIN | 32 | 44% | −$1.13 | −$36 |
| VALIDATION | 26 | 65% | +$5.33 | +$139 |
| **LOCKBOX** | 5 | 40% | **−$6.27** | **−$31** |

  In SPY terms the lockbox was 6 trades and −0.25R.
- **Cost sensitivity (TRAIN avg per trade):** $0.02 slippage −$1.13 · $0.01 +$0.84 · $0.00 +$3.02. Each cent of bid/ask cost per side is worth about $2 a trade, which is the whole edge.
- **Why options hurt:** in SPY terms F wins 1.5R vs loses 1R. In option dollars it averaged about +$21 vs −$18, because time decay and the spread take most of the gap.

## Verdict
1. **No version of F (or the full playbook) has shown a reliable, cost-proof edge on data it was not tuned on.** The validation profit is flattered by design bias, and the lockbox lost money.
2. Re-running "until positive" would select noise: with 576 tries, dozens look good by chance. The protocol above exists to catch that, and it did.
3. Only forward paper trades (new days) can now add honest evidence. Hypotheses worth tracking forward, not adopting:
   - no F entries after 2:00 PM (14:xx entries lost in all three windows);
   - limit orders at the mid to cut option costs.
