# Setup F exit study (owner OK, 2026-10-10)

Same 66 F entries as the 10/9 backtest (current rules), each re-managed with 10 exit plans (`f_exits.py`). SPY in R; options in dollars with the Black-Scholes model from `optbt.py` ($100 cap: one contract, or two ≤ $50 contracts for plans that sell half). Train = before 7/16, valid = 7/16–10/8. Note: option figures here step to a farther strike to fit the cap, so the "current" row differs a little from the 10/9 report, which skipped those trades.

| Exit plan | SPY R/trade train / valid | Option $/trade train / valid | Option win % train / valid |
|---|---|---|---|
| **Current: target 1.5R** | +0.18 / +0.50 | −2.55 / +4.52 | 45 / 64 |
| Break-even after +0.5R, target 1.5R | +0.21 / +0.23 | −0.49 / +1.73 | 34 / 39 |
| Half at +0.5R, rest BE, target 2R | +0.14 / +0.06 | −2.14 / −6.73 | 29 / 25 |
| Half at +0.5R, rest BE, hold to 3:25 | +0.29 / +0.10 | +3.95 / −8.73 | 18 / 7 |
| Half at +1R, rest BE, target 2R | +0.15 / +0.34 | −2.09 / −0.66 | 34 / 57 |
| **Trail 0.5R after +0.5R** | **+0.31 / +0.37** | **+1.04 / +2.02** | 42 / 54 |
| Trail 1R after +1R | +0.19 / +0.30 | +2.36 / −0.74 | 29 / 43 |
| Half at +0.5R, rest BE, trail 0.5R | +0.18 / +0.17 | −2.47 / −3.91 | 34 / 43 |
| Half at +1R, rest BE, trail 1R | +0.18 / +0.31 | +0.67 / −1.46 | 37 / 57 |
| Half at +0.25R, rest BE, target 1.5R | +0.05 / −0.10 | −4.12 / −9.22 | 24 / 21 |

Checks on the trailing plan:
- Neighbors (trail 0.3–0.75R, starting at +0.3/+0.5/+0.75R): SPY R positive everywhere (+0.18 to +0.53R). In options, starting the trail at +0.5R or +0.75R was positive in both halves in 9 of 10 combinations (exception: 0.75R trail after +0.75R, train −$0.59); starting at +0.3R tended to lose on valid. So "start trailing after +0.5–0.75R, trail 0.4–0.6R" is a stable region, not a single lucky point.
- Last month (9/10–10/8, 10 trades): trail −1.58R / −$44 options vs current +1.36R / +$2. Worse.
- Lockbox (2/23–3/20, 6 trades; opened before for the entries, never for exits): trail −2.73R / −$70 vs current −1.52R / −$55. Both lose.
- Option slippage: $0.01/side +$3.04 / +$4.02 per trade; $0.02 +$1.04 / +$2.02; $0.03 −$1.05 / +$0.02.

## Read
1. Selling half early (the 80% win-rate idea) **hurts F in options**: the $100 cap forces two cheaper, farther-OTM contracts, and the early half sells for little. Not recommended.
2. A **trailing stop after +0.5R** is the most consistent improvement: better than the 1.5R target in SPY terms in both halves and slightly positive in options in both. Its option win rate is ~42–54%, not 80%.
3. It is still a thin edge: about $1–2 per contract per trade at $0.02 slippage, gone at $0.03, and it lost in the last month and the lockbox.

## Proposal (not applied; owner decides)
Paper-trade F forward with the trailing exit logged alongside the current 1.5R exit on every F trade (same entry, two exit columns), and buy options with limit orders at the mid. After 15–20 forward F trades, keep whichever exit did better.
