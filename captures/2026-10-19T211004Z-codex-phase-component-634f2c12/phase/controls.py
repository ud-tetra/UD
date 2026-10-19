"""Frozen matcher/permutation/encoding controls, not new estimator outputs."""
import json
import numpy as np
from flint import arb
from common import P,freeze,up
from phase import match_emissions,target_setup,emitted_integer,op
from numeric_math import complex_residual,cmul
from proof_math import fm
def run():
    freeze();setup=target_setup()
    with np.load(P/'inputs/PARENT_EMISSION.npz',allow_pickle=False) as z:old=z['two_step_phase'].copy()
    recipes=[('old_saved_positive',old.copy(),True),('old_shift_stationary',old.copy(),False),('old_duplicate_emission',old.copy(),False),('old_permuted_order',old.copy(),True)]
    recipes[1][1][0]+=1<<40;recipes[2][1][1]=recipes[2][1][0];recipes[3][1][[0,1]]=recipes[3][1][[1,0]];rows=[]
    for name,values,want in recipes:
        result=match_emissions(values,setup);got=result['status']=='CERTIFIED_FINITE_EMITTED_TWO_STEP_BIJECTION';assert got==want
        rows.append({'id':name,'expected_match':want,'actual_match':got,'status':result['status']})
    for name,angle,want in [('positive_half_even',2.**-61,0),('positive_three_halves',3*2.**-61,2),('negative_three_halves',-3*2.**-61,-2),('negative_half_even',-2.**-61,0)]:
        got=emitted_integer(angle);assert got==want;rows.append({'id':name,'expected_integer':want,'actual_integer':got})
    eye=np.eye(2,dtype=object);zero=np.zeros((2,2),dtype=object);rho,rho2=complex_residual(cmul(fm(eye),fm(zero),fm(zero),fm(zero)),0,(fm(eye),fm(zero)),0);assert rho>1
    rows.append({'id':'zero_inverse_refusal','inverse_residual_F_upper':up(rho),'exact_residual_squared':[str(x) for x in rho2],'exceeds_unit_invertibility_margin':True})
    ident=op(eye,zero,0);assert ident==arb(1);rows.append({'id':'identity_inverse_norm','operator_norm_upper':up(ident)})
    result={'status':'PASS_TEN_FROZEN_MATCH_ENCODING_AND_COMPLEX_ARITHMETIC_CONTROLS','rows':rows,'scope':'Old source positive/mutation/permutation controls and exact tiny arithmetic controls; none is a new four-case estimator output or fit. All main outputs retained separately.','new_estimator_SVD_alignment_fits':0,'physical_promotion':0};p=P/'CONTROLS.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'controls':len(rows)}),flush=True)
if __name__=='__main__':run()
