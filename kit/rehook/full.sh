r=$1; K=/tmp/w/$r; cd /tmp/ssp/kit
CFG=$K/cfg.py python3 build2.py 2>&1 | grep -v -E "WARN|^[0-9]+$"
ffmpeg -v error -y -i $K/body.mp4 -i assets/endcard.mov -i $K/audio.wav -filter_complex "[0:v]fps=30,format=yuv420p,setsar=1[v0];[1:v]fps=30,format=yuv420p,setsar=1[v1];[v0][v1]concat=n=2:v=1:a=0[v]" -map "[v]" -map 2:a -c:v libx264 -preset veryfast -crf 19 -c:a aac -b:a 160k -movflags +faststart -shortest $K/reel_full.mp4
echo $r done $(ffprobe -v error -show_entries format=duration -of csv=p=0 $K/reel_full.mp4)
