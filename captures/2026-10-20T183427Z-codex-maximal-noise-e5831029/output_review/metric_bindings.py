"""Independent advertised-metric enclosure checks; no estimator or fitting calls.
Exact residual identities do not alone prove that an advertised norm upper is
outward. Bind the original phase gate metrics to the actual saved arrays.
"""
from fractions import Fraction as F
import numpy as np

def encloses_squared_norm(advertised,squared):
 bound=F(int(advertised[0]),int(advertised[1]));value=F(int(squared[0]),int(squared[1]))
 return bound>=0 and value>=0 and bound*bound>=value

def argument_within(value,bound):
 # value and bound are validated Arb intervals; indeterminate comparisons HOLD.
 return bool(value<=bound)

def validate(case,result,phase_audit,m):
 phase=result['phase'];metrics=phase['metrics']
 assert encloses_squared_norm(metrics['inverse_residual'],phase_audit['inverse_residual_squared']),'advertised inverse-residual metric is not an outward enclosure'
 assert encloses_squared_norm(metrics['eigenpair_residual'],phase_audit['eigenpair_residual_squared']),'advertised eigenpair-residual metric is not an outward enclosure'
 assert m.frac(metrics['proposed_inverse_norm'])>=m.frac(phase_audit['inverse_norm_upper']),'advertised inverse norm underreports independent upper'
 with np.load(case/'PHASE_META.npz',allow_pickle=False)as z:values=z['eigenvalues']
 with np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False)as z:emissions=z['two_step_phase']
 lr,li,bits=m.cx(values);bound=m.aa(metrics['emitted_argument_error'])
 assert bound>=0
 for j in range(209):
  val=m.acb(m.aa(F(int(lr[j,0]),1<<bits)),m.aa(F(int(li[j,0]),1<<bits)))
  assert abs(val)>0
  theta=m.aa(F(int(emissions[j]),1<<60));actual=m.circular(val.arg()-theta)
  assert argument_within(actual,bound),'actual saved emitted argument outside advertised metric at index'+str(j)
 return {'status':'PASS_INDEPENDENT_ADVERTISED_PHASE_METRIC_ENCLOSURES','exact_squared_residuals_bound_to_advertised_norms':True,'inverse_norm_bound_independently_checked':True,'actual_argument_errors_compared_to_advertised_bound':209,'argument_comparison':'Validated Arb actual circular argument error <= advertised exact dyadic bound; no rounding tolerance or fallback','metric_caps_unchanged':True,'new_estimator_calls':0}

def controls(m):
 rows=[]
 def ck(name,value):
  assert value,name;rows.append({'id':name,'pass':True})
 ck('squared_norm_exact_boundary_accepted',encloses_squared_norm([3,2],[9,4]))
 ck('inverse_metric_underreport_rejected',not encloses_squared_norm([3,2],[10,4]))
 ck('eigen_metric_zero_underreport_rejected',not encloses_squared_norm([0,1],[1,1<<100]))
 ck('negative_advertised_norm_rejected',not encloses_squared_norm([-1,1],[1,1]))
 ck('negative_exact_square_rejected',not encloses_squared_norm([1,1],[-1,1]))
 ck('outward_larger_norm_accepted',encloses_squared_norm([2,1],[9,4]))
 ck('validated_argument_bound_accepted',argument_within(m.aa([1,8]),m.aa([1,4])))
 ck('argument_underreport_rejected',not argument_within(m.aa([1,8]),m.aa([1,16])))
 ck('argument_indeterminate_interval_rejected',not argument_within(m.arb('0.125 +/- 0.01'),m.aa([1,8])))
 return rows
