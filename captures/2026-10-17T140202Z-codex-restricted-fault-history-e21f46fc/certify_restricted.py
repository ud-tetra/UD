"""Fit-independent restricted-fault certification and history-contract transfer.

No apparatus data. All precision requirements and fault-family restrictions
are hypotheses, not physical laws or observed performance.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json
import numpy as np
from scipy.sparse import csr_matrix
from flint import arb,ctx

ROOT=Path(__file__).resolve().parent;ctx.prec=256
def a(x):
 x=F(x);return arb(x.numerator)/x.denominator
def pair(x):
 x=F(x);return [x.numerator,x.denominator]
def enc(x):return {'arb_enclosure':str(x),'display_only':float(x.mid())}
def read(name):return json.loads((ROOT/'sources'/name).read_text())
def write(name,x):(ROOT/name).write_text(json.dumps(x,indent=2)+'\n')
def poly_mul(x,y):
 z=[F(0)]*(len(x)+len(y)-1)
 for i,v in enumerate(x):
  for j,w in enumerate(y):z[i+j]+=v*w
 return z

d=read('PROBE_DESIGN.json');z=np.load(ROOT/'sources/operators.npz')
A=csr_matrix((z['A_data'].astype(np.int64),z['A_indices'],z['A_indptr']),shape=(2640,2640))
shell=np.load(ROOT/'sources/SHELL_OPERATORS.npz')
AS=csr_matrix((shell['A_data'],shell['A_indices'],shell['A_indptr']),shape=A.shape)
assert (A-AS).nnz==0 and (A+A.T).nnz==0 and A.nnz==14880
assert set(map(int,A.data))=={-1,1}
obs=list(map(int,z['obs']));assert obs==d['observed_coordinates'] and len(obs)==189
assert set(shell['obs'])<=set(obs)
grade=np.repeat(np.arange(4),[120,720,1200,600]);color=d['colors'];qs=d['preparation_denominators'];m=d['color_count']
assert all(1<=q<=5 for q in qs)
coo=A.tocoo();assert np.all(np.abs(grade[coo.row]-grade[coo.col])==1)
channels=[]
for k in range(3):
 mask=np.minimum(grade[coo.row],grade[coo.col])==k
 channels.append(csr_matrix((coo.data[mask],(coo.row[mask],coo.col[mask])),shape=A.shape))
for i in range(3):
 for j in range(3):
  if i!=j:
   product=channels[i]@channels[j];product.eliminate_zeros();assert product.nnz==0
assert 9+3*arb(5).sqrt()<16 # inherited maximum squared frequency
assert {1,133,486,878,1680,2040}<=set(obs)
adj=[set(map(int,A.indices[A.indptr[i]:A.indptr[i+1]])) for i in range(2640)]
JC={int(r):v for r,v in d['readout_stencils'].items()}
JK={int(r):v for r,v in d['generator_row_stencils'].items()}
keys=set()
for r,cols in JC.items():
 for j in cols:
  assert color[j]>=0 and (r,color[j]) not in keys
  keys.add((r,color[j]))
  assert qs[color[j]]<=5
assert len(keys)==16175 and m==260
for c in range(m):
 support=[i for i,v in enumerate(color) if v==c]
 assert len(support)<=qs[c]**2 and len({int(grade[i]%2) for i in support})==1
for r,cols in JK.items():
 assert set(cols)<=set(JC[r]) and all(grade[j]%2!=grade[r]%2 for j in cols)

minimum=999;witness=None;checked=0
for u,v in d['metric_pairs']:
 assert grade[u]==grade[v]
 for r,t in [(u,v),(v,u)]:
  if r not in JC:continue
  exclusive=adj[t]-adj[r]
  assert exclusive<=set(JK[r]) and len(exclusive)>=3
  if len(exclusive)<minimum:minimum=len(exclusive);witness=[r,t]
  checked+=1
assert minimum==3

# Odd tenth-order derivative weights. Their power moments obey a rational
# generating function with nonnegative remainder coefficients.
order=5
w=[2*F((-1)**(k+1),k)*F(factorial(order)**2,factorial(order-k)*factorial(order+k)) for k in range(1,order+1)]
for r in range(order):assert sum(c*k**(2*r+1) for k,c in enumerate(w,1))==int(r==0)
denpoly=[F(1)]
for k in range(1,order+1):denpoly=poly_mul(denpoly,[F(1),F(-k*k)])
numerator=[F(0)]*(order+1)
for k,c in enumerate(w,1):
 prod=[F(1)]
 for j in range(1,order+1):
  if j!=k:prod=poly_mul(prod,[F(1),F(-j*j)])
 for j,v in enumerate(prod):numerator[j]+=c*k*v
expected=denpoly[:];expected[order]+=factorial(order)**2
assert numerator==expected
# Thus M_r=0 for1<=r<=4 and M_(5+j)=(5!)^2 h_j(1,4,9,16,25)>0.
h=F(1,128);Omega=F(5);eps=F(1,2**64);zz=a(Omega*h)
remainder=(sum(a(c)*(k*zz).sinh() for k,c in enumerate(w,1))-zz)/a(h)
assert remainder>0
Fh=sum(a(abs(c)*k*Omega)*(k*zz).exp() for k,c in enumerate(w,1))
noise_factor=(sum(abs(c) for c in w)+abs(sum(w)))/h
acode=arb(d['sum_preparation_denominator_squared']).sqrt()
arow=arb(d['maximum_dynamic_row_weight_squared']).sqrt()
tauC=acode*a(eps);TC=F(23,2**63)
assert tauC<a(TC)
Epass=a(TC)+tauC;Estar=F(1,2**57)
assert Epass<a(Estar)
tauK=arow*(remainder+Epass*Fh+a(noise_factor*eps))
TD=F(9,2**51);assert tauK<a(TD)
lo,hi=F(15,16),F(17,16)
cmetric=arb(minimum).sqrt()*a(lo/hi**2)
Spass=(a(TD)+tauK)/cmetric;Sstar=F(1,2**47)
assert Spass<2*a(TD)/cmetric<a(Sstar)
assert 4*hi/(lo-F(1,16))<Omega

# Sufficient component-wise way to realize the TOTAL per-code response bound.
expmax=a(Omega*(5*h+eps/128)).exp();assert expmax<a(F(5,4))
component_response=2*expmax*a(eps/16)+2*a(Omega)*expmax*a(eps/128)+2*a(eps/4)
assert component_response<a(eps)

# After fault passage, re-derive six-ratio accuracy in the presence of bounded
# off-diagonal metric and readout errors; do not assume the calibration theorem
# already applies when using that theorem to test model adequacy.
cal=read('PARENT_SIX_RATIO_CERTIFICATE.json')
assert cal['candidate_precision_contract']['requested_each_ratio_absolute_error_gate']==[1,2**39]
hc=F(1,32);mu=F(1,2**49);jc=F(1,2**55);solver=F(1,2**44)
eg=(hi+1)*mu
B0=a(5*(hc+jc)).exp()*a(mu+2*eg+hi*mu+2*hi*5*jc)/a(hc*lo)+a(F(1,2**60))
g0=a(hi/lo).sqrt();gs=a((hi+Sstar)/(lo-Sstar)).sqrt()
es=4*hi*Sstar/(lo*(lo-Sstar))
BS=2*g0*gs*a(es/lo)
gain_extra=a(Estar)*arb(6).sqrt()*a(1+mu)
BE=(a(Estar)*gs*a(2+mu)+2*gs*gain_extra)/a(hc*lo)
qerror=(B0+BS+BE+a(solver))*5/4
assert qerror<a(F(1,2**40))

# Shape reconstruction uses the parent's conservative2^-39 ratio cap.
delta=F(1,2**39);ell=a(delta/(lo-delta))
metric_diag=(6*ell).exp()-1
native_rate=a(F(1025,1024))*((1+a(F(1,2**38)))*(7*ell).exp()-1)
metric_frame_factor=(hi/lo)**3/lo
readout_frame_factor=(hi/lo)**3
metric_total=metric_diag+a(metric_frame_factor*Sstar)
readout_total=a(readout_frame_factor*Estar)
target=F(1,2**35)
assert metric_total<a(target) and native_rate<a(target) and readout_total<a(F(1,2**56))
ell40=a(F(1,2**40)/(lo-F(1,2**40)))
common_error=ell40.exp()-1
assert common_error<a(F(1,2**39))<a(F(1,1024))
parent=read('PARENT_FITTED_CERTIFICATE.json')
assert [p['retained_signal_condition_upper'] for p in parent['protocols']]==[19410,3385,1930]

# Exact one-color finite-response witnesses for native null and metric defects.
assert (0,4) in map(tuple,d['metric_pairs']) and 120 in JK[4] and 120 not in adj[4]
cc=color[120];scale=qs[cc]
prep=[int(c==cc) for c in color]
assert grade[4]%2!=grade[120]%2
assert sum(int(A[4,j]) for j,v in enumerate(prep) if v)==0
def metric_witness(rho):
 if rho:
  invden=rho.denominator**2-rho.numerator**2
  d0=rho.denominator;num=rho.numerator
 else:invden=1;d0=1;num=0
 rows=[]
 for i in range(2640):
  accum={};terms=[(i,invden)]
  if i==0:terms=[(0,d0*d0),(4,-num*d0)]
  if i==4:terms=[(4,d0*d0),(0,-num*d0)]
  for source,coefficient in terms:
   for k in range(A.indptr[source],A.indptr[source+1]):
    j=int(A.indices[k]);accum[j]=accum.get(j,0)+coefficient*int(A.data[k])
  rows.append(list(accum.items()))
 x=prep[:];powers=[x[4]];N=40
 for n in range(1,N+1):
  x=[sum(v*x[j] for j,v in row) for row in rows];powers.append(x[4])
 values=[];tails=[]
 for k in range(1,6):
  t=k*h;coefficient=F(1);value=F(powers[0])
  for n in range(1,N+1):
   coefficient*=t/(invden*n);value+=coefficient*powers[n]
  values.append(value/scale)
  zt=a(Omega*t);tails.append(zt.exp()*zt**(N+1)/factorial(N+1))
 decoded=sum(c*v for c,v in zip(w,values))*scale/h
 tail=sum(a(abs(c))*t for c,t in zip(w,tails))*a(F(scale,1)/h)
 coefficient=F(dict(rows[4]).get(120,0),invden)
 error=abs(a(decoded-coefficient))+tail
 assert error<a(scale)*remainder
 signal=abs(a(decoded))-tail
 if rho:
  assert signal-a(scale*noise_factor*eps)>a(TD)
 else:assert abs(a(decoded))+tail<a(TD)
 return {'rho':pair(rho),'decoded_value':pair(decoded),'true_forbidden_coefficient':pair(coefficient),
  'finite_estimator_coefficient_error_bound':enc(error),'signal_lower':enc(signal),
  'decision':'REJECT' if rho else 'WITHIN_NULL_GATE','synthetic':True}
controls=[metric_witness(F(0)),metric_witness(F(1,2**44)),metric_witness(F(-1,2**44))]
epsilon=F(1,2**40);encoded=epsilon/qs[color[0]]
assert 0 in JC[4] and encoded*qs[color[0]]==epsilon
assert a(epsilon)>a(TC)+tauC

raw=2*(m+1)*6*189;assert raw==591948
write('RESTRICTED_FAULT_CERTIFICATE.json',{
 'status':'DERIVED_CONDITIONAL_CONSTRUCTOR_VERIFIED','physical_promotion':0,'independent_review':'pending','lane':'development; no registry entry',
 'fault_family':{'coordinates':'selected fitted/normalized chain coordinates; all receipts apply in this frame',
  'H':'H0+S, H0 grade scalar with entries in[15/16,17/16]',
  'S':'symmetric same-grade off-diagonal matching on the2574 source-listed pairs, each pair has an observed endpoint; norm<=1/16',
  'w':'three positive native weights in[15/16,17/16], logger scale absorbed',
  'background_effective_ratios':'D_k=w_k/h_(k-1),U_k=w_k/h_k in[15/16,17/16]',
  'K':'(H0+S)^-1 A_w, constant through validation, calibration and later acquisition',
  'C':'189-by2640 readout; C-R supported in source local stencils; coarse normC<=2',
  'extra_skewJ':'excluded; set0, not inferred small by this protocol',
  'excluded':['Nonmatching metric defects','Cross-grade or diagonal metric heterogeneity','Readout outside listed stencils','Extra generator terms that could cancel a metric signal','Unbounded drift or nonlinear response']},
 'code':{'preparations':m,'controlled_coordinates':d['prepared_coordinate_count'],'local_readout_coefficient_rank':len(keys),
  'readout_code_sigma_min':[1,5],'metric_pairs':len(d['metric_pairs']),
  'minimum_exclusive_native_neighbor_count':minimum,'exclusive_count_witness':witness,'oriented_observed_endpoints_checked':checked,
  'times':[[0,1]]+[pair(k*h) for k in range(1,6)],'epochs':2,'blank_extra_each_epoch':True,
  'scalar_readings':raw,'including_one_six_ratio_calibration_scalar_readings':raw+12},
 'fit_independent_test':'Decode only coefficientsj withA[r,j]=0. They vanish for every diagonal grade-scalar background; do not subtract a fitted generator.',
 'instrument_contract':{'per_code_normalized_blank_corrected_189_vector_error':pair(eps),
  'sufficient_component_contract':{'coarse_readout_norm_upper':2,'full_state_preparation_error':pair(eps/16),
   'logger_time_error':pair(eps/128),'blank_corrected_additive_vector_error':pair(eps/4),
   'computation_error':pair(eps/4),'total_response_error_bound':enc(component_response)},
  'status':'candidate requirements; no apparatus receipt supplied'},
 'static_gate':{'decoded_residual_threshold':pair(TC),'decoded_error_bound':enc(tauC),
  'passing_readout_operator_error':enc(Epass),'declared_passing_readout_error_ceiling':pair(Estar),
  'unused_static_data_Frobenius_gate':pair(17*eps)},
 'dynamic_gate':{'positive_time_weights':[pair(c) for c in w],'zero_time_weight':pair(-sum(w)),
  'step':pair(h),'generator_norm_upper':5,'moment_identity':'sum_(r>=0) M_r t^r =1+14400t^5/product_(k=1..5)(1-k^2t)',
  'derivative_remainder_bound':enc(remainder),'readout_contamination_factor':enc(Fh),
  'noise_amplification_factor':pair(noise_factor),'maximum_row_decoder_factor':enc(arow),
  'row_error_bound':enc(tauK),'forbidden_row_residual_acceptance_ceiling':pair(TD),
  'metric_signal_lower_factor':enc(cmetric),'passing_metric_defect_bound':enc(Spass),
  'declared_passing_metric_defect_ceiling':pair(Sstar),
  'visibility_proof':'For matched pair(r,t), forbidden row equals[-s/(h_grade^2-s^2)]*(A_w rowt) off native support; exclusive count>=3 andw>=15/16.'},
 'robust_six_ratio_extension':{'gain_preparation_observed_infinity_error':[1,2**49],
  'full_gain_preparation_error_additional_receipt':'at actual gain readout, full state norm<=sqrt6*2^-49 including unobserved coordinates; this supplements the observed infinity receipt',
  'larger_generator_envelope':5,'baseline_feature_error_bound':enc(B0),
  'metric_model_feature_error_bound':enc(BS),'readout_model_feature_error_bound':enc(BE),
  'resulting_six_ratio_vector_error_bound':enc(qerror),'declared_six_ratio_vector_ceiling':[1,2**40],
  'scope':'Re-derived after restricted-fault passage; no circular assumption that the original diagonal-only calibration theorem already applies'},
 'history_transfer':{'metric_defect_frame_factor':pair(metric_frame_factor),'readout_frame_factor':pair(readout_frame_factor),
  'requires_measured_effective_rate_shape_gate':[1,2**38],'diagonal_metric_shape_error':enc(metric_diag),
  'total_metric_shape_error_including_S':enc(metric_total),'native_rate_shape_error':enc(native_rate),
  'readout_error_in_final_fitted_frame':enc(readout_total),'declared_final_readout_ceiling':[1,2**56],
  'common_scale_error_after_chat_time_normalization':enc(common_error),'declared_common_scale_error_ceiling':[1,2**39],
  'parent_metric_and_rate_budget_each':[1,2**35],'extra_skewJ':0,
  'history_sampling':'logger step1/(2*chat), transformed37 preparations andsoftware outputframe corrections',
  'gain_correction_policy':'Retain the globally validatedC for history. The six residual gain estimates normalize calibration features only; changing the acquisition correction requires renewed readout validation.',
  'retained_signal_count':1893,'parent_condition_bounds':{'2048':19410,'4096':3385,'8192':1930},
  'additional_required_history_receipts':{'preparation_error':[1,2**25],'additive_noise':[1,2**26],
   'origin_error':[1,2**29],'jitter':[1,2**29],'constant_params_entire_batch':True},
  'actual_kernel_dimension_unchanged_claimed':False},
 'synthetic_metric_controls':controls,
 'synthetic_static_control':{'row':4,'column':0,'epsilon':pair(epsilon),'encoded':pair(encoded),'exactly_decoded':True,'decision':'REJECT','synthetic':True},
 'limits':{'unrestricted_static_readout_nullity_per_row':2380,'six_time_unrestricted_readout_nullity_per_row_lower':1080,
  'restricted_family_membership_not_proved_by_gate_passage':True,'finite_epochs_do_not_certify_arbitrary_future_drift':True,
  'independent_review':'pending','physical_experiment':'not executed'},
 'verification':{'exact_sparse_entries':14880,'local_coefficients_injective':len(keys),
  'metric_exclusive_neighbor_bound':'all listed observed endpoints checked','moment_rational_identity':'exact',
  'interval_bits':ctx.prec,'finite_metric_control_count':3}})
print(json.dumps({'status':'PASS','static_error_ceiling':pair(Estar),'metric_error_ceiling':pair(Sstar),
 'dynamic_threshold':pair(TD),'metric_bound_display':float(Spass),'robust_ratio_error_display':float(qerror),
 'history_total_metric_error_display':float(metric_total),'validation_readings':raw}))
