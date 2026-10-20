"""Independent exact fixed-U LS-centered operator-lag quotient/grid audit."""
import argparse,hashlib,json,importlib.util
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent;SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();R=lambda p:json.loads(Path(p).read_text());q=lambda p:F(int(p[0]),int(p[1]));pair=lambda p:[str(p.numerator),str(p.denominator)]
def calculate(d,e,eta,cap):
 assert d>=0 and e>=0 and 0<=eta<1 and cap>0
 a=1+eta/2;return a,(cap-d-a*e)/a

def controls():
 rows=[]
 def ck(n,v):assert v,n;rows.append({'id':n,'pass':True})
 def reject(fn):
  try:fn();return False
  except AssertionError:return True
 a,b=calculate(F(1,4),F(1,16),F(1,2),F(1,2))
 ck('closed_radius_envelope_equality',F(1,4)+a*(F(1,16)+b)==F(1,2))
 ck('next_larger_not_certified',F(1,4)+a*(F(1,16)+b+F(1,1024))>F(1,2))
 ck('A_concavity_upper',a*a>=1+F(1,2))
 ck('negative_saved_lag_refused',reject(lambda:calculate(F(-1),F(0),F(0),F(1))))
 ck('negative_LS_distance_refused',reject(lambda:calculate(F(0),F(-1),F(0),F(1))))
 ck('invalid_Gram_refused',reject(lambda:calculate(F(0),F(0),F(1),F(1))))
 ck('nonpositive_cap_refused',reject(lambda:calculate(F(0),F(0),F(0),F(0))))
 ck('no_positive_budget_preserved',calculate(F(1),F(0),F(0),F(1))[1]==0)
 ck('negative_budget_preserved',calculate(F(1),F(1),F(0),F(1))[1]<0)
 ck('exact_LS_distance_debits_radius',calculate(F(1,4),F(1,8),F(0),F(1,2))[1]==F(1,8))
 return rows

def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--root',required=True);a.add_argument('--primary',required=True);a.add_argument('--release',required=True);args=a.parse_args();repo=Path(args.repo);root=Path(args.root);primary=Path(args.primary);f=R(P/'BUDGET_REVIEW_FREEZE.json');assert SHA(__file__)==f['code_sha256'];assert SHA(root/'FREEZE.json')==f['root_freeze_sha256'];assert R(args.release)['LS_lag_budget_execution_released']is True
 rf=R(root/'FREEZE.json')
 for path,h in rf['files'].items():assert SHA(root/path)==h
 docs={}
 for name,pin in rf['sources'].items():assert SHA(repo/pin['path'])==pin['sha256'];docs[name]=R(repo/pin['path'])
 cert=R(primary/'CERTIFICATE.json');assert cert['freeze_sha256']==SHA(root/'FREEZE.json');assert len(cert['rows'])==2;rows=[];maps=[{r['case']:r for r in docs[key]['rows']}for key in ['quality','operator','LS']]
 for case,published in zip(rf['cases'],cert['rows']):
  old,op,ls=[m[case]for m in maps];assert case==published['case'];assert old['record_sha256']==op['record_sha256']==ls['record_sha256']==published['record_sha256'];assert published['old_campaign_status_preserved']==old['status']
  d=q(op['norm']['operator_norm_upper']);e=q(ls['LS']['LS_step_operator_distance_upper']);eta=q(old['measured']['etaU']);cap=q(docs['caps']['quality_caps']['sA']);A,b=calculate(d,e,eta,cap)
  for field,expected in [('saved_lag_operator_upper',d),('saved_LS_step_distance_upper',e),('A_operator_upper',A),('LS_centered_sufficient_radius',b)]:assert q(published[field])==expected
  assert published['status']==('CERTIFIED_POSITIVE_FIXED_BASIS_LS_CENTERED_LAG_BUDGET'if b>0 else'HOLD_NO_POSITIVE_SUFFICIENT_BUDGET');assert [r['k']for r in published['grid']]==list(range(20,101));selected=[]
  for row in published['grid']:
   epsilon=F(1,1<<row['k']);lag=d+A*e+A*epsilon;assert q(row['epsilon'])==epsilon and q(row['lag_envelope'])==lag and row['operator_lag_cap_sufficient']==(lag<=cap)
   if lag<=cap:selected.append(row)
  assert published['largest_positive_grid_epsilon']==(selected[0]if selected else None);assert not published['backend_rounding_guaranteed']and not published['phase_guaranteed_for_replacement_T'];rows.append({'case':case,'status':'PASS_EXACT_POSTKNOWN_LS_CENTERED_LAG_RADIUS_AND_81_ROWS','sufficient_closed_radius':pair(b),'selected_k':None if not selected else selected[0]['k'],'old_campaign_status_preserved':old['status']})
 out=P/'BUDGET_REVIEW_RECEIPT.json';assert not out.exists();out.write_text(json.dumps({'status':'PASS_INDEPENDENT_FIXED_U_LS_CENTERED_OPERATOR_LAG_SUPPLEMENT','rows':rows,'grid_rows_checked':162,'freeze_sha256':SHA(P/'BUDGET_REVIEW_FREEZE.json'),'source_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'new_estimator_calls':0,'new_norms_or_matrices_computed':0,'scope':'Operator-lag only around exact fixed-U LS center; no phase/profile/backend/raw-noise guarantee and no old Frobenius HOLD change','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n');print(json.dumps(rows))
if __name__=='__main__':main()
