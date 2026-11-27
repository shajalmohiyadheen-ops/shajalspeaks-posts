import os, sys, numpy as np, wave, subprocess
k=sys.argv[1]; os.environ['CFG']=f'{k}/cfg.py'; sys.argv=['x']
import importlib.util
spec=importlib.util.spec_from_file_location('b','build_ho.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
sr=44100
def load(p):
    w=wave.open(p); return np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768
hits=[np.asarray(h,dtype=float) for h in np.load('common/hits.npy',allow_pickle=True)]
Wh=load('common/whoosh.wav'); f=int(0.01*sr); Wh[:f]*=np.linspace(0,1,f); Wh[-f:]*=np.linspace(1,0,f); Wh=Wh/np.abs(Wh).max()*0.9
th=load('common/thud.wav')[int(0.17*sr):]
n=int(b.BODY_END*sr); out=np.zeros(n); rng=np.random.default_rng(5)
def put(sig,t,g):
    j=int(t*sr)
    if j<0: sig=sig[-j:]; j=0
    L=min(len(sig),n-j)
    if L>0: out[j:j+L]+=sig[:L]*g
for i,ws,s in ([] if os.environ.get('NOTAPS') else b.PLACED):
    for wd in ws:
        kk=int(min(4,max(1,np.ceil(wd.chars/4))))
        for m in range(kk): put(hits[rng.integers(len(hits))], wd.t+m*0.06+rng.uniform(-0.008,0.008), rng.uniform(0.20,0.26))
for st,t0 in b.STEP_START.items(): put(Wh, t0-0.20+0.143, 0.40)
if b.TICKS:
    t=b.TICKS[0]; kk=0; times=[]
    while t<b.TICKS[1]: times.append(t); kk+=1; t+=max(0.028,0.075-0.004*kk)
    for i,tt in enumerate(times):
        fq=2200-1100*i/len(times); L=int(0.018*sr)
        put(np.sin(2*np.pi*fq*np.arange(L)/sr)*np.exp(-np.arange(L)/(0.004*sr)), tt, 0.34)
put(th, b.SLAM, 1.35)
out=np.clip(out,-1,1)
ww=wave.open(f'{k}/sfx.wav','wb'); ww.setnchannels(1); ww.setsampwidth(2); ww.setframerate(sr); ww.writeframes((out*32767).astype(np.int16).tobytes()); ww.close()
print(k,'body_end',round(b.BODY_END,2))
