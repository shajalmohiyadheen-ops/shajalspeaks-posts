import json as _j
T = _j.load(open(K + '/times_c.json'))
LABEL_RGB = (255, 255, 255)
BODY_END = T[-1][1] + 0.6
SLAM = T[2][0] + 0.45
TICKS = None
HOOK = dict(pill=None, a_text='QUOTATION SENT', size_a=112, a_col='Y', b_label='PRICE', b_static='ശരിയായിരുന്നു', b_start=T[1][0] - 0.2, b_col1='G', slam_text='ORDER: LOST', size_s=132)
LINES = [
 (T[3], 1, [('pill', [('Y', 'ഒരു ഉദാഹരണം')]), ('big', [('W', 'ദമ്മാമിലെ ഒരു school.')])]),
 (T[4], 1, [('big', [('W', 'CCTV project. Quotation: '), ('Y', '80,000 റിയാൽ.')])]),
 (T[5], 2, [('big', [('W', 'Anoop quotation email ചെയ്തു.')])]),
 (T[6], 2, [('big', [('W', 'എന്നിട്ട് കാത്തിരുന്നു. '), ('Y', '"Customer വിളിക്കും."')])]),
 (T[7], 3, [('small', [('W', 'രണ്ടാഴ്ച കഴിഞ്ഞ് Anoop വിളിച്ചു.')])]),
 (T[8], 3, [('big', [('R', '"Sorry, order മറ്റൊരു company-ക്ക് കൊടുത്തു."')])]),
 (T[9], 4, [('big', [('W', 'Competitor-ന്റെ price '), ('Y', 'നമ്മളേക്കാൾ കൂടുതലായിരുന്നു.')])]),
 (T[10], 4, [('big', [('W', 'പക്ഷേ അവർ '), ('G', 'മൂന്ന് തവണ വിളിച്ചു,'), ('G', 'ഒരിക്കൽ site-ൽ വന്നു.')])]),
 (T[11], 5, [('small', [('W', 'Manager പറഞ്ഞു:')])]),
 (T[12], 5, [('big', [('W', '"Quotation അയക്കുന്നത് sales അല്ല. '), ('G', 'Follow-up ആണ് sales."')])]),
 (T[13], 6, [('big', [('G', '1. Quotation കൊടുക്കുമ്പോൾ തന്നെ next meeting date fix ചെയ്യുക.')])]),
 (T[14], 6, [('big', [('G', '2. 48 മണിക്കൂറിനുള്ളിൽ വിളിക്കുക.')])]),
 (T[15], 6, [('big', [('G', '3. Customer-ന്റെ doubt എന്താണെന്ന് ചോദിക്കുക.')])]),
 (T[16], 7, [('small', [('W', 'നിങ്ങളോട് എന്റെ ചോദ്യം:')])]),
 (T[17], 7, [('big', [('W', 'ഇപ്പോൾ എത്ര '), ('Y', 'quotation-കൾ'), ('W', 'മറുപടി കാത്ത് കിടക്കുന്നു?')])]),
 (T[18], 7, [('big', [('R', 'ഒന്ന് ആലോചിക്കൂ.')])]),
]
exec(open('common/hook.py').read())
