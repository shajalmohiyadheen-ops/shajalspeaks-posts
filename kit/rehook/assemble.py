import os, sys, json, wave, subprocess, numpy as np, importlib.util
r=sys.argv[1]; W='/tmp/w/'+r; os.environ['CFG']=W+'/cfg.py'; sys.argv=['x']
spec=importlib.util.spec_from_file_location('b','build2.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
P=json.load(open('/tmp/w/scripts/params.json'))[r]; m=json.load(open(W+'/meta.json')); sr=44100
def load(p):
    w=wave.open(p); return np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768
hv=load(W+'/hookvoice.wav'); n=len(hv); out=np.zeros(n)
def put(sig,t,g):
    j=int(t*sr); L=min(len(sig),n-j)
    if L>0: out[j:j+L]+=sig[:L]*g
th=load('common/thud.wav')[int(0.17*sr):]
if b.TICKS:
    t=b.TICKS[0]; kk=0; times=[]
    while t<b.TICKS[1]: times.append(t); kk+=1; t+=max(0.028,0.075-0.004*kk)
    for i,tt in enumerate(times):
        fq=2200-1100*i/len(times); L=int(0.018*sr)
        put(np.sin(2*np.pi*fq*np.arange(L)/sr)*np.exp(-np.arange(L)/(0.004*sr)),tt,0.34)
put(th,b.SLAM,1.35)
hk=hv+out; pk=np.abs(hk).max()
raw=subprocess.run(['ffmpeg','-v','error','-f','f32le','-ar','44100','-ac','1','-i','-','-af','alimiter=limit=0.95:attack=1:release=50:level=disabled','-f','f32le','-'],input=hk.astype(np.float32).tobytes(),capture_output=True).stdout
hk=np.frombuffer(raw,np.float32).astype(float)[:n]
if len(hk)<n: hk=np.pad(hk,(0,n-len(hk)))
old=load(P['old_wav'])[int(m['cut_old']*sr):]
y=np.concatenate([hk,old])
w=wave.open(W+'/audio.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes()); w.close()
fo=round(m['cut_old']*30)
subprocess.run(['ffmpeg','-v','error','-y','-i',W+'/hook.mp4','-i',P['old_mp4'],'-i',W+'/audio.wav','-filter_complex',
 f'[1:v]trim=start_frame={fo},setpts=PTS-STARTPTS,fps=30,format=yuv420p,setsar=1[o];[0:v]fps=30,format=yuv420p,setsar=1[h];[h][o]concat=n=2:v=1:a=0[v]',
 '-map','[v]','-map','2:a','-c:v','libx264','-preset','veryfast','-crf','19','-c:a','aac','-b:a','160k','-movflags','+faststart','-shortest',W+'/reel.mp4'],check=True)
print(r,'pk',round(float(pk),2),subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',W+'/reel.mp4'],capture_output=True,text=True).stdout.strip(),'old',subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',P['old_mp4']],capture_output=True,text=True).stdout.strip())
