from eng import DAYS,play
import itertools,sys
def run(strat,p):
    T=[]
    for i in range(1,len(DAYS)):
        d,S,Q=DAYS[i];_,P,_=DAYS[i-1]
        PDH=max(b['h'] for b in P);PDL=min(b['l'] for b in P);PDC=P[-1]['c']
        for tr in strat(S,Q,PDH,PDL,PDC,p): T.append((d,)+tr)
    return T
def stats(T):
    n=len(T);w=sum(1 for t in T if t[1]>0);R=sum(t[1] for t in T)
    return n,w,(w/n if n else 0),R,(R/n if n else 0)

# A: sweep then reclaim with confirmation: pierce level, then close back inside AND on right side of VWAP; entry at first such close after 9:45
def sweep_vwap(S,Q,PDH,PDL,PDC,p):
    out=[]
    for side,lvl in ((1,PDL),(-1,PDH)):
        pierced=None
        for j,b in enumerate(S):
            if b['m']>14*60+25: break
            if pierced is None:
                if (b['l']<lvl-p['pen'] if side>0 else b['h']>lvl+p['pen']): pierced=j
                else: continue
            if j-pierced>p['win']: break
            ext=min(x['l'] for x in S[pierced:j+1]) if side>0 else max(x['h'] for x in S[pierced:j+1])
            ok=(b['c']>lvl and b['c']>b['vw'] and b['c']>b['o']) if side>0 else (b['c']<lvl and b['c']<b['vw'] and b['c']<b['o'])
            if p.get('qqq'):
                q=Q.get(b['m']); ok=ok and q and ((q['c']>q['vw']) if side>0 else (q['c']<q['vw']))
            if ok and b['m']>=9*60+45:
                e=b['c']
                st=(ext-p['buf']) if p['stop']=='ext' else ((b['l']-p['buf']) if side>0 else (b['h']+p['buf']))
                R=abs(e-st)
                if R<0.15 or R>p['maxR']: break
                tg=e+side*p['rr']*R
                r,why=play(S,j,side,e,st,tg,p.get('ts'))
                out.append((r,why,side,b['t'].strftime('%H:%M')));break
    return out

# B: breakout-retest: close beyond level, later bar retests level (wick within tol) and closes beyond with VWAP agreement
def brk_retest(S,Q,PDH,PDL,PDC,p):
    out=[]
    for side,lvl in ((1,PDH),(-1,PDL)):
        broke=None
        for j,b in enumerate(S):
            if b['m']>14*60+25: break
            if broke is None:
                if (b['c']>lvl+0.05 if side>0 else b['c']<lvl-0.05) and b['m']>=9*60+35: broke=j
                continue
            touch=(b['l']<=lvl+p['tol'] and b['c']>lvl) if side>0 else (b['h']>=lvl-p['tol'] and b['c']<lvl)
            if (b['c']<lvl-0.3 if side>0 else b['c']>lvl+0.3): break  # failed breakout
            if touch and b['m']>=9*60+45 and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])):
                e=b['c'];st=(min(b['l'],lvl)-p['buf']) if side>0 else (max(b['h'],lvl)+p['buf'])
                R=abs(e-st)
                if R<0.15 or R>p['maxR']: break
                r,why=play(S,j,side,e,st,e+side*p['rr']*R,p.get('ts'))
                out.append((r,why,side,b['t'].strftime('%H:%M')));break
    return out

# C: rejection fade from inside: price approaches level from inside, wicks to within tol (no close beyond), closes back away -> fade toward middle
def reject(S,Q,PDH,PDL,PDC,p):
    out=[]
    o=S[0]['o']
    if not (PDL<o<PDH): return out
    for side,lvl in ((-1,PDH),(1,PDL)):
        for j,b in enumerate(S):
            if b['m']>14*60+25: break
            if (b['c']>lvl if side<0 else b['c']<lvl): break  # closed beyond -> no fade
            touched=(b['h']>=lvl-p['tol']) if side<0 else (b['l']<=lvl+p['tol'])
            if touched and b['m']>=9*60+45 and ((b['c']<b['o']) if side<0 else (b['c']>b['o'])):
                e=b['c'];st=(max(b['h'],lvl)+p['buf']) if side<0 else (min(b['l'],lvl)-p['buf'])
                R=abs(e-st)
                if R<0.15 or R>p['maxR']: break
                r,why=play(S,j,-side*-1 if False else (1 if side>0 else -1),e,st,e+(1 if side>0 else -1)*p['rr']*R,p.get('ts'))
                out.append((r,why,side,b['t'].strftime('%H:%M')));break
    return out
