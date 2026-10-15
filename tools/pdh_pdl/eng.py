import json
from datetime import datetime,timedelta
raw=json.load(open(__import__('sys').argv[1] if len(__import__('sys').argv)>1 else 'data/bars.json'))
def load():
    days={}
    for sym in ('SPY','QQQ'):
        for k,v in raw[sym].items():
            t=datetime.fromisoformat(k.replace('Z','+00:00'))
            # DST: EDT until Nov 1 2026; all data Jun-Oct -> UTC-4
            t=t-timedelta(hours=4)
            days.setdefault(t.date(),{}).setdefault(sym,[]).append(dict(t=t,m=t.hour*60+t.minute,o=v[0],h=v[1],l=v[2],c=v[3],v=v[4]))
    out=[]
    for d in sorted(days):
        S=sorted(days[d]['SPY'],key=lambda b:b['m']);Q=sorted(days[d].get('QQQ',[]),key=lambda b:b['m'])
        if len(S)<70: continue  # skip half days
        for B in (S,Q):
            pv=vv=0
            for b in B:
                pv+=(b['h']+b['l']+b['c'])/3*b['v'];vv+=b['v'];b['vw']=pv/vv
        out.append((d,S,{b['m']:b for b in Q}))
    return out
DAYS=load()
def play(S,j,side,e,st,tg,tstop=None):
    R=abs(e-st)
    for k in range(j+1,len(S)):
        y=S[k]
        if y['m']>=15*60+30: return ((y['o']-e) if side>0 else (e-y['o']))/R,'eod'
        if (y['l']<=st if side>0 else y['h']>=st): return -1.0,'stop'
        if (y['h']>=tg if side>0 else y['l']<=tg): return abs(tg-e)/R,'tgt'
        if tstop and k==j+tstop:
            r=((y['c']-e) if side>0 else (e-y['c']))/R
            if r<=0: return r,'time'
    return 0,'end'
