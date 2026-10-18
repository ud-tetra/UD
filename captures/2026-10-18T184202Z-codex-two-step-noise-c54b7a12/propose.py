"""New two-step record-only adapter; source phases/rates/coefficients are not loaded."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd,lstsq,eigvals,eig
from bindings import P,sha,freeze
from sketch import sketch

def run(record,out,instrument=False):
 f=freeze();t=time.monotonic();record=Path(record);out=Path(out);out.mkdir(parents=True,exist_ok=False);before=sha(record);assert record.stat().st_size==150321232
 Y=np.memmap(record,dtype='<i8',mode='r',shape=(37,8191,62));D=np.asarray(Y.transpose(1,2,0).reshape(8191,2294),float)/2.**48;Z=D@(sketch().astype(float)/128.)
 U,s,_=svd(Z,full_matrices=False,check_finite=False);cut=f['source_precision_cutoff'][0]/f['source_precision_cutoff'][1];q=int(np.count_nonzero(s>cut));audit={'record_sha256':before,'learned_order_float':q,'cutoff':f['source_precision_cutoff'],'singular_values_float':s.tolist(),'source_phases_loaded':False,'instrumented':instrument,'physical_promotion':0};(out/'DISCOVERY.json').write_text(json.dumps(audit,indent=2))
 if q<3 or q>=321 or q%2!=1:
  (out/'HOLD.json').write_text(json.dumps({'status':'HOLD_SOURCE_PRECISION_ORDER','order':q},indent=2));return
 U=U[:,:q];T=lstsq(U[:-2],U[2:],check_finite=False)[0];ev=eigvals(T,check_finite=False);angles=np.angle(ev);emitted=np.rint(angles*2.**60).astype(np.int64);np.savez_compressed(out/'PHASE_PROPOSAL.npz',two_step_phase=emitted)
 if instrument:
  vals,V=eig(T,check_finite=False);matching=np.argmin(abs(ev[:,None]-vals[None,:]),axis=1);assert len(set(map(int,matching)))==q;V=V[:,matching];H=np.linalg.inv(V)
  np.savez_compressed(out/'BASIS_A.npz',basis=U[:4096]);np.savez_compressed(out/'BASIS_B.npz',basis=U[4096:]);np.savez_compressed(out/'FLOAT_META.npz',shift=T,eigenvalues=ev,eigenvectors=V,inverse=H,angles=angles)
 assert sha(record)==before;(out/'REPORT.json').write_text(json.dumps({'record_sha256':before,'proposal_sha256':sha(out/'PHASE_PROPOSAL.npz'),'learned_order':q,'seconds':time.monotonic()-t,'physical_promotion':0,'independent_review':'pending'},indent=2));print(json.dumps({'order':q,'instrumented':instrument,'seconds':time.monotonic()-t}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('out');p.add_argument('--instrument',action='store_true');a=p.parse_args();run(a.record,a.out,a.instrument)
