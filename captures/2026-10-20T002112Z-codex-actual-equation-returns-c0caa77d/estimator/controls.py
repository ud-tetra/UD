"""Frozen non-fit arithmetic, implication and output-guard controls."""
import argparse,json,os,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from common import P,freeze,repo,external_output,write_new
import certify

def run():
 freeze();rows=[]
 def check(name,actual,expected):
  assert actual==expected,(name,actual,expected);rows.append({'id':name,'pass':True})
 check('exact_dyadic_identity_Gram',certify.gram_squared(np.eye(2,dtype=object)*8,3),F(0))
 check('exact_dyadic_nonorthogonal_Gram',certify.gram_squared(np.array([[8,0],[0,4]],dtype=object),3),F(9,16))
 A=certify.fm([[24,0],[0,8]]);V=certify.fm([[8],[0]]);U=certify.fm([[8],[0]]);Sigma=24
 check('retained_equation_zero_with_nonzero_tail',certify.squared_norm(A*V-U*Sigma,6),F(0))
 check('nonzero_equation_exact_scaling',certify.squared_norm(certify.fm([[1],[-2]]),3),F(5,64))
 check('raw_lag_exact_scaling',certify.squared_norm(certify.fm([[3],[-4]]),4),F(25,256))
 for name,path in [('self',P),('descendant',P/'invalid'),('ancestor',P.parent)]:
  try:external_output(path);got=False
  except RuntimeError:got=True
  check('guard_'+name,got,True)
 with tempfile.TemporaryDirectory(prefix='ud-guard-control-')as td:
  q=Path(td)/'alias';q.symlink_to(P,target_is_directory=True)
  try:external_output(q/'bad');got=False
  except RuntimeError:got=True
  check('guard_symlink_descendant',got,True)
 m,c,C=certify.inherited_equation();inherited=m.controls(repo(),c,C);check('all_inherited_equation_controls',inherited['status'],'PASS_SIXTEEN_CONTROLS')
 freeze();return {'status':'PASS_FROZEN_NON_FIT_CONTROLS','rows':rows,'inherited':inherited,'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
 q=argparse.ArgumentParser();q.add_argument('--repo',required=True);q.add_argument('--out',required=True);a=q.parse_args();os.environ['UD_REPO']=str(Path(a.repo).resolve());out=external_output(a.out);out.mkdir(parents=True,exist_ok=False);write_new(out/'CONTROLS.json',run())
