"""Exact augmented-sketch Gram and residual-verified spectral enclosures."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time,resource,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigh
from flint import ctx,arb,fmpq
from proof_math import fm,arr,norm_exact,up,down,quantize64
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(record,out):
 t=time.monotonic();out=Path(out);out.mkdir(parents=True,exist_ok=False)
 frozen=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());contract=P/'inputs/FROZEN_CONTRACT.json'
 assert sha(contract)==frozen['contract_sha256']
 assert Path(record).stat().st_size==150321232
 before=sha(record);Y=np.memmap(record,dtype='<i8',mode='r',shape=(37,8191,62))
 X=np.array(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64)
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 short=np.asarray(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64)
 assert short.shape==(320,)
 v=np.pad(short,(0,1974))
 A=np.column_stack((2*W,v));maxraw=max(abs(int(X.min())),abs(int(X.max())))
 # Bound every partial sum in signed int64 before multiplication.
 col_l1=max(sum(abs(int(x)) for x in A[:,j]) for j in range(161))
 assert maxraw*col_l1<2**63
 Z=X@A;del X
 z=fm(Z);G=z.transpose()*z;gg=arr(G)
 np.savez_compressed(out/'EXACT_SKETCH_GRAM.npz',integers_decimal=np.array([[str(x) for x in row] for row in gg]))
 d,Q=eigh(np.asarray(gg,dtype=float)/2.**110,check_finite=False);idx=np.argsort(d)[::-1];d=d[idx];Q=Q[:,idx]
 qn=quantize64(Q,60);dn=quantize64(d,40);assert np.all(dn[:-1]>=dn[1:]);q=fm(qn)
 np.savez_compressed(out/'EIGEN_PROPOSAL.npz',Q=qn,eigenvalues=dn)
 eta=norm_exact(arr(q.transpose()*q)-np.eye(161,dtype=object)*(1<<120),120)
 # G*Q uses denominator 2^(110+60); Q*Lambda denominator 2^100.
 R=arr(G*q)-qn.astype(object)*dn.astype(object)[None,:]*(1<<70)
 res=norm_exact(R,170);gnorm=norm_exact(gg,110);assert eta<1
 normq=(1+eta).sqrt();dist=eta/(1+(1-eta).sqrt())
 radius=gnorm*eta+res*normq+arb(max(abs(int(x)) for x in dn))/(1<<40)*dist*(normq+1)
 rule=json.loads((P/'inputs/SKETCH_RULE.json').read_text());cut=arb(fmpq(*rule['cutoff']));noise=arb(fmpq(*rule['noise_squared_ceiling'])).sqrt()
 # Use squared threshold comparisons to avoid square roots of negative lower bounds.
 cutoff2=cut*cut;above=[];below=[]
 for i,n in enumerate(dn):
  center=arb(int(n))/(1<<40)
  if center-radius>cutoff2:above.append(i)
  elif center+radius<cutoff2:below.append(i)
  else:raise ArithmeticError('HOLD: exact sketch order unresolved')
 count=len(above);assert above==list(range(count))
 if count==0:raise ArithmeticError('HOLD: no resolved positive sketch modes')
 lo=(arb(int(dn[count-1]))/(1<<40)-radius).sqrt();hi=(arb(int(dn[0]))/(1<<40)+radius).sqrt()
 tail=(arb(int(dn[count]))/(1<<40)+radius).sqrt() if count<161 else arb(0)
 result={'status':'CERTIFIED_EXACT_SKETCH_ORDER_AND_CONDITION','scope':'161-column temporal sketch only, not full Hankel spectral acceptance','record_sha256':before,'contract_sha256':sha(contract),'sketch_rule_sha256':sha(P/'inputs/SKETCH_RULE.json'),'witness_sha256':sha(P/'inputs/NULL_VECTOR.json'),'gram_shape':[161,161],'gram_denominator':2**110,'integer_partial_sum_upper':maxraw*col_l1,'above_cutoff_count':count,'cutoff':rule['cutoff'],'retained_sigma_lower':down(lo),'largest_sigma_upper':up(hi),'discarded_sigma_upper':up(tail),'retained_condition_upper':up(hi/lo),'eigenvector_orthogonality_defect_upper':up(eta),'eigenpair_residual_upper':up(res),'gram_eigenvalue_radius_upper':up(radius),'all_eigenvalues_classified':len(above)+len(below)==161,'uniform_105_separation_in_error_ball':bool(count==105 and lo-noise>cut and tail+noise<cut),'full_record_signature_certified':False,'physical_promotion':0,'independent_review':'pending','source_operator_or_nominal_modes_used':False,'wall_seconds':time.monotonic()-t,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'readable':{'sigma_retained_lower':float(lo.lower()),'sigma_largest_upper':float(hi.upper()),'sigma_discarded_upper':float(tail.upper()),'condition_upper':float((hi/lo).upper()),'cutoff':float(F(*rule['cutoff'])),'noise_envelope':float(noise.upper())}}
 assert sha(record)==before
 result['input_identity_stable']=True
 (out/'SKETCH_CERTIFICATE.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2),flush=True)
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('output');a=p.parse_args();run(a.record,a.output)
