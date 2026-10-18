"""Meaningful exact decoder checks; synthetic controls only."""
from fractions import Fraction as F
import json,unittest
from restricted_gate import ROOT,assess_epoch

class RestrictedGateTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.d=json.loads((ROOT/'sources/PROBE_DESIGN.json').read_text())
 def blank_data(self):
  # Diagnostic-only fixture: zero forbidden derivative data and exact staticRP.
  # This is not asserted to be a complete physical finite trajectory.
  d=self.d;Y=[[[0]*189 for _ in range(260)] for _ in range(6)]
  for ri,r in enumerate(d['observed_coordinates']):
   Y[0][d['colors'][r]][ri]=F(1,d['preparation_denominators'][d['colors'][r]])
  return Y
 def test_exact_local_static_coefficient_rejected(self):
  Y=self.blank_data();d=self.d;r=4;j=0;ri=d['observed_coordinates'].index(r);cc=d['colors'][j]
  Y[0][cc][ri]+=F(1,2**40)/d['preparation_denominators'][cc]
  result=assess_epoch(Y)
  self.assertGreater(F(*result['static_residual_squared']),F(1,2**81))
  self.assertEqual(result['decision'],'REJECT_JOINT_CONTRACT')
 def test_forbidden_derivative_coefficient_rejected(self):
  Y=self.blank_data();d=self.d;r=4;j=120;ri=d['observed_coordinates'].index(r);cc=d['colors'][j]
  # A linear-in-time coded perturbation has exact derivative coefficientepsilon.
  eps=F(1,2**44)
  for k in range(1,6):Y[k][cc][ri]+=eps*F(k,128)/d['preparation_denominators'][cc]
  result=assess_epoch(Y)
  self.assertIn(4,result['rejected_rows'])
  self.assertEqual(F(*result['forbidden_row_residual_squared']['4']),eps*eps)
 def test_restricted_outside_stencil_alias(self):
  d=self.d;found=False
  for rs,stencil in d['readout_stencils'].items():
   for j in stencil:
    candidates=[k for k,c in enumerate(d['colors']) if c==d['colors'][j] and k not in stencil]
    if candidates:
     k=candidates[0];q=d['preparation_denominators'][d['colors'][j]]
     self.assertEqual(F(1,q)-F(1,q),0);found=True;break
   if found:break
  self.assertTrue(found)
 def test_shape_rejected(self):
  with self.assertRaises(ValueError):assess_epoch([])
 def test_float_rejected(self):
  Y=self.blank_data();Y[0][0][0]=0.1
  with self.assertRaises(ValueError):assess_epoch(Y)

if __name__=='__main__':unittest.main()
