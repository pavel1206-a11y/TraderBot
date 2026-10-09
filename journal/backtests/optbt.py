"""Option-priced replay of bt.py trades (0DTE SPY calls/puts, Black-Scholes model).

Robinhood keeps 5-min option bars for only about a month, so historical option prices are modeled:
  IV = IV_MULT x realized 5-min volatility of the last 24 bars (annualized), clipped to [0.08, 0.45].
  Calibrated 10/9 on real 0DTE quotes: 10/8 13:30 771P ($1.13, IV 0.225 vs RV 0.096) and
  10/6 12:20 780P ($0.51, IV 0.121 vs RV 0.055): ratio about 2.2-2.35.
Fills: buy at model + SLIP, sell at model - SLIP (bid/ask cost). Expiry 16:00 ET same day.
One contract per trade; skipped if the premium is over CAP (dollars).
"""
from math import log, sqrt, erf
import bt

IV_MULT, SLIP = 2.3, 0.02
N = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
YEAR_MIN = 365 * 24 * 60

def bs(S, K, T, s, put):
    if T <= 0:
        return max(0.0, (K - S) if put else (S - K))
    d1 = (log(S / K) + 0.5 * s * s * T) / (s * sqrt(T)); d2 = d1 - s * sqrt(T)
    c = S * N(d1) - K * N(d2)
    return c - S + K if put else c

def mins_to_close(hhmm, plus=0.0):
    h, m = map(int, hhmm.split(":")); return max(0.5, 16 * 60 - (h * 60 + m) - plus)

def rv(S, i, n=24):
    r = [log(S[k]["c"] / S[k - 1]["c"]) for k in range(max(1, i - n), i + 1)]
    if len(r) < 3:
        return 0.06
    m = sum(r) / len(r); v = sum((x - m) ** 2 for x in r) / (len(r) - 1)
    return sqrt(v * 78 * 252)

def price_trade(t, S, otm=0, cap=100.0):
    """otm = strikes out of the money (0 = nearest strike at or just OTM)."""
    i = next(k for k, b in enumerate(S) if b["t"] == t["t"])
    iv = min(0.45, max(0.08, IV_MULT * rv(S, i)))
    put = t["dir"] < 0
    s0 = t["entry"]
    K = (int(s0) - otm) if put else (int(s0) + 1 + otm)
    T0 = mins_to_close(t["t"], plus=5) / YEAR_MIN
    p0 = bs(s0, K, T0, iv, put) + SLIP
    if p0 * 100 > cap or p0 < 0.05:
        return None
    s1 = t["exit"]
    T1 = mins_to_close(t["xt"], plus=2.5 if t["xt"] < "15:25" else 5) / YEAR_MIN
    p1 = max(0.01, bs(s1, K, T1, iv, put) - SLIP)
    return dict(K=K, iv=iv, p0=p0, p1=p1, usd=(p1 - p0) * 100)

def replay(bars, F, days, otm=0, cap=100.0):
    out = []
    for t in bt.run(bars, F, days):
        o = price_trade(t, bars["SPY"][t["day"]], otm, cap)
        if o:
            t.update(o); out.append(t)
    return out

def usd_stats(ts):
    if not ts:
        return dict(n=0, win=0, usd=0, avg=0, pf=0, dd=0, avgwin=0, avgloss=0)
    w = [t["usd"] for t in ts if t["usd"] > 0]; l = [t["usd"] for t in ts if t["usd"] <= 0]
    eq = pk = dd = 0.0
    for t in ts:
        eq += t["usd"]; pk = max(pk, eq); dd = max(dd, pk - eq)
    return dict(n=len(ts), win=len(w) / len(ts), usd=sum(w) + sum(l), avg=(sum(w) + sum(l)) / len(ts),
                pf=sum(w) / -sum(l) if l and sum(l) else 99, dd=dd,
                avgwin=sum(w) / len(w) if w else 0, avgloss=sum(l) / len(l) if l else 0)
