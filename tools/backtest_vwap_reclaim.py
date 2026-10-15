# Backtest of the VWAP-reclaim line (playbook section 10, added 2026-10-15).
# Input: a saved Robinhood get_equity_historicals JSON (SPY + QQQ, 5-minute bars).
# Usage: python3 tools/backtest_vwap_reclaim.py bars.json
import json,sys
from datetime import datetime,timedelta
d=json.load(open(sys.argv[1]))
bars={}
for r in d['data']['results']:
    for b in r['bars']:
        t=datetime.fromisoformat(b['begins_at'].replace('Z','+00:00'))-timedelta(hours=4)
        bars.setdefault(t.date(),{}).setdefault(r['symbol'],[]).append(dict(t=t,o=float(b['open_price']),h=float(b['high_price']),l=float(b['low_price']),c=float(b['close_price']),v=b['volume']))
def vw(bs):
    pv=vv=0;out=[]
    for b in bs:
        pv+=(b['h']+b['l']+b['c'])/3*b['v'];vv+=b['v'];out.append(pv/vv if vv else b['c'])
    return out
days=sorted(bars); prev=None; trades=[]
def hm(t): return t.hour*60+t.minute
for day in days:
    S=bars[day].get('SPY');Q=bars[day].get('QQQ')
    if not S or not Q or len(S)<60: prev=None;continue
    S.sort(key=lambda b:b['t']);Q.sort(key=lambda b:b['t'])
    qm={b['t']:b for b in Q}
    sv=vw(S); qv_list=vw(Q); qv={b['t']:x for b,x in zip(Q,qv_list)}
    levels=[]
    if prev:
        H,L,C=prev;P=(H+L+C)/3;levels=[H,L,P,2*P-L,2*P-H,P+(H-L),P-(H-L)]
    for side in ('long','short'):
        armed=False;i=0;dayext=None
        while i<len(S):
            b=S[i];m=hm(b['t'])
            dayext = b['l'] if dayext is None else (min(dayext,b['l']) if side=='long' else dayext)
            if side=='short': dayext = b['h'] if i==0 else max(dayext,b['h'])
            newext = (b['l']<=min(x['l'] for x in S[:i+1])) if side=='long' else (b['h']>=max(x['h'] for x in S[:i+1]))
            if m>=9*60+45 and m<=14*60+15 and newext and ((b['c']<sv[i]) if side=='long' else (b['c']>sv[i])):
                armed=True
            if armed and i>=3 and m<=14*60+20:
                pr=S[max(0,i-10):i]; avg=sum(x["v"] for x in pr)/len(pr)
                qb=qm.get(b['t']);qprev=qm.get(S[i-1]['t'])
                if qb and qprev:
                    if side=='long':
                        cond=b['c']>sv[i]+0.10 and qb['c']>qv[b['t']]
                        qre=qprev['c']<qv[S[i-1]['t']] and qb['c']>qv[b['t']]
                    else:
                        cond=b['c']<sv[i]-0.10 and qb['c']<qv[b['t']]
                        qre=qprev['c']>qv[S[i-1]['t']] and qb['c']<qv[b['t']]
                    vol=b['v']>=avg or (b['v']>=0.7*avg and qre)
                    if cond and vol:
                        # bar 2
                        for j in range(i+1,min(i+7,len(S))):
                            c2=S[j]
                            if hm(c2['t'])>14*60+25: break
                            ok = (c2['l']>=sv[j]-0.05 and c2['c']>c2['o']) if side=='long' else (c2['h']<=sv[j]+0.05 and c2['c']<c2['o'])
                            if ok:
                                e=c2['c']; st=c2['l']-0.10 if side=='long' else c2['h']+0.10
                                R=abs(e-st); tg=e+1.5*R if side=='long' else e-1.5*R
                                hi_so_far=max(x['h'] for x in S[:j+1]); lo_so_far=min(x['l'] for x in S[:j+1])
                                lv=[x for x in levels+[hi_so_far if side=='long' else lo_so_far] if (x>e+0.05 if side=='long' else x<e-0.05)]
                                nxt=(min(lv) if side=='long' else max(lv)) if lv else None
                                room_ok = nxt is None or abs(nxt-e)>=1.5*R
                                res=None
                                for k in range(j+1,len(S)):
                                    x=S[k]
                                    if hm(x['t'])>=15*60+30: res=('3:30',(x['o']-e) if side=='long' else (e-x['o']));break
                                    hs = x['l']<=st if side=='long' else x['h']>=st
                                    ht = x['h']>=tg if side=='long' else x['l']<=tg
                                    if hs: res=('stop',-R);break
                                    if ht: res=('target',1.5*R);break
                                    if k==j+6 and ((x['c']<=e) if side=='long' else (x['c']>=e)):
                                        res=('time',(x['c']-e) if side=='long' else (e-x['c']));break
                                # max favorable before 15:30
                                rest=[x for x in S[j+1:] if hm(x['t'])<15*60+30]
                                mfe=(max(x['h'] for x in rest)-e) if side=='long' else (e-min(x['l'] for x in rest)) if rest else 0
                                trades.append(dict(day=str(day),side=side,b1=b['t'].strftime('%H:%M'),b2=c2['t'].strftime('%H:%M'),e=round(e,2),R=round(R,2),room=room_ok,res=res[0],pnl=round(res[1],2),rr=round(res[1]/R,2),mfe=round(mfe,2),volx=round(b['v']/avg,2),rng=round(b['h']-b['l'],2)))
                                i=k; armed=False
                                break
                        else:
                            pass
                        if not armed: i+=1; continue
            i+=1
    H=max(x['h'] for x in S);L=min(x['l'] for x in S);prev=(H,L,S[-1]['c'])
print(len(days),'days',days[0],days[-1])
for t in trades: print(t)
for side in ('long','short'):
  for rf in (False,True):
    T=[t for t in trades if t['side']==side and (t['room'] or not rf)]
    w=[t for t in T if t['pnl']>0]
    print(side,'room-filter' if rf else 'all', len(T),'trades',len(w),'wins', 'sumR',round(sum(t['rr'] for t in T),2),'sum$',round(sum(t['pnl'] for t in T),2))
