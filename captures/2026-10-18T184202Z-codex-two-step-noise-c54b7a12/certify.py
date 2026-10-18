"""Actual two-step floating-output similarity certificate, exact residual arithmetic."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time
import numpy as np
from flint import ctx,arb,acb
from bindings import P,sha,witness
from reference import model_frame
from proof_math import fm,arr,up,down
from numeric_math import encode,encode_complex,diffnorm,complex_residual,cmul,norm2_receipt
from operator_bounds import gram_norm
ctx.prec=512

def real_op(a,b):return gram_norm(a,b)[0]
def complex_op(r,i,b):
 R,I=fm(r),fm(i);gr=arr(R.transpose()*R+I.transpose()*I);gi=arr(R.transpose()*I-I.transpose()*R);trace=sum(int(gr[j,j]) for j in range(gr.shape[0]));row=max(sum(abs(int(gr[j,k]))+abs(int(gi[j,k])) for k in range(gr.shape[0])) for j in range(gr.shape[0]));return arb(min(trace,row)).sqrt()/(1<<b)

def run(n,replay=False):
 start=time.monotonic();e,o=witness(n);order=json.loads((o/'ORDER_CERTIFICATE.json').read_text());q=1+104*len(e['classes']);hashes={p.name:sha(p) for p in o.glob('*.npz')}
 with np.load(o/'BASIS_A.npz',allow_pickle=False) as z:ua=z['basis']
 with np.load(o/'BASIS_B.npz',allow_pickle=False) as z:ub=z['basis']
 U=np.r_[ua,ub]
 with np.load(o/'FLOAT_META.npz',allow_pickle=False) as z:w={k:z[k] for k in z.files}
 with np.load(o/'SOURCE_WITNESS.npz',allow_pickle=False) as z:D=z['reduction'];K=z['inverse']
 with np.load(o/'PHASE_PROPOSAL.npz',allow_pickle=False) as z:emitted=z['two_step_phase']
 assert U.shape==(8191,q) and w['shift'].shape==(q,q) and D.shape==(q,q) and emitted.shape==(q,)
 pp,J,targets,points,sep=model_frame(e);un,bu=encode(U);tn,bt=encode(w['shift']);dn,bd=encode(D);kn,bk=encode(K)
 eta,_=diffnorm(fm(un).transpose()*fm(un),2*bu,fm(np.eye(q,dtype=object)),0);shift,_=diffnorm(fm(un[2:]),bu,fm(un[:-2])*fm(tn),bu+bt)
 rhoD,_=diffnorm(fm(dn)*fm(kn),bd+bk,fm(np.eye(q,dtype=object)),0);h=real_op(kn,bk);d=real_op(dn,bd)
 lj,_=diffnorm(fm(tn)*fm(dn),bt+bd,fm(dn)*fm(J),bd+60);lj+=d*arb(1)/(1<<59)
 bits=max(60,bu+bd);spanN=arr(fm(pp)*(1<<(bits-60))-fm(un)*fm(dn)*(1<<(bits-bu-bd)));span=real_op(spanN,bits)+arb(8191*(q-1)).sqrt()/(1<<60)
 vr,vi,bv=encode_complex(w['eigenvectors']);ir,ii,bi=encode_complex(w['inverse']);lr,li,bl=encode_complex(w['eigenvalues']);vf=(fm(vr),fm(vi));hf=(fm(ir),fm(ii));identity=(fm(np.eye(q,dtype=object)),fm(np.zeros((q,q),dtype=object)))
 rhoV,_=complex_residual(cmul(*vf,*hf),bv+bi,identity,0);hv=complex_op(ir,ii,bi)
 eigen,_=complex_residual((fm(tn)*vf[0],fm(tn)*vf[1]),bt+bv,(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:])),bv+bl)
 argnum=0
 for idx in range(q):
  num,den=float(w['angles'][idx]).as_integer_ratio();quo,rem=divmod(num*(1<<60),den);assert int(emitted[idx])==quo+int(2*rem>den or(2*rem==den and quo%2))
  z=acb(arb(int(lr[idx]))/(1<<bl),arb(int(li[idx]))/(1<<bl));diff=z.arg()-arb(int(emitted[idx]))/(1<<60);errnum=min(up(abs(diff))[0],up(abs(diff+2*arb.pi()))[0],up(abs(diff-2*arb.pi()))[0]);argnum=max(argnum,errnum)
 argerr=arb(argnum)/(1<<100)
 metrics={'basis_orthogonality_upper':up(eta),'two_step_shift_residual_upper':up(shift),'source_frame_span_residual_upper':up(span),'source_inverse_residual_upper':up(rhoD),'source_inverse_norm_upper':up(h),'source_reduction_norm_upper':up(d),'intertwining_residual_upper':up(lj),'eigenvector_inverse_residual_upper':up(rhoV),'eigenvector_inverse_norm_upper':up(hv),'actual_eigenpair_residual_upper':up(eigen),'argument_emission_error_upper':up(argerr),'minimum_target_chord_lower':down(sep)}
 result={'status':'HOLD_TWO_STEP_MATCHING','case':n,'source_order':q,'metrics':metrics,'physical_promotion':0,'independent_review':'pending','target':'Pinned learned model two-step circular phases, not SI frequencies','original_204_205_cutoff_HOLD_unchanged':True,'replay':replay}
 try:
  assert order['status']=='CERTIFIED_SOURCE_PRECISION_ORDER' and order['exact_encoded_count_above_source_cutoff']==q,'HOLD: source precision excitation'
  assert eta<1 and rhoD<1 and rhoV<1,'HOLD: inverse or basis rank'
  invD=h/(1-rhoD);backward=eigen*hv/(1-rhoV);radius=invD*(lj+d*backward);assert radius<1,'HOLD: eigenvalue disk crosses origin';angle=radius.asin()+argerr
  result.update(eigenvalue_radius_upper=up(radius),two_step_phase_error_radians_upper=up(angle),conditional_source_lift_error_radians_upper=up(angle/2),readable={'eigenvalue_radius_upper':float(radius.upper()),'two_step_phase_error_radians_upper':float(angle.upper()),'minimum_target_chord_lower':float(sep.lower())})
  assert 2*radius<sep and 2*angle<sep,'HOLD: two-step target separation'
  matches=[];used=set()
  for i,point in enumerate(points):
   candidates=[k for k in range(q) if abs(acb(arb(int(lr[k]))/(1<<bl),arb(int(li[k]))/(1<<bl))-point)<radius]
   assert len(candidates)==1 and candidates[0] not in used,'HOLD: explicit target labeling';idx=candidates[0];used.add(idx);matches.append({**targets[i],'emitted_index':idx})
  result.update(status='CERTIFIED_ACTUAL_TWO_STEP_PHASE_MATCHING',unique_target_matching=True,target_matches=matches,source_lift_is_conditional_modulo_pi=True)
 except AssertionError as ex:result['reason']=str(ex)
 result.update(array_hashes=hashes,record_sha256=e['record_sha256'],source_precision_order_certificate_sha256=sha(o/'ORDER_CERTIFICATE.json'),seconds=time.monotonic()-start)
 assert all(sha(o/name)==h for name,h in hashes.items());dest=o/('REPLAY_CERTIFICATE.json' if replay else 'CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({'case':n,'status':result['status'],'reason':result.get('reason'),'readable':result.get('readable')},indent=2),flush=True);return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.case,a.replay)
