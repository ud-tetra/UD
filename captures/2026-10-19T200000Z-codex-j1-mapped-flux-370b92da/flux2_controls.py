"""Malformed flux proposal controls in isolated output directories."""
from pathlib import Path
import json,subprocess,tempfile,copy,sys
folder=Path(sys.argv[1]);runner=Path(sys.argv[2]).resolve();w=json.loads((folder/'FLUX_WITNESS.json').read_text());records=[]
for name in ['nonfinite_root_free','truncated_patch_free']:
 v=copy.deepcopy(w)
 if name=='nonfinite_root_free':v['root_free_hex'][0][0]='nan'
 else:v['patches'][0]['free_hex'][0]=v['patches'][0]['free_hex'][0][:-1]
 with tempfile.TemporaryDirectory() as td:
  t=Path(td);(t/'FLUX_WITNESS.json').write_text(json.dumps(v))
  for f in ['STATE_WITNESS.json','SOLVE_RESULTS.json']:(t/f).write_bytes((folder/f).read_bytes())
  r=subprocess.run([sys.executable,str(runner),td],capture_output=True,text=True);assert r.returncode!=0,name+' accepted';token='cannot convert NaN' if name=='nonfinite_root_free' else 'AssertionError';assert token in r.stderr,(name,r.stderr)
  records.append({'name':name,'rejected':True,'diagnostic':r.stderr.splitlines()[-1]})
print(json.dumps({'status':'PASS','proposal_controls':records},indent=2))
