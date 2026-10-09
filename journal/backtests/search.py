"""Parameter search for setup F with option-priced P&L.

Protocol (to avoid fitting noise):
  1. Rank every combination on TRAIN (2026-03-23..07-15) only.
  2. Check the top TRAIN candidates on VALIDATION (07-16..10-08).
  3. Open the LOCKBOX (2026-02-23..03-20, never used before) once, for the single final pick.
Usage: python3 search.py data/spy_qqq_5min.csv [lockbox_csv]
"""
import itertools, sys
import bt, optbt

bars = bt.load(sys.argv[1])
days = sorted(d for d in bars["SPY"] if d in bars["QQQ"])
train = [d for d in days if d < bt.SPLIT]; valid = [d for d in days if d >= bt.SPLIT]

grid = dict(exit=[1.0, 1.5, 2.0], otm=[0, 1, 2], last=["13:55", "14:25"], sqz=[9, 12],
            sqzw=[1.5, 2.5], band=[0.10, 0.20], vol=["new", "old"], first_f=["11:00", "12:00"])
keys = list(grid)
rows = []
for combo in itertools.product(*grid.values()):
    p = dict(zip(keys, combo)); otm = p.pop("otm")
    F = dict(bt.DEFAULT, setups="F", **p)
    s = optbt.usd_stats(optbt.replay(bars, F, train, otm=otm, cap=100))
    rows.append((s, dict(p, otm=otm)))
print(f"combinations tried on TRAIN: {len(rows)}")
ok = [r for r in rows if r[0]["n"] >= 25]
ok.sort(key=lambda r: r[0]["avg"], reverse=True)
pos = sum(r[0]["usd"] > 0 for r in rows)
print(f"positive on TRAIN: {pos} of {len(rows)}; with n>=25: {len(ok)}\n")
print("TOP 12 on TRAIN -> checked on VALIDATION ($ per 1 contract)")
for s, p in ok[:12]:
    otm = p["otm"]; F = dict(bt.DEFAULT, setups="F", **{k: v for k, v in p.items() if k != "otm"})
    v = optbt.usd_stats(optbt.replay(bars, F, valid, otm=otm, cap=100))
    print(f"train n={s['n']:>3} avg=${s['avg']:+6.2f} PF={s['pf']:.2f} DD=${s['dd']:.0f} | valid n={v['n']:>3} "
          f"avg=${v['avg']:+6.2f} PF={v['pf']:.2f} DD=${v['dd']:.0f} | {p}")
base = dict(exit=1.5, otm=0, last="14:25", sqz=9, sqzw=2.5, band=0.10, vol="new", first_f="11:00")
for lab, dset in (("TRAIN", train), ("VALID", valid)):
    F = dict(bt.DEFAULT, setups="F", **{k: v for k, v in base.items() if k != "otm"})
    s = optbt.usd_stats(optbt.replay(bars, F, dset, otm=0, cap=100))
    print(f"\nCurrent F rules, {lab}: n={s['n']} win={s['win']*100:.0f}% avg=${s['avg']:+.2f} total=${s['usd']:+.0f} "
          f"PF={s['pf']:.2f} DD=${s['dd']:.0f} avgwin=${s['avgwin']:.0f} avgloss=${s['avgloss']:.0f}")
