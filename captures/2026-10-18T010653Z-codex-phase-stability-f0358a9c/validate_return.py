from pathlib import Path
from fractions import Fraction as F
import json,hashlib,subprocess,sys
import numpy as np
from replay_phase import replay
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
 replay();fixtures=json.loads((P/'FIXTURE_MANIFEST.json').read_text());controls=json.loads((P/'CONTROL_RESULTS.json').read_text());assert len(controls['cases'])==2
 for case,result in zip(fixtures['cases'],controls['cases']):
  d=F(*case['declared_vector_budget']);assert F(*case['exact_max_vector_error_squared'])<=d*d
  assert F(*case['exact_max_scalar_error'])<=F(1,2**23)
  report=result['proposal_report'];n=case['case']
  assert report['input_files']['record_sha256']==case['record_sha256'] and report['temporal_dimension']==105
  assert report['proposal_sha256']==sha(P/f'results/proposal-{n}/PROPOSAL.npz')
  with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:expected=z['theta'].astype(object)
  expected[case['intended_positive_phase_index']]+=case['intended_phase_shift'][0]
  with np.load(P/f'results/proposal-{n}/PROPOSAL.npz',allow_pickle=False) as z:observed=z['theta'].astype(object)
  differences=[int(x)-int(y) for x,y in zip(observed,expected)]
  assert [max(abs(x) for x in differences),2**60]==result['maximum_intended_phase_discrepancy_exact']
  assert [sum(x*x for x in differences),2**120]==result['sum_squared_intended_phase_discrepancy_exact']
 full=P/'results/certificate-phase_budget_2neg20';c=json.loads((full/'CERTIFICATE.json').read_text());r=json.loads((full/'RECORD_RESIDUAL.json').read_text());contract=json.loads((P/'inputs/FROZEN_CONTRACT.json').read_text());T=F(*contract['spectral_rule']['selection_threshold'])
 assert c['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' and c['target_count']==1893
 assert F(*c['sigma_r_lower'])>T>F(*c['sigma_r_plus1_upper']) and F(*c['condition_upper'])<2029
 assert c['input_sha256']==r['input_sha256'] and r['scalar_readings_checked']==18790154
 assert c['input_sha256']['record']==fixtures['cases'][1]['record_sha256']
 assert c['input_sha256']['proposal']==sha(P/'results/proposal-phase_budget_2neg20/PROPOSAL.npz') and c['input_identity_stable']
 b=json.loads((full/'BENCHMARK.json').read_text());assert not b['dense_hankel_allocated']
 assert b['executed_code_sha256']=={n:sha(P/n) for n in ['certify_record.py','proof_math.py','residual_preflight.py']}
 tests=subprocess.run([sys.executable,'-m','unittest','-v','test_phase'],cwd=P,capture_output=True,text=True);assert tests.returncode==0,tests.stderr
 (P/'TEST_RESULTS.txt').write_text(tests.stdout+tests.stderr)
 return {'status':'PASS','phase_frame_pairs':5460,'dyadic_grid_points':21,'conditional_phase_bound_tests':6,'coherent_control_records':2,'full_Hankel_certificates':1,'all_readings_in_reference_phase_residual':18790154,'all_readings_in_new_full_Hankel_certificate':18790154,'full_verifier_unchanged':True,'full_2neg20_unique_phase_matching':'NOT_CERTIFIED_BY_THIS_BOUND','floating_phase_algorithm_validation':'OPEN','physical_promotion':0,'independent_review':'pending'}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
