import unittest
from fractions import Fraction as F
import numpy as np
from flint import arb
from noise_math import noise_upper
from reference import rounded
class NoiseTests(unittest.TestCase):
 def test_vector_gate_exact_max_amp(self):
  self.assertEqual(F(62*(1<<25)**2,1<<96)/F(1,1<<40),F(31,32))
 def test_amplitude_squared_int64_safe(self):
  a=np.ones((1,62),np.int64)*(1<<25);self.assertEqual(int(np.sum(a*a,dtype=np.int64)),62*(1<<50));self.assertLess(62*(1<<50),1<<63)
 def test_small_Gram_operator_upper_and_scaling(self):
  g=np.eye(321,dtype=object)*4;one=noise_upper(g,1);two=noise_upper(g,2);self.assertTrue(one>0);self.assertTrue(abs(two-2*one)<arb(1)/(1<<400));self.assertTrue(one>=arb(2)/(1<<55))
 def test_dc_lies_in_stationary_span(self):
  x=np.arange(6,dtype=object).reshape(1,6);D=np.ones((7,1),dtype=object)@x
  self.assertTrue(np.array_equal(D[1:],D[:-1]))
 def test_quantum_and_uniform_order_scale_distinct(self):
  self.assertLess(F(1,1<<48),F(1,1<<37));self.assertLess(F(1,1<<37),F(1,1<<20))
 def test_rounding_signed_ties(self):self.assertEqual([rounded(n,1) for n in [-5,-3,-1,1,3,5]],[-2,-2,0,0,2,2])
if __name__=='__main__':unittest.main()
