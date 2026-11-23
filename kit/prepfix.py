# like prep.py but with hand-checked line times (res.json) instead of auto-align
import numpy as np, wave, json, sys
sys.path.insert(0,'.')
from align import bursts
k=sys.argv[1]; vend=float(sys.argv[2]); hook_n=int(sys.argv[3])
lines=json.load(open(f'{k}/lines.json')); res=json.load(open(f'{k}/res.json'))
w=wave.open(f'{k}/old.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768
x=x[:int(vend*sr)]
bs=[b for b in bursts(f'{k}/old.wav',0.12) if b[1]<=vend+0.05]
hook_end=res[hook_n][0]
cuts=[]; out=[]; t_new=0.0; prev_end=None
for (s,e) in bs:
    s0=max(0,s-0.04); e0=min(vend,e+0.06)
    if prev_end is None: gap_new=0.06
    else:
        g=s0-prev_end; lim=0.18 if s<hook_end else 0.6
        gap_new=max(0,min(g,lim))
        if abs(s-hook_end)<0.05: gap_new=0.75
    t_new+=gap_new
    cuts.append((s0,e0,t_new)); seg=x[int(s0*sr):int(e0*sr)].copy()
    f=int(0.01*sr); seg[:f]*=np.linspace(0,1,f); seg[-f:]*=np.linspace(1,0,f)
    out.append(np.zeros(int(gap_new*sr))); out.append(seg); t_new+=len(seg)/sr; prev_end=e0
y=np.concatenate(out)
def mp(t):
    for s0,e0,n0 in cuts:
        if s0-0.01<=t<=e0+0.001: return n0+max(0,t-s0)
    return t
newres=[(round(mp(s),3),round(mp(e),3)) for s,e in res]
json.dump(newres,open(f'{k}/times_c.json','w'))
ww=wave.open(f'{k}/voice_c.wav','wb'); ww.setnchannels(1); ww.setsampwidth(2); ww.setframerate(sr); ww.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes()); ww.close()
print(k,'voice len',round(len(y)/sr,2))
for l,(s,e) in zip(lines,newres): print(f"{s:6.2f}-{e:6.2f} {l}")
