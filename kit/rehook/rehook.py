# usage: python3 rehook.py <name>   (run from /tmp/ssp/kit)
import numpy as np, wave, json, sys, os, subprocess
from scipy.signal import welch, stft, istft
from PIL import Image
sr=44100; FPS=30
P=json.load(open('/tmp/w/scripts/params.json'))[sys.argv[1]]
W='/tmp/w/'+sys.argv[1]; os.makedirs(W,exist_ok=True); os.makedirs(W+'/assets',exist_ok=True)
def load(p):
    w=wave.open(p); return np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768
def save(p,y):
    w=wave.open(p,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes()); w.close()
fr=lambda t: round(t*FPS)/FPS
Told=json.load(open(P['kitdir']+'/times_c.json')); nh=P['nh']
old=load(P['old_wav']); new=load(P['new_wav'])
# --- hook voice: chunks with compressed gaps
GAP=P.get('gap',0.10); segs=[]; t=0.10; chunk_t=[]
for s,e in P['chunks']:
    s0,e0=s-0.03,e+0.05
    seg=new[int(s0*sr):int(e0*sr)].copy(); f=int(0.01*sr); seg[:f]*=np.linspace(0,1,f); seg[-f:]*=np.linspace(1,0,f)
    chunk_t.append((t+0.03,t+0.03+(e-s))); segs.append((t,seg)); t+=len(seg)/sr+GAP
hook_end=chunk_t[-1][1]
cut_old=fr(Told[nh][0]-0.40); cut_new=fr(hook_end+0.30); delta=cut_new-cut_old
hv=np.zeros(int(cut_new*sr))
for t0,seg in segs: hv[int(t0*sr):int(t0*sr)+len(seg)]+=seg
# --- EQ match to old body voice
tgt=old[int((cut_old+0.4)*sr):int((cut_old+30)*sr)]
f,Pt=welch(tgt,sr,nperseg=4096); _,Ps=welch(new[int(P['chunks'][0][0]*sr):int(P['chunks'][-1][1]*sr)],sr,nperseg=4096)
g=np.sqrt(Pt/(Ps+1e-15)); gs=np.ones_like(g)
for i,fc in enumerate(f):
    if fc<60: continue
    m=(f>=fc/2**(1/6))&(f<=fc*2**(1/6)); gs[i]=np.exp(np.mean(np.log(g[m]+1e-9)))
gdb=20*np.log10(gs); gdb-=np.mean(gdb[(f>300)&(f<1000)]); gdb=np.clip(gdb,-6,8); gdb[f>15000]=np.minimum(gdb[f>15000],0)
fs,_,Z=stft(hv,sr,nperseg=4096); _,hv2=istft(Z*(10**(np.interp(fs,f,gdb)/20))[:,None],sr,nperseg=4096); hv=hv2[:len(hv)]
# --- level match on active speech
def act(x):
    h=int(0.05*sr); r=np.array([np.sqrt(np.mean(x[i:i+h]**2)) for i in range(0,len(x)-h,h)]); r=r[r>10**(-35/20)*np.max(r)/np.max(r)*1] 
    return np.percentile(r,75)
def act2(x):
    h=int(0.05*sr); r=np.array([np.sqrt(np.mean(x[i:i+h]**2)) for i in range(0,len(x)-h,h)]); m=r.max(); return np.percentile(r[r>m*0.1],75)
gain=act2(tgt)/act2(hv); hv*=gain
print('EQ dB 2k/4k/8k',[round(float(np.interp(x,f,gdb)),1) for x in [2000,4000,8000]],'gain dB',round(20*np.log10(gain),1))
# --- new times
Tn=[]
for grp in P['groups']: Tn.append([round(chunk_t[grp[0]][0],3),round(chunk_t[grp[-1]][1],3)])
Tn+= [[round(a+delta,3),round(b+delta,3)] for a,b in Told[nh:]]
json.dump(Tn,open(W+'/times_c.json','w'))
# voice for envelope
vc=np.concatenate([hv,old[int(cut_old*sr):]]); save(W+'/voice_c.wav',vc)
# --- cfg
cfg=open(P['kitdir']+'/cfg.py').read()
for a,b in P.get('cfg_sub',[]): 
    assert a in cfg, a; cfg=cfg.replace(a,b)
open(W+'/cfg.py','w').write(cfg)
# --- bg: first old frame, band from frame at old STEP_START-0.05
vid=P['old_mp4']; ss=Told[nh][0]-0.30-0.05
for nm,tt in (('a',0.0),('b',ss)):
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{tt:.3f}','-i',vid,'-frames:v','1',f'{W}/bg_{nm}.png'],check=True)
A=np.array(Image.open(W+'/bg_a.png').convert('RGB')); B=np.array(Image.open(W+'/bg_b.png').convert('RGB'))
A[380:1270]=B[380:1270]; Image.fromarray(A).save(W+'/assets/bg.png')
os.system(f'cp assets/photo_block.png {W}/assets/')
json.dump(dict(cut_old=cut_old,cut_new=cut_new,delta=delta,hook_end=hook_end),open(W+'/meta.json','w'))
save(W+'/hookvoice.wav',hv)
print(sys.argv[1],'chunks',[tuple(round(v,2) for v in c) for c in chunk_t],'cut_old',cut_old,'cut_new',cut_new,'delta',round(delta,2))
