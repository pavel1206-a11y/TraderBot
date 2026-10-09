"""Mechanical backtest of the playbook setups on SPY 5-min bars (QQQ as the confirm filter).

Usage:  python3 bt.py data/spy_qqq_5min.csv
Results are in SPY points and R (multiples of risk), net of a per-trade cost.
Setups: A (ORB), B (VWAP pullback), C (break and retest), E (close through a level),
F (45-min squeeze break). D is not modeled (not mechanical; it lost in the 10/6 replay).
Rules shared by every variant: entries 9:45-14:25 (bar close), one position at a time,
max 3 trades a day, stop after 2 losing trades, flat at 15:30, stop wins a tie with the target.
"""
import csv, sys
from collections import defaultdict

COST = 0.04          # SPY points per round trip (slippage on market entry + exit)
SPLIT = "2026-07-16"  # train < SPLIT <= test

def load(path):
    bars = defaultdict(lambda: defaultdict(list))
    for r in csv.DictReader(open(path)):
        d, t = r["et"].split()
        if not ("09:30" <= t <= "15:55"):
            continue
        bars[r["symbol"]][d].append(dict(t=t, o=float(r["o"]), h=float(r["h"]), l=float(r["l"]),
                                         c=float(r["c"]), v=int(float(r["v"]))))
    return bars

def vwap(bs):
    out, pv, vv = [], 0.0, 0
    for b in bs:
        pv += (b["h"] + b["l"] + b["c"]) / 3 * b["v"]; vv += max(b["v"], 1); out.append(pv / vv)
    return out

DEFAULT = dict(setups="ABCEF", vol="new", bcap=False, band=0.10, exit=1.5, climax=None, qqq=True, room=1.5,
               sqz=9, sqzw=2.5, last="14:25", first_f="11:00")

def sim_day(S, Q, prev, F):
    if len(S) < 70 or len(Q) != len(S):
        return []
    sv, qv = vwap(S), vwap(Q)
    H, L, C = max(b["h"] for b in prev), min(b["l"] for b in prev), prev[-1]["c"]
    P = (H + L + C) / 3
    base = [H, L, C, P, 2 * P - L, 2 * P - H, P + (H - L), P - (H - L)]
    orh = max(b["h"] for b in S[:3]); orl = min(b["l"] for b in S[:3])
    qorh = max(b["h"] for b in Q[:3]); qorl = min(b["l"] for b in Q[:3])
    or_avg = sum(b["v"] for b in S[:3]) / 3
    trades, pos, losses = [], None, 0
    broken = []  # (level, dir, bar index) for setup C
    for i in range(3, len(S)):
        b, p = S[i], S[i - 1]
        if pos:
            d = pos["dir"]
            hit_s = (b["l"] <= pos["stop"]) if d > 0 else (b["h"] >= pos["stop"])
            hit_t = (b["h"] >= pos["tgt"]) if d > 0 else (b["l"] <= pos["tgt"])
            ex = pos["stop"] if hit_s else pos["tgt"] if hit_t else (b["c"] if b["t"] >= "15:25" else None)
            if ex is not None:
                pnl = (ex - pos["entry"]) * d - COST
                pos.update(exit=ex, xt=b["t"], pnl=pnl, R=pnl / pos["risk"])
                trades.append(pos); losses += pnl < 0; pos = None
            continue
        avg10 = sum(x["v"] for x in S[max(0, i - 10):i]) / min(10, i)
        vr = b["v"] / max(avg10, 1)
        atr = sum(x["h"] - x["l"] for x in S[max(0, i - 14):i]) / min(14, i)
        dayhi = max(x["h"] for x in S[:i]); daylo = min(x["l"] for x in S[:i])
        keys = base + [orh, orl]
        win = S[i - F["sqz"]:i] if i >= F["sqz"] else None
        rng = (max(x["h"] for x in win), min(x["l"] for x in win)) if win else None
        qwin = Q[i - 9:i] if i >= 9 else None
        qrng = (max(x["h"] for x in qwin), min(x["l"] for x in qwin)) if qwin else None
        # remember fresh level breaks for C (before entry filters, so C can catch gap-throughs)
        for k in keys:
            for dr in (1, -1):
                if (b["c"] - k) * dr > 0 and (p["c"] - k) * dr <= 0:
                    broken.append((k, dr, i))
        broken = [x for x in broken if i - x[2] <= 12]
        if not ("09:45" <= b["t"] <= F["last"]) or len(trades) >= 3 or losses >= 2:
            continue
        cands = []
        for dr in (1, -1):
            above = lambda x, y: (x - y) * dr > 0
            q_ok = above(Q[i]["c"], qv[i]) if F["qqq"] else True
            q_brk = qrng is not None and above(Q[i]["c"], qrng[0] if dr > 0 else qrng[1])
            if F["vol"] == "new":
                vol_ok = vr >= 1.0 or (vr >= 0.7 and q_brk)
            else:
                vol_ok = vr >= 1.5
            climax_bad = F["climax"] is not None and abs(b["c"] - sv[i]) > F["climax"] * atr
            nxt = [k for k in keys + [dayhi, daylo] if above(k, b["c"] + 0.05 * dr)]
            nxt_lvl = (min(nxt) if dr > 0 else max(nxt)) if nxt else None
            if "A" in F["setups"] and b["t"] <= "10:30":
                edge = orh if dr > 0 else orl
                if above(b["c"], edge) and not above(p["c"], edge) and abs(b["c"] - edge) <= F["band"] \
                        and above(b["c"], sv[i]) and q_ok:
                    vA = b["v"] >= or_avg or (F["vol"] == "new" and b["v"] >= 0.7 * or_avg
                                              and above(Q[i]["c"], qorh if dr > 0 else qorl))
                    if vA:
                        stop = (orl - 0.10 if dr > 0 else orh + 0.10) if orh - orl <= 1.5 else (orh + orl) / 2
                        cands.append(("A", dr, stop, nxt_lvl))
            if "B" in F["setups"] and i >= 6 and all(above(S[j]["c"], sv[j]) for j in range(i - 3, i)) \
                    and abs(b["l" if dr > 0 else "h"] - sv[i]) <= 0.10 and above(b["c"], sv[i]) \
                    and above(b["c"], p["c"]) and q_ok and (not F["bcap"] or abs(b["c"] - sv[i]) <= 0.15):
                ext = b["l"] if dr > 0 else b["h"]
                stop = (min(ext, sv[i]) - 0.30) if dr > 0 else (max(ext, sv[i]) + 0.30)
                cands.append(("B", dr, stop, nxt_lvl))
            if "C" in F["setups"] and not climax_bad:
                for k, kd, j in broken:
                    if kd != dr or j >= i:
                        continue
                    ext = b["l"] if dr > 0 else b["h"]
                    if abs(ext - k) <= 0.10 and above(b["c"], k) and vr >= 1.0 and q_ok:
                        stop = (min(k - 0.30, ext - 0.15)) if dr > 0 else (max(k + 0.30, ext + 0.15))
                        cands.append(("C", dr, stop, nxt_lvl)); break
            if not climax_bad and vol_ok and q_ok:
                tests = []
                if "E" in F["setups"]:
                    tests += [(k, "E") for k in keys + [sv[i]]]
                if "F" in F["setups"] and b["t"] >= F["first_f"] and rng and rng[0] - rng[1] < F["sqzw"]:
                    tests.append((rng[0] if dr > 0 else rng[1], "F"))
                for k, nm in tests:
                    if above(b["c"], k) and not above(p["c"], k) and abs(b["c"] - k) <= F["band"]:
                        if nm == "F":
                            mid = (rng[0] + rng[1]) / 2
                            far = b["l"] if dr > 0 else b["h"]
                            stop = max(mid - 0.10, far - 0.10) if dr > 0 else min(mid + 0.10, far + 0.10)
                        else:
                            stop = k - 0.40 * dr
                        cands.append((nm, dr, stop, nxt_lvl)); break
        for name, dr, stop, nl in cands:
            risk = (b["c"] - stop) * dr
            if risk <= 0.10 or risk > 1.50:
                continue
            room = (nl - b["c"]) * dr / risk if nl is not None else 99
            if room < F["room"] or (F["exit"] == "level" and nl is None):
                continue
            tgt = b["c"] + dr * F["exit"] * risk if F["exit"] != "level" else nl
            pos = dict(t=b["t"], setup=name, dir=dr, entry=b["c"], stop=stop, tgt=tgt, risk=risk, vr=vr)
            break
    return trades

def run(bars, F, days):
    out = []
    for k, d in enumerate(days):
        if k == 0 or d not in bars["QQQ"]:
            continue
        for t in sim_day(bars["SPY"][d], bars["QQQ"][d], bars["SPY"][days[k - 1]], F):
            t["day"] = d; out.append(t)
    return out

def stats(ts):
    if not ts:
        return dict(n=0, win=0, R=0.0, avgR=0.0, pts=0.0, pf=0.0, maxdd=0.0)
    w = [t for t in ts if t["R"] > 0]
    gw = sum(t["R"] for t in w); gl = -sum(t["R"] for t in ts if t["R"] <= 0)
    eq = peak = dd = 0.0
    for t in ts:
        eq += t["R"]; peak = max(peak, eq); dd = max(dd, peak - eq)
    return dict(n=len(ts), win=len(w) / len(ts), R=sum(t["R"] for t in ts), avgR=sum(t["R"] for t in ts) / len(ts),
                pts=sum(t["pnl"] for t in ts), pf=gw / gl if gl else 99, maxdd=dd)

def fmt(label, s):
    return (f"{label:<44} n={s['n']:>3}  win={s['win']*100:4.0f}%  R={s['R']:+6.1f}  avg={s['avgR']:+.2f}R  "
            f"PF={s['pf']:4.2f}  maxDD={s['maxdd']:4.1f}R  pts={s['pts']:+6.2f}")

if __name__ == "__main__":
    bars = load(sys.argv[1])
    days = sorted(d for d in bars["SPY"] if d in bars["QQQ"])
    train = [d for d in days if d < SPLIT]; test = [d for d in days if d >= SPLIT]
    print(f"days: {len(days)} ({days[0]} to {days[-1]}); train {len(train)}, test {len(test)}; cost {COST} pts/trade\n")
    variants = [
        ("Current playbook (10/8 rules)", {}),
        ("Old volume rule (1.5x)", dict(vol="old")),
        ("B close cap back on", dict(bcap=True)),
        ("Exit at +1.0R", dict(exit=1.0)),
        ("Exit at +2.0R", dict(exit=2.0)),
        ("Exit at next level", dict(exit="level")),
        ("Band $0.20", dict(band=0.20)),
        ("No QQQ filter", dict(qqq=False)),
        ("Climax filter 2.0 ATR", dict(climax=2.0)),
        ("Climax filter 3.0 ATR", dict(climax=3.0)),
        ("Room check 1.0R", dict(room=1.0)),
    ]
    for s in "ABCEF":
        variants.append((f"Only setup {s}", dict(setups=s)))
    print(f"{'':44} --- TRAIN ({train[0]} to {train[-1]}) ---")
    res = {}
    for label, kw in variants:
        F = dict(DEFAULT, **kw)
        res[label] = (run(bars, F, train), run(bars, F, test))
        print(fmt(label, stats(res[label][0])))
    print(f"\n{'':44} --- TEST ({test[0]} to {test[-1]}) ---")
    for label, kw in variants:
        print(fmt(label, stats(res[label][1])))
    if len(sys.argv) > 2:
        F = dict(DEFAULT, **eval(sys.argv[2]))
        for t in run(bars, F, days):
            print(f"{t['day']} {t['t']} {t['setup']} {'L' if t['dir']>0 else 'S'} in {t['entry']:.2f} "
                  f"stop {t['stop']:.2f} tgt {t['tgt']:.2f} -> {t['exit']:.2f} @{t['xt']} {t['R']:+.2f}R")
