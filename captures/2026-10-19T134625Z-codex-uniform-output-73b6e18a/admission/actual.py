"""Check frozen universal output gates on actual, hash-bound PR208 saved factors."""
import json,sys,hashlib
from pathlib import Path
import numpy as np
from flint import arb,fmpq,ctx,fmpz_mat
from uniform import P,sha,a,up
ctx.prec=512
# Reuse published exact arithmetic helpers; bytes bound by freeze before admission.
Q=P.parent/'record-contract-work';sys.path.insert(0,str(Q))
from numeric_math import encode,encode_complex,complex_residual,cmul,diffnorm
from proof_math import fm,arr
from operator_bounds import gram_norm

def op(r,i,b):
 R,I=fm(r),fm(i);g=arr(R.transpose()*R+I.transpose()*I);h=arr(R.transpose()*I-I.transpose()*R)
 tr=sum(int(g[j,j]) for j in range(g.shape[0]));row=max(sum(abs(int(g[j,k]))+abs(int(h[j,k])) for k in range(g.shape[0])) for j in range(g.shape[0]))
 return arb(min(tr,row)).sqrt()/(1<<b)
def verify():
 f=json.loads((P/'FREEZE.json').read_text());g=f['gates']
 for n,h in f['code_sha256'].items():assert sha(P/n)==h
 for n,h in f['helper_sha256'].items():assert sha(Q/n)==h
 root=P.parent/'rounding-replay-work';inp=Q/'inputs/cyclic_unit/FLOAT_META.npz';assert sha(inp)==f['phase_witness_sha256']
 with np.load(inp,allow_pickle=False) as z:V=z['eigenvectors'];H=z['inverse']
 rows=[];bindings={}
 for mode in ['legacy_gemm','integer_projection']:
  d=root/'results'/mode
  for p in sorted(d.glob('*.npz')):
   rel=str(p.relative_to(root));assert sha(p)==f['actual_arrays_sha256'][rel];bindings[rel]=sha(p)
  cert=json.loads((d/'CERTIFICATE.json').read_text());assert sha(d/'CERTIFICATE.json')==f['actual_certificates_sha256'][mode]
  assert cert['status']=='CERTIFIED_ACTUAL_SVD_ORDER' and cert['learned_order']==209
  U=np.vstack([np.load(d/f'FACTOR_{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209]
  with np.load(d/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift'];ev=z['eigenvalues'];angles=z['angles']
  with np.load(d/'PHASE_PROPOSAL.npz',allow_pickle=False) as z:em=z['two_step_phase']
  # Reuse the same metrics only after exact equality of every relevant returned array.
  if rows:
   for x,y in zip((U,T,ev,angles,em),saved):assert np.array_equal(x,y)
   r=dict(rows[0]);r['mode']=mode;r['exact_input_identity_to']='legacy_gemm';rows.append(r);continue
  saved=tuple(x.copy() for x in (U,T,ev,angles,em))
  un,bu=encode(U);tn,bt=encode(T);shift,_=diffnorm(fm(un[2:]),bu,fm(un[:-2])*fm(tn),bu+bt)
  vr,vi,bv=encode_complex(V);ir,ii,bi=encode_complex(H);lr,li,bl=encode_complex(ev);vf=(fm(vr),fm(vi));ident=(fm(np.eye(209,dtype=object)),fm(np.zeros((209,209),dtype=object)))
  rho,_=complex_residual(cmul(*vf,fm(ir),fm(ii)),bv+bi,ident,0);hinv=op(ir,ii,bi)
  eig,_=complex_residual((fm(tn)*vf[0],fm(tn)*vf[1]),bt+bv,(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:])),bv+bl)
  from flint import acb
  argnum=0
  for j in range(209):
   n,den=float(angles[j]).as_integer_ratio();z,r=divmod(n*(1<<60),den);assert int(em[j])==z+int(2*r>den or(2*r==den and z%2))
   v=acb(arb(int(lr[j]))/(1<<bl),arb(int(li[j]))/(1<<bl));err=v.arg()-arb(int(em[j]))/(1<<60)
   argnum=max(argnum,min(up(abs(err))[0],up(abs(err+2*arb.pi()))[0],up(abs(err-2*arb.pi()))[0]))
  arge=arb(argnum)/(1<<180)
  metrics={'full_left_orthogonality':a(cert['eta_left_upper']),'full_right_orthogonality':a(cert['eta_right_upper']),'full_SVD_error':a(cert['singular_error_upper']),'raw_shift_residual':shift,'inverse_residual':rho,'proposed_inverse_norm':hinv,'eigenpair_residual':eig,'emitted_argument_error':arge}
  gates={n:bool(v<=a(g[n])) for n,v in metrics.items()}
  r={'mode':mode,'status':'ADMITTED_UNIFORM_RETURNED_OUTPUT_GATES' if all(gates.values()) else 'HOLD_OUTPUT_GATES','gates':gates,'metrics':{n:up(v) for n,v in metrics.items()},'readable':{n:float(v.upper()) for n,v in metrics.items()}};rows.append(r)
 result={'status':'ACTUAL_GATE_EVALUATION','rows':rows,'bindings':bindings,'physical_promotion':0,'new_estimator_runs':0,'new_SVD_runs':0,'external_review':'PENDING','full_SVD_certificate_recomputation':'separate parent replay required; hashes bind cached exact certificate here'}
 (P/'ACTUAL_ADMISSION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True);return result
if __name__=='__main__':verify()
