from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json,hashlib
pair=lambda x:[x.numerator,x.denominator]
tau=Q(5,2)**41/factorial(41)/(1-Q(5,84))
r0=Q(52,2**104); rounding=120*r0; cap=4096
local=tau*cap+rounding
accum=4096*local
fwd=accum+Q(504,2**96); adj=accum+Q(52,2**96)
terms=[Q(5,2)**k/factorial(k) for k in range(41)]
max_term=max(terms)
term_norm=4*cap+3*r0
row_int_bound=24*term_norm*2**104
sum_norm=13*cap+rounding
sum_int_bound=sum_norm*2**104
checks={
 'tau_lt_2^-110':tau<Q(1,2**110),
 'coefficient_max_25_over_8':max_term==Q(25,8),
 'polynomial_abs_sum_lt_13':sum(terms)<13,
 'all_partial_row_accumulators_lt_2^123':row_int_bound<2**123,
 'all_partial_output_sums_lt_2^121':sum_int_bound<2**121,
 'accum_lt_1':accum<1,
 'forward_lt_2^-68':fwd<Q(1,2**68),
 'adjoint_lt_2^-68':adj<Q(1,2**68),
 'forward_lt_2^-79':fwd<Q(1,2**79),
 'adjoint_lt_2^-79':adj<Q(1,2**79),
 'state_bootstrap_2050_lt_cap':2050<cap,
 'input96_domain2049_lt_2^108':2049*2**96<2**108,
 'shifted_input104_domain2049_lt_2^116':2049*2**104<2**116,
}
assert all(checks.values()),checks
result={'status':'PASS','checks':checks,'exact':{k:pair(v) for k,v in {'tau':tau,'coordinate_vector_rounding':r0,'step_rounding':rounding,'local_cap_error':local,'accumulated_error':accum,'forward_error':fwd,'adjoint_error':adj,'term_norm':term_norm,'row_integer_bound':row_int_bound,'sum_norm':sum_norm,'sum_integer_bound':sum_int_bound}.items()},'display_only':{'forward_error':float(fwd),'adjoint_error':float(adj),'row_integer_log2_upper':123,'sum_integer_log2_upper':121},'scope':'mathematical sufficient bounds; not an implementation or physical attestation','physical_promotion':0}
Path(__file__).with_name('BOUND_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'forward':float(fwd),'adjoint':float(adj)}))
