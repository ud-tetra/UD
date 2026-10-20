"""Frozen synthetic exact normal/scaling/rank/guard controls; no saved-data calls."""
import argparse,json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import certify as c

def run():
 rows=[]
 def check(n,x,y):
  c.require(x==y,'control failed '+n);rows.append({'id':n,'pass':True})
 A=np.array([[3],[4]],dtype=object);B=np.array([[7],[1]],dtype=object);T=np.array([[5]],dtype=object);G,N,bG,bN=c.normal_witness(A,B,T,2,3)
 check('exact_Gram_scaled',F(int(G[0,0]),1<<bG),F(25,16));check('exact_normal_scaled',F(int(N[0,0]),1<<bN),F(-75,128))
 check('normal_expression_wrong_sign_rejected',int(N[0,0])==75,False);check('normal_expression_wrong_single_scale_rejected',F(int(N[0,0]),1<<(2+3))==F(-75,128),False)
 q=c.summarize(G,N,bG,bN);check('full_rank_positive_floor',q['status'],'CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE');check('exact_scalar_LS_distance',F(*map(int,q['LS_step_operator_distance_upper'])),F(3,8))
 A=np.array([[1],[0]],dtype=object);B=np.array([[2],[1]],dtype=object);T=np.array([[2]],dtype=object);G,N,bG,bN=c.normal_witness(A,B,T,0,0);q=c.summarize(G,N,bG,bN)
 check('zero_normal_nonzero_lag',int(N[0,0])==0 and np.any(A@T-B),True);check('zero_normal_exact_LS_distance',q['LS_step_operator_distance_upper'],['0','1'])
 Z=c.fm([[0]]);check('rank_deficiency_refused',c.summarize(Z,Z,0,0)['status'],'HOLD_NO_POSITIVE_FULL_COLUMN_RANK_FLOOR')
 for name,p in [('self',c.P),('descendant',c.P/'bad'),('ancestor',c.P.parent)]:
  try:c.guard(p);got=False
  except ValueError:got=True
  check('output_guard_'+name,got,True)
 with tempfile.TemporaryDirectory(prefix='ud-LS-guard-')as td:
  p=Path(td)/'alias';p.symlink_to(c.P,target_is_directory=True)
  try:c.guard(p/'bad');got=False
  except ValueError:got=True
  check('output_guard_symlink',got,True)
 return {'status':'PASS_FROZEN_SYNTHETIC_LS_CONTROLS','rows':rows,'new_estimator_calls':0,'new_saved_data_normal_computations':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();c.bindings(Path(a.repo).resolve());out=c.guard(a.out);out.mkdir(parents=True,exist_ok=False);r=run();c.bindings(Path(a.repo).resolve())
 with(out/'CONTROLS.json').open('x')as f:json.dump(r,f,indent=2);f.write('\n')
