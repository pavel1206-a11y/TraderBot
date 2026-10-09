# Paper Trade Journal

Practice phase: no real money. Every A or B grade setup from
`../strategies/playbook.md` is logged here as if it had been taken, using real
quotes for the contract. Rules for graduating to real money are in
`../CLAUDE.md`.

## Scoreboard

| Closed trades | Trades | Wins | Losses | Win rate | Avg win | Avg loss | Net P&L |
|---|---|---|---|---|---|---|---|
| Options, A grade* | 1 | 1 | 0 | 100% | +$13.50 | – | +$13.50 |
| Options, B grade | 5 | 1 | 4 | 20% | +$42 | -$13.25 | -$11 |
| Fractional, A grade* | 1 | 1 | 0 | 100% | +$0.31 | – | +$0.31 |
| Fractional, B grade | 4 | 0 | 4 | 0% | – | -$0.19 | -$0.77 |
| **All** | 11 | 3 | 8 | 27% | +$18.60 | -$6.73 | +$2.04 |

\* The only A-grade trades so far (10/6 VWAP pullback) were armed with reward/risk 0.66 at the trigger close, an arming error. Whether they count toward graduation is for the owner to decide at the Friday review.

Open: none.

By setup: ORB 0 · VWAP pullback 2 · Break and retest 4 · 4H manipulation 0 · Squeeze F 1 · Momentum E 2 · E/F (10/9) 1

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

**Setup check (12:43 PM ET): no trade; nothing fired**
- Replay: neither armed trigger fired (range $768.91–769.85; no close below $768.14 or above $770.40).
- SPY $769.73, under a flat VWAP ($770.26). Lunch volume (17–123k per bar). Grade C.
- 4H (12–4 PM): accumulation, $768.91–769.91.
- Squeeze (F): **$768.14–769.91** ($1.77), now 75 min old. Prior 10-bar average volume ≈ 105k.

ARMED (valid until 12:57 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 210k), QQQ below $749.20; entry = trigger close; stop = $769.12; target = $764.60; valid until 12:57.
- ARMED B long: trigger = 5-min close above $770.40 on ≥ 1.5× volume (≈ 160k), QQQ above its VWAP (~$751.1); entry = trigger close; stop = $769.50; target = $772.30; valid until 12:57.

**Setup check (12:58 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (range $768.72–769.85).
- SPY $769.49, under a flat VWAP ($770.22). QQQ $749.66, under its VWAP ($751.22). Grade C (chop, thin volume).
- 4H (12–4 PM): accumulation, $768.72–769.91.
- Squeeze (F): **$768.14–769.91** ($1.77), 90 min old. Prior 10-bar average volume ≈ 93k.

ARMED (valid until 1:12 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 185k), QQQ below $748.90; entry = trigger close; stop = $769.12; target = $764.60; valid until 1:12.
- ARMED B long: trigger = 5-min close above $770.40 on ≥ 1.5× volume (≈ 140k), QQQ above its VWAP (~$751.2); entry = trigger close; stop = $769.50; target = $772.30; valid until 1:12.

**Setup check (1:13 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (range $768.84–770.05; the 1:00 high of $770.05 stayed under the $770.40 trigger).
- SPY $769.50, under VWAP ($770.20). Grade C, chop.
- 4H (12–4 PM): accumulation, $768.72–770.05.
- Squeeze (F): **$768.14–770.05** ($1.91). Prior 10-bar average volume ≈ 95k.

ARMED (valid until 1:27 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 190k), QQQ below $748.90; entry = trigger close; stop = $769.20; target = $764.30; valid until 1:27.
- ARMED B/F long: trigger = 5-min close above $770.40 (above the range and VWAP) on ≥ 2× volume (≈ 190k), QQQ above its VWAP (~$751.2); entry = trigger close; stop = $769.50; target = $772.30; valid until 1:27.

**Setup check (1:28 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (range $768.64–769.86).
- SPY $768.76, drifting to the lower half of the range. 1:20 bar on 123k (1.2×). QQQ $748.47, the weaker of the two. Still under VWAP ($770.17). Grade C until the range breaks.
- 4H (12–4 PM): accumulation, $768.64–770.05.
- Squeeze (F): **$768.14–770.05** ($1.91). Prior 10-bar average volume ≈ 102k.

ARMED (valid until 1:42 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 205k), QQQ below $748.30; entry = trigger close; stop = $769.20; target = $764.30; valid until 1:42.
- ARMED B/F long: trigger = 5-min close above $770.40 on ≥ 2× volume (≈ 205k), QQQ above its VWAP (~$751.1); entry = trigger close; stop = $769.50; target = $772.30; valid until 1:42.

**Setup check (1:43 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (low $768.33 stayed above $768.14; high $769.30).
- SPY $768.90, pressing the bottom of the range. QQQ $748.62 made a new afternoon low ($747.78). Under VWAP ($770.12). Grade C.
- 4H (12–4 PM): $768.33–770.05; drifting lower inside the range.
- Squeeze (F): **$768.14–770.05**. Prior 10-bar average volume ≈ 102k.

ARMED (valid until 1:57 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 205k), QQQ below $747.70; entry = trigger close; stop = $769.20; target = $764.30; valid until 1:57.
- ARMED B/F long: trigger = 5-min close above $770.40 on ≥ 2× volume (≈ 205k), QQQ above its VWAP (~$751.0); entry = trigger close; stop = $769.50; target = $772.30; valid until 1:57.

**Setup check (1:58 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (range $768.565–769.46).
- SPY $769.40, under VWAP ($770.09). Range-bound since 11:30. Grade C.
- 4H (12–4 PM): accumulation, $768.33–770.05.
- Squeeze (F): **$768.14–770.05**. Prior 10-bar average volume ≈ 99k.

ARMED (valid until 2:12 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 200k), QQQ below $747.70; entry = trigger close; stop = $769.20; target = $764.30; valid until 2:12.
- ARMED B/F long: trigger = 5-min close above $770.40 on ≥ 2× volume (≈ 200k), QQQ above its VWAP (~$751.0); entry = trigger close; stop = $769.50; target = $772.30; valid until 2:12.

**Setup check (2:13 PM ET): no trade; nothing fired**
- Replay: neither trigger fired (range $768.66–769.46).
- SPY $769.14, under VWAP ($770.06). Tight range for 2h40m. Grade C.
- 4H (12–4 PM): accumulation, $768.33–770.05.
- Squeeze (F): **$768.14–770.05**. Prior 10-bar average volume ≈ 111k.

ARMED (last of the day, valid until 2:27 PM):
- ARMED F short: trigger = 5-min close below $768.14 on ≥ 2× the prior 10-bar volume (≈ 220k), QQQ below $747.70; entry = trigger close; stop = $769.20; target = $764.30; valid until 2:27.
- ARMED B/F long: trigger = 5-min close above $770.40 on ≥ 2× volume (≈ 220k), QQQ above its VWAP (~$751.0); entry = trigger close; stop = $769.50; target = $772.30; valid until 2:27.

**Setup check (2:28 PM ET): entry window closed; no trade**
- Replay: neither trigger fired (low $768.51, above $768.14; high $769.35).
- SPY $768.60, drifting toward the range low, but no new entries after 2:30. No open paper trades. Remaining checks only report until the close.

**End of day (3:48 PM ET)**
- Paper trades today: 1 signal, 2 legs (setup C bearish retest of $769.4, B grade). 767P −$19, SH −$0.16. Day: **−$19.16**.
- Running totals: 4 trades, 1 win, 3 losses, **+$22.76** after 4 days.
- Day: gap up $6.5, failed ORB breakout at $772.65, a $5.5 flush to $767.15 by 11:25, then four hours of chop in $768.14–770.05. Close ~$769.8.
- Missed: +$3.6 sweep-and-reclaim at 9:55 and −$5.5 setup E short at 11:05 (between checks). See missed-moves.md.
- Lesson: the retest stop sat $0.10 above the level and was taken out by noise. The confirming candle had low volume.

---

## Weekly review: 2026-09-29 to 2026-10-02 (playbook section 8)

| | Trades | W/L | Net | Notes |
|---|---|---|---|---|
| Options (0DTE) | 2 | 1/1 | **+$23** | 759P +$42 (premium $83, **over the $50 cap**); 767P −$19 |
| Fractional | 2 | 0/2 | −$0.24 | SH stopped both times by about a cent |
| By setup | C (break & retest) 4 | 1/3 | +$22.76 | A, B, D, E, F: 0 trades |
| By grade | B 4 | 1/3 | +$22.76 | **A-grade: 0 trades** |

- **Rule breaks:** 1. The 10/1 winner cost $83, above the $50 cap; on cap-fitting contracts it would have been smaller.
- **Graduation check:** not yet (4 of 10 trades; no A-grade trades to judge).
- **What worked:** reading direction off a broken level; the option leg captures the move when it comes fast.
- **What didn't:** the fractional leg (SH stops set on SH's price are too tight, about $0.03 away); retest stops sitting inside noise; moves firing between checks (now addressed with 15-min checks and armed triggers).

### Proposed playbook changes (need the owner's OK; not applied)

1. **Setup F volume: 2× → 1.5×** for the breakout candle, keep the QQQ-agrees rule. (10/2: 1.5–1.6× breakdown ran $5.5.)
2. **Setup C stop buffer:** stop at least $0.30 beyond the level (or $0.15 beyond the retest extreme, whichever is farther), and the confirming candle needs volume ≥ the prior 10-bar average. (10/2 loss: $0.10 buffer, 0.7× volume.)
3. **Fractional stops on the SPY level, not the inverse fund's price:** set the alert on SPY at the setup's stop, sell SH/PSQ when it fires. SH-price stops were hit by tracking noise twice.
4. **Gap-and-go only with volume:** the ORB-long-on-gap-days rule requires breakout volume ≥ 1.0× (10/2's 0.7× breakout failed).

**Owner decision (2026-10-02 evening):** all four proposed changes approved and applied to the playbook (F volume 1.5×, setup C stop buffer + volume, fractional stops on the SPY/QQQ level, gap-day ORB volume ≥ 1.0×).

### 2026-10-05 (Mon)

**Pre-market brief (8:54 AM ET)**
- SPY pre-market $768.41 (−0.16%); QQQ $747.50 (−0.28%); IWM flat. Small gap down, inside Friday's range.
- Friday: high $772.65, low $767.15, close $769.64.
- Pivots (from Friday): R2 $775.32, R1 $772.48, **P $769.81**, S1 $766.97, S2 $764.31.
- 20-day SMA $764.83, 50-day SMA $763.70 (price above both; daily uptrend intact).
- Strong levels: $772.3–772.65 (Fri high + R1 + 9/25 high), **$769.4–769.8** (pivot + gap level, Friday's afternoon ceiling ~$770.05), $767.0–767.15 (S1 + Friday's low), $764.3–765.0 (S2 + 20-day SMA).
- News: quiet, mixed (analyst calls, J.B. Hunt earnings warning). No big index-moving earnings.
- Event: **ISM Services PMI likely at 10:00 AM** (3rd business day; not confirmed). Treat 9:45–10:05 entries with caution; a 10:00 data candle can start the day's move (10/1 pattern).
- **Bias: none (neutral).** Bullish above $770.05 (Friday's range top) with volume; bearish below $767.0.
- Playbook changes from the week-1 review are live today (F 1.5×, C stop buffer + volume, SPY-level fractional stops, gap-day ORB volume).

**9:43 AM ET: opening range forming**
- SPY opened $769.69 (gap down erased), first bar up to $770.93 on 549k; now $770.59. Range so far $769.65–770.97. QQQ stronger: $752.12, above Friday's close.
- Above Friday's $770.05 ceiling already. The 9:45 OR is final at the 9:40 bar's close.
- ISM Services (likely 10:00): a 10:00-candle trigger is valid but gets extra care in the score (news factor).

ARMED (9:45–10:12; ORH/ORL = the final 9:30–9:45 high/low, currently $770.97 / $769.65):
- ARMED A long: trigger = 5-min close above ORH on ≥ 1.0× the average volume of the bars since 9:30, SPY above VWAP, QQQ above its own OR high; entry = trigger close; stop = $770.30; target = $772.65 (Friday high / R1); valid until 10:12.
- ARMED A short: trigger = 5-min close below ORL and below $769.4 on ≥ 1.0× that average, QQQ below its OR low; entry = trigger close; stop = $770.40; target = $767.15 (Friday low / S1); valid until 10:12.

**Setup check (9:58 AM ET): no trade; nothing fired**
- Opening range final: **$769.65–770.97**. Since 9:35 SPY has sat in $770.26–770.97 on a flat VWAP ($770.55), now $770.42. QQQ firmer ($752.17, OR $749.08–753.10). Grade C (VWAP flat, inside the range).
- Replay: no close above $770.97 or below $769.65.
- ISM Services due at 10:00 (next bar).
- 4H (8 AM–12 PM): opened ~$768.4 pre-market; up into Friday's range ceiling. No sweep yet, so no setup D.

ARMED (valid until 10:27 AM; average volume since 9:30 ≈ 255k):
- ARMED A long: trigger = 5-min close above $770.97 on ≥ 1.0× (≈ 255k), SPY above VWAP, QQQ above $753.10; entry = trigger close; stop = $770.30; target = $772.65; valid until 10:27.
- ARMED A short: trigger = 5-min close below $769.40 on ≥ 1.0× (≈ 255k), QQQ below $749.08; entry = trigger close; stop = $770.40; target = $767.15; valid until 10:27.

**Setup check (10:22 AM ET; trigger fired 9 min late): no trade; armed long did NOT fire (QQQ condition)**
- Replay of A long (close > $770.97 on ≥ 255k, above VWAP, QQQ > $753.10): 10:05 bar closed $771.80 on 287k and 10:10 closed $771.94 on 269k. SPY's part met, but **QQQ closed $752.23 / $752.31, below its $753.10 OR high**. Not fired. 10:15 also fails (233k, QQQ $752.89). Strict replay rules: no trade.
- What it would have done: entry $771.80, target $772.65 hit at 10:15 (+$0.85, ~1.6R). Logged as a **near miss**: SPY led and QQQ lagged. Something to watch: is requiring QQQ's own OR break too strict when QQQ is above its VWAP?
- A short: did not fire.
- Now: SPY $772.42, right at the **$772.48–772.65 resistance** (R1 + Friday's high), above a rising VWAP ($770.98). ISM bar (10:00) wicked to $769.98 and closed up. Higher highs and lows since. QQQ $752.89, still under its OR high.
- Grade: no entry. Price is at resistance, QQQ is lagging, and volume (233k) is under average.
- 4H (8 AM–12 PM): opened ~$768.4, trending up (distribution up); no sweep, so no setup D.

ARMED (valid until 10:42 AM; prior 10-bar average ≈ 249k):
- ARMED E long: trigger = 5-min close above $772.70 (Friday high) on ≥ 1.5× (≈ 375k), QQQ above $753.10; entry = trigger close; stop = $771.90; target = $774.90 (9/21–22 highs); valid until 10:42.
- ARMED C long: trigger = a 5-min bar that tags $771.30 or lower (OR high / VWAP retest) and closes ≥ $771.50 on ≥ 1.0× volume, QQQ above its VWAP; entry = trigger close; stop = $770.70; target = $773.69; valid until 10:42.

**Setup check (10:28 AM ET): no trade; nothing fired**
- Replay: E long needed a close above $772.70 on ≥ 375k. 10:20 closed $772.71 on 215k, so volume failed. C long (tag ≤ $771.30) did not happen (low $771.82).
- SPY $772.71, grinding up through Friday's high on below-average volume. QQQ now above its OR high ($753.56 > $753.10), above VWAP ($751.99). SPY VWAP $771.12, rising.
- Steady trend, no volume. No chase: $1.74 above VWAP, at resistance.

ARMED (valid until 10:42 AM; prior 10-bar average ≈ 215k):
- ARMED E long: trigger = 5-min close above $773.00 on ≥ 1.5× (≈ 323k), QQQ above $753.10; entry = trigger close; stop = $772.10; target = $774.90; valid until 10:42.
- ARMED C long: trigger = a 5-min bar that tags $771.90 or lower (Friday-high retest) and closes ≥ $772.20 on ≥ 1.0× (≈ 215k), QQQ above its VWAP; entry = trigger close; stop = $771.40; target = $774.20; valid until 10:42.

**Setup check (10:43 AM ET): no trade; nothing fired**
- Replay, C long: the 10:30 bar tagged $771.67 but closed $771.79 (below $772.20). The 10:35 bar tagged $771.79 and closed $772.40, but on **144k < 215k** (the new 1.0× volume rule). Not fired. E long (close > $773.00): no.
- SPY $772.40, holding above Friday's high on a light-volume pullback. VWAP $771.31 rising. QQQ $753.13, around its OR high.
- Squeeze forming: $771.67–772.96 since 10:15 (30 min).

ARMED (valid until 10:57 AM; prior 10-bar average ≈ 205k):
- ARMED E long: trigger = 5-min close above $773.00 on ≥ 1.5× (≈ 307k), QQQ above $753.94 (today's high); entry = trigger close; stop = $772.10; target = $774.90; valid until 10:57.
- ARMED C long: trigger = a 5-min bar that tags $771.90 or lower and closes ≥ $772.20 on ≥ 1.0× (≈ 205k), QQQ above its VWAP; entry = trigger close; stop = $771.40; target = $774.20; valid until 10:57.

**Setup check (10:58 AM ET): no trade; nothing fired**
- Replay: no close above $773.00. No bar tagged ≤ $771.90 (lows ≥ $772.11).
- SPY $772.40, flat for 45 min above Friday's high. Volume drying up (114–122k). VWAP $771.41. QQQ $753.67, above its VWAP ($752.24).
- **Squeeze (F): $771.67–772.96 ($1.29) since 10:15, valid now.** Prior 10-bar average ≈ 188k.
- 4H (8 AM–12 PM): opened ~$768.4, trending up; no sweep.

ARMED (valid until 11:12 AM):
- ARMED F long: trigger = 5-min close above $772.96 on ≥ 1.5× (≈ 282k), QQQ above $753.94; entry = trigger close (≤ $0.75 past the edge); stop = $772.21 (range mid − $0.10); target = $775.54 (measured move); valid until 11:12.
- ARMED F short: trigger = 5-min close below $771.67 on ≥ 1.5× (≈ 282k), QQQ below $752.63 and below its VWAP; entry = trigger close; stop = $772.42; target = $769.09; valid until 11:12.

**Setup check (11:16 AM ET; trigger fired 4 min late): no trade; nothing fired**
- Replay: F long/short did not fire (range held, $772.16–772.91 since 10:55).
- SPY $772.57; squeeze **$771.67–772.96** now 60 min old ($1.29). VWAP $771.59 rising underneath. QQQ $753.45. Volume ≈ 150k/bar (thin). Grade C until the break.

ARMED (valid until 11:27 AM; prior 10-bar average ≈ 152k):
- ARMED F long: trigger = 5-min close above $772.96 on ≥ 1.5× (≈ 228k), QQQ above $754.10; entry = trigger close; stop = $772.21; target = $775.54; valid until 11:27.
- ARMED F short: trigger = 5-min close below $771.67 on ≥ 1.5× (≈ 228k), QQQ below $752.63; entry = trigger close; stop = $772.42; target = $769.09; valid until 11:27.

**Setup check (11:28 AM ET): no trade; nothing fired**
- Replay: no close outside $771.67–772.96.
- 11:20 bar traded 353k (2.2×) but closed $772.80, inside the range: heavy volume near the top edge without a break. Worth watching.
- SPY $772.80; squeeze $771.67–772.96, 75 min. VWAP $771.70. QQQ $753.67. Grade C until the break.

ARMED (valid until 11:42 AM; prior 10-bar average ≈ 162k):
- ARMED F long: trigger = 5-min close above $772.96 on ≥ 1.5× (≈ 243k), QQQ above $754.10; entry = trigger close; stop = $772.21; target = $775.54; valid until 11:42.
- ARMED F short: trigger = 5-min close below $771.67 on ≥ 1.5× (≈ 243k), QQQ below $752.63; entry = trigger close; stop = $772.42; target = $769.09; valid until 11:42.

**Setup check (11:43 AM ET): no trade; nothing fired**
- Replay, F long: 11:30 closed $773.05 (> $772.96) but on 131k < 243k, and QQQ $753.33 < $754.10. 11:35 $773.06 on 187k, also below. Not fired: a slow drift over the edge with no volume and QQQ lagging.
- SPY $773.06; range now $771.67–773.13 ($1.46). VWAP $771.80. QQQ flat at $753.29.

ARMED (valid until 11:57 AM; prior 10-bar average ≈ 166k):
- ARMED F long: trigger = 5-min close above $773.13 on ≥ 1.5× (≈ 249k), QQQ above $754.10; entry = trigger close; stop = $772.30; target = $776.05 (edge + 2× range); valid until 11:57.
- ARMED F short: trigger = 5-min close below $771.67 on ≥ 1.5× (≈ 249k), QQQ below $752.63; entry = trigger close; stop = $772.50; target = $768.75; valid until 11:57.

**Setup check (11:58 AM ET): no trade; nothing fired**
- Replay: F long needed a close > $773.13 on ≥ 249k. 11:40–11:50 closed $773.29–773.33 on 109–145k; QQQ ≤ $753.82. Not fired.
- SPY $773.29, slow grind higher (+$3.6 from the open) on falling volume; VWAP $771.90. QQQ $753.82.
- Squeeze tightened: **$772.28–773.48 ($1.20) since 11:10.** Prior 10-bar average ≈ 159k.
- 4H (8 AM–12 PM): closing near its high (~$773.3) from a ~$768.4 open; strong bullish candle, no sweep. The 12–4 PM candle opens ~$773.3: watch for a sweep below its open/the range low that recovers (setup D long).

ARMED (valid until 12:12 PM):
- ARMED F long: trigger = 5-min close above $773.48 on ≥ 1.5× (≈ 238k), QQQ above $754.10; entry = trigger close; stop = $772.78; target = $775.88; valid until 12:12.
- ARMED F short: trigger = 5-min close below $772.28 on ≥ 1.5× (≈ 238k), QQQ below $753.00; entry = trigger close; stop = $772.98; target = $769.88; valid until 12:12.

**Setup check (12:13 PM ET): no trade; nothing fired**
- Replay: no close outside $772.28–773.48 (range $772.92–773.37).
- SPY $773.14. Squeeze **$772.28–773.48**, 60 min. VWAP $771.98. QQQ $753.51. Volume ~120–140k. Grade C.
- 4H (12–4 PM): opened ~$773.3, dipped to $772.92: accumulation. No sweep yet; D long needs a drop through $772.28 (range low) that closes back above it.

ARMED (valid until 12:27 PM; prior 10-bar average ≈ 154k):
- ARMED F long: trigger = 5-min close above $773.48 on ≥ 1.5× (≈ 231k), QQQ above $754.10; entry = trigger close; stop = $772.78; target = $775.88; valid until 12:27.
- ARMED F short: trigger = 5-min close below $772.28 on ≥ 1.5× (≈ 231k), QQQ below $753.00; entry = trigger close; stop = $772.98; target = $769.88; valid until 12:27.
- ARMED D long: trigger = a 5-min bar that trades below $772.28 and then a bar closing back above $772.28 (within 2 bars), QQQ above $752.60; entry = that close; stop = sweep low − $0.15; target = $775.00; valid until 12:27.

**Setup check (12:28 PM ET): no trade; nothing fired**
- Replay, F long: 12:20 closed $773.50 (> $773.48) on 137k < 231k, QQQ $753.68 < $754.10. Not fired (third light-volume poke over the top). F short / D long: low $772.855, no sweep of $772.28.
- SPY $773.50, new high $773.64. VWAP $772.05. Range $772.28–773.64.

ARMED (valid until 12:42 PM; prior 10-bar average ≈ 130k):
- ARMED F long: trigger = 5-min close above $773.64 on ≥ 1.5× (≈ 195k), QQQ above $754.10; entry = trigger close; stop = $772.86; target = $776.36; valid until 12:42.
- ARMED F short: trigger = 5-min close below $772.28 on ≥ 1.5× (≈ 195k), QQQ below $752.80; entry = trigger close; stop = $773.06; target = $769.56; valid until 12:42.

**Setup check (12:43 PM ET): no trade; nothing fired**
- Replay, F long (close > $773.64 on ≥ 195k, QQQ > $754.10): 12:30 closed $773.68 on 100k; 12:35 closed $773.97 on 135k, QQQ $753.95. Volume and QQQ both failed. Short: no.
- SPY $773.97, day high $774.04. Grinding up in $0.20–0.30 steps on below-average volume. VWAP $772.14. QQQ tagged $754.15 (new day high).
- Pattern of the day: a slow, quiet trend that never gives a volume breakout or a VWAP pullback. None of setups A–F catches this kind of move by design. Note for the weekly review.

ARMED (valid until 12:57 PM; prior 10-bar average ≈ 121k):
- ARMED E long: trigger = 5-min close above $774.04 on ≥ 1.5× (≈ 181k), QQQ above $754.15; entry = trigger close; stop = $773.40; target = $775.10 (9/21–22 highs); valid until 12:57.
- ARMED F short: trigger = 5-min close below $772.85 on ≥ 1.5× (≈ 181k), QQQ below $753.20; entry = trigger close; stop = $773.60; target = $771.00; valid until 12:57.

**Setup check (12:58 PM ET): no trade; nothing fired**
- Replay, E long (close > $774.04 on ≥ 181k, QQQ > $754.15): 12:40 closed $774.45 with QQQ $754.44 ✓, but **volume 116k < 181k**. Not fired. Short: no.
- SPY $774.37, new day high $774.54 (+$4.85 from the open). Still on falling volume (85–116k). VWAP $772.24. Next resistance $774.9–775.1 (9/21–22 highs).
- Volume-gated triggers keep missing this grind. The near misses today (10:05 ORB, 12:40 E) both went on to work. Weekly-review item: on days where SPY trends above a rising VWAP with QQQ agreeing, is a 1.0× volume bar enough for E?

ARMED (valid until 1:12 PM; prior 10-bar average ≈ 114k):
- ARMED E long: trigger = 5-min close above $775.10 on ≥ 1.5× (≈ 171k), QQQ above $754.60; entry = trigger close; stop = $774.30; target = $776.80; valid until 1:12.
- ARMED E short: trigger = 5-min close below $773.60 on ≥ 1.5× (≈ 171k), QQQ below $753.80; entry = trigger close; stop = $774.40; target = $772.25 (VWAP); valid until 1:12.

**Setup check (1:13 PM ET): no trade; nothing fired**
- Replay: no close > $775.10 or < $773.60 (range $773.77–774.54).
- SPY $773.99, small pullback off the $774.54 high on very light volume (~90k). VWAP $772.31. QQQ $754.13.

ARMED (valid until 1:27 PM; prior 10-bar average ≈ 110k):
- ARMED E long: trigger = 5-min close above $774.60 on ≥ 1.5× (≈ 165k), QQQ above $754.60; entry = trigger close; stop = $773.70; target = $776.10; valid until 1:27.
- ARMED E short: trigger = 5-min close below $773.60 on ≥ 1.5× (≈ 165k), QQQ below $753.60; entry = trigger close; stop = $774.40; target = $772.30 (VWAP); valid until 1:27.

**Owner's own trade (real money, individual account, placed by the owner): SPY 774C 0DTE, +$22.00**
- Bought 1 × SPY 10/5 $774 call, limit $0.30, **filled $0.28 at 10:09 AM** ($28.04). Sold by **stop-limit at $0.50 (trigger $0.50 / limit $0.49) at 10:23 AM**, +$22.00 (+79%) in 14 minutes.
- That was exactly the armed **A long (ORB break above $770.97)** that fired on SPY at 10:05 ($771.80 close on 287k ≥ 255k, above VWAP) and that **I blocked** with a QQQ condition stricter than the playbook ("QQQ above its own OR high $753.10"). QQQ was $752.23, above its VWAP (~$752), which is what score-card factor 9 actually asks.
- Fix (applied to playbook section 10): the default QQQ condition for armed triggers is now "QQQ on the same side of its VWAP." Setup F keeps "QQQ breaking the same way."
- Under the fixed rule this would have been a replayed paper trade: entry SPY $771.80 at 10:10, target $772.65 hit by 10:15. Not added to the scoreboard (no after-the-fact rule changes), but logged as the reference case.
- What the owner's trade shows that the playbook should keep:
  - Contract: ~$2 OTM 0DTE call at $0.28, well inside the $25–50 cap, liquid.
  - Exit: a resting stop-limit placed above entry to lock the gain (+79%) instead of watching it.
- Note: it counts as a day trade in that account (PDT: 1 of 3 per rolling 5 business days, if that account is under $25k).

**Setup check (1:28 PM ET): no trade; nothing fired**
- Replay: no close > $774.60 or < $773.60 (range $773.77–774.40).
- SPY $774.39, near the $774.54 high. QQQ $754.70, above its VWAP ($752.91), so the new QQQ condition is met for longs. Volume still thin (~100k).

ARMED (valid until 1:42 PM; prior 10-bar average ≈ 102k; QQQ condition = same side of its VWAP):
- ARMED E long: trigger = 5-min close above $774.60 on ≥ 1.5× (≈ 153k), QQQ above its VWAP; entry = trigger close; stop = $773.70; target = $776.10; valid until 1:42.
- ARMED E short: trigger = 5-min close below $773.60 on ≥ 1.5× (≈ 153k), QQQ below $753.60; entry = trigger close; stop = $774.40; target = $772.40 (VWAP); valid until 1:42.

**Setup check (1:43 PM ET): no trade; nothing fired**
- Replay: no close > $774.60 or < $773.60 (range $774.15–774.47).
- **Squeeze (F): $773.77–774.54 ($0.77) since 12:35, ~65 min.** Very tight, very quiet (50–110k). VWAP $772.4; QQQ $754.64 above its VWAP ($752.98), day high $754.87.

ARMED (valid until 1:57 PM; prior 10-bar average ≈ 90k):
- ARMED F long: trigger = 5-min close above $774.54 on ≥ 1.5× (≈ 135k), QQQ breaking above $754.87; entry = trigger close; stop = $774.06; target = $776.08; valid until 1:57.
- ARMED F short: trigger = 5-min close below $773.77 on ≥ 1.5× (≈ 135k), QQQ breaking below $754.40; entry = trigger close; stop = $774.26; target = $772.23; valid until 1:57.

**Owner decision (2026-10-05 ~1:50 PM):** added playbook section 7 "Trend days: runner exit" (trend-day check reported at each check from 10:30; 2-contract half-out + break-even runner trailed on SPY; re-entry on VWAP/level pullback). Paper trades use it from the next check.

**Setup check (1:58 PM ET): PAPER TRADE OPENED (armed, replayed). Setup F long, B grade**
- Replay: **ARMED F long fired on the 1:40 bar**: close $774.875 (> $774.54) on 138k (≥ 135k = 1.5× of 90k), QQQ closed $755.49 (> $754.87). Entry SPY $774.875 at 1:45 PM.

| # | Factor | Long? | Reading (1:40 bar) |
|---|---|---|---|
| 1 | VWAP (required) | ✅ | $774.88 vs VWAP ~$772.5, rising all day |
| 2 | ADX > 20 (required) | ✅ | 40.3 |
| 3 | EMA 9/21 | ✅ | above the 21 EMA $773.93, stacked up |
| 4 | Candles | ✅ | higher lows all day; close out of the squeeze |
| 5 | Key level | ❌ | breakout runs straight into $774.9–775.1 (9/21–22 highs) |
| 6 | Volume | ✅ | 1.5× |
| 7 | Momentum | ❌ | RSI 71 (stretched), MACD a hair under signal |
| 8 | Higher timeframe | ✅ | above the 20/50-day SMAs, new highs |
| 9 | QQQ agrees | ✅ | broke its day high, above VWAP |
| 10 | News | ❌ | none |

**Score 7/10, grade B.** Trend day: **yes** (all 5 checks), so the **runner exit** applies.

**Option leg (0DTE):** SPY 10/5 **776 call ×2**. 1:40 bar close $0.21 + half spread → **entry $0.22 each ($44 total), fits cap: yes**. Spread 7%, OI 5,029.
- Contract 1: sell at +50% = **$0.33** (limit).
- Contract 2 (runner): stop to entry after contract 1 fills; trail on SPY (5-min close below the last higher low or VWAP).
- Initial stop on both: $0.11 option (50%) or SPY 5-min close < $774.06 (invalidation). Time stop 2:15 PM if not working. Hard exit 3:30.
- (The 775 call, ~ATM at $0.52, would have broken the $50 cap.)

**Fractional leg: not taken.** At the trigger price, R/R to the $776.08 target is 1.48 (< 1.5 rule).

- Since entry: 776C high $0.24, low $0.13; now bid $0.13 / ask $0.14 (**−$0.09 each, −$18 open**). SPY $774.58, low $774.58: well above the $774.06 invalidation. RSI was stretched into resistance (factors 5 and 7). Watch the 2:15 time stop.

**Setup check (2:14 PM ET): 776C ×2 STOPPED, −$22**
- Replay: the 2:05 bar traded the 776C down to **$0.11 = the 50% option stop**. Exit both at $0.11 → **−$0.11 × 2 × 100 = −$22**. The SPY invalidation ($774.06) was never hit (SPY low $774.37), and target $0.33 never reached (high $0.24).
- Why: SPY stalled at the $774.9–775.1 resistance (score-card factor 5 was ❌), and a $1+ OTM 0DTE call loses value fast after 1:30 PM while SPY goes sideways. The option-price stop was taken out by time decay, not by the setup failing.
- Lessons for the Friday review: (1) don't buy a breakout that runs straight into a strong level within $0.30 (the key-level ❌ was a real warning); (2) after ~1:30 PM, prefer the nearest-the-money strike that fits the cap, or skip; (3) consider the SPY invalidation as the primary stop for cheap OTM 0DTE (with a hard premium floor) instead of 50% of a $0.22 premium.
- Losing trades today: 1 (filter: done after 2).
- SPY $774.70; trend day still yes. QQQ $755.04, above VWAP.

ARMED (last of the day, valid until 2:27 PM; prior 10-bar average ≈ 108k):
- ARMED E long: trigger = 5-min close above $775.10 on ≥ 1.5× (≈ 162k), QQQ above its VWAP; entry = trigger close; stop = $774.40; target = $776.30; option = nearest-the-money call that fits the cap; valid until 2:27.

**Setup check (2:28 PM ET): entry window closing; nothing fired**
- Replay: E long (close > $775.10) did not fire; high $774.98. SPY $774.95, pinned under the $775 resistance on light volume.
- No open paper trades. Remaining checks only report until the close; the EOD review runs at 3:47.

**End of day (3:48 PM ET)**
- Paper trades today: 1 (setup F long, armed and replayed, B grade): SPY 776C ×2 → **−$22** (option stop $0.11 at 2:05).
- Running totals: **5 trades, 1 win, 4 losses, +$0.76** (options +$1, fractional −$0.24). A-grade trades: 0.
- Day: a trend day. Gap down erased at the open, ORB break at 10:05, steady climb above a rising VWAP all day, close ~$775.8 (+$6.2 from the open). Low-volume grind that our volume-gated triggers mostly filtered out.
- **Painful detail:** the stopped 776C setup was right. SPY hit the trade's $776.08 target at ~3:05 PM (high $776.61). The 50% option stop was taken out at 2:05 by time decay while SPY held above the $774.06 invalidation. That is evidence for proposal (3) below: use the SPY invalidation as the primary stop on cheap OTM 0DTE.
- The last armed E long (close > $775.10) closed $775.15 on the 2:25 bar, at 2:30. That's after the 2:27 validity and the 2:30 entry cutoff, so not taken (correct per rules).
- Owner traded the 10:05 ORB himself: 774C, +$22 (+79%), in his individual account (not on this scoreboard).

**Proposals for Friday's review (not applied):**
1. E/F on trend days: volume ≥ 1.0× instead of 1.5× when the trend-day check is yes.
2. No breakout entries within $0.30 of a strong level (enter on the break of the level instead).
3. Cheap OTM 0DTE (premium < $0.40): primary stop = SPY invalidation level, with a hard premium floor of −70%, instead of −50% of premium.
4. After 1:30 PM, use the nearest-the-money strike that fits the cap, or skip.

### 2026-10-06 (Tue)

**Pre-market brief (8:54 AM ET)**
- SPY pre-market $777.84 (+0.39%, gap up ~$3.0); QQQ $759.89 (+0.49%), IWM +0.47%. Continuation of Monday's trend day; price above the 9/21–22 highs ($774.9–775.1) = highest levels in our records.
- Monday: high $776.61, low $769.63, close $774.83.
- Pivots: R2 $780.66, **R1 $777.75**, P $773.69, S1 $770.78, S2 $766.71.
- 20-day SMA $765.06, 50-day SMA $764.42 (rising; daily uptrend).
- Strong levels: **$777.75** (R1; pre-market is sitting on it), **$776.6** (Monday high, first support), $774.9–775.1 (old resistance, now support), $773.7 (pivot).
- News: quiet, mildly positive (no index-moving earnings). No major scheduled release found; treat 10:00 AM as a possible data time anyway.
- Gap of $3 (< $4), so the gap-day rule does not apply; normal ORB rules (breakout volume ≥ 1.0× for gap-direction ORB).
- **Bias: bullish** while above $776.6. A drop back below $775 (gap filled into old resistance) = no bias.

**Opening check (9:42 AM ET): opening range forming, no entries before 9:45**
- SPY opened $778.16, above R1 $777.75 and well above $776.6. 9:30–9:40 range so far: **high $778.73, low $777.96**; last $778.41 (9:35 bar), just above VWAP $778.29 (flat). Volume 409k, then 287k.
- QQQ $760.38, slightly above its VWAP $760.26 after dipping under it at 9:35.
- Read: gap held so far, sitting on R1. Bias stays bullish above $776.6. The range is final once the 9:40 bar closes; triggers below use its final high/low.

ARMED (valid 9:45–10:12 AM; volume reference = average of the three opening-range bars):
- ARMED A long (ORB): trigger = 5-min close above the final range high (≈ $778.73) on ≥ 1.0× volume, SPY above VWAP, QQQ above its VWAP; entry = trigger close; stop = $777.80 (below the range low and R1); target = $780.66 (R2); option = nearest-the-money 0DTE call that fits the $25 cap; valid until 10:12.
- ARMED B long (VWAP pullback): trigger = a 5-min bar whose low comes within $0.10 of VWAP and closes above VWAP and above the prior bar's close, with QQQ above its VWAP; entry = trigger close; stop = $777.60; target = $780.00; option as above; valid until 10:12.
- ARMED A short (failed gap): trigger = 5-min close below $776.60 (below the range low and Monday's high), QQQ below its VWAP; entry = trigger close; stop = $777.40; target = $775.10; option = nearest-the-money 0DTE put that fits the cap; valid until 10:12.

**Setup check (9:58 AM ET): ARMED B long FIRED (armed, replayed)**
- Final opening range: high $778.78, low $777.96. Volume of the 3 opening bars averaged ≈ 323k.
- Replay:
  - A long (ORB) did not fire. The 9:45 bar closed $779.05 on 201k (0.62×) and the 9:50 bar closed $779.26 on 280k (0.87×), both under 1.0×.
  - **B long (VWAP pullback) fired on the 9:45 bar.** Low $778.43 vs VWAP $778.45, close $779.045 above VWAP and above the prior close $778.65. QQQ closed $760.41, above its VWAP of $760.28. **Entry is SPY $779.045 at 9:50.**
  - A short did not fire.
- **Arming error (mine):** the line had no cap on how far above VWAP the trigger bar could close. At $779.045, stop $777.60 / target $780.00 gives reward/risk of only **0.66**, below the 1.5 minimum. A live preview would have rejected it. The trade is logged exactly as written (replay rule: no rewording). The owner decides at Friday's review whether it counts. Fix from now on: every VWAP-pullback line caps the trigger close at VWAP + $0.30.
- Score card at the 9:45 bar: **8/10 (A)**.
  - ✅ 1 VWAP: above, rising.
  - ✅ 2 ADX: 47.
  - ✅ 3 EMA stack: $779.05 > 9 EMA $777.29 > 21 EMA $776.36.
  - ✅ 4 Candles: higher highs and higher lows, with the VWAP hold as the confirming candle.
  - ✅ 5 Key level: holding above R1 $777.75.
  - ❌ 6 Volume: 0.62×.
  - ❌ 7 Momentum: RSI 75.6 is overbought, though MACD is above its signal.
  - ✅ 8 Higher timeframe: daily above the 50-day; Monday was a trend day.
  - ✅ 9 QQQ: above its VWAP.
  - ✅ 10 News: quiet, mildly positive.
- 0DTE checklist:
  - Direction: ✅
  - Candles: ✅
  - News: ✅
  - Risk: ✅ $25.50 is within the 10% max, $0.50 over the 5% default.
  - Time: ✅ after 9:45.
- **Option:** SPY 782C 10/6 ×1. Entry is $0.25 (5-min close) + $0.005 (half spread) = **$0.255 ($25.50)**. The 782C is the nearest-the-money strike under the cap; the 781C at $0.445 was over. Stop = 50% of premium ($0.13) or a SPY close below $777.60. Target: SPY $780.00. Out by 3:30.
- **Fractional:** SPY 0.3209 sh @ $779.045 (≈ $250, 50% of the account). The stop is an alert at SPY $777.60 (risk $0.46); target $780.00 (+$0.31). Out by 3:45.
- Play-forward to 9:57: the stop and target have not been hit. SPY high $779.95, $0.05 under the target; 782C last $0.47 (+84%). **Still open.**
- 4H (8 AM–12 PM bar): this is the expansion leg up from the pre-market open (~$777.8), with no sweep below the open first, so no setup D.
- F squeeze: n/a; less than 45 minutes of session.

ARMED (valid until 10:12):
- ARMED B long (VWAP pullback, second entry): trigger = a 5-min bar with low within $0.10 of VWAP that closes above VWAP **and no more than VWAP + $0.30**, and above the prior close, QQQ above its VWAP; entry = trigger close; stop = $778.00; target = $780.66 (R2); reward/risk ≥ 1.5 at any allowed close; option = nearest-the-money 0DTE call ≤ $25 (total open premium stays ≤ $50); valid until 10:12.

**Setup check (10:23 AM ET; the :12 run fired late): 10/6 VWAP pullback CLOSED, both legs winners**
- **Option 782C ×1:** the journal exit rule is a +50% limit, $0.39. The 782C reached $0.47 in the 9:55 bar, so the limit filled at **$0.39 → +$13.50** (+53%). The 9:58 check reported the trade still open at $0.47; that was wrong under this rule, and this entry corrects it.
- **Fractional SPY 0.3209 sh:** the target of $780.00 was hit at 10:00 (high $780.19) → **+$0.31**.
- Day trades used (paper): 1.
- Replay of the 9:58 ARMED B long (with the VWAP + $0.30 cap): did not fire. The 9:55, 10:00 and 10:05 bars never came within $0.10 of VWAP; the closest low was $779.27 vs VWAP $778.75.
- Now: SPY tagged **R2 $780.66** (high $780.67 on the 10:10 bar) and was turned back. The 10:15 bar closed at $779.64 on a pullback toward VWAP ($779.23, still rising). QQQ $761.35, above its VWAP of $760.79. ADX was 47 at 9:50. RSI has cooled from 76. No A/B entry at this moment: price is mid-pullback, between R2 resistance and VWAP.
- 4H (8 AM–12 PM bar): still the expansion leg up, no setup D.
- F squeeze: n/a; less than 45 minutes in a tight range.

ARMED (valid until 10:42):
- ARMED B long (VWAP pullback): trigger = a 5-min bar with low within $0.10 of VWAP that closes above VWAP and no more than VWAP + $0.15 (at + $0.30 the reward/risk would be only 1.3), and above the prior close, QQQ above its VWAP; entry = trigger close; stop = $778.70 (below the OR high $778.78); target = $780.66 (R2 / day high); reward/risk ≥ 1.5 at any allowed close; option = nearest-the-money 0DTE call ≤ $25; valid until 10:42.

**Setup check (10:27 AM ET): nothing fired**
- Replay: the 10:20 bar came within $0.10 of VWAP (low $779.35 vs VWAP $779.25). But it closed at $779.545, above the $779.40 cap and below the prior close of $779.64, so the B long did not fire.
- SPY is drifting down toward VWAP after the R2 rejection. QQQ $761.11 is still above its VWAP of $760.81. No open trades; no new A/B setup.
- The 10:23 ARMED B long stays armed unchanged until 10:42.

**Setup check (10:42 AM ET): nothing fired; SPY chopping around VWAP**
- Replay of the B long (cap VWAP + $0.15):
  - 10:25 and 10:30 bars closed *below* VWAP (low $778.565), so no.
  - 10:35 bar: low $779.16, within $0.10 of VWAP $779.24, but it closed $779.69, above the $779.39 cap. Not fired.
- SPY $779.69 is back above VWAP $779.24 after two closes below it. VWAP is now flat. QQQ $760.95 is above its VWAP of $760.75.
- **Trend-day check (from 10:30): no.** SPY closed on the wrong side of VWAP at 10:25 and 10:30.
- The 0DTE "direction is clear" check fails while SPY crosses VWAP back and forth. No VWAP-pullback arm until it holds one side again.
- 4H (8 AM–12 PM bar): up from the open, now pulling back inside the bar. No setup D.
- **F squeeze range (9:55–10:40, 45 min):** high $780.67 (= R2), low $778.565; $2.10 wide. Prior 10-bar volume average ≈ 241k, so 1.5× ≈ 362k.
- No A/B setup now.

ARMED (valid until 10:57):
- ARMED F long: trigger = 5-min close above $780.67 and no higher than $780.75 on ≥ 1.5× (≈ 362k), QQQ breaking above its range high $762.09; entry = trigger close; stop = $780.15; target = $781.65; reward/risk ≥ 1.5 for any allowed close; option = nearest-the-money 0DTE call ≤ $25; valid until 10:57.
- (No F short: it is against the bullish bias above $776.6, and R1 $777.75 is too close below the range low for reward/risk ≥ 1.5.)

**Setup check (10:58 AM ET): nothing fired**
- Replay: F long (close > $780.67) did not fire. The highest close was $780.325 (10:50 bar), on light volume (142k).
- SPY $780.33 is back above a rising VWAP ($779.34): four closes above it since 10:35. ADX 42. QQQ $762.14 is above its VWAP of $760.88, at its range high.
- F squeeze range unchanged: $778.565–$780.67 ($2.10 wide, held since 9:55). Prior 10-bar volume average ≈ 226k, so 1.5× ≈ 339k.
- 4H (8 AM–12 PM bar): up, consolidating under R2; no setup D.
- No A/B setup now: SPY is mid-range, $0.35 under R2. A VWAP-pullback arm can't reach reward/risk 1.5 with the stop below the 10:30 low.

ARMED (valid until 11:12):
- ARMED F long: trigger = 5-min close above $780.67 and no higher than $780.75 on ≥ 1.5× (≈ 339k), QQQ breaking above its range high $762.19; entry = trigger close; stop = $780.15; target = $781.65; option = nearest-the-money 0DTE call ≤ $25; valid until 11:12.

**Setup check (11:13 AM ET): nothing fired. R2 broke on light volume**
- Replay: F long. The 11:05 bar closed $780.75, inside the $780.67–$780.75 band, but on 155k vs the ≥ 339k needed (0.69×). **Not fired** (no partial credit). QQQ did break its range high ($762.73).
- Quiet grind again (pattern 8 in missed-moves): SPY made a new high of $781.00 on falling volume. VWAP $779.46 is rising; QQQ is above its VWAP.
- Trend-day check: still no, because of the 10:25 and 10:30 closes below VWAP.
- F squeeze range is no longer valid: price closed above $780.67. R2 $780.66 is now the level to retest. R3 ≈ $784.7 (too far to target); the range-height projection is ≈ $782.8.
- 4H (8 AM–12 PM bar): up, new high; no setup D.
- No live A/B entry: $780.75 sits right on the break, and buying a breakout on 0.69× volume fails factor 6.

ARMED (valid until 11:27; prior 10-bar average ≈ 191k):
- ARMED C long (break and retest of R2): trigger = 5-min bar with low between $780.56 and $780.76 (a retest of $780.66), closing above $780.66 and no higher than $780.85, on ≥ 1.0× (≈ 191k), QQQ above its VWAP; entry = trigger close; stop = $780.36 ($0.30 below the level); target = $781.65; reward/risk ≥ 1.6 at any allowed close; option = nearest-the-money 0DTE call ≤ $25; valid until 11:27.

**Setup check (11:27 AM ET): nothing fired. SPY grinding higher without us**
- Replay of the C long (R2 retest): the 11:10 bar's low $780.71 was a valid retest, but it closed $781.14 (above the $780.85 cap) on 90k (0.47×, needed ≥ 1.0×). Not fired.
- SPY $781.42 (high $781.49): five straight higher closes since 11:00, all on below-average volume. VWAP is $779.59 and rising; QQQ $762.46 is above its VWAP.
- Missed-move candidate for the EOD review: R2 broke at 11:05 and SPY rose +$0.75 by 11:25, on light volume again (pattern 8).
- Trend-day check: still no, because of the 10:25 and 10:30 closes below VWAP.
- 4H (8 AM–12 PM bar): up, new highs. No setup D.
- No F range: price is trending, not compressing.

ARMED (valid until 11:42; prior 10-bar average ≈ 156k):
- ARMED C long (R2 retest, second try): trigger = 5-min bar with low between $780.56 and $780.90, closing above $780.66 and no higher than $781.00, on ≥ 1.0× (≈ 156k), QQQ above its VWAP; entry = trigger close; stop = $780.36; target = $782.40; reward/risk ≥ 2.1 at any allowed close; option = nearest-the-money 0DTE call ≤ $25; valid until 11:42.

**Setup check (11:43 AM ET): nothing fired**
- Replay: C long (R2 retest) did not fire. The lows were $781.29, $781.01 and $781.07, never down to $780.90.
- SPY $781.40 is pausing under the $781.62 high. VWAP is $779.73 and rising; QQQ $762.12 is above its VWAP of $761.25, though slightly weaker than SPY.
- **F squeeze range (10:55–11:40):** $780.125–$781.62, $1.50 wide. Prior 10-bar average ≈ 143k, so 1.5× ≈ 214k.
- 4H (8 AM–12 PM bar): up; it closes at noon. No setup D.
- No live A/B: mid-range, volume light.

ARMED (valid until 11:57):
- ARMED F long: trigger = 5-min close above $781.62 and no higher than $781.75 on ≥ 1.5× (≈ 214k), QQQ breaking above its range high $762.86; entry = trigger close; stop = $781.20; target = $782.60; reward/risk ≥ 1.5 at any allowed close; option = nearest-the-money 0DTE call ≤ $25; valid until 11:57.
- ARMED C long (R2 retest): unchanged from 11:27 (low $780.56–$780.90, close $780.66–$781.00, ≥ 1.0× ≈ 143k, QQQ above its VWAP; stop $780.36; target $782.40); valid until 11:57.

**Setup check (11:58 AM ET): nothing fired; midday lull**
- Replay:
  - F long: no close above $781.62.
  - C long: the 11:45 bar's low $780.87 was a valid retest, but it closed $781.24 (above the $781.00 cap). Not fired.
- SPY $781.11 is flat in a tight range. VWAP $779.82 is rising; QQQ $761.99 is above its VWAP of $761.32. Volume is drying up (84k on the last bar).
- F squeeze range (10:55–11:55): $780.125–$781.62, $1.50 wide. Prior 10-bar average ≈ 131k, so 1.5× ≈ 197k.
- 4H: the 8 AM–12 PM bar closes near its highs (bullish). The 12–4 PM bar opens at noon; watch for a sweep below its open (setup D).
- No live A/B.

ARMED (valid until 12:12):
- ARMED F long: trigger = 5-min close above $781.62 and no higher than $781.75 on ≥ 1.5× (≈ 197k), QQQ breaking above $762.86; entry = trigger close; stop = $781.20; target = $782.60; option = nearest-the-money 0DTE call ≤ $25; valid until 12:12.
- ARMED C long (R2 retest): low $780.56–$780.90, close $780.66–$781.00 on ≥ 1.0× (≈ 131k), QQQ above its VWAP; entry = trigger close; stop = $780.36; target = $782.40; valid until 12:12.

**Setup check (12:14 PM ET): nothing fired. The QQQ filter blocked the R2 retest**
- Replay:
  - F long: no close above $781.62.
  - **C long:** the 12:05 bar met the price and volume parts: low $780.71 (retest), close $780.80 (inside $780.66–$781.00), 163k (≥ 1.0× ≈ 126k). **But QQQ closed $761.21, below its VWAP of $761.34, so it did not fire.** That is the market-agreement filter working as written. Track this bar in the EOD play-forward (would it have stopped at $780.36 or reached $782.40?).
- SPY $780.80 is easing within the range; VWAP $779.89 is still rising. **QQQ has slipped below its VWAP** (rolling over from $762.86): SPY and QQQ now disagree.
- F squeeze range (10:55–12:10): $780.125–$781.62, held 75 min. Prior 10-bar average ≈ 126k.
- 4H 12–4 PM bar: opened ≈ $781.1 and is trading below its open. A sweep of $780.125 and then a reclaim would be the setup D pattern; watch for it.
- No live A/B: SPY and QQQ disagree.

ARMED (valid until 12:27):
- ARMED B long (VWAP pullback): trigger = 5-min bar with low within $0.10 of VWAP (≈ $779.90) that closes above VWAP and no more than VWAP + $0.10, and above the prior close, **QQQ back above its VWAP**; entry = trigger close; stop = $779.45; target = $781.10; reward/risk ≥ 1.9; option = nearest-the-money 0DTE call ≤ $25; valid until 12:27.
- ARMED C long (R2 retest): as before (low $780.56–$780.90, close $780.66–$781.00, ≥ 1.0× ≈ 126k, QQQ above its VWAP; stop $780.36; target $782.40); valid until 12:27.

**Setup check (12:28 PM ET): nothing fired**
- Replay:
  - B long: lows $780.45–$780.76, never within $0.10 of VWAP ($779.93).
  - C long: 12:10 bar closed $781.02 (cap $781.00); 12:15 low $780.45 was below the retest band. 12:20 bar matched on price (low $780.565, close $780.69) but had 114k (0.92×, needed 1.0×), and QQQ was below its VWAP. Not fired.
- SPY $780.69 is slipping back toward R2; VWAP $779.94 is rising. QQQ $761.14 is still below its VWAP of $761.33. The divergence continues.
- F range ($780.125–$781.62) still holds, now 90 min.
- 4H 12–4 PM bar: below its ≈ $781.1 open. A sweep of $780.125 followed by a reclaim would be the setup D pattern.
- No live A/B. Dropping the C retest line: it has failed four times and the level is being worn down.

ARMED (valid until 12:42):
- ARMED D long (sweep and reclaim): trigger = after a 5-min low below $780.125, a 5-min close back above $780.30 and no higher than $780.45, QQQ back above its VWAP; entry = trigger close; stop = $779.70; target = $781.62; reward/risk ≥ 1.5; option = nearest-the-money 0DTE call ≤ $25; valid until 12:42.
- ARMED B long (VWAP pullback): as at 12:14 (low within $0.10 of VWAP ≈ $779.95, close above VWAP and ≤ VWAP + $0.10, above the prior close, QQQ above its VWAP; stop $779.45; target $781.10); valid until 12:42.

**Setup check (12:43 PM ET): nothing fired**
- Replay:
  - D long: the 12:35 bar swept to $780.04 (below $780.125) and closed $780.30. But QQQ closed $761.05, below its VWAP of $761.31, so it did not fire.
  - B long: the 12:35 low $780.04 was within $0.10 of VWAP ($779.96), but it closed $780.30, above the VWAP + $0.10 cap. Not fired.
- SPY $780.30 is drifting down toward VWAP ($779.96, flattening). QQQ is still below its VWAP. The F range low ($780.125) has been poked; the range is losing shape.
- 4H 12–4 PM bar: below its open, in a possible manipulation leg (setup D) if SPY reclaims $780.6+ with QQQ.
- No live A/B: QQQ disagrees with SPY.

ARMED (valid until 12:57):
- ARMED B long (VWAP pullback): low within $0.10 of VWAP (≈ $779.97), close above VWAP and ≤ VWAP + $0.10, above the prior close, QQQ above its VWAP; stop $779.45; target $781.10; valid until 12:57.
- ARMED D long (sweep and reclaim): after a 5-min low below $780.125, a later 5-min close of $780.30–$780.45 with QQQ above its VWAP; stop $779.70; target $781.62; valid until 12:57.

**Setup check (12:58 PM ET): nothing fired; chop at VWAP**
- Replay: QQQ never closed back above its VWAP ($761.30; best close $761.19), so the B and D longs both stayed blocked. The B long also failed on price at 12:45 (low $779.86, but it closed $780.12, above the VWAP + $0.10 cap, and below the prior close).
- SPY $780.06 is sitting on a flat VWAP ($779.97). QQQ is below its VWAP. The F range ($780.125–$781.62) has failed on the low side by a few cents only; no break.
- 0DTE check 1 (direction is clear) fails: SPY is on VWAP and QQQ is against it. **No trade.**
- 4H 12–4 PM bar: below its open (≈ $781.1), low $779.86. Still possible manipulation-then-expansion (setup D) if SPY and QQQ reclaim together.

ARMED (valid until 1:12):
- ARMED D long (sweep and reclaim): after the 12:45 sweep to $779.86, a 5-min close of $780.30–$780.45 with QQQ above its VWAP; stop $779.70; target $781.62; option = nearest-the-money 0DTE call ≤ $25; valid until 1:12.
- ARMED B long (VWAP pullback): low within $0.10 of VWAP (≈ $779.98), close above VWAP and ≤ VWAP + $0.10, above the prior close, QQQ above its VWAP; stop $779.45; target $781.10; valid until 1:12.

**Setup check (1:13 PM ET): nothing fired; SPY slipping under VWAP**
- Replay: no D or B long. QQQ stayed below its VWAP the whole time (closes $760.63–$761.06 vs $761.28–$761.30), so neither could fire.
- SPY closed $779.88 and $779.93, just under a flat VWAP ($779.97); afternoon low $779.70. QQQ $760.63 is pulling away below its VWAP. Volume is light (≈ 108k average).
- The F range ($780.125–$781.62) has broken on the low side, with no volume.
- 4H 12–4 PM bar: below its open; the low is extending ($779.70). Not a D reversal yet.
- No A/B: SPY is on VWAP, so direction is unclear.

ARMED (valid until 1:27; prior 10-bar average ≈ 108k):
- ARMED E short (VWAP breakdown): trigger = 5-min close below $779.70 and no lower than $779.55 on ≥ 1.5× (≈ 162k), QQQ below its VWAP; entry = trigger close; stop = $780.10; target = $778.60 (above the morning low $778.565); reward/risk ≥ 1.7; option = nearest-the-money 0DTE put ≤ $25 (after 1:30 use the nearest-the-money strike or skip); valid until 1:27.
- ARMED D long (sweep and reclaim): a 5-min close of $780.30–$780.45 with QQQ above its VWAP; stop $779.70; target $781.62; valid until 1:27.

**Setup check (1:28 PM ET): nothing fired. SPY broke below VWAP on light volume**
- Replay:
  - E short: the 1:10 bar closed $779.60 (inside the $779.55–$779.70 band) but on 103k vs ≥ 162k (0.64×). The 1:15 bar closed $779.23, below the band. Not fired.
  - D long: no.
- **Missed-move candidate:** SPY fell from $779.93 to a $778.90 low (−$1.0) in 15 minutes, again on light volume (pattern 8, this time downward).
- SPY $779.24 is below VWAP ($779.94, now sloping down slightly). QQQ $760.16 is below its VWAP of $761.24. They agree on bearish for the first time today.
- Morning low $778.565 is the next support, then R1 $777.75. The daily trend and the bias (bullish above $776.6) are against shorts, so factor 8 is ❌; B grade at best.
- 4H 12–4 PM bar: low $778.90, below its open. Distribution so far.
- After 1:30: nearest-the-money strike only, or skip (Friday proposal 4, followed here as a precaution).

ARMED (valid until 1:42; prior 10-bar average ≈ 110k):
- ARMED B short (VWAP rejection): trigger = 5-min bar with high within $0.10 of VWAP (≈ $779.93) that closes below VWAP and no lower than VWAP − $0.10, below the prior close, QQQ below its VWAP; entry = trigger close; stop = $780.35; target = $778.60; reward/risk ≥ 2.0; option = nearest-the-money 0DTE put ≤ $25, or skip; valid until 1:42.
- ARMED E short (continuation): trigger = 5-min close below $778.90 and no lower than $778.75 on ≥ 1.5× (≈ 165k), QQQ below its VWAP; entry = trigger close; stop = $779.35; target = $777.80 (just above R1); reward/risk ≥ 1.5; valid until 1:42.

**Setup check (1:43 PM ET): nothing fired; V-bounce back to VWAP**
- Replay:
  - B short: 1:25 high $779.76 was $0.17 short of VWAP; 1:30 closed $779.99, *above* VWAP; 1:35 high $780.08 was $0.15 over (outside the $0.10 band). Not fired.
  - E short: no close below $778.90. Not fired.
- The 1:20 sweep to $778.90 was bought hard: 1:25 bar +$0.47 on 201k (≈ 1.9×). SPY $779.88 is back on a flat VWAP ($779.93). QQQ $761.00 is recovering toward its VWAP ($761.21).
- 4H 12–4 PM bar: low $778.90 swept, now reclaiming. A setup D shape is forming, but SPY needs to get back above VWAP with QQQ.
- No live A/B: SPY is on VWAP.
- Entry windows: new 0DTE entries until 2:30, arming until 2:15. After 1:30, nearest-the-money strike only or skip.

ARMED (valid until 1:57):
- ARMED D long (sweep $778.90 → reclaim): trigger = 5-min close above VWAP (≈ $779.95) and no higher than $780.10, QQQ above its VWAP; entry = trigger close; stop = $779.45; target = $781.10; reward/risk ≥ 1.5; option = nearest-the-money 0DTE call ≤ $25, or skip; valid until 1:57.
- ARMED B short (VWAP rejection): 5-min bar with high within $0.10 of VWAP, closing below VWAP and no lower than VWAP − $0.10, below the prior close, QQQ below its VWAP; stop $780.35; target $778.90; valid until 1:57.

**Setup check (1:58 PM ET): nothing fired; flat at VWAP**
- Replay:
  - D long: the 1:45 bar closed $779.995 (above VWAP, inside the band), but QQQ was $760.97, below its VWAP of $761.21. Blocked.
  - B short: the 1:40 bar matched on high and close but closed $779.90, *above* the prior close $779.88. 1:50 high $780.19 was outside the band. Not fired.
- SPY $779.85 is on a flat VWAP ($779.93). QQQ is just under its VWAP. Dead midday chop.
- **F squeeze range (1:10–1:55):** $778.90–$780.19 ($1.29 wide). Prior 10-bar average ≈ 113k, so 1.5× ≈ 170k.
- 4H 12–4 PM bar: swept to $778.90 then reclaimed, flat. No expansion yet.
- Last arming of the day (arming stops at 2:15; no new 0DTE after 2:30; nearest-the-money strike only).

ARMED (valid until 2:12):
- ARMED F long: trigger = 5-min close above $780.19 and no higher than $780.30 on ≥ 1.5× (≈ 170k), QQQ above its VWAP; entry = trigger close; stop = $779.80; target = $781.10; reward/risk ≥ 1.6; option = nearest-the-money 0DTE call if ≤ $25, else skip; valid until 2:12.
- ARMED F short: trigger = 5-min close below $778.90 and no lower than $778.75 on ≥ 1.5× (≈ 170k), QQQ below its range low $759.73; entry = trigger close; stop = $779.35; target = $777.80; reward/risk ≥ 1.5; option = nearest-the-money 0DTE put if ≤ $25, else skip; valid until 2:12.

**Setup check (2:14 PM ET): nothing fired; arming closed for the day**
- Replay: F long: closes $780.14 and $780.18, never above $780.19 (2:00 bar 154k, 2:05 bar 83k). F short: no. Neither fired.
- SPY $780.18 is just above a flat VWAP ($779.93); QQQ $761.39 is back above its VWAP of $761.20. Range $778.90–$780.24.
- No new ARMED list: a trigger armed now would fire at the earliest on the 2:15 bar, too close to the 2:30 cutoff for new 0DTE entries. No open paper trades. Remaining checks report only; EOD review at 3:47.

**Setup check (2:28 PM ET): entry window closing; nothing armed or open**
- SPY $779.91, flat around VWAP (≈ $779.93) in a $778.90–$780.35 afternoon range. No triggers were armed. No paper trades are open. Remaining checks report only; EOD review at 3:47.

**End of day (3:48 PM ET)**
- Paper trades today: 1 setup (B, VWAP pullback, armed and replayed, graded A with a reward/risk arming defect), two legs:
  - SPY 782C: **+$13.50** (+50% limit filled at 9:55).
  - SPY fractional: **+$0.31** (target $780 at 10:00).
- No open positions overnight.
- Running totals: **7 trades, 3 wins, 4 losses, +$14.57** (options +$14.50, fractional +$0.07). A-grade: 2 legs (asterisked).
- Day: gap up held, R2 $780.66 broke on light volume (high $781.62 at 11:25), then a slow fade into a flat VWAP (≈ $779.9). Close ≈ $779.6 (+$4.8 vs Monday).
- **QQQ filter check:** the 12:05 R2-retest trigger blocked by QQQ < VWAP would have been stopped at $780.36 (12:15 low $780.45; the 12:25 low $780.24 went through it). The filter saved a loss.
- Missed: +$3.06 (10:30–11:25); see missed-moves.md.

### 2026-10-07 (Wed)

**Pre-market brief (8:54 AM ET)**
- SPY pre-market $776.16 (−0.38%, gap down ≈ $2.9); QQQ $754.52 (−0.68%), IWM −0.84%. Tech is leading lower.
- Tuesday: high $781.62, low $777.96, close $779.09.
- Pivots: R2 $783.22, R1 $781.15, **P $779.56**, **S1 $777.49**, **S2 $775.90**.
- 20/50-day SMA: indicator call failed this morning. Last known values (10/6): ≈ $765 / $764.4, both rising, so the daily uptrend is intact.
- Strong levels: **$777.5–778.0** (S1 and Tuesday's low; first resistance from below), **$779.1–779.6** (Tuesday's close, pivot, Tuesday's VWAP area), **$775.9** (S2), $776.6 (Monday's high).
- News and calendar: Alpha Vantage news was rate-limited, so neither could be checked. Treat 10:00 AM and 2:00 PM as possible event times (FOMC minutes may be due this week; not verified).
- Gap < $4: normal ORB rules.
- **Bias: bearish below $777.5** (opening under Tuesday's low and S1, QQQ weaker). It flips to none on a reclaim of $777.5 and bullish only above $779.6. Watch S2 $775.9 for a gap-fill bounce.

**Opening check (9:42 AM ET): opening range forming, weak open**
- SPY opened $775.75 (below S2 $775.90) and dropped: range so far **$774.25–$776.15**; last $774.51. VWAP ≈ $775.35 (computed from the bars; the indicator tool returned an error this morning). Volume is heavy: 522k, then 321k.
- QQQ $752.50 is below its VWAP (≈ $753.67) and weaker than SPY. **Bias: bearish** (below S2, Tuesday's low and VWAP, QQQ agrees).
- Supports below: Monday's pivot $773.69 and Monday's 10:55 high $772.9; then Monday's S1 $770.78.

ARMED (valid 9:45–10:12; volume reference = average of the three opening-range bars; final range set at 9:45):
- ARMED A short (ORB): trigger = 5-min close below the final range low (≈ $774.25) and no more than $0.10 below it, on ≥ 1.0×, SPY below VWAP, QQQ below its VWAP; entry = trigger close; stop = $774.85; target = $772.90; reward/risk ≥ 1.8; option = nearest-the-money 0DTE put ≤ $25; valid until 10:12.
- ARMED B short (VWAP rejection): trigger = 5-min bar with high within $0.10 of VWAP that closes below VWAP, no more than $0.15 below it, and below the prior close, QQQ below its VWAP; entry = trigger close; stop = VWAP + $0.35; target = the range low ($774.25); reward/risk ≥ 1.5 at the actual close or skip; valid until 10:12.

**Setup check (9:58 AM ET): nothing fired; bounce back to VWAP**
- Final opening range: **$774.25–$776.15**. Average volume of the 3 opening bars ≈ 367k.
- Replay:
  - A short: no close below $774.25 (9:45 close $774.31, low $774.10).
  - B short: the 9:50 bar touched VWAP but closed $775.02, *above* the prior close. Not fired.
- SPY $775.02 is sitting on VWAP ($775.02, falling). QQQ $753.40 has crept just above its VWAP ($753.30). Volume is fading (217k–219k). Direction is unclear now, so the 0DTE check 1 fails. No entry.
- 4H (8 AM–12 PM bar): opened ≈ $776 pre-market, low $774.10 so far. A possible manipulation leg down (setup D) if SPY reclaims $776.15 later; too early to call.

ARMED (valid until 10:12):
- ARMED A short (ORB): 5-min close $774.15–$774.25 (just below the range low) on ≥ 1.0× (≈ 367k), SPY below VWAP, QQQ below its VWAP; stop $774.85; target $772.90; valid until 10:12.
- ARMED B short (VWAP rejection): 5-min bar with high within $0.10 of VWAP (≈ $775.0) that closes below VWAP, no more than $0.15 below it, and below the prior close, QQQ below its VWAP; stop VWAP + $0.35; target $774.25; skip if reward/risk < 1.5 at the actual close; valid until 10:12.
- (No long: the bias stays bearish below $777.5.)

**Setup check (10:19 AM ET; the :12 run fired late): nothing fired; slow drift at the range low**
- Replay:
  - A short: no close below $774.25 (closes $774.79, $774.55, $774.47).
  - B short: 9:55 closed $774.79, more than $0.15 under VWAP, and QQQ was *above* its VWAP. Not fired.
- SPY $774.31 is drifting down to the range low on falling volume (111k–147k). VWAP ≈ $774.9. QQQ $753.49 is back above its VWAP (≈ $753.4): SPY and QQQ disagree. No trade.
- **F squeeze range (9:35–10:15):** $774.03–$775.55, $1.52 wide. Prior 9-bar average ≈ 236k, so 1.5× ≈ 355k.
- 4H (8 AM–12 PM bar): down from the open, low $774.03.

ARMED (valid until 10:27):
- ARMED F short: 5-min close below $774.03 and no more than $0.10 below it, on ≥ 1.5× (≈ 355k), QQQ breaking below its range low $751.76; entry = trigger close; stop $774.45; target $772.90; reward/risk ≥ 2.0; option = nearest-the-money 0DTE put ≤ $25; valid until 10:27.

**Setup check (10:28 AM ET): nothing fired; double bottom at $774.03–774.10**
- Replay: F short did not fire. The 10:10 low $774.03 held, with no close below it.
- SPY $774.77 is bouncing off a double bottom ($774.10 at 9:45, $774.03 at 10:10), just under VWAP (≈ $774.85). **QQQ is leading up:** $754.74, well above its VWAP (≈ $753.5) and back near its opening high.
- The bearish bias is weakening: SPY is lagging QQQ. A VWAP reclaim with QQQ strength would be a B-grade long against the morning bias (factor 10/news unknown, factor 8 daily trend ✅).
- F range: $774.03–$775.55 (since 9:35).

ARMED (valid until 10:42):
- ARMED B long (VWAP reclaim after the double bottom): trigger = 5-min close above VWAP (≈ $774.85) and no more than VWAP + $0.15, above the prior close, QQQ above its VWAP; entry = trigger close; stop = $774.45 (below the 10:20 low); target = $776.15 (opening-range high); reward/risk ≥ 1.5 at the actual close or skip; option = nearest-the-money 0DTE call ≤ $25; valid until 10:42.

**Setup check (10:43 AM ET): nothing fired; tight range**
- Replay: B long did not fire. No close above VWAP (≈ $774.8): closes $774.44, $774.49, $774.63.
- SPY $774.63 is boxed in $774.03–$774.99 since 10:00 on thin volume (76k–159k). QQQ $754.59 is above its VWAP. SPY is lagging. No A/B setup.
- **F squeeze range (10:00–10:40):** $774.03–$774.99, $0.96 wide. Prior 10-bar average ≈ 138k, so 1.5× ≈ 207k.
- 4H (8 AM–12 PM bar): down from ≈ $776, basing at $774.0. A reclaim of $776.15 would make it a setup D reversal.

ARMED (valid until 10:57):
- ARMED F long: 5-min close above $774.99 and no higher than $775.10 on ≥ 1.5× (≈ 207k), QQQ breaking above its range high $755.09; stop $774.55; target $776.15; reward/risk ≥ 1.9; option = nearest-the-money 0DTE call ≤ $25; valid until 10:57.
- ARMED F short: 5-min close below $774.03 and no lower than $773.93 on ≥ 1.5× (≈ 207k), QQQ breaking below its range low $752.86; stop $774.45; target $772.90; reward/risk ≥ 2.1; option = nearest-the-money 0DTE put ≤ $25; valid until 10:57.

**Setup check (10:58 AM ET): nothing fired; slow leak lower**
- Replay: F short: the 10:40 bar closed $773.88, below $774.03 but outside the $0.10 band, on 124k (needed ≥ 207k), with QQQ not breaking its low. Not fired. F long: no.
- SPY $773.98, low $773.61. It is drifting below the range on light volume again (pattern 8). VWAP ≈ $774.6 and falling. QQQ $753.76 is near its VWAP (≈ $753.6), no confirmation.
- Next support: Monday's pivot $773.69 (being tested) and Monday's 10:55 high $772.9.
- A continuation short below $773.61 fails reward/risk (no level before $772.9). Only a VWAP-rejection short has room.

ARMED (valid until 11:12):
- ARMED B short (VWAP rejection): 5-min bar with high within $0.10 of VWAP (≈ $774.55) that closes below VWAP, no more than $0.15 below it, and below the prior close, QQQ below its VWAP; entry = trigger close; stop $774.95; target $773.61; reward/risk ≥ 1.5 at the actual close or skip; option = nearest-the-money 0DTE put ≤ $25; valid until 11:12.

**Setup check (11:15 AM ET; the :12 run fired late): nothing fired; QQQ breaking out, SPY reclaiming VWAP**
- Replay: B short did not fire. Highs $774.47/$774.39/$774.47 stayed $0.2+ under VWAP (≈ $774.7), and QQQ was above its VWAP.
- 11:10 bar: SPY closed **$774.83, back above VWAP ($774.68)** on 162k (1.4×). **QQQ broke its morning high** ($755.56 > $755.09), well above its VWAP ($753.70).
- Not a live entry: SPY's VWAP is still flat or falling (score-card factor 1, required, is ❌), and the reclaim is one bar old. The morning low $773.61 is now a higher-timeframe sweep. If SPY holds above VWAP, this becomes a setup D (sweep and reclaim) shape on the 8 AM–12 PM 4H bar.

ARMED (valid until 11:27; prior 10-bar average ≈ 115k):
- ARMED B long (VWAP hold): 5-min bar with low within $0.10 of VWAP (≈ $774.7) that closes above VWAP, no more than $0.15 above it, and above the prior close, QQQ above its VWAP; stop $774.25; target $776.15 (opening-range high); reward/risk ≥ 1.5 at the actual close or skip; option = nearest-the-money 0DTE call ≤ $25; valid until 11:27.
- ARMED E long (opening-range-high break): 5-min close above $776.15 and no higher than $776.25 on ≥ 1.5× (≈ 173k), QQQ above its VWAP; stop $775.70; target $777.49 (S1); reward/risk ≥ 2.2; valid until 11:27.

**Setup check (11:28 AM ET): nothing fired (B long missed the close band by $0.01)**
- Replay (VWAP ≈ $774.69):
  - 11:15 bar: low $774.67 (on VWAP) and close $774.8475, above VWAP and the prior close, QQQ above its VWAP. But the close band is VWAP + $0.15 = $774.84, so it was **over by $0.0075. Not fired** (rule as written).
  - 11:20 bar: closed below the prior close. Not fired.
  - E long: no close above $776.15.
- SPY $774.73 is chopping on VWAP; QQQ $754.76 is holding above its VWAP and near its high. Factor 1 (VWAP slope) is still flat, so no live entry.
- Play-forward of the near-miss for the record: track it in EOD (entry $774.85, stop $774.25, target $776.15).

ARMED (valid until 11:42): same two lines as 11:15.
- ARMED B long (VWAP hold): low within $0.10 of VWAP, close above VWAP and no more than VWAP + $0.15, above the prior close, QQQ above its VWAP; stop $774.25; target $776.15; reward/risk ≥ 1.5 or skip; valid until 11:42.
- ARMED E long: 5-min close of $776.15–$776.25 on ≥ 1.5× (≈ 165k), QQQ above its VWAP; stop $775.70; target $777.49; valid until 11:42.

**Setup check (11:43 AM ET): nothing fired; SPY pushing up with QQQ**
- Replay (VWAP ≈ $774.70):
  - B long: the 11:25 low $774.59 was $0.11 under VWAP (outside the band); the 11:30 bar touched VWAP but closed $775.04, $0.34 above it (over the $0.15 band); 11:35 never touched. Not fired.
  - E long: no close above $776.15.
- SPY $775.78 (11:35 bar +$0.74 on 173k, 1.5×). QQQ $756.03 is at a new day high. The morning low ($773.61) sweep and reclaim is now a setup D shape on the 8 AM–12 PM 4H bar.
- Unfilled 11:15 near-miss (B long $774.85, stop $774.25, target $776.15): still alive (low $774.42, high $775.94).
- Next level: the opening-range high $776.15, then S1 $777.49.

ARMED (valid until 11:57; prior 10-bar average ≈ 111k):
- ARMED E long (opening-range-high break): 5-min close of $776.15–$776.25 on ≥ 1.5× (≈ 167k), QQQ above its VWAP; stop $775.70; target $777.49; reward/risk ≥ 2.2; option = nearest-the-money 0DTE call ≤ $25; valid until 11:57.

**Setup check (11:58 AM ET): nothing fired. Rally from the low; E long missed the band by $0.01**
- Replay: E long. The 11:45 bar closed **$776.26** (band $776.15–$776.25, over by $0.01) on 149k (needed ≥ 167k, 0.89× of 1.5×). **Not fired.**
- **Missed-move candidate:** 10:50 low $773.61 → 11:50 high $776.60 = **+$3.0 in about an hour.** Sweep of the morning low, VWAP reclaim at 11:10 (1.4×), QQQ leading to new highs. For the EOD review.
- **Unfilled 11:15 near-miss** (B long, entry $774.85, stop $774.25, target $776.15): **target hit at 11:45** (high $776.45). It would have been +$1.30 (+2.2R). Not counted (it did not fire as written), but noted for the band-rule review.
- SPY $776.28 is above the opening-range high and VWAP (now turning up). QQQ $756.73 is near its highs.

ARMED (valid until 12:12; prior 10-bar average ≈ 117k):
- ARMED C long (retest of the opening-range high $776.15): 5-min bar with low $776.05–$776.25, closing $776.15–$776.35, on ≥ 1.0× (≈ 117k), QQQ above its VWAP; entry = trigger close; stop $775.80; target $777.49 (S1 / Tuesday's low area); reward/risk ≥ 2.0; option = nearest-the-money 0DTE call ≤ $25; valid until 12:12.

**Setup check (12:13 PM ET): nothing fired; the volume filter saved a loss**
- Replay of the C long (retest of $776.15):
  - 11:55 bar matched on price (low $776.17, close $776.34) but had 94k (0.80×, needed ≥ 1.0×). **Not fired.**
  - 12:00 low $775.80 was below the band. 12:05 close $776.485 was above the band.
- Play-forward of the 11:55 near-miss: entry $776.34, stop $775.80. **The 12:00 low $775.799 would have stopped it by $0.001.** The filter saved a loss.
- SPY $776.49 is holding above the opening-range high and VWAP. QQQ $756.66 is above its VWAP. Day high $776.65; next level S1 $777.49.
- A continuation long above $776.65 fails reward/risk (S1 is only $0.84 away).
- 4H 12–4 PM bar: just opened ≈ $776.3.

ARMED (valid until 12:27):
- ARMED C long (retest of $776.15, wider stop): 5-min bar with low $776.05–$776.25, closing $776.15–$776.35, on ≥ 1.0× (≈ 117k), QQQ above its VWAP; entry = trigger close; stop $775.70 (below the 12:00 low); target $777.49; reward/risk ≥ 1.75; option = nearest-the-money 0DTE call ≤ $25; valid until 12:27.

**Setup check (12:28 PM ET): nothing fired; lunch drift up**
- Replay: C long did not fire (lows $776.35–$776.54, never back to $776.25).
- SPY $776.76 is at a new day high on very thin volume (45k–58k). QQQ $756.50 is flat above its VWAP. VWAP is rising (≈ $775.2).
- No A/B: entering here is chasing, with S1 $777.49 only $0.73 away.

ARMED (valid until 12:42): the same C long (low $776.05–$776.25, close $776.15–$776.35, ≥ 1.0× ≈ 95k, QQQ above its VWAP; stop $775.70; target $777.49).

**Setup check (12:43 PM ET): nothing fired**
- Replay: C long did not fire (lows $776.49 and $776.32, not back to $776.25).
- SPY $776.32 is easing toward the $776.15 retest zone on very thin volume (37k–67k). QQQ $755.99 is easing too but is still above its VWAP.
- ARMED (valid until 12:57): the same C long (low $776.05–$776.25, close $776.15–$776.35, ≥ 1.0× ≈ 76k, QQQ above its VWAP; stop $775.70; target $777.49).

**Setup check (12:58 PM ET): nothing fired; tight lunch range**
- Replay: C long did not fire (closest low $776.27, $0.02 above the band).
- SPY $776.34 is in a $775.80–$776.90 range since 12:00 ($1.10 wide) on very thin volume (avg ≈ 65k). QQQ is flat above its VWAP.
- F breakouts either way fail reward/risk inside this range (S1 $777.49 above, VWAP ≈ $775.4 below). Not armed.
- ARMED (valid until 1:12): the same C long (low $776.05–$776.25, close $776.15–$776.35, ≥ 1.0× ≈ 65k, QQQ above its VWAP; stop $775.70; target $777.49).

**Setup check (1:13 PM ET): nothing fired; the 1:00 pop ran without us**
- Replay of the C long:
  - 12:55 bar matched on price (low $776.21, close $776.35) but had 33k (≈ 0.5×). Not fired.
  - 1:00 bar: low $776.12, then a spike to $777.20 on 218k (≈ 3×), closing $776.63, above the close band.
  - 1:05: no retest.
- SPY $777.25 (high $777.39) is now just under **S1 $777.49 / Tuesday's low $777.96**, the resistance band from this morning's brief. QQQ $757.23 is at a new high.
- A long here fails reward/risk (S1 is $0.24 away). A fade short would be counter-trend. No arms this check.

**Setup check (1:28 PM ET): nothing armed or open**
- SPY $777.61 has pushed through S1 $777.49. Tuesday's low $777.96 is the next resistance, $0.35 away. The day's move from the 10:50 low is +$4.1 ($773.61 → $777.70) in about 2.5 hours, a quiet trend up led by QQQ ($757.28, new highs).
- No long has room (Tuesday's low is $0.35 above, then the pivot $779.56). A short is counter-trend. No arms.

**Setup check (1:43 PM ET): nothing fired; SPY stalling under Tuesday's low**
- Replay: nothing was armed at 1:28.
- SPY $777.28 is in a tight $777.16–$777.70 range since 1:15 on thin volume (44k–120k, avg ≈ 83k). It is still under Tuesday's low $777.96 and about $2 above VWAP (≈ $775.5). QQQ $757.00 is flat at its highs, above its VWAP.
- 4H candle: the 1:30 candle opened at $777.31, so it is in its opening (accumulation) phase. Squeeze range edges (F): $777.70 / $777.16.
- An F long over $777.70 runs into $777.96 ($0.26 of room), which fails reward/risk. A short is counter-trend.
- ARMED (valid until 1:57): **E long, reclaim of Tuesday's low.** All of these must hold:
  - a 5-min close at $777.96–$778.06;
  - volume ≥ 1.5× (≈ 125k);
  - QQQ above its VWAP.
  - Stop $777.56. Target the pivot $779.56, the nearest level (reward/risk ≈ 3.5). If it fires, the contract is picked from live quotes on the next check.

**Setup check (1:58 PM ET): nothing fired; very quiet range**
- Replay of the E long from 1:43: did not fire. The highest close was $777.44, and the 1:45 high of $777.74 stayed under $777.96.
- SPY $777.21 has held $777.01–$777.74 since 1:15 ($0.73 wide) on very thin volume (12k–46k, 10-bar avg ≈ 61k). QQQ $756.63 eased but is still above its VWAP.
- 4H candle (12–4 PM): opened at $776.34, high $777.74, low $776.12. It is in its expansion phase, pushing up. There is no sweep for setup D.
- Squeeze range edges (F): $777.74 / $777.01.
- An F long has no room under $777.96. An F short toward VWAP (≈ $775.5) is counter-trend while QQQ is above its VWAP. Not armed.
- ARMED (valid until 2:12): **the same E long.** All of these must hold:
  - a 5-min close at $777.96–$778.06;
  - volume ≥ 1.5× (≈ 91k);
  - QQQ above its VWAP.
  - Stop $777.56. Target the pivot $779.56.

**Setup check (2:13 PM ET): skipped, no data**
- Bar requests failed three times on a tool permission-check error, and the journal commit failed too. This entry was written at 2:28.

**Setup check (2:28 PM ET): nothing fired; last check before the 2:30 0DTE cutoff**
- Replay of the E long armed at 1:58 (valid until 2:12): did not fire. Closes from 1:55 to 2:10 topped out at $777.48, and the 2:05 high of $777.78 stayed under $777.96.
- SPY $777.45 is still in a $776.92–$777.78 range since 1:15 (about $0.86 wide) on 70k–90k volume. QQQ $757.38 is above its VWAP, near its highs.
- 4H candle (12–4 PM): expansion phase, pushing up (high $777.78, low $776.12). No setup D.
- Squeeze range edges (F): $777.78 / $776.92. There is no fresh close through either edge, VWAP (≈ $775.5), or a strong level.
- No A or B setup. Arming is closed (cutoff 2:15), and no new 0DTE entries are allowed after 2:30. **No paper trades today so far.**

**Setup check (2:43 PM ET): past the 0DTE cutoff; nothing open**
- No triggers to replay and no open paper trades. SPY $777.28 is still inside the $776.92–$777.78 range. 4H (12–4 PM): expansion, still holding up. No new entries after 2:30.

**End of day (3:47 PM ET)**
- Paper trades today: **none**. No positions were open, so there was nothing to close.
- Running totals unchanged: **7 trades, 3 wins, 4 losses, +$14.57** (options +$14.50, fractional +$0.07).
- Day: gap down to $774.25–776.15. The morning chopped on a flat VWAP, swept to $773.61 at 10:50, then trended up quietly with QQQ leading (S1 $777.49 reclaimed at 1:20). The afternoon stalled under Tuesday's low ($777.96). A 2:50 spike to $779.10 on 1.09M shares (10-min bar) fully reversed, after the entry window. Last price ≈ $776.86.
- Near-miss play-forwards (not counted; the rules as written did not fire):
  - 11:15 B long: missed the close band by $0.0075. Target hit at 11:45, **+2.2R**.
  - 11:45 E long: missed the band by $0.01 and was short on volume. It would have reached S1 $777.49 at 1:20.
  - 11:55 C long: failed the volume rule. It would have been **stopped by $0.001**, so the filter saved a loss.
  - 12:55 C long: matched on price, but volume was 0.5× (needed 1.0×). Target $777.49 hit at 1:20 with no stop touch, **+1.75R**.
  - Net, the filters that blocked these cost about +3.95R today and saved −1R. This goes to Friday's review with the band and volume proposals.
- Missed: +$3.0 (10:50–11:50); see missed-moves.md.

### 2026-10-08 (Thu)

**Pre-market brief (8:55 AM ET)**
- SPY pre-market $774.07 (8:40 bar; gap down ≈ $3.15 / −0.4% vs Wednesday's $777.22 close). QQQ $752.72, also weaker. The quote tool was denied by a permission check, so prices come from extended-hours bars.
- Wednesday: high $779.10, low $773.61, close $777.22.
- Pivots: R2 $782.14, **R1 $779.68**, **P $776.64**, **S1 $774.19**, S2 $771.15.
- 20/50-day SMA (computed from daily closes): ≈ $766.5 / $765.9, both below price, so the daily uptrend is intact.
- Strong levels: **$773.6–774.2** (Wednesday's low/sweep and S1, where SPY is sitting now), **$776.6** (pivot and Wednesday's afternoon range), $777.96 (Tuesday's low, capped Wednesday), $779.1–779.7 (Wednesday's high and R1), $771.15 (S2).
- News: Alpha Vantage was rate-limited again, so news is unverified. Thursday 8:30 jobless claims are already out. Treat 10:00 AM and 2:00 PM as possible event times.
- Gap < $4: normal ORB rules.
- **Bias: none at the open, bearish below $773.6.** A hold below Wednesday's low opens S2 $771.15. A reclaim of the pivot $776.64 turns it bullish (with the daily trend). Watch for a sweep of $773.6 and a reclaim (setup D shape, like Wednesday 10:50).
- **New rules in effect today** (playbook, 10/8): E/F volume ≥ 1.0× (or ≥ 0.7× with a same-bar QQQ break); first target +1.5R on SPY or +50% on the option; B pullbacks have no VWAP close cap (reward/risk ≥ 1.5 at the actual close).

**Setup check (9:43 AM ET): opening range forming**
- SPY opened $774.85 (gap down $2.37). The range so far is **$774.49–775.33**; the 9:40 bar is still open. Volume: 674k, then 163k. SPY $774.96. QQQ $753.97 dipped back after a $754.95 high.
- The opening range sits between S1 $774.19 (and Wednesday's low $773.61) below and the pivot $776.64 above.
- A short off the range low has no room: S1 is $0.30 under it, so reward/risk is < 1.5. Not armed. Watch for a sweep of $773.6–774.2 and a reclaim (setup D).

ARMED (9:45–10:12; uses the final 9:30–9:45 range):
- ARMED A long (ORB): trigger = 5-min close above the range high (now $775.33), no more than $0.10 above it, on ≥ 1.0× the opening-range average bar volume, QQQ above its VWAP; entry = trigger close; stop = range low − $0.10 (now $774.39); target = entry + 1.5R (≈ $776.75 at the current range, at or just past the pivot $776.64, so cap the target at the pivot and require reward/risk ≥ 1.5 there, or skip); option = nearest-the-money 0DTE call ≤ $25; valid until 10:12.
- Correction (9:44): at the current range the A long fails its own check. Entry ≈ $775.40, stop $774.39 (risk $1.01), and the pivot $776.64 is only $1.24 away (reward/risk 1.23). **It fires only if the final range is narrower** (range low ≥ $774.65 or so). Otherwise nothing is armed for 9:45–10:12; the next check reassesses.

**Setup check (9:58 AM ET): nothing fired; SPY chopping on VWAP, QQQ weakening**
- Final opening range: **$774.45–775.33**. The range low is below $774.65, so the A long stayed disqualified (reward/risk 1.2 to the pivot).
  - Replay for the record: the 9:45 bar closed $775.43 (inside the band). But it had 146k against the opening-range average of 336k (0.43×), and QQQ was below its VWAP. It would not have fired anyway.
- SPY $774.93 sits on a flat VWAP (≈ $775.0). The 9:50 push to $775.74 failed. QQQ $752.42 has made a new low below its opening range ($753.11), with SPY not following yet.
- Score card: factor 1 (VWAP side and slope) ❌, flat and chopping. No A or B setup. 4H (8 AM–12 PM): its accumulation phase is forming, with Wednesday's low $773.61 as the sweep level to watch. No squeeze range yet.

ARMED (valid until 10:12; prior 5-bar average ≈ 261k; the 10:00 bar may carry data):
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 261k), or ≥ 0.7× (≈ 183k) if QQQ closes below $753.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle's high + $0.10, capped at $774.20 (S1); target = entry − 1.5R (S2 $771.15 is the room check); option = nearest-the-money 0DTE put ≤ $25; valid until 10:12. ADX can't be checked (indicator tool down); noted as unverified.

**Setup check (10:17 AM ET): nothing fired; SPY turning up**
- Replay: the E short did not fire. The lowest bar since 9:55 was $774.86, and Wednesday's low $773.61 was never tested.
- SPY $775.86 has made four higher lows ($774.86 → 775.14 → 775.47 → 775.68) and is now above a VWAP turning up (≈ $775.15) and above the opening-range high $775.33 (cleared at 10:00 on 111k, below average). QQQ $754.43 recovered back above its VWAP.
- Score card: factor 1 is just turning ✅ (above VWAP, slope turning up). ADX can't be checked (tool down). The pivot $776.64 is $0.78 overhead. No A or B grade at this check: a chase entry here has < 1.5R to the pivot.
- 4H (8 AM–12 PM): opened ≈ $774 pre-market, low $774.45, no sweep of $773.61. It is moving into expansion up. No squeeze range (F) yet.

ARMED (valid until 10:27; prior 10-bar average ≈ 195k, inflated by the opening bar):
- ARMED B long (VWAP pullback): trigger = 5-min bar with low within $0.10 of VWAP (≈ $775.15–775.30) that closes above VWAP and above the prior close, QQQ above its VWAP; entry = trigger close (no close cap); stop = min(bar low, VWAP) − $0.30; target = entry + 1.5R, fired only if that is ≤ the pivot $776.64; option = nearest-the-money 0DTE call ≤ $25; valid until 10:27.
- ARMED E long (pivot break): trigger = 5-min close **$776.64–776.74** on ≥ 1.0× (≈ 195k), or ≥ 0.7× (≈ 137k) if QQQ closes above $754.95 (its day high) on the same bar; QQQ above its VWAP; entry = trigger close; stop = $776.24; target = entry + 1.5R (≈ $777.35, under Tuesday's low $777.96); option = nearest-the-money 0DTE call ≤ $25; valid until 10:27.

**Setup check (10:28 AM ET): nothing fired; SPY grinding toward the pivot**
- Replay: the B long did not fire (lows $775.71 and $775.90, never back to VWAP ≈ $775.3). The E long did not fire (highest close $776.14, under $776.64).
- SPY $776.14, with the 10:20 bar on 247k (1.7×), is $0.50 under the pivot $776.64. QQQ $756.01 is at a new day high, leading.
- Still no entry with ≥ 1.5R of room to the pivot. 4H (8 AM–12 PM): expansion up. No squeeze range.

ARMED (valid until 10:42; prior 10-bar average ≈ 144k):
- ARMED E long (pivot break): trigger = 5-min close **$776.64–776.74** on ≥ 1.0× (≈ 144k), or ≥ 0.7× (≈ 101k) if QQQ closes above $756.02 on the same bar; QQQ above its VWAP; entry = trigger close; stop = $776.24; target = entry + 1.5R (≈ $777.35, under Tuesday's low $777.96); option = nearest-the-money 0DTE call ≤ $25; valid until 10:42.
- ARMED B long (VWAP pullback): trigger = 5-min bar with low within $0.10 of VWAP (≈ $775.3–775.4) closing above VWAP and above the prior close, QQQ above its VWAP; entry = trigger close; stop = min(bar low, VWAP) − $0.30; target = entry + 1.5R, fired only if that is ≤ $776.64; option = nearest-the-money 0DTE call ≤ $25; valid until 10:42.

**Setup check (10:43 AM ET): nothing fired; stalling just under the pivot**
- Replay: E long did not fire (high $776.555, never closed ≥ $776.64). B long did not fire (lowest $775.94, VWAP ≈ $775.5).
- SPY $776.16 has been capped at $776.55 three bars in a row. QQQ $755.99 is off its $757.18 high but still above its VWAP.
- 4H (8 AM–12 PM): expansion up, stalling at the pivot. No squeeze range yet (the range since 10:05 is $775.47–776.55).

ARMED (valid until 10:57; prior 10-bar average ≈ 137k):
- ARMED E long (pivot break): trigger = 5-min close **$776.64–776.74** on ≥ 1.0× (≈ 137k), or ≥ 0.7× (≈ 96k) if QQQ closes above $757.18 on the same bar; QQQ above its VWAP; entry = trigger close; stop = $776.24; target = entry + 1.5R (≈ $777.35); option = nearest-the-money 0DTE call ≤ $25; valid until 10:57.
- ARMED B long (VWAP pullback): trigger = 5-min bar with low within $0.10 of VWAP (≈ $775.4–775.6) closing above VWAP and above the prior close, QQQ above its VWAP; entry = trigger close; stop = min(bar low, VWAP) − $0.30; target = entry + 1.5R, only if ≤ $776.64; option = nearest-the-money 0DTE call ≤ $25; valid until 10:57.

**Setup check (10:58 AM ET): nothing fired; rejected at the pivot, back to VWAP**
- Replay (VWAP computed from bars):
  - B long, 10:45 bar: low $775.60 within $0.10 of VWAP ($775.50) and close $775.605 above VWAP, **but below the prior close ($775.92). Not fired.**
  - B long, 10:50 bar: low $774.82, $0.67 under VWAP; closed below it. Not fired.
  - E long: no close ≥ $776.64 (the pivot capped it at $776.555).
  - Play-forward of the 10:45 near-miss: the 10:50 low $774.82 would have stopped it (stop $775.20). The rule saved a loss.
- SPY $775.04 is back under VWAP ($775.49); QQQ $754.44 is falling. Factor 1 is ❌ again, so it is a chop day so far: rejected at the pivot twice.
- 4H (8 AM–12 PM): expansion up failed at the pivot. A wick top is forming.
- Squeeze range (F) since 9:55: **$774.82–776.555** ($1.74 wide, ~60 min).
- A short under $774.82 has < 1.5R of room to S1 $774.19 / the opening-range low $774.45. Not armed.

ARMED (valid until 11:12; prior 10-bar average ≈ 134k):
- ARMED E/F long (pivot and range-top break): trigger = 5-min close **$776.64–776.74** on ≥ 1.0× (≈ 134k), or ≥ 0.7× (≈ 94k) if QQQ closes above $757.18 on the same bar; QQQ above its VWAP; entry = trigger close; stop = $776.24; target = entry + 1.5R (≈ $777.35); option = nearest-the-money 0DTE call ≤ $25; valid until 11:12.

**Setup check (11:15 AM ET): nothing fired; range broke down into support**
- Replay: the E/F long did not fire (highest close $775.35).
- **11:10 bar closed $774.48, below the squeeze range low $774.82**, on 118k = 0.90× the prior 10-bar average (≈ 131k). QQQ closed $753.68 below its own 45-min low ($753.88) on the same bar, so under the new volume rule (≥ 0.7× with a QQQ break) **the F short's volume test passes**. It was not armed: the 10:58 check rejected it for room.
- Live F check now: entry $774.48 (within $0.75 of the edge); stop = the closer of the range midpoint ($775.69) and the breakout candle's high + $0.10 ($775.23), so $775.23 (risk $0.75). The 1.5R target is $773.36. But the opening-range low $774.45, S1 $774.19 and Wednesday's low $773.61 all sit before it, and the first strong level (S1) is only 0.4R away. **No trade (no room).** Score: factor 1 (below a flat VWAP ≈ $775.4) ✅ weak; the support cluster ❌.
- 4H (8 AM–12 PM): wick top at the pivot, now driving down. If $773.6 is swept and reclaimed into the 12:00 candle, that is a setup D shape.

ARMED (valid until 11:27; prior 10-bar average ≈ 131k):
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 131k), or ≥ 0.7× (≈ 92k) if QQQ closes below its day low $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R (room to S2 $771.15); option = nearest-the-money 0DTE put ≤ $25; valid until 11:27.

**Setup check (11:28 AM ET): nothing fired; holding on S1**
- Replay: the E short did not fire. The lowest bar was $774.26, so Wednesday's low $773.61 was never reached.
- SPY $774.40 is sitting on S1 $774.19 / the opening-range low $774.45. The 11:15 bar traded 221k (1.7×) without breaking S1, so buyers are absorbing. QQQ $753.90 is flat, below its VWAP.
- 4H (8 AM–12 PM): distribution down from the pivot wick. A sweep of $773.6 and a reclaim would be the setup D shape into the 12:00 candle. No squeeze range (the 9:55–11:05 range broke at 11:10).

ARMED (valid until 11:42; prior 10-bar average ≈ 130k):
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 130k), or ≥ 0.7× (≈ 91k) if QQQ closes below $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $25; valid until 11:42.

**Setup check (11:43 AM ET): nothing fired; pinned on S1**
- Replay: E short did not fire (lowest $774.18, $0.01 under S1; Wednesday's low $773.61 was not reached).
- SPY $774.28 has held $774.18–774.83 since 11:15. QQQ $753.05 is sliding toward its day low $752.11, below its VWAP.
- 4H (8 AM–12 PM): distribution leg; the candle closes at 12:00. Squeeze (F): $774.18–774.83 is forming (35 min, not yet 45).

ARMED (valid until 11:57; prior 10-bar average ≈ 110k):
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 110k), or ≥ 0.7× (≈ 77k) if QQQ closes below $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $25; valid until 11:57.

**Setup check (11:58 AM ET): nothing fired; tight squeeze on S1**
- Replay: E short did not fire (lowest $774.20).
- **Squeeze range (F): $774.18–774.83** ($0.65 wide, 45 min since 11:15), sitting on S1 $774.19 under a VWAP of ≈ $775.4. QQQ $752.84 is near its day low ($752.11), below its VWAP.
- 4H: the 8 AM–12 PM candle closes as a distribution bar (top at the pivot, close near the low). The 12–4 PM candle opens next; a sweep of $773.6 and a reclaim would be setup D.
- An F long over $774.83 fails reward/risk (stop at the range midpoint − $0.10 ≈ $774.40, and VWAP ≈ $775.4 caps it). Not armed.

ARMED (valid until 12:12; prior 10-bar average ≈ 108k):
- ARMED F short (squeeze break): trigger = 5-min close **$774.08–774.18** on ≥ 1.0× (≈ 108k), or ≥ 0.7× (≈ 76k) if QQQ closes below $752.83 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of the range midpoint + $0.10 ($774.61) and the trigger candle high + $0.10; target = entry − 1.5R, **fired only if that target is at or above Wednesday's low $773.61** (room check); option = nearest-the-money 0DTE put ≤ $25; valid until 12:12.
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 108k), or ≥ 0.7× if QQQ closes below $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R; valid until 12:12.

**Setup check (12:13 PM ET): nothing fired; lunch squeeze, volume drying up**
- Replay: F short did not fire (lowest close $774.29; the 11:55 low $774.15 poked $0.03 under the range but closed back inside). E short did not fire (no trade near $773.61).
- SPY $774.62. Range since 11:15 is **$774.15–774.83** (60 min, $0.68 wide). Volume is 36k–59k, under half the morning's. QQQ $753.04 bounced off $752.29, just above its day low, and is still below its VWAP.
- 4H (12–4 PM): just opened ≈ $774.3. The 8 AM–12 PM candle closed as distribution. A sweep of $773.6 and a reclaim this afternoon would be setup D.

ARMED (valid until 12:27; prior 10-bar average ≈ 80k):
- ARMED F short (squeeze break): trigger = 5-min close **$774.05–774.15** on ≥ 1.0× (≈ 80k), or ≥ 0.7× (≈ 56k) if QQQ closes below $752.29 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of the range midpoint + $0.10 ($774.59) and the trigger candle high + $0.10; target = entry − 1.5R, only if ≥ $773.61; option = nearest-the-money 0DTE put ≤ $25; valid until 12:27.
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 80k), or ≥ 0.7× if QQQ closes below $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R; valid until 12:27.

**Setup check (12:28 PM ET): nothing fired; the squeeze broke UP on a spike**
- Replay: neither short fired (no close ≤ $774.15).
- **12:15 bar: spike from $774.62 to $777.09 on 477k (≈ 6×), closing $775.42.** It broke the $774.15–774.83 squeeze to the upside; QQQ spiked to $755.55 with it. The long side was not armed (10:58 and 11:58 checks: VWAP ≈ $775.4 capped the room). The big upper wick ($1.67) shows sellers at $777. The cause was not checked (news feed down).
- SPY $775.79 is above VWAP (≈ $775.45). QQQ $754.34 is around its VWAP.
- Live F long: price is $0.96 past the range edge, more than the $0.75 no-chase limit. Wait for a pullback that holds. No entry now.
- 4H (12–4 PM): opened ≈ $774.3 and spiked up. The candle is in its expansion phase; no setup D sweep.

ARMED (valid until 12:42; the prior 10-bar average ≈ 113k includes the spike bar):
- ARMED B long (VWAP hold after breakout): trigger = 5-min bar with low within $0.10 of VWAP (≈ $775.35–775.55) closing above VWAP and above the prior close, QQQ above its VWAP; entry = trigger close; stop = min(bar low, VWAP) − $0.30; target = entry + 1.5R, only if ≤ the pivot $776.64; option = nearest-the-money 0DTE call ≤ $25; valid until 12:42.
- ARMED F long (range-edge retest): trigger = 5-min bar with low $774.83–775.10 closing ≥ $775.00 and above the prior close, QQQ above its VWAP; entry = trigger close; stop = $774.39 (range midpoint − $0.10); target = entry + 1.5R (≤ $776.64 or skip); valid until 12:42.

**Setup check (12:43 PM ET): nothing fired; spike fully faded**
- Replay (VWAP ≈ $775.47):
  - B long: the 12:25 bar touched VWAP (low $775.37) but closed $775.44, under VWAP and the prior close. 12:30 low $775.28 was outside the band. 12:35 closed under VWAP. Not fired.
  - F long: the 12:35 low $774.78 went under the $774.83 band, and it closed $774.975 < $775.00. Not fired.
- SPY $774.98 has given back the whole 12:15 spike and sits under VWAP. QQQ $753.51 is under its VWAP. The trap shape (failed breakout) points to chop or a fade. Score: factor 1 ❌ (VWAP flat, price chopping across it).
- 4H (12–4 PM): a long upper wick to $777.09 with the body back near the open. Distribution-looking, no sweep. No squeeze range (the spike widened it to $2.94).

ARMED (valid until 12:57; prior 10-bar average ≈ 112k, inflated by the spike):
- ARMED E short (Wednesday's-low break): trigger = 5-min close **$773.51–773.61** on ≥ 1.0× (≈ 112k), or ≥ 0.7× (≈ 78k) if QQQ closes below $752.11 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10, capped at $774.20; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $25; valid until 12:57.

**Setup check (12:58 PM ET): selloff blew through Wednesday's low; armed short missed its band**
- Replay of the E short (band $773.51–773.61): **the 12:45 bar closed $773.255** on 263k (≈ 2.4×, QQQ below its VWAP). That is $0.255 past the band, a gap-through, so **not fired.** The 12:50 bar closed $773.10, also outside the band.
  - Play-forward for the record (not counted): entry $773.255, stop $774.20 (cap), risk $0.945, 1.5R target $771.84. Low so far $772.485, open.
- **The move: $775.51 (12:40 high) → $772.485 (12:50 low) = −$3.0 in 15 min**, led by QQQ (−$5.8, $753.96 → $748.19, 888k on the 12:50 bar). The cause was not checked (news feed down). Missed-move candidate.
- Live E check: the 12:50 bar held below the level (E entry rule), but the stop beyond the breakout candle's high ($775.10) is $2.00 away, and S2 $771.15 is only 1R. **No trade (reward/risk).** Score: factor 1 ❌ (VWAP ≈ $775.3 is still flat).
- 4H (12–4 PM): the $777.09 wick top, then a sweep below Wednesday's low. Expansion down. A reclaim of $773.61 would be a setup D long shape.

ARMED (valid until 13:12; prior 10-bar average ≈ 179k):
- ARMED C short (retest of $773.61 from below): trigger = 5-min bar with high $773.51–773.81 that closes below $773.61 and below the prior close, on ≥ 1.0× (≈ 179k) or ≥ 0.7× if QQQ makes a new low on the same bar; QQQ below its VWAP; entry = trigger close; stop = the farther of $773.91 (level + $0.30) and bar high + $0.15; target = entry − 1.5R (room to S2 $771.15); option = nearest-the-money 0DTE put ≤ $25; valid until 13:12.

**Setup check (1:13 PM ET): nothing fired, missed by a rule detail; selloff extending**
- Replay of the C short: the 12:55 bar had high $773.51 (in band) and closed $773.14 (below $773.61) on 318k (1.8×) with QQQ below its VWAP. **But it closed $0.04 above the prior close ($773.10), so it did not fire.** Later bars stayed out of the band.
- Play-forwards for the record (not counted):
  - 12:55 C near-miss: entry $773.14, stop $773.91, 1.5R target $771.985 → **hit at 1:00 (low $771.93), +1.5R.**
  - 12:45 E gap-through (from the last check): entry $773.255, 1.5R target $771.84 → **hit at 1:05 (low $771.80), +1.5R.**
  - Two winners missed today on entry-wording details (a band gap-through and a "below the prior close" filter). For Friday's review.
- SPY $772.46 (low $771.80) is $0.65 above S2 $771.15. QQQ $746.96 (−$11 from its high) is driving it. VWAP ≈ $774.9 is now turning down. Score: factor 1 ✅ (below a VWAP turning down); ADX unverified.
- 4H (12–4 PM): expansion down after the $777.09 wick (Power-of-3 distribution shape). S3 ≈ $768.69.

ARMED (valid until 1:27; prior 10-bar average ≈ 210k):
- ARMED E short (S2 break): trigger = 5-min close **$771.05–771.15** on ≥ 1.0× (≈ 210k), or ≥ 0.7× (≈ 147k) if QQQ closes at a new day low on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10 (max risk $1.00 or skip); target = entry − 1.5R (room to S3 ≈ $768.69); option = nearest-the-money 0DTE put ≤ $25; valid until 1:27.
- ARMED C short (retest of $773.61 from below): trigger = 5-min bar with high $773.51–773.81 closing below $773.61, on ≥ 1.0× (≈ 210k) or ≥ 0.7× with a QQQ new low; QQQ below its VWAP; entry = trigger close; stop = the farther of $773.91 and bar high + $0.15; target = entry − 1.5R; valid until 1:27. (The "below the prior close" condition is dropped: it is not in setup C's playbook text.)

**Setup check (1:28 PM ET): nothing fired; grinding toward S2**
- Replay: E short (S2) did not fire (lowest close $771.83). C short did not fire (bounce highs $773.34 and $773.47 stayed under the $773.51 band).
- SPY $771.83 (low $771.64) is making lower highs ($773.47) under a falling VWAP. QQQ $745.46 is at a new day low. Day range $777.09 → $771.64.
- 4H (12–4 PM): expansion down continues. No squeeze.

ARMED (valid until 1:42; prior 10-bar average ≈ 250k):
- ARMED E short (S2 break): trigger = 5-min close **$771.05–771.15** on ≥ 1.0× (≈ 250k), or ≥ 0.7× (≈ 175k) if QQQ closes at a new day low on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10 (skip if risk > $1.00); target = entry − 1.5R (room to S3 ≈ $768.69); option = nearest-the-money 0DTE put ≤ $25; valid until 1:42.

**Setup check (1:43 PM ET): armed E short FIRED at 1:25 and was stopped at 1:30 (armed, replayed)**
- Trigger: the 1:25 bar closed **$771.08** (band $771.05–771.15) on 339k = 1.39× the prior 10-bar average (244k); QQQ $744.39 was far below its VWAP. Fired as written.
- Score card (B, as armed): 1 VWAP side/slope ✅ (below, turning down) · 2 ADX > 20 ⚠️ unverified (indicator tool down) · 3 level break (S2) ✅ · 4 volume ≥ 1.0× ✅ · 5 QQQ agrees ✅ · 6 4H expansion down ✅ · 7 room to S3 ≈ $768.69 ✅ · 8 not chasing (in band) ✅ · 9 trend-day check: no (morning chop) ❌ · 10 time (before 2:30) ✅. Graded B (≈ 7) with the ADX caveat.
- Plan: SPY entry $771.08, stop $772.00 (candle high $771.90 + $0.10; risk $0.92), target $769.70 (−1.5R).
- **Result: the 1:30 bar ran to $772.03 → stopped.** Its low was $770.87; the target was never close. SPY then bounced to $772.55.
  - **0DTE leg: SPY 10/8 767P** (nearest-the-money put ≤ $25; the 771P at $1.13 and 768P at $0.32 were over the cap). Entry $0.22 (bar close $0.21 + half spread), exit $0.12 on the invalidation stop → **−$10 (−45%).**
  - **Fractional leg: SH** 7.79 sh (≈ $250, 50% cap) at $32.08, exit $32.045 when the SPY stop hit → **−$0.27.**
- Lesson: an S2 break after a −$5.5 leg on climax volume (QQQ 783k) = a capitulation bar; the next bar reversed. Note for Friday: E breaks late in an extended move (> 2× ATR from VWAP) may need a "no climax bar" filter. No rule change now.
- Running totals: **9 trades, 3 wins, 6 losses, +$4.30.** Daily loss so far: −$10.27 (well under the $50 daily limit).
- SPY $772.55, QQQ $746.64 bouncing. No revenge entry. ARMED (valid until 1:57): none. One loss today; next check reassesses with fresh structure.

**Setup check (1:58 PM ET): nothing armed, no open trades; chop after the flush**
- SPY $771.67 has been in $770.44–772.83 since 1:25 (35 min, $2.39 wide), back under S2 $771.15–772 on and off. QQQ $745.55 is near its lows. VWAP ≈ $774.6 is falling.
- 4H (12–4 PM): expansion down; the bounce off $770.44 so far is shallow.
- No A/B setup now: mid-range, no fresh close through a level.

ARMED (valid until 2:12; prior 10-bar average ≈ 230k):
- ARMED E short (day-low break): trigger = 5-min close **$770.33–770.43** on ≥ 1.0× (≈ 230k), or ≥ 0.7× (≈ 161k) if QQQ closes below $743.23 on the same bar; QQQ below its VWAP; entry = trigger close; stop = trigger candle high + $0.10 (skip if risk > $1.00); target = entry − 1.5R (room to S3 ≈ $768.69); option = nearest-the-money 0DTE put ≤ $25; valid until 2:12. (Not a revenge trade: a fresh level, a new plan, and within the daily limit.)

**Setup check (2:13 PM ET): nothing fired; last arming of the day**
- Replay: the E short did not fire (lowest $771.41).
- SPY $772.02. **Squeeze range (F) since 1:25: $770.44–772.83** (50 min, $2.39 wide) under a falling VWAP (≈ $774.5). QQQ $745.86 is flat near its lows.
- An F long over $772.83 fails reward/risk (stop at the midpoint ≈ $771.64; the 1.5R target ≈ $774.6 is above VWAP). Not armed.
- 4H (12–4 PM): expansion down, now basing.

ARMED (valid until 2:27, the final window before the 2:30 cutoff; prior 10-bar average ≈ 200k):
- ARMED E/F short (day-low and squeeze-low break): trigger = 5-min close **$770.34–770.44** on ≥ 1.0× (≈ 200k), or ≥ 0.7× (≈ 140k) if QQQ closes below $743.23 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of the trigger candle high + $0.10 and the range midpoint + $0.10 ($771.74) (skip if risk > $1.00); target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $25; valid until 2:27.

**Setup check (2:28 PM ET): nothing fired; squeeze broke up instead**
- Replay: the E/F short did not fire (no close under $771.95).
- SPY broke the $772.83 range top at 2:15 (close $773.19, 188k ≈ 0.9×, QQQ breaking up too) and is at $773.45, back near Wednesday's low $773.61. The long side was not armed: reward/risk failed under VWAP ≈ $774.4.
- 0DTE cutoff 2:30: no new entries. No open paper trades. Remaining checks report only; EOD at 3:47.

**Setup check (2:43 PM ET):** past the 2:30 0DTE cutoff; nothing armed, no open paper trades. Report only; EOD at 3:47.

**End of day (3:47 PM ET)**
- Paper trades today: **1 setup (E short, S2 break, armed, replayed), two legs, both stopped:** SPY 767P −$10 (−45%), SH fractional −$0.27. No positions open overnight.
- Running totals: **9 trades, 3 wins, 6 losses, +$4.30** (options +$4.50, fractional −$0.20). Daily loss −$10.27 (limit $50).
- Day: gap down, then morning chop on a flat VWAP (rejected twice at the pivot $776.64). Lunch squeeze on S1, a 12:15 spike to $777.09 that fully faded, then a **−$5.1 selloff 12:40–1:25** ($775.51 → $770.44) led by QQQ (−$13, $757.18 → $743.23). Afternoon base $770.4–773.9. Last ≈ $773.3 (−$3.9 vs Wednesday).
- Rule notes for Friday:
  - Three short entries today missed winners on wording: the 12:45 band gap-through (+1.5R), and the 12:55 "below the prior close" filter (+1.5R; that filter was my addition, not playbook text).
  - The one that did fire (1:25) was a climax bar and reversed.
- Missed: −$5.1 (12:40–1:25); see missed-moves.md.

### 2026-10-09 (Fri)

**Pre-market brief (8:55 AM ET)**
- SPY pre-market $776.33 (8:40 bar; gap up ≈ $2.40 / +0.3% vs Thursday's $773.93 close), fading from $777.78. QQQ $752.51 is softer.
- Thursday: high $777.09, low $770.44, close $773.93.
- Pivots: R2 $780.47, **R1 $777.20**, **P $773.82**, **S1 $770.55**, S2 $767.16.
- 20/50-day SMA ≈ $767 / $766 (from daily closes), so the daily uptrend is intact.
- Strong levels: **$777.1–777.96** (R1, Thursday's spike high, Tuesday's low), **$773.6–773.9** (pivot, Wednesday's low, Thursday's close), $770.4–770.6 (Thursday's low and S1), $779.1 (Wednesday's high).
- News and calendar: not checked (Alpha Vantage rate-limited). Treat 10:00 AM as a possible data time.
- Gap < $4: normal ORB rules.
- **Bias: none.** The gap opens into R1 resistance after Thursday's −$5 selloff. Bullish only on acceptance above $777.96; bearish below the pivot $773.8.
- Today is Friday: weekly review at EOD (backtest and option-replay findings, the F-only proposal, graduation check). The playbook is unchanged until the owner OKs the F-only proposal.

**Setup check (9:43 AM ET): opening range forming**
- SPY opened $776.24. The range so far is **$775.88–776.84** (9:40 bar still open); first bars 256k and 169k. SPY $776.65 is holding. **QQQ is weak** ($751.57, new lows at $750.20), so the two diverge.
- An ORB long has no room: R1 $777.20 is $0.36 above the range high. Not armed.
- An ORB short has room to the pivot $773.82 (about 1.8R at the current range).

ARMED (9:45–10:12; uses the final 9:30–9:45 range):
- ARMED A short (ORB): trigger = 5-min close below the range low (now $775.88), no more than $0.10 below it, on ≥ 1.0× the opening-range average bar volume, SPY below its VWAP, QQQ below its VWAP; entry = trigger close; stop = range high + $0.10 (now $776.94); target = entry − 1.5R (≈ $774.2), only if the pivot $773.82 leaves ≥ 1.5R; option = nearest-the-money 0DTE put ≤ $100 (new $1,000 cap); valid until 10:12.

**Setup check (9:58 AM ET): nothing fired**
- Final opening range: **$775.35–776.84** ($1.49 wide). The A short had to close $775.25–775.35. Closes were $775.78 and $775.735 → **not fired.** Its stop would be $776.94 (risk $1.64, over the $1.50 max), and the pivot $773.82 is only 0.9R away, so it would have been skipped anyway.
- SPY $775.74 sits on a flat VWAP (≈ $775.9). **QQQ is selling hard** ($748.78, −$3.8 from the open) while SPY holds, a divergence. Score: factor 1 ❌ (flat, chopping). No A or B setup.
- 4H (8 AM–12 PM): opened ≈ $777 pre-market, fading. No squeeze yet.

ARMED (valid until 10:12):
- ARMED B short (VWAP rejection): trigger = 5-min bar whose high comes within $0.10 of VWAP and closes below VWAP and below the prior close, after 3 closes below VWAP, QQQ below its VWAP; entry = trigger close; stop = max(bar high, VWAP) + $0.30; target = entry − 1.5R, only if the pivot $773.82 leaves ≥ 1.5R; option = nearest-the-money 0DTE put ≤ $100; valid until 10:12.

**Setup check (10:22 AM ET): nothing fired; chop**
- Replay: the B short did not fire. The 9:55 bar closed $776.06, above VWAP (≈ $775.95), and after that the "3 closes below VWAP" condition no longer held.
- SPY $776.42 is back above a flat VWAP, inside $775.14–776.84 since 9:40. QQQ $749.66 is flat at its lows. SPY/QQQ divergence; factor 1 ❌.
- 4H (8 AM–12 PM): sideways. Squeeze forming: $775.14–776.84 ($1.70, about 45 min); F is valid from 11:00.
- ARMED (until 10:42): none. A long over $776.84 has no room to R1 $777.20, and a short has no strong break level inside the range.

**Setup check (10:28 AM ET): nothing armed, nothing open.** SPY $776.62 is drifting up inside $775.14–776.84 under R1 $777.20. QQQ $749.69 is flat at its lows. No A/B setup; no arms (same reasons as 10:22).

**Setup check (10:43 AM ET): nothing armed, nothing open.** SPY $776.35 has held $775.14–776.84 for ~1 hour ($1.70 wide), the squeeze range for F (valid from 11:00). QQQ $749.82 is just off its lows. 4H (8 AM–12 PM): range-bound. The F short under $775.14 has room to the pivot $773.82 and will be armed at the 10:57 check (for bars from 11:00). An F long over $776.84 has no room to R1 $777.20.

**Setup check (10:58 AM ET): range broke UP at 10:50; no entry (before the F window, outside the band)**
- No triggers were armed. The 10:50 bar closed **$777.08**, above the $776.84 range top, on 162k (≈ 1.6×), with QQQ turning up ($750.50, back above its VWAP).
  - F starts at 11:00, so F does not apply. As an E break of $776.84 the close was $0.24 past (band $0.10), and R1 $777.20 is just overhead. Not a trade.
- SPY $777.08 sits under R1 $777.20 / Tuesday's low $777.96 (resistance band). Above it: Wednesday's high $779.10, then R2 $780.47.
- 4H (8 AM–12 PM): breaking up out of the morning range. The F short line is dropped (the range broke the other way).

ARMED (valid until 11:12; prior 10-bar average ≈ 100k):
- ARMED E long (R1 break): trigger = 5-min close **$777.20–777.30** on ≥ 1.0× (≈ 100k), or ≥ 0.7× if QQQ closes above $750.57 on the same bar; QQQ above its VWAP; entry = trigger close; stop $776.80; target = entry + 1.5R, only if ≤ $777.96 (room check); option = nearest-the-money 0DTE call ≤ $100; valid until 11:12.
- ARMED E long (Tuesday's-low reclaim): trigger = 5-min close **$777.96–778.06** on ≥ 1.0× (≈ 100k), or ≥ 0.7× with a QQQ same-bar new high; QQQ above its VWAP; entry = trigger close; stop $777.56; target = entry + 1.5R (room to Wednesday's high $779.10); option = nearest-the-money 0DTE call ≤ $100; valid until 11:12.

**Setup check (11:18 AM ET): nothing fired; stalling at R1**
- Replay of the R1 long: the 10:55 bar closed $777.32, $0.02 over the band, on 96k (0.96×; QQQ did not make a same-bar high). Not fired, two reasons. It would have failed the room check anyway (1.5R target $778.10 > $777.96), and the 11:05 low $776.535 would have stopped it. The Tuesday's-low long: no trade near $777.96.
- SPY $777.15 is chopping at R1 ($776.54–777.57 since 10:50). QQQ $749.51 is soft again. Range since 9:40: $775.14–777.57 ($2.43, F-eligible). Its edges sit at R1 above and near the morning low below.
- 4H (8 AM–12 PM): range-bound with an upside poke.

ARMED (valid until 11:27; prior 10-bar average ≈ 105k):
- ARMED E long (Tuesday's-low reclaim): trigger = 5-min close **$777.96–778.06** on ≥ 1.0× (≈ 105k), or ≥ 0.7× with a same-bar QQQ high above $750.84; QQQ above its VWAP; entry = trigger close; stop $777.56; target = entry + 1.5R (room to $779.10); option = nearest-the-money 0DTE call ≤ $100; valid until 11:27.

**Setup check (11:28 AM ET): nothing fired**
- Replay: the Tuesday's-low long did not fire (high $777.80, highest close $777.61, under $777.96).
- SPY $777.48 is grinding up under $777.96 on ≈ 1.1× volume. QQQ $750.26 is recovering toward its VWAP. Range since 10:50: $776.54–777.80.

ARMED (valid until 11:42; prior 10-bar average ≈ 112k):
- ARMED E long (Tuesday's-low reclaim): trigger = 5-min close **$777.96–778.06** on ≥ 1.0× (≈ 112k), or ≥ 0.7× with a same-bar QQQ high above $750.84; QQQ above its VWAP; entry = trigger close; stop $777.56; target = entry + 1.5R (room to $779.10); option = nearest-the-money 0DTE call ≤ $100; valid until 11:42.

**Setup check (11:43 AM ET): nothing fired; squeeze under R1**
- Replay: the Tuesday's-low long did not fire (highest close since 11:25 was $777.20).
- SPY $777.20. **Squeeze range (F) since 10:50: $776.54–777.80** (55 min, $1.26 wide), capped by R1 and Tuesday's low. QQQ $750.28 is around its VWAP, chopping.
- An F long over $777.80 has no room ($777.96 is $0.16 above). Not armed.

ARMED (valid until 11:57; prior 10-bar average ≈ 100k):
- ARMED F short (squeeze break): trigger = 5-min close **$776.44–776.54** on ≥ 1.0× (≈ 100k), or ≥ 0.7× if QQQ closes below $749.13 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of the range midpoint + $0.10 ($777.27) and the trigger candle high + $0.10; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $100; valid until 11:57.

**Setup check (11:58 AM ET): nothing fired; lunch squeeze tightening**
- Replay: F short did not fire (lowest close $777.19; range low $776.54 not tested).
- SPY $777.42. Squeeze since 10:50 is still **$776.54–777.80** (70 min) on fading volume (38k–68k). QQQ $750.46 is back above its VWAP.
- 4H: the 8 AM–12 PM candle closes as a doji-like range (no D). The 12–4 PM candle opens next.

ARMED (valid until 12:12; prior 10-bar average ≈ 90k):
- ARMED F short (squeeze break): trigger = 5-min close **$776.44–776.54** on ≥ 1.0× (≈ 90k), or ≥ 0.7× if QQQ closes below $749.13 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of $777.27 and the trigger candle high + $0.10; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $100; valid until 12:12.
- ARMED E long (Tuesday's-low reclaim, also the F top break): trigger = 5-min close **$777.96–778.06** on ≥ 1.0× (≈ 90k), or ≥ 0.7× with a same-bar QQQ high above $750.84; QQQ above its VWAP; entry = trigger close; stop $777.56; target = entry + 1.5R (room to $779.10); option = nearest-the-money 0DTE call ≤ $100; valid until 12:12.

**Setup check (12:13 PM ET): nothing fired; squeeze holds**
- Replay: neither line fired (closes $777.27–777.58; no close ≤ $776.54 or ≥ $777.96).
- SPY $777.58. Squeeze still **$776.54–777.80** (85 min). QQQ $750.79 is above its VWAP, pushing its highs. 4H (12–4 PM): just opened ≈ $777.4.

ARMED (valid until 12:27; prior 10-bar average ≈ 85k): the same two lines.
- E long: close **$777.96–778.06**, ≥ 1.0× (≈ 85k) or ≥ 0.7× with a same-bar QQQ high above $750.93, QQQ above its VWAP; stop $777.56; target entry + 1.5R (room to $779.10); 0DTE call ≤ $100.
- F short: close **$776.44–776.54**, ≥ 1.0× (≈ 85k) or ≥ 0.7× if QQQ closes below $749.13, QQQ below its VWAP; stop the closer of $777.27 and candle high + $0.10; target entry − 1.5R; 0DTE put ≤ $100.

**Setup check (12:28 PM ET): nothing fired; pressing Tuesday's low**
- Replay: E long did not fire. The 12:15 bar closed **$777.90** (band $777.96–778.06, $0.06 short) on 105k; the highs were $778.07 and $778.10. F short did not fire.
- SPY $777.87 is pressing $777.96–778.10 with QQQ flat ($750.55, above its VWAP). The squeeze top is now $778.10.

ARMED (valid until 12:42; prior 10-bar average ≈ 80k):
- E long: close **$778.11–778.21** (above Tuesday's low and today's high), ≥ 1.0× (≈ 80k) or ≥ 0.7× with a same-bar QQQ high above $751.08; QQQ above its VWAP; stop $777.70; target entry + 1.5R (≤ $779.10 or skip); 0DTE call ≤ $100; valid until 12:42.
- F short: close **$776.44–776.54**, same terms as before; valid until 12:42.

**Setup check (12:43 PM ET): nothing fired; coiling at Tuesday's low**
- Replay: E long did not fire (closes $777.94–777.99; the high of $778.23 never closed ≥ $778.11). F short did not fire.
- SPY $777.94 sits in a very tight $777.74–778.23 band since 12:15, just under Wednesday's high $779.10. QQQ $750.46 is flat above its VWAP. Wider squeeze since 10:50: $776.54–778.23.

ARMED (valid until 12:57; prior 10-bar average ≈ 75k):
- E/F long: close **$778.24–778.34** (above today's high), ≥ 1.0× (≈ 75k) or ≥ 0.7× with a same-bar QQQ high above $751.08; QQQ above its VWAP; stop $777.84; target entry + 1.5R (≤ $779.10 or skip); 0DTE call ≤ $100; valid until 12:57.
- F short: close **$776.44–776.54**, same terms; valid until 12:57.

**Setup check (12:58 PM ET): armed E/F long FIRED at 12:45 (armed, replayed); open**
- Trigger: the 12:45 bar closed **$778.25** (band $778.24–778.34) on 124.5k = 1.71× the prior 10-bar average (72.8k); QQQ $750.88 above its VWAP ($750.13). Fired as written. (The F short did not fire.)
- Score card (B, as armed): 1 above a rising VWAP ($776.83) ✅ · 2 ADX ⚠️ not checked · 3 close through today's high / squeeze top ✅ · 4 volume ≥ 1.0× ✅ · 5 QQQ agrees ✅ · 6 4H (12–4 PM) building up ✅ · 7 room to Wednesday's high $779.10 ≥ 1.5R ✅ · 8 in band, not chasing ✅ · 9 trend day: no (range morning) ❌ · 10 time before 2:30 ✅. Graded B.
- Plan: SPY entry $778.25, stop $777.84 (risk $0.41), target **$778.87** (+1.5R, under $779.10). Time stop 1:20 (30 min).
  - **0DTE leg: SPY 10/9 778C** (nearest the money; 779C was $0.32). Entry **$0.77** (bar close $0.75 + half spread) = $77, fits the $100 cap. Option target +50% = $1.16; option stop −45% ≈ $0.42, or the SPY stop first.
  - **Fractional leg: SPY** 0.6425 sh (≈ $500, 50% cap) at $778.25, alert-stop $777.84 (risk ≈ $0.26), target $778.87, out by 3:45.
- Since entry (12:50 bar): SPY high $778.70 (target not hit), low $778.26; 778C high $1.06 (+38%), close $0.78. Up 30% touched → option stop raised to break-even $0.77 (stops only move up).
- ARMED (valid until 1:12): none new; one position at a time. Manage the open long at the next check.

**Setup check (1:13 PM ET): option leg stopped at break-even; fractional leg open**
- Since 12:55: SPY $778.22 → $778.35 → **$778.02** (high $778.44; target $778.87 not hit; stop $777.84 not hit). QQQ $750.38, still above its VWAP.
- **0DTE leg closed:** the 778C fell to $0.70 on the 12:55 bar, hitting the break-even stop ($0.77, raised after the +38% touch). Fill $0.75 (stop less half spread) → **−$2 (−3%).** It is now $0.59.
- **Fractional leg open:** SPY 0.6425 sh at $778.25, now $778.02 (−$0.15). Alert-stop $777.84, target $778.87; time stop 1:20 (30 min with no progress) is reviewed at the next check.
- 4H (12–4 PM): small up candle ≈ $777.4 → $778.0, no D. Squeeze (F) since 10:50 is now $776.54–778.70 ($2.16).
- Running totals: **10 trades closed, 3 wins, 7 losses, +$2.30** (fractional leg pending).
- ARMED (valid until 1:27): none; one position open.

**Setup check (1:28 PM ET): fractional leg stopped; trade closed**
- The 1:15 bar traded down to $777.72, through the $777.84 alert-stop → **SPY fractional sold ≈ $777.84 → −$0.26.** SPY now $777.88; QQQ $750.42 just above its VWAP ($750.13).
- **10/9 E/F long result, both legs stopped:** 778C −$2 (break-even stop after +38%), SPY fractional −$0.26. Note for Friday: the 12:50 bar hit $778.70, $0.17 short of the +1.5R target, and the option got +38% (the +50% target needed $1.16). Same pattern as earlier this week: near-misses on the first target.
- Running totals: **11 trades closed, 3 wins, 8 losses, +$2.04.** Daily loss −$2.26 (well under the $100 limit).
- 4H (12–4 PM): up candle fading back to its open ≈ $777.4–777.9; no D. Squeeze (F) since 10:50: **$776.54–778.70** ($2.16).
- Score: no fresh close through a level; mid-range. An F long over $778.70 has no room (Wednesday's high $779.10 is $0.40 above, under 1.5R). Not armed.

ARMED (valid until 1:42; prior 10-bar average ≈ 76k):
- ARMED F short (squeeze break): trigger = 5-min close **$776.44–776.54** on ≥ 1.0× (≈ 76k), or ≥ 0.7× if QQQ closes below $749.13 on the same bar; QQQ below its VWAP; entry = trigger close; stop = the closer of the range midpoint + $0.10 ($777.72) and the trigger candle high + $0.10; target = entry − 1.5R; option = nearest-the-money 0DTE put ≤ $100; valid until 1:42. (Opposite side and a new plan, not a revenge trade.)

**Setup check (1:43 PM ET): nothing fired; quiet mid-range**
- Replay: F short did not fire (lowest close $777.88).
- SPY $778.08 in a tight $777.72–778.23 drift on light volume (27k–49k). QQQ $750.62 above its VWAP. 4H (12–4 PM): flat, no D. Squeeze (F) since 10:50: $776.54–778.70.
- No fresh close through a level; long side still capped by Wednesday's high $779.10 (no 1.5R room).

ARMED (valid until 1:57; prior 10-bar average ≈ 65k):
- ARMED F short: close **$776.44–776.54**, ≥ 1.0× (≈ 65k) or ≥ 0.7× if QQQ closes below $749.13; QQQ below its VWAP; stop the closer of $777.72 and candle high + $0.10; target entry − 1.5R; nearest-the-money 0DTE put ≤ $100; valid until 1:57.

**Setup check (1:58 PM ET): nothing fired; drifting up on thin volume**
- Replay: F short did not fire (lowest close $778.08).
- SPY $778.28 (19k–61k bars, thinnest of the day). QQQ $750.84 above its VWAP. 4H (12–4 PM): small up candle, no D. Squeeze (F) since 10:50: $776.54–778.70.
- No fresh close through a level. Long over $778.70 still lacks 1.5R room to $779.10.

ARMED (valid until 2:12; prior 10-bar average ≈ 43k):
- ARMED F short: close **$776.44–776.54**, ≥ 1.0× (≈ 43k) or ≥ 0.7× if QQQ closes below $749.13; QQQ below its VWAP; stop the closer of $777.72 and candle high + $0.10; target entry − 1.5R; nearest-the-money 0DTE put ≤ $100; valid until 2:12.

**Setup check (2:14 PM ET): nothing fired; last arming window**
- Replay: F short did not fire (lowest close $778.11).
- SPY $778.49 creeping up toward the $778.70 squeeze top on light volume (48k). QQQ $750.97 above its VWAP. 4H (12–4 PM): small up candle, no D. Squeeze (F) since 10:50: $776.54–778.70.
- No fresh close through a level. A long over $778.70 still lacks 1.5R room to Wednesday's high $779.10.

ARMED (final window; entries only on bar closes through 2:25, then no new 0DTE after 2:30; prior 10-bar average ≈ 40k):
- ARMED F short: close **$776.44–776.54**, ≥ 1.0× (≈ 40k) or ≥ 0.7× if QQQ closes below $749.13; QQQ below its VWAP; stop the closer of $777.72 and candle high + $0.10; target entry − 1.5R; nearest-the-money 0DTE put ≤ $100; valid until 2:27.

**Setup check (2:28 PM ET): nothing fired; entry window closing**
- Replay: F short did not fire (closes $778.47–778.66, nowhere near $776.54; the 2:25 bar is checked at the next check).
- SPY $778.66 pressing the squeeze top (high $778.74 vs $778.70) with QQQ at a new day high $751.66. No close through $778.70 yet; even if one comes it has no 1.5R room under Wednesday's high $779.10, and no new 0DTE after 2:30.
- No more arming today (past 2:15). Open: none.
