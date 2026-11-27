import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (255, 255, 255)
BODY_END = T[-1][1] + 0.6
SLAM = T[2][0] + 0.05
_BS = T[1][0] - 0.15
TICKS = (_BS + 0.1, SLAM - 0.1)
HOOK = dict(pill='ഒരു ഉദാഹരണം', a_text='BEFORE ORDER: 20 CALLS', size_a=86, a_col='G',
            b_label='AFTER ORDER, CUSTOMER CALLED', b_from=0, b_to=20, b_fmt=lambda v: f'{int(round(v))} TIMES', b_start=_BS,
            b_col0='W', b_col1='R', label_size=52, label_col='R', label_y=840,
            slam_text='AMC LOST: SAR 1.35 LAKH', size_s=80)
LINES = [
 (T[3], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'ഖോബാറിലെ ഒരു hotel.')])]),
 (T[4], 1, [('big', [('W', 'Access control. AMC വർഷം '), ('Y', '45,000 റിയാൽ.')])]),
 (T[5], 2, [('big', [('W', 'Install കഴിഞ്ഞ് ഒരു '), ('R', 'door lock problem.')])]),
 (T[6], 2, [('big', [('W', 'രാത്രി 11 മണിക്ക് ഒരു family-ക്ക് '), ('R', 'room-ൽ കയറാൻ പറ്റിയില്ല.')])]),
 (T[7], 3, [('big', [('W', 'Anoop: '), ('R', '"Service team-നെ വിളിക്കൂ, sir. ഞാൻ new projects-ൽ busy ആണ്."')])]),
 (T[8], 4, [('small', [('W', 'Hotel GM Basheer sir-നോട് പറഞ്ഞു:')])]),
 (T[9], 4, [('big', [('W', '"ഞങ്ങൾ വാങ്ങിയത് system അല്ല. '), ('Y', 'നിങ്ങളുടെ ആളെ ആണ് വിശ്വസിച്ചത്."')])]),
 (T[10], 5, [('big', [('W', 'AMC '), ('R', 'മറ്റൊരു company-ക്ക്.')])]),
 (T[11], 5, [('big', [('W', '3 വർഷം: '), ('R', '1.35 ലക്ഷം റിയാൽ.')])]),
 (T[12], 6, [('small', [('W', 'Ismail install കഴിഞ്ഞ് മൂന്ന് തവണ വിളിക്കും:')])]),
 (T[13], 6, [('big', [('G', 'ഒന്നാം ആഴ്ച, ഒന്നാം മാസം, മൂന്നാം മാസം.')])]),
 (T[14], 6, [('small', [('W', 'Problem ഇല്ലെങ്കിലും.')])]),
 (T[15], 6, [('big', [('W', 'Ismail-ന്റെ അടുത്ത order പലപ്പോഴും '), ('G', 'ആ calls-ൽ നിന്നാണ് വരുന്നത്.')])]),
 (T[16], 7, [('small', [('W', 'Order-ന് ശേഷമുള്ള 3-call plan വേണോ?')])]),
 (T[17], 7, [('big', [('Y', 'SERVICE '), ('W', 'എന്ന് comment ചെയ്യൂ.')])]),
 (T[18], 7, [('big', [('G', 'ഞാൻ DM ചെയ്യാം.')])]),
]
exec(open('reels/fu_v2/hook_fu.py').read())
