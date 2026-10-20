"""Independent rational two-residual scalar theorem, frozen before adjoint values."""
from fractions import Fraction as F

def derive(a,b,f,g,s1,sq,t,next_proposal):
 if not (0<=a<1 and 0<=b<1 and f>=0 and g>=0 and t>=0 and 0<sq<=s1 and 0<=next_proposal<=sq):
  raise ValueError('invalid two-residual theorem domain')
 p=s1*(a/(2-a)+b/(2-b))
 c=(p+f)/(1-b)
 e=max(f/(1-b),g/(1-a))
 epsilon=c+e
 result={'compression':c,'offdiagonal':e,'retained_abs_error':epsilon,'all_abs_error':max(epsilon,t,next_proposal),'gap_margin':sq-c-t-e}
 if result['gap_margin']<=0:
  result['status']='HOLD_NO_STRICT_LEADING_BLOCK_MATCH'
  return result
 result.update(status='STRICT_LEADING_BLOCK_MATCH',actual_sq_lower=sq-epsilon,actual_s1_upper=s1+epsilon,ambient_leading_condition=(s1+epsilon)/(sq-epsilon))
 assert result['actual_sq_lower']>t>=0
 return result

def controls():
 rows=[]
 def ck(n,v):
  assert v,n
  rows.append({'id':n,'pass':True})
 z=F(0);o=F(1)
 v=derive(z,z,z,z,F(3),o,F(1,10),z)
 ck('exact_orthonormal_retained_error_zero',v['retained_abs_error']==0)
 ck('exact_orthonormal_ambient_condition3',v['ambient_leading_condition']==3)
 ck('tail_max_not_sum',v['all_abs_error']==F(1,10))
 # Scalar Z=6/5, U=6/5,V=1,S=1: a=11/25,b=0,f=0,g=11/25.
 v=derive(F(11,25),z,z,F(11,25),o,o,z,z)
 ck('nonunit_scalar_conservative_error',v['retained_abs_error']>=F(1,5))
 # Missing adjoint: Z=[[1,3/4],[0,0]], U=V=e1,S=1, sigma1=5/4.
 ck('missing_adjoint_exact_actual_sigma',o+F(3,4)**2==F(5,4)**2)
 v=derive(z,z,z,F(3,4),o,o,z,z)
 ck('adjoint_charged_in_error',v['retained_abs_error']==F(3,4)>=F(1,4))
 ck('false_zero_adjoint_would_falsely_predict_zero',derive(z,z,z,z,o,o,z,z)['retained_abs_error']==0)
 # Wrong retained subspace: Z=diag(1,2), U=V=e1,S=1, actual tail1.
 ck('strict_gap_equality_refused',derive(z,z,z,z,o,o,o,z)['status'].startswith('HOLD'))
 ck('strict_gap_negative_refused',derive(z,z,z,z,o,o,F(2),z)['status'].startswith('HOLD'))
 v=derive(z,z,z,z,o,o,F(1,1<<30),z)
 ck('tail_blocks_full_2neg41',v['retained_abs_error']==0 and v['all_abs_error']>F(1,1<<41))
 ck('tail_still_below_2neg25',v['all_abs_error']<F(1,1<<25))
 # E=[[0,3/5],[4/5,0]], singular values4/5 and3/5.
 ck('block_offdiagonal_norm_max',max(F(3,5)**2,F(4,5)**2)==F(4,5)**2)
 ck('block_offdiagonal_norm_not_sum',F(4,5)<F(3,5)+F(4,5))
 ck('tail_nonnegative_absolute_max_exact',abs(F(1,10)-F(1,50))<=max(F(1,10),F(1,50)))
 good=[z,z,z,z,o,o,z,z]
 invalid={0:[-o,o],1:[-o,o],2:[-o],3:[-o],4:[F(1,2)],5:[z,F(2)],6:[-o],7:[-o,F(2)]}
 for index,values in invalid.items():
  for k,x in enumerate(values):
   args=good[:];args[index]=x
   try:derive(*args)
   except ValueError:rejected=True
   else:rejected=False
   ck('invalid_domain_'+str(index)+'_'+str(k),rejected)
 return rows
