# Reel build kit (kinetic voice-over Reels)
- build.py: renders body.mp4 (1080x1920, 30fps) from LINES (timed to the voice recording, trimmed by OFF).
- Audio: voice loudnorm -16 LUFS; SFX = word taps (sfx/word_taps.npy, from Shajal's clip), clean whoosh on step changes (sfx/whoosh_clean.wav), opening counter ticks + stamp thud (assets/thud.wav); end card assets/endcard.mov appended (logo stamp + typewriter tagline).
- Do NOT reuse sound cut from Video 05: it contains his voice + BGM.
