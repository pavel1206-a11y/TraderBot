"""Replay paper days 9/29-10/6 with OLD vs NEW trigger rules (SPY points, 1 unit)."""
import json, sys
from datetime import datetime, timedelta
from collections import defaultdict

d = json.load(open(sys.argv[1]))
bars = {}
for r in d["data"]["results"]:
    byday = defaultdict(list)
    for b in r["bars"]:
        t = datetime.fromisoformat(b["begins_at"].replace("Z", "+00:00")) - timedelta(hours=4)
        byday[t.date().isoformat()].append(dict(t=t.strftime("%H:%M"), o=float(b["open_price"]),
            h=float(b["high_price"]), l=float(b["low_price"]), c=float(b["close_price"]), v=b["volume"]))
    bars[r["symbol"]] = dict(byday)

DAYS = ["2026-09-29", "2026-09-30", "2026-10-01", "2026-10-02", "2026-10-05", "2026-10-06"]
alldays = sorted(bars["SPY"])

def vwap(bs):
    out, pv, vv = [], 0.0, 0
    for b in bs:
        pv += (b["h"] + b["l"] + b["c"]) / 3 * b["v"]; vv += b["v"]; out.append(pv / vv)
    return out

def levels_for(day):
    prev = alldays[alldays.index(day) - 1]
    pb = bars["SPY"][prev]
    H, L, C = max(b["h"] for b in pb), min(b["l"] for b in pb), pb[-1]["c"]
    P = (H + L + C) / 3
    return [H, L, C, P, 2*P - L, 2*P - H, P + (H - L), P - (H - L)]

def sim(day, F):
    new = True
    S, Q = bars["SPY"][day], bars["QQQ"][day]
    sv, qv = vwap(S), vwap(Q)
    lv = levels_for(day)
    orh = max(b["h"] for b in S[:3]); orl = min(b["l"] for b in S[:3])
    qorh = max(b["h"] for b in Q[:3]); qorl = min(b["l"] for b in Q[:3])
    or_avg = sum(b["v"] for b in S[:3]) / 3
    trades, pos, losses = [], None, 0
    for i in range(3, len(S)):
        b, p = S[i], S[i - 1]
        # manage open position
        if pos:
            if pos["dir"] > 0:
                hit_s, hit_t = b["l"] <= pos["stop"], b["h"] >= pos["tgt"]
            else:
                hit_s, hit_t = b["h"] >= pos["stop"], b["l"] <= pos["tgt"]
            ex = None
            if hit_s: ex = pos["stop"]
            elif hit_t: ex = pos["tgt"]
            elif b["t"] >= "15:25": ex = b["c"]
            if ex is not None:
                pnl = (ex - pos["entry"]) * pos["dir"]
                pos.update(exit=ex, xt=b["t"], pnl=round(pnl, 2), R=round(pnl / pos["risk"], 2))
                trades.append(pos); losses += pnl < 0; pos = None
            continue
        if not ("09:45" <= b["t"] <= "14:25") or len(trades) >= 3 or losses >= 2:
            continue
        avg10 = sum(x["v"] for x in S[max(0, i - 10):i]) / min(10, i)
        vr = b["v"] / avg10
        dayhi = max(x["h"] for x in S[:i]); daylo = min(x["l"] for x in S[:i])
        keys = lv + [orh, orl, dayhi, daylo]
        win = S[i - 9:i] if i >= 9 else None
        rng = (max(x["h"] for x in win), min(x["l"] for x in win)) if win else None
        qwin = Q[i - 9:i] if i >= 9 else None
        qrng = (max(x["h"] for x in qwin), min(x["l"] for x in qwin)) if qwin else None
        cands = []
        for dr in (1, -1):
            above = lambda x, y: (x - y) * dr > 0
            q_ok = above(Q[i]["c"], qv[i])
            nxt = [k for k in keys if above(k, b["c"] + 0.05 * dr)]
            nxt_lvl = (min(nxt) if dr > 0 else max(nxt)) if nxt else None
            # A: opening-range breakout until 10:30
            edge = orh if dr > 0 else orl
            if b["t"] <= "10:30" and above(b["c"], edge) and not above(p["c"], edge) and above(b["c"], sv[i]) and q_ok:
                vol_ok = b["v"] >= or_avg or (F['vol'] and b["v"] >= 0.7 * or_avg and above(Q[i]["c"], qorh if dr > 0 else qorl))
                if vol_ok:
                    w = orh - orl
                    stop = (orl - 0.10 if dr > 0 else orh + 0.10) if w <= 1.5 else (orh + orl) / 2
                    tg = nxt_lvl
                    if F['tgt']: tg = max([x for x in [tg, b["c"] + dr * w] if x is not None], key=lambda x: x * dr)
                    cands.append(("A ORB", dr, stop, tg))
            # B: VWAP pullback with the prior 3 closes on the trend side
            if all(above(S[j]["c"], sv[j]) for j in range(i - 3, i)) and abs(b["l" if dr > 0 else "h"] - sv[i]) <= 0.10 \
               and above(b["c"], sv[i]) and above(b["c"], p["c"]) and q_ok:
                if F['nocap'] or abs(b["c"] - sv[i]) <= 0.15:
                    ext = b["l"] if dr > 0 else b["h"]
                    stop = (min(ext, sv[i]) - 0.30) if dr > 0 else (max(ext, sv[i]) + 0.30)
                    cands.append(("B VWAP pullback", dr, stop, nxt_lvl))
            # E/F: fresh close through a key level or a 45-min range edge (< $2.50 wide)
            lvls = [(k, "level") for k in keys]
            if rng and rng[0] - rng[1] < 2.5:
                lvls.append((rng[0] if dr > 0 else rng[1], "range"))
            for k, kind in lvls:
                if above(b["c"], k) and not above(p["c"], k):
                    q_brk = qrng is not None and above(Q[i]["c"], qrng[0] if dr > 0 else qrng[1])
                    vok = (vr >= 1.0 or (vr >= 0.7 and q_brk)) if F['vol'] else vr >= 1.5
                    bok = abs(b["c"] - k) <= (F["band"] if F["nocap"] else 0.10)
                    qok2 = q_ok if F['vol'] else (q_brk if kind == "range" else q_ok)
                    ok = vok and bok and qok2
                    if ok:
                        stop = k - F['buf'] * dr
                        tg = nxt_lvl
                        if F['tgt'] and rng:
                            tg = max([x for x in [tg, b["c"] + dr * (rng[0] - rng[1])] if x is not None], key=lambda x: x * dr)
                        cands.append(("E/F break " + kind, dr, stop, tg))
                        break
            # D (new only): sweep beyond VWAP within the last 4 bars, then a close back across it
            if F['D'] and not above(p["c"], sv[i - 1]) and above(b["c"], sv[i]) and q_ok:
                look = S[max(0, i - 4):i]
                sweep = min(x["l"] for x in look) if dr > 0 else max(x["h"] for x in look)
                if abs(sweep - sv[i]) >= 0.30 and (sweep < sv[i]) == (dr > 0):
                    cands.append(("D sweep-reclaim", dr, sweep - 0.15 * dr, nxt_lvl))
        for name, dr, stop, tg in cands:
            risk = (b["c"] - stop) * dr
            if tg is None or risk <= 0.05: continue
            rr = (tg - b["c"]) * dr / risk
            if rr >= 1.5:
                if F.get('scalp'): tg = b["c"] + dr * F['scalp'] * risk
                pos = dict(day=day, t=b["t"], setup=name, dir=dr, entry=b["c"], stop=round(stop, 2), tgt=round(tg, 2),
                           risk=risk, rr=round(rr, 2), vr=round(vr, 2))
                break
    return trades


BASE=dict(band=0.6,scalp=0,vol=False,nocap=False,tgt=False,D=False,buf=0.40)
def run(label,**kw):
    F=dict(BASE,**kw); allt=[]
    for day in DAYS: allt+=sim(day,F)
    w=[t for t in allt if t["pnl"]>0]
    print(f"{label:<34} {len(allt):>2} trades {len(w):>2} wins  {sum(t['pnl'] for t in allt):+6.2f} pts  {sum(t['R'] for t in allt):+6.2f}R")
    return allt
for sc in (1.0,1.5):
  for bd in (0.10,0.20,0.30,0.60):
    run(f"VOL band {bd:.2f} exit {sc}R", scalp=sc, vol=True, nocap=True, band=bd)
import sys
if len(sys.argv)>2:
    for t in run("DETAIL",**eval(sys.argv[2])):
        print(f"  {t['day'][5:]} {t['t']} {'L' if t['dir']>0 else 'S'} {t['setup']:<18} in {t['entry']:.2f} stop {t['stop']:.2f} tgt {t['tgt']:.2f} vol {t['vr']}x -> {t['exit']:.2f} @{t['xt']} {t['pnl']:+.2f} ({t['R']:+.2f}R)")
