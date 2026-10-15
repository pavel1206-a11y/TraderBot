# Backtest: previous-day high/low sweep and reverse (owner's entry idea, 2026-10-15).
# Usage: python3 tools/backtest_pdh_pdl_sweep.py bars.json  (saved get_equity_historicals JSON, 5-min)
import json,sys
from datetime import datetime,timedelta
d=json.load(open(sys.argv[1]));bars={}
for r in d['data']['results']:
    if r['symbol']!='SPY':continue
    for b in r['bars']:
        t=datetime.fromisoformat(b['begins_at'].replace('Z','+00:00'))-timedelta(hours=4)
        bars.setdefault(t.date(),[]).append(dict(t=t,o=float(b['open_price']),h=float(b['high_price']),l=float(b['low_price']),c=float(b['close_price'])))
days=sorted(bars);prev=None;T=[]
hm=lambda t:t.hour*60+t.minute
for day in days:
    S=sorted(bars[day],key=lambda b:b['t'])
    if prev:
        PDH,PDL=prev
        for side,lvl in (('short@PDH',PDH),('long@PDL',PDL)):
            for i,b in enumerate(S):
                if hm(b['t'])>14*60+25: break
                pierced = b['h']>lvl if side[0]=='s' else b['l']<lvl
                if not pierced: continue
                # look for a close back inside within this bar or next 3
                for j in range(i,min(i+4,len(S))):
                    x=S[j]
                    back = x['c']<lvl if side[0]=='s' else x['c']>lvl
                    if back and hm(x['t'])<=14*60+25 and (j>i or (x['c']<x['o'] if side[0]=='s' else x['c']>x['o'])):
                        ext=max(y['h'] for y in S[i:j+1]) if side[0]=='s' else min(y['l'] for y in S[i:j+1])
                        e=x['c'];st=ext+0.10 if side[0]=='s' else ext-0.10;R=abs(e-st)
                        tg=e-1.5*R if side[0]=='s' else e+1.5*R;res=('3:30',0)
                        for y in S[j+1:]:
                            if hm(y['t'])>=15*60+30: res=('3:30',(e-y['o']) if side[0]=='s' else (y['o']-e));break
                            if (y['h']>=st if side[0]=='s' else y['l']<=st): res=('stop',-R);break
                            if (y['l']<=tg if side[0]=='s' else y['h']>=tg): res=('target',1.5*R);break
                        rest=[y for y in S[j+1:] if hm(y['t'])<15*60+30]
                        mfe=(e-min(y['l'] for y in rest)) if side[0]=='s' else (max(y['h'] for y in rest)-e)
                        T.append((str(day),side,round(lvl,2),x['t'].strftime('%H:%M'),round(e,2),round(R,2),res[0],round(res[1]/R,2),round(mfe,2)))
                        break
                break  # first pierce only
    prev=(max(b['h'] for b in S),min(b['l'] for b in S))
print('last day',days[-1],'H/L',prev)
for t in T: print(t)
for s in ('short@PDH','long@PDL'):
    X=[t for t in T if t[1]==s];w=[t for t in X if t[7]>0]
    print(s,len(X),'trades',len(w),'wins','sumR',round(sum(t[7] for t in X),2))
