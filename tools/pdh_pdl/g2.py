from strat import *
from datetime import date
import itertools
f=lambda s:f"{s[0]}t {s[1]}W {s[2]*100:.0f}% {s[3]:+.1f}R ({s[4]:+.2f}/t)"
rows=[]
for pen,win,buf,stop,rr,qqq,ts in itertools.product([0.0,0.10,0.25],[6,12,24],[0.25,0.40,0.60],['ext','bar'],[1.0,1.5,2.0],[0,1],[None,6]):
    p=dict(pen=pen,win=win,buf=buf,stop=stop,rr=rr,qqq=qqq,ts=ts,maxR=2.5)
    T=run(sweep_vwap,p)
    a=[t for t in T if t[0]>=date(2026,7,17)];c=[t for t in T if t[0]<date(2026,7,17)]
    h1=[t for t in a if t[0]<=date(2026,8,31)];h2=[t for t in a if t[0]>date(2026,8,31)]
    sa,s1,s2,sc=stats(a),stats(h1),stats(h2),stats(c)
    if all(s[3]>0 for s in (s1,s2,sc)) and sa[0]>=15:
        rows.append((sa[2],sa[4],p,sa,s1,s2,sc))
rows.sort(key=lambda r:(-r[0],-r[1]))
print(len(rows),'robust variants (positive in all 3 periods)')
for r in rows[:15]: print(r[2],'| 90d',f(r[3]),'| h1',f(r[4]),'| h2',f(r[5]),'| early',f(r[6]))
