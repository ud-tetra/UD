"""Exact source-frame residuals and normal equations for three frozen floating outputs."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq
from common import P,freeze,check_evidence,sha,a,up
from numeric_math import encode
from proof_math import fm,arr,norm_exact
def verify(evidence):
 f=freeze();check_evidence(evidence);pf=json.loads((P/'PROPOSAL_FREEZE.json').read_text())
 for n,h in pf['files'].items():assert sha(P/n)==h
 U0=np.vstack([np.load(evidence/('U0_'+k+'.npz'),allow_pickle=False)['basis'] for k in ['A','B']]);u0,b0=encode(U0);U0f=fm(u0)
 old=json.loads((P/'inputs/PARENT_NORMAL.json').read_text())['rows'];gates=json.loads((P/'inputs/PARENT_GATES.json').read_text())['rows'];data=json.loads((P/'inputs/PARENT_DATA.json').read_text())['records'];rows=[]
 for n in f['cases']:
  row0=next(x for x in old if x['case']==n);gr=next(x for x in gates if x['case']==n);dr=next(x for x in data if x['case']==n)
  assert row0['record_sha256']==gr['record_sha256']==dr['record_sha256'] and dr['noise_budget']==[1,1<<48] and dr['vector_integer_squared_error_max']==1
  U1=np.vstack([np.load(evidence/f'{n}_F{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209]
  with np.load(evidence/f'{n}_PHASE.npz',allow_pickle=False) as z:T=z['shift']
  with np.load(P/'witnesses'/f'{n}.npz',allow_pickle=False) as z:X=z['alignment']
  assert U1.shape==(8191,209) and T.shape==X.shape==(209,209)
  un,bu=encode(U1);tn,bt=encode(T);xn,bx=encode(X);Uf=fm(un);Gfull=Uf.transpose()*Uf
  eta=norm_exact(arr(Gfull)-np.eye(209,dtype=object)*(1<<(2*bu)),2*bu);assert eta<1
  scale=max(bu,b0+bx);R=Uf*(1<<(scale-bu))-(U0f*fm(xn))*(1<<(scale-b0-bx));rn=sum(int(x)**2 for rr in R.tolist() for x in rr);r2=F(rn,1<<(2*scale));r=arb(fmpq(r2.numerator,r2.denominator)).sqrt()
  A=fm(un[:-2]);B=fm(un[2:]);G=A.transpose()*A;H=A.transpose()*B;GT=G*fm(tn);N=arr(H*(1<<bt)-GT);n2=F(sum(int(x)**2 for x in N.flat),1<<(4*bu+2*bt))
  bnorm=sum(int(x)**2 for x in un[2:].flat);quad=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(GT).flat));cross=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(H).flat));snum=(bnorm<<(2*bt))+quad-2*(cross<<bt);assert snum>=0;s2=F(snum,1<<(2*bu+2*bt))
  assert n2==F(*map(int,row0['exact_normal_residual_squared'])) and s2==F(*map(int,row0['exact_shift_residual_squared']))
  nu=arb(fmpq(n2.numerator,n2.denominator)).sqrt();svd=json.loads((evidence/f'{n}_SVD.json').read_text());assert svd['status']=='CERTIFIED_ACTUAL_SVD_ORDER' and svd['learned_order']==209
  row={'case':n,'record_sha256':row0['record_sha256'],'retained_Gram_defect_F_upper':up(eta),'alignment_residual_squared':[str(r2.numerator),str(r2.denominator)],'alignment_residual_F_upper':up(r),'normal_residual_squared':[str(n2.numerator),str(n2.denominator)],'normal_F_upper':up(nu),'actual_raw_shift_squared':[str(s2.numerator),str(s2.denominator)],'full_SVD_F_error_upper':svd['singular_error_upper'],'auxiliary_X_sha256':pf['files'][f'witnesses/{n}.npz'],'source_and_output_members':{x['destination']:x['sha256'] for x in json.loads((P/'INPUT_INDEX.json').read_text())['members'] if x['destination'].startswith((n,'U0_'))},'scope':'Measured source-subspace displacement includes input perturbation and floating effects; not roundoff alone. Exact normal/shift fractions match PR217.','readable':{'alignment_residual_F_upper':float(r.upper()),'retained_Gram_defect_F_upper':float(eta.upper()),'normal_F_upper':float(nu.upper())},'physical_promotion':0};rows.append(row);print(json.dumps({'case':n,'readable':row['readable']}),flush=True)
 return {'status':'CERTIFIED_THREE_DIRECT_DYADIC_SOURCE_FRAME_AND_NORMAL_WITNESSES','rows':rows,'new_state_estimator_runs':0,'external_review':'PENDING','physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify(args.evidence);dest=P/'DIRECT_METRICS.json'
 if args.replay:assert json.loads(dest.read_text())==r
 else:assert not dest.exists();dest.write_text(json.dumps(r,indent=2))
