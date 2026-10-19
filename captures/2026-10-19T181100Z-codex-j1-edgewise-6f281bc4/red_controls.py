"""Expected-rejection controls, each in an isolated temporary directory."""
import tempfile,subprocess,json,sys,copy
from pathlib import Path
w=json.loads(Path(sys.argv[1]).read_text());runner=Path(sys.argv[2]).resolve();records=[]
for name in ['under_solved_zero','nonfinite','truncated_free_flux']:
 v=copy.deepcopy(w)
 if name=='under_solved_zero':v['fixtures'][2]['x_real_hex']=['0x0.0p+0']*len(v['fixtures'][2]['x_real_hex']);v['fixtures'][2]['x_imag_hex']=['0x0.0p+0']*len(v['fixtures'][2]['x_imag_hex'])
 elif name=='nonfinite':v['fixtures'][0]['x_real_hex'][0]='nan'
 else:v['fixtures'][0]['free_real_hex']=v['fixtures'][0]['free_real_hex'][:-1]
 with tempfile.TemporaryDirectory() as td:
  Path(td,'WITNESS.json').write_text(json.dumps(v));r=subprocess.run([sys.executable,str(runner),td],capture_output=True,text=True)
  assert r.returncode!=0,name+' was accepted'
  expected={'under_solved_zero':'raw algebraic budget 2','nonfinite':'cannot convert NaN','truncated_free_flux':'AssertionError'}[name]
  assert expected in r.stderr,(name,r.stderr)
  records.append({'name':name,'rejected':True,'diagnostic':r.stderr.splitlines()[-1]})
print(json.dumps({'status':'PASS','expected_rejections':records},indent=2))
