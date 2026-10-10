# First-candle breakout test (owner question, 2026-10-10)

Rule: mark the 9:30 candle's high and low; enter on whichever side breaks first (1 cent through), checked on 1-minute bars. Cost $0.02/share. Script: `orb_first_candle.py`.

## Last month (22 sessions, 2026-09-10 to 2026-10-09, 1-minute data)

| Range candle | Exit | Profitable days | Net per share |
|---|---|---|---|
| 5-min (9:30–9:35) | stop at other side, target 1R | **11 of 22 (50%)** | −$1.91 |
| 5-min | stop at other side, target 2R | 8 of 22 (36%) | −$4.22 |
| 5-min | stop at other side, hold to 3:55 | 5 of 22 (23%) | −$1.74 |
| 5-min | no stop, hold to 3:55 | 10 of 22 (45%) | +$12.06 |
| 1-min (9:30) | stop, target 1R | 7 of 22 (32%) | −$5.03 |
| 1-min | stop, target 2R | 6 of 22 (27%) | −$3.46 |
| 1-min | stop, hold to 3:55 | 4 of 22 (18%) | +$1.97 |
| 1-min | no stop, hold to 3:55 | 10 of 22 (45%) | +$6.95 |

## Longer check (139 sessions, Mar 23 – Oct 8, 5-minute data, 5-min candle)
All stopped versions lost in both halves (1R: 45% / 44% winners, about −0.13R per trade). No-stop hold-to-close: −$10.01 (Mar–Jun), +$3.09 (Jul–Oct). On 5-minute data a bar that breaks both sides counts as a loss, which leans slightly negative.

## Read
A break of the first candle is close to a coin flip on SPY. The only positive month-long result (no stop, hold to close) breaks the "every trade has a stop" rule, and it lost over March–June. Not a candidate for the playbook as is.

## Follow-up: "make it 80–90%" (owner, 2026-10-10)
Search: 640 combinations (`orb_search.py`): entry on touch or 5-min close; target 0.25–1.5R; stop at the other side or the midpoint; filters for gap direction, QQQ also breaking its first candle, VWAP side, candle width ≤ $1, cutoff 10:30 or 3:00. Ranked on Mar–Jun, checked on Jul–Oct 8.

- **No combination reached 80% on Mar–Jun with 20+ trades, and none above 73% made money there.**
- Highest win rate: touch entry, QQQ must also break its first candle, stop at the other side, **target 0.25R**. Win rate 73% (Mar–Jun) and 86% (Jul–Oct). Over all 6 months: 68 trades, **79% wins, avg win $0.36, avg loss −$1.37, net +$0.21/share** (≈ breakeven). By month: Mar −$2.41, Apr −$2.54, May +$0.73, Jun +$0.89, Jul −$1.59, Aug +$3.90 (12/12), Sep +$0.77, Oct +$0.46.
- Why: a high win rate here comes from a tiny target and a wide stop. At 80% wins the break-even payoff is avg win ≥ 0.25 × avg loss; this rule sits right at that line (0.26×), so one extra loss a month wipes it out. 0DTE option spread and decay on a $0.25–0.40 SPY target would push it negative.
- Verdict: an 80–90% win rate is reachable, but only by trading a small, frequent win for a rare large loss, and it does not make money. Not recommended for the playbook.
