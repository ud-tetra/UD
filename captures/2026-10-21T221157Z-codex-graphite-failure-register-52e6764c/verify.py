from pathlib import Path
import json,numpy as np
root=Path(__file__).resolve().parent.parent;p=root/'graphite-branch-aware-addendum';r=json.loads((p/'FAILURE_REGISTER.json').read_text());got=[];dirs=[]
for case in json.loads((root/'graphite-branch-aware/FREEZE.json').read_text())['inputs']:
 a=np.load(root/'graphite-branch-aware'/case/'MATRIX_RAW.npz');H=a['matrices']
 for k in range(2):
  D=H[k+1]-H[k]
  got.extend((case,int(j),k) for j in np.flatnonzero(np.max(abs(D),axis=0)>=1e-6))
 d=np.load(root/'graphite-branch-aware'/case/'DIRECTION_RAW.npz');adj=np.diff(d['derivatives'],axis=1);dirs.extend((case,int(i)) for i in np.flatnonzero(np.max(abs(adj),axis=(1,2))>=1e-6))
assert sorted(got)==sorted((v['case'],v['column_0based'],v['pair_index']) for v in r['failures'] if v['kind']=='matrix_column');assert dirs==[(v['case'],v['index']) for v in r['failures'] if v['kind']=='direction'];assert len(got)==4 and len(dirs)==1
v={'status':'PASS_CONSTRUCTOR_FULL_FAILED_SET_SCAN','matrix_columns':got,'directions':dirs,'physical_promotion':0,'review':'Non-constructor pending'};(p/'VERIFICATION.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(v))
