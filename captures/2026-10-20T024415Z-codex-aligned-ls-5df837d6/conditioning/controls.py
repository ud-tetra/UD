"""Synthetic exact geometry and premise controls; no actual grid or source data."""
from fractions import Fraction as F
from pathlib import Path
import tempfile,json
import condition as m

def main():
 rows=[]
 def ck(k,v):m.req(v,k);rows.append({'id':k,'pass':True})
 def reject(k,fn):
  try:fn()
  except ValueError:rows.append({'id':k,'pass':True});return
  raise ValueError('negative control accepted '+k)
 c={k:F(0)for k in ('etaU','etaV','eta0','rho','rhoD','xi','sA','eV','a','r','delta0','singular_floor_debit','lag0','LJ')};c.update(C=F(1),h=F(1),hD0=F(1),dD=F(1),M0=F(1),s0=F(2),tail0=F(0),cutoff=F(1),beta=F(1),sep=F(1),quantum=F(1,4))
 z=m.evaluate(F(0),c);ck('zero_perturbation_zero_errors_certified',z['status']=='CERTIFIED_CONDITIONAL_GAUGE_ALIGNED_REGION')
 ck('sign_gauge_projectors_equal_factor_distance_two',F(1)**2==F(-1)**2 and abs(F(1)-F(-1))==2)
 cosine,sine=F(3,5),F(4,5);ck('principal_angle_projector_eigenvalue_squared',sine*sine==1-cosine*cosine)
 ck('Procrustes_stable_identity_squared',2-2*cosine==sine*sine*2/(1+cosine))
 reject('negative_extra_input',lambda:m.evaluate(F(-1),c))
 bad=dict(c,etaU=F(1));reject('Gram_defect_one',lambda:m.evaluate(F(0),bad))
 bad=dict(c,rho=F(1));reject('inverse_residual_one',lambda:m.evaluate(F(0),bad))
 bad=dict(c,C=F(0));reject('zero_projection_multiplier',lambda:m.evaluate(F(0),bad))
 ck('nonpositive_proposed_floor_HOLD',m.evaluate(F(2),c)['status']=='HOLD_POSITIVE_PROPOSED_FLOOR')
 ck('cutoff_touch_not_exact_rank_certified',not m.evaluate(F(1),c)['exact_order_209_at_cutoff'])
 small=m.evaluate(F(1,16),c);ck('nonzero_conditioning_record',small['readable_projector_upper']>0)
 ck('raw_ball_below_quantum_is_zero_only',small['additional_encoded_ball_only_zero'])
 ck('raw_quantum_boundary_not_zero_only',not m.evaluate(F(1,4),c)['additional_encoded_ball_only_zero'])
 # Matrix identity with noncommuting R=diag(2,1), T=[[0,1],[0,0]].
 R=[[F(2),F(0)],[F(0),F(1)]];Ri=[[F(1,2),F(0)],[F(0),F(1)]];T=[[F(0),F(1)],[F(0),F(0)]]
 def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(2))for j in range(2)]for i in range(2)]
 ck('polar_similarity_cannot_be_omitted',mm(mm(R,T),Ri)==[[0,2],[0,0]]and mm(mm(R,T),Ri)!=T)
 for n,p in [('package',m.P),('descendant',m.P/'bad'),('ancestor',m.P.parent)]:reject('guard_'+n,lambda p=p:m.guard(p))
 with tempfile.TemporaryDirectory()as td:
  p=Path(td);(p/'link').symlink_to(m.P,target_is_directory=True);reject('guard_symlink',lambda:m.guard(p/'link'/'bad'))
 print(json.dumps({'status':'PASS_PURE_GEOMETRY_PREMISE_CUSTODY_CONTROLS','checks':rows,'new_estimator_calls':0,'actual_conditioning_grid_evaluated':False},indent=2))
if __name__=='__main__':main()
