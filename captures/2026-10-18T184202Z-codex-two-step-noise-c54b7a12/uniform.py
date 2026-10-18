"""Uniform order ball and conditional ideal top209 lag2 phase sufficient bound."""
import json
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq,ctx
from bindings import P,freeze
from proof_math import up,down
from numeric_math import encode,norm2_receipt
ctx.prec=512
a=lambda p:arb(fmpq(*p))
def run():
 f=freeze();base=json.loads((P/'inputs/BASE_ORDER_CERTIFICATE.json').read_text());phase=json.loads((P/'inputs/BASE_PHASE_CERTIFICATE.json').read_text());mtr=phase['metrics'];s0=a(base['qth_sigma_lower']);eps=a(base['qplus1_sigma_upper']);cut=a(f['source_precision_cutoff']);C=(arb(37*8191)*arb(738137)/4096).sqrt();margin=min(s0-cut,cut-eps);delta=margin/C
 eta=a(mtr['basis_orthogonality_upper']);span=a(mtr['source_frame_span_residual_upper']);rho=a(mtr['source_inverse_residual_upper']);h=a(mtr['source_inverse_norm_upper'])/(1-rho);d=a(mtr['source_reduction_norm_upper']);m=(1-eta).sqrt()/h-span;M=(1+eta).sqrt()*d+span;assert m>0
 with np.load(P/'inputs/BASE_LAST_ROWS.npz',allow_pickle=False) as z:last=z['basis_last_two']
 nums,bits=encode(last);lastnorm,_=norm2_receipt(nums,bits);betaU=(1-lastnorm*lastnorm/(1-eta)).sqrt();t0=span/m;dist0=(2-2*(1-t0*t0).sqrt()).sqrt();beta=betaU-dist0;assert beta>0;K=M/m;sep=a(mtr['minimum_target_chord_lower']);alpha=s0-eps
 rows=[]
 for k in [None,*f['uniform_exponents']]:
  raw=arb(0) if k is None else arb(1)/(1<<k);e=eps+C*raw;order=bool(C*raw<margin);r={'delta':[0,1] if k is None else [1,1<<k],'order209_guaranteed':order,'phase_status':'HOLD_UNIFORM_IDEAL_PHASE_BOUND'}
  if alpha>2*e:
   t=e/(alpha-e);dist=(2-2*(1-t*t).sqrt()).sqrt()
   if beta>dist:
    R=2*K*t/((beta-dist)*(1-t*t).sqrt());r['ideal_eigenvalue_radius_upper']=up(R)
    if R<1:r['ideal_two_step_phase_error_upper']=up(R.asin());r['phase_status']='CERTIFIED_CONDITIONAL_IDEAL_PHASE_MATCHING' if 2*R<sep and 2*R.asin()<sep else 'HOLD_UNIFORM_IDEAL_PHASE_BOUND'
  rows.append(r)
 result={'status':'UNIFORM_ORDER_AND_IDEAL_PHASE_SUFFICIENT_BOUNDS','physical_promotion':0,'uniform_vector_order_radius_lower':down(delta),'uniform_vector_order_radius_upper':up(delta),'noise_multiplier_upper':up(C),'parent_source_frame_sigma_lower':down(m),'parent_source_frame_norm_upper':up(M),'deleted_two_rows_beta_lower':down(beta),'parent_source_frame_condition_upper':up(K),'rows':rows,'readable':{'uniform_order_radius_lower':float(delta.lower()),'noise_multiplier_upper':float(C.upper()),'source_frame_sigma_lower':float(m.lower()),'deleted_rows_beta_lower':float(beta.lower())},'uniform_actual_floating_convergence_claimed':False,'uniform_phase_HOLD_is_not_failure_proof':True}
 dest=P/'UNIFORM_CERTIFICATE.json';dest.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':run()
