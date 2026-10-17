"""Bind all stored receipts, exact recipes and unchanged implementations after the campaign."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys,subprocess
import numpy as np
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());manifest=json.loads((P/'RECORD_MANIFEST.json').read_text());rows=json.loads((P/'CAMPAIGN_RESULTS.json').read_text())
assert manifest['freeze_sha256']==sha(P/'CAMPAIGN_FREEZE.json');assert len(rows)==len(spec['cases'])==3
for n,h in spec['code_sha256'].items():assert sha(P/n)==h,n
base=P.parent/'observer-work/inputs/normalized_history.i64le';assert sha(base)==spec['baseline_sha256'];S=(37,8191,62);Y=np.memmap(base,dtype='<i8',mode='r',shape=S)
v=np.zeros(2294,np.int64);v[:320]=json.loads((P/'NULL_VECTOR.json').read_text())['vector'];V=v.reshape(62,37).T;count=0
contract=json.loads((P/'inputs/FROZEN_CONTRACT.json').read_text());T=F(*contract['spectral_rule']['selection_threshold'])
for case,row,entry in zip(spec['cases'],rows,manifest['records']):
 name=case['name'];assert row['case']==entry['case']==name
 p=P/'records'/(name+'.i64le');assert sha(p)==entry['record_sha256']==row['proposal_record_sha256']
 Z=np.memmap(p,dtype='<i8',mode='r',shape=S);f=np.where(np.arange(8191)%2==0,1,-1)
 if name=='bounded_null_impulse':f[:]=0;f[4095]=1
 for a in range(37):assert np.array_equal(Z[a]-Y[a],f[:,None]*V[a,None,:]*case['scale'])
 count+=int(np.prod(S));out=P/'results'/('certificate-'+name);cert=json.loads((out/'CERTIFICATE.json').read_text())
 assert cert['input_identity_stable'] and not cert['source_operator_or_nominal_modes_used'] and not cert['apparatus_execution_claimed']
 assert cert['input_sha256']['record']==entry['record_sha256'] and cert['input_sha256']['contract']==sha(P/'inputs/FROZEN_CONTRACT.json')
 assert cert['input_sha256']['proposal']==sha(P/'results'/('proposal-'+name)/'PROPOSAL.npz')
 assert row['temporal_dimension']==105 and row['proposal_exit']==row['certificate_exit']==0
 assert cert['selection_threshold']==contract['spectral_rule']['selection_threshold'] and cert['target_count']==1893
 if name.startswith('bounded'):
  assert cert['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
  assert F(*cert['sigma_r_lower'])>T>F(*cert['sigma_r_plus1_upper'])
  assert F(*cert['condition_upper'])<2029
 else:assert cert['status']=='HOLD' and not entry['vector_budget_met']
subprocess.run([sys.executable,str(P/'certify_blind_family.py')],check=True,capture_output=True)
d=json.loads((P/'EXACT_BLIND_FAMILY_CERTIFICATE.json').read_text());assert d['noisy_rank_lower']==30875
receipt={'status':'PASS','complete_records_checked':3,'scalar_readings_compared_to_exact_recipes':count,'bounded_signature_certificates':2,'oversized_control_hold':1,'unchanged_proposer_and_verifier_hashes':True,'same_discovery_order_in_all_cases':105,'exact_rank_lower_bound_for_bounded_impulse':30875,'physical_promotion':0,'independent_review':'not established','full_acquisition_admission':False}
(P/'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
