from eng import DAYS
from datetime import date
COST=0.02
def ctx(i):
    d,S,Q=DAYS[i];_,P,_=DAYS[i-1]
    return dict(d=d,S=S,Q=Q,PDH=max(b['h'] for b in P),PDL=min(b['l'] for b in P),PDC=P[-1]['c'])
def play2(S,j,side,e,st,p):
    R=abs(e-st);stop=st;mode=p['exit'];be=p.get('be')
    for k in range(j+1,len(S)):
        y=S[k]
        if y['m']>=15*60+30: return ((y['o']-e)*side-COST)/R
        if (y['l']<=stop if side>0 else y['h']>=stop): return ((stop-e)*side-COST)/R
        fav=((y['h']-e) if side>0 else (e-y['l']))/R
        if mode[0]=='R' and fav>=mode[1]: return (mode[1]*R-COST)/R
        if be and fav>=be: stop=max(stop,e) if side>0 else min(stop,e)
        c=y['c']
        if mode[0]=='vwap' and k>j+1 and ((c<y['vw']) if side>0 else (c>y['vw'])): return ((c-e)*side-COST)/R
        if mode[0]=='trail':  # trail stop to prior bar extreme after +trigger R
            if fav>=mode[1]:
                ns=(y['l']-0.05) if side>0 else (y['h']+0.05)
                stop=max(stop,ns) if side>0 else min(stop,ns)
        if mode[0]=='chand':  # chandelier: highest high - X
            pass
    return 0
def ok_q(c,b,side):
    q=c['Q'].get(b['m']);return bool(q) and ((q['c']>q['vw']) if side>0 else (q['c']<q['vw']))
def mk(c,j,side,st,p):
    b=c['S'][j];e=b['c'];R=abs(e-st)
    if R<0.12 or R>p.get('maxR',1.5): return None
    return (c['d'],play2(c['S'],j,side,e,st,p),side,b['t'].strftime('%H:%M'))
def stopfor(S,j,side,p,extra=None):
    b=S[j]
    if p['stop']=='bar': return (b['l']-p['buf']) if side>0 else (b['h']+p['buf'])
    if p['stop']=='2bar': return (min(b['l'],S[j-1]['l'])-p['buf']) if side>0 else (max(b['h'],S[j-1]['h'])+p['buf'])
    if p['stop']=='vwap': return (b['vw']-p['buf']) if side>0 else (b['vw']+p['buf'])
    if p['stop']=='lvl': return (extra-p['buf']) if side>0 else (extra+p['buf'])
# E1 ORB
def orb(c,p):
    S=c['S'];n=p['n'];H=max(b['h'] for b in S[:n]);L=min(b['l'] for b in S[:n]);out=[]
    if p.get('maxor') and H-L>p['maxor']: return out
    for j in range(n,len(S)):
        b=S[j]
        if b['m']>p['last']: break
        for side,lvl in ((1,H),(-1,L)):
            if (b['c']>lvl if side>0 else b['c']<lvl) and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])) and (not p.get('q') or ok_q(c,b,side)):
                if p.get('vol') and b['v']<p['vol']*sum(x['v'] for x in S[max(0,j-10):j])/max(1,len(S[max(0,j-10):j])): continue
                t=mk(c,j,side,stopfor(S,j,side,p,lvl),p)
                return [t] if t else []
    return out
# E2 PDH/PDL breakout
def pdbrk(c,p):
    S=c['S'];out=[]
    o=S[0]['o']
    for side,lvl in ((1,c['PDH']),(-1,c['PDL'])):
        if (o>lvl if side>0 else o<lvl): continue  # gapped beyond; skip
        for j,b in enumerate(S):
            if b['m']>p['last']: break
            if b['m']<9*60+45: continue
            if (b['c']>lvl+0.03 if side>0 else b['c']<lvl-0.03) and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])) and (not p.get('q') or ok_q(c,b,side)):
                if p.get('vol') and b['v']<p['vol']*sum(x['v'] for x in S[max(0,j-10):j])/max(1,len(S[max(0,j-10):j])): break
                t=mk(c,j,side,stopfor(S,j,side,p,lvl),p)
                if t: out.append(t)
                break
    return out
# E3 flush + VWAP reclaim + hold (both directions)
def reclaim(c,p):
    S=c['S'];out=[]
    for side in (1,-1):
        armed=False;rec=None
        for j,b in enumerate(S):
            if b['m']>p['last']: break
            ext=min(x['l'] for x in S[:j+1]) if side>0 else max(x['h'] for x in S[:j+1])
            if (b['l']<=ext if side>0 else b['h']>=ext) and ((b['c']<b['vw']) if side>0 else (b['c']>b['vw'])) and b['m']>=9*60+35: armed=True;rec=None;continue
            if armed and rec is None and ((b['c']>b['vw']+0.1) if side>0 else (b['c']<b['vw']-0.1)) and (not p.get('q') or ok_q(c,b,side)): rec=j;continue
            if rec is not None:
                if j-rec>6: armed=False;rec=None;continue
                hold=(b['l']>=b['vw']-0.05 and b['c']>b['o']) if side>0 else (b['h']<=b['vw']+0.05 and b['c']<b['o'])
                if hold and b['m']>=9*60+45:
                    t=mk(c,j,side,stopfor(S,j,side,p),p)
                    if t: out.append(t)
                    break
    return out
# E4 squeeze breakout: range of last N bars < W, close beyond
def squeeze(c,p):
    S=c['S'];out=[];N=p['N']
    for j in range(N,len(S)):
        b=S[j]
        if b['m']>p['last']: break
        if b['m']<10*60+30: continue
        win=S[j-N:j];H=max(x['h'] for x in win);L=min(x['l'] for x in win)
        if H-L>p['W']: continue
        for side,lvl in ((1,H),(-1,L)):
            if (b['c']>lvl if side>0 else b['c']<lvl) and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])) and (not p.get('q') or ok_q(c,b,side)):
                if p.get('vol') and b['v']<p['vol']*sum(x['v'] for x in win[-10:])/10: continue
                st=stopfor(S,j,side,p,(L+H)/2 if p['stop']=='lvl' else None)
                t=mk(c,j,side,st,p)
                if t: return [t]
    return out
FAM=dict(orb=orb,pdbrk=pdbrk,reclaim=reclaim,squeeze=squeeze)
def run(fn,p,lo,hi):
    T=[]
    for i in range(21,len(DAYS)):
        if lo<=DAYS[i][0]<=hi: T+=fn(ctx(i),p)
    return T
def st(T):
    n=len(T)
    if not n: return dict(n=0)
    W=[t[1] for t in T if t[1]>0];L=[t[1] for t in T if t[1]<=0]
    aw=sum(W)/len(W) if W else 0;al=-sum(L)/len(L) if L else 1e-9
    return dict(n=n,wr=len(W)/n,aw=aw,al=al,ratio=aw/al if al else 99,R=sum(t[1] for t in T),exp=sum(t[1] for t in T)/n,pf=(sum(W)/-sum(L)) if L and sum(L)<0 else 99)
