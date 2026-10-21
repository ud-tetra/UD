#!/usr/bin/env python3
"""Independent full8192-step diagonal-proxy arithmetic control.
This is NOT the actual weighted600-cell oracle or decoder.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from flint import arb,ctx
P=Path(__file__).resolve().parent;ctx.prec=192
s=F(61,27648);a=s*s;c=(1+a)/2;d=(1-a)/2;sig=c/d;N=8192;bits=96;unit=F(1,2**67)
A=(F(0),F(1,65536),F(1));target=(F(0),F(1,2),F(1,4));g=tuple(A[i]*target[i]for i in range(3))
def ball(x):return arb(x.numerator)/x.denominator
def quant(x):
 n=int((x*2**bits).mid().floor().unique_fmpz());q=arb(n)/2**bits
 assert abs(x-q)<arb(1)/2**80
 return F(n,2**bits)
results=[]
for injected in [False,True]:
 # Error norms are eachu/2, withinu, with opposite signs to avoid cancellation.
 ge=(unit/2 if injected else F(0));ae=(-unit/2 if injected else F(0))
 gp=(ge,g[1],g[2]);prev=[F(0)]*3;x=[quant(ball(t)/ball(c))for t in gp];local_coordinate_checks=3;maximum=max(abs(t)for t in x);rho_prev=ball(d/c)
 for k in range(1,N):
  rho=1/(2*ball(sig)-rho_prev);assert rho>0 and rho<1
  nxt=[]
  for i in range(3):
   oracle= A[i]*x[i]+(ae if i==0 else 0)
   exact=ball(x[i])+rho*rho_prev*(ball(x[i])-ball(prev[i]))+(2*rho/ball(d))*(ball(gp[i])-ball(oracle))
   nxt.append(quant(exact));local_coordinate_checks+=1
  prev,x=x,nxt;rho_prev=rho;maximum=max(maximum,*map(abs,x))
  assert sum(v*v for v in x)<2048**2
 err2=sum((x[i]-target[i])**2 for i in range(3));bound=F(1,2**51)+11*F(1,2**46)
 assert err2<bound*bound
 if injected:assert x[0]>0 # coherent hidden forcing survives; not range-P rounded.
 results.append({'mode':'coherent_hidden_oracle_errors'if injected else'clean_exact_proxy_actions','final_state_denominator_power2':bits,'final_state_numerators':[str(int(v*2**bits))for v in x],'squared_error_vs_observable_target':str(err2),'error_upper_for_comparison':str(bound),'complete_update_coordinate_error_checks':local_coordinate_checks,'maximum_coordinate_absolute':str(maximum),'actual_weighted600_oracle_test':False})
r={'status':'PASS_INDEPENDENT_ARBITRARY_PRECISION_FULL8192_DIAGONAL_PROXY_CONTROLS','N':N,'proxy_normal_diagonal':[str(v)for v in A],'proxy_F':'two output rows selecting state2/256 and state3','state_grid_bits':bits,'coefficient_Arb_bits':192,'local_coordinate_defect_strict_upper':'2^-80','source_decay_and_Green_proof':'REFERENCE_CHECKS.json and DECODER_LEMMAS.md','cases':results,'scope':{'finite_proxy_reference_only':True,'not_actual_600cell_oracle_or_floating_estimator':True,'one_proxy_vector_test_not_full_operator_conformance':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'ARB_REFERENCE_CHECKS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'total_coordinate_checks':sum(v['complete_update_coordinate_error_checks']for v in results)}))
