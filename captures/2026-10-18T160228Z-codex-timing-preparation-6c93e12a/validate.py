import json,subprocess,sys
from bindings import P,sha,check
from calibration_math import budget
from fractions import Fraction as F
from controls import controls

def validate():
 f=check();a=json.loads((P/'BUDGET_CERTIFICATE.json').read_text());b=json.loads((P/'REPLAY_CERTIFICATE.json').read_text());dynamic={'replay','wall_seconds','peak_rss_kib'}
 assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic};assert not a['replay'] and b['replay'];assert sha(P/'RIGHT_INVERSE.npz')==a['right_inverse_sha256']
 c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants']
 for r in a['rows']:
  q=budget(c,a['metrics'],F(*r['preparation_fraction_of_certified_gamma']),F(*r['jitter_sample_units']),F(*r['absolute_clock_rate_error']),F(*r['raw_vector_error']),r['model_floor_included']);assert all(r[k]==v for k,v in q.items())
 assert json.loads((P/'CONTROL_RESULTS.json').read_text())==controls()
 t=subprocess.run([sys.executable,'-m','unittest','-v','test_calibration'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','same_team_review_only':True,'grid_rows_checked':len(a['rows']),'tests':8,'exact_control_families':6,'all_saved_integer_Gram_receipts_recomputed':True,'right_inverse_validated':True,'frame_constants_recomputed':True,'joint_control':a['joint_control']['status'],'full_raw_2neg20_unique_matching':a['raw_full_2neg20_matching_certified'],'actual_floating_convergence_claimed':False,'SI_timing_certification_claimed':False,'all_HOLDs_retained':True}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
