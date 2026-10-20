"""Prospective pure recipe/arithmetic/custody controls, no raw and no estimator."""
import argparse,json,os,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from common import P,repo,freeze,need,guard,write_new
import records,exact_math as e

def run():
 freeze();rows=[]
 def check(n,x,y):need(x==y,'control '+n);rows.append({'id':n,'pass':True})
 w,chosen=records.weights();check('one_coefficient_per_preparation',np.all(np.count_nonzero(w.reshape(62,37),axis=0)==1),True);check('unit_integer_norm_every_preparation',np.all(np.sum(w.reshape(62,37)**2,axis=0)==1),True)
 v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974))
 check('fixed_negation_selected_signs',all(int(w[37*c+p])==(-1 if int(v[37*c+p])>=0 else 1)for p,c in enumerate(chosen)),True);check('one_quantum_inside_frozen_ball',F(1,1<<96)<=F(3,1<<49)**2,True)
 G,Gamma,N,rawsq=e.matrices(np.array([[3],[4],[7]],dtype=object),np.array([[5]],dtype=object),2,3);check('lag_integer_Gram_scaling',F(int(G[0,0]),1<<10),F(1681,1024));check('LS_Gram_scaling',F(int(Gamma[0,0]),1<<4),F(9,16));check('LS_normal_scaling',F(int(N[0,0]),1<<7),F(-123,128));check('wrong_normal_sign_refused',int(N[0,0])==123,False);check('wrong_normal_denominator_refused',F(int(N[0,0]),1<<5)==F(-123,128),False)
 lag,ls=e.matrix_bounds(G,Gamma,N,2,3);check('fixed_Gram_Frobenius_route',lag['route'],'PRESELECTED_GRAM_FROBENIUS_ONLY');distance=e.fraction(ls['LS_step_operator_distance_upper']);check('scalar_outward_LS_distance',F(41,24)<=distance<F(41,24)+F(1,1<<179),True)
 Z=e.fm([[0]]);_,ls=e.matrix_bounds(Z,Z,Z,0,0);check('deficient_rank_HOLD',ls['status'],'HOLD_NO_POSITIVE_LS_GRAM_FLOOR')
 Aeq=e.fm([[3,0],[0,1]]);ueq=e.fm([[1],[0]]);check('zero_retained_equation_nonzero_tail',e.sqnorm(Aeq*ueq-ueq*3,0)==0 and int(Aeq[1,1])==1,True)
 # A=[1,0]^T, B=[2,1]^T, T=2 is exactly LS despite nonzero lag.
 A=e.fm([[1],[0]]);B=e.fm([[2],[1]]);T=e.fm([[2]]);D=A*T-B;check('zero_normal_nonzero_lag',A.transpose()*D==e.fm([[0]])and e.sqnorm(D,0)>0,True)
 for name,p in [('self',P),('descendant',P/'bad'),('ancestor',P.parent)]:
  try:guard(p);got=False
  except ValueError:got=True
  check('guard_'+name,got,True)
 with tempfile.TemporaryDirectory(prefix='ud-fresh-guard-')as td:
  p=Path(td)/'alias';p.symlink_to(P,target_is_directory=True)
  try:guard(p/'bad');got=False
  except ValueError:got=True
  check('guard_symlink',got,True)
 freeze();return {'status':'PASS_PROSPECTIVE_PURE_CONTROLS','rows':rows,'new_raw_records':0,'new_estimator_calls':0,'actual_new_output_checks':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);q=p.parse_args();os.environ['UD_REPO']=str(Path(q.repo).resolve());out=guard(q.out);out.mkdir(parents=True,exist_ok=False);write_new(out/'CONTROLS.json',run())
