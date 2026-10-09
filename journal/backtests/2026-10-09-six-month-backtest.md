# Six-month backtest: SPY 5-min, 2026-03-23 to 2026-10-08 (139 days)

Owner asked (10/9): "How can you get profitable quicker?" and approved building a proper backtest.

## Method
- Data: Robinhood SPY + QQQ 5-min regular-hours bars, 139 sessions (`data/spy_qqq_5min.csv`). Script: `bt.py` (run `python3 bt.py data/spy_qqq_5min.csv`).
- Setups A, B, C, E and F coded as mechanical rules from the playbook (10/8 version). D is not modeled.
- Same rules for every variant: entries 9:45–2:25 (bar close), one position at a time, max 3 trades a day, stop after 2 losses, flat by 3:30, stop wins a tie with the target. Each trade is charged $0.04 SPY for slippage.
- **Walk-forward:** variants were judged on the TRAIN half (3/23–7/15, 79 days) and checked on the TEST half (7/16–10/8, 60 days), which they had not seen.
- Results are in R (multiples of the SPY stop distance). There is no option pricing yet; see "Dollars" below.

## Results

| Rules | Train n / avg R / PF | Test n / avg R / PF |
|---|---|---|
| Whole playbook (A+B+C+E+F, 10/8 rules) | 118 / +0.04 / 1.08 | 78 / +0.12 / 1.21 |
| Whole playbook, old 1.5× volume rule | 78 / −0.01 / 0.98 | 47 / +0.01 / 1.02 |
| Only A (ORB) | 1 / – | 1 / – (almost never qualifies as coded) |
| Only B (VWAP pullback) | 10 / +0.33 / 1.79 | 10 / −0.32 / 0.57 |
| Only C (break and retest) | 49 / −0.20 / 0.70 | 33 / +0.03 / 1.05 |
| Only E (close through a level) | 62 / +0.04 / 1.06 | 29 / −0.14 / 0.79 |
| **Only F (midday squeeze break)** | **38 / +0.18 / 1.35** | **28 / +0.50 / 2.26** |

F variants (train / test avg R): exit +1.0R +0.12/+0.32 · **exit +1.5R +0.18/+0.50** · exit +2.0R +0.26/+0.51 · exit at the next level +0.24/+0.19 · old 1.5× volume +0.41/−0.29 (only 13/6 trades) · band $0.20 −0.10/+0.28 · no QQQ filter +0.00/+0.18 · climax filter 3 ATR −0.09/+0.44 · F+B +0.21/+0.33 · F+C −0.09/+0.23 · F+E +0.11/+0.10.

**F as written (current rules), all 139 days:** 66 trades, 58% wins, +20.8R, +0.32R per trade, PF 1.67, max drawdown 4.3R, longest losing streak 4. Positive in 7 of 8 months (September −2.5R; August +12.7R carries a lot, and without August it is +0.15R per trade). Median stop distance $0.40 SPY. By entry hour: 11:xx +6.6R (10), 12:xx +0.9R (15), 13:xx +19.1R (27), **14:xx −5.7R (14)**.

## What this says
1. **The full playbook has no real edge after costs** (about +0.05–0.10R per trade). Most setups are noise; C and E lose in at least one half.
2. **Setup F is the only setup positive in both halves, with every tested exit.** Caveat: F was designed on 10/2 from missed moves in late September, which sit inside the test half, so the test number is flattered. The train half (March–July, never looked at) is the honest figure: about +0.18R per trade.
3. The 10/8 changes held up: the new volume rule beat the old 1.5× rule, and the +1.5R exit beat +1.0R and next-level exits.
4. 14:xx F entries lost money (−5.7R). This is a hypothesis to test, not a rule yet (14 trades).

## Dollars (the catch)
- At $25 risk per trade, +0.18 to +0.3R is about **$5–8 per trade, about 1 trade every 2 days**.
- **Fractional shares make this almost worthless in dollars:** a $250 SPY position with a $0.40 stop risks about $0.13.
- **0DTE options at the $25–50 cap force far out-of-the-money contracts** (10/8: the 771P cost $113 and the 767P $22). Those barely move on a $0.60 SPY target and lose to decay and spread. An at-the-money contract (about 0.5 delta, roughly $0.20 lost at a $0.40 SPY stop, +$0.30 at target) fits the edge much better but costs about $100–150 midday.
- Option pricing is not in this backtest yet. Next step: replay F trades with real option bars (Robinhood option historicals) at several strikes.

## Proposals for the owner (not applied)
1. Trade only setup F (plus B as a watch-only candidate) for the rest of paper trading; drop A, C and E from arming.
2. Arm triggers from code (`bt.py` logic run live) instead of by hand, to stop the wording errors seen this week.
3. Re-test with option prices before any real money.

## Addendum: $1,000 → $10,000? (owner goal, 10/9)
Monte Carlo: resample setup F's backtest trades 4,000 times and compound at a fixed risk per trade. Option losses can run to −1.3R on gaps. "Cost" subtracts 0.15R per trade for option spread and decay, which this backtest doesn't model yet.

| Edge assumed | Risk/trade | P(10× within ~4 yrs) | P(a 50% drawdown on the way) | Median time to 10× |
|---|---|---|---|---|
| All 6 months (+0.32R), no option cost | 5% | 100% | 7% | 1.3 yr |
| same | 10% | 99% | 47% | 0.7 yr |
| same | 20% | 87% | 81% | 0.4 yr |
| Train half only (+0.18R) − 0.15R option cost | 5% | 8% | 95% | 3.0 yr |
| same | 10% | 17% | 97% | 1.5 yr |
| same | 20% | 13% | 97% | 0.4 yr |

Read: 10× is plausible over 1–2+ years at the current 5–10% risk **only if** the edge is real and survives option costs. Raising risk to 20–30% barely speeds it up and makes a 50%+ drawdown near-certain. If the edge is closer to the honest train-half number after option costs, no risk level gets there reliably. These numbers rest on 66 backtest trades; the option-price replay and live paper trades are what will tell us which row we are in.
