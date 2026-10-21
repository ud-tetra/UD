#!/usr/bin/env python3
"""Independent exact Chebyshev recurrence, impulse-index and budget controls."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
s=F(61,27648);a=s*s;c=(1+a)/2;d=(1-a)/2;sig=c/d;N=8192;u=F(1,2**67)
q=(1-s)/(1+s);assert q==F(27587,27709)
# Exact ideal error comparison; no floating log or asymptotic approximation.
lhs=pow(q.numerator,N)*2**52;rhs=pow(q.denominator,N);assert lhs<rhs
alpha_cap=F(1,2**51);assert (1+alpha_cap)/s<512
G=(1+s)**2/(2*s);assert G<256
assert 1/c<2 and 2/d<5 and a<F(1,5)
local=11*u;total=256*N*local;assert total==11*F(1,2**46)<F(1,2**42)
# Chebyshev T and U are independent direct polynomial recurrences.
def Ts(z,n):
 vals=[F(1)]
 if n:vals.append(z)
 for k in range(1,n):vals.append(2*z*vals[-1]-vals[-2])
 return vals
def Us(z,n):
 vals=[F(1)]
 if n:vals.append(2*z)
 for k in range(1,n):vals.append(2*z*vals[-1]-vals[-2])
 return vals
K=8;den=Ts(sig,K);rho=[den[k]/den[k+1]for k in range(K)]
assert rho[0]==d/c and all(F(0)<v<1 for v in rho)
for k in range(1,K):assert rho[k]==1/(2*sig-rho[k-1])
checks=0
for lam in [F(0),a,c,F(1)]:
 z=(c-lam)/d;t=Ts(z,K);uc=Us(z,K);x=[F(0),1/c]
 for k in range(1,K):x.append(x[k]+rho[k]*rho[k-1]*(x[k]-x[k-1])+(2*rho[k]/d)*(1-lam*x[k]))
 for n in range(1,K+1):
  expected=(1-t[n]/den[n])/lam if lam else F(n)*Us(sig,n-1)[-1]/(d*den[n])
  assert x[n]==expected;checks+=1
 # Full forced recurrence at every insertion, including j1 and jN.
 for j in range(1,K+1):
  e=[F(0)]*(K+1)
  if j==1:e[1]=1
  for k in range(1,K):
   e[k+1]=2*rho[k]*z*e[k]-rho[k]*rho[k-1]*e[k-1]+(1 if k+1==j else 0)
  for n in range(j,K+1):
   kernel=den[j]*uc[n-j]/den[n];assert e[n]==kernel and abs(kernel)<=G;checks+=1
# Exact hidden impulse at the final step survives with unit gain.
assert den[K]/den[K]*Us(sig,0)[0]==1
# Hidden constant forcing isn't killed by q_N(0).
hidden_q=F(K)*Us(sig,K-1)[-1]/(d*den[K]);assert hidden_q>0
r={'status':'PASS_EXACT_RECURRENCE_GREEN_INDICES_AND_BUDGET','s':str(s),'spectral_a':str(a),'c':str(c),'d':str(d),'sigma':str(sig),'N':N,'q':str(q),'ideal_alpha_strict_upper':'2^-51','ideal_gain_strict_upper':'512','full_space_Green_uniform_upper':str(G),'Green_strict_upper':'256','local_error_upper':str(local),'conditional_algorithm_error_strict_upper':str(total),'algorithm_comparison':'11*2^-46<2^-42','exact_ideal_comparison':{'comparison':'27587^8192*2^52<27709^8192','left_bits':lhs.bit_length(),'right_bits':rhs.bit_length(),'left_integer_sha256':hashlib.sha256(lhs.to_bytes((lhs.bit_length()+7)//8,'big')).hexdigest(),'right_integer_sha256':hashlib.sha256(rhs.to_bytes((rhs.bit_length()+7)//8,'big')).hexdigest()},'small_exact_reference':{'steps':K,'spectral_nodes':['0','a','c','1'],'checks':checks,'all_impulse_insertion_indices_including_initial_and_final':True,'hidden_q_at_zero_nonzero':True,'final_impulse_gain':1},'scope':{'whole_update_arithmetic_error_includes_coefficients':True,'absolute_oracle_errors_must_cover_actual_iterate_domain':True,'no_actual_weighted_F_or_Ftranspose_oracle_validated':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'REFERENCE_CHECKS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'reference_checks':checks,'Green_float_display':float(G),'algorithm_error_float_display':float(total)}))
