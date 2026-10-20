"""Pure synthetic rational controls; no actual saved factor or source metadata is opened."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,tempfile
import certify_v0_2 as c

def main():
 rows=[]
 def ck(k,v):c.req(v,k);rows.append({'id':k,'pass':True})
 def reject(k,fn):
  try:fn()
  except ValueError:rows.append({'id':k,'pass':True});return
  raise ValueError('negative control accepted '+k)
 C={k:F(0)for k in ('etaU','etaV','xi','ell','eV','rho','a')};C.update(U=F(1),V=F(1),T=F(1),W=F(1),Z=F(3),Sigma=F(3),smin=F(2),h=F(1))
 e=F(1,16);env=c.envelopes(C,e,e,e,e);worst={k:F(0)for k in ('etaU','etaV','xi','sA','eV')}
 for du,dv,ds,dt in product((-e,e),repeat=4):
  actual={'etaU':abs((1+du)**2-1),'etaV':abs((1+dv)**2-1),'xi':max(abs(z*(1+dv)-(1+du)*(z+ds))for z in (F(2),F(3))),'sA':abs((1+du)-(1+du)*(1+dt)),'eV':abs(dt)}
  for k,v in actual.items():worst[k]=max(worst[k],v);c.req(v<=env[k],'synthetic bound fails '+k)
 ck('sixteen_signed_diagonal_tuples_obey_all_five_envelopes',all(worst[k]<=env[k]for k in worst))
 ck('Gram_quadratic_term_required',env['etaU']==2*e+e*e and env['etaU']>2*e)
 ck('equation_cross_term_required',env['xi']==7*e+e*e)
 ck('lag_cross_term_required',env['sA']==3*e+e*e)
 ck('eigenpair_proposal_fixed_residual_change',env['eV']==e)
 ck('diagonal_minimum_floor_debit',env['proposed_smin']==2-e)
 ck('fixed_inverse_argument_metrics_unchanged',all(env[k]==C[k]for k in ('rho','h','a')))
 reject('negative_U_radius',lambda:c.envelopes(C,-e,e,e,e))
 reject('negative_V_radius',lambda:c.envelopes(C,e,-e,e,e))
 reject('negative_Sigma_radius',lambda:c.envelopes(C,e,e,-e,e))
 reject('negative_T_radius',lambda:c.envelopes(C,e,e,e,-e))
 zero=c.envelopes(C,F(0),F(0),F(0),F(0));ck('zero_box_recovers_source_bounds',zero['xi']==C['xi']and zero['sA']==C['ell'])
 small=c.envelopes(C,e/2,e/2,e/2,e/2);ck('all_increasing_bounds_monotone',all(small[k]<=env[k]for k in worst)and small['proposed_smin']>=env['proposed_smin'])
 ck('lag_exact_boundary_vs_double_radius',F(1,4)**2+3*F(1,4)==F(13,16)and F(1,2)**2+3*F(1,2)>F(13,16))
 for name,p in [('package',c.P),('descendant',c.P/'bad'),('ancestor',c.P.parent)]:reject('protected_'+name,lambda p=p:c.guard(p))
 with tempfile.TemporaryDirectory()as td:
  p=Path(td);(p/'link').symlink_to(c.P,target_is_directory=True);reject('protected_symlink',lambda:c.guard(p/'link'/'bad'));(p/'exists').mkdir();reject('existing_output',lambda:c.guard(p/'exists'))
 ck('empty_grid_retained_as_null_HOLD_selection',c.first_qualified([{'status':'HOLD_INSUFFICIENT_QUALITY_ENVELOPE'}],'status','CERTIFIED_WHOLE_TYPED_FACTOR_BOX') is None)
 print(json.dumps({'status':'PASS_PURE_SAVED_FACTOR_BOUND_AND_CUSTODY_CONTROLS','checks':rows,'actual_saved_factors_opened':False,'new_estimator_calls':0},indent=2))
if __name__=='__main__':main()
