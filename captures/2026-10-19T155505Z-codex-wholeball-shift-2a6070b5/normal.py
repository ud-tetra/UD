"""Exact dyadic normal equations and fixed-returned-basis LS minimum enclosure."""
import sys
sys.dont_write_bytecode=True
import json,argparse
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq,ctx
from bounds import P,freeze,sha,a,up,down,terms
from numeric_math import encode
from proof_math import fm,arr
ctx.prec=512
def verify(evidence):
 f=freeze()
 for index in ['PACKAGE_MANIFEST.json','ARRAY_INDEX.json']:
  assert sha(evidence/index)==f['evidence_indices_sha256'][index]
  for row in json.loads((evidence/index).read_text())['files']:
   rel=Path(row['path']);assert not rel.is_absolute() and '..' not in rel.parts;q=evidence/rel
   assert q.is_file() and q.stat().st_size==row['size_bytes'] and sha(q)==row['sha256']
 gates=json.loads((evidence/'GATE_RESULTS.json').read_text())['rows'];data=json.loads((evidence/'DATA_FREEZE.json').read_text())['records'];t=terms('returned_F_certificate',f['encoded_radius']);rows=[]
 for entry in gates:
  name=entry['case'];raw=next(x for x in data if x['case']==name);assert raw['record_sha256']==entry['record_sha256'] and raw['vector_integer_squared_error_max']==1 and raw['noise_budget']==f['encoded_radius']
  d=evidence/'results'/name/'results/integer_projection';cert=json.loads((d/'CERTIFICATE.json').read_text());assert cert['status']=='CERTIFIED_ACTUAL_SVD_ORDER' and cert['learned_order']==209
  oldg=json.loads((P/'inputs/PR210_FREEZE.json').read_text())['gates']
  for metric in ['full_left_orthogonality','full_right_orthogonality','full_SVD_error']:assert a(entry['metrics'][metric])<=a(oldg[metric])
  U=np.vstack([np.load(d/f'FACTOR_{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209]
  with np.load(d/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
  assert U.shape==(8191,209) and T.shape==(209,209)
  un,bu=encode(U);tn,bt=encode(T);A=fm(un[:-2]);B=fm(un[2:]);G=A.transpose()*A;H=A.transpose()*B;GT=G*fm(tn)
  n=arr(H*(1<<bt)-GT);n2=F(sum(int(x)**2 for x in n.flat),1<<(4*bu+2*bt))
  # Exact expanded Frobenius residual, not a rounded norm used as a lower bound.
  bnorm=sum(int(x)**2 for x in un[2:].flat);quad=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(GT).flat));cross=sum(int(x)*int(y) for x,y in zip(tn.flat,arr(H).flat))
  snum=(bnorm<<(2*bt))+quad-2*(cross<<bt);assert snum>=0;s2=F(snum,1<<(2*bu+2*bt))
  s=arb(fmpq(s2.numerator,s2.denominator)).sqrt();nu=arb(fmpq(n2.numerator,n2.denominator)).sqrt();gap=nu/t['amin'];lower_square=arb(fmpq(s2.numerator,s2.denominator))-gap**2
  low=arb(0) if not lower_square>0 else arb(lower_square.lower()).sqrt()
  upper=(t['J']**2+gap**2).sqrt();assert s<=upper
  old_shift=a(oldg['raw_shift_residual']);old_recorded=a(entry['metrics']['raw_shift_residual']);assert s<=old_recorded
  row={'case':name,'record_sha256':entry['record_sha256'],'exact_shift_residual_squared':[str(s2.numerator),str(s2.denominator)],'exact_normal_residual_squared':[str(n2.numerator),str(n2.denominator)],
       'normal_residual_F_upper':up(nu),'LS_residual_component_gap_upper':up(gap),'exact_LS_minimum_residual_lower':down(low),'exact_LS_minimum_residual_upper':up(s),
       'conditional_wholeball_returned_shift_upper':up(upper),
       'every_shift_on_this_saved_basis_violates_v1_gate':bool(low>old_shift),
       'original_policy_status':entry['status'],'readable':{'normal_residual_F_upper':float(nu.upper()),'LS_component_gap_upper':float(gap.upper()),'exact_LS_minimum_residual_lower':float(low.lower()),'exact_LS_minimum_residual_upper':float(s.upper()),'wholeball_returned_shift_upper':float(upper.upper())},'physical_promotion':0}
  rows.append(row);print(json.dumps(row),flush=True)
 return {'status':'CERTIFIED_NORMAL_RESIDUAL_AND_FIXED_BASIS_LS_MINIMUM','rows':rows,'new_SVD_or_fits':0,'external_review':'PENDING','physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);p.add_argument('--replay',action='store_true');a0=p.parse_args();r=verify(a0.evidence.resolve());q=P/'NORMAL_CERTIFICATES.json'
 if a0.replay:assert json.loads(q.read_text())==r
 else:
  assert not q.exists();q.write_text(json.dumps(r,indent=2))
