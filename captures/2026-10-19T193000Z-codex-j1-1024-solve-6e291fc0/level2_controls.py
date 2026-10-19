"""Isolated malformed/under-solved witness rejection controls."""
from pathlib import Path
import json,subprocess,copy,tempfile,sys
w=json.loads(Path(sys.argv[1]).read_text());runner=Path(sys.argv[2]).resolve();records=[]
for name in ['zero_state','nonfinite_word','truncated_low_word']:
 x=copy.deepcopy(w)
 if name=='zero_state':
  for key in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']:x['fixtures'][2][key]=['0x0.0p+0']*284
 elif name=='nonfinite_word':x['fixtures'][0]['hi_real_hex'][0]='nan'
 else:x['fixtures'][0]['low_real_hex']=x['fixtures'][0]['low_real_hex'][:-1]
 with tempfile.TemporaryDirectory() as td:
  Path(td,'WITNESS.json').write_text(json.dumps(x));r=subprocess.run([sys.executable,str(runner),td],capture_output=True,text=True)
  assert r.returncode!=0,name+' accepted'
  token={'zero_state':'raw algebraic1e-10 budget','nonfinite_word':'cannot convert NaN','truncated_low_word':'AssertionError'}[name];assert token in r.stderr,(name,r.stderr)
  records.append({'name':name,'rejected':True,'diagnostic':r.stderr.splitlines()[-1]})
print(json.dumps({'status':'PASS','expected_rejections':records},indent=2))
