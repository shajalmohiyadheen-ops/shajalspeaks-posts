import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (255, 255, 255)
BODY_END = T[-1][1] + 0.6
SLAM = T[3][0] + 0.05
_BS = T[1][0] - 0.15
TICKS = (_BS + 0.1, SLAM - 0.1)
HOOK = dict(pill='ഒരു ഉദാഹരണം', a_text='ANOOP: ON LEAVE', size_a=104, a_col='Y',
            b_label='MISSED CALLS', b_from=0, b_to=14, b_fmt=lambda v: str(int(round(v))), b_start=_BS,
            b_col0='W', b_col1='R', label_size=64, label_col='R', label_y=840,
            slam_text='ORDER: COMPETITOR', size_s=100)
LINES = [
 (T[4], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'റിയാദിലെ ഒരു logistics company.')])]),
 (T[5], 1, [('big', [('W', 'Access control: '), ('Y', '2.4 ലക്ഷം റിയാൽ.')])]),
 (T[6], 2, [('small', [('W', 'PO-ക്ക് മുമ്പ് customer-ന്')]), ('big', [('Y', 'ഒരു ചെറിയ clarification മാത്രം വേണമായിരുന്നു.')])]),
 (T[7], 2, [('big', [('W', 'Office-ൽ '), ('R', 'ആർക്കും '), ('W', 'ആ deal അറിയില്ല.')])]),
 (T[8], 3, [('big', [('W', 'File Anoop-ന്റെ '), ('Y', 'laptop-ൽ.')])]),
 (T[9], 3, [('big', [('W', 'Laptop Anoop-ന്റെ കൂടെ '), ('R', 'നാട്ടിൽ.')])]),
 (T[10], 4, [('small', [('W', 'മകളുടെ school annual day.')])]),
 (T[11], 4, [('big', [('W', 'Stage-ൽ അവൾ ഡാൻസ് ചെയ്യുമ്പോൾ Anoop-ന്റെ കണ്ണ് '), ('R', 'phone-ൽ ആയിരുന്നു.')])]),
 (T[12], 4, [('big', [('R', 'Order-ഉം പോയി.')])]),
 (T[13], 4, [('big', [('R', 'ആ നിമിഷവും പോയി.')])]),
 (T[14], 5, [('small', [('W', 'Ismail leave-ന് പോകുന്നതിന് മുമ്പ് ഒരു page എഴുതും:')])]),
 (T[15], 5, [('big', [('G', 'ഓരോ deal, contact, next step, ആര് നോക്കും.')])]),
 (T[16], 5, [('big', [('W', 'Leave സമയത്ത് Ismail-ന്റെ '), ('G', 'ഒരു deal-ഉം നിന്നില്ല.')])]),
 (T[17], 5, [('big', [('G', 'Phone-ഉം ശബ്ദിച്ചില്ല.')])]),
 (T[18], 6, [('small', [('Y', 'Owners:')]), ('big', [('W', 'handover ഇല്ലാതെ leave '), ('R', 'approve ചെയ്യരുത്.')])]),
 (T[19], 6, [('small', [('Y', 'Salespeople:')]), ('big', [('W', 'handover നിങ്ങളുടെ leave-നെയും '), ('G', 'രക്ഷിക്കും.')])]),
 (T[20], 7, [('small', [('W', 'Ismail-ന്റെ one-page handover format വേണോ?')])]),
 (T[21], 7, [('big', [('Y', 'HANDOVER '), ('W', 'എന്ന് comment ചെയ്യൂ.')])]),
 (T[22], 7, [('big', [('G', 'ഞാൻ DM ചെയ്യാം.')])]),
]
exec(open('reels/fu_v2/hook_fu.py').read())
