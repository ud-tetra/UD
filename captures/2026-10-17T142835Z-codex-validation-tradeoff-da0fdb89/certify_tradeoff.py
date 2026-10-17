"""Optimize a declared central-stencil certificate family, not all experiments.

Exact rational geometry and finite gate bounds; Arb solves continuous step
optimization and precision ceilings. No independent/stochastic averaging.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
import json,hashlib
import numpy as np
from scipy.sparse import csr_matrix
from flint import arb,ctx

ROOT=Path(__file__).resolve().parent;ctx.prec=512
def a(x):
 if isinstance(x,arb):return x
 x=F(x);return arb(x.numerator)/x.denominator
def pair(x):
 x=F(x);return [x.numerator,x.denominator]
def enc(x):return {'arb_enclosure':str(x),'display_only':float(x.mid())}
def read(name):return json.loads((ROOT/'sources'/name).read_text())
def write(name,x):(ROOT/name).write_text(json.dumps(x,indent=2)+'\n')
def interval_max(xs):
 out=xs[0]
 for x in xs[1:]:
  if x>out:out=x
  elif not out>=x:out=out.union(x)
 return out

d=read('PROBE_DESIGN.json');z=np.load(ROOT/'sources/operators.npz')
A=csr_matrix((z['A_data'].astype(np.int64),z['A_indices'],z['A_indptr']),shape=(2640,2640))
assert (A+A.T).nnz==0 and set(map(int,A.data))=={-1,1}
obs=set(d['observed_coordinates']);colors=d['colors'];q=d['preparation_denominators']
adj=[set(map(int,A.indices[A.indptr[i]:A.indptr[i+1]])) for i in range(2640)]
records=[];row_factor={}
for rs,stencil in d['readout_stencils'].items():
 r=int(rs);M=sum(q[colors[j]]**2 for j in stencil)
 root=isqrt(M);ceil=root+int(root*root<M)
 # A strict null-covering rational threshold even for perfect squareM.
 t=F(ceil)+F(1,16);row_factor[r]=(t,F(2*ceil)+F(1,16),M)
 assert a(t)>arb(M).sqrt()
for u,v in d['metric_pairs']:
 for r,t in [(u,v),(v,u)]:
  if r not in obs:continue
  js=sorted(adj[t]-adj[r]);assert len(js)>=3
  mean=sum(F(q[colors[j]]) for j in js)/len(js)
  records.append({'row':r,'partner':t,'exclusive_columns':js,
   'exclusive_signs':[int(A[t,j]) for j in js],
   'mean_decode_denominator':pair(mean),
   'readout_row_gate_factor':pair(row_factor[r][0]),
   'readout_row_error_factor':pair(row_factor[r][1])})
pairs=sorted(set((F(*x['mean_decode_denominator']),F(*x['readout_row_error_factor'])) for x in records))
assert len(records)==3171 and len(pairs)==107
assert max(x[0] for x in pairs)==F(14,3)
assert d['sum_preparation_denominator_squared']==2073
write('MATCHED_FILTER_DESIGN.json',{'status':'EXACT_CONSTRUCTOR_VERIFIED','physical_promotion':0,
 'records':records,'oriented_filters':len(records),'distinct_bound_pairs':len(pairs),
 'score':'mean_(j inN_partner minusN_row) A[partner,j] * decodedK[row,j]',
 'row_gate_factors':{str(r):pair(v[0]) for r,v in row_factor.items()},
 'global_readout_gate_factor':46,'unused_static_gate_factor':17})

lo,hi=F(15,16),F(17,16);G=F(8,7);om=5;cS=lo/hi**2
assert (a(F(9,7))).sqrt()<a(G)
hc=F(1,32);mu=F(1,2**49);jc=F(1,2**55);solver=F(1,2**44)
eg=(hi+1)*mu
B0=a(5*(hc+jc)).exp()*a(mu+2*eg+hi*mu+2*hi*5*jc)/a(hc*lo)+a(F(1,2**60))
base=(B0+a(solver))*5/4
def calibration(S,E):
 S=a(S);E=a(E)
 g0=a(hi/lo).sqrt();gs=((a(hi)+S)/(a(lo)-S)).sqrt()
 es=4*a(hi)*S/(a(lo)*(a(lo)-S))
 BS=2*g0*gs*es/a(lo)
 extra=E*arb(6).sqrt()*a(1+mu)
 BE=(E*gs*a(2+mu)+2*gs*extra)/a(hc*lo)
 return base+(BS+BE)*5/4
def constants(m):
 w=[2*F((-1)**(k+1),k)*F(factorial(m)**2,factorial(m-k)*factorial(m+k)) for k in range(1,m+1)]
 for r in range(m):assert sum(c*k**(2*r+1) for k,c in enumerate(w,1))==int(r==0)
 C=G*F(factorial(m)**2,factorial(2*m+1))*om**(2*m+1)
 FF=G*om*sum(abs(c)*k for k,c in enumerate(w,1))
 NN=abs(sum(w))+sum(abs(c) for c in w)
 return w,C,FF,NN
def step_bounds(m,h,eps):
 w,C,FF,NN=constants(m)
 B=C*h**(2*m);N=NN/h
 S=max(2*v*(B+(L*FF+N)*eps)/cS for v,L in pairs)
 E=92*eps
 return {'weights':w,'C':C,'F':FF,'N':N,'B':B,'S':S,'E':E,
         'calibration':calibration(S,E) if S<lo else arb(100)}
def optimal(m,eps):
 _,C,FF,NN=constants(m)
 h=(a(NN*eps/(2*m*C)).log()/(2*m+1)).exp()
 f=(2*m+1)*a(C)*h**(2*m)
 S=interval_max([2*a(v)*(f+a(L*FF*eps))/a(cS) for v,L in pairs])
 E=92*eps
 return h,S,E,calibration(S,E)

# Continuoush optimum is exact: minimizeC h^(2m)+NN eps/h.
# Maximum over pair-affine increasing functions has the same minimizingh.
target=a(F(1,2**39));front=[]
for m in range(1,13):
 lower=F(1,2**90);upper=F(1,2**45)
 assert optimal(m,lower)[3]<target and optimal(m,upper)[3]>target
 for _ in range(80):
  mid=(lower+upper)/2;err=optimal(m,mid)[3]
  if err<target:lower=mid
  elif err>target:upper=mid
  else:raise AssertionError('Increase interval precision for root comparison')
 bits=next(b for b in range(45,91) if F(1,2**b)<=lower)
 # Root bracket determines the binary precision unambiguously.
 assert F(1,2**(bits-1))>upper
 # Exact simple power-of-two step representative; not claimed continuous-optimal.
 candidates=[]
 for k in range(3,33):
  h=F(1,2**k);v=step_bounds(m,h,F(1,2**bits))
  if v['calibration']<target:candidates.append((v['calibration'],k,v))
 assert candidates
 # Select the best certified rational step by a comparison with disjoint
 # enclosures; no decision uses a floating-point midpoint.
 selected=candidates[0]
 for cand in candidates[1:]:
  if cand[0]<selected[0]:selected=cand
  elif not cand[0]>selected[0]:raise AssertionError('Ambiguous step comparison')
 _,k,v=selected;h=F(1,2**k)
 hstar=optimal(m,F(1,2**bits))[0]
 front.append({'order_half':m,'derivative_order':2*m,'positive_samples':m,
  'total_time_nodes':m+1,'scalar_readings':2*261*(m+1)*189,
  'continuous_error_ceiling_bracket':[pair(lower),pair(upper)],
  'minimum_binary_precision_bits':bits,'dyadic_error_ceiling':[1,2**bits],
  'continuous_optimal_step_at_binary_precision':enc(hstar),
  'certified_power_of_two_step':pair(h),'certified_last_time':pair(m*h),
  'certified_metric_defect_bound':pair(v['S']),'certified_readout_error_bound':pair(v['E']),
  'certified_six_ratio_error':enc(v['calibration'])})
pareto=[]
best_precision=F(0)
for x in front:
 L,U=[F(*v) for v in x['continuous_error_ceiling_bracket']]
 if L>best_precision:pareto.append(x['order_half']);best_precision=L
 elif U>=best_precision:raise AssertionError('Refine precision brackets')
best=max(front,key=lambda x:F(*x['continuous_error_ceiling_bracket'][0]))
best_eps=F(*best['continuous_error_ceiling_bracket'][0])
assert all(best_eps>F(*x['continuous_error_ceiling_bracket'][1]) for x in front if x is not best)
best_h_interval=optimal(best['order_half'],best_eps)[0]
best_h_centre=F(str(best_h_interval.mid().fmpq()))*2**80
best_h=F((2*best_h_centre.numerator+best_h_centre.denominator)//(2*best_h_centre.denominator),2**80)
best_feasible=step_bounds(best['order_half'],best_h,best_eps)
assert best_feasible['calibration']<target
# Allhigherorders are dominated once even the static-contamination floor
# exceeds the calibration gate. FF_m grows strictly withm.
cutoff=13;_,_,FFcut,_=constants(cutoff)
Sfloor=max(2*v*L*FFcut*best_eps/cS for v,L in pairs)
assert calibration(Sfloor,92*best_eps)>target

# A global binary precision floor within this error-envelope family.
# m>=4 ruled out by monotone readout floor; m=1,2,3 by their exact continuous optima.
eps57=F(1,2**57);_,_,FF4,_=constants(4)
floor4=max(2*v*L*FF4*eps57/cS for v,L in pairs)
assert calibration(floor4,92*eps57)>target
for m in [1,2,3]:assert optimal(m,eps57)[3]>target
assert min(x['minimum_binary_precision_bits'] for x in front)==58

# Recommended dyadic corner: minimum bits, then smallest reading count.
rec=next(x for x in front if x['minimum_binary_precision_bits']==58)
assert rec['order_half']==4
m=4;h=F(*rec['certified_power_of_two_step']);eps=F(1,2**58)
v=step_bounds(m,h,eps);S,E=v['S'],v['E']
assert h==F(1,256)
ell=a(F(1,2**39)/(lo-F(1,2**39)))
metric_diag=(6*ell).exp()-1
rate=a(F(1025,1024))*((1+a(F(1,2**38)))*(7*ell).exp()-1)
metric_total=metric_diag+a((hi/lo)**3/lo*S)
readout_total=a((hi/lo)**3*E)
common=ell.exp()-1
assert metric_total<a(F(1,2**35)) and rate<a(F(1,2**35))
assert readout_total<a(F(1,2**25)) and common<a(F(1,1024))

# Same previous strongerE,S,q limits, with fewer reads butno precision relaxation.
strict=[]
for mm in range(1,13):
 for k in range(3,33):
  vv=step_bounds(mm,F(1,2**k),F(1,2**64))
  if vv['S']<F(1,2**47) and vv['E']<F(1,2**57) and vv['calibration']<a(F(1,2**40)):
   strict.append((mm,k,vv));break
assert min(x[0] for x in strict)==3
strictm,strictk,strictv=min(strict,key=lambda x:x[:2])
for mm in [1,2]:assert optimal(mm,F(1,2**64))[1]>a(F(1,2**47))

write('TRADEOFF_CERTIFICATE.json',{
 'status':'DERIVED_CONDITIONAL_CONSTRUCTOR_VERIFIED','physical_promotion':0,'independent_review':'pending',
 'lane':'development; no registry entry','fault_family':'Unchanged fromPARENT_RESTRICTED_CERTIFICATE.json; matching same-gradeS, local readout stencils, positive constant native rates, noextraJ',
 'proof_improvements':{'matched_filter_count':3171,'scalar_metric_visibility_lower':pair(cS),
  'largest_mean_decoder_denominator':pair(F(14,3)),
  'readout_row_bound':'normE_row < (ceil_sqrtM+1/16+sqrtM)eps <=(2ceil_sqrtM+1/16)eps',
  'coarse_propagator_norm_upper':pair(G),'Hermite_remainder':'G*(m!)^2/(2m+1)! *5^(2m+1)*h^(2m)',
  'readout_contamination':'G*5*sum_k abs(a_k)*k; no exponential time penalty',
  'averaging':'No statistical cancellation or independent-noise assumption'},
 'search_family':{'stencils':'standard maximally accurate equispaced centered first-derivative formula, interpolation exact throughdegree2m, for everym>=1; odd-output negativevalues supplied by established native parity',
  'orders_explicitly_solved':list(range(1,13)),'higher_orders':'m>=13 dominated by monotone static-contamination floor',
  'step_domain_for_continuous_optimum':'all positiveh',
  'dyadic_step_representatives_exhausted':'h=2^-k,k=3..32',
  'root_bisection_steps':80,'interval_bits':ctx.prec,
  'optimal_step_formula':'hstar=(N_m eps/(2m C_m))^(1/(2m+1))',
  'optimality_scope':'For this fixed260-code deterministic error-envelope certificate family only; not a universal experimental or information bound'},
 'continuous_precision_frontier':front,'continuous_pareto_orders_half':pareto,
 'best_continuous_precision_order_half':best['order_half'],
 'near_continuous_ceiling_feasible_witness':{'order_half':best['order_half'],
  'response_error_ceiling':pair(best_eps),'rational_step':pair(best_h),
  'six_ratio_error':enc(best_feasible['calibration']),
  'scope':'A certified near-ceiling rational witness; the root itself is a strict admissibility boundary'},
 'binary_precision_floor':{'minimum_bits':58,'eps2^-57_not_certifiable_by_this_envelope':True,
  'm1to3_continuous_optimum_check':True,'m_ge4_monotone_readout_floor_check':True,
  'not_a_physical_or_information_theoretic_noise_floor':True},
 'recommended':{**rec,'total_response_error_ceiling':[1,2**58],
  'positive_time_weights':[pair(x) for x in v['weights']],
  'zero_time_weight':pair(-sum(v['weights'])),'stable_remainder_bound':pair(v['B']),
  'readout_contamination_factor':pair(v['F']),'noise_amplification_factor':pair(v['N']),
  'pair_gate':'abs(score_(r,t))<qmean_(r,t)*[B+(L_row*F+N)*eps]',
  'static_global_gate_factor':46,'static_row_gate':'(ceil_sqrtM+1/16)*eps','unused_static_gate_factor':17,
  'full_preparation_error_sufficient':[1,2**62],'logger_time_error_sufficient':[1,2**65],
  'blank_corrected_additive_error_sufficient':[1,2**60],'computation_error_sufficient':[1,2**60],
  'shape_acceptance_gate_retained':[1,2**38],
  'history_total_metric_bound':enc(metric_total),'history_native_rate_bound':enc(rate),
  'history_final_readout_bound':enc(readout_total),'history_common_scale_bound':enc(common),
  'history_signal_count':1893,'history_conditions':{'2048':19410,'4096':3385,'8192':1930},
  'separate_history_acquisition_receipts':'Retained unchanged; not supplied by the validator'},
 'strict_target_variant':{'previous_readout_ceiling':[1,2**57],'previous_metric_ceiling':[1,2**47],
  'previous_ratio_ceiling':[1,2**40],'response_error_ceiling':[1,2**64],
  'order_half':strictm,'step':pair(F(1,2**strictk)),
  'scalar_readings':2*261*(strictm+1)*189,'metric_bound':pair(strictv['S']),
  'ratio_bound':enc(strictv['calibration'])},
 'comparison_to_parent':{'parent_readings':591948,'recommended_readings':493290,
  'recommended_reading_reduction_fraction':[1,6],'recommended_allowable_response_error_ratio':[64,1],
  'strict_variant_reading_reduction_fraction':[1,3],
  'important':'Recommended variant preserves history targets but relaxes the previousextra safety marginsE2^-57,S2^-47,q2^-40. Strict variant retains them.'},
 'open':['Actual bounded-error and preparation receipts','Fault-family membership','Measured shape gate','Stability through later acquisition','Independent review','Alternative codes, correction schemes and stochastic models outside optimization family']})
print(json.dumps({'status':'PASS','pareto_m':pareto,'best_continuous_m':best['order_half'],
 'recommended_m':4,'recommended_step':pair(h),'error_ceiling':[1,2**58],
 'readings':493290,'ratio_error_display':float(v['calibration']),
 'metric_fault_display':float(S),'strict_variant_m':strictm}))
