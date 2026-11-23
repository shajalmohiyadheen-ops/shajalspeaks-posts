import numpy as np, wave, sys
from scipy.signal import welch, stft, istft
def load(p):
    w=wave.open(p); return np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768, w.getframerate()
tgt,sr=load('/home/claude/reel/voice_norm.wav')
src,sr2=load(sys.argv[1]); assert sr==sr2
f,Pt=welch(tgt,sr,nperseg=4096); _,Ps=welch(src,sr,nperseg=4096)
g=np.sqrt(Pt/(Ps+1e-15))
# smooth in 1/3 octave
gs=np.ones_like(g)
for i,fc in enumerate(f):
    if fc<60: gs[i]=1; continue
    m=(f>=fc/2**(1/6))&(f<=fc*2**(1/6)); gs[i]=np.exp(np.mean(np.log(g[m]+1e-9)))
gdb=20*np.log10(gs); gdb=np.clip(gdb,-6,float(sys.argv[3]) if len(sys.argv)>3 else 12)
gdb[f>15000]=np.minimum(gdb[f>15000],0)
# normalise so 300-1000Hz ~ 0 dB
ref=np.mean(gdb[(f>300)&(f<1000)]); gdb-=ref
fs,ts,Z=stft(src,sr,nperseg=4096)
G=10**(np.interp(fs,f,gdb)/20)
_,y=istft(Z*G[:,None],sr,nperseg=4096)
y=y[:len(src)]; y=y/np.abs(y).max()*0.9
w=wave.open(sys.argv[2],'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((y*32767).astype(np.int16).tobytes()); w.close()
print(sys.argv[1], 'gain dB at 2k,4k,6k,8k,12k:', [round(float(np.interp(x,f,gdb)),1) for x in [2000,4000,6000,8000,12000]])
