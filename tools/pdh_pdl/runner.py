import sys; sys.path.insert(0,'.')
from eng import DAYS
def ema(cs,n=9):
    k=2/(n+1);e=None;o=[]
    for c in cs: e=c if e is None else c*k+e*(1-k); o.append(e)
    return o
def entries(side):
    out=[];prev=None
    for d,S,Q in DAYS:
        PH=PL=None
        if prev: PH=max(b['h'] for b in prev);PL=min(b['l'] for b in prev)
        prev=S
        E=ema([b['c'] for b in S])
        armed=False;swept=False;i=0
        while i<len(S):
            b=S[i];m=b['m']
            lo=min(x['l'] for x in S[:i+1]);hi=max(x['h'] for x in S[:i+1])
            if side>0:
                newext=b['l']<=lo; wrong=b['c']<b['vw']
                if PL and lo<PL-0.10: swept=True
            else:
                newext=b['h']>=hi; wrong=b['c']>b['vw']
                if PH and hi>PH+0.10: swept=True
            if 585<=m<=855 and newext and wrong: armed=True
            q=Q.get(m)
            if armed and i>=3 and m<=860 and q:
                avg=sum(x['v'] for x in S[max(0,i-10):i])/len(S[max(0,i-10):i])
                qp=Q.get(S[i-1]['m'])
                cond=(b['c']-b['vw'])*side>0.10 and (q['c']-q['vw'])*side>0
                qre=qp and (qp['c']-qp['vw'])*side<0 and (q['c']-q['vw'])*side>0
                if cond and (b['v']>=avg or (b['v']>=0.7*avg and qre)):
                    for j in range(i+1,min(i+7,len(S))):
                        c2=S[j]
                        if c2['m']>865: break
                        ok=(c2['l']>=c2['vw']-0.05 and c2['c']>c2['o']) if side>0 else (c2['h']<=c2['vw']+0.05 and c2['c']<c2['o'])
                        if ok:
                            e=c2['c'];st=c2['l']-0.10 if side>0 else c2['h']+0.10
                            out.append((d,S,E,j,side,e,st,swept));i=len(S);break
                    armed=False
            i+=1
    return out
def sim(t,mode):
    d,S,E,j,side,e,st,sw=t;R=abs(e-st);tg=e+1.5*R*side
    half=False;real=0;stop=st;peak=e
    for k in range(j+1,len(S)):
        x=S[k]
        if x['m']>=930: px=x['o'];return real+((px-e)*side/R)*(0.5 if half else 1)
        hit=(x['l']<=stop) if side>0 else (x['h']>=stop)
        if hit: return real+((stop-e)*side/R)*(0.5 if half else 1)
        if mode=='fixed':
            if (x['h']-tg)*side>=0 if side>0 else (tg-x['l'])>=0: return 1.5
            if k==j+6 and (x['c']-e)*side<=0: return (x['c']-e)*side/R
            continue
        if not half and ((x['h']>=tg) if side>0 else (x['l']<=tg)):
            if mode.startswith('half'): real=0.75;half=True
            else: half=False
            stop=e  # breakeven on runner
            started=True
        elif k==j+6 and stop==st and (x['c']-e)*side<=0: return (x['c']-e)*side/R
        # trail after target touched
        if stop!=st:
            if mode.endswith('vwap'):
                if (x['c']-x['vw'])*side<0: return real+((x['c']-e)*side/R)*(0.5 if half else 1)
            elif mode.endswith('ema'):
                if (x['c']-E[k])*side<0: return real+((x['c']-e)*side/R)*(0.5 if half else 1)
            elif mode.endswith('trail1R'):
                peak=max(peak,x['h']) if side>0 else min(peak,x['l'])
                ns=peak-R*side; stop=max(stop,ns) if side>0 else min(stop,ns)
    return real
import collections
for side,name in ((1,'LONG'),(-1,'SHORT')):
    T=entries(side)
    for sub,lab in ((T,'all VWAP reclaims'),([t for t in T if t[7]],'after a PDL/PDH sweep')):
        print(f"{name} {lab}: {len(sub)} trades")
        for mode in ('fixed','half_vwap','half_ema','half_trail1R','all_vwap','all_ema','all_trail1R'):
            r=[sim(t,mode) for t in sub]
            if not r: continue
            h1=sum(x for t,x in zip(sub,r) if t[0].month<=6);h2=sum(r)-h1
            w=sum(1 for x in r if x>0)
            print(f"   {mode:13s} win {w/len(r):.0%}  total {sum(r):+6.1f}R  avg {sum(r)/len(r):+.2f}R  best {max(r):+.1f}R  (Jan-Jun {h1:+.1f}, Jul-Oct {h2:+.1f})")
