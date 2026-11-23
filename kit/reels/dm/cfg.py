import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (89, 184, 125)
BODY_END = T[-1][1] + 0.6
SLAM = T[2][0] + 0.45
TICKS = (T[1][0], SLAM - 0.08)
HOOK = dict(b_label='', pill='ഒരു ഉദാഹരണം', a_text='14 MEETINGS', a_col='Y', b_from=0, b_to=90, b_fmt=lambda v: f'{int(round(v))} ദിവസം', b_start=T[1][0] - 0.2, b_col0='W', b_col1='W', slam_text='ORDER: 0')
LINES = [
 (T[3], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'റിയാദിലെ ഒരു hospital.')])]),
 (T[4], 1, [('big', [('W', 'Anoop-ന്റെ contact: '), ('Y', 'Procurement-ലെ Joseph sir.')])]),
 (T[5], 2, [('small', [('W', 'എല്ലാ meeting-ലും അദ്ദേഹം പറഞ്ഞു:')]), ('big', [('Y', '"Good proposal. Next week നോക്കാം."')])]),
 (T[6], 3, [('small', [('W', '90 ദിവസം കഴിഞ്ഞ് Anoop അറിഞ്ഞു:')])]),
 (T[7], 3, [('big', [('W', 'Order sign ചെയ്യുന്നത് '), ('R', 'Joseph sir അല്ല.')])]),
 (T[8], 3, [('big', [('Y', 'Facility Director'), ('W', 'ആണ്. അദ്ദേഹം Anoop-നെ '), ('R', 'ഒരിക്കൽ പോലും കണ്ടിട്ടില്ല.')])]),
 (T[9], 4, [('big', [('W', 'ആ സമയത്ത് '), ('R', 'competitor'), ('W', 'നേരെ Director-നെ കണ്ടു.')])]),
 (T[10], 4, [('big', [('R', 'Order അവർക്ക് പോയി.')])]),
 (T[11], 5, [('small', [('W', 'Manager ചോദിച്ചു:')]), ('big', [('Y', '"ആരാണ് sign ചെയ്യുന്നത്?"')])]),
 (T[12], 5, [('big', [('R', 'Anoop-ന് ഉത്തരം ഇല്ലായിരുന്നു.')])]),
 (T[13], 6, [('small', [('W', 'ആദ്യ meeting-ൽ തന്നെ ചോദിക്കുക:')])]),
 (T[14], 6, [('big', [('G', '1. ആരാണ് decision എടുക്കുന്നത്?')])]),
 (T[15], 6, [('big', [('G', '2. Budget ആരുടെ കയ്യിലാണ്?')])]),
 (T[16], 6, [('big', [('G', '3. Order എപ്പോൾ വേണം?')])]),
 (T[17], 7, [('small', [('W', 'നിങ്ങളോട് എന്റെ ചോദ്യം:')])]),
 (T[18], 7, [('big', [('W', 'നിങ്ങളുടെ ഏറ്റവും വലിയ deal-ൽ, '), ('Y', 'sign ചെയ്യുന്ന ആളെ'), ('W', 'നിങ്ങൾ കണ്ടിട്ടുണ്ടോ?')])]),
 (T[19], 7, [('big', [('G', 'ഒന്ന് ആലോചിക്കൂ.')])]),
]
exec(open('common/hook.py').read())
