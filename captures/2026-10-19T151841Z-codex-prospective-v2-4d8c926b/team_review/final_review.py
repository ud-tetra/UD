"""Read-only same-team frozen prospective-record and policy audit; no new fitting."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
import numpy as np
P=Path(__file__).resolve().parent;W=P.parent/'prospective-v2-work';Q=P.parent/'record-contract-work';repo=P.parent/'ud-repo'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((W/'PROTOCOL_FREEZE.json').read_text());bindings={}
for key,base in [('code_sha256',W),('inputs_sha256',W/'inputs'),('helper_sha256',Q)]:
 for name,h in f[key].items():assert sha(base/name)==h;bindings[str(base/name)]=h
assert sha(P/'DESIGN_REVIEW.json')==f['same_team_design_review_sha256']
sf=json.loads((W/'SUPPLEMENT_FREEZE.json').read_text());assert sha(W/'supplement.py')==sf['code_sha256'];bindings[str(W/'supplement.py')]=sf['code_sha256']
for n,h in sf['output_sha256'].items():assert sha(W/n)==h;bindings[str(W/n)]=h
old=P.parent/'adversarial-admission-work'
identities={n:sha(W/n)==sha(old/n) for n in ['run.py','gates.py','full_svd.py','sketch.py']};assert all(identities.values())
data=json.loads((W/'DATA_FREEZE.json').read_text());assert data['protocol_sha256']==sha(W/'PROTOCOL_FREEZE.json')
assert json.loads((P/'DESIGN_REVIEW.json').read_text())['reviewed_at_utc']<f['frozen_at_utc']<sf['frozen_utc']
root=repo/'captures'/f['v2_capture']['id'];assert sha(root/'MANIFEST.json')==f['v2_capture']['manifest_sha256']
for e in json.loads((root/'MANIFEST.json').read_text())['files']:
 path=repo/e['path'];assert path.is_file() and not path.is_symlink() and path.stat().st_size==e['size_bytes'] and sha(path)==e['sha256']
allow=json.loads((root/'SOURCE_ALLOWANCE.json').read_text());v2=json.loads((W/'V2_RESULTS.json').read_text());assert v2['published_v2_source_allowance']==allow
policy=json.loads((W/'inputs/PARENT_GATE_FREEZE.json').read_text())['gates'];assert {k:v for k,v in policy.items() if k!='raw_shift_residual'}==allow['other_seven_gates']
gate=json.loads((W/'GATE_RESULTS.json').read_text());index=json.loads((W/'INTEGER_INDEX.json').read_text());supp=json.loads((W/'SUPPLEMENT_RESULTS.json').read_text());run=json.loads((W/'RUN_EXECUTIONS.json').read_text())
regen=P.parent/'prospective-v2-regenerated';rr=json.loads((regen/'RAW_REGENERATION_RECEIPT.json').read_text());assert rr['records']==data['records'];assert index['integer_entries']==7887933
rawlog=json.loads((W/'raw_projection.log').read_text());assert rawlog['status']=='PASS_COMPLETE_RAW_AND_NUMERATOR_REPLAY' and rawlog['integer_entries']==7887933
baseline=P.parent/f['baseline'];assert sha(baseline)==f['baseline_sha256'];base=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62))
anchors=[]
for s in f['integer_anchor']:
 path=P.parent/s['path'];assert sha(path)==s['sha256'];bindings[str(path)]=s['sha256']
 with np.load(path,allow_pickle=False) as z:anchors.append(z['numerator'])
arrays={str(x):sha(x) for x in sorted((W/'results').rglob('*.npz'))}
sel=json.loads((W/'inputs/SPATIAL_SELECTION.json').read_text());rng=np.random.Generator(np.random.PCG64(219101));bc=rng.integers(0,62,size=(37,64),dtype=np.int64);bs=rng.integers(0,2,size=(37,64),dtype=np.int64)*2-1
assert len(data['records'])==len(gate['rows'])==len(v2['rows'])==len(supp['rows'])==len(run)==3
rows=[];total=0
for entry,gr,vr,sr,ir,execution in zip(data['records'],gate['rows'],v2['rows'],supp['rows'],index['cases'],run):
 name=entry['case'];assert name==gr['case']==vr['case']==sr['case']==ir['case']==execution['case']
 raw=W/'records'/(name+'.i64le');assert sha(raw)==entry['record_sha256']==sha(regen/(name+'.i64le'))==gr['record_sha256']==vr['record_sha256']
 y=np.memmap(raw,dtype='<i8',mode='r',shape=base.shape);checked=0
 for first in range(0,8191,257):
  stop=min(first+257,8191);t=np.arange(first,stop)[None,:];a=np.arange(37)[:,None];diff=y[:,first:stop]-base[:,first:stop]
  if name=='rotating_checker':channels=(a+3*t)%62;sign=1-2*((a+t)%2)
  elif name=='block128':channels=bc[:,np.arange(first,stop)//128];sign=bs[:,np.arange(first,stop)//128]
  else:
   assert name=='directed_period4';channels=np.broadcast_to(np.array(sel['channels'])[:,None],(37,stop-first));sign=np.array(sel['signs'])[:,None]*np.where(t%4<2,1,-1)
  assert np.all(np.count_nonzero(diff,axis=2)==1) and np.all(np.sum(diff*diff,axis=2,dtype=np.int64)==1)
  assert np.array_equal(np.take_along_axis(diff,channels[...,None],axis=2)[...,0],sign);checked+=diff.size
 assert checked==18790154;total+=checked
 assert gr['learned_order']==execution['order']==209 and execution['SVD_certificate']=='CERTIFIED_ACTUAL_SVD_ORDER' and len(gr['checks'])==8
 for n,passed in gr['checks'].items():
  if passed:assert F(*gr['metrics'][n])<=F(*policy[n])
 strict=F(*map(int,sr['exact_raw_shift_residual_squared']))>F(1,1<<68);assert strict==sr['strict_v1_shift_violation']==('raw_shift_residual' in gr['failed_gates'])
 assert vr['v1_status']==gr['status'] and vr['v2']['status']=='CERTIFIED_RETURNED_OUTPUT_V2' and all(vr['v2']['checks'].values())
 assert F(*gr['metrics']['raw_shift_residual'])<F(*allow['raw_shift_strict_upper_allowance_lower'])
 assert F(*vr['v2']['matching_margin_lower'])>0 and F(*vr['v2']['phase_error_upper_if_certified'])*2<F(*allow['target_chord_lower'])
 chunks=[]
 for k,c in enumerate(ir['chunks']):
  path=W/c['delta_path'];assert sha(path)==c['delta_sha256']
  with np.load(path,allow_pickle=False) as z:d=z['delta'];assert d.dtype==np.int16 and np.max(np.abs(d.astype(np.int64)))<=1040
  n=anchors[k]+d.astype(np.int64)
  with np.load(W/'results'/name/'results'/f'INTEGER_{k}.npz',allow_pickle=False) as z:assert np.array_equal(n,z['numerator'])
  assert hashlib.sha256(n.astype('<i8').tobytes()).hexdigest()==c['integer_bytes_sha256']
  with np.load(W/'results'/name/'results/integer_projection'/f'FACTOR_{k}.npz',allow_pickle=False) as z:assert str(z['projection_sha256'])==hashlib.sha256((n.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest()
  chunks.append(c['delta_sha256'])
 rows.append({'case':name,'independently_checked_raw_differences':checked,'noise_vector_squared_integer_error':1,'learned_order':209,'v1_status':gr['status'],'v2_status':vr['v2']['status'],'strict_v1_shift_violation':strict,'phase_upper':vr['v2']['phase_error_upper_if_certified'],'delta_chunk_hashes':chunks})
assert total==56370462 and [r['strict_v1_shift_violation'] for r in rows]==[False,False,True]
assert supp['status']=='PASS_EXACT_GATE_COMPARISONS_AND_TWO_ACTUAL_WITNESS_CONTROLS' and len(supp['controls'])==2
assert all(sha(Path(p))==h for p,h in bindings.items()) and all(sha(Path(p))==h for p,h in arrays.items())
reports=['PROTOCOL_FREEZE.json','DATA_FREEZE.json','RUN_EXECUTIONS.json','GATE_RESULTS.json','V2_RESULTS.json','INTEGER_INDEX.json','SUPPLEMENT_FREEZE.json','SUPPLEMENT_RESULTS.json','raw_projection.log','regeneration.log']
result={'status':'PASS_SAME_TEAM_PROSPECTIVE_CAMPAIGN_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'review_code_sha256':sha(__file__),'scope':'Read-only source/policy/binding review, independently expressed raw-pattern checks and cached projection lineage; no new SVD/fitting or fullrawmatrixprojection by this reviewer','source_hashes_before_after':bindings,'result_array_hashes_before_after':arrays,'report_hashes':{n:sha(W/n) for n in reports},'unchanged_parent_adapter_bytes':identities,'raw_differences_independently_checked':total,'integer_entries_lineage_checked':index['integer_entries'],'rows':rows,'findings':['Recipes and explicit RNGdrawlayout matchprospective design; blockfinaltail127.','Frozen run causally requires DATA_FREEZE before fitting, which requires allrawhashes after generation; designreview precedes protocolfreeze.','Publishedv2capture bytes/allowance unchanged; oldv1policy andallHOLDs preserved.','All3actualfullfactorcertificates report209; quantitative replay remains separate clean-package dependency.','Post-fit supplement is separately frozen and disclosed; exactgate comparisons andtwo hostilewitness controls change no policy or estimator output.','No private account metadata was used or placed in this review; externalreview remains pending.'],'material_issues':[],'dependencies':['Clean complete savedfactor replay being prepared; this receipt does not claim its future success.','Pinned source/baseline/order/similarity and sourceallowance proof dependencies.'],'new_estimator_runs_by_reviewer':0,'new_SVD_runs_by_reviewer':0,'new_rawgeneration_by_reviewer':False,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'FINAL_REVIEW.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:result[k] for k in ['status','raw_differences_independently_checked','material_issues']}))
