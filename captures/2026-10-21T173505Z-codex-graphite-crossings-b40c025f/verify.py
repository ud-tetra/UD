from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).parent;r=json.loads((p/'RESULTS.json').read_text());a=np.load(p/'PAIRS.npz');checks=[]
for fn,sha in r['input_sha256'].items():assert hashlib.sha256((p.parent/fn).read_bytes()).hexdigest()==sha
assert hashlib.sha256((p/'PAIRS.npz').read_bytes()).hexdigest()==r['pairs_sha256']
for row in r['rows']:
 name=row['case'];c=row['cutoff_A'];prefix=f'{name}_{c}'
 if row['kind']=='local_g':
  obs=a[prefix+'_observed'];pred=a[prefix+'_predicted'];res=obs-pred
  assert np.array_equal(res,a[prefix+'_residual'])
  assert abs(float(abs(res).max())-row['max_residual_after_attribution'])<1e-16
  assert row['attribution_pass']==bool(abs(res).max()<=1e-7)
  keys=[prefix+f'_axis{i}' for i in [0,1]]
 else:
  key=prefix+f'_energyaxis{row["axis"]}';pred=float((a[key+'_energy_g']-a[key+'_force_g']).sum());res=row['observed_signed_error']-pred
  assert abs(pred-row['predicted_signed_error'])<1e-16
  assert row['attribution_pass']==bool(abs(res)<=5e-6)
  keys=[key]
 for key in keys:
  mem=a[key+'_membership'];assert np.all(mem.any(0)&~mem.all(0));assert len(a[key+'_r'])==mem.shape[1]
 checks.append({'case':name,'kind':row['kind'],'passes':True})
t=json.loads((p/'RUNTIME_CHECK.json').read_text());assert len(t['checks'])==9 and all(v['passes'] for v in t['checks'])
assert all(z['attribution_pass'] for z in r['rows'])
out={'status':'CONSTRUCTOR_VERIFICATION_PASS','checks':checks,'runtime_pair_checks':9,'inputs_hash_checked':len(r['input_sha256']),'scope':'Recorded input/pair hashes, crossing membership, aggregation and frozen diagnostic criteria; same-constructor verification, not independent review','scientific_gate':'HOLD','physical_promotion':0}
(p/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
