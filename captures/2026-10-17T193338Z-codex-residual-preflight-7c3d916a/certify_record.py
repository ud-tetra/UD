#!/usr/bin/env python3
"""Certificate from a frozen numeric record and untrusted learned modal proposal only."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,time,json,hashlib,resource,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import ctx,arb,acb
from proof_math import fm,arr,dyad,up,verify
from residual_preflight import residual_preflight
ctx.prec=512
PROTOCOL='ba28c60cffd40806d3ecd76bf83db7b2caac71de9173b0de7a471b504e84d20c'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(record_path,contract_path,proposal_path,work):
 start=time.monotonic();O=Path(work);O.mkdir(exist_ok=False,parents=True);progress=[]
 def emit(stage,**info):
  progress.append({'stage':stage,'elapsed_seconds':time.monotonic()-start,**info});(O/'PROGRESS.json').write_text(json.dumps(progress,indent=2));print(stage,info,flush=True)
 hashes={'record':sha(record_path),'contract':sha(contract_path),'proposal':sha(proposal_path)}
 if hashes['contract']!=PROTOCOL:raise ValueError('Frozen contract mismatch')
 contract=json.loads(Path(contract_path).read_text());fmt=contract['data_format'];shape=tuple(fmt['shape']);rule=contract['spectral_rule']
 if Path(record_path).stat().st_size!=fmt['bytes']:raise ValueError('Incomplete record; no zero fill')
 Y=np.memmap(record_path,dtype=fmt['dtype'],mode='r',shape=shape)
 if fmt['scale']!=[1,2**48] or shape!=(37,8191,62):raise ValueError('Unexpected frozen format')
 with np.load(proposal_path,allow_pickle=False) as z:
  if set(z.files)!={'theta','coeff'}:raise ValueError('Unexpected proposal metadata')
  theta=z['theta'];coeff=z['coeff']
 if theta.dtype!=np.int64 or theta.ndim!=1 or coeff.dtype!=np.int64 or coeff.shape!=(2*len(theta)+1,37*62):raise ValueError('Malformed proposal')
 if len(theta)>160 or np.any((coeff < -(2**60)) | (coeff > 2**60)):raise ValueError('HOLD: proposal resource/range limit')
 for j,nn in enumerate(theta):
  v=arb(int(nn))/(1<<60)
  if not(v>0 and v<arb.pi()) or(j>0 and nn<=theta[j-1]):raise ValueError('HOLD: phase bounds/duplicate')
 q=coeff.shape[0];P=np.zeros((8191,q),np.int64);P[:,0]=1<<60;phase_gate=arb(1)/(1<<60)
 for j,nn in enumerate(theta):
  phase=arb(int(nn))/(1<<60)
  for k in range(8191):
   z=acb(0,k*phase).exp();a,b=dyad(z.real),dyad(z.imag)
   if not(abs(z.real-arb(a)/(1<<60))<phase_gate and abs(z.imag-arb(b)/(1<<60))<phase_gate):raise ArithmeticError('HOLD: phase rounding not enclosed')
   P[k,2*j+1]=a;P[k,2*j+2]=b
 emit('phase_enclosures',temporal_dimension=q,phase_components_checked=2*len(theta)*8191)
 # All record readings checked exactly; no physical noise model or observer-generator assumption.
 cf=fm(coeff);weighted=0;energy=0;maxdiff=0
 for k in range(0,8191,128):
  block=arr(fm(P[k:k+128])*cf)
  raw=Y[:,k:k+len(block),:].transpose(1,2,0).reshape(len(block),2294)
  for local in range(len(block)):
   d=block[local]-raw[local].astype(object)*(1<<72);squared=sum(int(v)**2 for v in d);weight=min(k+local+1,8191-k-local,4096);weighted+=weight*squared
   energy+=weight*sum(int(v)**2 for v in raw[local]);maxdiff=max(maxdiff,max(abs(int(v)) for v in d))
  if k%2048==0:emit('record_residual_progress',time_index=k)
 rational_residual=F(weighted,4096**2*(1<<240));efit=arb(rational_residual.numerator).sqrt()/arb(rational_residual.denominator).sqrt()
 coefbound=sum(int(v) for v in np.max(np.abs(coeff[1:]),axis=1));phase_h_error=arb(37*62).sqrt()*arb(coefbound)/(1<<120)
 totalfit=efit+phase_h_error
 energyexact=F(energy,4096**2*(1<<96))
 residual={'exact_weighted_squared_error':[rational_residual.numerator,rational_residual.denominator],'dyadic_phase_fit_hankel_error_upper':up(efit),'phase_rounding_hankel_error_upper':up(phase_h_error),'record_fit_hankel_error_upper':up(totalfit),'max_scalar_dyadic_phase_residual':[maxdiff,1<<120],'energy_exact':[energyexact.numerator,energyexact.denominator],'record_shape':list(shape),'scalar_readings_checked':int(np.prod(shape)),'input_sha256':hashes}
 (O/'RECORD_RESIDUAL.json').write_text(json.dumps(residual,indent=2));emit('all_readings_checked',fit_error=str(totalfit.upper()),energy=str(arb(energyexact.numerator)/energyexact.denominator))
 # Exact preflight; only negative decisions bypass the unchanged spectral proof.
 preflight=residual_preflight(rational_residual,coefbound,F(*rule['selection_threshold']))
 preflight.update(input_sha256=hashes,scalar_readings_checked=int(np.prod(shape)))
 (O/'RESIDUAL_PREFLIGHT.json').write_text(json.dumps(preflight,indent=2))
 emit('residual_preflight',decision=preflight['status'])
 if preflight['status']=='EARLY_HOLD':
  certificate={'status':'HOLD','reason':'Exact proposal-residual lower bound exceeds frozen threshold; current residual-budget proof cannot pass',
   'spectral_bounds_computed':False,'stages_skipped':['modal_factors','factor_grams','cholesky','core_svd','svd_verification'],
   'physical_promotion':0,'target_count':rule['target_count'],'selection_threshold':rule['selection_threshold']}
 else:
  # An unsuccessful proposal is HOLD. No adjustment of the frozen target or gate occurs.
  try:certificate=verify(theta,coeff,totalfit,contract,O,emit)
  except (ArithmeticError,np.linalg.LinAlgError) as e:certificate={'status':'HOLD','reason':str(e),'physical_promotion':0}
 after={'record':sha(record_path),'contract':sha(contract_path),'proposal':sha(proposal_path)}
 if after!=hashes:raise RuntimeError('Inputs changed during certification')
 certificate.update(input_sha256=hashes,input_identity_stable=True,source_operator_or_nominal_modes_used=False,empirical_provenance_validated=False,apparatus_execution_claimed=False,independent_review='pending',lane='development — no registry entry',independent_blinded_execution_claimed=False)
 certificate['readable']={k:float(F(*certificate[k])) for k in ['sigma_r_lower','sigma_1_upper','sigma_r_plus1_upper','condition_upper'] if certificate.get(k) is not None}
 (O/'CERTIFICATE.json').write_text(json.dumps(certificate,indent=2))
 result={'status':certificate['status'],'wall_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'dense_hankel_allocated':False,'dense_hankel_bytes_avoided':307895468032,'source_operator_or_nominal_modes_used':False,'readable_bounds':certificate['readable'],'executed_code_sha256':{n:sha(Path(__file__).resolve().parent/n) for n in ['certify_record.py','proof_math.py','residual_preflight.py']}}
 (O/'BENCHMARK.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2),flush=True)
 return certificate
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('contract');p.add_argument('proposal');p.add_argument('output');a=p.parse_args();run(a.record,a.contract,a.proposal,a.output)
