k=$1
BE=$(python3 -c "import json;T=json.load(open('$k/times_c.json'));print(round(T[-1][1]+0.6,3))")
ffmpeg -v error -y -i $k/voice_eq.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11,apad=whole_dur=$BE" -ar 44100 -ac 1 -t $BE $k/vn.wav
ffmpeg -v error -y -i $k/vn.wav -i $k/sfx.wav -filter_complex "[0][1]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95" -ac 1 $k/body_a.wav
ffmpeg -v error -y -i $k/body.mp4 -i $k/body_a.wav -i $k/assets/endcard.mov -filter_complex "[0:v]fps=30,format=yuv420p,setsar=1[v0];[2:v]fps=30,format=yuv420p,setsar=1[v1];[1:a]aformat=sample_rates=44100:channel_layouts=mono[a0];[2:a]aformat=sample_rates=44100:channel_layouts=mono[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -preset veryfast -crf 19 -c:a aac -b:a 160k -movflags +faststart $k/reel_v8.mp4
echo $k reel $(ffprobe -v error -show_entries format=duration -of csv=p=0 $k/reel_v8.mp4) body $(ffprobe -v error -show_entries format=duration -of csv=p=0 $k/body.mp4) audio $(ffprobe -v error -show_entries format=duration -of csv=p=0 $k/body_a.wav)
