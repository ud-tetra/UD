import unittest,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import ctx
from operator_bounds import gram_norm
from numeric_math import encode,assemble
ctx.prec=512
P=Path(__file__).resolve().parent
class OperatorTests(unittest.TestCase):
 def test_identity_is_operator_norm_not_frobenius(self):
  _,r=gram_norm(np.eye(3,dtype=object),0)
  self.assertEqual(F(*r['chosen_squared_bound']),1);self.assertEqual(F(*r['trace_squared_bound']),3)
 def test_rank_one_dense_norm(self):
  _,r=gram_norm(np.ones((3,2),dtype=object),0)
  self.assertEqual(F(*r['chosen_squared_bound']),6)
 def test_zero_and_dyadic_scale(self):
  _,r=gram_norm(np.zeros((4,2),dtype=object),7);self.assertEqual(F(*r['chosen_squared_bound']),0)
  _,r=gram_norm(np.diag([3,4]).astype(object),3);self.assertEqual(F(*r['chosen_squared_bound']),F(1,4))
 def test_exact_psd_bounds_and_frobenius_dominance(self):
  a=np.array([[2,-7,4],[0,8,-9],[11,-3,5]],dtype=object);_,r=gram_norm(a,4);g=a.T@a
  self.assertEqual(F(*r['trace_squared_bound']),F(sum(int(g[i,i]) for i in range(3)),256))
  self.assertEqual(F(*r['Gershgorin_squared_bound']),F(max(sum(abs(int(x)) for x in row) for row in g),256))
  self.assertLessEqual(F(*r['chosen_squared_bound']),F(*r['trace_squared_bound']))
 def test_exact_encoding_subnormal(self):
  a=np.array([0.1,float.fromhex('0x0.0000000000001p-1022')]);n,b=encode(a)
  for x,y in zip(a,n):self.assertEqual(F(int(y),1<<b),F(*float(x).as_integer_ratio()))
 def test_changed_shift_refuses_and_baseline_passes(self):
  m=json.loads((P/'inputs/ADAPTER_TEST_REFERENCE.json').read_text())['metrics'];c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];c['discovery_cutoff']=json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff']
  self.assertTrue(assemble(m,c)['unique_reference_phase_matching']);m['shift_residual_upper']=[1,10]
  with self.assertRaises(AssertionError):assemble(m,c)
if __name__=='__main__':unittest.main()
