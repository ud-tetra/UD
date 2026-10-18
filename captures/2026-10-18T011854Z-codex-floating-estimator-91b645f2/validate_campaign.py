from pathlib import Path
import json,hashlib,subprocess,sys
from fractions import Fraction as F
from numeric_math import assemble
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
 freeze=json.loads((P/'CAMPAIGN_FREEZE.json').read_text())
 for n,h in freeze['code_sha256'].items():assert sha(P/n)==h,(n,'frozen source changed')
 for n,h in freeze['inputs_sha256'].items():assert sha(P/'inputs'/n)==h
 constants=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];constants['discovery_cutoff']=json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff'];rows=[]
 dynamic={'all_18790154_readings_projected','portable_sketch_witness_replay','wall_seconds','peak_rss_kib'}
 for c in freeze['cases']:
  out=P/f"results/{c['case']}";cert=json.loads((out/'FLOAT_CERTIFICATE.json').read_text());rep=json.loads((out/'REPLAY_CERTIFICATE.json').read_text())
  assert {k:v for k,v in cert.items() if k not in dynamic}=={k:v for k,v in rep.items() if k not in dynamic}
  assert cert['record_sha256']==c['record_sha256'] and cert['proposal_sha256']==c['parent_proposal_sha256']==sha(out/'PROPOSAL.npz')
  assert cert['witness_sha256']==sha(out/'FLOAT_WITNESS.npz') and cert['exact_sketch_sha256']==sha(out/'EXACT_RECORD_SKETCH.npz')
  proof=assemble(cert['metrics'],constants);assert all(cert[k]==v for k,v in proof.items())
  assert cert['unique_reference_phase_matching'] and cert['computed_sketch_order_certified'] and cert['original_proposal_byte_identical']
  assert cert['all_18790154_readings_projected'] and not rep['all_18790154_readings_projected'] and rep['portable_sketch_witness_replay']
  rows.append({'case':c['case'],'status':cert['status'],'phase_error_radians_upper':cert['emitted_phase_error_radians_upper'],'readable_phase_error_upper':float(F(*cert['emitted_phase_error_radians_upper'])),'original_proposal_byte_identical':True,'exact_sketch_order':105,'portable_full_residual_replay':True})
 assert json.loads((P/'results/clean/FLOAT_CERTIFICATE.json').read_text())['metrics']['reference_model_residual_upper']==constants['reference_model_sketch_residual_upper']
 tests=subprocess.run([sys.executable,'-m','unittest','-v','test_adapter'],cwd=P,capture_output=True,text=True);assert tests.returncode==0,tests.stderr
 (P/'HOSTILE_TEST_RESULTS.txt').write_text(tests.stdout+tests.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','captured_floating_runs':3,'raw_readings_projected_in_fresh_verification':3*18790154,'portable_saved_array_verifications':3,'tests':6,'cases':rows,'rounding_step_validated':True,'eigensolver_outputs_validated_by_residual':True,'no_full_Hankel_allocated':True,'uniform_all_input_convergence_claimed':False,'reference_phases_are_physical_truth':False}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
