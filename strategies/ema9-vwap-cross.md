# 9 EMA / VWAP cross, calls only (candidate, paper only)

Owner request 2026-10-17: a 9 EMA + VWAP strategy that has been profitable in the past.

## Rules (SPY 5-min chart)

1. Plot the **9 EMA** (on 5-min closes) and **VWAP**.
2. **Entry (9:45–11:30 AM ET, first signal of the day only):** the 9 EMA crosses from below VWAP to **above VWAP** on this candle, the candle **closes above the 9 EMA**, and **QQQ is above its own VWAP**. Buy at the candle's close.
3. **Stop:** $0.30 below that candle's low (average risk ≈ $0.89 per SPY share).
4. **Exit:** the first 5-min candle that **closes back below VWAP**, or 3:30 PM, whichever comes first. No fixed target: let it run.

## Results (Jan 5–Oct 15, 2026, $0.02/trade cost)

| Period | Trades | Win rate | Avg win | Avg loss | Net per SPY share |
|---|---|---|---|---|---|
| Jan–Jun (rules chosen here) | 43 | 33% | +$3.01 | −$0.71 | **+$21.6** |
| **Jul–Oct (not seen by the search)** | **39** | **31%** | **+$2.71** | **−$0.68** | **+$14.3** |
| All | 82 | 32% | +$2.87 | −$0.69 | **+$35.9** |

- 7 of 9 months positive (May −$2.3, July −$0.8). Longest losing streak: 9.
- Neighbouring settings also profitable: stop buffer $0.15/$0.30/$0.50, with or without the QQQ filter (+$14.7 to +$35.9 per share).
- **The short mirror (EMA crosses below VWAP → puts) lost** (54 trades, −$1.5/share). Calls only.
- Wins about 4× losses, but only about 1 in 3 trades wins.

## Also tested

- **Pullback to the 9 EMA in an uptrend** (EMA ≥ $0.25 above VWAP, rising; candle tags the EMA and closes green above it; exit on a close below VWAP): 111 trades, 25% wins, +$29.2/share, but September went 0 for 13 and the worst losing streak was 20. Less consistent.
- **VWAP pullback with the 9 EMA still above VWAP:** did not hold up out of sample.
- Over 15,000 variants across the three families; chosen on Jan–Jun, checked on Jul–Oct. Code: `tools/pdh_pdl/s4.py`, `search4.py`.

## Caveats

R and dollars are SPY moves per share, not option prices. A 0DTE call held to a VWAP-close exit also decays, so paper-trade it before real money. Small sample (82 trades).
