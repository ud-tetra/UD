"""Record-wise actual-output contract, with no exact-LS or floating-convergence assumption."""
import json,argparse
import numpy as np
from flint import arb,acb,fmpq,ctx
from bindings import P,sha,freeze,entry,basis
from numeric_math import encode,encode_complex,complex_residual,cmul,diffnorm
from operator_bounds import gram_norm
from proof_math import fm,arr,norm_exact,up,down
from reference import model_frame
ctx.prec=512
a=lambda x:arb(fmpq(*x))
def upper(x):return up(arb(x.upper()))
def poldist(x):return x/(1+(1-x).sqrt())
def complex_op(r,i,b):
 R,I=fm(r),fm(i);g=arr(R.transpose()*R+I.transpose()*I);h=arr(R.transpose()*I-I.transpose()*R);trace=sum(int(g[j,j]) for j in range(g.shape[0]));row=max(sum(abs(int(g[j,k]))+abs(int(h[j,k])) for k in range(g.shape[0])) for j in range(g.shape[0]));return arb(min(trace,row)).sqrt()/(1<<b)
def fit_squared(C,G,K,bn2,bu):
 c,bc=encode(C);gc=arr(fm(G)*fm(c));L=max(110,2*bu+2*bc,bu+55+bc);num=(bn2<<(L-110))+(sum(int(x)*int(y) for x,y in zip(c.flat,gc.flat))<<(L-2*bu-2*bc))-(2*sum(int(x)*int(y) for x,y in zip(c.flat,K.flat))<<(L-bu-55-bc));assert num>=0,'REJECT: inconsistent fit Gram';return [num,1<<L]
def run(n,replay=False):
 f=freeze();e=entry(n);o=P/'results'/n;raw=json.loads((o/'RAW_ELIGIBILITY.json').read_text());assert raw['record_sha256']==e['record_sha256'];result={'case':n,'physical_promotion':0,'independent_review':'pending','uniform_floating_convergence_claimed':False,'replay':replay}
 if raw['status']!='RAW_BALL_ELIGIBLE':
  result.update(status='HOLD_RAW_NOISE_BALL',phase_status='NOT_EVALUATED_BY_THIS_CONTRACT',previous_phase_status=json.loads((P/'inputs'/n/'CERTIFICATE.json').read_text())['status'],not_a_phase_failure_claim=True)
 else:
  U=basis(n);U0=basis('baseline');un,bu=encode(U);u0,b0=encode(U0);q=209;inp=P/'inputs'/n;report=json.loads((inp/'REPORT.json').read_text());disc=json.loads((inp/'DISCOVERY.json').read_text());assert report['record_sha256']==e['record_sha256'] and sha(inp/'PHASE_PROPOSAL.npz')==report['proposal_sha256'] and disc['learned_order_float']==q
  parent=json.loads((P/'inputs/PARENT_PHASE_CERTIFICATE.json').read_text());mt=parent['metrics'];ref=json.loads((P/'inputs/PARENT_UNIFORM_CERTIFICATE.json').read_text());assert next(x for x in ref['rows'] if x['delta']==[1,1<<48])['phase_status']=='CERTIFIED_UNIFORM_IDEAL_TWO_STEP_PHASE_MATCHING'
  for name in ['BASIS_A.npz','BASIS_B.npz','FLOAT_META.npz']:assert sha(P/'inputs/baseline'/name)==parent['array_hashes'][name]
  assert sha(P/'inputs/PARENT_SOURCE_WITNESS.npz')==parent['array_hashes']['SOURCE_WITNESS.npz']
  with np.load(o/'EXACT_GRAMS.npz',allow_pickle=False) as z:G,H,K=[np.array([[int(v) for v in row] for row in z[k]],object) for k in ['basis','reference_cross','sketch_cross']]
  assert np.array_equal(arr(fm(un).transpose()*fm(un)),G) and np.array_equal(arr(fm(un).transpose()*fm(u0)),H),'REJECT: actual basis/cross-Gram mismatch'
  with np.load(o/'PROPOSALS.npz',allow_pickle=False) as z:C=z['coefficient'];O=z['alignment']
  receipt=json.loads((o/'PROJECTION.json').read_text());assert receipt['record_sha256']==e['record_sha256'] and receipt['basis_bits']==bu and receipt['reference_basis_bits']==b0;bn2=int(receipt['sketch_norm_squared_integer']);fit2=fit_squared(C,G,K,bn2,bu);fit=a(fit2).sqrt();fitgate=a(ref['baseline_low_rank_residual_upper'])+a(ref['per_vector_noise_multiplier_upper'])/(1<<48)
  eta=norm_exact(G-np.eye(q,dtype=object)*(1<<(2*bu)),2*bu);on,bo=encode(O);og=fm(on).transpose()*fm(on);etaO=norm_exact(arr(og)-np.eye(q,dtype=object)*(1<<(2*bo)),2*bo);eta0=a(mt['basis_orthogonality_upper']);assert eta<1 and etaO<1 and eta0<1
  G0=arr(fm(u0).transpose()*fm(u0));go=arr(fm(G)*fm(on));L=max(2*bo+2*bu,2*b0,bo+bu+b0);num=(sum(int(x)*int(y) for x,y in zip(on.flat,go.flat))<<(L-2*bo-2*bu))+(sum(int(G0[i,i]) for i in range(q))<<(L-2*b0))-(2*sum(int(x)*int(y) for x,y in zip(on.flat,H.flat))<<(L-bo-bu-b0));assert num>=0;align=arb(num).sqrt()/(arb(2)**(arb(L)/2));distance=align+(1+eta).sqrt()*poldist(etaO)+poldist(eta)+poldist(eta0)
  beta=(1-norm_exact(u0[-2:],b0)**2/(1-eta0)).sqrt();sigma0=a(mt['two_step_shift_residual_upper'])/(1-eta0).sqrt();M0=(1+sigma0)/beta
  with np.load(inp/'FLOAT_META.npz',allow_pickle=False) as z:w={k:z[k] for k in z.files}
  with np.load(inp/'PHASE_PROPOSAL.npz',allow_pickle=False) as z:emitted=z['two_step_phase']
  tn,bt=encode(w['shift']);shift,_=diffnorm(fm(un[2:]),bu,fm(un[:-2])*fm(tn),bu+bt);sigmaa=shift/(1-eta).sqrt();vr,vi,bv=encode_complex(w['eigenvectors']);ir,ii,bi=encode_complex(w['inverse']);lr,li,bl=encode_complex(w['eigenvalues']);vf=(fm(vr),fm(vi));identity=(fm(np.eye(q,dtype=object)),fm(np.zeros((q,q),dtype=object)));rho,_=complex_residual(cmul(*vf,fm(ir),fm(ii)),bv+bi,identity,0);hv=complex_op(ir,ii,bi);eig,_=complex_residual((fm(tn)*vf[0],fm(tn)*vf[1]),bt+bv,(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:])),bv+bl)
  argnum=0
  for i in range(q):
   num0,den=float(w['angles'][i]).as_integer_ratio();v,r=divmod(num0*(1<<60),den);assert int(emitted[i])==v+int(2*r>den or(2*r==den and v%2)),'REJECT: emitted phase mismatch';z=acb(arb(int(lr[i]))/(1<<bl),arb(int(li[i]))/(1<<bl));d=z.arg()-arb(int(emitted[i]))/(1<<60);argnum=max(argnum,min(upper(abs(d))[0],upper(abs(d+2*arb.pi()))[0],upper(abs(d-2*arb.pi()))[0]))
  argerr=arb(argnum)/(1<<100);metrics={'actual_sketch_fit_residual_upper':upper(fit),'fit_envelope_upper':upper(fitgate),'basis_orthogonality_upper':upper(eta),'alignment_orthogonality_upper':upper(etaO),'aligned_basis_distance_upper':upper(distance),'deleted_row_margin_lower':down(beta-distance),'actual_shift_residual_upper':upper(sigmaa),'eigenvector_inverse_residual_upper':upper(rho),'eigenvector_inverse_norm_upper':upper(hv),'actual_eigenpair_residual_upper':upper(eig),'argument_error_upper':upper(argerr)}
  result.update(metrics=metrics,raw_status=raw['status'],actual_sketch_fit_squared=fit2,status='HOLD_RECORD_WISE_PHASE_CONTRACT')
  try:
   assert fit<=fitgate,'HOLD: exact sketch approximation quality';assert beta>distance,'HOLD: deleted-row rank';assert rho<1,'HOLD: eigenvector inverse'
   delta=eig*hv/(1-rho);b=(sigma0+sigmaa+distance*(1+M0))/(beta-distance);hD=a(mt['source_inverse_norm_upper'])/(1-a(mt['source_inverse_residual_upper']));k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+eta)/(1-eta)).sqrt();R=hD*a(mt['intertwining_residual_upper'])+k0*hD*a(mt['source_reduction_norm_upper'])*(b+ka*delta);assert R<1,'HOLD: eigenvalue disk crosses origin';angle=R.asin()+argerr;sep=a(mt['minimum_target_chord_lower']);result.update(eigenvalue_radius_upper=upper(R),actual_two_step_phase_error_upper=upper(angle),readable={'aligned_basis_distance_upper':float(distance.upper()),'actual_sketch_fit_residual_upper':float(fit.upper()),'fit_envelope_upper':float(fitgate.upper()),'phase_error_upper':float(angle.upper())});assert 2*R<sep and 2*angle<sep,'HOLD: target separation'
   _,_,targets,points,_=model_frame(e);used=set();matches=[]
   for t,pt in zip(targets,points):
    candidates=[k for k in range(q) if abs(acb(arb(int(lr[k]))/(1<<bl),arb(int(li[k]))/(1<<bl))-pt)<R];assert len(candidates)==1 and candidates[0] not in used,'HOLD: explicit target matching';used.add(candidates[0]);matches.append({'label':t['label'],'emitted_index':candidates[0]})
   result.update(status='CERTIFIED_RECORD_WISE_FLOATING_PHASE_CONTRACT',unique_target_matching=True,target_matches=matches,original_phase_ambiguity_modulo_pi=True)
  except AssertionError as ex:result['reason']=str(ex)
  zero_fit=a(fit_squared(np.zeros_like(C),G,K,bn2,bu)).sqrt();assert zero_fit>fitgate;zero_rho,_=complex_residual(cmul(*vf,fm(np.zeros_like(ir)),fm(np.zeros_like(ii))),bv+bi,identity,0);assert zero_rho>=1;result['negative_controls']={'zero_coefficient':'HOLD_SKETCH_APPROXIMATION_QUALITY','zero_eigenvector_inverse':'HOLD_EIGENVECTOR_INVERSE','zero_inverse_residual_lower':down(zero_rho),'zero_coefficient_fit_lower':down(zero_fit)}
 result['input_record_sha256']=e['record_sha256'];dest=o/('REPLAY_CERTIFICATE.json' if replay else 'CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k in ['case','status','reason','readable','previous_phase_status']}),flush=True);return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');x=p.parse_args()
 for e in freeze()['cases']:run(e['case'],x.replay)
