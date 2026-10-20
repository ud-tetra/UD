"""Postknown fixed-basis exact LS-centered operator-lag budget. No fits/factor loading."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,os
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def req(c,m):
 if not c:raise ValueError(m)
def q(x):
 req(isinstance(x,list)and len(x)==2,'rational pair');req(all(type(v)in(int,str)for v in x),'exact integers only');n,d=map(int,x);req(d>0,'positive denominator');return F(n,d)
def pair(x):return [str(x.numerator),str(x.denominator)]
def budget(d,e,eta,cap):
 req(d>=0 and e>=0 and 0<=eta<1 and cap>0,'valid nonnegative bounds');a=1+eta/2;return a,(cap-d)/a-e

def controls():
 a,b=budget(F(1,4),F(0),F(0),F(1,2));req(a==1 and b==F(1,4),'exact scalar budget');req(F(1,4)+a*b==F(1,2),'closed cap touching admitted');req(F(1,4)+a*(b+F(1,100))>F(1,2),'above budget not admitted');req(budget(F(1),F(0),F(0),F(1))[1]==0,'zero slack no positive radius');req(budget(F(1,2),F(1),F(0),F(1))[1]<0,'LS error debits margin')
 for eta in [F(0),F(1,2),F(3,4)]:req((1+eta/2)**2>=1+eta,'rational square-root upper')
 for args in [(F(-1),F(0),F(0),F(1)),(F(0),F(0),F(1),F(1))]:
  try:budget(*args)
  except ValueError:pass
  else:raise ValueError('bad bound admitted')
 return {'status':'PASS_EIGHT_BUDGET_CONTROLS','controls':8}

def guard(raw):
 lex=Path(os.path.abspath(raw));out=lex.resolve();protected={P,P.resolve()}
 for parent in(P,*P.parents):
  if(parent/'MANIFEST.json').is_file():protected.update((parent.absolute(),parent.resolve()))
 for candidate in(lex,out):req(all(candidate!=v and v not in candidate.parents and candidate not in v.parents for v in protected),'protected output')
 req(not out.exists(),'new output');return out

def run(repo,out):
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():req(sha(P/n)==h,'core freeze changed')
 docs={}
 for key,pin in f['sources'].items():
  path=repo/pin['path'];req(sha(path)==pin['sha256'],'pinned source changed');docs[key]=json.loads(path.read_text())
 rows=[];cap=q(docs['caps']['quality_caps']['sA']);req(cap==F(1,1<<34),'source operator-lag cap unchanged')
 maps=[{v['case']:v for v in docs[k]['rows']}for k in ['quality','operator','LS']]
 req(all(set(m)==set(f['cases'])and len(docs[k]['rows'])==2 for m,k in zip(maps,['quality','operator','LS'])),'exact case set')
 for name in f['cases']:
  try:
   quality,operator,ls=[m[name]for m in maps];req(quality['record_sha256']==operator['record_sha256']==ls['record_sha256'],'same record');req(operator['norm']['selected_bound']=='Gram_Frobenius','frozen operator route');req(ls['LS']['status']=='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE'and q(ls['LS']['gamma_squared_lower'])>0,'positive LS rank premise');d=q(operator['norm']['operator_norm_upper']);e=q(ls['LS']['LS_step_operator_distance_upper']);eta=q(quality['measured']['etaU']);a,b=budget(d,e,eta,cap);grid=[{'epsilon':pair(F(1,1<<k)),'k':k,'lag_envelope':pair(d+a*(e+F(1,1<<k))),'operator_lag_cap_sufficient':d+a*(e+F(1,1<<k))<=cap}for k in f['grid_k']];selected=next((v for v in grid if v['operator_lag_cap_sufficient']),None)
   rows.append({'case':name,'record_sha256':quality['record_sha256'],'status':'CERTIFIED_POSITIVE_FIXED_BASIS_LS_CENTERED_LAG_BUDGET'if b>0 else 'HOLD_NO_POSITIVE_SUFFICIENT_BUDGET','old_campaign_status_preserved':quality['status'],'operator_norm_kind':'PR258 preselected Gram_Frobenius','saved_lag_operator_upper':pair(d),'saved_LS_step_distance_upper':pair(e),'A_operator_upper':pair(a),'LS_centered_sufficient_radius':pair(b),'readable_LS_centered_sufficient_radius':float(b),'largest_positive_grid_epsilon':selected,'grid':grid,'backend_rounding_guaranteed':False,'phase_guaranteed_for_replacement_T':False})
  except Exception as exc:rows.append({'case':name,'status':'HOLD_BUDGET_EXCEPTION','error_type':type(exc).__name__,'error':str(exc),'retry_allowed':False})
 result={'artifact_type':'POSTKNOWN_FIXED_SAVED_BASIS_LS_CENTERED_OPERATOR_LAG_BUDGET','freeze_sha256':sha(P/'FREEZE.json'),'rows':rows,'controls':controls(),'norm_matrices_and_factor_truth_inherited_not_recomputed':True,'new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'old_campaign_relabelled':False,'lane':'Development — no registry entry','external_review':'PENDING','physical_promotion':0};out.mkdir(parents=True,exist_ok=False);(out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps([{'case':v['case'],'status':v['status'],'radius':v.get('readable_LS_centered_sufficient_radius'),'grid_k':(v.get('largest_positive_grid_epsilon')or{}).get('k')}for v in rows]))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--out',required=True);v=a.parse_args();run(Path(v.repo).resolve(),guard(v.out))
