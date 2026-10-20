"""Postknown exact fixed-basis minimal Frobenius-lag corollary. No fitting or factor loading."""
import argparse,hashlib,json,os
from pathlib import Path
from fractions import Fraction as F
from flint import arb,fmpq,ctx
P=Path(__file__).resolve().parent;ctx.prec=512

def req(x,s):
 if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fr(p):return F(int(p[0]),int(p[1]))
def pair(x):return [str(x.numerator),str(x.denominator)]
def lower_squared(lag2,norm2,floor):
 req(lag2>=0 and norm2>=0 and floor>0,'nonnegative exact squares and positive Gram floor required');return max(F(0),lag2-norm2/floor)
def controls():
 req(lower_squared(F(2),F(1),F(1))==1,'orthogonal nonzero model residual');req(lower_squared(F(1),F(0),F(1))==1,'zero normal not zero model');req(not(F(1)>F(1)),'touching cap not NO_GO')
 try:lower_squared(F(1),F(0),F(0))
 except ValueError:pass
 else:raise ValueError('zero floor accepted')
 return {'status':'PASS_FOUR_PURE_COROLLARY_CONTROLS','controls':4}
def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();pro={P,P.resolve()}
 for p in(P,*P.parents):
  if(p/'MANIFEST.json').is_file():pro.update((p.absolute(),p.resolve()))
 for x in(lex,out):req(all(x!=p and p not in x.parents and x not in p.parents for p in pro),'protected output')
 req(not out.exists(),'new output required');return out

def run(ls_path,prior_path,out):
 freeze=json.loads((P/'FREEZE.json').read_text())
 for name,h in freeze['files'].items():req(sha(P/name)==h,'frozen supplement changed')
 req(sha(ls_path)==freeze['LS_certificate_sha256']and sha(prior_path)==freeze['prior_lag_certificate_sha256'],'source certificate changed');ls=json.loads(ls_path.read_text());prior=json.loads(prior_path.read_text());rows=[];cap=F(1,1<<34)
 for a,b in zip(ls['rows'],prior['rows']):
  req(a['case']==b['case']and a['record_sha256']==b['record_sha256']and a['status']=='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE','same certified saved tuple required')
  lag2=fr(b['measured']['exact_squared']['raw_lag_F']);n2=fr(a['LS']['normal_Frobenius_squared']);floor=fr(a['LS']['gamma_squared_lower']);lo=lower_squared(lag2,n2,floor);root=(arb(fmpq(lo.numerator,lo.denominator))).sqrt();lower=F(int((arb(root.lower())*(1<<180)).floor().unique_fmpz()),1<<180)
  rows.append({'case':a['case'],'old_campaign_status_preserved':b['status'],'minimum_Frobenius_lag_squared_lower':pair(lo),'minimum_Frobenius_lag_lower':pair(lower),'readable_minimum_Frobenius_lag_lower':float(lower),'fixed_basis_any_T_Frobenius_cap_NO_GO':lo>cap*cap,'cap':pair(cap),'operator_norm_failure_inferred':False,'phase_failure_inferred':False})
 req(len(rows)==2,'exactly two fixed cases');result={'artifact_type':'POSTKNOWN_FIXED_SAVED_BASIS_LS_RESIDUAL_COROLLARY','status':'COMPLETE_TWO_EXACT_COROLLARIES','freeze_sha256':sha(P/'FREEZE.json'),'rows':rows,'controls':controls(),'source_certificates_inherited_and_hash_pinned':True,'new_estimator_calls':0,'new_normals_or_Grams_computed':0,'old_campaign_relabelled':False,'physical_promotion':0,'external_review':'PENDING'};out.mkdir(parents=True,exist_ok=False);(out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps([{'case':r['case'],'NO_GO':r['fixed_basis_any_T_Frobenius_cap_NO_GO'],'minimum_lag_lower':r['readable_minimum_Frobenius_lag_lower']}for r in rows]))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--ls-cert',required=True);p.add_argument('--prior-cert',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.ls_cert),Path(a.prior_cert),guard(a.out))
