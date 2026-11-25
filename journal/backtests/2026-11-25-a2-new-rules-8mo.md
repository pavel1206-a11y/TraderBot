# A2 new rules backtest: 8 months, 5-min SPY, modeled 0DTE contract (owner ask 2026-11-25)

Script: `a2_v2.py` (daily rows in `a2_v2_days.csv`). Data: SPY 5-min bars, 173 sessions, 2026-03-23 to 2026-11-25 (11/18–11/25 added today in `data/spy_5min_1118_1125.csv`).

## Method
- **Signals (5-min):**
  - **Cross:** the first close beyond the 9:30–9:45 high/low, then the next close still beyond it. Stop: range midpoint ∓ $0.10.
  - **Swoop:** a one-sided poke past a mark that closes back inside, or a cross undone on the next bar. Trade the other way. Stop: the poke's extreme ∓ $0.10 (the midpoint stop can't work for a swoop because it sits on the wrong side of entry).
  - One trade a day, on the first signal.
- **Exit (the current rule):** half at +50%, the rest trailed one 5-min bar behind (never below entry), out at 11:00.
- **Option model:**
  - Black-Scholes, with IV taken from the trailing 10-day realized vol.
  - $0.03 slippage each way.
  - If a bar touches both the stop and a profit level, the stop is assumed hit first.
  - Dollar levels are approximate (see the 11/17 test's check against real fills); compare variants against each other.

## Results (one contract per signal)
| Variant | Trades | Win | Total | Mar–Jun | Jul–Oct 8 | Oct 9–Nov 25 | Max DD | Without top 3 days |
|---|---|---|---|---|---|---|---|---|
| 1. Old rules ($0.75–1.25, to 10:30, no swoop) | 126 | 44% | **−$409** | −$332 | −$200 | +$123 | −$672 | −$917 |
| 2. New band only ($1.25–1.75) | 92 | 43% | −$527 | −$503 | +$45 | −$69 | −$733 | −$1,123 |
| 3. 10:15 cutoff only | 104 | 44% | −$427 | −$352 | −$114 | +$40 | −$690 | −$935 |
| 4. Swoop only | 166 | 43% | +$31 | −$23 | −$315 | +$368 | −$724 | −$559 |
| **5. New rules (all three)** | 119 | 46% | **+$484** | +$71 | −$32 | +$446 | **−$379** | −$196 |
| 5b. New rules, every signal (nearest to $1.50 within $0.75–1.75) | 159 | n/a | **+$591** | +$179 | −$144 | +$556 | n/a | n/a |
| 6. New rules with the old band | 159 | 44% | +$160 | +$26 | −$274 | +$408 | −$624 | −$430 |

- **Split by signal type (new rules):** swoops 74 trades **+$579**; crosses 45 trades **−$105**. Crosses alone with the new band and cutoff: 78 trades, **−$531**.
- **Selection check:** variant 5 skips 40 signal days that have no contract in $1.25–1.75. Those days made −$106 under the old band. Trading every signal at the nearest-to-$1.50 contract (5b) still gives +$591, so the gain is not from skipping days.

## Findings
1. **The new rules beat the old ones by about $900 over 8 months** (−$409 → +$484). Max drawdown fell by almost half ($672 → $379). The improvement holds in every period except Jul–Oct 8, where it is roughly flat (−$32 vs −$200).
2. **Almost all of the gain comes from the swoop.**
   - Crosses have no edge in this data: every cross-only variant loses.
   - The closer-to-ATM band helps only when combined with the swoop. Bigger contracts mean bigger wins (+$72 average vs +$53) and bigger losses (−$54 vs −$40).
   - The **10:15 cutoff alone adds nothing** (−$427 vs −$409). It is neutral, and it keeps the decay problem out of live trading.
3. **Swoops depend on the regime.** They lost in Jul–Oct 8 (−$273 over 25 trades) and won in Mar–Jun (+$432) and Oct 9–Nov 25 (+$420).
4. **The result is not robust yet.** Without its 3 best days, the new rule set is −$196. The edge is real against the old rules, but it rests on a modest number of big days.

## Proposed next test (owner's call; not changed)
**Swoops only:** drop A2 cross entries. Crosses lost money in all three periods. Judge it on the next 10 live paper signals before changing the rule.
