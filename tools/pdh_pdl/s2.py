from eng import DAYS,play
from datetime import date
COST=0.02  # $ per trade on SPY (spread+slippage), charged against R
def ctx(i):
    d,S,Q=DAYS[i];_,P,_=DAYS[i-1]
    return dict(d=d,S=S,Q=Q,PDH=max(b['h'] for b in P),PDL=min(b['l'] for b in P),PDC=P[-1]['c'],PDO=P[0]['o'],
                closes=[DAYS[k][1][-1]['c'] for k in range(max(0,i-20),i)])
def finish(c,j,side,e,st,p,tgt_price=None):
    S=c['S'];R=abs(e-st)
    if R<p.get('minR',0.15) or R>p.get('maxR',3.0): return None
    tg=tgt_price if tgt_price is not None else e+side*p['rr']*R
    r,why=play(S,j,side,e,st,tg,p.get('ts'))
    r-=COST/R
    return (c['d'],r,why,side,S[j]['t'].strftime('%H:%M'))
def trend_ok(c,side,p):
    f=p.get('trend')
    if not f: return True
    sma=sum(c['closes'])/len(c['closes'])
    up=c['PDC']>sma
    return (up if f=='with' else not up) if side>0 else ((not up) if f=='with' else up)

# 1 sweep + VWAP reclaim
def sweep(c,p):
    S,Q=c['S'],c['Q'];out=[]
    for side,lvl in ((1,c['PDL']),(-1,c['PDH'])):
        if p.get('only') and p['only']!=side: continue
        if not trend_ok(c,side,p): continue
        pier=None
        for j,b in enumerate(S):
            if b['m']>p.get('last',14*60+25): break
            if pier is None:
                if (b['l']<lvl-p['pen'] if side>0 else b['h']>lvl+p['pen']): pier=j
                continue
            if j-pier>p['win']: break
            ok=(b['c']>lvl and b['c']>b['vw'] and b['c']>b['o']) if side>0 else (b['c']<lvl and b['c']<b['vw'] and b['c']<b['o'])
            if ok and p.get('qqq'):
                q=Q.get(b['m']);ok=bool(q) and ((q['c']>q['vw']) if side>0 else (q['c']<q['vw']))
            if ok and b['m']>=9*60+45:
                st=(b['l']-p['buf']) if side>0 else (b['h']+p['buf'])
                if p.get('stopext'):
                    ext=min(x['l'] for x in S[pier:j+1]) if side>0 else max(x['h'] for x in S[pier:j+1])
                    st=ext-p['buf'] if side>0 else ext+p['buf']
                t=finish(c,j,side,b['c'],st,p)
                if t: out.append(t)
                break
    return out

# 2 gap fade: open beyond PDH/PDL (or gap >= g), fade after first reversal candle below/above OR; target = fraction of gap toward PDC
def gapfade(c,p):
    S=c['S'];o=S[0]['o'];gap=o-c['PDC'];out=[]
    if abs(gap)<p['g']: return out
    side=-1 if gap>0 else 1
    if p.get('only') and p['only']!=side: return out
    if p.get('beyond') and not ((o>c['PDH']) if side<0 else (o<c['PDL'])): return out
    if not trend_ok(c,side,p): return out
    n=p['orb']  # bars in opening range
    ORH=max(b['h'] for b in S[:n]);ORL=min(b['l'] for b in S[:n])
    for j in range(n,len(S)):
        b=S[j]
        if b['m']>p.get('last',11*60): break
        trig=(b['c']<ORL and b['c']<b['vw']) if side<0 else (b['c']>ORH and b['c']>b['vw'])
        if trig:
            e=b['c'];st=(ORH+p['buf']) if side<0 else (ORL-p['buf'])
            tg=e+side*abs(e-c['PDC'])*p['frac'] if p.get('frac') else None
            if tg is not None and abs(tg-e)<0.1: break
            t=finish(c,j,side,e,st,p,tg)
            if t: out.append(t)
            break
    return out

# 3 VWAP stretch reversion: price > k * (day range so far) away from VWAP... use $ distance; reversal candle; target VWAP fraction
def vwaprev(c,p):
    S=c['S'];out=[];done=set()
    for j in range(3,len(S)):
        b=S[j]
        if b['m']<9*60+45: continue
        if b['m']>p.get('last',14*60+25): break
        dist=b['c']-b['vw']
        for side in (1,-1):
            if side in done or (p.get('only') and p['only']!=side): continue
            prev=S[j-1]
            stretched=(prev['l']-prev['vw']<=-p['k']) if side>0 else (prev['h']-prev['vw']>=p['k'])
            rev=(b['c']>b['o'] and b['c']>prev['h']) if side>0 else (b['c']<b['o'] and b['c']<prev['l'])
            if stretched and rev and trend_ok(c,side,p):
                e=b['c'];st=(min(prev['l'],b['l'])-p['buf']) if side>0 else (max(prev['h'],b['h'])+p['buf'])
                tg=e+side*abs(b['vw']-e)*p['frac'] if p.get('frac') else None
                if tg is not None and abs(tg-e)<0.1: continue
                t=finish(c,j,side,e,st,p,tg)
                if t: out.append(t);done.add(side)
    return out

# 4 breakout-retest continuation at PDH/PDL
def retest(c,p):
    S=c['S'];out=[]
    for side,lvl in ((1,c['PDH']),(-1,c['PDL'])):
        if p.get('only') and p['only']!=side: continue
        if not trend_ok(c,side,p): continue
        broke=None
        for j,b in enumerate(S):
            if b['m']>p.get('last',14*60+25): break
            if broke is None:
                if (b['c']>lvl+0.05 if side>0 else b['c']<lvl-0.05): broke=j
                continue
            if (b['c']<lvl-0.3 if side>0 else b['c']>lvl+0.3): break
            touch=(b['l']<=lvl+p['tol'] and b['c']>lvl and b['c']>b['o']) if side>0 else (b['h']>=lvl-p['tol'] and b['c']<lvl and b['c']<b['o'])
            if touch and b['m']>=9*60+45 and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])):
                st=(min(b['l'],lvl)-p['buf']) if side>0 else (max(b['h'],lvl)+p['buf'])
                t=finish(c,j,side,b['c'],st,p)
                if t: out.append(t)
                break
    return out
FAM=dict(sweep=sweep,gapfade=gapfade,vwaprev=vwaprev,retest=retest)
def run(fn,p,lo,hi):
    T=[]
    for i in range(21,len(DAYS)):
        if lo<=DAYS[i][0]<=hi:
            T+=fn(ctx(i),p)
    return T
def st(T):
    n=len(T);w=sum(1 for t in T if t[1]>0);R=sum(t[1] for t in T)
    return n,w,(w/n if n else 0),R
