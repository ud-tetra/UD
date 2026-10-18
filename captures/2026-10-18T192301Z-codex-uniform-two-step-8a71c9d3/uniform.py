"""Positive uniform IDEAL two-step phase tolerance about an encoded baseline."""
import json,argparse
import numpy as np
from flint import arb,fmpq,ctx
from bindings import P,freeze,sha
from proof_math import fm,arr,up,down,norm_exact
from numeric_math import encode
from sketch import sketch
ctx.prec=512
a=lambda x:arb(fmpq(*x))
def verify(replay=False,corrupt=False):
 f=freeze();parent=json.loads((P/'inputs/BASE_CERTIFICATE.json').read_text());order=json.loads((P/'inputs/BASE_ORDER_CERTIFICATE.json').read_text());mtr=parent['metrics'];out=P/'baseline';receipt=json.loads((out/'PROJECTION.json').read_text());assert receipt['record_sha256']==f['baseline_sha256']
 for n in ['BASIS_A.npz','BASIS_B.npz','FLOAT_META.npz','SOURCE_WITNESS.npz']:assert sha(P/'inputs'/('BASE_'+n))==parent['array_hashes'][n]
 with np.load(P/'inputs/BASE_BASIS_A.npz',allow_pickle=False) as z:ua=z['basis']
 with np.load(P/'inputs/BASE_BASIS_B.npz',allow_pickle=False) as z:ub=z['basis']
 U=np.r_[ua,ub];un,bu=encode(U);assert bu==receipt['basis_scale_bits']
 with np.load(out/'EXACT_GRAMS.npz',allow_pickle=False) as z:G=np.array([[int(x) for x in row] for row in z['basis_gram_decimal']],object);H=np.array([[int(x) for x in row] for row in z['cross_gram_decimal']],object);SG=z['sketch_gram']
 assert G.shape==(209,209) and H.shape==(209,321);assert np.array_equal(arr(fm(un).transpose()*fm(un)),G),'HOLD: actual basis Gram mismatch'
 A=sketch();assert np.array_equal(A.T@A,SG),'HOLD: sketch Gram mismatch';snorm=arb(max(sum(abs(int(v)) for v in row) for row in SG)).sqrt()/128;C=(arb(37*8191)).sqrt()*snorm
 with np.load(out/'COEFFICIENT_PROPOSAL.npz',allow_pickle=False) as z:coeff=z['coefficient']
 if corrupt:coeff=np.zeros_like(coeff)
 cn,bc=encode(coeff);gc=arr(fm(G)*fm(cn));L=max(110,2*bu+2*bc,bu+55+bc);rnum=(int(receipt['raw_sketch_norm_squared_integer'])<<(L-110))+(sum(int(x)*int(y) for x,y in zip(cn.flat,gc.flat))<<(L-2*bu-2*bc))-(2*sum(int(x)*int(y) for x,y in zip(cn.flat,H.flat))<<(L-bu-55-bc));assert rnum>=0,'HOLD: inconsistent cross-Gram residual'
 r=arb(rnum).sqrt()/(arb(2)**(arb(L)/2));eta=norm_exact(G-np.eye(209,dtype=object)*(1<<(2*bu)),2*bu);assert eta<1 and eta<=a(mtr['basis_orthogonality_upper']);last=norm_exact(un[-2:],bu);beta=(1-last*last/(1-eta)).sqrt();assert beta>0
 sigma=a(mtr['two_step_shift_residual_upper'])/(1-eta).sqrt();Mbar=(1+sigma)/beta;polar=((1+eta)/(1-eta)).sqrt();rho=a(mtr['source_inverse_residual_upper']);assert rho<1;hD=a(mtr['source_inverse_norm_upper'])/(1-rho);dD=a(mtr['source_reduction_norm_upper']);Lj=a(mtr['intertwining_residual_upper']);sep=a(mtr['minimum_target_chord_lower']);s0=a(order['qth_sigma_lower']);eps0=a(order['qplus1_sigma_upper']);cut=a(f['source_precision_cutoff']);alpha=s0-r;rows=[]
 for k in [None,*f['uniform_exponents']]:
  delta=arb(0) if k is None else arb(1)/(1<<k);e=r+C*delta;row={'delta':[0,1] if k is None else [1,1<<k],'order209_guaranteed':bool(C*delta<min(s0-cut,cut-eps0)),'phase_status':'HOLD_UNIFORM_IDEAL_PHASE_BOUND'}
  if alpha>2*e:
   t=e/(alpha-e);distance=(2-2*(1-t*t).sqrt()).sqrt()
   if beta>distance:
    b=(sigma+distance*(1+Mbar))/(beta-distance);R=hD*Lj+polar*hD*dD*b;row['ideal_eigenvalue_radius_upper']=up(R)
    if R<1:
     angle=R.asin();row['ideal_two_step_phase_error_upper']=up(angle)
     if row['order209_guaranteed'] and 2*R<sep and 2*angle<sep:row['phase_status']='CERTIFIED_UNIFORM_IDEAL_TWO_STEP_PHASE_MATCHING'
  rows.append(row)
 result={'status':'ENCODED_BASELINE_UNIFORM_IDEAL_PHASE_BOUNDS','physical_promotion':0,'independent_review':'pending','actual_floating_uniform_convergence_claimed':False,'source_comparison':'Pinned PR197209-target model; circular radians per TWO-STEP sample','baseline_exact_low_rank_residual_squared':[rnum,1<<L],'baseline_low_rank_residual_upper':up(r),'basis_orthogonality_upper':up(eta),'deleted_two_rows_beta_lower':down(beta),'sketch_operator_norm_upper':up(snorm),'per_vector_noise_multiplier_upper':up(C),'comparison_shift_residual_upper':up(sigma),'comparison_shift_norm_upper':up(Mbar),'minimum_target_chord_lower':mtr['minimum_target_chord_lower'],'rows':rows,'readable':{'baseline_low_rank_residual_upper':float(r.upper()),'noise_multiplier_upper':float(C.upper()),'beta_lower':float(beta.lower())},'Gram_sha256':sha(out/'EXACT_GRAMS.npz'),'coefficient_proposal_sha256':sha(out/'COEFFICIENT_PROPOSAL.npz'),'replay':replay}
 if corrupt:return result
 dest=P/('UNIFORM_REPLAY.json' if replay else 'UNIFORM_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({'readable':result['readable'],'passing_exponents':[k for k,row in zip([None,*f['uniform_exponents']],rows) if row['phase_status'].startswith('CERTIFIED')]}),flush=True);return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');x=p.parse_args();verify(x.replay)
