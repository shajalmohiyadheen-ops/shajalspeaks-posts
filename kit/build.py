import numpy as np, wave, subprocess, math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
OFF = 3.04            # trim leading silence from recording
LEAD = 0.25           # text leads voice
BODY_END = 46.0       # end card starts here
A = 'assets/'
ANEK = 'fonts/anek.ttf'; NOTO = 'fonts/notoml.ttf'
MONT = '/usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf'

C = dict(W=(255, 255, 255), Y=(255, 196, 0), R=(255, 59, 65), G=(43, 196, 106), D=(150, 150, 150))

def font(path, size, wght, wdth=100):
    f = ImageFont.truetype(path, size, layout_engine=ImageFont.Layout.RAQM)
    axes = f.get_variation_axes()
    vals = [wght if a['name'] in (b'Weight', 'Weight') else wdth for a in axes]
    try:
        f.set_variation_by_axes(vals)
    except Exception:
        f.set_variation_by_axes([wght, wdth])
    return f

BIG = font(ANEK, 68, 800)
SMALL = font(NOTO, 44, 700)

# ---------------- script ----------------
# each line: (start,end in trimmed seconds, step, [blocks]); block = (style, [(color,text),...]) ; style 'big'|'small'|'pill'
def t(a, b): return (a - OFF, b - OFF)
LINES = [
    (t(6.62, 8.46), 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'ദമ്മാമിലെ ഒരു contractor.')])]),
    (t(8.90, 10.22), 1, [('big', [('W', 'Quotation: '), ('Y', 'രണ്ട് ലക്ഷം റിയാൽ')])]),
    (t(10.74, 14.14), 1, [('big', [('W', 'Margin '), ('Y', '12%.'), ('W', 'Profit: '), ('Y', '24,000 റിയാൽ')])]),
    (t(14.88, 17.32), 2, [('small', [('W', 'ആദ്യ meeting-ൽ തന്നെ customer ചോദിച്ചു:')]), ('big', [('Y', '"Best price?"')])]),
    (t(17.88, 19.88), 2, [('big', [('W', 'Anoop ഉടനെ: '), ('R', '"10% കുറയ്ക്കാം, sir."')])]),
    (t(20.78, 22.90), 3, [('big', [('W', '10% discount = '), ('R', '20,000 റിയാൽ')])]),
    (t(23.54, 25.56), 3, [('big', [('W', 'Profit '), ('Y', '24,000-ൽ'), ('W', 'നിന്ന് '), ('R', '4,000'), ('W', ' ആയി.')])]),
    (t(26.28, 28.58), 3, [('big', [('R', 'Profit-ന്റെ 83%'), ('W', ' ഒരു വാക്കിൽ പോയി.')])]),
    (t(29.12, 30.30), 4, [('small', [('W', 'Customer-ന് ഒരു കാര്യം മനസ്സിലായി:')])]),
    (t(30.50, 31.60), 4, [('big', [('R', 'ചോദിച്ചാൽ ഇനിയും കുറയും.')])]),
    (t(32.16, 33.36), 4, [('big', [('W', 'അടുത്ത order-ലും '), ('R', 'ഇതേ കളി.')])]),
    (t(34.02, 37.06), 5, [('small', [('W', 'Discount ആദ്യം കൊടുക്കരുത്.')]), ('big', [('G', 'Value'), ('W', ' ആദ്യം കാണിക്കുക.')])]),
    (t(37.36, 39.34), 6, [('big', [('W', 'Discount ചോദിച്ചാൽ, '), ('G', 'പകരം എന്തെങ്കിലും വാങ്ങുക.')])]),
    (t(39.62, 42.48), 6, [('big', [('G', 'Advance,'), ('G', 'വലിയ quantity,'), ('W', 'അല്ലെങ്കിൽ'), ('G', 'long-term order.')])]),
    (t(43.10, 43.94), 7, [('small', [('W', 'നിങ്ങളോട് എന്റെ ചോദ്യം:')])]),
    (t(44.42, 47.32), 7, [('big', [('W', 'അവസാനത്തെ deal-ൽ ചോദിക്കാതെ കൊടുത്ത '), ('Y', 'discount എത്ര?')])]),
    (t(47.74, 48.38), 7, [('big', [('Y', 'ഒന്ന് ആലോചിക്കൂ.')])]),
]

# ---------------- layout ----------------
X0, MAXW, Y0 = 90, 900, 520
def words_of(block):
    out = []
    for col, txt in block[1]:
        parts = txt.split(' ')
        for i, p in enumerate(parts):
            if p == '': continue
            out.append((col, p))
    return out

def render_word(fnt, txt, col):
    bb = fnt.getbbox(txt)
    im = Image.new('RGBA', (bb[2] + 8, fnt.size * 2), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((4, 0), txt, font=fnt, fill=C[col] + (255,))
    return im

class Word: pass

def layout_line(line, ytop):
    """returns list of Word with img,x,y, block heights; and next y"""
    (s, e), step, blocks = line
    ws = []
    y = ytop
    for blk in blocks:
        style = blk[0]
        if style == 'pill':
            f = font(NOTO, 36, 800)
            txt = blk[1][0][1]
            bb = f.getbbox(txt)
            pw, ph = bb[2] + 44, 62
            im = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
            d = ImageDraw.Draw(im)
            d.rounded_rectangle((0, 0, pw - 1, ph - 1), radius=31, fill=(255, 196, 0, 210))
            d.text((22, 30), txt, font=f, fill=(20, 20, 20, 255), anchor='lm')
            w = Word(); w.img = im; w.x = X0; w.y = y; w.chars = len(txt); ws.append(w)
            y += ph + 22
            continue
        f = BIG if style == 'big' else SMALL
        lh = int(f.size * 1.22)
        sp = f.getlength(' ')
        x = X0
        for col, wd in words_of(blk):
            wl = f.getlength(wd)
            if x > X0 and x + wl > X0 + MAXW:
                x = X0; y += lh
            w = Word(); w.img = render_word(f, wd, col); w.x = x - 4; w.y = y - int(f.size * 0.18); w.chars = len(wd)
            ws.append(w)
            x += wl + sp
        y += lh + (14 if style == 'small' else 18)
    # word timings: spread over spoken span by char weight
    tot = sum(w.chars for w in ws)
    acc = 0
    for w in ws:
        w.t = s - LEAD + (e - s) * 0.9 * acc / tot
        acc += w.chars
    return ws, y

# group by step; place lines sequentially, shifting up if overflow
STEP_START = {}
PLACED = []   # (line_index, words, step)
for step in range(1, 8):
    idx = [i for i, l in enumerate(LINES) if l[1] == step]
    y = Y0
    for i in idx:
        ws, y2 = layout_line(LINES[i], y)
        PLACED.append((i, ws, step))
        y = y2 + 10
    if y > 1250:
        print('WARN overflow step', step, y)
    STEP_START[step] = LINES[idx[0]][0][0] - LEAD - 0.05
step_of_time = lambda tt: max([s for s, st in STEP_START.items() if st <= tt], default=0)

# ---------------- static assets ----------------
bg = Image.open(A + 'bg.png').convert('RGB')
photo = Image.open(A + 'photo_block.png').convert('RGB')
footer = Image.open(A + 'footer.png').convert('RGB')
labf = font(MONT, 30, 700)

def label_img(step):
    im = Image.new('RGBA', (420, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 24, 12, 36), fill=(255, 59, 60, 255))
    x = 24
    for ch in f'STEP {step:02d} / 07':
        d.text((x, 30), ch, font=labf, fill=(255, 59, 60, 255), anchor='lm'); x += labf.getlength(ch) + 4
    return im
LABELS = {s: label_img(s) for s in range(1, 8)}

# voice envelope
wv = wave.open('voice_trim.wav'); sr = wv.getframerate()
xs = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(float) / 32768
def env(tt):
    i = int(tt * sr); n = int(sr / FPS)
    seg = xs[max(0, i - n):i + n]
    if len(seg) == 0: return 0
    db = 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9)
    return float(np.clip((db + 48) / 30, 0, 1))
ENV = [env(f / FPS) for f in range(int(BODY_END * FPS) + 2)]
sm = 0; ENVS = []
for v in ENV:
    sm = sm + (v - sm) * (0.6 if v > sm else 0.25); ENVS.append(sm)

# ---------------- hook ----------------
HF1 = font(ANEK, 128, 800)
HF2 = font(ANEK, 120, 800)
HF3 = font(ANEK, 140, 800)
HSM = font(NOTO, 44, 700)
SLAM = 1.50   # "83%" spoken ~4.56 raw -> 1.52 trimmed
def hook_layer(tt):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    # pill
    pf = font(NOTO, 34, 800); txt = 'ഒരു ഉദാഹരണം'
    pw = int(pf.getlength(txt)) + 44
    d.rounded_rectangle((X0, 520, X0 + pw, 580), radius=30, fill=(255, 196, 0, 200))
    d.text((X0 + 22, 550), txt, font=pf, fill=(20, 20, 20, 255), anchor='lm')
    d.text((X0, 730), '10% DISCOUNT', font=HF1, fill=C['Y'] + (255,), anchor='ls')
    # counter
    if tt >= 0.55:
        d.text((X0, 830), 'PROFIT', font=HSM, fill=(170, 170, 170, 255), anchor='ls')
        p = np.clip((tt - 0.7) / (SLAM - 0.08 - 0.7), 0, 1)
        p = 1 - (1 - p) ** 2
        val = int(round((24000 - 20000 * p) / 10) * 10)
        col = tuple(int(a + (b - a) * p) for a, b in zip((255, 255, 255), C['R']))
        d.text((X0, 960), f'SAR {val:,}', font=HF2, fill=col + (255,), anchor='ls')
    if tt >= SLAM:
        k = np.clip((tt - SLAM) / 0.12, 0, 1)
        sc = 1.7 - 0.7 * (1 - (1 - k) ** 3)
        txt = '−83% PROFIT'
        tw = int(HF3.getlength(txt)) + 20
        im = Image.new('RGBA', (tw, 200), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 165), txt, font=HF3, fill=C['R'] + (255,), anchor='ls')
        if sc != 1:
            im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        a = int(255 * min(1, k * 2.5))
        if a < 255:
            im.putalpha(im.getchannel('A').point(lambda v: v * a // 255))
        # anchor left baseline at (X0, 1060)
        L.alpha_composite(im, (int(X0 - (im.width - tw) * 0.0), int(1170 - 165 * sc)))
    return L

def shake(tt):
    if SLAM <= tt < SLAM + 0.3:
        a = 14 * (1 - (tt - SLAM) / 0.3)
        rnd = random.Random(int(tt * 1000))
        return int(rnd.uniform(-a, a)), int(rnd.uniform(-a, a))
    return 0, 0

# ---------------- frames ----------------
def ease(x): return 1 - (1 - x) ** 3

def frame(fi):
    tt = fi / FPS
    canvas = bg.copy().convert('RGBA')
    dx, dy = shake(tt)
    HOOK_OUT = STEP_START[1] - 0.35
    if tt < HOOK_OUT + 0.25:
        L = hook_layer(tt)
        if tt > HOOK_OUT:
            a = 1 - (tt - HOOK_OUT) / 0.25
            L.putalpha(L.getchannel('A').point(lambda v: int(v * a)))
        canvas.alpha_composite(L, (dx, dy))
    # text of current step
    st = step_of_time(tt)
    # exit of previous step: slide left + fade over 0.22s
    if st and st > 1 and tt - STEP_START[st] < 0.22:
        k = (tt - STEP_START[st]) / 0.22
        prevL = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for i, ws, s in PLACED:
            if s != st - 1: continue
            for w in ws:
                prevL.alpha_composite(w.img, (int(w.x), int(w.y)))
        prevL = prevL.filter(ImageFilter.BoxBlur(int(1 + 10 * k)))
        prevL.putalpha(prevL.getchannel('A').point(lambda v: int(v * 0.55 * (1 - k))))
        canvas.alpha_composite(prevL, (int(-140 * ease(k)), 0))
    if st:
        enter_k = min(1, (tt - STEP_START[st]) / 0.25)
        slide = int(90 * (1 - ease(enter_k)))
        for i, ws, s in PLACED:
            if s != st: continue
            # dim if a later line in this step has started
            later = [LINES[j][0][0] - LEAD for j, _, s2 in PLACED if s2 == st and j > i]
            dim = any(tt >= l for l in later)
            for w in ws:
                if tt < w.t: continue
                k = min(1, (tt - w.t) / 0.18)
                img = w.img
                alpha = min(1, ease(k) * 1.6) * (0.42 if dim else 1.0)
                sc = 1.45 - 0.45 * ease(k)
                if k < 1:
                    br = 7 * (1 - ease(k))
                    if br > 0.4:
                        img = img.filter(ImageFilter.GaussianBlur(br))
                if sc != 1:
                    img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BILINEAR)
                if alpha < 1:
                    img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * alpha)))
                ox = int(w.x - (img.width - w.img.width) / 2) + slide; oy = int(w.y - (img.height - w.img.height) / 2)
                canvas.alpha_composite(img, (ox, oy))
    # chrome (label, photo, line, dashes, footer) fades in at 3.0s
    ca = np.clip((tt - (STEP_START[1] - 0.25)) / 0.3, 0, 1)
    if ca > 0:
        ch = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        if st: ch.alpha_composite(LABELS[st], (90, 217))
        ch.paste(photo.convert('RGBA'), (70, 1300))
        d = ImageDraw.Draw(ch)
        v = ENVS[min(fi, len(ENVS) - 1)]
        half = int(20 + 100 * v)
        d.rounded_rectangle((215 - half, 1600, 215 + half, 1614), radius=7, fill=(255, 196, 0, 255))
        for k in range(7):
            x = 90 + 58 * k
            d.rectangle((x, 1662, x + 45, 1669), fill=(255, 196, 0, 255) if k < st else (51, 51, 51, 255))
        if ca < 1:
            ch.putalpha(ch.getchannel('A').point(lambda q: int(q * ca)))
        canvas.alpha_composite(ch)
    canvas.alpha_composite(footer.convert('RGBA'), (70, 1720))
    return canvas.convert('RGB')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'stills':
        for tt in map(float, sys.argv[2:]):
            frame(int(tt * FPS)).save(f'stills/s_{tt:05.2f}.png')
        sys.exit()
    n = int(BODY_END * FPS)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', 'body.mp4'], stdin=subprocess.PIPE)
    for fi in range(n):
        p.stdin.write(frame(fi).tobytes())
        if fi % 150 == 0: print(fi, flush=True)
    p.stdin.close(); p.wait()
