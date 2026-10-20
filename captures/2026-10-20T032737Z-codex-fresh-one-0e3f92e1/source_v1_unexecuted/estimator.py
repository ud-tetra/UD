"""Same frozen numerical arithmetic, one transient raw record at a time."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,time,hashlib,platform
from pathlib import Path
import numpy as np,scipy
from scipy.linalg import svd,lstsq,eigvals,eig
from common import P,freeze,sha

def sketch():
 old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64);assert int(v@v)==16228 and np.all(v@old==0);return np.column_stack((2*old,v,2*new))
def project(raw):
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch();mx=max(abs(int(X.min())),abs(int(X.max())));partial=mx*int(np.abs(A).sum(axis=0).max());assert partial<2**63;N=X@A;maximum=max(abs(int(N.min())),abs(int(N.max())));assert maximum<2**53,'HOLD exact dyadic projection range';return N,dict(partial_sum_bound=partial,numerator_max=maximum,integer_bytes_sha256=hashlib.sha256(N.astype('<i8').tobytes()).hexdigest(),projection_bytes_sha256=hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest())
def estimate(raw,record):
 freeze();start=time.monotonic();assert sha(raw)==record['record_sha256'];name=record['case'];case=P/'results'/name;case.mkdir(parents=True,exist_ok=False);q=None;error=None;projection=None
 try:
  N,projection=project(raw);Z=N.astype(float)/2.**55;U,s,vt=svd(Z,full_matrices=False,check_finite=False);q=int(np.count_nonzero(s>2.**-24));np.savez_compressed(case/'SVD_META.npz',singular=s,right_transpose=vt)
  for k,(a,b) in enumerate([(0,2731),(2731,5462),(5462,8191)]):np.savez_compressed(case/f'U_{k}.npz',basis=U[a:b,:q])
  if q>=3 and q<321 and q%2==1:
   ur=U[:,:q];T=lstsq(ur[:-2],ur[2:],check_finite=False)[0];ev=eigvals(T,check_finite=False);angles=np.angle(ev);em=np.rint(angles*2.**60).astype(np.int64);vals,V=eig(T,check_finite=False);match=np.argmin(abs(ev[:,None]-vals[None,:]),axis=1);assert len(set(map(int,match)))==q;V=V[:,match];H=np.linalg.inv(V);np.savez_compressed(case/'PHASE_META.npz',shift=T,eigenvalues=ev,angles=angles,eigenvectors=V,inverse=H);np.savez_compressed(case/'PHASE_PROPOSAL.npz',two_step_phase=em)
 except Exception as exc:error=dict(type=type(exc).__name__,message=str(exc),policy='HOLD; no retry or replacement or fallback')
 r=dict(case=name,record_sha256=record['record_sha256'],learned_order=q,execution_status='COMPLETED' if error is None else 'HOLD_ESTIMATOR_EXECUTION',execution_error=error,cutoff=[1,1<<24],rank_not_forced=True,source_phases_loaded_by_estimator=False,projection=projection,numeric_witnesses={x.name:sha(x) for x in case.glob('*.npz')},full_SVD_certificate_executed=False,python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,seconds=time.monotonic()-start,physical_promotion=0);(case/'RUN.json').write_text(json.dumps(r,indent=2));assert sha(raw)==record['record_sha256'];print(json.dumps(dict(stage='actual_floating_estimator',case=name,order=q,execution_status=r['execution_status'])),flush=True);return r
