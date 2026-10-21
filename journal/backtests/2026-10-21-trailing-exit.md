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

## Check on 10/16–10/20 (owner request, 2026-10-21)

Added the 10/16, 10/19 and 10/20 bars and replayed the six real paper trades with the trailing exit (5-min bars):

| Trade | R | Fixed 1.5R | Trail 1R | Trail 1.5R | Trail 2R |
|---|---|---|---|---|---|
| 10/16 2:25 E short | $0.40 | −1.0R | −1.0R | −1.0R | −1.0R |
| 10/19 10:00 E short | $0.40 | −1.0R | −1.0R | −1.0R | −1.0R |
| 10/19 10:15 VWAP reclaim long | $0.46 | −1.0R | −1.0R | −1.0R | −1.0R |
| 10/19 11:15 E long | $0.40 | +1.5R | +1.85R (out 11:30) | +1.35R | +0.85R |
| 10/19 1:10 E short | $0.40 | +1.5R | +0.83R (out 1:50) | +0.33R | 0.0R |
| 10/20 9:50 VWAP reclaim long | $0.69 | +1.5R | +1.81R (out 10:05, by $0.03) | **+6.9R** | +6.4R |
| **Total** | | **+1.50R** | **+1.49R** | +5.58R | +4.25R |

- With the adopted 1R trail, these four days come out the same as the fixed exit. On 10/20 the 1R trail ($0.69) was hit at 10:05 by 3 cents (peak $768.42, stop $767.73, low $767.70), so it would not have caught the run the owner caught; the owner's option stop was wider.
- A 1.5R trail catches 10/20 (+6.9R) but over the full Jan–Oct 20 data it is weaker than 1R in Jul–Oct (E lines +9.3R vs +20.0R; VWAP reclaim +20.0R vs +27.1R). A 2R trail scores highest on E lines (+67.9R) but wins only 36% of trades and does worse on the VWAP reclaim (+19.1R).
- Full-period totals including 10/16–10/20: E lines fixed +18.7R vs trail 1R +45.6R; VWAP reclaim (long + short) fixed +18.7R vs trail 1R +27.1R.
- Conclusion: keep the 1R trail; it is the most consistent across lines and periods. Do not widen it to fit one day. Revisit at the Friday review with more live trades.
