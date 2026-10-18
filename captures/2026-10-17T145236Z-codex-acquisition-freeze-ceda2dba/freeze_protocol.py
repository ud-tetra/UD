"""Build an immutable proposed acquisition contract from the inherited certificates."""
from pathlib import Path
from fractions import Fraction as F
import csv,hashlib,json
import numpy as np
from scipy.sparse import csr_matrix
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parent
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def digest(x):return hashlib.sha256(x).hexdigest()
def pair(x):x=F(x);return [x.numerator,x.denominator]
def f(x):return F(*x)
def a(x):x=F(x);return arb(x.numerator)/x.denominator
def bound(x,up,bits=80):
 y=(x*2**bits).upper() if up else (x*2**bits).lower()
 return F(int((y.ceil() if up else y.floor()).fmpq()),2**bits)
def read(n):return json.loads((ROOT/'sources'/n).read_text())
def save(n,x):(ROOT/n).write_text(json.dumps(x,indent=2)+'\n')

def build():
 d=read('PARENT_NOISE_CERTIFICATE.json');choices=read('PARENT_ACQUISITION_CHOICES.json')
 trade=read('PARENT_TRADEOFF_CERTIFICATE.json');fit=read('PARENT_FITTED_CERTIFICATE.json')
 six=read('PARENT_SIX_RATIO_CERTIFICATE.json')
 modal=d['modal_blocks'];budget=d['budgets']['restricted_pass_contract']
 P=next(p for p in d['protocols'] if p['M']==4096)
 row=next(s for s in P['models']['restricted_pass_contract']['samples'] if s['delta_exponent']==-20)
 assert row['guaranteed_retained_count']==1893
 b2=f(row['beta_squared_upper']);B=bound(a(b2).sqrt(),True);epsilon=B/4096
 ell=min(f(c['modal_positive_sigma_squared_lower']) for c in modal)
 uu=max(f(c['modal_sigma_squared_upper']) for c in modal)
 s2=f(P['frame_low'])**2*ell;t2=f(P['frame_high'])**2*uu
 assert B*B>=b2 and s2>=16*B*B
 lower=bound(a(s2).sqrt()-a(B+epsilon),False)
 upper=bound(a(t2).sqrt()+a(B+epsilon),True)
 assert upper/lower<2029 and lower>2*B and B+epsilon<2*B
 X=np.load(ROOT/'sources'/'BASE_PREPARATIONS.npz',allow_pickle=False)
 S=X['numerator'];den=int(X['denominator'])
 assert S.shape==(2640,37) and S.dtype==np.int8 and den==52
 domain=b'UD-600cell-original-link-37-preparations-v0.1-2026-10-17'
 bits=np.unpackbits(np.frombuffer(hashlib.shake_256(domain).digest((S.size+7)//8),dtype=np.uint8),bitorder='little')[:S.size]
 assert np.array_equal(S,(2*bits.astype(np.int8)-1).reshape(2640,37))
 assert F(S.shape[0],den**2)==F(165,169)
 z=np.load(ROOT/'sources'/'OPERATORS.npz',allow_pickle=False)
 A=csr_matrix((z['A_data'],z['A_indices'],z['A_indptr']),shape=(2640,2640))
 assert A.nnz==14880 and np.all(np.abs(A.data)==1) and (A+A.T).nnz==0
 obs=z['obs'].tolist();assert len(obs)==62 and len(set(obs))==62
 def grade(i):return 0 if i<120 else 1 if i<840 else 2 if i<2040 else 3
 Q=[F(1),F(65,64),F(33,32),F(67,64)];c=F(33,32)
 ratio_centre=[pair(v) for g in range(1,4) for v in [c*Q[g]/Q[g-1],c*Q[g-1]/Q[g]]]
 assert six['ratio_order']==['D1','U1','D2','U2','D3','U3']
 assert ratio_centre==next(v['true_ratios'] for v in six['synthetic_round_trips'] if v['case']=='fitted_centre')
 with (ROOT/'CHANNEL_ORDER.csv').open('w',newline='') as file:
  w=csv.writer(file);w.writerow(['channel_zero_based','unique_simplex_index_zero_based','grade','raw_to_normalized_factor'])
  for j,i in enumerate(obs):w.writerow([j,i,grade(i),str(Q[grade(i)])])
 with (ROOT/'PREPARATION_ORDER.csv').open('w',newline='') as file:
  w=csv.writer(file);w.writerow(['preparation_zero_based','canonical_sign_column_sha256','normalization_denominator'])
  for j in range(37):w.writerow([j,digest(S[:,j].tobytes()),52])
 params=budget['parameters']
 units={
  'history_preparation':('normalized_state_l2',F(1,2**25)),
  'history_origin':('normalized_time',F(1,2**29)),
  'history_jitter':('normalized_time',F(1,2**29)),
  'history_instrument':('normalized_scalar_absolute',F(1,2**24)),
  'history_blank_correction':('normalized_scalar_absolute',F(1,2**25)),
  'history_processing':('normalized_scalar_absolute',F(1,2**26)),
  'history_quantization':('normalized_scalar_absolute',F(1,2**49)),
  'history_metric':('normalized_operator_l2',f(params['eta'])),
  'history_rate':('relative_native_rate_each',f(params['r'])),
  'history_readout':('normalized_operator_l2',f(params['rho'])),
  'history_extra_skew':('normalized_operator_l2',F(0)),
  'history_common_scale':('relative_common_rate',F(1,1024)),
  'diagnostic_response':('diagnostic_scalar_absolute',F(1,2**58)),
  'diagnostic_preparation':('diagnostic_state_l2',F(1,2**62)),
  'diagnostic_logger':('diagnostic_time',F(1,2**65)),
  'diagnostic_additive':('diagnostic_scalar_absolute',F(1,2**60)),
  'diagnostic_computation':('diagnostic_scalar_absolute',F(1,2**60)),
  'six_ratio_error':('six_ratio_l2',F(1,2**39)),
  'shape_statistic':('source_defined_relative_shape_statistic',F(1,2**38))}
 for k,unit in {
  'gain_preparation_observed_coefficient_infinity_error':'six_ratio_gain_preparation_linf',
  'gain_initial_reading_infinity_noise':'six_ratio_gain_noise_linf',
  'dynamic_combined_two_preparation_state_error_2norm':'six_ratio_combined_preparation_l2',
  'dynamic_six_scalar_raw_noise_2norm':'six_ratio_six_noise_l2',
  'per_run_logger_interval_total_error':'six_ratio_logger_time',
  'normalized_data_computation_error_2norm':'six_ratio_feature_computation_l2'}.items():
  units['six_'+k]=(unit,f(six['candidate_precision_contract'][k]))
 scalar=sum(units[k][1] for k in ['history_instrument','history_blank_correction','history_processing','history_quantization'])
 assert scalar<F(1,2**23) and 62*scalar**2<F(1,2**40)
 evidence={k:{'unit':unit,'upper_ceiling':pair(v),'comparison':'<' if k=='six_ratio_error' else '<='} for k,(unit,v) in units.items()}
 bindings={p.name:digest(p.read_bytes()) for p in sorted((ROOT/'sources').iterdir()) if p.is_file()}
 config={'id':'UD_ACQUISITION_CONTRACT_v0.1','status':'CONSTRUCTOR_FROZEN_PROPOSAL_BEFORE_DATA',
  'physical_promotion':0,'independent_review':'pending','lane':'development; no registry entry',
  'source_sha256':bindings,'preparation_order_sha256':digest((ROOT/'PREPARATION_ORDER.csv').read_bytes()),
  'channel_order_sha256':digest((ROOT/'CHANNEL_ORDER.csv').read_bytes()),
  'reference_transfer':{'status':'Explicit candidate centre, not an empirical fit or a physical unit bridge',
   'grade_Q':[pair(q) for q in Q],'common_c':pair(c),'raw_step':pair(1/(2*c)),
   'last_raw_time':pair(F(8190)/(2*c)),'raw_preparation_rule':'For gradeg, sign/(52*Q_g); normalizedX=S/52',
   'corrected_readout_rule':'Multiply raw selected channel by its gradeQ factor',
   'sufficient_raw_state_error_ceiling':pair(F(64,67)*F(1,2**25)),
   'sufficient_raw_origin_and_jitter_ceiling_each':pair(F(32,33)*F(1,2**29)),
   'SI_transfer':'OPEN; do not label normalized time as seconds or normalized output as volts'},
  'acquisition':{'M':4096,'preparations':37,'channels':62,'time_vectors_per_preparation':8191,
   'vector_records':303067,'scalar_readings':18790154,'normalized_step':[1,2],
   'normalized_last_time':[4095,1],'indexing':'Y[a,k,c], a=0..36,k=0..8190,c=0..61, C order',
   'missing_or_duplicate_samples':'HOLD; no interpolation, zero fill, adaptive rank fallback or sample deletion',
   'processing_rule':'Freeze calibration, raw-source hashes and processing implementation before analysis; preserve raw and corrected data'},
  'data_format':{'filename':'normalized_history.i64le','dtype':'<i8','shape':[37,8191,62],
   'scale':[1,2**48],'quantization':'round to nearest; ties to even; no clipping; error<=2^-49 per scalar',
   'bytes':18790154*8,
   'index_ledger':{'filename':'sample_index.csv','columns':['preparation_zero_based','time_zero_based','raw_record_id'],
    'rows':303067,'order':'Same a,k order as binary data; globally unique nonempty raw_record_id per62-vector',
    'timestamp_evidence':'Actual timestamps remain in the raw source, covered by origin and jitter receipts'},
   'dense_Hankel_shape':[253952,151552],
   'dense_Hankel_float64_bytes':253952*151552*8,'no_dense_allocation_in_checker':True},
  'diagnostic_encoding':{'separate_from_history':True,
   'reason':'History quantum2^-48 cannot meet diagnostic response error2^-58.',
   'format':'Exact arbitrary-precision integer numerators in decimal strings, denominator2^64; no binary64 or signedint64 conversion of the scaled integer',
   'rounding_error_per_scalar':[1,2**65],
   'quantization_budget':'Include2^-65 within the total diagnostic computation allowance2^-60; other computation errors must fit the remaining allowance.',
   'source':'PARENT_DIAGNOSTIC_REPLAY_PACKAGE.zip and PARENT_SIX_RATIO_CERTIFICATE.json; preserve their distinct stages'},
  'budgets':evidence,'history_vector_error_ceiling':[1,2**20],
  'sufficient_history_scalar_error_ceiling':[1,2**23],
  'calibration':{'six_ratio_error_strictly_below':[1,2**39],
   'shape_gate_ceiling':[1,2**38],'shape_gate_meaning':'Inherited source-defined shape statistic, not an arbitrary norm',
   'diagnostic_scalar_readings':493290,'six_ratio_scalar_readings':12,
   'six_ratio_order':six['ratio_order'],
   'six_ratio_reference_centre':ratio_centre,
   'six_ratio_protocol':six['finite_protocol'],
   'six_ratio_reference_is_not_parent_fit_array_order':True,
   'diagnostic_protocol':'Inherited m4,h=1/256,260 parity-separated codes,189 diagnostic outputs,two epochs plus blanks',
   'membership':'positive native rates; source-listed same-grade matching metric defects and local readout stencils; J=0',
   'future_stability':'Separate evidence over the full history acquisition required; two diagnostic epochs alone are insufficient'},
  'spectral_rule':{'normalization':[1,4096],'target_count':1893,'nominal_hidden_dimension':747,
   'data_Hankel_operator_error_ceiling':pair(B),'selection_threshold':pair(2*B),
   'numerical_operator_error_ceiling':pair(epsilon),
   'computed_sigma_1893_lower':pair(lower),'computed_sigma_1894_upper':pair(B+epsilon),
   'computed_sigma_1_upper':pair(upper),'retained_condition_number_strict_upper':2029,
   'numerical_proof_required':'Validated matrix-norm error for the computed Hankel/solver approximation, or directly verified singular-value enclosures. A floating SVD tolerance is insufficient.',
   'acceptance_scope':'A conditional finite observer signature; agreement does not identify hidden dynamics, the full plant or a physical law'},
  'known_reading_count_total':18790154+493290+12,
  'reading_count_exclusions':['additional metrology','independent held-out validation','extra blank or drift tracking','repeats and rejected runs'],
  'decision_order':['Bind frozen contract and independently review proposal','Check calibration, model-family and acquisition receipts','Verify complete hashed raw and corrected records','Obtain independently validated spectral enclosures','Evaluate frozen signature; retain all rejected and inconclusive runs'],
  'no_retroactive_tuning':'Rank target,window,preparations,channels,noise ceilings,calibration and analysis implementation must be fixed before data unblinding. Any revision creates a new version and a new run.',
  'open':['Independent review','Hardware/SI transfer','Apparatus data and bounded-error receipts','Validated large-matrix spectral computation adapter']}
 payload=canonical(config);(ROOT/'FROZEN_CONTRACT.json').write_bytes(payload)
 protocol_hash=digest(payload)
 template={'schema_version':1,'protocol_sha256':protocol_hash,'run_id':None,'acquisition_executed':False,
  'selected_target_count':1893,'started_utc':None,'completed_utc':None,'raw_source_sha256':None,
  'processing_implementation_sha256':None,'normalized_data_sha256':None,'sample_index_sha256':None,
  'review_receipt':None,'family_and_stability_receipt':None,
  'diagnostic_pass_receipt':None,'shape_gate_pass_receipt':None,'six_ratio_gate_receipt':None,
  'error_evidence':{k:{'unit':v['unit'],'reported_upper':None,'evidence_sha256':None,'method':None} for k,v in evidence.items()},
  'spectral_proof_receipt':None,'signature_evaluation':None}
 save('RUN_RECEIPT_TEMPLATE.json',template)
 proof={'status':'EXACT_RATIONAL_GATES_AND_INTERVAL_CONSTRUCTOR_CHECKED','physical_promotion':0,
  'independent_review':'pending','protocol_sha256':protocol_hash,
  'Hankel_error_squared_from_parent':pair(b2),'rounded_B_squared_dominates':B*B>=b2,
  'nominal_min_squared_lower':pair(s2),'nominal_max_squared_upper':pair(t2),
  'quarter_gap_squared_check':s2>=16*B*B,'computed_gap_above_threshold':lower>2*B,
  'computed_tail_below_threshold':B+epsilon<2*B,'computed_condition_upper_rational':pair(upper/lower),
  'computed_condition_below2029':upper/lower<2029,'scalar_component_sum':pair(scalar),
  'vector_error_squared_sufficient':pair(62*scalar**2),'preparation_SHAKE_design_matched':True,
  'A_skew_and_sparse_entries_checked':14880,'raw_data_generated':False,'normalized_dataset_generated':False}
 save('FREEZE_CERTIFICATE.json',proof)
 return config,proof
if __name__=='__main__':
 c,p=build();print(json.dumps({'protocol_sha256':p['protocol_sha256'],'history_readings':c['acquisition']['scalar_readings'],
 'known_total_readings':c['known_reading_count_total'],'data_bytes':c['data_format']['bytes'],
 'computed_condition_upper':float(f(p['computed_condition_upper_rational'])),'status':c['status']}))
