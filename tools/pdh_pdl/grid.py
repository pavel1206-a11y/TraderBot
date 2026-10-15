from strat import *
from datetime import date
import itertools
def split(T):
    a=[t for t in T if date(2026,7,17)<=t[0]<=date(2026,8,31)]
    b=[t for t in T if date(2026,9,1)<=t[0]<=date(2026,10,15)]
    c=[t for t in T if t[0]<date(2026,7,17)]
    return a,b,c
res=[]
for pen,win,buf,stop,rr,qqq,ts in itertools.product([0.0,0.10,0.25],[3,6,12],[0.10,0.25,0.40],['ext','bar'],[1.0,1.5,2.0],[0,1],[None,6]):
    p=dict(pen=pen,win=win,buf=buf,stop=stop,rr=rr,qqq=qqq,ts=ts,maxR=2.5)
    res.append(('sweep_vwap',p,split(run(sweep_vwap,p))))
for tol,buf,rr,ts in itertools.product([0.10,0.20,0.35],[0.10,0.25,0.40],[1.0,1.5,2.0],[None,6]):
    p=dict(tol=tol,buf=buf,rr=rr,ts=ts,maxR=2.5)
    res.append(('brk_retest',p,split(run(brk_retest,p))))
for tol,buf,rr,ts in itertools.product([0.05,0.15,0.30],[0.10,0.25,0.40],[1.0,1.5,2.0],[None,6]):
    p=dict(tol=tol,buf=buf,rr=rr,ts=ts,maxR=2.5)
    res.append(('reject',p,split(run(reject,p))))
good=[]
for name,p,(a,b,c) in res:
    sa,sb,sc=stats(a),stats(b),stats(c)
    if sa[0]>=8 and sb[0]>=8 and sa[2]>0.5 and sb[2]>0.5 and sa[3]>0 and sb[3]>0:
        good.append((sb[4]+sa[4],name,p,sa,sb,sc))
good.sort(key=lambda x:-x[0])
print(len(res),'variants;',len(good),'pass train+test')
f=lambda s:f"{s[0]}t {s[1]}W {s[2]*100:.0f}% {s[3]:+.1f}R ({s[4]:+.2f}/t)"
for g in good[:25]: print(g[1],g[2],'| train',f(g[3]),'| test',f(g[4]),'| early',f(g[5]))
# best per family regardless
for fam in ('sweep_vwap','brk_retest','reject'):
    X=[(stats(a+b)[3],p,stats(a+b),stats(c)) for n,p,(a,b,c) in res if n==fam]
    X.sort(key=lambda x:-x[0]); print('BEST',fam,X[0][1],f(X[0][2]),'| early',f(X[0][3]))
