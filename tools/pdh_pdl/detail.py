from s3 import *
import s3,collections
p={'n': 6, 'stop': '2bar', 'last': 750, 'vol': 1.2, 'exit': ('eod',), 'be': 1.0, 'buf': 0.05, 'q': 1}
# instrument play2 to return $ too
rows=[]
for i in range(21,len(DAYS)):
    c=ctx(i);S=c['S'];n=6
    H=max(b['h'] for b in S[:n]);L=min(b['l'] for b in S[:n])
    for j in range(n,len(S)):
        b=S[j]
        if b['m']>750: break
        hit=None
        for side,lvl in ((1,H),(-1,L)):
            if (b['c']>lvl if side>0 else b['c']<lvl) and ((b['c']>b['vw']) if side>0 else (b['c']<b['vw'])) and ok_q(c,b,side):
                pr=S[max(0,j-10):j]
                if b['v']<1.2*sum(x['v'] for x in pr)/len(pr): continue
                hit=side;break
        if hit:
            side=hit;st_=stopfor(S,j,side,p);e=b['c'];R=abs(e-st_)
            if R<MINR or R>1.5: break
            r=play2(S,j,side,e,st_,p)
            rows.append((c['d'],b['t'].strftime('%H:%M'),'CALL' if side>0 else 'PUT',round(e,2),round(R,2),round(r,2),round(r*R,2)))
            break
W=[x for x in rows if x[5]>0.05];BE=[x for x in rows if -0.2<x[5]<=0.05];L=[x for x in rows if x[5]<=-0.2]
print(len(rows),'trades | wins',len(W),'| scratches (breakeven)',len(BE),'| full losses',len(L))
print('avg risk $',round(sum(x[4] for x in rows)/len(rows),2),'| avg win $',round(sum(x[6] for x in W)/len(W),2),'| avg full loss $',round(sum(x[6] for x in L)/len(L),2),'| net $/sh',round(sum(x[6] for x in rows),2))
print('biggest wins:',sorted(rows,key=lambda x:-x[6])[:8])
m=collections.defaultdict(list)
for x in rows: m[x[0].strftime('%Y-%m')].append(x)
for k in sorted(m): v=m[k];print(k,len(v),'t',sum(1 for x in v if x[5]>0.05),'W',round(sum(x[5] for x in v),1),'R',round(sum(x[6] for x in v),2),'$')
# losing streak
s=mx=0
for x in rows:
    s=s+1 if x[5]<=0.05 else 0;mx=max(mx,s)
print('longest run without a win',mx)
# equity drawdown in R
eq=pk=dd=0
for x in rows: eq+=x[5];pk=max(pk,eq);dd=min(dd,eq-pk)
print('total R',round(eq,1),'max drawdown R',round(dd,1))
print('calls',sum(1 for x in rows if x[2]=='CALL'),'R',round(sum(x[5] for x in rows if x[2]=='CALL'),1),'| puts',sum(1 for x in rows if x[2]=='PUT'),'R',round(sum(x[5] for x in rows if x[2]=='PUT'),1))
