import sys, subprocess
from PIL import Image, ImageDraw, ImageFont
r,mp4,t=sys.argv[1],sys.argv[2],sys.argv[3]
subprocess.run(['ffmpeg','-v','error','-y','-ss',t,'-i',mp4,'-frames:v','1',f'/tmp/w/{r}/late.png'],check=True)
pb=Image.open(f'/tmp/w/{r}/late.png').convert('RGB').crop((70,1300,800,1590))
bg=Image.open(f'/tmp/w/{r}/assets/bg.png').convert('RGB')
pb.paste(bg.crop((70+292,1300+84,70+705,1300+137)),(292,84))
f=ImageFont.truetype('/tmp/ssp/kit/fonts/notoml.ttf',40,layout_engine=ImageFont.Layout.RAQM)
ax=f.get_variation_axes(); f.set_variation_by_axes([800 if a['name'] in (b'Weight','Weight') else 100 for a in ax])
ImageDraw.Draw(pb).text((301,89),'Shajal Speaks',font=f,fill=(255,255,255))
pb.save(f'/tmp/w/{r}/assets/photo_block.png')
