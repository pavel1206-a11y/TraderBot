"""A2 rule-change backtest (owner ask 2026-11-25: "backtest a few months").

Compares the A2 rules before and after the owner's 2026-11-25 changes, one factor at a time:
  contract band   old $0.75-1.25 (target $1.00)  vs  new $1.25-1.75 (target $1.50, closer to ATM)
  entry cutoff    old: entry bar closes by 10:30  vs  new: by 10:15
  swoop           old: not traded                 vs  new: traded (poke past a mark that closes back
                  inside, or a cross undone on the next bar -> the other way; stop = poke extreme -/+ $0.10)
Cross entries: the first 5-min close beyond the 9:30-9:45 high/low, then the next close still beyond it;
stop = range midpoint -/+ $0.10. Exit (current rule, "d"): half at +50%, rest trailed one 5-min bar
behind (never below entry), out at 11:00. One trade a day (first signal).
Option model and costs: same as a2_exits.py (Black-Scholes on trailing 10-day realized vol, $0.03 slip
each way). Model dollars are approximate; compare variants against each other.
"""
import math, sys
from collections import defaultdict
from a2_exits import load, bs, mins_left, YEAR, realized_iv

def signal(b, cutoff, swoop):
    H = max(x["h"] for x in b[:3]); L = min(x["l"] for x in b[:3]); mid = (H + L) / 2
    for i in range(3, len(b) - 1):
        if b[i]["t"] > cutoff: return None
        x = b[i]; c = x["c"]
        if c > H or c < L:
            call = c > H; n = b[i + 1]
            if n["t"] <= cutoff and ((n["c"] > H) if call else (n["c"] < L)):
                return dict(i=i + 1, call=call, stop=mid - 0.10 if call else mid + 0.10, kind="cross")
            if swoop and n["t"] <= cutoff and L <= n["c"] <= H:   # cross undone right away -> other way
                ext = max(x["h"], n["h"]) if call else min(x["l"], n["l"])
                return dict(i=i + 1, call=not call, stop=ext + 0.10 if call else ext - 0.10, kind="swoop")
            continue
        if swoop and (x["h"] > H) != (x["l"] < L):              # one-sided poke, close back inside
            call = x["l"] < L
            return dict(i=i, call=call, stop=x["l"] - 0.10 if call else x["h"] + 0.10, kind="swoop")
    return None

def run(bars, days, i, band, cutoff, swoop):
    b = bars[days[i]]
    if len(b) < 70: return None
    iv = realized_iv(bars, days, i)
    if iv is None: return None
    s = signal(b, cutoff, swoop)
    if not s: return None
    j0, call, stop = s["i"], s["call"], s["stop"]; S0 = b[j0]["c"]; dr = 1 if call else -1
    if (S0 - stop) * dr <= 0: return None
    lo, hi = band; tgt = (lo + hi) / 2; T0 = mins_left(b[j0]["t"]) / YEAR; best = None
    for k in range(0, 20):
        K = (math.ceil(S0) + k) if call else (math.floor(S0) - k)
        p = bs(S0, K, T0, iv, call)
        if lo <= p <= hi and (best is None or abs(p - tgt) < abs(best[1] - tgt)): best = (K, p)
    if not best: return None
    K, p0 = best; cost = p0 + 0.03
    val = lambda S, t: bs(S, K, mins_left(t) / YEAR, iv, call)
    tp = 1.5 * cost; half, booked, size = False, 0.0, 1.0
    for j in range(j0 + 1, len(b)):
        y = b[j]; adv = y["l"] if call else y["h"]; fav = y["h"] if call else y["l"]
        if (adv - stop) * dr <= 0:
            return booked + size * (val(stop, y["t"]) - 0.03 - cost) * 100, s["kind"], cost
        if not half and val(fav, y["t"]) >= tp:
            booked += 0.5 * (tp - 0.03 - cost) * 100; size = 0.5; half = True
            if (S0 - stop) * dr > 0: stop = S0
        if half:
            ns = y["l"] if call else y["h"]
            if (ns - stop) * dr > 0: stop = ns
        if y["t"] >= "10:55":
            return booked + size * (val(y["c"], y["t"]) - 0.03 - cost) * 100, s["kind"], cost
    return None

VARIANTS = [
    ("1 old rules ($0.75-1.25, to 10:30, no swoop)", (0.75, 1.25), "10:25", False),
    ("2 new band only ($1.25-1.75)",                 (1.25, 1.75), "10:25", False),
    ("3 10:15 cutoff only",                          (0.75, 1.25), "10:10", False),
    ("4 swoop only",                                 (0.75, 1.25), "10:25", True),
    ("5 NEW RULES (band + 10:15 + swoop)",           (1.25, 1.75), "10:10", True),
    ("6 new rules, old band",                        (0.75, 1.25), "10:10", True),
]

if __name__ == "__main__":
    bars = load(sys.argv[1:]); days = sorted(d for d in bars if len(bars[d]) >= 70)
    periods = [("all", "0000", "9999"), ("Feb23-Jun30", "0000", "2026-06-30"),
               ("Jul1-Oct8", "2026-07-01", "2026-10-08"), ("Oct9-Nov25", "2026-10-09", "9999"),
               ("last 3 mo (Aug25-)", "2026-08-25", "9999")]
    print(f"sessions: {len(days)} ({days[0]}..{days[-1]})")
    out = defaultdict(dict)
    for name, band, cut, sw in VARIANTS:
        rows = []
        for i in range(len(days)):
            r = run(bars, days, i, band, cut, sw)
            if r: rows.append((days[i],) + r); out[days[i]][name[0]] = r
        print(f"\n[{name}]")
        for nm, lo, hi in periods:
            rr = [r for r in rows if lo <= r[0] <= hi]
            if not rr: continue
            pl = [r[1] for r in rr]; w = [p for p in pl if p > 0]; l = [p for p in pl if p <= 0]
            eq = pk = dd = 0
            for p in pl: eq += p; pk = max(pk, eq); dd = min(dd, eq - pk)
            sw_n = [r[1] for r in rr if r[2] == "swoop"]
            print(f"  {nm:18s} n={len(pl):3d} win={len(w)/len(pl)*100:3.0f}% total=${sum(pl):7.0f} "
                  f"avgW=${(sum(w)/len(w) if w else 0):4.0f} avgL=${(sum(l)/len(l) if l else 0):5.0f} "
                  f"maxDD=${dd:6.0f} ex-top3=${sum(pl)-sum(sorted(pl)[-3:]):6.0f} avgCost=${sum(r[3] for r in rr)/len(rr)*100:4.0f}"
                  + (f" | swoops n={len(sw_n)} ${sum(sw_n):.0f}" if sw_n else ""))
    with open("a2_v2_days.csv", "w") as f:
        f.write("date," + ",".join(f"v{v[0][0]}_pl,v{v[0][0]}_kind" for v in VARIANTS) + "\n")
        for d in sorted(out):
            f.write(d + "," + ",".join(f"{out[d][v[0][0]][0]:.0f},{out[d][v[0][0]][1]}" if v[0][0] in out[d] else ","
                                       for v in VARIANTS) + "\n")
