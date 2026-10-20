"""Prospective independent review of two frozen producer cases. No raw or fits."""
from pathlib import Path
import json,hashlib,subprocess,sys,os,datetime
import numpy as np
import review_data as d
P=Path(__file__).resolve().parent;W=P.parent/'c15_campaign';R=P.parent/'ud-repo';sha=d.sha;J=d.read
cf=J(W/'CAMPAIGN_FREEZE.json');assert cf['case_order']==list(d.CASES);assert cf['new_raw_records']==cf['new_estimator_calls']==0
codefreeze=J(P/'REVIEW_CODE_FREEZE.json')
for n,h in codefreeze['files'].items():assert sha(P/n)==h
old=R/'captures/2026-10-20T133845Z-codex-three-noise-f72a62fa/campaign/cases/block257_port17';rows=[]
for name in d.CASES:
 p=W/'cases'/name;assert sha(p/'FREEZE.json')==cf['case_freeze_sha256'][name];f=J(p/'FREEZE.json')
 for n,h in f['files'].items():assert sha(p/n)==h
 for n,h in f['repository_sources'].items():assert sha(R/n)==h
 for n in ['estimator.py','certify.py','phase.py','exact_math.py','numeric_math.py','proof_math.py','driver.py']:assert (p/n).read_bytes()==(old/n).read_bytes(),n
 assert J(p/'PROFILE.json')['source_noise_ball']==[3,1<<49]
 assert J(p/'PROFILE.json')['original_quality_caps']==J(old/'PROFILE.json')['original_quality_caps']
 assert J(p/'PROFILE.json')['lag_route']=='PRESELECTED_GRAM_FROBENIUS_ONLY'
 for n in ['DATA_GENERATION_INTENT.json','DATA_FREEZE.json','FIT_INTENT.json','RUN_EXECUTIONS.json','results']:assert not(p/n).exists(),'prospective stage violated '+n
 cmd="import sys,hashlib,json; sys.path.insert(0,sys.argv[1]); import records; import numpy as np; a=np.stack([np.stack(records.pattern(p,np.arange(8191)),axis=1) for p in range(37)]).astype('<i8'); print(json.dumps({'shape':list(a.shape),'sha256':hashlib.sha256(a.tobytes()).hexdigest()}))"
 got=json.loads(subprocess.check_output([sys.executable,'-c',cmd,str(p)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True))
 own=np.empty((37,8191,4),np.int64)
 for prep in range(37):
  for t in range(8191):
   (c1,s1),(c2,s2)=d.at(name,prep,t);own[prep,t]=[c1,c2,s1,s2]
 ownhash=hashlib.sha256(own.astype('<i8').tobytes()).hexdigest();assert got=={'shape':[37,8191,4],'sha256':ownhash}
 rows.append({'case':name,'producer_freeze_sha256':sha(p/'FREEZE.json'),'independently_matched_channel_sign_values':int(own.size),'independently_matched_vectors':37*8191,'complete_pattern_sha256':ownhash,'all_numerical_modules_and_driver_byte_identical_PR269':True,'raw_generation_recommended':True,'fit_recommended_now':False})
freeze={'status':'INDEPENDENT_DATA_DRIVER_BOUND_TO_BOTH_PROSPECTIVE_CASES','driver_sha256':sha(P/'review_data.py'),'cases':cf['case_freeze_sha256'],'code_and_controls_freeze_sha256':sha(P/'REVIEW_CODE_FREEZE.json'),'campaign_freeze_sha256':sha(W/'CAMPAIGN_FREEZE.json'),'new_estimator_calls':0,'new_raw_records':0}
with(P/'DATA_DRIVER_FREEZE.json').open('x')as f:json.dump(freeze,f,indent=2);f.write('\n')
result={'status':'PASS_PROSPECTIVE_BOUNDARY_RAW_ONLY_REVIEW','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'campaign_freeze_sha256':sha(W/'CAMPAIGN_FREEZE.json'),'data_driver_freeze_sha256':sha(P/'DATA_DRIVER_FREEZE.json'),'review_code_freeze_sha256':sha(P/'REVIEW_CODE_FREEZE.json'),'review_source_sha256':sha(Path(__file__)),'cases':rows,'independent_pure_controls':len(J(P/'DATA_CONTROLS.json')['rows']),'exact_lattice_classification':'7689 distinct allowed pointwise vectors; maximum squared radius ratio8/9; no whole-trajectory guarantee','lattice_theorem_check_sha256':sha(P/'LATTICE_THEOREM_CHECK.json'),'all_raw_records_at_review':0,'actual_estimator_calls_at_review':0,'numerical_outputs_unknown':True,'raw_generation_recommended':True,'fit_recommended_now':False,'fit_prerequisites':['both full actual raw audits','both exact projection digests','distinctness and bounded prior digest exposure','frozen independent post-output audit','root all-data fit release'],'custody_limits':'Source hashes and truthful releases; no cryptographic caller authentication','external_review':'PENDING','physical_promotion':0}
with(P/'RAW_PRE_RUN_REVIEW.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':result['status'],'raw_only_release_recommended':True,'sha256':sha(P/'RAW_PRE_RUN_REVIEW.json')}))
