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
