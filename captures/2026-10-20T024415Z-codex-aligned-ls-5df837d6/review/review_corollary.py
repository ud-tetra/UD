"""Postknown fixed-U Frobenius LS obstruction. Exact rational, no norm recomputation."""
from fractions import Fraction as F
import argparse,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();R=lambda p:json.loads(Path(p).read_text());q=lambda p:F(int(p[0]),int(p[1]));pair=lambda x:[str(x.numerator),str(x.denominator)]

def lower(lag2,normal2,floor):
 assert lag2>=0 and normal2>=0 and floor>0
 # Independently associated exact numerator form of lag2-normal2/floor.
 return max(F(0),(lag2*floor-normal2)/floor)
def controls():
 rows=[]
 def ck(k,v):assert v,k;rows.append({'id':k,'pass':True})
 def reject(fn):
  try:fn();return False
  except AssertionError:return True
 ck('exact_scalar_rectangular_Pythagoras',lower(F(2),F(1),F(1))==1)
 ck('conservative_lower_Gamma_is_safe',lower(F(2),F(1),F(1,2))==0)
 ck('negative_floor_refused',reject(lambda:lower(F(2),F(1),F(-1))))
 ck('zero_floor_refused',reject(lambda:lower(F(2),F(1),F(0))))
 ck('negative_squared_norm_refused',reject(lambda:lower(F(-1),F(0),F(1))))
 ck('negative_deficit_clipped_to_zero',lower(F(1),F(2),F(1))==0)
 ck('strict_equal_boundary_not_NO_GO',not lower(F(2),F(1),F(1))>1)
 ck('zero_normal_nonzero_minimum_NO_GO',lower(F(2),F(0),F(1))>1)
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--LS-primary',required=True);ap.add_argument('--root-corollary',required=True);ap.add_argument('--root-output',required=True);ap.add_argument('--release',required=True);args=ap.parse_args();freeze=R(P/'COROLLARY_REVIEW_FREEZE.json');assert SHA(__file__)==freeze['code_sha256'];assert R(args.release)['corollary_execution_released']is True
 repo=Path(args.repo);ls=Path(args.LS_primary);root=Path(args.root_corollary);out=Path(args.root_output);old=R(repo/'captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d/estimator_primary/CERTIFICATE.json');normals=R(ls/'CERTIFICATE.json');rows=[];published=R(out/'CERTIFICATE.json');assert len(published['rows'])==2
 for prior,normal,result in zip(old['rows'],normals['rows'],published['rows']):
  assert prior['case']==normal['case']==result['case'];lag2=q(prior['measured']['exact_squared']['raw_lag_F']);n2=q(normal['LS']['normal_Frobenius_squared']);floor=q(normal['LS']['gamma_squared_lower']);bound=lower(lag2,n2,floor);cap=F(1,1<<34)
  # Root schema names are frozen separately before invocation; compare all rational quantities there.
  assert q(result['minimum_Frobenius_squared_lower'])==bound
  assert result['fixed_U_old_Frobenius_cap_NO_GO']==(bound>cap*cap)
  assert result['case']==prior['case']
  rows.append({'case':prior['case'],'status':'PASS_INDEPENDENT_EXACT_FIXED_U_FROBENIUS_OBSTRUCTION_CHECK','minimum_Frobenius_squared_lower':pair(bound),'strict_cap_squared_margin':pair(bound-cap*cap),'fixed_U_Frobenius_NO_GO':bound>cap*cap,'old_campaign_status_preserved':prior['status']})
 target=P/'COROLLARY_REVIEW_RECEIPT.json';assert not target.exists();target.write_text(json.dumps({'status':'PASS_POSTKNOWN_FIXED_U_LS_PYTHAGORAS_COROLLARY','rows':rows,'code_freeze_sha256':SHA(P/'COROLLARY_REVIEW_FREEZE.json'),'root_certificate_sha256':SHA(out/'CERTIFICATE.json'),'scope':'No T-only repair of old Frobenius gate where lower exceeds cap; no operator-norm or phase failure, no U change analyzed','normal_and_factor_recomputation':False,'new_estimator_calls':0,'new_raw_or_factor_copies':0,'external_review':'PENDING','physical_promotion':0},indent=2)+'\n');print(json.dumps(rows))
if __name__=='__main__':main()
