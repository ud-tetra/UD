"""Independent direct-tail reanchor; old nominal-tail/source-L not accuracy inputs."""
from fractions import Fraction as F

def derive(a,b,forward,adjoint,s1,sq,eta,r,s210,cutoff,source_L=None):
 if not (0<=a<1 and 0<=b<1 and forward>=0 and adjoint>=0 and 0<sq<=s1 and 0<=eta<1 and r>=0 and 0<=s210<=sq and cutoff>0):
  raise ValueError('invalid direct-tail reanchor scalar domain')
 tail=r/(1-eta)
 c=(s1*(a/(2-a)+b/(2-b))+forward)/(1-b)
 e=max(forward/(1-b),adjoint/(1-a))
 epsilon=c+e;gap=sq-c-tail-e
 answer={'direct_tail_upper':tail,'compression_upper':c,'offdiagonal_upper':e,'retained_abs_error_upper':epsilon,'new_matching_gap':gap}
 if gap<=0:
  answer['status']='HOLD_NO_DIRECT_TAIL_RETAINED_MATCH'
  return answer
 lower=sq-epsilon
 assert lower>tail>=0
 answer.update(status='DIRECT_TAIL_RETAINED_MATCH',ambient_sigma209_lower=lower,ambient_sigma1_upper=s1+epsilon,ambient_leading_condition_upper=(s1+epsilon)/lower,discarded_abs_error_upper=max(tail,s210),full321_abs_error_upper=max(epsilon,tail,s210),tail_cutoff_margin=cutoff-tail,retained_cutoff_margin=lower-cutoff,strict_actual_cutoff_count209=tail<cutoff<lower)
 if source_L is not None:
  answer['original_proposal_floor_margin']=sq-source_L+F(1,2**41)
  answer['original_proposal_floor_comparison']=answer['original_proposal_floor_margin']>=0
 return answer

def controls():
 rows=[]
 def ck(n,b):
  assert b,n
  rows.append({'id':n,'pass':True})
 z=F(0);o=F(1)
 v=derive(z,z,z,z,F(3),o,z,z,z,F(1,2))
 ck('zero_residual_direct_match',v['status']=='DIRECT_TAIL_RETAINED_MATCH')
 ck('zero_tail_full_error0',v['full321_abs_error_upper']==0)
 ck('ambient_condition3',v['ambient_leading_condition_upper']==3)
 ck('strict_actual_cutoff_count',v['strict_actual_cutoff_count209'])
 ck('matching_equality_HOLD',derive(z,z,z,z,F(3),o,z,o,z,F(1,2))['status'].startswith('HOLD'))
 ck('matching_negative_HOLD',derive(z,z,z,z,F(3),o,z,F(2),z,F(1,2))['status'].startswith('HOLD'))
 a=derive(z,z,z,z,F(3),o,z,z,z,F(1,2),source_L=z)
 b=derive(z,z,z,z,F(3),o,z,z,z,F(1,2),source_L=F(100))
 ck('source_L_not_accuracy_premise',all(a[k]==b[k]for k in ['direct_tail_upper','retained_abs_error_upper','full321_abs_error_upper','ambient_leading_condition_upper','new_matching_gap']))
 ck('source_L_only_protocol_floor_comparison',a['original_proposal_floor_comparison'] and not b['original_proposal_floor_comparison'])
 v=derive(z,z,F(1,1<<46),F(1,1<<45),o,F(1,2),z,F(1,1<<44),F(1,1<<43),F(1,4))
 ck('nonzero_c_e_correct',v['compression_upper']==F(1,1<<46) and v['offdiagonal_upper']==F(1,1<<45))
 ck('new_tail_changes_gap_not_c_e',v['new_matching_gap']==F(1,2)-F(1,1<<46)-F(1,1<<45)-F(1,1<<44))
 ck('full_bound_max_saved_tail',v['full321_abs_error_upper']==F(1,1<<43))
 ck('finite_full321_can_pass_2neg41',v['full321_abs_error_upper']<F(1,1<<41))
 ck('cutoff_equality_refused',not derive(z,z,z,z,F(3),o,z,F(1,2),z,F(1,2))['strict_actual_cutoff_count209'])
 good=[z,z,z,z,F(3),o,z,z,z,F(1,2)]
 for i,x in [(0,o),(1,o),(2,-o),(3,-o),(4,F(1,2)),(5,z),(6,o),(7,-o),(8,-o),(8,F(2)),(9,z)]:
  args=good[:];args[i]=x
  try:derive(*args)
  except ValueError:bad=True
  else:bad=False
  ck('invalid_domain_'+str(i)+'_'+str(x),bad)
 return rows
