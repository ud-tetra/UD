"""Exact retained-factor cutoff, measured-frame transport and emitted-list checks."""
import json
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,fmpq
from common import P,freeze,sha,a,up,down
from numeric_math import encode,encode_complex,complex_residual,cmul
from proof_math import fm,arr,norm_exact

def cutoff_predicate(q,epsilon,sq,threshold):
 return bool(q==209 and epsilon<threshold and sq-epsilon>threshold)
def cutoff(N,U,s,vt,q):
 if not(q==209 and U.shape==(8191,q) and s.shape==(321,) and vt.shape==(321,321)):
  return dict(status='HOLD_CUTOFF_DIMENSION',learned_order=q)
 assert np.all(s>=0) and np.all(s[:-1]>=s[1:]) and q==int(np.count_nonzero(s>2.**-24))
 un,bu=encode(U);sn,bs=encode(s[:q]);vn,bv=encode(vt[:q]);cn=sn[:,None]*vn;bc=bs+bv;uf=fm(un);cf=fm(cn);G=uf.transpose()*uf;H=uf.transpose()*fm(N.astype(object));vf=fm(vn)
 etaU=norm_exact(arr(G)-np.eye(q,dtype=object)*(1<<(2*bu)),2*bu);etaV=norm_exact(arr(vf*vf.transpose())-np.eye(q,dtype=object)*(1<<(2*bv)),2*bv)
 if not(etaU<1 and etaV<1):return dict(status='HOLD_CUTOFF_GRAM',learned_order=q)
 bz=55;L=max(2*bz,2*bu+2*bc,bu+bz+bc);normz=sum(int(x)**2 for x in N.flat);gc=arr(G*cf);h=arr(H);quadratic=sum(int(x)*int(y) for x,y in zip(cn.flat,gc.flat));cross=sum(int(x)*int(y) for x,y in zip(cn.flat,h.flat));numer=(normz<<(L-2*bz))+(quadratic<<(L-2*bu-2*bc))-2*(cross<<(L-bu-bz-bc));assert numer>=0;fraction=F(numer,1<<L);r=a([fraction.numerator,fraction.denominator]).sqrt();p=lambda e:e/(1+(1-e).sqrt());epsilon=r+arb(float(s[0]))*(p(etaU)*(1+etaV).sqrt()+p(etaV));cut=arb(1)/(1<<24);sq=arb(float(s[q-1]));passed=cutoff_predicate(q,epsilon,sq,cut)
 return dict(status='CERTIFIED_EXACT_SKETCH_CUTOFF_209' if passed else 'HOLD_EXACT_SKETCH_CUTOFF',learned_order=q,cutoff=[1,1<<24],retained_left_Gram_F_upper=up(etaU),retained_right_Gram_F_upper=up(etaV),exact_truncated_residual_squared=[str(fraction.numerator),str(fraction.denominator)],truncated_residual_F_upper=up(r),rankq_operator_error_upper=up(epsilon),sigma209_lower=down(sq-epsilon),sigma210_upper=up(epsilon),readable=dict(rankq_operator_error_upper=float(epsilon.upper()),sigma209_lower=float((sq-epsilon).lower()),sigma210_upper=float(epsilon.upper())),scope='Exactly209 singular values of the exact projected sketch exceed2^-24. Retained rankq polar approximation, not full321-factor SVD accuracy or native1893 Hankel rank.')

def op(r,i,b):
 R,I=fm(r),fm(i);g=arr(R.transpose()*R+I.transpose()*I);h=arr(R.transpose()*I-I.transpose()*R);tr=sum(int(g[j,j]) for j in range(g.shape[0]));row=max(sum(abs(int(g[j,k]))+abs(int(h[j,k])) for k in range(g.shape[0])) for j in range(g.shape[0]));return arb(min(tr,row)).sqrt()/(1<<b)
def circular(v):
 return min((arb(abs(v+2*k*arb.pi()).upper()) for k in [-1,0,1]),key=lambda x:float(x.upper()))
def match_emissions(em):
 source=json.loads((P/'inputs/SOURCE_PHASE.json').read_text());targets=source['target_matches'];sep=a(source['metrics']['minimum_target_chord_lower']);assert len(targets)==len(em)==209;rows=[];target_angles=[]
 for target in targets:
  omega=a(target['omega']);assert abs(2*omega)<4*arb.pi();target_angles.append(acb(0,2*omega).exp().arg())
 for i,n in enumerate(em):
  theta=arb(int(n))/(1<<60);assert abs(theta)<arb.pi()+arb(1)/(1<<59)
  errors=[]
  for t in target_angles:
   v=theta-t;distances=[abs(v+2*k*arb.pi()) for k in [-1,0,1]];lo=min(z.lower() for z in distances);hi=min(z.upper() for z in distances);errors.append((arb(lo),arb(hi)))
  j=min(range(209),key=lambda k:float(errors[k][1]));err=errors[j][1];unique=all(err<errors[k][0] for k in range(209) if k!=j);ok=bool(unique and err<sep/2);rows.append(dict(emitted_index=i,target_index=j,target_label=targets[j]['label'],circular_error_upper=up(err),unique_and_within_fixed_radius=ok))
 bijective=len({r['target_index'] for r in rows})==209;passed=bijective and all(r['unique_and_within_fixed_radius'] for r in rows);maximum=a([max(r['circular_error_upper'][0] for r in rows),1<<180])
 return dict(status='CERTIFIED_OBSERVED_TWO_STEP_EMISSION_BIJECTION' if passed else 'HOLD_OBSERVED_EMISSION_MATCH',bijective=bijective,maximum_circular_error_upper=up(maximum),readable_maximum_circular_error_upper=float(maximum.upper()),source_chord_lower=source['metrics']['minimum_target_chord_lower'],rows=rows,scope='Finite emitted-list match to pinned learned-model TWO-STEP targets; not exact eigenvalues of returned T, SI frequency identification or removal of modulo-pi ambiguity.')

def phase(case,frame):
 with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift'];ev=z['eigenvalues'];angles=z['angles'];V=z['eigenvectors'];H=z['inverse']
 with np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False) as z:em=z['two_step_phase']
 assert T.shape==V.shape==H.shape==(209,209) and ev.shape==angles.shape==em.shape==(209,)
 tn,bt=encode(T);vr,vi,bv=encode_complex(V);ir,ii,bi=encode_complex(H);lr,li,bl=encode_complex(ev);vf=(fm(vr),fm(vi));ident=(fm(np.eye(209,dtype=object)),fm(np.zeros((209,209),dtype=object)));rho,rho2=complex_residual(cmul(*vf,fm(ir),fm(ii)),bv+bi,ident,0);hinv=op(ir,ii,bi);eigres,eig2=complex_residual((fm(tn)*vf[0],fm(tn)*vf[1]),bt+bv,(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:])),bv+bl)
 argnums=[];ties=True
 for j in range(209):
  n,de=float(angles[j]).as_integer_ratio();v,z=divmod(n*(1<<60),de);ties=ties and int(em[j])==v+int(2*z>de or(2*z==de and v%2));zz=acb(arb(int(lr[j]))/(1<<bl),arb(int(li[j]))/(1<<bl));argnums.append(up(circular(zz.arg()-arb(int(em[j]))/(1<<60)))[0])
 arg=a([max(argnums),1<<180])
 old=json.loads((P/'inputs/OLD_POLICY.json').read_text())['gates'];metrics=dict(inverse_residual=rho,proposed_inverse_norm=hinv,eigenpair_residual=eigres,emitted_argument_error=arg);gates={n:bool(v<=a(old[n])) for n,v in metrics.items()};gates['emission_ties_even_consistency']=bool(ties)
 observed=match_emissions(em);gates['observed_emission_bijection']=observed['status']=='CERTIFIED_OBSERVED_TWO_STEP_EMISSION_BIJECTION'
 transport=None
 if rho<1 and frame.get('direct_bound') is not None:
  u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());m=json.loads((P/'inputs/SOURCE_PHASE.json').read_text())['metrics'];eta=a(frame['retained_Gram_defect_F_upper']);d=a(frame['direct_bound']['distance']);beta=a(u['deleted_two_rows_beta_lower']);s=a(frame['actual_raw_shift_F_upper']);eta0=a(m['basis_orthogonality_upper']);hD=a(m['source_inverse_norm_upper'])/(1-a(m['source_inverse_residual_upper']));K=((1+eta0)/(1-eta0)).sqrt()*hD*a(m['source_reduction_norm_upper']);L=hD*a(m['intertwining_residual_upper']);delta=eigres*hinv/(1-rho)
  if eta<1 and d<beta:
   b=(a(u['comparison_shift_residual_upper'])+s/(1-eta).sqrt()+d*(1+a(u['comparison_shift_norm_upper'])))/(beta-d);R=L+K*(b+((1+eta)/(1-eta)).sqrt()*delta);sep=a(m['minimum_target_chord_lower']);angle=R.asin()+arg if R<1 else None;ok=bool(angle is not None and 2*R<sep and 2*angle<sep);transport=dict(status='CERTIFIED_MEASURED_FRAME_PHASE_TRANSPORT' if ok else 'HOLD_PHASE_TRANSPORT',radius_upper=up(R),phase_error_upper=None if angle is None else up(angle),readable_radius_upper=float(R.upper()),scope='Measured-frame comparison to pinned source similarity; no original-baseline raw-ball premise. Nearby diagonalizable correction VLambdaV^-1, not exact spectrum(T).')
 gates['measured_frame_transport']=bool(transport is not None and transport['status']=='CERTIFIED_MEASURED_FRAME_PHASE_TRANSPORT')
 return dict(status='CERTIFIED_SAVED_TWO_STEP_PHASE_OUTPUT' if all(gates.values()) else 'HOLD_SAVED_PHASE_OUTPUT',gates=gates,metrics={n:up(v) for n,v in metrics.items()},exact_inverse_residual_squared=[str(x) for x in rho2],exact_eigenpair_residual_squared=[str(x) for x in eig2],observed=observed,transport=transport,readable={n:float(v.upper()) for n,v in metrics.items()},old_full_factor_or_raw_ball_policy_admission_claimed=False,physical_promotion=0)

def verify_one(name,case,run,N,frame):
 for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h
 q=run['learned_order'];base=dict(case=name,record_sha256=run['record_sha256'],learned_order=q,physical_promotion=0)
 if run['execution_status']!='COMPLETED' or q!=209:return dict(**base,status='HOLD_EXECUTION_OR_ORDER',execution=run)
 U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
 with np.load(case/'SVD_META.npz',allow_pickle=False) as z:s=z['singular'];vt=z['right_transpose']
 cut=cutoff(N,U,s,vt,q);ph=phase(case,frame);passed=frame['status']=='CERTIFIED_FRESH_MEASURED_SOURCE_FRAME_SHIFT' and cut['status']=='CERTIFIED_EXACT_SKETCH_CUTOFF_209' and ph['status']=='CERTIFIED_SAVED_TWO_STEP_PHASE_OUTPUT'
 return dict(**base,status='CERTIFIED_CUTOFF_PHASE_AND_FIXED_FRAME' if passed else 'HOLD_COMBINED_FROZEN_CONTRACT',frame_status=frame['status'],cutoff=cut,phase=ph)
