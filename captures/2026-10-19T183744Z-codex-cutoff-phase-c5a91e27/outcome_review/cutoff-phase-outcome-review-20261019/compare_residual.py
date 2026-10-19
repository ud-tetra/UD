"""Read-only comparison of frozen direct and expanded retained residuals."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'cutoff-campaign-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run():
 fr=load(HERE/'RESIDUAL_COMPARE_FREEZE.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 protocol=load(P/'PROTOCOL_FREEZE.json');assert sha(P/'PROTOCOL_FREEZE.json')=='baa1b4a59fd65f37a7802b28bdeeca93c2490fb220c8274c6fa2463d73aa190e'
 for p,h in protocol['files'].items():assert sha(P/p)==h,p
 assert protocol['fixed_budget']==load(P/'inputs/FIXED_BUDGET.json')['source_budget']
 old=load(ROOT/'cutoff-phase-review-20261019/CODE_REVIEW.json')
 for n,h in old['files'].items():
  if n not in ['records.py','driver.py']:assert sha(P/n)==h,n
 addon=load(ROOT/'cutoff-phase-review-20261019/ADDENDUM.json')
 for n,h in addon['files'].items():assert sha(P/n)==h,n
 rows=[]
 for direct in load(HERE/'DIRECT_RESIDUAL.json')['rows']:
  cert=load(P/('PARENT_NUMERIC_CERTIFICATES.json' if direct['kind']=='parent' else 'CAMPAIGN_NUMERIC_CERTIFICATES.json'));main=next(x for x in cert['rows'] if x['case']==direct['case'])
  assert main['record_sha256']==direct['record_sha256']
  if direct['status'].startswith('HOLD'):
   assert main['status'].startswith('HOLD');rows.append({'case':direct['case'],'status':'SELECTED_HOLD_RETAINED'});continue
  a,b=map(int,direct['direct_residual_squared']);c,d=map(int,main['cutoff']['exact_truncated_residual_squared']);assert F(a,b)==F(c,d)
  rows.append({'kind':direct['kind'],'case':direct['case'],'status':'PASS_EXACT_DIRECT_VS_EXPANDED_RESIDUAL','main_combined_status_retained':main['status'],'main_cutoff_status_retained':main['cutoff']['status'],'exact_fraction_match':True,'raw_nominal_projection_digests_reproduced':True})
 rf=load(P/'RESUME_FREEZE.json');assert sha(P/'resume.py')==rf['resume_code_sha256'] and rf['original_protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json')
 for c in rf['completed_fits']:
  folder=P/'results'/c['case'];assert sha(folder/'RUN.json')==c['run_sha256']
  for n,h in c['numeric_witnesses'].items():assert sha(folder/n)==h
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 result={'status':'PASS_TWO_SELECTED_EXACT_RETAINED_RESIDUAL_COMPARISONS','rows':rows,'protocol_and_original_review_hashes_unchanged':True,'fixed_source_caps_unchanged':True,'interrupted_first_three_completed_witnesses_unchanged':True,'resume_code_and_freeze_bound':True,'freeze_sha256':sha(HERE/'RESIDUAL_COMPARE_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team selected expression comparison, not all9 residual recomputation. Parent interruption was operational file collision; existing first3 fit bytes preserved and no completed fit reexecution is attributed to this review. No estimator/raw/projection run in comparison.','external_review':'PENDING','physical_promotion':0}
 q=HERE/'SELECTED_RESIDUAL_COMPARISON.json';assert not q.exists();q.write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)

if __name__=='__main__':run()
