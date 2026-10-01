# Trading Playbook

How TraderBot finds, scores, and manages trades. The risk and 0DTE rules in
`../CLAUDE.md` always come first: a perfect score never overrides a risk limit.
Everything here is analysis to support the owner's decisions, not investment
advice.

## 1. Daily routine (times ET)

| When | What |
|---|---|
| 8:30–9:25 | **Pre-market brief:** overnight/pre-market move, news and sentiment, today's scheduled events (CPI, jobs, FOMC, Fed speakers, big earnings), key levels (below). Set a bias: bullish, bearish, or no bias. |
| 9:30–9:45 | **Watch only.** Mark the 15-minute opening range (high and low). No entries. |
| 9:45–2:30 | **Hunt:** score setups with the confluence card. Only A-grade or B-grade setups get proposed. |
| By 3:30 | **Flat:** every 0DTE position closed. |
| After close | **Journal:** log each trade, update running totals and the day-trade count. |

## 2. Key levels (mark before the open)

- Previous day high, low, close
- Pre-market high and low
- Opening range high and low (9:30–9:45)
- Classic pivot points: P, R1, S1 (`pivot_points` indicator, daily)
- 50-day and 20-day moving averages (daily)
- Round numbers (e.g. $760, $765, $770 on SPY)

Levels that stack within about $1 of each other count as one **strong level**.

## 3. Confluence score card

Score every setup before proposing it. A factor scores a point only if it
points the **same way** as the trade.

| # | Factor | How to check | Point if (bullish example; flip for bearish) |
|---|---|---|---|
| 1 | **VWAP** (required) | `vwap`, 5-min | Price holding above VWAP, VWAP sloping up |
| 2 | **Trend strength** (required) | `adx`, 5-min, period 14 | ADX above 20 (a trending day, not chop) |
| 3 | **EMA stack** | `ema` 9 and 21, 5-min | Price > 9 EMA > 21 EMA |
| 4 | **Candle structure** | 5-min bars | Higher highs and higher lows, plus a confirming candle |
| 5 | **Key level** | Section 2 | Breaking and holding above a level, or bouncing off support; not buying straight into resistance |
| 6 | **Volume** | 5-min bars | Breakout candle volume above the average of the prior 10 bars |
| 7 | **Momentum** | `rsi` 14 and `macd`, 5-min | RSI 50–70 (not overbought) and MACD above its signal line |
| 8 | **Higher timeframe** | 15-min / hourly trend, daily vs 50-day SMA | Bigger trend points the same way |
| 9 | **Market agreement** | QQQ (and IWM) vs their own VWAP | The rest of the market moves the same way |
| 10 | **News** | Sentiment, calendar | News supports the direction; no event due before exit that could flip it |

**Grades**
- **A (8–10 points):** propose the trade at normal size (5% default).
- **B (6–7 points):** propose only as a smaller trade, or wait for one more factor.
- **C (under 6), or either required factor missing:** no trade.

Show the filled score card in every trade proposal and copy it into the
journal entry.

## 4. Setups

Setups A–C, E and F trade with the trend. Setup D trades the reversal after a
4-hour manipulation move, and only after the sweep, the reclaim, and a shift
in structure have all happened. Other "catch the reversal" trades are left out
on purpose: they lose more often, and 0DTE leaves no time to be wrong.

### A. Opening Range Breakout (ORB)
- **Setup:** after 9:45, a 5-min candle **closes** outside the opening range,
  with volume above average, on the same side of VWAP as the break.
- **Entry:** on the close of the breakout candle, or on the first retest of
  the range edge that holds.
- **Invalidation:** price closes back inside the opening range.
- **Best when:** the pre-market bias and the break point the same way.

### B. VWAP Pullback (trend continuation)
- **Setup:** a clear trend (ADX above 20, EMAs stacked). Price pulls back to
  VWAP or the 9 EMA and holds: a candle wicks into it and closes back in the
  trend direction.
- **Entry:** above the high (calls) or below the low (puts) of that holding
  candle.
- **Invalidation:** a 5-min close on the wrong side of VWAP.
- **Best when:** it's the first or second pullback of the day. Later
  pullbacks fail more often.

### C. Key Level Break and Retest
- **Setup:** price breaks a strong level from section 2 (for example the
  previous day's high), comes back to test it, and the level holds as
  support (or resistance, for puts).
- **Entry:** on the confirming candle off the retest.
- **Invalidation:** a 5-min close back through the level.

### D. 4-Hour Manipulation (Power of 3)

Each 4-hour candle tends to move in three phases: **accumulation** (a range
near the open), **manipulation** (a fake push to one side that sweeps
liquidity), then **distribution** (the real move the other way). Wait for the
manipulation; trade the distribution.

- **4H candles (ET):** 8:00 AM–12:00 PM (includes pre-market) and
  12:00–4:00 PM, as Robinhood's `4hour` bars with extended bounds.
- **Manipulation:** price pushes away from the 4H open and **sweeps** a
  liquidity level: the prior 4H candle's high/low, the pre-market high/low,
  the previous day's high/low, or the opening range. Then it **fails**: a
  5-min candle closes back inside the level.
- **Entry (after all three):**
  1. Sweep of the level.
  2. 5-min close back through it (the reclaim).
  3. **Shift in structure:** after a sweep low, a 5-min close above the last
     lower high (bullish); after a sweep high, a close below the last higher
     low (bearish). Enter on that close or the first pullback that holds.
- **Never enter during the manipulation leg.** A push through a level with no
  reclaim is either a real breakout (setups A/C) or nothing yet.
- **Stop:** beyond the sweep extreme, plus about $0.10 on SPY.
- **Target:** the other side of the 4H range, or the next strong level.
  Reward/risk at least 1.5.
- **Score it:** the sweep and reclaim count as the key-level factor. The VWAP
  requirement is met once price **reclaims VWAP** in the new direction; until
  then it is not an entry.
- **Best when:** the distribution direction matches the daily trend, and the
  sweep happens into a strong level (section 2).
- **Example (2026-09-29):** the 12–4 PM candle opened $763.25, swept below
  the morning 4H low ($762.57) to $762.35, reclaimed, and ran to $765.30. A
  clean bullish Power of 3. Entry on the structure shift (~$763.6, over the
  $763.56 lower high) with a stop at $762.25 gave only about 1.2:1 to the
  $765.30 high, so it would have been skipped under the 1.5 rule.

### E. Momentum Run (volume breakout)

For fast run-ups and run-downs that never pull back to VWAP. Catch the start
of the move, not the middle of it.

- **Trigger:** after 9:45, a 5-min candle **closes through** VWAP or a strong
  level (section 2) in the trend direction, with volume at least **1.5× the
  average of the prior 10 bars**, ADX at least 20 and rising, and QQQ moving
  the same way.
- **Entry:** the close of the **next** 5-min candle if it holds beyond the
  level, or the first pullback to the 9 EMA that holds, whichever comes first.
- **Don't chase:** skip it if price is already more than **$1.50** past the
  breakout level, or already at the next strong level.
- **Stop:** beyond the breakout candle's low (bullish) or high (bearish),
  plus about $0.10.
- **Target:** the next strong level. Reward/risk at least 1.5, as always.
- **Example (2026-10-01):** the 1:20 PM candle closed back above the broken
  $762.2–762.7 zone and VWAP on about 2× volume, QQQ ripping. Entry ~$763.70,
  stop $762.45, but the next strong level ($764.7–765.1) was only ~1.2R away,
  so it would have been skipped; price stalled at $765.32, right at that level.

### F. Midday Squeeze Breakout

From the missed-move review (journal/missed-moves.md): 4 of 7 sessions had
this, each worth $2.70–4.60.

- **When:** 11:00 AM–2:30 PM ET.
- **Squeeze:** SPY stays inside a range no wider than **$2.50** for at least
  **45 minutes** (tighter is better). Mark the range high and low.
- **Trigger:** a 5-min candle **closes outside** the range on at least **2×**
  the prior 10-bar average volume, with QQQ breaking the same way.
- **Entry:** on the trigger candle's close if it is within **$0.75** of the
  range edge; otherwise wait for the first pullback toward the edge that
  holds (do not chase).
- **Stop:** back inside the range: the range midpoint or the breakout
  candle's opposite end, whichever is closer, plus about $0.10.
- **Target:** the **measured move**: range edge + 2× the range height
  (bullish; minus for bearish). Take it earlier if price stalls at a strong
  level.
- **Examples:** 9/24 range $763.39–764.65 → target $767.17, reached $768.95.
  9/28 range $764.66–765.83 → target $768.17, reached $769.54. 9/29 range
  $762.35–763.56 → target $765.98, reached $765.30 (fell short; trail the
  stop under each higher low).
- **Speed:** these moves finish in 15–30 minutes. Each check reports the
  current range edges; in the real-money phase, price alerts sit on them.

## 5. No-trade filters

Skip the day or the setup if any of these apply:
- ADX under 20, or price crossing VWAP back and forth (chop).
- A major scheduled event before the planned exit time.
- SPY and QQQ disagree on direction.
- Two losing trades already today: done for the day.
- The trade would break any rule in `CLAUDE.md` (size, day-trade count, time
  window).
- Feeling the need to "make it back": no revenge trades.

## 6. Contract selection (0DTE)

- **Strike:** at the money or 1–2 strikes out of the money.
- **Spread:** bid-ask no wider than 10% of the option's price.
- **Liquidity:** open interest and volume in the thousands on SPY; skip thin
  strikes.
- **Budget reality:** with the premium capped at $25–50 (5–10% of $500), SPY
  0DTE contracts often have to be further out of the money, especially early
  in the day. Those win less often. Never buy a cheaper, farther strike just
  to fit the budget if it breaks the rules above; skip the trade instead.

## 7. Trade management

- **Stop on the option:** a broker stop order at about 40–50% below the entry
  price, placed right after the fill.
- **Invalidation stop:** if the underlying hits the setup's invalidation
  point first, close the trade even if the option stop hasn't triggered.
- **Time stop:** if the trade hasn't moved in your favor within 30 minutes,
  close it. Time decay is working against you.
- **Protecting profit** (stops only move up):
  - Option up 30%: raise the stop to break-even.
  - Option up 60%: raise the stop to lock in about +30%.
  - Target: +50% to +100%, or the next strong key level on the underlying.
- **Hard exit:** closed by 3:30 PM ET, win or lose.

## 8. Weekly review

Every weekend, from `../journal/trades.md`:
- Win rate and average win vs average loss, per setup (A, B, C).
- Win rate by confluence grade: are A-grade trades actually better?
- Rule breaks: which rules were broken, and what they cost.
- Keep what works, cut what doesn't, and update this playbook.

## 9. Fractional share trades (dollar-based)

A second, lower-risk way to trade the same confluence signals: buy a dollar
amount of an ETF instead of an option. Moves are smaller than 0DTE, but so is
the risk, and there is no time decay.

### Instruments (all fractional-tradable on the Agentic account)

| Direction | Buy | Tracks |
|---|---|---|
| Bullish S&P 500 | **SPY** | S&P 500 |
| Bearish S&P 500 | **SH** | Inverse (−1x daily) S&P 500 |
| Bullish Nasdaq | **QQQ** | Nasdaq 100 |
| Bearish Nasdaq | **PSQ** | Inverse (−1x daily) Nasdaq 100 |

Fractional shares cannot be sold short, so bearish trades buy an inverse ETF.
Only 1x inverse funds: leveraged 2x/3x inverse funds decay and can move too
fast for alert-based stops.

### How fractional orders work here

- **Market orders only, regular hours only** (9:30 AM–4:00 PM ET). No limit,
  stop, or after-hours orders on fractional shares.
- **No broker stop order.** The stop is a Robinhood **price alert** at the
  stop level; when it fires, the position is sold at market. Real fills can
  land below the stop in a fast move.
- Buying and selling the same day is a **day trade** (counts toward the 3 per
  rolling 5 business days).

### Sizing

- **Position size: at most 50% of the account** ($250 at $500).
- **Risk = position × distance to stop**, and must stay within 5% of the
  account ($25). With structure-based stops on SPY (usually 0.3–1% away), real
  risk is often $1–3 per trade.
- **Reward/risk at least 1.5:** the target (next key level) must be at least
  1.5× as far as the stop.

### Same-day only

The owner exits every candle trade by the end of the day: no overnight holds.

- **Candles:** 5-min for entries, 15-min for context. Hourly and daily charts
  set direction and key levels only.
- **Entries:** 9:45 AM–2:30 PM ET, same window as 0DTE.
- **Exit:** by **3:45 PM ET** at the latest (fractional orders only fill in
  regular hours, so leave room before the 4:00 close).
- **Day trades:** every candle trade uses one of the 3 allowed per rolling 5
  business days, shared with 0DTE trades. Pick the better of the two for each
  setup; do not take both on the same signal.
- **Stop:** the price alert, checked at every check-in; if the alert fires,
  sell at market right away.
- **Best days:** strong trend days (ADX over 25), where a candle move has room
  to run before the close.

### Candle patterns

A pattern only counts **at a key level (section 2)** and **after the next
candle confirms it** (trades through the pattern's high for bullish, low for
bearish). A pattern in the middle of nowhere is noise.

| Bullish (buy SPY/QQQ) | Bearish (buy SH/PSQ) | What it shows |
|---|---|---|
| Hammer | Shooting star | Long wick rejects a level; body closes away from it |
| Bullish engulfing | Bearish engulfing | Second candle's body swallows the first: control flips |
| Morning star | Evening star | Three-candle turn: push, pause (small body), reversal |
| Bull flag breakout | Bear flag breakdown | Sharp move, tight pullback, break in the trend direction |
| Inside-bar breakout up | Inside-bar breakdown | Tight candle inside the prior one, then a break out of it |

- **Stop:** just beyond the pattern's extreme (below a hammer's low, above a
  shooting star's high), plus a small buffer (about $0.10 on SPY).
- **Target:** the next strong key level, or trail the stop under each new
  higher low (bullish) / above each lower high (bearish). Stops only move in
  the trade's favor.
- **Score it:** the pattern must still pass the confluence card (section 3).
  It counts as the "candle structure" factor; the other factors still apply.

### Paper trading

During the paper phase, log fractional setups next to options setups with the
instrument, dollar amount, entry, alert-stop, target, and result, so the two
approaches can be compared.
