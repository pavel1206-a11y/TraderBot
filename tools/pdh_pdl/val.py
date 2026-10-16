from s2 import *
import json
hits=json.load(open('hits.json'))
V0,V1=date(2026,7,1),date(2026,10,15);D0,D1=date(2026,2,3),date(2026,6,30)
rows=[]
for fam,p in hits:
    a=st(run(FAM[fam],p,D0,D1));v=st(run(FAM[fam],p,V0,V1))
    rows.append((v[2],v[3],fam,p,a,v))
rows.sort(key=lambda r:(-r[0],-r[1]))
f=lambda s:f"{s[0]}t {s[1]}W {s[2]*100:.0f}% {s[3]:+.1f}R"
pas=[r for r in rows if r[5][0]>=12 and r[5][2]>=0.8 and r[5][3]>0]
print('pass validation (>=12 trades, >=80%, net>0):',len(pas),'of',len(rows))
for r in rows[:25]: print(r[2],{k:v for k,v in r[3].items() if v is not None},'| disc',f(r[4]),'| VALID',f(r[5]))
