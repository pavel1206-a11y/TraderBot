from eng import DAYS
from s3 import play2, COST
from datetime import date
# continuous EMA9 on 5-min closes (SPY and QQQ)
k=2/10;e=None;eq=None
for d,S,Q in DAYS:
    for b in S:
        e=b['c'] if e is None else e+k*(b['c']-e); b['ema']=e
    for m in sorted(Q):
        b=Q[m]; eq=b['c'] if eq is None else eq+k*(b['c']-eq); b['ema']=eq
def okq(Q,b,side,p):
    if not p.get('q'): return True
    q=Q.get(b['m']); 
    return bool(q) and ((q['c']>q['vw']) if side>0 else (q['c']<q['vw']))
def mk(S,j,side,st,p,d):
    e=S[j]['c'];R=abs(e-st)
    if R<p.get('minR',0.15) or R>p.get('maxR',2.0): return None
    return (d,play2(S,j,side,e,st,p),side,S[j]['t'].strftime('%H:%M'),R)
def stopf(S,j,side,p):
    b=S[j]
    if p['stop']=='bar': return b['l']-p['buf'] if side>0 else b['h']+p['buf']
    if p['stop']=='2bar': return (min(b['l'],S[j-1]['l'])-p['buf']) if side>0 else (max(b['h'],S[j-1]['h'])+p['buf'])
    if p['stop']=='vwap': return b['vw']-p['buf'] if side>0 else b['vw']+p['buf']
# A: EMA9 crosses VWAP
def cross(d,S,Q,p):
    out=[];n=0
    for j in range(2,len(S)):
        b=S[j];a=S[j-1]
        if b['m']<p['first'] or b['m']>p['last']: continue
        for side in (1,-1):
            if p.get('only') and p['only']!=side: continue
            c=(a['ema']<=a['vw'] and b['ema']>b['vw'] and b['c']>b['ema']) if side>0 else (a['ema']>=a['vw'] and b['ema']<b['vw'] and b['c']<b['ema'])
            if c and okq(Q,b,side,p):
                t=mk(S,j,side,stopf(S,j,side,p),p,d)
                if t: out.append(t); n+=1
                if n>=p['maxn']: return out
    return out
# B: pullback to EMA9 in an EMA>VWAP trend
def pull(d,S,Q,p):
    out=[];n=0;last=-99
    for j in range(3,len(S)):
        b=S[j]
        if b['m']<p['first'] or b['m']>p['last'] or j-last<6: continue
        for side in (1,-1):
            if p.get('only') and p['only']!=side: continue
            trend=(b['ema']>b['vw']+p['gap'] and b['ema']>S[j-3]['ema'] and b['c']>b['vw']) if side>0 else (b['ema']<b['vw']-p['gap'] and b['ema']<S[j-3]['ema'] and b['c']<b['vw'])
            touch=(b['l']<=b['ema']+p['tol'] and b['c']>b['ema'] and b['c']>b['o']) if side>0 else (b['h']>=b['ema']-p['tol'] and b['c']<b['ema'] and b['c']<b['o'])
            if trend and touch and okq(Q,b,side,p):
                t=mk(S,j,side,stopf(S,j,side,p),p,d)
                if t: out.append(t);n+=1;last=j
                if n>=p['maxn']: return out
    return out
# C: pullback to VWAP while EMA9 stays on the trend side, close back over EMA9
def vpull(d,S,Q,p):
    out=[];n=0;last=-99
    for j in range(3,len(S)):
        b=S[j]
        if b['m']<p['first'] or b['m']>p['last'] or j-last<6: continue
        for side in (1,-1):
            if p.get('only') and p['only']!=side: continue
            c=(b['ema']>b['vw'] and b['l']<=b['vw']+p['tol'] and b['c']>b['ema'] and b['c']>b['o']) if side>0 else (b['ema']<b['vw'] and b['h']>=b['vw']-p['tol'] and b['c']<b['ema'] and b['c']<b['o'])
            if c and okq(Q,b,side,p):
                t=mk(S,j,side,stopf(S,j,side,p),p,d)
                if t: out.append(t);n+=1;last=j
                if n>=p['maxn']: return out
    return out
FAM=dict(cross=cross,pull=pull,vpull=vpull)
def run(fn,p,lo,hi):
    T=[]
    for d,S,Q in DAYS:
        if lo<=d<=hi: T+=fn(d,S,Q,p)
    return T
def st(T):
    n=len(T)
    if not n: return dict(n=0,wr=0,exp=0,pf=0,R=0,aw=0,al=0)
    W=[t[1] for t in T if t[1]>0];L=[t[1] for t in T if t[1]<=0]
    return dict(n=n,wr=len(W)/n,R=sum(t[1] for t in T),exp=sum(t[1] for t in T)/n,pf=(sum(W)/-sum(L)) if L and sum(L)<0 else 99,
                usd=sum(t[1]*t[4] for t in T),aw=(sum(t[1]*t[4] for t in T if t[1]>0)/len(W)) if W else 0,al=(sum(t[1]*t[4] for t in T if t[1]<=0)/len(L)) if L else 0)
