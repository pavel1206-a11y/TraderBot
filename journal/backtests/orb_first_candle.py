"""First-candle breakout test (owner question 2026-10-10).

Mark the high and low of the 9:30 candle; enter on whichever side breaks first
(buy 1 cent above the high / sell 1 cent below the low, detected on 1-minute bars).
Range candle: the 9:30 1-minute bar, or the 9:30-9:35 5-minute bar.
Exits tested: stop at the other side of the candle with target 1R / 2R / none (exit 3:55),
and no stop (exit 3:55). If one 1-minute bar hits both stop and target, the stop counts.
If one bar breaks both sides, the day is scored as a loss (cannot tell which came first).
Cost: $0.02 per share round trip. Usage: python3 orb_first_candle.py file1.json [file2.json ...]
"""
import json, sys
from collections import defaultdict

COST = 0.02
days = defaultdict(list)
for f in sys.argv[1:]:
    for r in json.load(open(f))["data"]["results"]:
        for b in r["bars"]:
            if b.get("interpolated"):
                continue
            h, m = int(b["begins_at"][11:13]) - 4, int(b["begins_at"][14:16])  # EDT
            t = f"{h:02d}:{m:02d}"
            if "09:30" <= t <= "15:59":
                days[b["begins_at"][:10]].append(dict(t=t, h=float(b["high_price"]), l=float(b["low_price"]),
                                                      c=float(b["close_price"])))

def sim(bars, rng_min, tgt_R, use_stop):
    first = [b for b in bars if b["t"] < f"09:{30 + rng_min:02d}"]
    rest = [b for b in bars if b["t"] >= f"09:{30 + rng_min:02d}"]
    H, L = max(b["h"] for b in first), min(b["l"] for b in first)
    up, dn = H + 0.01, L - 0.01
    for i, b in enumerate(rest):
        hu, hd = b["h"] >= up, b["l"] <= dn
        if not (hu or hd):
            continue
        if hu and hd:
            return dict(t=b["t"], side="both", pnl=-(H - L) - COST, R=-1.0)
        d = 1 if hu else -1
        entry = up if d > 0 else dn
        stop = dn if d > 0 else up
        risk = (entry - stop) * d
        tgt = entry + d * tgt_R * risk if tgt_R else None
        for j, x in enumerate(rest[i:]):
            last = x["t"] >= "15:55"
            if use_stop and j > 0 and ((x["l"] <= stop) if d > 0 else (x["h"] >= stop)):
                ex = stop; break
            if tgt and ((x["h"] >= tgt) if d > 0 else (x["l"] <= tgt)) and j > 0:
                ex = tgt; break
            if last:
                ex = x["c"]; break
        else:
            ex = rest[-1]["c"]
        pnl = (ex - entry) * d - COST
        return dict(t=b["t"], side="long" if d > 0 else "short", entry=entry, exit=ex, pnl=pnl, R=pnl / risk, risk=risk)
    return None

if __name__ == "__main__":
    ds = sorted(d for d in days if len(days[d]) > 300)
    print(f"{len(ds)} sessions: {ds[0]} to {ds[-1]}\n")
    for rng in (1, 5):
        print(f"=== Range = first {rng}-minute candle ===")
        for label, tR, st in (("stop other side, target 1R", 1, True), ("stop other side, target 2R", 2, True),
                              ("stop other side, hold to 3:55", None, True), ("no stop, hold to 3:55", None, False)):
            res = [(d, sim(days[d], rng, tR, st)) for d in ds]
            tr = [r for _, r in res if r]
            w = [r for r in tr if r["pnl"] > 0]
            tot = sum(r["pnl"] for r in tr)
            print(f"{label:<32} trades {len(tr):>2}  profitable {len(w):>2}  ({len(w)/len(tr)*100:3.0f}%)  "
                  f"net ${tot:+6.2f}/share  avg {sum(r['R'] for r in tr)/len(tr):+.2f}R")
        print()
    print("Day by day (5-minute candle, stop other side, target 1R):")
    for d in ds:
        r = sim(days[d], 5, 1, True)
        fc = [b for b in days[d] if b["t"] < "09:35"]
        print(f"{d}  range {min(b['l'] for b in fc):.2f}-{max(b['h'] for b in fc):.2f}  "
              + (f"{r['side']:<5} @{r['t']}  {'WIN ' if r['pnl']>0 else 'LOSS'} {r['pnl']:+.2f} ({r['R']:+.2f}R)" if r else "no break"))
