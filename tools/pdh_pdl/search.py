from s2 import *
import itertools,random
D0,D1=date(2026,2,3),date(2026,6,30)   # discovery
V0,V1=date(2026,7,1),date(2026,10,15)  # validation (held out)
grids=dict(
 sweep=dict(pen=[0.0,0.1,0.25,0.5],win=[6,12,24],buf=[0.1,0.25,0.4,0.6,1.0],rr=[0.5,0.75,1.0],qqq=[0,1],ts=[None,6],only=[None,1,-1],trend=[None,'with','against'],stopext=[0,1],last=[11*60,14*60+25]),
 gapfade=dict(g=[0.5,1.0,2.0,3.0],beyond=[0,1],orb=[1,3,6],buf=[0.1,0.25,0.5],rr=[0.5,0.75,1.0],frac=[None,0.25,0.5],ts=[None,6],only=[None,1,-1],trend=[None,'with','against'],last=[10*60+30,12*60]),
 vwaprev=dict(k=[1.0,1.5,2.0,3.0],buf=[0.1,0.25,0.5],rr=[0.5,0.75,1.0],frac=[None,0.5,1.0],ts=[None,6],only=[None,1,-1],trend=[None,'with','against'],last=[12*60,14*60+25]),
 retest=dict(tol=[0.1,0.2,0.35],buf=[0.1,0.25,0.4,0.6,1.0],rr=[0.5,0.75,1.0],ts=[None,6],only=[None,1,-1],trend=[None,'with','against'],last=[11*60,14*60+25]),
)
res=[]
for fam,g in grids.items():
    keys=list(g);combos=list(itertools.product(*g.values()))
    random.seed(1)
    if len(combos)>6000: combos=random.sample(combos,6000)
    for vals in combos:
        p=dict(zip(keys,vals))
        if p.get('frac') and p.get('rr')!=keys and fam!='sweep' and p['rr']!=1.0: continue  # frac overrides rr; avoid dupes
        T=run(FAM[fam],p,D0,D1);s=st(T)
        if s[0]>=20 and s[2]>=0.80 and s[3]>0: res.append((s[2],s[3],fam,p,s))
res.sort(key=lambda r:(-r[0],-r[1]))
print('discovery hits (>=20 trades, >=80%, net>0):',len(res))
import json
json.dump([[r[2],r[3]] for r in res],open('hits.json','w'),default=str)
for r in res[:30]: print(r[2],r[3],r[4])
