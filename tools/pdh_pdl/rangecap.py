import sys
sys.path.insert(0,'.')
from eng import DAYS,play
def run(cap,band=0.10):
    out=[]
    prev=None
    for d,S,Q in DAYS:
        if prev is None: prev=S; continue
        H=max(b['h'] for b in prev);L=min(b['l'] for b in prev);C=prev[-1]['c'];P=(H+L+C)/3
        piv=[H,L,C,P,2*P-L,2*P-H,P+(H-L),P-(H-L)]
        prev=S
        orb=[b for b in S if b['m']<9*60+45]
        if len(orb)<3: continue
        orh=max(b['h'] for b in orb);orl=min(b['l'] for b in orb)
        busy=-1;n=0;losses=0
        for i,b in enumerate(S):
            if i<=busy or not(9*60+45<=b['m']<=14*60+25) or n>=3 or losses>=2 or i<10: continue
            q=Q.get(b['m']); 
            if not q: continue
            p=S[i-1]
            avg=sum(x['v'] for x in S[i-10:i])/10; vr=b['v']/avg if avg else 0
            dh=max(x['h'] for x in S[:i]);dl=min(x['l'] for x in S[:i])
            keys=piv+[orh,orl,dh,dl]
            qprev=[Q.get(x['m']) for x in S[i-9:i]];qprev=[x for x in qprev if x]
            for dr in (1,-1):
                ab=lambda x,y:(x-y)*dr>0
                if not(ab(b['c'],b['vw']) and ab(q['c'],q['vw'])): continue
                lv=[k for k in keys if ab(b['c'],k) and not ab(p['c'],k) and abs(b['c']-k)<=band]
                if not lv: continue
                qedge=(max(x['h'] for x in qprev) if dr>0 else min(x['l'] for x in qprev)) if qprev else None
                qbrk=qedge is not None and ((q['h']>qedge) if dr>0 else (q['l']<qedge))
                if not(vr>=1.0 or (vr>=0.7 and qbrk)): continue
                rng=b['h']-b['l']
                if cap is not None and rng>cap: continue
                e=b['c'];st=e-0.40*dr;tg=e+0.60*dr
                nxt=[k for k in keys if ab(k,e+0.05*dr)]
                if nxt:
                    nl=min(nxt) if dr>0 else max(nxt)
                    if abs(nl-e)<0.60: continue
                r,why=play(S,i,dr,e,st,tg,tstop=6)
                # find exit index approx: skip ahead until resolved
                out.append((d,b['m'],dr,round(rng,2),round(r,2),why))
                n+=1;losses+=r<0
                # block new entries until resolved: crude, advance 6 bars
                busy=i+6
                break
    return out
base=set((t[0],t[1]) for t in run(1.00))
for cap in (1.00,1.25,1.50,2.00,None):
    t=run(cap); w=[x for x in t if x[4]>0]
    extra=[x for x in t if (x[0],x[1]) not in base]
    ew=[x for x in extra if x[4]>0]
    print(f"cap {str(cap):>5}: {len(t):3d} trades {len(w)/max(1,len(t)):.0%} win {sum(x[4] for x in t):+6.1f}R | extra vs $1.00: {len(extra):3d} trades {len(ew)} wins {sum(x[4] for x in extra):+5.1f}R")
