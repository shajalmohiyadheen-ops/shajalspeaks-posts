import os, sys, json, subprocess, importlib.util
r=sys.argv[1]; W='/tmp/w/'+r; os.environ['CFG']=W+'/cfg.py'; sys.argv=['x']
spec=importlib.util.spec_from_file_location('b','build2.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
m=json.load(open(W+'/meta.json')); n=round(m['cut_new']*30)
for tt in (0.0,0.9,1.6,2.3,2.6,3.3):
    b.frame(int(tt*30)).save(f'{W}/s_{tt:.1f}.png')
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',W+'/hook.mp4'],stdin=subprocess.PIPE)
for fi in range(n): p.stdin.write(b.frame(fi).tobytes())
p.stdin.close(); p.wait(); print(r,'hook frames',n,'SLAM',round(b.SLAM,2),'STEP1',round(b.STEP_START[1],2))
