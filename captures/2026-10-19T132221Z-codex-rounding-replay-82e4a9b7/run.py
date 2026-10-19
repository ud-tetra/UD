"""Prospectively frozen paired fullfactor experiment on archived cyclic record."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,hashlib,time,platform
from pathlib import Path
import numpy as np,scipy
from scipy.linalg import svd,lstsq,eigvals
from sketch import sketch
from certify import P,sha,encode,up,arb

def run():
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h
 raw=P.parent/'uniform-two-work/records/cyclic_unit.i64le';assert sha(raw)==f['record_sha256']
 out=P/'results';out.mkdir(exist_ok=False)
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch()
 maxraw=max(abs(int(X.min())),abs(int(X.max())));l1=np.abs(A).sum(axis=0);assert maxraw*int(l1.max())<2**63
 t=time.monotonic();N=X@A;print('integer projection seconds',time.monotonic()-t,flush=True)
 L=np.abs(A).reshape(62,37,321).max(axis=0).sum(axis=0);nmax=max(abs(int(N.min())),abs(int(N.max())));allball=nmax+2*int(L.max());predicate=allball<2**53
 gamma=arb(2294)/(arb(2)**53-2294);bound=gamma*arb(30100665057351)/(1<<55)*(arb(8191)*(320*4588**2+1634**2)).sqrt()
 rounding={'legacy_range_only_conditional_projection_upper':up(bound),'legacy_arithmetic_model':'binary64 correctly rounded conventional reductions, no reduced precision, at most2294 rounds per term; opaque BLAS not independently qualified','raw_input_max':maxraw,'int64_partial_bound':(30100665057351)*int(l1.max()),'integer_product_max':nmax,'encoded_ball_integer_max_upper':allball,'encoded_ball_2pow53_predicate':predicate,'L_max':int(L.max()),'scope':'Encoded unit ball per62vector about PR195stress; cyclic anchor eligibility separately verified','uniform_SVD_or_phase_guarantee':False,'physical_promotion':0}
 (out/'ROUNDING.json').write_text(json.dumps(rounding,indent=2));print(json.dumps(rounding),flush=True)
 ranges=[(0,2731),(2731,5462),(5462,8191)]
 for k,(a,b) in enumerate(ranges):np.savez_compressed(out/f'INTEGER_{k}.npz',numerator=N[a:b])
 for mode in ['legacy_gemm','integer_projection']:
  d=out/mode;d.mkdir();Z=(X.astype(float)/2.**48)@(A.astype(float)/128.) if mode=='legacy_gemm' else N.astype(float)/2.**55
  U,s,vt=svd(Z,full_matrices=False,check_finite=False);q=int(np.count_nonzero(s>2.**-24));np.savez_compressed(d/'SVD_META.npz',singular=s,right_transpose=vt)
  for k,(a,b) in enumerate(ranges):
   zn,bz=encode(Z[a:b]);bb=max(55,bz);delta=zn*(1<<(bb-bz))-N[a:b].astype(object)*(1<<(bb-55));dm=max(abs(int(x)) for x in delta.flat);delta=np.array(delta,dtype=np.int64 if dm<2**63 else str)
   np.savez_compressed(d/f'FACTOR_{k}.npz',left=U[a:b],delta=delta,projection_bits=bb,projection_sha256=hashlib.sha256(Z[a:b].astype('<f8').tobytes()).hexdigest())
  if q>=3 and q<321 and q%2==1:
   T=lstsq(U[:-2,:q],U[2:,:q],check_finite=False)[0];ev=eigvals(T,check_finite=False);angles=np.angle(ev);np.savez_compressed(d/'PHASE_PROPOSAL.npz',two_step_phase=np.rint(angles*2.**60).astype(np.int64));np.savez_compressed(d/'PHASE_META.npz',shift=T,eigenvalues=ev,angles=angles)
  (d/'DISCOVERY.json').write_text(json.dumps({'order':q,'record_sha256':sha(raw),'cutoff':[1,1<<24],'source_phases_loaded':False,'phase_certificate':'NOT_CLAIMED_BY_THIS_SVD_TEST'},indent=2));print(mode,'order',q,flush=True)
 (out/'EXECUTION.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'record_sha256':sha(raw),'new_paired_estimator_executions':2,'elapsed_seconds':time.monotonic()-t,'physical_promotion':0},indent=2))
if __name__=='__main__':run()
