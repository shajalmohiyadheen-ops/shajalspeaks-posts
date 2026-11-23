import numpy as np, wave, sys
p=sys.argv[1]; gapmin=float(sys.argv[2]) if len(sys.argv)>2 else 0.9
w=wave.open(p);sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768
h=int(sr*0.02);n=len(x)//h
db=np.array([20*np.log10(np.sqrt(np.mean(x[i*h:(i+1)*h]**2))+1e-9) for i in range(n)])
sp=db>-40
segs=[];i=0
while i<n:
  if sp[i]:
    j=i
    while j<n and sp[j]: j+=1
    segs.append([i*0.02,j*0.02]);i=j
  else:i+=1
m=[]
for s in segs:
  if m and s[0]-m[-1][1]<gapmin: m[-1][1]=s[1]
  else: m.append(s)
m=[s for s in m if s[1]-s[0]>0.15]
for k,s in enumerate(m): print(k,round(s[0],2),round(s[1],2),round(s[1]-s[0],2), round(s[0]-(m[k-1][1] if k else 0),2))
