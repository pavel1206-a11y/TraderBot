"""Search for a high-win-rate version of the first-candle breakout (owner ask 2026-10-10: "make it 80-90%").
Rank on TRAIN (Mar 23 - Jun 30) only, then check VALID (Jul 1 - Oct 8). 5-minute bars, 5-minute first candle.
A bar that touches both stop and target counts as a stop. Cost $0.02/share.
"""
import itertools, bt
from statistics import mean

bars = bt.load("data/spy_qqq_5min.csv")
S, Q = bars["SPY"], bars["QQQ"]
days = sorted(d for d in S if len(S[d]) >= 70 and d in Q)
COST = 0.02

def trade(d, prev, F):
    b, q = S[d], Q[d]
    H, L = b[0]["h"], b[0]["l"]
    gap = b[0]["o"] - S[prev][-1]["c"]
    sv = bt.vwap(b)
    for i in range(1, len(b)):
        x = b[i]
        if x["t"] > F["last"]:
            return None
        if F["entry"] == "touch":
            up, dn = x["h"] > H, x["l"] < L
            if up and dn:
                return dict(pnl=-(H - L) - COST, win=False)
            if not (up or dn):
                continue
            dr = 1 if up else -1; e = H + 0.01 if up else L - 0.01
        else:  # 5-min close beyond the candle
            if x["c"] > H: dr, e = 1, x["c"]
            elif x["c"] < L: dr, e = -1, x["c"]
            else: continue
        # filters, judged at the break
        if F["gap"] and gap * dr <= 0: return None                 # trade only in the gap's direction
        if F["qqq"] and (q[i]["c"] - q[0]["h" if dr > 0 else "l"]) * dr <= 0: return None  # QQQ also broke
        if F["vwap"] and (x["c"] - sv[i]) * dr <= 0: return None
        if F["maxw"] and H - L > F["maxw"]: return None
        stop = (L - 0.01 if dr > 0 else H + 0.01) if F["stop"] == "other" else (H + L) / 2
        risk = (e - stop) * dr
        if risk <= 0.05: return None
        tgt = e + dr * F["k"] * risk
        for j in range(i + 1, len(b)):
            y = b[j]
            if (y["l"] <= stop) if dr > 0 else (y["h"] >= stop):
                ex = stop; break
            if (y["h"] >= tgt) if dr > 0 else (y["l"] <= tgt):
                ex = tgt; break
            if y["t"] >= "15:55":
                ex = y["c"]; break
        else:
            ex = b[-1]["c"]
        pnl = (ex - e) * dr - COST
        return dict(pnl=pnl, win=pnl > 0, R=pnl / risk)
    return None

def run(F, ds):
    out = []
    for d in ds:
        k = days.index(d)
        if k == 0: continue
        t = trade(d, days[k - 1], F)
        if t: out.append(t)
    return out

def st(ts):
    if not ts: return dict(n=0, wr=0, net=0, avg=0)
    return dict(n=len(ts), wr=sum(t["win"] for t in ts) / len(ts), net=sum(t["pnl"] for t in ts), avg=mean(t["pnl"] for t in ts))

train = [d for d in days if d < "2026-07-01"]; valid = [d for d in days if d >= "2026-07-01"]
grid = dict(entry=["touch", "close"], k=[0.25, 0.5, 0.75, 1.0, 1.5], stop=["other", "mid"], gap=[False, True],
            qqq=[False, True], vwap=[False, True], maxw=[None, 1.0], last=["10:30", "15:00"])
rows = []
for c in itertools.product(*grid.values()):
    F = dict(zip(grid, c)); s = st(run(F, train)); rows.append((s, F))
print(f"{len(rows)} combinations, ranked on TRAIN ({len(train)} days), checked on VALID ({len(valid)} days)\n")
def show(title, sel):
    print(title)
    for s, F in sel:
        v = st(run(F, valid))
        print(f"  train n={s['n']:>3} win {s['wr']*100:3.0f}% net ${s['net']:+6.2f} | valid n={v['n']:>3} win {v['wr']*100:3.0f}% net ${v['net']:+6.2f} | "
              + ", ".join(f"{k}={F[k]}" for k in F))
hi = sorted([r for r in rows if r[0]["n"] >= 20], key=lambda r: -r[0]["wr"])
show("A) Highest win rate on TRAIN (n>=20), regardless of profit:", hi[:5])
hp = sorted([r for r in rows if r[0]["n"] >= 20 and r[0]["net"] > 0], key=lambda r: -r[0]["wr"])
show("\nB) Highest win rate on TRAIN among combos that also made money on TRAIN:", hp[:8])
print(f"\nCombos with win >= 80% AND net > 0 on TRAIN (n>=20): {sum(1 for s,_ in rows if s['n']>=20 and s['wr']>=0.8 and s['net']>0)}")
print(f"Combos with win >= 80% on TRAIN (n>=20), any profit: {sum(1 for s,_ in rows if s['n']>=20 and s['wr']>=0.8)}")
