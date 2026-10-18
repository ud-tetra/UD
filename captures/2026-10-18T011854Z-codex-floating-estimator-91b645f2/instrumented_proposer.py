#!/usr/bin/env python3
"""Untrusted record-only temporal proposal. No nominal operator, roots or modal data."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,time,json,hashlib,resource
from pathlib import Path
import numpy as np
from scipy.linalg import svd,lstsq,eigvals,eig
PROTOCOL='ba28c60cffd40806d3ecd76bf83db7b2caac71de9173b0de7a471b504e84d20c'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(record_path,contract_path,out):
 t=time.monotonic();out=Path(out);out.mkdir(parents=True,exist_ok=True)
 if (out/'PROPOSAL.npz').exists():raise FileExistsError('Never overwrite a proposal')
 if sha(contract_path)!=PROTOCOL:raise ValueError('Frozen contract changed')
 contract=json.loads(Path(contract_path).read_text());fmt=contract['data_format'];shape=tuple(fmt['shape'])
 if Path(record_path).stat().st_size!=fmt['bytes']:raise ValueError('Record incomplete')
 before=sha(record_path);Y=np.memmap(record_path,dtype=fmt['dtype'],mode='r',shape=shape)
 # Time rows; output columns c*preparations+a. The random mixture only proposes a basis.
 D=np.asarray(Y.transpose(1,2,0).reshape(shape[1],-1),dtype=np.float64)/2.**48
 rng=np.random.default_rng(172026);old_mix=rng.choice([-1.,1.],size=(D.shape[1],160))/64.
 witness=Path(__file__).resolve().parent/'inputs/NULL_VECTOR.json'
 short=np.asarray(json.loads(witness.read_text())['vector'],dtype=np.int64)
 if short.shape!=(320,):raise ValueError('Expected 320-coordinate sparse witness prefix')
 v=np.pad(short,(0,1974))
 if v.shape!=(2294,) or int(v@v)!=16228:raise ValueError('Witness format/norm mismatch')
 if np.any(v@old_mix):raise ValueError('Witness is not orthogonal to old sketch')
 mix=np.column_stack((old_mix,v.astype(float)/128.));Z=D@mix
 delta=contract['history_vector_error_ceiling'][0]/contract['history_vector_error_ceiling'][1]
 sketch_frobenius=np.sqrt(371097)/64.
 noise_envelope=np.sqrt(shape[0]*shape[1])*delta*sketch_frobenius
 cutoff_pair=json.loads((Path(__file__).resolve().parent/'inputs/SKETCH_RULE.json').read_text())['cutoff']
 cutoff=cutoff_pair[0]/cutoff_pair[1]
 U,s,_=svd(Z,full_matrices=False,check_finite=False);q=int(np.count_nonzero(s>cutoff))
 print('learned temporal dimension',q,'absolute cutoff',cutoff,flush=True)
 audit={'temporal_dimension':q,'mixture_columns':161,'cutoff':cutoff,'singular_values_float':s.tolist(),'acceptance_certificate':False,'physical_promotion':0,'record_sha256':before,'contract_sha256':PROTOCOL,'witness_sha256':sha(witness),'model_support':'stationary plus non-Nyquist conjugate pairs only'}
 (out/'DISCOVERY_AUDIT.json').write_text(json.dumps(audit,indent=2))
 if q<3 or q>=161 or q%2!=1:
  if sha(record_path)!=before:raise RuntimeError('Record changed')
  raise ArithmeticError('HOLD: proposal order incompatible with current stationary/conjugate-pair model')
 shift=lstsq(U[:-1,:q],U[1:,:q],check_finite=False)[0];ev=eigvals(shift,check_finite=False);ph=np.angle(ev)
 # A proposed real oscillatory frame with a stationary term. The verifier checks its full residual.
 pos=np.sort(ph[ph>1e-10]);neg=np.sort(-ph[ph<-1e-10]);zero=ph[np.abs(ph)<=1e-10]
 if len(pos)!=(q-1)//2 or len(zero)!=1 or np.max(abs(pos-neg))>1e-8:raise ArithmeticError('HOLD: conjugate proposal pairing failed')
 theta=np.rint(pos*2.**60).astype(np.int64);k=np.arange(shape[1],dtype=np.float64);design=np.ones((shape[1],q))
 for j,x in enumerate(theta):
  angle=k*(float(x)/2.**60);design[:,2*j+1]=np.cos(angle);design[:,2*j+2]=np.sin(angle)
 C=lstsq(design,D,check_finite=False)[0]
 if not np.all(np.isfinite(C)) or np.max(abs(C))>1:raise ArithmeticError('HOLD: proposal amplitude range')
 coeff=np.rint(C*2.**60).astype(np.int64)
 np.savez_compressed(out/'PROPOSAL.npz',theta=theta,coeff=coeff)
 residual=D-design@(coeff.astype(float)/2.**60)
 info={'status':'UNTRUSTED_PROPOSAL_ONLY','physical_promotion':0,'independent_review':'pending','nominal_frequencies_or_factors_loaded':False,'input_files':{'record_sha256':before,'contract_sha256':PROTOCOL},'proposal_sha256':sha(out/'PROPOSAL.npz'),'temporal_dimension':q,'positive_frequency_count':len(pos),'mixture_columns':161,'seed':172026,'discovery_absolute_cutoff':cutoff,'noise_sketch_norm_envelope':noise_envelope,'sketch_denominator':128,'original_sign_columns_scaled_by':2,'complement_column':'v/128','modal_rank_allocation':'global paired target-rank energy proposal, checked by complete residual','max_float_entry_residual':float(np.max(abs(residual))),'phase_pairing_error':float(np.max(abs(pos-neg))),'unit_modulus_eigenvalue_defect':float(np.max(abs(abs(ev)-1))),'proposal_singular_value_above_cutoff':float(s[q-1]),'proposal_singular_value_below_cutoff':float(s[q]),'seconds':time.monotonic()-t,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 # Read-only instrumentation after the original phase/coefficient arithmetic.
 other_values,vectors=eig(shift,check_finite=False)
 matching=np.argmin(abs(ev[:,None]-other_values[None,:]),axis=1)
 if len(set(int(x) for x in matching))!=q:raise ArithmeticError('HOLD: eigenvector witness pairing unresolved')
 vectors=vectors[:,matching];inverse=np.linalg.inv(vectors)
 reduction=U[:,:q].T@Z
 np.savez_compressed(out/'FLOAT_WITNESS.npz',basis=U[:,:q],shift=shift,eigenvalues=ev,eigenvectors=vectors,inverse=inverse,reduction=reduction,angles=ph)
 if sha(record_path)!=before:raise RuntimeError('Record changed')
 (out/'PROPOSAL_REPORT.json').write_text(json.dumps(info,indent=2));print(json.dumps(info,indent=2),flush=True)
 return info
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('contract');p.add_argument('output');a=p.parse_args()
 try:run(a.record,a.contract,a.output)
 except (ArithmeticError,ValueError) as e:
  out=Path(a.output);out.mkdir(exist_ok=True,parents=True);(out/'HOLD.json').write_text(json.dumps({'status':'HOLD','reason':str(e),'acceptance_certificate':False},indent=2));print('HOLD',str(e),flush=True)
