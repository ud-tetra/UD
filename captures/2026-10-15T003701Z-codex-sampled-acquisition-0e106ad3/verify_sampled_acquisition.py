#!/usr/bin/env python3
"""Exact rational sampling certificates; no archived code is executed."""
from fractions import Fraction as F
import itertools as it,json,math,pathlib,sys
import sympy as sp
R=pathlib.Path(__file__).resolve().parent;checks={}
def check(name,condition,**data):
 assert condition,(name,data)
 checks[name]={'passed':True,**data}
def alt_sin(x,n):return sum(((-1)**k*x**(2*k+1)/math.factorial(2*k+1) for k in range(n+1)),F(0))
def sin_interval(x):
 assert 0<=x<=4
 # Tail terms decrease after these truncations; consecutive sums bracket sin(x).
 return alt_sin(x,25),alt_sin(x,26)
def square_interval(lo,hi):return (F(0) if lo<=0<=hi else min(lo*lo,hi*hi),max(lo*lo,hi*hi))
def atan_interval(x):
 def partial(n):return sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(n+1)),F(0))
 return partial(25),partial(26)
a0,a1=atan_interval(F(1,5));b0,b1=atan_interval(F(1,239))
pi_lo,pi_hi=16*a0-4*b1,16*a1-4*b0
z=(sp.Integer(5)+sp.I)**4*(sp.Integer(239)-sp.I)
check('Machin_angle_identity',sp.re(sp.expand(z))==sp.im(sp.expand(z)) and sp.re(sp.expand(z))>0,
      relation='pi=16*atan(1/5)-4*atan(1/239)')
check('pi_rational_enclosure',F(31,10)<pi_lo<pi_hi<F(22,7))
# Independently rederive the exact single-cell vertex trajectory.
cells=[list(it.combinations(range(4),k)) for k in range(1,5)];ofs=[0,4,10,14];A=sp.zeros(15)
for k in range(1,4):
 B=sp.zeros(len(cells[k-1]),len(cells[k]))
 for j,tet in enumerate(cells[k]):
  for i in range(k+1):B[cells[k-1].index(tet[:i]+tet[i+1:]),j]=(-1)**i
 i,j=ofs[k-1],ofs[k];A[i:i+B.rows,j:j+B.cols]=-B;A[j:j+B.cols,i:i+B.rows]=B.T
t=sp.symbols('t',real=True);e=sp.eye(15)[:,0];harm=sp.zeros(15,1);harm[:4,0]=sp.ones(4,1)/4
x=harm+sp.cos(2*t)*(e-harm)+sp.sin(2*t)*A*e/2
q=sp.trigsimp(x[4]**2+x[9]**2)
check('native_vertex_stock',A.T==-A and sp.simplify(x.diff(t)-A*x)==sp.zeros(15,1)
 and sp.trigsimp(q-sp.sin(2*t)**2/4)==0)
check('arbitrarily_fine_polling_misses_grazing',all(all(2*k!=n for k in range(n+1)) for n in range(3,200,2)),
      universal_argument='For every odd N, no grid k*pi/(2*N) equals peak pi/4 modulo pi/2',
      upper_threshold='1/4',lower_threshold='1/8',scope='direct threshold polling, not model-assisted reconstruction')
lo,hi=F(1,16),F(3,16);eps=F(1,128);delta=F(1,64);nu=F(3,8);D=2*eps/nu+delta
check('exact_sampling_budget',D==F(11,192) and D<F(1,16),epsilon=str(eps),delta=str(delta),
      slope_lower_bound=str(nu),delay_bound=str(D),linear_ideal_dwell='1/16')
# On the relevant rising/falling band |q'|^2=16*q*(1/4-q).
r=sp.symbols('r',real=True);speed_squared=16*r*(sp.Rational(1,4)-r)
check('transverse_slope_certificate',speed_squared.subs(r,sp.Rational(13,64))==sp.Rational(39,256)
 and speed_squared.subs(r,sp.Rational(3,64))==sp.Rational(39,256) and F(39,256)>nu*nu,
      endpoint_speed_squared='39/256',bound_squared='9/64')
margin=F(1,4)-(hi+2*eps)
check('confirmation_persistence_margin',margin==F(3,64) and 2*margin/F(2)>delta,
      two_sided_core_width_lower_bound='3/64',sample_gap='1/64')
# For this unimodal sinusoid the full upper/lower confirmation core is one interval.
N=128;trace=[];state=0;records=[];possible={(0,())}
for n in range(N+1):
 sl,sh=sin_interval(F(n,32));ql,qh=square_interval(sl,sh);ql/=4;qh/=4
 j0=(64*ql).numerator//(64*ql).denominator;j1=(64*qh).numerator//(64*qh).denominator
 assert j0==j1,'quantizer cell not certified';j=min(63,max(0,j0));y=F(2*j+1,128)
 old=state
 if state==0 and y-eps>=hi:state=1
 elif state==1 and y+eps<=lo:state=0
 mask=7 if state!=old else 0
 if mask:records.append({'tick':n,'mask':mask})
 # Overapproximate every possible independent additive observation error in [-eps,eps].
 updated=set()
 for st,word in possible:
  if st==0:
   can_flip=qh>=hi;can_hold=ql<hi+2*eps
  else:
   can_flip=ql<=lo;can_hold=qh>lo-2*eps
  if can_flip:updated.add((1-st,word+(n,)))
  if can_hold:updated.add((st,word))
 possible=updated
 trace.append({'tick':n,'q_interval':[str(ql),str(qh)],'quantizer_code':j,'quantized_stock':str(y),
               'response':state,'batch_mask':mask})
check('rational_quantizer_trace',len(trace)==129 and records==[{'tick':34,'mask':7},{'tick':84,'mask':7}],
      arithmetic='rational sine enclosures, no floating-point guard decisions',records=records)
check('quantization_error_enclosure',all(abs(F(x['quantized_stock'])-F(x['q_interval'][i]))<=eps for x in trace for i in [0,1]))
words=sorted({word for st,word in possible})
check('all_bounded_errors_preserve_per_address_word',all(st==0 and len(word)==2 for st,word in possible),
      possible_toggle_tick_words=[list(w) for w in words])
def delay_cert(tick,il,ih):return F(tick,64)>=ih and F(tick,64)<=il+D
check('all_error_words_meet_delay_bound',all(delay_cert(w[0],pi_lo/6,pi_hi/6)
 and delay_cert(w[1],5*pi_lo/12,5*pi_hi/12) for w in words),
      ideal_times=['pi/6','5*pi/12'],bound='11/192')
joint_words=list(it.product(words,repeat=3))
check('joint_error_batch_splitting',len(joint_words)==1728 and
 max(len(set(it.chain.from_iterable(w))) for w in joint_words)==6,
      per_address_word_combinations=1728,maximum_detection_batches=6,
      scope='bounded-error envelope; no probabilistic independence assumption')
check('horizon_no_unobserved_end_event',5*pi_hi/12+D<2 and 2*pi_lo/3>2+D,
      horizon='2',acquisition_ends_after_last_event_confirmation=True)
check('digitizer_delay_design',F(1,2**5)/nu+delta==F(19,192) and
      F(1,2**5)/nu+delta>F(1,16)>F(1,2**6)/nu+delta,
      minimum_bits_for_this_conservative_delay_certificate=6,chosen_bits=6,
      caveat='not a globally optimal ADC bit lower bound; criterion uses the supplied slope and linear dwell bound')
bits=6;tick_bits=math.ceil(math.log2(N+1));M=len(records)
resources={'sample_instants':N+1,'scalar_stock_values':3*(N+1),'current_stock_scratch_bits':3*bits,
 'raw_quantized_stock_archive_bits':3*(N+1)*bits,
 'response_bits':3,'tick_counter_bits':tick_bits,'batch_mask_buffer_bits':3,'dense_response_log_bits':3*(N+1),
 'sparse_log_bits':3+tick_bits+M*(3+tick_bits),'sparse_record_count':M,
 'independent_bounded_error_batch_records_upper_bound':6,'corresponding_sparse_bits_upper_bound':3+tick_bits+6*(3+tick_bits),
 'shared_metadata':'thresholds, scale, grid, error model, quantizer and initialization contract are supplied separately',
 'energy_cost':'OPEN','physical_boundary_area':'OPEN'}
check('finite_acquisition_ledger',resources['scalar_stock_values']==387 and tick_bits==8 and
 resources['raw_quantized_stock_archive_bits']==2322 and
 resources['dense_response_log_bits']==387 and resources['sparse_log_bits']==33 and
 resources['corresponding_sparse_bits_upper_bound']==77,**resources)
# Exact local finite-grid guard audit for the confirmation predicates.
grid=[F(k,64) for k in range(65)];err=[F(k,128) for k in range(-1,2)]
check('confirmed_guards_do_not_fire_early',all(not (v+e-eps>=hi) or v>=hi for v in grid for e in err)
 and all(not(v+e+eps<=lo) or v<=lo for v in grid for e in err),
      scope='finite-grid audit; universal guarantee follows from the written interval inequalities')
check('delay_order_criterion',F(1,10)>D and not(F(1,100)>D),
      sufficient_condition='later ideal time - earlier ideal time > earlier delay bound + 2*timestamp_error',
      global_gap_not_supplied_by_carrier=True)
check('three_event_order_receipt_lower_bound',math.factorial(3)==6 and 2**2<6<=2**3,
      bits=3,sufficient_to_observe_order=False)
out={'passed':True,'check_families':len(checks),'checks':checks,'physical_promotion':0,
 'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','scope':'Declared sampled passive observer; written proofs establish universal bounds; rational certificates verify the stated fixture.',
 'environment':{'python':sys.version,'sympy':sp.__version__}}
(R/'SAMPLED_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
(R/'SAMPLED_TRACE_CERTIFICATE.json').write_text(json.dumps({'pi_interval':[str(pi_lo),str(pi_hi)],
 'method':'sin partial sums at orders 25 and 26; 0<=argument<=4; exact rational guards','trace':trace,
 'possible_per_address_tick_words':words,'resources':resources},indent=2)+'\n')
print(json.dumps({'passed':True,'check_families':len(checks),'records':records,'possible_tick_words':words,'resources':resources}))
