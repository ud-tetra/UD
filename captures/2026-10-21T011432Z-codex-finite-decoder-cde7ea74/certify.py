#!/usr/bin/env python3
"""Exact finite-decoder theorem constants and small scalar recurrence controls."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib

S=F(61,27648)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 H=lambda b:hashlib.sha256(b).hexdigest()
 parent=a.repo/'captures/2026-10-20T235659Z-codex-error-propagation-550c9eb1';cond=a.repo/'captures/2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67'
 inputs={'error_result':(parent/'RESULT.json','753a86f65f285a60ad9cfa7a527c1ff464b359b46c2b5df1083dd4785e0516fb'),'error_theorem':(parent/'THEOREM.md','946d40156db42380406f476508236beea027c734deef46680b2bc944be18106c'),'condition_result':(cond/'RESULT.json','ccc92afdfc0c2057a2d0ee29940eef907ad7c2c3817497a8af4726dc063695d2')}
 for path,h in inputs.values():assert H(path.read_bytes())==h
 N=8192;a0=S*S;c=(1+a0)/2;d=(1-a0)/2;sigma=c/d;q=(1-S)/(1+S);C=1/S;G=(1+S)**2/(2*S);u=F(1,2**67)
 assert q==F(27587,27709);num=2*q.numerator**N;den=q.denominator**N;assert num*2**51<den
 alpha=F(1,2**51);gain=(1+alpha)/S;arith=11*F(1,2**46);assert gain<512 and G<256 and arith<F(1,2**42)
 assert 2/d<5 and 1/c<2 and 4*C+F(1,2**42)<2048
 assert 2640*F(1,2**160)<F(1,2**134)
 controls=0
 def T(k,x):
  p0=F(1)
  if k==0:return p0
  p1=x
  for _ in range(1,k):p0,p1=p1,2*x*p1-p0
  return p1
 def U(k,x):
  p0=F(1)
  if k==0:return p0
  p1=2*x
  for _ in range(1,k):p0,p1=p1,2*x*p1-p0
  return p1
 def reference(lam,g,n):
  x0=F(0);x1=g/c;rho=d/c
  for k in range(1,n):
   nex=1/(2*sigma-rho);x2=x1+nex*rho*(x1-x0)+(2*nex/d)*(g-lam*x1);x0,x1=x1,x2;rho=nex
  return x1
 for n in [1,2,3,4,8,16]:
  for lam in [F(0),a0,c,F(1)]:
   z=(c-lam)/d;p=T(n,z)/T(n,sigma)
   x=reference(lam,lam,n);assert x==1-p;controls+=1
   if lam==0:assert reference(lam,F(1),n)==n*U(n-1,sigma)/(d*T(n,sigma));controls+=1
 # The C28 data profile now substitutes derived ideal decoder alpha/beta.
 data=__import__('json').loads((parent/'RESULT.json').read_text());D=F(data['conditional_example']['normalized_data_error_bound']);total=alpha+512*D+arith;assert total<F(1,2**40)
 result={'status':'PASS_FINITE_MATRIX_FREE_DECODER_THEOREM_CONSTANTS','steps':N,'s':str(S),'a':str(a0),'c':str(c),'d':str(d),'rho_gap_ratio':str(q),'projection_defect_alpha':'<2^-51 on the full2640state space','exact_decoder_gain_beta':'<512','Green_full_space_uniform_bound':str(G)+'<256','whole_update_oracle_budget':'each g-error,A-action-error,aggregate arithmetic defect <=2^-67','accumulated_implementation_error':'<11*2^-46<2^-42','state_domain_for_data_norm_at_most2':2048,'factorized_action_contract':{'true_F_forward_error':'<=2^-68 absolute on state ball2048','true_F_adjoint_error':'<=2^-68 absolute on data ball2049','implied_normal_error':'<=2^-67','actual_600cell_action_status':'NOT_VALIDATED_HOLD'},'exact_scalar_recurrence_controls':controls,'conditional_C28_profile_total_upper':str(total),'conditional_C28_profile_implication':'<2^-40 IF physical/input and action-oracle bounds hold','actual_600cell_decoder_execution':'NOT_RUN_HOLD','physical_promotion':0,'external_promotion_review':'PENDING'}
 def ih(x):return H(x.to_bytes((x.bit_length()+7)//8,'big'))
 witness={'integer_power_inequality':'2*27587^8192*2^51<27709^8192','numerator_2_times_power_bits':num.bit_length(),'denominator_power_bits':den.bit_length(),'numerator_sha256_big_endian':ih(num),'denominator_sha256_big_endian':ih(den),'initial_state_exact_zero':True,'kernel_handling':'q_N(0) generally nonzero; exact Ftranspose seed lies in V, so B_N rangeV; finite errors treated on fullspace'}
 bindings={k:{'path':str(p.relative_to(a.repo)),'sha256':h}for k,(p,h)in inputs.items()}
 for name,obj in [('RESULT.json',result),('POLYNOMIAL_WITNESS.json',witness),('SOURCE_BINDINGS.json',bindings)]: (a.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':result['status'],'N':N,'scalar_controls':controls,'actual_action_admission':'HOLD'}))
if __name__=='__main__':main()
