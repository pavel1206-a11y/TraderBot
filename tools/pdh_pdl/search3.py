from s3 import *
import itertools,random,json
D0,D1=date(2026,2,3),date(2026,6,30);V0,V1=date(2026,7,1),date(2026,10,15)
exits=[('R',2.0),('R',3.0),('R',4.0),('vwap',),('trail',1.0),('trail',2.0),('eod',)]
common=dict(exit=exits,be=[None,1.0],buf=[0.05,0.15,0.3],q=[0,1])
grids=dict(
 orb=dict(n=[3,6,12],stop=['bar','2bar','vwap'],last=[11*60,12*60+30],vol=[None,1.2],maxor=[None,3.0],**common),
 pdbrk=dict(stop=['bar','2bar','lvl','vwap'],last=[11*60,14*60],vol=[None,1.2],**common),
 reclaim=dict(stop=['bar','2bar','vwap'],last=[11*60,14*60],**common),
 squeeze=dict(N=[9,12,18],W=[1.0,1.5,2.0],stop=['bar','2bar','lvl'],last=[14*60],vol=[None,1.5],**common),
)
res=[]
for fam,g in grids.items():
    keys=list(g);combos=list(itertools.product(*g.values()));random.seed(2)
    if len(combos)>5000: combos=random.sample(combos,5000)
    for vals in combos:
        p=dict(zip(keys,vals))
        s=st(run(FAM[fam],p,D0,D1))
        if s['n']>=25 and s['ratio']>=2.5 and s['exp']>=0.15 and s['pf']>=1.4: res.append((fam,p,s))
print('discovery hits',len(res))
out=[]
for fam,p,s in res:
    v=st(run(FAM[fam],p,V0,V1))
    out.append((fam,p,s,v))
json.dump([[a,b] for a,b,_,_ in out],open('hits3.json','w'),default=str)
good=[o for o in out if o[3].get('n',0)>=15 and o[3]['ratio']>=2.5 and o[3]['exp']>=0.15 and o[3]['pf']>=1.4]
print('pass held-out',len(good))
f=lambda s:f"{s['n']}t wr{s['wr']*100:.0f}% win{ s['aw']:.2f}R loss{s['al']:.2f}R ratio{s['ratio']:.1f} exp{s['exp']:+.2f}R PF{s['pf']:.2f}"
good.sort(key=lambda o:-(o[2]['exp']+o[3]['exp']))
for o in good[:30]: print(o[0],{k:v for k,v in o[1].items() if v not in (None,0)},'\n   disc',f(o[2]),'\n   VALID',f(o[3]))
