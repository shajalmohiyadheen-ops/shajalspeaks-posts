import numpy as np, sys, json, subprocess
def bursts(path, gap=0.35):
    out=subprocess.run(['python3','seg2.py',path,str(gap)],capture_output=True,text=True).stdout.split('\n')
    return [tuple(map(float,l.split()[1:3])) for l in out if l.strip()]
def align(lines, bs):
    ch=np.array([max(4,len(l)) for l in lines],float)
    rate=sum(b[1]-b[0] for b in bs)/ch.sum()
    L,B=len(lines),len(bs)
    INF=1e18; dp=np.full((L+1,B+1),INF); bk={}
    dp[0,0]=0
    for i in range(L+1):
        for j in range(B+1):
            if dp[i,j]>=INF: continue
            for nl in range(1,4):
                for nb in range(1,4):
                    if nl>1 and nb>1: continue
                    i2,j2=i+nl,j+nb
                    if i2>L or j2>B: continue
                    exp=ch[i:i2].sum()*rate; act=bs[j2-1][1]-bs[j][0]
                    c=((exp-act)/max(act,0.5))**2 + 0.3*(nl-1)+0.3*(nb-1)
                    if dp[i,j]+c<dp[i2,j2]: dp[i2,j2]=dp[i,j]+c; bk[(i2,j2)]=(i,j)
    # walk back
    i,j=L,B; groups=[]
    while (i,j)!=(0,0):
        pi,pj=bk[(i,j)]; groups.append((pi,i,pj,j)); i,j=pi,pj
    groups.reverse()
    res=[]
    for li0,li1,bj0,bj1 in groups:
        s,e=bs[bj0][0],bs[bj1-1][1]
        if li1-li0==1: res.append((s,e))
        else:
            # split by char proportion, snapping to internal low-energy not available -> proportional
            tot=ch[li0:li1].sum(); t=s
            for k in range(li0,li1):
                d=(e-s)*ch[k]/tot; res.append((t,t+d)); t+=d
    return res, groups, rate
if __name__=='__main__':
    lines=json.load(open(sys.argv[1])); bs=bursts(sys.argv[2])[:-1]  # drop end card
    res,g,rate=align(lines,bs)
    print('rate',round(rate,3),'groups',g)
    for l,(s,e) in zip(lines,res): print(f"{s:6.2f}-{e:6.2f} {l}")
    json.dump(res,open(sys.argv[3],'w'))
