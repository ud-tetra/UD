"""Exact dyadic measured-frame verification against the unchanged PR224 budget."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq
from common import P,freeze,check_source,sha,a,up,down
from numeric_math import encode
from proof_math import fm,arr,norm_exact

def constants():
 f=freeze();b=json.loads((P/'inputs/FIXED_BUDGET.json').read_text())['source_budget'];u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text())
 assert f['fixed_budget']==b
 return dict(eta=a(b['retained_Gram_cap']),nu=a(b['normal_cap']),raw=a(b['allowed_raw_frame_residual_lower']),allowance=a(b['allowance_lower']),beta=a(u['deleted_two_rows_beta_lower']),sigma=a(u['comparison_shift_residual_upper']),M0=a(u['comparison_shift_norm_upper']))
def bound(eta,nu,r,c):
 eta,nu,r=map(arb,(eta,nu,r))
 if not(0<=eta<1 and 0<=nu and 0<=r):return None
 s=r/(1-eta).sqrt()
 if not s<1:return None
 d=(2/(1+(1-s*s).sqrt())).sqrt()*s
 if not d<c['beta']:return None
 J=(1+eta).sqrt()*(c['sigma']+(1+c['M0'])*d);amin=(1-eta).sqrt()*(c['beta']-d)
 return dict(sine=s,distance=d,J=J,amin=amin,shift=(J*J+(nu/amin)**2).sqrt())
def classify(q,eta,nu,r,c):
 b=bound(eta,nu,r,c) if q==209 else None
 gates=dict(order_applicability=q==209,retained_Gram_cap=bool(0<=eta<=c['eta']),fixed_normal_cap=bool(0<=nu<=c['nu']),frame_budget=bool(0<=r<c['raw']),source_bound_strict_allowance=bool(b is not None and b['shift']<c['allowance']))
 failures=[k for k,v in gates.items() if not v]
 return ('CERTIFIED_FRESH_MEASURED_SOURCE_FRAME_SHIFT' if not failures else 'HOLD_'+'_AND_'.join(failures).upper()),gates,b

def verify(source):
 c=constants();check_source(source);pf=json.loads((P/'ALIGNMENT_FREEZE.json').read_text())
 assert pf['run_executions_sha256']==sha(P/'RUN_EXECUTIONS.json') and pf['data_freeze_sha256']==sha(P/'DATA_FREEZE.json')
 for n,h in pf['files'].items():assert sha(P/n)==h
 U0=np.vstack([np.load(source/('U0_'+k+'.npz'),allow_pickle=False)['basis'] for k in ['A','B']]);u0,b0=encode(U0);U0f=fm(u0);rows=[]
 data=json.loads((P/'DATA_FREEZE.json').read_text());runs=json.loads((P/'RUN_EXECUTIONS.json').read_text())['rows']
 assert data['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and len(runs)==len(freeze()['cases'])==len(data['records'])==len(freeze()['cases'])
 for recipe,record,run in zip(freeze()['cases'],data['records'],runs):
  name=recipe['case'];case=P/'results'/name;assert record['recipe']==recipe;assert run==json.loads((case/'RUN.json').read_text());assert name==record['case']==run['case'] and record['record_sha256']==run['record_sha256']
  for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h
  q=run['learned_order'];row=dict(case=name,record_sha256=record['record_sha256'],learned_order=q,rank_not_forced=True,physical_promotion=0)
  if run['execution_status']!='COMPLETED':
   row.update(status='HOLD_ESTIMATOR_EXECUTION',execution_error=run['execution_error'],scope='Frozen numerical exception retained; no retry or retuning.');rows.append(row);continue
  if q!=209:
   row.update(status='HOLD_ORDER_APPLICABILITY',scope='Measured direct 209-column theorem is inapplicable; all estimator outputs retained.');rows.append(row);continue
  U1=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
  with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
  with np.load(P/'alignments'/f'{name}.npz',allow_pickle=False) as z:X=z['alignment']
  assert U1.shape==(8191,209) and T.shape==X.shape==(209,209)
  un,bu=encode(U1);tn,bt=encode(T);xn,bx=encode(X);Uf=fm(un);Gfull=Uf.transpose()*Uf
  eta=norm_exact(arr(Gfull)-np.eye(209,dtype=object)*(1<<(2*bu)),2*bu)
  scale=max(bu,b0+bx);R=Uf*(1<<(scale-bu))-(U0f*fm(xn))*(1<<(scale-b0-bx));rn=sum(int(x)**2 for rr in R.tolist() for x in rr);r2=F(rn,1<<(2*scale));r=arb(fmpq(r2.numerator,r2.denominator)).sqrt()
  A=fm(un[:-2]);B=fm(un[2:]);G=A.transpose()*A;H=A.transpose()*B;GT=G*fm(tn);N=arr(H*(1<<bt)-GT);n2=F(sum(int(x)**2 for x in N.flat),1<<(4*bu+2*bt));nu=arb(fmpq(n2.numerator,n2.denominator)).sqrt()
  bnorm=sum(int(x)**2 for x in un[2:].flat);quad=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(GT).flat));cross=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(H).flat));snum=(bnorm<<(2*bt))+quad-2*(cross<<bt);assert snum>=0;s2=F(snum,1<<(2*bu+2*bt))
  status,gates,b=classify(q,eta,nu,r,c)
  if b is not None:assert a([s2.numerator,s2.denominator]).sqrt()<=b['shift']
  row.update(status=status,gates=gates,retained_Gram_defect_F_upper=up(eta),alignment_residual_squared=[str(r2.numerator),str(r2.denominator)],alignment_residual_F_upper=up(r),normal_residual_squared=[str(n2.numerator),str(n2.denominator)],normal_F_upper=up(nu),actual_raw_shift_squared=[str(s2.numerator),str(s2.denominator)],actual_raw_shift_F_upper=up(a([s2.numerator,s2.denominator]).sqrt()),direct_bound=None if b is None else {k:down(v) if k=='amin' else up(v) for k,v in b.items()},readable=dict(alignment_residual_F_upper=float(r.upper()),normal_F_upper=float(nu.upper()),retained_Gram_defect_F_upper=float(eta.upper()),direct_returned_shift_upper=None if b is None else float(b['shift'].upper()),fixed_raw_frame_budget_lower=float(c['raw'].lower()),fixed_normal_cap=float(c['nu'].upper())),scope='Measured frame displacement includes changed preparations, encoded noise and numerical error. No full SVD/order/phase/all-gates certificate; fixed-budget refusals retained even if diagnostic direct shift passes.');rows.append(row);print(json.dumps(dict(case=name,status=status,readable=row['readable'])),flush=True)
 return dict(status='BROADER_FIXED_BUDGET_EVALUATION_COMPLETE',rows=rows,certified=sum(x['status']=='CERTIFIED_FRESH_MEASURED_SOURCE_FRAME_SHIFT' for x in rows),held=sum(x['status'].startswith('HOLD') for x in rows),budget_sha256=sha(P/'inputs/FIXED_BUDGET.json'),protocol_sha256=sha(P/'PROTOCOL_FREEZE.json'),data_freeze_sha256=sha(P/'DATA_FREEZE.json'),alignment_freeze_sha256=sha(P/'ALIGNMENT_FREEZE.json'),external_review='PENDING',physical_promotion=0)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify(args.source);dest=P/'CERTIFICATE.json'
 if args.replay:assert json.loads(dest.read_text())==r
 else:assert not dest.exists();dest.write_text(json.dumps(r,indent=2))
