import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (255, 255, 255)
BODY_END = T[-1][1] + 0.6
SLAM = T[3][0] + 0.05
TICKS = None
HOOK = dict(pill='ഒരു ഉദാഹരണം', a_text='MEETING: PERFECT', size_a=104, a_col='W',
            b_label='CUSTOMER', b_static='HAPPY', b_start=T[1][0] - 0.15, b_col1='G',
            label_size=64, label_col='G', label_y=840,
            slam_text='ASKED FOR ORDER: NO', size_s=86)
LINES = [
 (T[5], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'ജിദ്ദയിലെ ഒരു restaurant chain.')])]),
 (T[6], 1, [('big', [('W', '8 branches-ന് attendance system. '), ('Y', '96,000 റിയാൽ.')])]),
 (T[7], 2, [('big', [('W', 'Owner: '), ('Y', '"Good presentation. നോക്കാം."')])]),
 (T[8], 2, [('big', [('W', 'Anoop: "Thank you, sir." '), ('R', 'നേരെ car-ലേക്ക്.')])]),
 (T[9], 3, [('big', [('W', 'Anoop കേട്ടത്: '), ('G', '"Yes."')])]),
 (T[10], 3, [('big', [('W', 'Owner ഉദ്ദേശിച്ചത്: '), ('R', '"Competitor-നെയും ഒന്ന് നോക്കാം."')])]),
 (T[11], 4, [('big', [('W', 'രണ്ടാഴ്ച കഴിഞ്ഞ് order '), ('R', 'competitor-ന്.')])]),
 (T[12], 4, [('big', [('W', 'അവർ '), ('Y', 'അന്ന് തന്നെ order ചോദിച്ചു.')])]),
 (T[13], 5, [('small', [('W', 'Basheer sir ചോദിച്ചു: "എന്തുകൊണ്ട് order ചോദിച്ചില്ല?"')])]),
 (T[14], 5, [('small', [('W', 'Anoop തല താഴ്ത്തി:')]), ('big', [('R', '"No കേൾക്കാൻ പേടിയായിരുന്നു, sir."')])]),
 (T[15], 6, [('small', [('W', 'Ismail എല്ലാ meeting-ഉം ഒരു ചോദ്യത്തോടെ തീർക്കും:')])]),
 (T[16], 6, [('big', [('G', '"Sir, ഈ മാസം start ചെയ്യാമോ? ഇല്ലെങ്കിൽ, എന്താണ് തടസ്സം?"')])]),
 (T[17], 6, [('big', [('W', '"Yes" കിട്ടിയാൽ '), ('G', 'order.')])]),
 (T[18], 6, [('small', [('W', '"No" കിട്ടിയാൽ, എന്താണ് മാറ്റേണ്ടത് എന്ന് അറിയാം. '), ('G', 'രണ്ടും ജയമാണ്.')])]),
 (T[19], 7, [('small', [('W', 'Order ചോദിക്കാനുള്ള 5 closing lines വേണോ?')])]),
 (T[20], 7, [('big', [('Y', 'ASK '), ('W', 'എന്ന് comment ചെയ്യൂ.')])]),
 (T[21], 7, [('big', [('G', 'ഞാൻ DM ചെയ്യാം.')])]),
]
exec(open('reels/fu_v2/hook_fu.py').read())
