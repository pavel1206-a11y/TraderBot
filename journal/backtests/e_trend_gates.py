"""E (momentum run) gate test: trend state vs range state (2026-11-25).

Question: the E close band ($0.30, extended $0.75 with >=1.2x vol) and the 1.5x volume bar missed every
leg of the 11/19, 11/20 and 11/25 trend days, but saved losses on range days (11/23, 11/24). Would
looser gates help when the trend is already clear at signal time, without hurting the rest?

Signal (SPY 5-min, 10:00-14:30, long; puts mirror): the bar closes above the session high so far
(the prior bars' max high), close - level <= band, volume >= vm x the prior 10-bar average.
Stop = the signal bar's low (risk at least $0.30). Exit: +1.5R target, the stop, or the 15:00 close.
At most one long and one short a day (first signal). Results in R (SPY points / risk): option P&L is
roughly proportional for near-the-money 0DTE, before decay.

Trend state (known at signal time, no hindsight): the last 6 closes all on the trade's side of VWAP
and VWAP higher (lower) than 12 bars earlier. Everything else = range state.
"""
import csv, sys
from collections import defaultdict

def load(paths):
    bars = defaultdict(dict)
    for p in paths:
        for r in csv.DictReader(open(p)):
            if r["symbol"] != "SPY": continue
            d, t = r["et"].split()
            if "09:30" <= t <= "15:55":
                bars[d][t] = dict(t=t, h=float(r["h"]), l=float(r["l"]), c=float(r["c"]), v=float(r["v"]))
    return {d: [v[k] for k in sorted(v)] for d, v in bars.items() if len(v) >= 70}

def day_signals(b, band, vm):
    out = []; pv = vv = 0.0; vw = []
    for x in b:
        pv += (x["h"] + x["l"] + x["c"]) / 3 * x["v"]; vv += x["v"]; vw.append(pv / vv)
    done = set()
    for i in range(12, len(b)):
        x = b[i]
        if not ("10:00" <= x["t"] <= "14:30"): continue
        avg = sum(y["v"] for y in b[i - 10:i]) / 10
        if x["v"] < vm * avg: continue
        hi = max(y["h"] for y in b[:i]); lo = min(y["l"] for y in b[:i])
        for side in (1, -1):
            if side in done: continue
            lvl = hi if side == 1 else lo
            past = (x["c"] - lvl) * side
            if not (0 < past <= band): continue
            trend = all((b[k]["c"] - vw[k]) * side > 0 for k in range(i - 5, i + 1)) and (vw[i] - vw[i - 12]) * side > 0
            stop = x["l"] if side == 1 else x["h"]; R = max(0.30, (x["c"] - stop) * side)
            stop = x["c"] - R * side; tgt = x["c"] + 1.5 * R * side; res = None
            for y in b[i + 1:]:
                if ((y["l"] if side == 1 else y["h"]) - stop) * side <= 0: res = -1.0; break
                if ((y["h"] if side == 1 else y["l"]) - tgt) * side >= 0: res = 1.5; break
                if y["t"] >= "15:00": res = (y["c"] - x["c"]) * side / R; break
            if res is not None:
                out.append((trend, res)); done.add(side)
    return out

if __name__ == "__main__":
    bars = load(sys.argv[1:]); days = sorted(bars)
    print(f"sessions {len(days)} ({days[0]}..{days[-1]})")
    halves = [("first half", days[: len(days) // 2]), ("second half", days[len(days) // 2:])]
    print(f"{'band':>5} {'vol':>4} | {'TREND n':>7} {'win':>4} {'sumR':>6} {'R/tr':>5} | {'RANGE n':>7} {'win':>4} {'sumR':>6} {'R/tr':>5} | trend R/tr by half")
    for band in (0.30, 0.75, 1.50, 2.50):
        for vm in (1.5, 1.2, 1.0):
            res = {True: [], False: []}; hres = []
            for d in days:
                for tr, r in day_signals(bars[d], band, vm): res[tr].append(r)
            for nm, ds in halves:
                rr = [r for d in ds for tr, r in day_signals(bars[d], band, vm) if tr]
                hres.append(f"{(sum(rr)/len(rr) if rr else 0):+.2f} (n={len(rr)})")
            f = lambda L: (len(L), (sum(1 for r in L if r > 0) / len(L) * 100 if L else 0), sum(L), (sum(L) / len(L) if L else 0))
            t, g = f(res[True]), f(res[False])
            print(f"{band:5.2f} {vm:4.1f} | {t[0]:7d} {t[1]:3.0f}% {t[2]:+6.1f} {t[3]:+5.2f} | {g[0]:7d} {g[1]:3.0f}% {g[2]:+6.1f} {g[3]:+5.2f} | " + " / ".join(hres))
