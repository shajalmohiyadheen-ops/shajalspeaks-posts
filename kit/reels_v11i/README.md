# v11 week rebuilt 27 Nov (Anees -> Ismail), re-recorded audio
Per reel: cfg.py, lines.json (spoken units), times_c.json (aligned + gap-compressed), bg.png.
To rebuild one (k = ho2|sm|ask|sv): copy folder to kit/reels/<k>, add assets/ (bg.png, photo_block_rgba.png as photo_block.png, footer_rgba.png as footer.png, assets/endcard.mov), old.wav (recording, mono 44.1k), then:
  python3 prep18.py reels/<k> <voice_end_s> <hook_units>   # ho2/sm: 4, ask: 5, sv: 3
  ffmpeg -i reels/<k>/voice_c.wav -af "highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=10:release=150" reels/<k>/voice_eq.wav
  NOTAPS=1 python3 mix_ho.py reels/<k>; CFG=reels/<k>/cfg.py python3 build_ho.py; bash assemble.sh reels/<k>
cfg.py execs reels/fu_v2/hook_fu.py (hook layer). build_ho.py = build2.py with RGBA photo/footer.
