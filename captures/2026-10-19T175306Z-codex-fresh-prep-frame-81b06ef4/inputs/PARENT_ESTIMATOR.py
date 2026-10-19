"""Integerprojection variant; same SVD/lagtwoLS/eigen/angle arithmetic. No sourcephases."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,time
import numpy as np
from scipy.linalg import svd,lstsq,eigvals,eig
from bindings import P,sha,freeze
from sketch import sketch
import full_svd

def run():
 f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json');A=sketch();anchor=[]
 for k,source in enumerate(f['integer_anchor']):
  p=P.parent/source['path'];assert sha(p)==source['sha256']
  with np.load(p) as z:anchor.append(z['numerator'])
 anchor=np.vstack(anchor);out=P/'results';out.mkdir(exist_ok=False);ranges=[(0,2731),(2731,5462),(5462,8191)];executions=[]
 for row in data['records']:
  name=row['case'];t=time.monotonic();raw=P/'records'/(name+'.i64le');assert sha(raw)==row['record_sha256'];Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);mx=max(abs(int(X.min())),abs(int(X.max())));assert mx*int(np.abs(A).sum(axis=0).max())<2**63;N=X@A;del X
  nmax=max(abs(int(N.min())),abs(int(N.max())));assert nmax<=2504646576090828<2**53;delta=N-anchor;assert max(abs(int(delta.min())),abs(int(delta.max())))<=1040
  case=out/name;case.mkdir();d=case/'results/integer_projection';d.mkdir(parents=True);Z=N.astype(float)/2.**55;U,s,vt=svd(Z,full_matrices=False,check_finite=False);q=int(np.count_nonzero(s>2.**-24));np.savez_compressed(d/'SVD_META.npz',singular=s,right_transpose=vt)
  for k,(a,b) in enumerate(ranges):
   np.savez_compressed(case/f'SKETCH_DELTA_{k}.npz',delta=delta[a:b].astype(np.int16));np.savez_compressed(case/'results'/f'INTEGER_{k}.npz',numerator=N[a:b]);np.savez_compressed(d/f'FACTOR_{k}.npz',left=U[a:b],delta=np.zeros((b-a,321),np.int64),projection_bits=55,projection_sha256=__import__('hashlib').sha256(Z[a:b].astype('<f8').tobytes()).hexdigest())
  disc={'case':name,'record_sha256':sha(raw),'cutoff':[1,1<<24],'learned_order':q,'rank_not_forced':True,'source_phases_loaded':False,'projection_backend':'Exact int64 thenexactdyadicconversion','raw_projection_readings':18790154,'integer_projection_entries':int(N.size),'integer_partial_bound':mx*int(np.abs(A).sum(axis=0).max()),'integer_numerator_max':nmax,'physical_promotion':0}
  (d/'DISCOVERY.json').write_text(json.dumps(disc,indent=2));print(json.dumps(disc),flush=True)
  if q>=3 and q<321 and q%2==1:
   ur=U[:,:q];T=lstsq(ur[:-2],ur[2:],check_finite=False)[0];ev=eigvals(T,check_finite=False);angles=np.angle(ev);em=np.rint(angles*2.**60).astype(np.int64);np.savez_compressed(d/'PHASE_PROPOSAL.npz',two_step_phase=em)
   vals,V=eig(T,check_finite=False);match=np.argmin(abs(ev[:,None]-vals[None,:]),axis=1);assert len(set(map(int,match)))==q;V=V[:,match];H=np.linalg.inv(V);np.savez_compressed(d/'PHASE_META.npz',shift=T,eigenvalues=ev,angles=angles,eigenvectors=V,inverse=H)
  else:(d/'HOLD.json').write_text(json.dumps({'status':'HOLD_SOURCE_PRECISION_ORDER','order':q}))
  old=full_svd.P;full_svd.P=case
  try:cert=full_svd.certify('integer_projection',write=True)
  finally:full_svd.P=old
  executions.append({'case':name,'seconds':time.monotonic()-t,'order':q,'SVD_certificate':cert['status']});assert sha(raw)==row['record_sha256'];(P/'RUN_EXECUTIONS.json').write_text(json.dumps(executions,indent=2))
if __name__=='__main__':run()
