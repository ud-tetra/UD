import numpy as np
from fractions import Fraction as F
from flint import arb,ctx
from proof_math import fm,up
from operator_bounds import gram_norm
ctx.prec=512

def controls():
 P=np.array([[1,1,0],[1,0,1],[1,-1,0],[1,0,-1]],dtype=object);R=np.array([[1,0,0],[0,0,1],[0,-1,0]],dtype=object)
 assert np.array_equal(R.T@R,np.eye(3,dtype=object)) and fm(np.c_[P,P@R]).rank()==3
 coeff=np.array([[1,0,0],[0,1,-1],[0,0,0]],dtype=object);assert fm(P@coeff).rank()==2
 E=np.array([[0,0],[1,0],[0,1]],dtype=object);rot=np.array([[0,0],[1,1],[0,0]],dtype=object);n0,_=gram_norm(E,0);n1,receipt=gram_norm(rot,0);assert n0==1 and F(*receipt['chosen_squared_bound'])==2 and fm(rot.T@rot).rank()==1
 assert np.array_equal(P@R,np.roll(P,-1,axis=0));B=np.array([[2],[3],[5]],dtype=object);assert np.array_equal(P@R@B,np.roll(P,-1,axis=0)@B)
 raw=np.zeros((4,2),dtype=object);raw[3]=[1,1];squared=sum(int(x)**2 for x in raw.flat);assert squared==2 and arb(squared)<2*(arb.pi()/2)**2
 return {'status':'PASS','physical_promotion':0,'families':[{'name':'common_origin_preserves_span','exact_joint_rank':3,'orthogonal_rotation':R.tolist()},{'name':'preparation_specific_origin_loses_rank','exact_coefficient_matrix':coeff.tolist(),'exact_temporal_rank':2},{'name':'global_preparation_norm_not_invariant','squared_operator_norm_before':1,'squared_operator_norm_after':2,'each_preparation_column_norm_preserved':True},{'name':'forward_rotation_sign','exact_waveform_identity_verified':True},{'name':'correlated_preparation_jitter','exact_raw_residual_squared_norm':2,'derivative_squared_bound_upper':up(2*(arb.pi()/2)**2),'independence_assumption':False}],'finite_controls_do_not_replace_general_proof':True}
if __name__=='__main__':
 import json
 from bindings import P,check
 check();out=P/'CONTROL_RESULTS.json';assert not out.exists();out.write_text(json.dumps(controls(),indent=2));print('All five exact/validated control families PASS')
