# Trailing exit vs fixed 1.5R (2026-10-21)

Owner request after 10/20: on the same PDL sweep + VWAP reclaim the bot sold its 768C at the fixed target (+$44, +50%), while the owner trailed a stop-limit on a 770C and made +$193. Question: should the bot trail too?

Data: SPY/QQQ 5-min, 2026-01-02 to 10-15 (198 sessions). R = SPY risk per trade. Scripts: `tools/pdh_pdl/runner.py` (VWAP-reclaim line) and `tools/pdh_pdl/rangecap.py` (E lines, $0.30 band, $1.00 bar cap).

Exits compared: **fixed** = sell all at +1.5R (current rule); **trail 1R** = at +1.5R keep holding, stop to 1R behind the best price since entry, exit on the trail or 3:30; also half-off variants and trails on a close below VWAP / the 9 EMA.

| Line | Exit | Trades | Win rate | Total | Jan–Jun | Jul–Oct | Best trade |
|---|---|---|---|---|---|---|---|
| E lines | fixed | 212 | 43% | +18.2R | +5.1R | +13.1R | +1.5R |
| E lines | **trail 1R** | 212 | 43% | **+44.8R** | +25.6R | +19.2R | +5.7R |
| VWAP reclaim, long | fixed | 76 | 46% | +14.9R | +12.3R | +2.6R | +1.5R |
| VWAP reclaim, long | **trail 1R** | 76 | 46% | **+20.0R** | +13.1R | +6.9R | +5.0R |
| VWAP reclaim, short | fixed | 67 | 42% | +6.8R | +4.4R | +2.4R | +1.5R |
| VWAP reclaim, short | **trail 1R** | 67 | 42% | **+10.1R** | +5.6R | +4.5R | +4.4R |

- The trail keeps the win rate (a trade that reaches +1.5R locks at least +0.5R) and adds the big runs. Every trailing variant beat the fixed exit on every line.
- Trailing on a close below VWAP or the 9 EMA made more on some lines but won far less often (18–32%) and was uneven across the year; the 1R price trail was the most consistent, and it matches what the owner did with a stop-limit.
- Long reclaims that followed a PDL sweep specifically: 28 trades, fixed +7.6R vs trail +10.5R; not better than reclaims in general, so no sweep filter is added.
- Caveats: SPY points, not option prices (a 0DTE call held longer also decays); simplified simulators; 10/16–10/20 not in the data.

Decision (owner, 2026-10-21): adopt the 1R trailing exit on all lines (playbook section 7).
