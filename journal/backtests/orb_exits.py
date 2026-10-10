"""Exit study for the first-candle breakout (owner ask 2026-10-10: "think about exits to better our win rate").
Entry fixed: touch of the 9:30-9:35 candle high/low (1 cent through), first side to break, optional QQQ filter.
Initial stop: other side of the candle (1R = candle range). 5-minute bars; inside a bar the stop is assumed hit
before the target (conservative). Stop moves (break-even, trailing) take effect from the next bar.
Win = net P&L > +$0.02/share, scratch = within +/-$0.02 (after $0.02 cost), loss = below.
Train Mar 23 - Jun 30, valid Jul 1 - Oct 8.
"""
import bt
S = bt.load("data/spy_qqq_5min.csv"); SPY, QQQ = S["SPY"], S["QQQ"]
days = sorted(d for d in SPY if len(SPY[d]) >= 70 and d in QQQ)
COST = 0.02

def entry(d, qqq):
    b, q = SPY[d], QQQ[d]; H, L = b[0]["h"], b[0]["l"]
    for i in range(1, len(b)):
        x = b[i]; up, dn = x["h"] > H, x["l"] < L
        if up and dn: return dict(i=i, both=True, H=H, L=L)
        if up or dn:
            dr = 1 if up else -1
            if qqq and (q[i]["h" if dr > 0 else "l"] - q[0]["h" if dr > 0 else "l"]) * dr <= 0: return None
            return dict(i=i, dr=dr, e=H + 0.01 if up else L - 0.01, stop=L - 0.01 if up else H + 0.01, H=H, L=L)
    return None

def manage(d, E, X):
    """X: tgt (R or None), be (move stop to entry+cost after +be R), trail (R distance once +trail_on R),
    partial (fraction taken at +p R), time (bars allowed to reach +0.25R), vwap (exit on close back through VWAP)."""
    b = SPY[d]; sv = bt.vwap(b)
    if E.get("both"): return -(E["H"] - E["L"]) - COST
    dr, e, stop = E["dr"], E["e"], E["stop"]; R = (e - stop) * dr
    tgt = e + dr * X["tgt"] * R if X.get("tgt") else None
    best, booked, size = 0.0, 0.0, 1.0
    for j in range(E["i"], len(b)):
        y = b[j]; fav = (y["h"] - e) * dr if dr > 0 else (e - y["l"]); adv_px = y["l"] if dr > 0 else y["h"]
        if j > E["i"] and (adv_px - stop) * dr <= 0:
            return booked + size * ((stop - e) * dr) - COST
        if X.get("partial") and size == 1.0 and fav >= X["partial"] * R and j >= E["i"]:
            booked += X["pfrac"] * X["partial"] * R; size -= X["pfrac"]
            stop = e + dr * 0.02  # rest goes to break-even
        if tgt is not None and j > E["i"] and fav >= X["tgt"] * R:
            return booked + size * X["tgt"] * R - COST
        if y["t"] >= "15:55":
            return booked + size * (y["c"] - e) * dr - COST
        best = max(best, (y["c"] - e) * dr, fav)
        if X.get("vwap") and j > E["i"] and (y["c"] - sv[j]) * dr < 0:
            return booked + size * (y["c"] - e) * dr - COST
        if X.get("time") and j - E["i"] >= X["time"] and best < 0.25 * R:
            return booked + size * (y["c"] - e) * dr - COST
        if X.get("be") is not None and best >= X["be"] * R:
            stop = e + dr * 0.02 if (e + dr * 0.02 - stop) * dr > 0 else stop
        if X.get("trail") and best >= X.get("trail_on", 0) * R:
            ns = e + dr * (best - X["trail"] * R)
            if (ns - stop) * dr > 0: stop = ns
    return booked + size * (b[-1]["c"] - e) * dr - COST

EXITS = [
    ("Baseline: target 1R", dict(tgt=1.0)),
    ("Baseline: target 0.25R", dict(tgt=0.25)),
    ("Hold to close (stop only)", dict()),
    ("Target 1R + break-even after +0.5R", dict(tgt=1.0, be=0.5)),
    ("Target 2R + break-even after +0.5R", dict(tgt=2.0, be=0.5)),
    ("Target 1R + break-even after +0.25R", dict(tgt=1.0, be=0.25)),
    ("Half at +0.5R, rest BE, target 2R", dict(tgt=2.0, partial=0.5, pfrac=0.5)),
    ("Half at +0.25R, rest BE, target 1R", dict(tgt=1.0, partial=0.25, pfrac=0.5)),
    ("Half at +0.5R, rest BE, hold to close", dict(partial=0.5, pfrac=0.5)),
    ("Trail 0.5R after +0.5R, no target", dict(trail=0.5, trail_on=0.5)),
    ("Trail 1R from entry, no target", dict(trail=1.0, trail_on=0.0)),
    ("Target 1R + time stop 30 min", dict(tgt=1.0, time=6)),
    ("Target 1R + exit on VWAP close-through", dict(tgt=1.0, vwap=True)),
    ("Half +0.5R, BE, trail 0.5R, time 30m", dict(partial=0.5, pfrac=0.5, trail=0.5, trail_on=0.5, time=6)),
]

def stats(pn):
    w = [p for p in pn if p > 0.02]; l = [p for p in pn if p < -0.02]; s = len(pn) - len(w) - len(l)
    return (f"n={len(pn):>3} win {len(w)/len(pn)*100:3.0f}% scr {s/len(pn)*100:3.0f}% loss {len(l)/len(pn)*100:3.0f}% "
            f"avgW {sum(w)/max(1,len(w)):.2f} avgL {sum(l)/max(1,len(l)):+.2f} net {sum(pn):+6.2f}")

if __name__ == "__main__":
    tr = [d for d in days if d < "2026-07-01"]; va = [d for d in days if d >= "2026-07-01"]
    for qqq in (False, True):
        print(f"\n=== Entry: first-candle break{' + QQQ also breaks' if qqq else ''} ===")
        for name, X in EXITS:
            res = {}
            for lab, ds in (("T", tr), ("V", va)):
                pn = [manage(d, E, X) for d in ds for E in [entry(d, qqq)] if E]
                res[lab] = stats(pn)
            print(f"{name:<40} TRAIN {res['T']}\n{'':<40} VALID {res['V']}")
