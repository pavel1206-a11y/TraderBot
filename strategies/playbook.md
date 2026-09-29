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

Trade only these three with-trend setups. Counter-trend "catch the reversal"
trades are left out on purpose: they lose more often, and 0DTE leaves no time
to be wrong.

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
  land below the stop, and a gap overnight can blow straight through it.
- Buying and selling the same day is a **day trade** (counts toward the 3 per
  rolling 5 business days).

### Sizing

- **Position size: at most 50% of the account** ($250 at $500).
- **Risk = position × distance to stop**, and must stay within 5% of the
  account ($25). With structure-based stops on SPY (usually 0.3–1% away), real
  risk is often $1–3 per trade.
- **Reward/risk at least 1.5:** the target (next key level) must be at least
  1.5× as far as the stop.

### Two modes

| | Intraday | Swing |
|---|---|---|
| Candles | 5-min and 15-min | Hourly and daily |
| Hold | Same day; out by 3:45 PM ET | 1–5 days |
| Day trade used | Yes | No |
| Stop | Alert, checked at every check-in | Alert; re-check each morning for gaps |
| Best for | Strong trend days (ADX over 25) | Daily-chart patterns at key levels |

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
