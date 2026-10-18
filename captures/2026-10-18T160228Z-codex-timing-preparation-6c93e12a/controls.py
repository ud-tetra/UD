"""Small exact controls and validated evaluations of analytic obstructions."""
import json
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,ctx
from proof_math import fm,up,down
ctx.prec=512

def controls():
 P=np.array([[1,1,0],[1,0,1],[1,-1,0],[1,0,-1]],dtype=object);R=np.array([[1,0,0],[0,0,1],[0,-1,0]],dtype=object)
 assert np.array_equal(R.T@R,np.eye(3,dtype=object));assert fm(P).rank()==fm(np.c_[P,P@R]).rank()==3
 boundary=np.diag([1,1,0]).astype(object);specific=np.array([[1,0,0],[0,1,-1],[0,0,0]],dtype=object)
 assert fm(P@boundary).rank()==fm(P@specific).rank()==2
 jitter=P.copy();jitter[3]=P[0];diff=jitter-P;squared=sum(int(x)**2 for x in diff.flat);assert squared==2 and arb(squared)<arb.pi()**2/4
 aliases=[]
 for m in [1,2,16,1024]:
  integer_defect=max(abs(acb(0,2*arb.pi()*m*k).exp()-1) for k in range(5));ratio=acb(0,arb.pi()).exp();assert integer_defect<arb(2)**-400 and abs(ratio+1)<arb(2)**-400 and abs(ratio-1)>arb(1999)/1000
  aliases.append({'alias_index':m,'jitter':[1,2*m],'integer_sample_defect_upper':up(integer_defect.upper()),'perturbed_discrepancy_lower':[1999,1000],'exact_symbolic_perturbed_discrepancy':2})
 theta=arb.pi()/3;rate=arb(1)/1000;defect=max(abs(acb(0,theta*(1+rate)*k).exp()-acb(0,((1+rate)*theta)*k).exp()) for k in range(17));assert defect<arb(2)**-400
 return {'status':'PASS','physical_promotion':0,'common_offset':{'quarter_turn_coefficient_rotation':R.tolist(),'joint_span_rank':3,'orthogonal':True},'excitation_boundary':{'coefficient_matrix':boundary.tolist(),'rank':2,'strict_margin_required':True},'preparation_specific_offsets':{'coefficient_matrix':specific.tolist(),'rank':2,'unconditional_rank_preservation_refuted':True},'single_row_jitter':{'exact_residual_norm_squared':2,'derivative_bound_squared_upper':up(arb.pi()**2/4)},'alias_jitter_family':aliases,'clock_rate_confounding':{'relative_rate':[1,1000],'finite_checked_samples':17,'difference_upper':up(defect.upper()),'exact_identity':'theta*(1+rate)*k == ((1+rate)*theta)*k for every k'},'finite_controls_are_not_the_general_proof':True}
if __name__=='__main__':
 from bindings import P,check
 check();out=P/'CONTROL_RESULTS.json';assert not out.exists();out.write_text(json.dumps(controls(),indent=2));print('All exact finite controls and validated no-go evaluations PASS')
