"""Pure small-matrix tests; no actual saved factors are opened."""
import json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat
import certify as c

def main():
 rows=[]
 def check(k,v):c.require(v,k);rows.append({'id':k,'pass':True})
 def reject(k,fn):
  try:fn()
  except ValueError:rows.append({'id':k,'pass':True});return
  raise ValueError('negative control accepted '+k)
 D=fmpz_mat([[1,0],[0,1]]);G=D.transpose()*D
 q=c.bounds(G,0,F(1));check('operator_pass_despite_Frobenius_overcap',q['trace']==['2','1']and q['status']=='CERTIFIED_OPERATOR_NORM_AT_FIXED_CAP')
 check('exact_cap_equality_allowed',q['squared_cap_tests']['absolute_row_sum'])
 check('overcap_all_declared_bounds_HOLD',c.bounds(fmpz_mat([[4,0],[0,4]]),0,F(1))['status'].startswith('HOLD'))
 check('dyadic_scaling_exact',c.bounds(fmpz_mat([[4,0],[0,4]]),1,F(1))['absolute_row_sum']==['1','1'])
 reject('nonpositive_cap_refused',lambda:c.bounds(G,0,F(0)))
 reject('asymmetric_Gram_refused',lambda:c.bounds(fmpz_mat([[1,1],[0,1]]),0))
 reject('negative_diagonal_refused',lambda:c.bounds(fmpz_mat([[-1,0],[0,1]]),0))
 reject('positive_diagonal_indefinite_unbound_Gram_refused',lambda:c.gram_equal(fmpz_mat([[1,2],[2,1]]),G))
 reject('tampered_Gram_refused',lambda:c.gram_equal(fmpz_mat([[1,0],[0,2]]),G))
 x,b=c.decode(np.array([[-.5,.25]],dtype=np.float64));check('negative_and_fractional_decode',b==2 and x.tolist()==[[-2,1]])
 for name,dest in [('package',c.P),('descendant',c.P/'bad'),('ancestor',c.P.parent)]:reject('protected_'+name,lambda dest=dest:c.guard(dest))
 with tempfile.TemporaryDirectory()as td:
  p=Path(td);(p/'link').symlink_to(c.P,target_is_directory=True);reject('protected_symlink',lambda:c.guard(p/'link'/'bad'));(p/'existing').mkdir();reject('existing_output_refused',lambda:c.guard(p/'existing'))
 print(json.dumps({'status':'PASS_PURE_SMALL_MATRIX_AND_CUSTODY_CONTROLS','checks':rows,'actual_saved_factors_opened':False,'new_estimator_calls':0},indent=2))
if __name__=='__main__':main()
