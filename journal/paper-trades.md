# Paper Trade Journal

Practice phase: no real money. Every A or B grade setup from
`../strategies/playbook.md` is logged here as if it had been taken, using real
quotes for the contract. Rules for graduating to real money are in
`../CLAUDE.md`.

## Scoreboard

| Closed trades | Trades | Wins | Losses | Win rate | Avg win | Avg loss | Net P&L |
|---|---|---|---|---|---|---|---|
| Options, A grade | 0 | 0 | 0 | – | – | – | $0 |
| Options, B grade | 3 | 1 | 2 | 33% | +$42 | -$20.50 | +$1 |
| Fractional, A grade | 0 | 0 | 0 | – | – | – | $0 |
| Fractional, B grade | 2 | 0 | 2 | 0% | – | -$0.12 | -$0.24 |
| **All** | 5 | 1 | 4 | 20% | +$42 | -$10.31 | +$0.76 |

Open: none.

By setup: ORB 0 · VWAP pullback 0 · Break and retest 4 · 4H manipulation 0 · Squeeze F 1

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
