import numpy as np, wave, sys
w=wave.open('voice.wav');sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
hop=int(sr*0.02);n=len(x)//hop
e=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2)) for i in range(n)])
db=20*np.log10(e+1e-9)
thr=float(sys.argv[1]) if len(sys.argv)>1 else -38
mingap=float(sys.argv[2]) if len(sys.argv)>2 else 0.25
sp=db>thr
segs=[];i=0
while i<n:
  if sp[i]:
    j=i
    while j<n and sp[j]: j+=1
    segs.append([i*0.02,j*0.02]);i=j
  else:i+=1
# merge gaps<mingap
m=[]
for s in segs:
  if m and s[0]-m[-1][1]<mingap: m[-1][1]=s[1]
  else: m.append(s)
m=[s for s in m if s[1]-s[0]>0.12]
for k,s in enumerate(m):
  gap = s[0]-m[k-1][1] if k else 0
  print(f"{k:2d} {s[0]:6.2f}-{s[1]:6.2f} dur {s[1]-s[0]:4.2f} gap_before {gap:4.2f}")
