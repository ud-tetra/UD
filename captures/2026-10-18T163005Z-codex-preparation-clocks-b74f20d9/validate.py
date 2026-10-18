import json,subprocess,sys
from fractions import Fraction as F
from bindings import P,sha,check
from prep_math import budget
from controls import controls

def validate():
 f=check();a=json.loads((P/'CERTIFICATE.json').read_text());b=json.loads((P/'REPLAY_CERTIFICATE.json').read_text());dynamic={'replay','wall_seconds','peak_rss_kib'};assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic};assert not a['replay'] and b['replay']
 c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];m=a['metrics']
 for r in a['rows']:
  q=budget(c,m,F(*r['offset_box_sample_units']),F(*r['preparation_fraction_of_gamma']),F(*r['jitter_sample_units']),F(*r['absolute_preparation_rate_error']),F(*r['raw_vector_error']),model_floor=r['model_floor_included']);assert all(r[k]==v for k,v in q.items())
 for e in a['profiles']:assert sha(P/'profiles'/f"{e['name']}.npz")==e['witness_sha256']
 assert json.loads((P/'CONTROL_RESULTS.json').read_text())==controls();t=subprocess.run([sys.executable,'-m','unittest','-v','test_preparation'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','same_team_review_only':True,'grid_rows_checked':len(a['rows']),'profile_witnesses_replayed':len(a['profiles']),'tests':10,'control_families':5,'joint_control_status':a['joint_control']['status'],'new_actual_phase_estimator_execution':False,'SI_clock_accuracy_certified':False,'all_HOLD_and_one_sided_results_retained':True}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
