"""A2 exit study (owner ask 2026-11-17: "run the test").

Entry (playbook A2, 5-min version): mark the 9:30-9:45 high/low (wicks). From the 9:45 bar on, the first
5-min close beyond a mark, then the next 5-min close still beyond it -> enter at that close (calls above,
puts below). Entries by the 10:25 bar (window to 10:30). One trade a day.
Stop: range midpoint -/+ $0.10 on SPY, checked against each bar's low/high (stop hit first if a bar
touches both the stop and a profit level: conservative).

Option model: one 0DTE SPY contract, Black-Scholes (r = 0), time to 16:00 in trading-time years (252 x 390 min),
IV = the prior 10 sessions' realized 5-min vol (annualized), clamped 8-60%. Strike = the
out-of-the-money $1 strike whose price is closest to $1.00 within $0.75-1.25 (skip the day if none).
Costs: buy at model + $0.03, sell at model - $0.03 (per share). P&L in dollars per contract.

Exits compared:
  a  +50% take-profit (whole contract), else out at 11:00
  b  hold to 11:00 (stop only)
  c  half at +50%, stop on the rest moves to entry (SPY), rest out at 11:00
  d  half at +50%, rest trailed one 5-min bar behind (prior bar's low for calls / high for puts,
     never below entry), rest out at 11:00
  e  same as d but the rest may run to 12:30
"""
import csv, math, sys
from collections import defaultdict

def load(paths):
    bars = defaultdict(list)
    for p in paths:
        for r in csv.DictReader(open(p)):
            if r["symbol"] != "SPY": continue
            d, t = r["et"].split()
            if "09:30" <= t <= "15:55":
                bars[d].append(dict(t=t, o=float(r["o"]), h=float(r["h"]), l=float(r["l"]), c=float(r["c"]), v=float(r["v"])))
    for d in bars:
        seen = {}
        for b in bars[d]: seen[b["t"]] = b
        bars[d] = [seen[k] for k in sorted(seen)]
    return bars

def ncdf(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def bs(S, K, T, iv, call):
    if T <= 0: return max(0.0, (S - K) if call else (K - S))
    s = iv * math.sqrt(T); d1 = (math.log(S / K) + 0.5 * s * s) / s; d2 = d1 - s
    return S * ncdf(d1) - K * ncdf(d2) if call else K * ncdf(-d2) - S * ncdf(-d1)

def mins_left(t):  # minutes from the END of the bar starting at t to 16:00
    h, m = map(int, t.split(":")); return 16 * 60 - (h * 60 + m + 5)

YEAR = 252 * 390  # trading-time year (0DTE decays over trading minutes)

def realized_iv(bars, days, i):
    rets = []
    for d in days[max(0, i - 10):i]:
        b = bars[d]
        for k in range(1, len(b)): rets.append(math.log(b[k]["c"] / b[k - 1]["c"]))
    if len(rets) < 200: return None
    sd = (sum(x * x for x in rets) / len(rets)) ** 0.5
    return min(0.60, max(0.08, 1.0 * sd * math.sqrt(78 * 252)))

VWAP_FILTER = "--vwap" in sys.argv

def vwap_ok(b, i, call):
    """0DTE checklist item 1 (CLAUDE.md): calls only above a rising VWAP, puts only below a falling one.
    VWAP is approximated with typical price x equal weights (no volume in some rows) -> use the bar series."""
    pv = vv = 0.0; vw = []
    for x in b[: i + 1]:
        w = x.get("v", 1) or 1; pv += (x["h"] + x["l"] + x["c"]) / 3 * w; vv += w; vw.append(pv / vv)
    if i < 3: return False
    rising = vw[i] > vw[i - 3]
    return (b[i]["c"] > vw[i] and rising) if call else (b[i]["c"] < vw[i] and not rising)

def signal(b):
    H = max(x["h"] for x in b[:3]); L = min(x["l"] for x in b[:3])
    for i in range(3, len(b) - 1):
        if b[i]["t"] > "10:20": return None
        c = b[i]["c"]
        if c > H or c < L:
            call = c > H
            n = b[i + 1]["c"]
            if ((n > H) if call else (n < L)) and (not VWAP_FILTER or vwap_ok(b, i + 1, call)):
                return dict(i=i + 1, call=call, H=H, L=L, mid=(H + L) / 2)
            # failed cross: keep scanning (swoop-and-return is the owner's discretionary part; not modeled)
    return None

def run(bars, days, i, X):
    d = days[i]; b = bars[d]
    if len(b) < 70: return None
    iv = realized_iv(bars, days, i)
    if iv is None: return None
    s = signal(b)
    if not s: return None
    j0, call = s["i"], s["call"]; S0 = b[j0]["c"]; T0 = mins_left(b[j0]["t"]) / YEAR
    best = None
    for k in range(1, 15):
        K = (math.ceil(S0) + k) if call else (math.floor(S0) - k)
        p = bs(S0, K, T0, iv, call)
        if 0.75 <= p <= 1.25 and (best is None or abs(p - 1) < abs(best[1] - 1)): best = (K, p)
    if not best: return None
    K, p0 = best; cost = p0 + 0.03
    dr = 1 if call else -1
    stop = s["mid"] - 0.10 if call else s["mid"] + 0.10
    val = lambda S, t: bs(S, K, mins_left(t) / YEAR, iv, call)
    tp_px = 1.5 * cost  # option price for +50%
    half_done, booked, size = False, 0.0, 1.0
    last_t = "10:55" if X != "e" else "12:25"
    for j in range(j0 + 1, len(b)):
        y = b[j]
        adv = y["l"] if call else y["h"]; fav = y["h"] if call else y["l"]
        # 1) stop first (conservative)
        if (adv - stop) * dr <= 0:
            px = val(stop, y["t"]) - 0.03
            return booked + size * (px - cost) * 100, "stop" if not half_done else "half+stop"
        # 2) +50%
        if not half_done and X in "acde" and val(fav, y["t"]) >= tp_px:
            if X == "a": return (tp_px - 0.03 - cost) * 100, "+50%"
            booked += 0.5 * (tp_px - 0.03 - cost) * 100; size = 0.5; half_done = True
            if X == "c": stop = S0
            if X in "de": stop = S0 if (S0 - stop) * dr > 0 else stop
        # 3) trail (d/e): one bar behind, after the half is off
        if half_done and X in "de":
            ns = y["l"] if call else y["h"]
            if (ns - stop) * dr > 0: stop = ns
        if y["t"] >= last_t:
            px = val(y["c"], y["t"]) - 0.03
            return booked + size * (px - cost) * 100, "time"
    return None

if __name__ == "__main__":
    bars = load([a for a in sys.argv[1:] if not a.startswith("--")])
    days = sorted(d for d in bars if len(bars[d]) >= 70)
    names = dict(a="+50% TP, else 11:00", b="hold to 11:00", c="half +50%, rest BE stop, 11:00",
                 d="half +50%, rest 1-bar trail, 11:00", e="half +50%, rest 1-bar trail, 12:30")
    res = {X: [] for X in "abcde"}
    for i in range(len(days)):
        for X in "abcde":
            r = run(bars, days, i, X)
            if r: res[X].append((days[i], r[0], r[1]))
    def stats(rows):
        pl = [x[1] for x in rows]; w = [x for x in pl if x > 0]; l = [x for x in pl if x <= 0]
        eq, peak, dd = 0, 0, 0
        for x in pl: eq += x; peak = max(peak, eq); dd = min(dd, eq - peak)
        top3 = sum(sorted(pl)[-3:])
        return dict(n=len(pl), w=len(w), tot=sum(pl), avgw=sum(w)/len(w) if w else 0, avgl=sum(l)/len(l) if l else 0,
                    dd=dd, ex3=sum(pl) - top3)
    periods = [("all", "0000", "9999"), ("Feb23-Jun30", "0000", "2026-06-30"), ("Jul1-Oct8", "2026-07-01", "2026-10-08"),
               ("Oct9-Nov17", "2026-10-09", "9999")]
    print(f"sessions with data: {len(days)} ({days[0]}..{days[-1]})")
    for X in "abcde":
        print(f"\n[{X}] {names[X]}")
        for nm, lo, hi in periods:
            s = stats([r for r in res[X] if lo <= r[0] <= hi])
            if s["n"]:
                print(f"  {nm:12s} n={s['n']:3d} win={s['w']/s['n']*100:4.0f}% total=${s['tot']:8.0f} "
                      f"avgW=${s['avgw']:5.0f} avgL=${s['avgl']:5.0f} maxDD=${s['dd']:6.0f} ex-top3=${s['ex3']:7.0f}")
    if "--days" in sys.argv[0:] or True:
        with open("a2_exits_days%s.csv" % ("_vwap" if VWAP_FILTER else ""), "w") as f:
            f.write("date," + ",".join(f"{X}_pl,{X}_why" for X in "abcde") + "\n")
            by = defaultdict(dict)
            for X in "abcde":
                for dte, pl, why in res[X]: by[dte][X] = (pl, why)
            for dte in sorted(by):
                f.write(dte + "," + ",".join(f"{by[dte].get(X,(0,''))[0]:.0f},{by[dte].get(X,(0,''))[1]}" for X in "abcde") + "\n")
