"""Exit study for setup F (owner OK 2026-10-10): apply the best exit ideas from the first-candle study to F.
Entries: current F rules from bt.py (baseline +1.5R run), each re-managed independently with the exit plans below.
Management starts on the bar after entry; inside a bar the stop is assumed hit before any target/partial.
Stop moves apply from the next bar. Flat at 15:25. SPY cost 0.04 pts/trade.
Options: 0DTE, Black-Scholes model from optbt.py. Total premium cap $100: one contract (<= $100) for single exits,
two contracts (<= $50 each, farther OTM if needed) for plans that sell half. Train < 2026-07-16 <= valid.
"""
import bt, optbt
from statistics import mean

bars = bt.load("data/spy_qqq_5min.csv")
days = sorted(d for d in bars["SPY"] if d in bars["QQQ"])
BASE = dict(bt.DEFAULT, setups="F")
ENTRIES = bt.run(bars, BASE, days)

PLANS = [
    ("Current: target 1.5R", dict(tgt=1.5)),
    ("Break-even after +0.5R, target 1.5R", dict(tgt=1.5, be=0.5)),
    ("Half at +0.5R, rest BE, target 2R", dict(tgt=2.0, partial=0.5)),
    ("Half at +0.5R, rest BE, hold to 3:25", dict(partial=0.5)),
    ("Half at +1R, rest BE, target 2R", dict(tgt=2.0, partial=1.0)),
    ("Trail 0.5R after +0.5R", dict(trail=0.5, trail_on=0.5)),
    ("Trail 1R after +1R", dict(trail=1.0, trail_on=1.0)),
    ("Half at +0.5R, rest BE, trail 0.5R", dict(partial=0.5, trail=0.5, trail_on=0.5)),
    ("Half at +1R, rest BE, trail 1R", dict(partial=1.0, trail=1.0, trail_on=1.0)),
    ("Half at +0.25R, rest BE, target 1.5R", dict(tgt=1.5, partial=0.25)),
]

def manage(t, S, X):
    i0 = next(k for k, b in enumerate(S) if b["t"] == t["t"])
    dr, e, stop = t["dir"], t["entry"], t["stop"]; R = (e - stop) * dr
    legs, size, best, took = [], 1.0, 0.0, False
    for j in range(i0 + 1, len(S)):
        y = S[j]
        if (y["l"] <= stop) if dr > 0 else (y["h"] >= stop):
            legs.append((size, stop, y["t"])); break
        fav = (y["h"] - e) if dr > 0 else (e - y["l"])
        if X.get("partial") and not took and fav >= X["partial"] * R:
            legs.append((0.5, e + dr * X["partial"] * R, y["t"])); size, took = 0.5, True
            stop = e + dr * 0.04 if (e + dr * 0.04 - stop) * dr > 0 else stop
        if X.get("tgt") and fav >= X["tgt"] * R:
            legs.append((size, e + dr * X["tgt"] * R, y["t"])); break
        if y["t"] >= "15:25":
            legs.append((size, y["c"], y["t"])); break
        best = max(best, fav)
        if X.get("be") is not None and best >= X["be"] * R and (e + dr * 0.04 - stop) * dr > 0:
            stop = e + dr * 0.04
        if X.get("trail") and best >= X["trail_on"] * R:
            ns = e + dr * (best - X["trail"] * R)
            if (ns - stop) * dr > 0: stop = ns
    else:
        legs.append((size, S[-1]["c"], S[-1]["t"]))
    pnl = sum(f * (px - e) * dr for f, px, _ in legs) - bt.COST
    return legs, pnl, pnl / R

def option_usd(t, S, legs, two):
    i = next(k for k, b in enumerate(S) if b["t"] == t["t"])
    iv = min(0.45, max(0.08, optbt.IV_MULT * optbt.rv(S, i))); put = t["dir"] < 0
    cap = 50.0 if two else 100.0
    T0 = optbt.mins_to_close(t["t"], plus=5) / optbt.YEAR_MIN
    for otm in range(0, 8):
        K = (int(t["entry"]) - otm) if put else (int(t["entry"]) + 1 + otm)
        p0 = optbt.bs(t["entry"], K, T0, iv, put) + optbt.SLIP
        if p0 * 100 <= cap: break
    else:
        return None
    if p0 < 0.05: return None
    n = 2 if two else 1; usd = 0.0
    for f, px, xt in legs:
        T1 = optbt.mins_to_close(xt, plus=2.5 if xt < "15:25" else 5) / optbt.YEAR_MIN
        p1 = max(0.01, optbt.bs(px, K, T1, iv, put) - optbt.SLIP)
        usd += f * n * (p1 - p0) * 100
    return usd

def line(xs, money=False):
    if not xs: return "n=0"
    w = [x for x in xs if x > (0.5 if money else 0.01)]; l = [x for x in xs if x <= (0.5 if money else 0.01)]
    u = "$" if money else "R"
    return (f"n={len(xs):>3} win {len(w)/len(xs)*100:3.0f}%  avgW {mean(w) if w else 0:+6.2f}{u} avgL {mean(l) if l else 0:+6.2f}{u}  "
            f"total {sum(xs):+7.2f}{u}  per trade {mean(xs):+5.2f}{u}")

if __name__ == "__main__":
    print(f"F entries: {len(ENTRIES)} ({days[0]} to {days[-1]}); split at {bt.SPLIT}\n")
    for name, X in PLANS:
        two = "partial" in X
        out = {"T": ([], []), "V": ([], [])}
        for t in ENTRIES:
            S = bars["SPY"][t["day"]]; legs, pnl, R = manage(t, S, X)
            k = "T" if t["day"] < bt.SPLIT else "V"
            out[k][0].append(R)
            o = option_usd(t, S, legs, two)
            if o is not None: out[k][1].append(o)
        print(name + ("  [2 contracts <= $50 each]" if two else "  [1 contract <= $100]"))
        for k, lab in (("T", "TRAIN"), ("V", "VALID")):
            print(f"  {lab} SPY  {line(out[k][0])}")
            print(f"  {lab} OPT  {line(out[k][1], True)}")
