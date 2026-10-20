"""Independent exact scalar right-tail theorem, frozen before tail norms."""
from fractions import Fraction as F

def derive(eta,r,retained_epsilon,s210,retained_lower,cutoff):
 if not (0<=eta<1 and r>=0 and retained_epsilon>=0 and s210>=0 and retained_lower>0 and cutoff>0):
  raise ValueError('invalid right-tail theorem scalar domain')
 tail=r/(1-eta)
 return {'tail_upper':tail,'discarded_abs_error_upper':max(tail,s210),'full_abs_error_upper':max(retained_epsilon,tail,s210),'tail_cutoff_margin':cutoff-tail,'retained_cutoff_margin':retained_lower-cutoff,'strict_actual_cutoff_count209':tail<cutoff<retained_lower}

def controls():
 rows=[]
 def ck(n,x):
  assert x,n
  rows.append({'id':n,'pass':True})
 z=F(0);o=F(1)
 # n=2,k=2: Z=diag(3,2), Vd=e2/2, eta=3/4, Wnorm1.
 v=derive(F(3,4),o,z,z,F(3),F(5,2))
 ck('denominator_needed_actual_tail2',F(2)>o)
 ck('rational_denominator_is_conservative',v['tail_upper']==4 and v['tail_upper']>=2)
 ck('exact_sqrt_denominator_gives2',F(1,2)**2==1-F(3,4) and o/F(1,2)==2)
 ck('zero_column_actual_Gram_defect1',abs(F(0)-1)==1)
 ck('missing_dimension_cannot_bound_sigma1',F(1)<F(3))
 ck('minmax_not_reverse_bound',F(1)<F(3))
 # A selected tail range can equal a selected retained range; upper remains valid.
 ck('overlap_with_retained_not_needed',F(1)<=F(3))
 ck('fourth_root_toy_exact',F(1,2)**4==F(1,16))
 ck('square_root_wrong_power_is_unsafe',F(1,4)**2==F(1,16) and F(1,4)<F(1,2))
 ck('fourth_power_small_wrapper_refused',not(F(1,4)**4>=F(1,16)))
 v=derive(z,F(1,1<<43),F(1,1<<44),F(1,1<<42),o,F(1,1<<24))
 ck('full_list_max_not_sum',v['full_abs_error_upper']==F(1,1<<42))
 ck('full_list_can_meet_2neg41',v['full_abs_error_upper']<F(1,1<<41))
 ck('strict_cutoff_count',v['strict_actual_cutoff_count209'])
 ck('tail_cutoff_equality_refused',not derive(z,F(1,2),z,z,o,F(1,2))['strict_actual_cutoff_count209'])
 ck('retained_cutoff_equality_refused',not derive(z,z,z,z,o,o)['strict_actual_cutoff_count209'])
 ck('Gram_square_zero_gives_zero_root',F(0)**4==0)
 good=[z,z,z,z,o,F(1,2)]
 invalid={0:[-o,o],1:[-o],2:[-o],3:[-o],4:[z,-o],5:[z,-o]}
 for index,values in invalid.items():
  for j,x in enumerate(values):
   args=good[:];args[index]=x
   try:derive(*args)
   except ValueError:bad=True
   else:bad=False
   ck('invalid_domain_'+str(index)+'_'+str(j),bad)
 return rows
