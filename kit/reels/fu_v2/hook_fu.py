# generic hook: HOOK = dict(pill, a_text, a_col, b_label, b_from, b_to, b_fmt, b_start, b_col0, b_col1, b_static, slam_text, size_a)
_HA = font(ANEK, HOOK.get('size_a', 124), 800)
_HB = font(ANEK, 116, 800)
_HS = font(ANEK, HOOK.get('size_s', 136), 800)
_HL = font(ANEK, HOOK.get('label_size', 44), 800) if HOOK.get('label_size') else font(NOTO, 44, 700)
_PF = font(NOTO, 34, 800)
def hook_layer(tt):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    if HOOK.get('pill'):
        txt = HOOK['pill']; pw = int(_PF.getlength(txt)) + 44
        d.rounded_rectangle((X0, 520, X0 + pw, 580), radius=30, fill=(255, 196, 0, 200))
        d.text((X0 + 22, 550), txt, font=_PF, fill=(20, 20, 20, 255), anchor='lm')
    d.text((X0, 730), HOOK['a_text'], font=_HA, fill=C[HOOK['a_col']] + (255,), anchor='ls')
    if tt >= HOOK['b_start']:
        d.text((X0, HOOK.get('label_y', 830)), HOOK['b_label'], font=_HL, fill=(C[HOOK['label_col']] if HOOK.get('label_col') else (170, 170, 170)) + (255,), anchor='ls')
        if HOOK.get('b_static'):
            k = min(1, (tt - HOOK['b_start']) / 0.15)
            col = C[HOOK['b_col1']] + (int(255 * k),)
            d.text((X0, HOOK.get('b_y', 960)), HOOK['b_static'], font=_HB, fill=col, anchor='ls')
        else:
            p = np.clip((tt - HOOK['b_start'] - 0.1) / (SLAM - 0.08 - HOOK['b_start'] - 0.1), 0, 1)
            p = 1 - (1 - p) ** 2
            v = HOOK['b_from'] + (HOOK['b_to'] - HOOK['b_from']) * p
            c0, c1 = C[HOOK['b_col0']], C[HOOK['b_col1']]
            col = tuple(int(a + (b - a) * p) for a, b in zip(c0, c1))
            d.text((X0, 960), HOOK['b_fmt'](v), font=_HB, fill=col + (255,), anchor='ls')
    if tt >= SLAM:
        k = np.clip((tt - SLAM) / 0.12, 0, 1)
        sc = 1.7 - 0.7 * (1 - (1 - k) ** 3)
        txt = HOOK['slam_text']; tw = int(_HS.getlength(txt)) + 20
        im = Image.new('RGBA', (tw, 200), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 165), txt, font=_HS, fill=C['R'] + (255,), anchor='ls')
        if sc != 1: im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        a = int(255 * min(1, k * 2.5))
        if a < 255: im.putalpha(im.getchannel('A').point(lambda v: v * a // 255))
        L.alpha_composite(im, (X0, int(1170 - 165 * sc)))
    return L
