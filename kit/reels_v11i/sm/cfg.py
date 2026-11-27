import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (255, 255, 255)
BODY_END = T[-1][1] + 0.6
SLAM = T[3][0] + 0.05
_BS = T[2][0] - 0.15
TICKS = (_BS + 0.1, SLAM - 0.1)
def _inr(v):
    n = int(round(v / 1000.0)) * 1000; s = str(n)
    if len(s) > 3:
        h, t = s[:-3], s[-3:]; parts = []
        while len(h) > 2: parts.insert(0, h[-2:]); h = h[:-2]
        if h: parts.insert(0, h)
        s = ','.join(parts) + ',' + t
    return 'SAR ' + s
HOOK = dict(pill='ഒരു ഉദാഹരണം', a_text='ENQUIRY: SAR 4,000', size_a=92, a_col='Y',
            b_label='5 YEARS LATER', b_from=4000, b_to=3000000, b_fmt=_inr, b_start=_BS,
            b_col0='W', b_col1='G', label_size=64, label_col='R', label_y=840,
            slam_text='NOT TO ANOOP', size_s=120)
LINES = [
 (T[4], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'റിയാദിലെ ഒരു ചെറിയ clinic. '), ('Y', '6 cameras.')])]),
 (T[5], 1, [('big', [('W', 'Admin Nikhil '), ('Y', 'മൂന്ന് തവണ വിളിച്ചു.')])]),
 (T[6], 2, [('big', [('W', 'Anoop: '), ('R', '"ഇത്ര ചെറിയ order-ന് സമയം ഇല്ല."')])]),
 (T[7], 3, [('big', [('W', 'നാലാം തവണ phone എടുത്തത് '), ('G', 'Ismail.')])]),
 (T[8], 3, [('big', [('G', 'പോയി. Install ചെയ്തു.')])]),
 (T[9], 3, [('small', [('W', 'Nikhil-ന്റെ ഓരോ സംശയത്തിനും WhatsApp-ൽ മറുപടി.')])]),
 (T[10], 4, [('big', [('W', 'അഞ്ച് വർഷം കഴിഞ്ഞ് Nikhil '), ('Y', 'ഒരു hospital group-ന്റെ procurement head.')])]),
 (T[11], 5, [('small', [('W', 'Order sign ചെയ്യുമ്പോൾ Nikhil പറഞ്ഞു:')])]),
 (T[12], 5, [('big', [('Y', '"എന്നെ ആരും കണക്കാക്കാത്ത കാലത്ത് Ismail വന്നു.')])]),
 (T[13], 5, [('big', [('G', 'അത് ഞാൻ മറന്നിട്ടില്ല."')])]),
 (T[14], 6, [('big', [('W', 'ചെറിയ customer എന്നൊന്നില്ല.')])]),
 (T[15], 6, [('big', [('G', 'ചെറിയ തുടക്കം മാത്രം.')])]),
 (T[16], 6, [('small', [('Y', 'Owners: '), ('W', 'ഓരോ enquiry-ക്കും 24 മണിക്കൂറിനുള്ളിൽ മറുപടി. ചെറുതായാലും.')])]),
 (T[17], 7, [('small', [('W', 'ആ 24-hour reply system വേണോ?')])]),
 (T[18], 7, [('big', [('Y', 'SMALL '), ('W', 'എന്ന് comment ചെയ്യൂ.')])]),
 (T[19], 7, [('big', [('G', 'ഞാൻ DM ചെയ്യാം.')])]),
]
exec(open('reels/fu_v2/hook_fu.py').read())
