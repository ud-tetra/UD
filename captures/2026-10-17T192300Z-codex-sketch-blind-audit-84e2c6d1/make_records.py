"""Construct exact sketch-null additive records; no change to frozen learning or verification."""
from pathlib import Path
import json,hashlib,time
import numpy as np
P=Path(__file__).resolve().parent;S=(37,8191,62)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());vdata=json.loads((P/'NULL_VECTOR.json').read_text())
assert sha(P/'NULL_VECTOR.json')==spec['null_vector_sha256']
v=np.zeros(2294,np.int64);v[:320]=vdata['vector'];W=np.random.default_rng(172026).choice([-1,1],size=(2294,160)).astype(np.int64)
assert np.all(v@W==0) and np.any(v)
V=v.reshape(62,37).T
baseline=P.parent/'observer-work/inputs/normalized_history.i64le';assert sha(baseline)==spec['baseline_sha256']
Y=np.memmap(baseline,dtype='<i8',mode='r',shape=S);rows=[]
for case in spec['cases']:
 path=P/'records'/(case['name']+'.i64le');assert not path.exists()
 clock=np.where(np.arange(8191)%2==0,1,-1).astype(np.int64)
 if case['name']=='bounded_null_impulse':clock[:]=0;clock[4095]=1
 scale=case['scale'];spatial=V*scale
 # Object arithmetic: the deliberate strong control exceeds the int64-square range.
 peak=max(sum(int(x)**2 for x in spatial[a]) for a in range(37));coordinate=max(abs(int(x)) for x in spatial.flat)
 Z=np.memmap(path,dtype='<i8',mode='w+',shape=S)
 for a in range(37):Z[a]=Y[a]+clock[:,None]*spatial[a,None,:]
 Z.flush();del Z
 rows.append({'case':case['name'],'record_sha256':sha(path),'bytes':path.stat().st_size,'scale':scale,'max_coordinate_integer_error':coordinate,'max_vector_integer_squared_error':peak,'vector_budget_met':peak<=2**56,'sufficient_coordinate_gate_met':coordinate<=2**25,'exact_sketch_perturbation_zero':True,'nonzero_time_vectors':int(np.count_nonzero(clock))})
 print(rows[-1],flush=True)
(P/'RECORD_MANIFEST.json').write_text(json.dumps({'freeze_sha256':sha(P/'CAMPAIGN_FREEZE.json'),'records':rows},indent=2)+'\n')
