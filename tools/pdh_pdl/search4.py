from s4 import *
import itertools,random,json
D0,D1=date(2026,1,5),date(2026,6,30);V0,V1=date(2026,7,1),date(2026,10,15)
ex=[('R',1.0),('R',1.5),('R',2.0),('R',3.0),('vwap',),('trail',1.0),('eod',)]
com=dict(exit=ex,be=[None,1.0],buf=[0.05,0.15,0.3],q=[0,1],only=[None,1,-1],maxn=[1,3],first=[9*60+45,10*60+15],last=[11*60+30,14*60+25])
grids=dict(cross=dict(stop=['bar','2bar','vwap'],**com),
           pull=dict(stop=['bar','2bar','vwap'],gap=[0.0,0.25,0.5],tol=[0.0,0.10],**com),
           vpull=dict(stop=['bar','2bar','vwap'],tol=[0.0,0.10],**com))
res=[]
for fam,g in grids.items():
    keys=list(g);cs=list(itertools.product(*g.values()));random.seed(4)
    if len(cs)>6000: cs=random.sample(cs,6000)
    for v in cs:
        p=dict(zip(keys,v));s=st(run(FAM[fam],p,D0,D1))
        if s['n']>=30 and s['exp']>=0.15 and s['pf']>=1.4 and s['usd']>0: res.append((fam,p,s))
print('discovery passes',len(res))
good=[]
for fam,p,s in res:
    v=st(run(FAM[fam],p,V0,V1))
    if v['n']>=20 and v['exp']>=0.10 and v['pf']>=1.3 and v['usd']>0: good.append((fam,p,s,v))
print('pass held-out',len(good))
json.dump([[f,p] for f,p,_,_ in good],open('hits4.json','w'),default=str)
f=lambda s:f"{s['n']}t wr{s['wr']*100:.0f}% exp{s['exp']:+.2f}R PF{s['pf']:.2f} ${s['usd']:+.1f}/sh (win ${s['aw']:+.2f} loss ${s['al']:+.2f})"
good.sort(key=lambda o:-(min(o[2]['exp'],o[3]['exp'])))
for o in good[:25]: print(o[0],{k:v for k,v in o[1].items() if v not in (None,0)},'\n  disc',f(o[2]),'\n  VALID',f(o[3]))
from collections import Counter
print(Counter(o[0] for o in good))
