# E gate test: trend state vs range state (2026-11-25)

Script: `e_trend_gates.py`. Data: SPY 5-min, 173 sessions, 2026-03-23 to 2026-11-25.

**Signal:** a 5-min close above the session high so far (puts: below the low), 10:00–14:30, within a close band of the level, on volume ≥ N× the prior 10-bar average. **Stop:** the signal bar's low (min $0.30). **Exit:** +1.5R, the stop, or 15:00. Results are in R on SPY (no option decay; read as relative).

**Trend state** is known at signal time: the last 6 closes are on the trade's side of VWAP and VWAP has moved that way over 12 bars. Everything else is the range state.

| Band | Volume | Trend: n | Trend: R/trade | Range: n | Range: R/trade | Trend R/trade, 1st half / 2nd half |
|---|---|---|---|---|---|---|
| $0.30 | 1.5× | 52 | +0.20 | 19 | +0.08 | +0.25 / +0.14 |
| $0.30 | 1.0× (playbook E) | 88 | +0.23 | 27 | +0.05 | +0.37 / +0.06 |
| $0.75 | 1.2× (current extended band) | 95 | +0.12 | 35 | +0.00 | +0.18 / +0.05 |
| **$0.75** | **1.0×** | **99** | **+0.30** | **42** | **+0.15** | **+0.35 / +0.25** |
| $1.50 | 1.0× | 98 | +0.29 | 48 | +0.20 | +0.36 / +0.22 |
| $2.50 | 1.0× | 100 | +0.29 | 48 | +0.20 | +0.37 / +0.20 |

## Findings
1. **Trend state is the better place for E in every variant.** It earned about 2–4× the R per trade of the range state.
2. **The 1.5× bar is not better than 1.0×.** At 1.0× there are 70% more trades at a similar or higher R. The 1.2× row is the worst of the three, so the volume bar is noisy and has no smooth optimum.
3. **The best robust choice is the $0.75 band at 1.0×.** It is positive in both halves and in both states.
   - Wider bands ($1.50 / $2.50) add almost nothing on trend trades.
   - They lift range trades only slightly, with the lowest-volume entries.
   - So the no-chase limit is not what cost the big moves.
4. **Today's trend legs would still have been missed.** Their volume was 0.77–0.98× on the in-band bars. On quiet staircase trends, no reasonable volume bar catches each push.

## Change applied (standing tuning rule, change 8)
- The E/F extended band ($0.31–0.75) volume bar drops from 1.2× to **1.0×**. The QQQ condition is kept, which is more conservative than the test.
- Review after 10 signals or 2 weeks.
