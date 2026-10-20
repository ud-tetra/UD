from pathlib import Path
from fractions import Fraction as F
import json,hashlib
root=Path('/workspace/scratch/f3d1c2f040c9');repo=root/'ud-repo'
def load(p):return json.loads(p.read_text())
def rat(v):return F(int(v[0]),int(v[1]))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for short in ['block','rotating']:
 case='boundary_pair_'+short
 p=root/'c20_primary_v1_1'/case;r=root/'c20_replay_v1_1'/case
 a=load(p/'CERTIFICATE.json')
 assert a['status']=='CERTIFIED_FINITE_SUPPLIED_RECORD' and all(a['gates'].values())
 assert a['dimensions']=={'m':8191,'n':321,'q':209}
 assert a['prior_certificate_inputs']==0 and a['new_estimator_calls']==0
 for name in ['CERTIFICATE.json','WITNESS.json.gz']:
  assert (p/name).read_bytes()==(r/name).read_bytes(),(case,name)
 assert (p/'WITNESS.json.gz').read_bytes()==(root/'c20_primary'/case/'WITNESS.json.gz').read_bytes()
 old=load(repo/'captures/2026-10-20T200634Z-codex-direct-tail-f478656e/primary'/case/'CERTIFICATE.json')
 # External regression only: old outputs are not producer input premises.
 assert rat(a['bounds']['direct_tail_upper'])==rat(old['bounds']['direct_tail_upper'])
 assert float(rat(a['bounds']['full_abs_error_upper']))==old['readable']['full321_abs_error_upper']
 assert rat(a['bounds']['full_abs_error_upper'])<F(1,1<<41)
 assert rat(a['bounds']['direct_tail_upper'])<F(1,1<<24)<rat(a['bounds']['ambient_sigma_q_lower'])
 rows.append({'case':case,'scientific_replay_sha256':{n:sha(p/n) for n in ['CERTIFICATE.json','WITNESS.json.gz']},'old_direct_tail_exact_equal':True,'old_full_error_readable_equal':True,'regression_only_no_prior_certificate_in_producer':True})
seal=load(root/'c20_verifier/SEAL.json')
for n,h in seal['files'].items():assert sha(root/'c20_verifier'/n)==h
out={'status':'PASS_BOTH_FRESH_ALL_METRIC_RECORDS_AND_SCIENTIFIC_REPLAYS','cases':rows,'byte_identical_scientific_files':4,'host_dependent_RESOURCE_excluded':True,'fresh_metrics_per_case':['a','b','eta','r','f','g'],'source_seal_unchanged':True,'active_version':'1.1','v1_to_v1_1_matrix_witnesses_byte_identical':True,'new_estimator_calls':0,'new_record_identities':0,'all_input_backend_conformance':'OPEN','physical_promotion':0,'external_review':'PENDING'}
(root/'c20_root/REPLAY_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
