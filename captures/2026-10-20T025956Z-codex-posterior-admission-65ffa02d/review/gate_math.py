"""Independent exact admission predicates and synthetic adversarial controls.
These predicates do not verify matrices or admit fresh unpinned bundles.
"""
import re
from fractions import Fraction as F
KEYS=('etaU','etaV','xi','sA','rho','h','eV','a')
def integer(x):
 if type(x)is int:return x
 if type(x)is str and re.fullmatch(r'-?(0|[1-9][0-9]*)',x):return int(x)
 raise ValueError('exact integer or canonical integer string required')
def rational(p):
 if type(p)not in (list,tuple)or len(p)!=2:raise ValueError('two-part rational required')
 n,d=map(integer,p)
 if d<=0:raise ValueError('strictly positive denominator required')
 return F(n,d)
def pair(v):return [str(v.numerator),str(v.denominator)]
def conjunction(m,caps,floor,smin,LSnormal,LSfloor,LSdistance,radius,phase_error,half,indices,encoding,source_identity,lag_kind,fresh=False):
 if fresh:return {'admissible':False,'reason':'HOLD_FRESH_UNVERIFIED_BUNDLE'}
 try:
  values={k:rational(m[k])for k in KEYS};limits={k:rational(caps[k])for k in KEYS};lo,sm,n,g,e,R,ang,h=map(rational,[floor,smin,LSnormal,LSfloor,LSdistance,radius,phase_error,half])
 except (ValueError,TypeError,KeyError,OverflowError):return {'admissible':False,'reason':'HOLD_SCHEMA_OR_MISSING_METRIC'}
 gates={k:0<=values[k]<=limits[k]and limits[k]>0 for k in KEYS};gates.update(positive_singular_floor=lo>0 and sm>=lo,LS_positive_floor=g>0,LS_finite_nonnegative=n>=0 and e>=0,LS_conservative_quotient=g>0 and e*g>=n,strict_phase_disks=0<=R<1 and R<h and h>0,strict_phase_angle=0<=ang<h,finite209_bijection=type(indices)is list and len(indices)==209 and all(type(x)is int for x in indices)and set(indices)==set(range(209)),encoding=encoding is True,source_identity=source_identity is True,preselected_lag_kind=lag_kind=='Gram_Frobenius')
 return {'admissible':all(gates.values()),'gates':gates}

def controls():
 rows=[]
 def ck(k,v):assert v,k;rows.append({'id':k,'pass':True})
 m={k:[1,8]for k in KEYS};c={k:[1,4]for k in KEYS};base=dict(m=m,caps=c,floor=[1,2],smin=[1,1],LSnormal=[1,8],LSfloor=[1,2],LSdistance=[1,4],radius=[1,8],phase_error=[1,8],half=[1,4],indices=list(range(209)),encoding=True,source_identity=True,lag_kind='Gram_Frobenius')
 ck('all_valid_synthetic_conjunction',conjunction(**base)['admissible'])
 def modified(**changes):b=dict(base);b.update(changes);return conjunction(**b)
 exact=dict(m);exact['xi']=[1,4];ck('nonstrict_cap_equality',modified(m=exact)['admissible'])
 over=dict(m);over['xi']=[257,1024];ck('overcap_rejected_despite_other_passes',not modified(m=over)['admissible'])
 negative=dict(m);negative['xi']=[-1,8];ck('negative_upper_refused',not modified(m=negative)['admissible'])
 missing=dict(m);del missing['xi'];ck('missing_gate_refused',not modified(m=missing)['admissible'])
 bad=dict(m);bad['xi']=[1,0];ck('zero_denominator_refused',not modified(m=bad)['admissible'])
 bad=dict(m);bad['xi']=[True,8];ck('boolean_integer_refused',not modified(m=bad)['admissible'])
 bad=dict(m);bad['xi']=[1.5,8];ck('float_rational_refused',not modified(m=bad)['admissible'])
 bad=dict(m);bad['xi']=['NaN','8'];ck('nonfinite_string_refused',not modified(m=bad)['admissible'])
 ck('nonpositive_singular_floor_refused',not modified(floor=[0,1])['admissible'])
 ck('LS_nonpositive_floor_refused',not modified(LSfloor=[0,1])['admissible'])
 ck('LS_underreported_distance_refused',not modified(LSdistance=[1,8])['admissible'])
 ck('strict_phase_angle_equality_refused',not modified(phase_error=[1,4])['admissible'])
 ck('strict_phase_disk_equality_refused',not modified(radius=[1,4])['admissible'])
 ck('duplicate_targets_refused',not modified(indices=[0]*209)['admissible'])
 ck('wrong_target_count_refused',not modified(indices=list(range(208)))['admissible'])
 ck('source_record_or_factor_mismatch_refused',not modified(source_identity=False)['admissible'])
 ck('wrong_lag_bound_kind_refused',not modified(lag_kind='raw_Frobenius')['admissible'])
 ck('foreign_fresh_allpass_still_HOLD',modified(fresh=True)['reason']=='HOLD_FRESH_UNVERIFIED_BUNDLE')
 ck('exact_LS_quotient_boundary_allowed',modified(LSdistance=[1,4])['admissible'])
 return rows
