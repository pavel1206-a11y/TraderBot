# Paper Trade Journal

Practice phase: no real money. Every A or B grade setup from
`../strategies/playbook.md` is logged here as if it had been taken, using real
quotes for the contract. Rules for graduating to real money are in
`../CLAUDE.md`.

## Scoreboard

| Closed trades | Trades | Wins | Losses | Win rate | Avg win | Avg loss | Net P&L |
|---|---|---|---|---|---|---|---|
| Options, A grade | 0 | 0 | 0 | – | – | – | $0 |
| Options, B grade | 2 | 1 | 1 | 50% | +$42 | -$19 | +$23 |
| Fractional, A grade | 0 | 0 | 0 | – | – | – | $0 |
| Fractional, B grade | 2 | 0 | 2 | 0% | – | -$0.12 | -$0.24 |
| **All** | 4 | 1 | 3 | 25% | +$42 | -$6.41 | +$22.76 |

Open: none.

By setup: ORB 0 · VWAP pullback 0 · Break and retest 4 · 4H manipulation 0

Exit rule used for options: sell at the first target (+50%) with a limit order;
the trailing rules in playbook section 7 apply only if price moves before the
first target is reached.

Would the $25–50 premium cap have allowed the trade? Track "fits cap: yes/no"
on each entry.

---

## Template

### YYYY-MM-DD HH:MM ET: SPY call/put, strike, expiry

- Setup: ORB / VWAP pullback / break and retest
- Score: X/10, grade A/B. Factors: ...
- Contract: bid/ask at entry, entry price (ask), fits cap: yes/no
- Stop: option price (and underlying invalidation level)
- Target: option price (and underlying level)
- Result: exit time, exit price (bid), how (stop / target / time stop / 3:30 close)
- P&L per contract: $ and %
- Note:

---

## Daily log

### 2026-09-29 (Tue)

**Pre-market brief (9:16 AM ET)**
- SPY pre-market $766.79 (+0.15%); QQQ +0.34%, IWM +0.21%.
- Yesterday: high $769.54, low $763.72, close $765.61.
- Pre-market: high $767.73, low $762.75.
- Pivots (from yesterday): R1 $768.86, P $766.29, S1 $763.04.
- 20-day SMA $765.16, 50-day SMA $762.01.
- Strong levels: $769.5–770 (yesterday's high + round), $765–765.6 (20-day SMA + close + round), $763–763.7 (S1 + yesterday's low).
- News: 10-year yield ~5.2%+, oil up on Iran / Strait of Hormuz tension, Fed hike fears; Monday's selloff hit tech and autos.
- Events: possible 10:00 AM data (last Tuesday of the month; unverified). No market-moving earnings.
- **Bias: none.** Slight green pre-market against a bearish macro backdrop. Let the opening range decide; watch $765 and $769.5.

**Setup check (9:57 AM ET): no trade**
- Opening range (9:30–9:45): high $766.94, low $764.94. SPY $765.26, inside the range.
- Price within $0.20 of VWAP ($765.47) and crossing it: chop.
- Score (bearish lean) 4/10, grade C. Scored: EMA stack (price < 9 EMA $765.37 < 21 EMA $765.77), momentum (RSI 42, MACD below signal), news (yields/oil).
- Missed: VWAP direction unclear, ADX 21 and falling, no lower-high/lower-low structure, sitting on $765 support, no volume breakout, daily trend still above 50-day SMA.
- Watch: a 5-min close below $764.94 (range low) under VWAP, or above $766.94 over VWAP.

**Spot check (10:39 AM ET): no trade**
- SPY $765.33, stuck in $764.60–765.75 for 40 minutes; VWAP flat at $765.29; ADX down to 15 (chop).
- 9:55 bar closed $764.72, below the opening-range low, but reversed straight back: a failed breakdown. The ADX filter (under 20) would have kept us out.
- QQQ grinding up ($739.70) while SPY is flat: the two disagree, another no-trade filter.

**Setup check (11:57 AM ET): no trade**
- SPY sold off 11:00–11:30 from ~$764.9 to $762.57, breaking the $763 support zone, then bounced to $763.90.
- Score (bearish) 5/10, grade C. Scored: below a falling VWAP ($764.65), selloff volume, momentum (RSI 36, MACD below signal), QQQ agrees, news.
- Missed: ADX 17.8 (required, under 20), price back above the 9 EMA ($763.69), higher lows since the bounce, bounce came off the 50-day SMA area ($762.01–762.75), daily trend.
- Note: the move happened between check-ins (11:00–11:30). A setup may have scored higher mid-move; this is a known limit of checking 3 times a day.
- Watch: a rejection at $764–764.65 (the broken zone and VWAP) would set up a bearish break-and-retest.

**Setup check (1:58 PM ET): no trade (last entry window)**
- SPY $763.05, drifting in a tight $762.35–763.56 range for 2 hours, pressing the $762–762.75 support (50-day SMA, pre-market low).
- Score (bearish) 4/10, grade C. Scored: below falling VWAP ($764.19), ADX 20.6 (just over), QQQ agrees, news.
- Missed: EMAs tangled (9 EMA $762.99, 21 EMA $763.11), no clean lower-high structure, shorting into support, no volume breakout, MACD crossed above signal, daily trend.
- No new entries after 2:30 PM, so no paper trades today.

**End of day (3:48 PM ET)**
- Paper trades: 0. P&L: $0. Running totals: 0 trades, $0.
- Day: chop around $765 all morning, a selloff 11:00–11:30 to $762.57 that stalled at the 50-day SMA, a slow drift, then a bounce after 2:00 PM back to ~$765.30 (SPY ~$764.6 at 3:30).
- Lesson: no setup reached B grade. The fake 9:55 breakdown and the support bounce both show why the ADX filter and "don't sell into support" matter. The one real move (11:00–11:30) fell between check-ins.

### 2026-09-30 (Wed)

**Pre-market brief (9:17 AM ET; scheduled brief was late)**
- SPY pre-market $767.10 (+0.38%); QQQ +0.44%, IWM +0.45%.
- Yesterday: high $766.98, low $762.35, close $764.20.
- Pre-market: high $768.37, low $763.23. Big swing in the 8 AM hour ($763.87–768.37), likely the 8:30 data.
- Pivots (from yesterday): R2 $769.14, R1 $766.67, P $764.51, S1 $762.04.
- 20-day SMA $765.02, 50-day SMA $762.45.
- Strong levels: $768.4–769.5 (pre-market high, R2, Monday's high), $766.7–767.0 (R1 + yesterday's high), $764.2–765.0 (close, pivot, 20-day SMA), $762.0–762.5 (S1 + 50-day SMA).
- 4H (setup D): the 8 AM–12 PM candle opened $764.91 and pushed up through yesterday's high ($766.98) to $768.37. Watch: a 5-min close back below $766.98 plus a lower-low shift = bearish manipulation (setup D); holding above it = real breakout.
- News: PCE inflation data due today (release result not confirmed); ADP jobs reported stronger than expected; Micron earnings after the close (can move QQQ tomorrow, not today).
- **Bias: bullish lean**, only while SPY holds above $766.7–767.0.

**Setup check (9:58 AM ET): no trade**
- Opening range (9:30–9:45): high $767.28, low $766.00. SPY $767.32, closing just over the range high on the lowest-volume bar of the day.
- 4H (setup D): the pre-market push to $768.37 took out yesterday's high; the open dipped back below $766.98 (closes $766.66–766.85) but made no lower low and is back above. No bearish shift, so no setup D. Treat as a breakout attempt.
- Score (bullish) 5/10, grade C. Scored: above rising VWAP ($766.73), ADX 27 rising, EMA stack (price > 9 EMA $766.15 > 21 EMA $765.29), higher timeframe, QQQ agrees.
- Missed: candles choppy inside the range, key level (buying $1 under the $768.4–769.5 resistance zone), weak breakout volume, RSI 75 (overbought), news mixed (PCE/strong jobs).
- Reward/risk also fails: stop under the range ($765.90) vs target $768.40 is under 1:1.
- Watch: a pullback to VWAP (~$766.7–766.8) that holds = setup B, stop ~$766.40, target $768.40 (about 4:1). Or a close above $768.40 on strong volume.

**Setup check (11:58 AM ET): no trade**
- SPY rallied after 10:00 to $769.15, then ranged $767.25–769.41; now $769.18, pressing Monday's high ($769.54).
- Missed between check-ins: the 10:30–10:40 dip to $767.25–767.37 near VWAP held, then ran to $769.41. That is the VWAP pullback flagged at 9:58. Not logged as a paper trade (no hindsight entries).
- 4H: the 8 AM–12 PM candle is in distribution up (open $764.91, high $769.41, no manipulation sweep after the open). The 12–4 PM candle starts next.
- Score (bullish) 6/10, grade B. Scored: above rising VWAP ($767.92), ADX 26, EMA stack (9 EMA $768.48 > 21 EMA $768.12), higher lows, higher timeframe, QQQ agrees (new highs $745.02).
- Missed: buying into Monday's high ($769.54), average volume, MACD below signal, news neutral.
- No trade anyway: reward/risk fails. Stop under the range (~$767.70) vs room to $769.54–770 is under 1:1.
- Watch: a 5-min close above $769.54 on strong volume. Stop ~$768.90, target $772.30 (Sep 25 high), about 3:1.

**Setup check (1:57 PM ET): no trade (last entry window)**
- 4H (setup D, bullish forming): the 12–4 PM candle opened $768.72, dropped at 1:10 PM through the morning range low ($767.25) to $766.26 (sweep), closed back above it (reclaim), and the 1:40 bar closed $767.86 over the last lower high ($767.18) (structure shift). Phase: manipulation done, distribution starting.
- Not an entry yet: VWAP ($767.91) not reclaimed (price $0.05 under). ADX 17.8 (required, under 20). Reward/risk also short: VWAP entry ~$768.0, stop $766.16, target 4H high $769.10–769.41 is about 1.1–1.4:1.
- Score (bullish) 4/10, grade C. Scored: key level (sweep + reclaim), higher timeframe, QQQ agrees (same sweep and bounce), candles (shift).
- Missed: VWAP, ADX, EMAs (9 EMA $767.59 < 21 EMA $767.76), volume, momentum (RSI 49, MACD below signal), news.
- Useful example for setup D: the pattern formed cleanly, but the room to the target was too small again.

**End of day (3:48 PM ET)**
- Paper trades: 0. P&L: $0. Running totals: 0 trades, $0 after 2 days.
- Day: bullish open and rally to $769.41 by late morning, a range under Monday's high ($769.54), then a 1:10 PM drop to $766.26 and a fade to ~$766.3 by 3:30.
- Lesson: the bullish setup D forming at 1:57 failed. SPY touched VWAP (~$767.97) but never held above it, then fell to $766.01, below the sweep low. The VWAP-reclaim requirement kept us out of a loser.
- Two days, 0 trades: filters and reward/risk blocked every setup. The one clean winner (10:30 VWAP pullback) came between check-ins.
- Note: SPY kept falling after the 3:30 note and closed at $762.63 (day low $762.18).

### 2026-10-01 (Thu)

**Pre-market brief (8:53 AM ET)**
- SPY pre-market $765.00 (+0.31%); QQQ +0.46%, IWM +0.23%. MU -1% after earnings.
- Yesterday: high $769.41, low $762.18, close $762.63 (closed near the low).
- Pre-market: high $767.87, low $761.93 (both swept in the 4–8 AM 4H candle).
- Pivots: R2 $771.97, R1 $767.30, P $764.74, S1 $760.07.
- 20-day SMA $765.06, 50-day SMA $762.74.
- Strong levels: $767.3–767.9 (R1 + pre-market high), $764.7–765.1 (pivot + 20-day SMA), $762.2–762.7 (yesterday's low/close + 50-day SMA), $760.1–761.9 (S1 + pre-market low). Above: $769.4 (yesterday's high).
- News: PCE came in benign (core +0.2%) with strong spending (+0.9%); ACN beat; Nike reports after the close. Possible 10:00 AM data (first business day of the month, e.g. ISM manufacturing; unverified): the 9:57 check waits for the reaction.
- **Bias: none.** Green pre-market, but price sits mid-range after a weak close. Above $765.1 and VWAP leans bullish toward $767.3–767.9; below $762.7 leans bearish toward $760–762.

**Setup check (9:58 AM ET): no trade (waiting on 10:00 data)**
- Opening range (9:30–9:45): high $765.33, low $763.21. The 9:45 bar broke below it to $762.61 (yesterday's close / 50-day SMA support) and the 9:50 bar snapped back to $763.76.
- Bearish read 6/10 (B on paper): below falling VWAP ($764.01), ADX 45, EMAs bearish (9 EMA $764.10 < 21 EMA $765.09), lower highs, selloff volume, RSI 40 / MACD below signal.
- Why no trade: (1) possible 10:00 AM report, playbook waits for the reaction; (2) price just swept and bounced off the $762.2–762.7 support zone (selling into support); (3) QQQ is bouncing hard ($740.39 to $742.32), not confirming.
- 4H: the 8 AM–12 PM candle swept the opening-range low into support and bounced: possible bullish setup D, not confirmed (needs a close over $763.92 and a VWAP reclaim).
- Watch after 10:00: (a) bearish: a 5-min close under $762.60 that holds, target $760.1–761.9; (b) bullish D: close over $763.92 + hold above VWAP, stop ~$762.50, target $767.30.

**Setup check (10:58 AM ET): PAPER TRADE OPENED (bearish, grade B)**
- What happened: the 10:00 data hit, SPY broke the $762.2–762.7 support zone and fell to $759.72. It bounced to $762.18 at 10:40, failed right at VWAP/the broken zone, and turned back down. Setup C: bearish break and retest.
- Score 7/10, grade B. Scored: below falling VWAP ($762.20), ADX 53, EMAs bearish (price < 9 EMA $761.29 < 21 EMA $762.37), lower high at $762.18, daily trend (below 20- and 50-day SMA), QQQ agrees (rejected $740.8), news (selloff on the 10:00 data).
- Missed: key level (price near S1 $760.07 / day low $759.72), volume average, MACD just crossed above signal.

### 2026-10-01 10:58 ET: SPY 759 put, 0DTE (paper)
- Setup: C, break and retest (bearish)
- Score: 7/10, grade B
- Contract: bid $0.82 / ask $0.83, entry $0.83 (ask), delta -0.32. Fits cap: **no** ($83 > $50 max).
- Stop: $0.45 on the option (-46%), or SPY back above $762.28 (retest high + $0.10)
- Target: $1.25 (+50%) to $1.66 (+100%); SPY $757.50 (S2)
- Result: **closed 11:00–11:05 AM at $1.25 (first target, limit sell)**. The option traded up to $1.47–1.66 as SPY hit $759.00. Stop never threatened.
- P&L per contract: **+$42 (+51%)**
- Note: fits-cap = no, so this result does not count toward the real-money cap test. With the section 7 trailing stop instead, the exit would have been $1.08 (+$25) after the pullback at 11:10.

### 2026-10-01 10:58 ET: SH fractional, $125 (paper, B grade = half size)
- Setup: C, break and retest (bearish); SPY $760.72 at entry
- Entry: SH $32.48 (ask), 3.848 shares
- Alert-stop: SH $32.41 (= SPY $762.28); risk about $0.27
- Target: SH $32.62 (= SPY $757.50); reward about $0.53; reward/risk 2.1:1
- Exit by 3:45 PM ET
- 11:58 update: SPY low $759.00 (SH high $32.55), not at target $32.62; SPY high since entry $761.33, stop not hit. SH now $32.485 (+$0.02).
- Stop trailed (stops only move in favor): to SPY $760.96, above the latest lower high $760.86 = SH about $32.47, roughly break-even.
- Result: **stopped 12:00–12:05 PM** when SPY rose to $761.25 (trailed stop $760.96). Sold at market, SH about $32.46.
- P&L: **-$0.08** (-0.06%), a scratch. The trail turned a 2:1 trade into break-even; SPY never reached the $757.50 target.

**Setup check (11:58 AM ET): updates only, no new trade**
- SPY $760.64, range $759.00–761.33 for the past hour (chop around S1 $760.07). No new entry while the range holds.
- 759 put closed at the +50% target (+$42, paper). SH still open with the stop trailed to break-even.
- 4H: the 8 AM–12 PM candle is in distribution down (open ~$765, low $759.00). The 12–4 PM candle starts next.

**Setup check (12:57 PM ET): SH stopped (scratch), no new trade**
- SH trailed stop hit at 12:00 (SPY $761.25 > $760.96): -$0.08.
- SPY rallied 12:00–12:35 to $762.57 (into the broken $762.2–762.7 zone), above VWAP, then fell back to $760.89, below VWAP ($761.54). Price crossing VWAP back and forth = chop filter, no trade. ADX 24 and falling.
- 4H: the 12–4 PM candle opened ~$760.7, pushed up into the broken zone and got rejected. If it rolls over below $759.00 (day low), that is bearish distribution; not there yet.

**Setup check (1:58 PM ET): no trade (last entry window)**
- Reversal: SPY rallied 1:10–1:50 PM from $760.3 to $765.32 on strong volume (540k+ per 10 min), reclaiming the broken $762.2–762.7 zone and VWAP. Now $764.53, just under the $764.7–765.1 resistance (pivot + 20-day SMA). QQQ ripped too ($737.7 to $744.7).
- Score (bullish) 7/10, grade B on the card. Scored: above rising VWAP ($762.00), ADX 30 rising, EMA stack (9 EMA $763.72 > 21 EMA $762.81), higher highs/lows, volume, momentum (RSI 59, MACD above signal), QQQ agrees.
- Missed: key level (at the $764.7–765.1 resistance; $765.32 high already tagged), daily trend (below 20-day SMA), news.
- Why no trade: no playbook setup has triggered. This is a straight run, not an ORB, VWAP pullback, retest, or 4H sweep (the 12–4 PM candle never swept the $759.00 day low). The entry would be a pullback to the 9 EMA/VWAP ($762.0–763.7) or a retest of $762.7 that holds, and there is no check before the 2:30 cutoff to catch it.
- 4H: the 12–4 PM candle opened ~$760.7 and is in distribution up (no sweep first).

**End of day (3:48 PM ET)**
- Paper trades today: 2 (both setup C, bearish break-and-retest, B grade). 759 put +$42 (over cap), SH -$0.08. Day: +$41.92.
- Running totals: 2 trades, 1 win, 1 loss, +$41.92 after 3 days. Trades counting toward the cap test: 1 (SH).
- Day: weak open, 10:00 data broke support, selloff to $759.00, two hours of chop, then a 1:10–1:50 PM run to $765.32 that held $763.3–765.2 into the close (~$764.5 at 3:30).
- Lesson: the bearish retest worked fast for the option (target in minutes) but the fractional target was too far. The afternoon run had no defined entry: added setup E (momentum run) and half-hour checks starting tomorrow.

### 2026-10-02 (Fri)

**Pre-market brief (8:54 AM ET)**
- SPY pre-market $770.49 (**+0.85%, gap up ~$6.50**); QQQ +1.17%, IWM +1.4%. Jumped from ~$767.4 to $770.5 in the 8 AM hour, likely the 8:30 jobs report (result not confirmed).
- Yesterday: high $765.65, low $758.79, close $763.99.
- Pivots: R3 $773.69, R2 $769.67, R1 $766.83, P $762.81, S1 $759.97.
- 20-day SMA $765.00, 50-day SMA $763.07.
- Strong levels: $774.9–775.1 (9/21–22 highs), $772.3 (9/25 high), **$769.4–769.7** (R2 + 9/28 and 9/30 highs; first support if the gap holds), $766.8–767.9 (R1 + pre-market base), $765.0–765.65 (20-day SMA + yesterday's high).
- Gap rule (missed-move review): gap days of $4+ that hold the first 15 minutes trended all day (9/21, 9/23). Above $769.5 after 9:45 = gap-and-go ORB long; losing $769.4 = gap-fill risk toward $767–765.
- News: risk-off tone in the morning headlines (strong dollar, yields), but futures sharply higher on the 8:30 data. No big earnings.
- Friday: weekly review at the close.
- **Bias: bullish** while above $769.4.

**Setup check (9:59 AM ET): no trade (failed ORB, chop at VWAP)**
- Opening range (9:30–9:45): high $771.65, low $769.49. Held the $769.4 gap support.
- 9:45 bar broke the ORB high to $772.09 (on 349k, about average) and closed back inside at $771.38. 9:50 bar fell to $770.16, closing below VWAP ($770.82). Now $770.11. Failed breakout, so no ORB long.
- QQQ $751.8, still above its open-range middle and green; SPY/QQQ diverging.
- Score (bullish) 4/10, grade C. VWAP fails (price below a flat VWAP); ADX 44 is inflated by the overnight gap. Bearish not scored: the gap support at $769.4 is intact and QQQ disagrees.
- Watch: $769.4 lost on volume = gap-fill short toward $767.9–767.0 (setup C on a retest). Reclaim $771.65 and hold above VWAP = second-chance ORB long toward $772.3–773.7.
- 4H (8 AM–12 PM): opened ~$767.4 and ran straight up to $772.09 (distribution up, no sweep first). No setup D.
- Squeeze (F): only 30 minutes of range ($769.49–772.09, $2.60 wide). Not valid yet.

**Setup check (10:28 AM ET): no trade (breakout on light volume, RSI stretched)**
- 9:55 bar swept the $769.4 support to $769.07 on 495k, then reclaimed it. SPY has climbed since, with higher lows, back above VWAP ($770.94). The 10:20 bar closed at $772.35, above the ORB/day high ($772.09) and the $772.3 level (9/25 high). Now $772.27. QQQ $754.47, above its VWAP ($751.81) at a new day high.
- Score (bullish) 7/10, grade B on the card. Scored: VWAP, ADX 41.6, EMA stack (9 EMA $770.95 > 21 EMA $768.89), higher highs/lows plus a close through the day high, higher timeframe (above the 20- and 50-day SMAs on a gap-up day), QQQ agrees, news (gap up on the 8:30 data).
- Missed: volume (breakout bar 226k = 0.69x the prior 10-bar average of 329k), momentum (RSI 75 is overbought; MACD above signal but histogram shrinking), key level (sitting right at the $772.3 resistance).
- Why no trade: A (ORB) needs above-average breakout volume and E needs 1.5x; both fail. No retest yet (C). The VWAP reclaim at 10:00 (B) was not caught; no chase now.
- Watch: a pullback to $772.0–772.3 that holds on a 5-min close = setup C long toward R3 $773.7 / $774.9–775.1. Losing VWAP again = back to chop.
- 4H (8 AM–12 PM): opened ~$767.4, in distribution up (new highs, no sweep below the open). No setup D.
- Squeeze (F): no; the range expanded ($769.07–772.35, $3.28).

**Setup check (10:58 AM ET): no trade (breakout stalled, back under VWAP)**
- 10:20 breakout above $772.3 never got follow-through: SPY topped at $772.65 (10:40) and rolled over. The 10:50 bar fell to $770.82 and closed $770.91, under VWAP ($771.19) on 280k (about 1.3x the recent 10-bar average). QQQ also slipped back to $751.76, at its VWAP.
- Score: C. Price crossing VWAP for the third time today = chop filter. RSI cooled to 60; 9 EMA $771.53 is above price.
- Squeeze (F): range **$770.70–772.65** ($1.95 wide) held 10:10–10:55, about 45 min. F window opens 11:00. Long trigger = 5-min close above $772.65 on 2x volume with QQQ breaking its high ($754.53). Short trigger = close below $770.70 on 2x volume, toward the $769.4 gap support and then $767.9.
- 4H (8 AM–12 PM): opened ~$767.4, high $772.65; upper wick forming. A close of this candle back near $769 would be a bearish distribution signal for the 12–4 PM candle. No setup D yet.

**Setup check (11:28 AM ET): no trade. Bearish momentum run missed between checks; too extended to chase**
- The squeeze broke **down**. 11:00 bar closed $769.97, below the $770.70 range low, on 341k (1.5x the prior 10-bar average of 223k; F needs 2x). 11:05 bar closed $769.03, below the **$769.4 gap support**, on 355k (1.6x). **That was a valid setup E short trigger** (close through a strong level on 1.5x+ volume, QQQ breaking too, below a falling VWAP), between checks.
- Selloff continued: 11:10 bar on 399k, now $767.36 (11:20 close). QQQ $747.79, down from $754.5.
- Why no trade now: price is $1.67 past the $769.03 trigger, beyond E's $1.50 no-chase limit. It is sitting on the $766.8–767.9 support (R1 + pre-market base) and the 4H open (~$767.4). Shorting into support after a $5 drop is a chase.
- Watch: a bounce back to $769.0–769.4 that fails (5-min close back under) = setup C short toward $765.0–765.65 (gap fill / yesterday's high). A close below $766.8 on volume = continuation toward $765.
- 4H (8 AM–12 PM): opened ~$767.4, high $772.65, now back at the open. A long upper wick means a bearish rejection. If it closes red, the 12–4 PM candle leans distribution down.
- Squeeze (F): broken down; no new range.
- Missed-move note for EOD: E short at 11:05 ($769.03), low so far $767.36 (+$1.67, ~1.0R on a $0.40 stop above $769.4).

**Setup check (11:58 AM ET): PAPER TRADE OPENED. Setup C, bearish break and retest of $769.4, B grade**
- SPY bounced off $767.15 (11:25) back to the broken $769.4 gap support. It tested $769.46–769.50 (11:35–11:40) and was rejected, with lower highs ($769.50, $769.30, $769.29). The 11:50 bar closed $768.68, below the prior bar's low ($768.86): that is the confirming candle. Now $768.95.

| # | Factor | Bearish? | Reading |
|---|---|---|---|
| 1 | VWAP (required) | ✅ | $768.95 below VWAP $770.36, VWAP falling since 10:45 |
| 2 | ADX > 20 (required) | ✅ | 28.3 |
| 3 | EMA 9/21 | ✅ | 9 EMA $769.06 < 21 EMA $769.32, price under both |
| 4 | Candles | ✅ | Lower highs/lows from $772.65; close through the prior low off the retest |
| 5 | Key level | ✅ | Retest of the broken $769.4–769.7 support (R2 + 9/28, 9/30 highs) held as resistance |
| 6 | Volume | ❌ | Confirming bar 178k vs ~260k prior 10-bar average |
| 7 | Momentum | ✅ | RSI 46 (room to fall), MACD below signal |
| 8 | Higher timeframe | ❌ | Daily still bullish (gap up, above the 20/50-day SMAs) |
| 9 | QQQ agrees | ✅ | $749.34, below its VWAP $751.32, same failed retest |
| 10 | News | ❌ | Morning data drove a gap up; no confirmed bearish catalyst |

**Score 7/10, grade B.** No-trade filters: none hit (no event before exit, SPY/QQQ agree, 0 losses today).

**Option leg (0DTE):** SPY 2026-10-02 **767 put**, bid/ask $0.48/0.49, entry **$0.49** ($49), **fits cap: yes** (under the $50 max). Delta −0.26, OI 5,049, spread 2%.
- Stop: $0.25 option (about 50%), or invalidation: a 5-min close above $769.50.
- Target: $0.74 (+50%), limit. Underlying near $767.15 (today's low); next $765.0–765.65.
- Time stop: 12:28 PM if not working. Hard exit 3:30 PM.

**Fractional leg:** **SH**, $125 at **$32.16** (3.887 shares).
- Alert stop SH $32.13 (SPY ~$769.60, above the retest high + $0.10). Risk ≈ $0.12.
- Target SH $32.23 (SPY ~$767.15). Reward ≈ $0.27, R/R ≈ 2.3.
- Exit by 3:45 PM.

- 4H (8 AM–12 PM): closing now near $768.9, slightly above its ~$767.4 open, with a long upper wick to $772.65 (bearish rejection). The 12–4 PM candle opens around $769. Watch for a push above the open that fails (manipulation up) for D.
- Squeeze (F): $767.15–769.50 ($2.35) since 11:20, about 40 min; becomes valid at 12:05.

**12:04 PM ET: open trades and process upgrade**
- Open trades: SPY $769.2 (bounced to $769.28, still under the $769.50 invalidation). 767P bid $0.41 (−$8). SH $32.14 (alert stop $32.13 not hit). Both still open; time stop for the option at 12:28.
- **New: checks every 15 minutes** (:12, :27, :42, :57) plus **armed triggers** (playbook section 10). Each check writes its triggers in advance; the next check replays the bars and logs any that fired, as of the trigger bar's close.

ARMED (valid until 12:12 PM):
- ARMED E short: trigger = 5-min close below $767.10 (new day low) on ≥ 1.5× the prior 10-bar volume, QQQ below $747.50; entry = trigger close; stop = $768.10; target = $765.10 (gap fill / 20-day SMA); valid until 12:12.
- ARMED B long: trigger = 5-min close above VWAP ~$770.45 on ≥ 1.5× volume, QQQ above its VWAP ($751.3); entry = trigger close; stop = $769.60; target = $772.30; valid until 12:12. (A fire here also invalidates the open short.)

**Setup check (12:14 PM ET): both paper legs closed for losses; no armed trigger fired**
- Replay of the 12:04 ARMED list: E short (close < $767.10) did not fire (low $768.52). B long (close > ~$770.45) did not fire (high $769.86).
- **SH stopped:** the 12:00 bar traded $32.12, through the $32.13 alert. Exit $32.12 → **−$0.16**.
- **767P invalidated:** the 12:05 bar closed $769.79, above the $769.50 invalidation level. Exit at the bid ≈ **$0.30** (option bar close $0.31) → **−$19 (−39%)**. The $0.25 option stop was never touched (low $0.31).
- Lesson: the retest high was only $0.10 above the level, so the stop sat inside normal noise. Light volume on the confirming candle (178k vs 260k) was the warning. Counted as **one losing signal** for the "two losses = done" filter, since live trading takes only one of the two legs.
- Now: SPY $769.79, back above $769.4 but under VWAP ($770.31), which is flat. QQQ $750.71, under its VWAP. Price crossing $769.4 and VWAP repeatedly = chop. **Grade C, no trade.**
- 4H (12–4 PM): opened ~$769.23; range $769.09–769.86 so far = accumulation.
- Squeeze (F): **$768.14–769.86** ($1.72) since 11:30, valid. Prior 10-bar average volume ≈ 185k.

ARMED (valid until 12:27 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 370k), QQQ below $749.20; entry = trigger close; stop = $769.10; target = $764.70 (measured move); valid until 12:27.
- ARMED B long: trigger = 5-min close above $770.40 (VWAP reclaim) on ≥ 1.5× volume (≈ 280k), QQQ above its VWAP (~$751.2); entry = trigger close; stop = $769.50; target = $772.30; valid until 12:27.

**Setup check (12:28 PM ET): no trade; nothing fired**
- Replay: F short (close < $768.14) did not fire (low $769.035). B long (close > $770.40) did not fire (high $769.91).
- SPY $769.10, under a flat VWAP ($770.29). Volume drying up (60–105k per bar, lunch lull). Grade C, chop.
- 4H (12–4 PM): opened ~$769.23, range $769.04–769.91 = accumulation; no sweep yet.
- Squeeze (F): **$768.14–769.91** ($1.77) since 11:30. Prior 10-bar average volume ≈ 129k.

ARMED (valid until 12:42 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 260k), QQQ below $749.20; entry = trigger close; stop = $769.12; target = $764.60; valid until 12:42.
- ARMED B long: trigger = 5-min close above $770.40 on ≥ 1.5× volume (≈ 195k), QQQ above its VWAP (~$751.2); entry = trigger close; stop = $769.50; target = $772.30; valid until 12:42.
