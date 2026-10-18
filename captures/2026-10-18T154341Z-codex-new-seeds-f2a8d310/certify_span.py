"""Actual-floating output verification for frozen new constructor records."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time,resource
import numpy as np
from flint import ctx,arb,acb
from proof_math import fm,arr,up
from numeric_math import encode,encode_complex,norm2_receipt,diffnorm,cmul,complex_residual
from frame_math import span_residual,assemble_span
from frame_values import values,constants as frame_constants
from bindings import P,sha,load_case
ctx.prec=512

def run(case,replay=False):
 start=time.monotonic();_,entry,out,parent=load_case(case)
 with np.load(out/'FLOAT_WITNESS.npz',allow_pickle=False) as z:w={n:z[n] for n in z.files}
 assert set(w)=={'basis','shift','eigenvalues','eigenvectors','inverse','reduction','angles'}
 assert w['basis'].shape==(8191,105) and w['shift'].shape==(105,105)
 with np.load(out/'PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta']
 assert theta.shape==(52,)
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:
  pp=values(z['theta']);recomputed=frame_constants(z['theta'])
 reduction=out/'FRAME_REDUCTION.npz';reduction_hash=sha(reduction)
 with np.load(reduction,allow_pickle=False) as z:D=z['reduction']
 assert D.shape==(105,105)
 span,span_receipt=span_residual(pp,w['basis'],D)
 un,bu=encode(w['basis']);tn,bt=encode(w['shift']);uf=fm(un);tf=fm(tn)
 eta,eta2=diffnorm(uf.transpose()*uf,2*bu,fm(np.eye(105,dtype=object)),0)
 shift,shift2=diffnorm(fm(un[1:]),bu,fm(un[:-1])*tf,bu+bt)
 vr,vi,bv=encode_complex(w['eigenvectors']);ir,ii,bi=encode_complex(w['inverse']);lr,li,bl=encode_complex(w['eigenvalues'])
 vf=(fm(vr),fm(vi));iv=(fm(ir),fm(ii));identity=(fm(np.eye(105,dtype=object)),fm(np.zeros((105,105),dtype=object)))
 inverse,inverse2=complex_residual(cmul(*vf,*iv),bv+bi,identity,0)
 invnorm,invnorm2=norm2_receipt(np.r_[ir.flat[:],ii.flat[:]],bi)
 left=(tf*vf[0],tf*vf[1]);right=(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:]))
 eigen,eigen2=complex_residual(left,bt+bv,right,bv+bl)
 angles=w['angles'];assert angles.shape==(105,)
 positive=np.where(angles>1e-10)[0];positive=positive[np.argsort(angles[positive])]
 assert len(positive)==52 and np.count_nonzero(angles<-1e-10)==52 and np.count_nonzero(abs(angles)<=1e-10)==1
 errors=[]
 for j,index in enumerate(positive):
  # Verify exact ties-to-even grid rounding of the captured angle bit pattern.
  n,d=float(angles[index]).as_integer_ratio();q,r=divmod(n*(1<<60),d);expected=q+int(2*r>d or (2*r==d and q%2))
  assert int(theta[j])==expected,'HOLD: emitted phase is not captured rounding result'
  z=acb(arb(int(lr[index]))/(1<<bl),arb(int(li[index]))/(1<<bl));arg=z.arg();assert arg>0 and arg<arb.pi()
  errors.append(up(abs(arg-arb(int(theta[j]))/(1<<60))))
 argerror=[max(x[0] for x in errors),1<<100]
 constants=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants']
 assert all(constants[k]==v for k,v in recomputed.items()),'HOLD: inherited frame constants do not replay'
 metrics={'basis_orthogonality_upper':up(eta),'frame_span_residual_upper':up(span),'shift_residual_upper':up(shift),'inverse_residual_upper':up(inverse),'inverse_norm_upper':up(invnorm),'eigenpair_residual_upper':up(eigen),'argument_output_error_upper':argerror}
 try:result=assemble_span(metrics,constants)
 except AssertionError as exc:result={'status':'HOLD','reason':str(exc),'unique_reference_phase_matching':False,'physical_promotion':0}
 result.update(case=case,record_sha256=entry['record_sha256'],witness_sha256=entry['witness_sha256'],proposal_sha256=entry['proposal_sha256'],frame_reduction_sha256=reduction_hash,metrics=metrics,frame_span_receipt=span_receipt,exact_squared_norms={'basis_orthogonality':eta2,'shift':shift2,'inverse':inverse2,'inverse_norm':invnorm2,'eigenpair':eigen2},exact_binary_scale_bits={'basis':bu,'shift':bt,'eigenvectors':bv,'inverse':bi,'eigenvalues':bl},proposer_status=parent['status'],saved_actual_floating_outputs=True,originated_from_fresh_constructor_execution=True,estimator_executed_by_this_verifier=False,original_estimator_and_proposal_unchanged=True,fresh_raw_readings_rechecked_for_noise_gates=0,source_proposer_input_readings=18790154,replay=replay,independent_review='pending',nominal_operator_or_source_modes_used=False,fixed_fitted_reference_phases_used=True,frame_constants_recomputed=True,wall_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 assert sha(reduction)==reduction_hash
 _,after,_,_=load_case(case);assert after['witness_sha256']==entry['witness_sha256'] and after['proposal_sha256']==entry['proposal_sha256']
 dest=out/('REPLAY_CERTIFICATE.json' if replay else 'SPAN_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({'case':case,'status':result['status'],'readable':result.get('readable'),'reason':result.get('reason'),'seconds':result['wall_seconds']},indent=2),flush=True)
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.case,a.replay)
