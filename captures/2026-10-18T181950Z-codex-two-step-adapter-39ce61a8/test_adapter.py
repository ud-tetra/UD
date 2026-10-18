import unittest
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,ctx
from reference import phase,mul,Q,rounded
from sketch import sketch
from certify import complex_op,real_op
ctx.prec=512
class AdapterTests(unittest.TestCase):
 def test_original_prefix_and_new_width(self):
  a=sketch();old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);self.assertEqual(a.shape,(2294,321));self.assertTrue(np.array_equal(a[:,:160],2*old))
 def test_two_step_closes_jitter_and_alias_remains(self):
  w=arb(3)/7;j=arb(1)/16
  for k in [0,1,7]:
   g=acb(0,w*k+j*(-1)**k).exp();n=acb(0,w*(k+2)+j*(-1)**k).exp();self.assertTrue(abs(n-acb(0,2*w).exp()*g)<arb(1)/(1<<400));self.assertTrue(abs(acb(0,2*(w+arb.pi())).exp()-acb(0,2*w).exp())<arb(1)/(1<<400))
 def test_complex_operator_bound_contains_known_norm(self):
  r=np.array([[3,0],[0,0]],object);i=np.array([[4,0],[0,0]],object);self.assertTrue(complex_op(r,i,0)>=5);self.assertTrue(complex_op(r,i,0)<arb(5001)/1000)
 def test_rotation_intertwining_sign(self):
  w=arb(3)/7;phase0=arb(1)/5;c=(2*w).cos();s=(2*w).sin();x=phase0.cos();y=phase0.sin();self.assertTrue(abs(x*c-y*s-(phase0+2*w).cos())<arb(1)/(1<<400));self.assertTrue(abs(x*s+y*c-(phase0+2*w).sin())<arb(1)/(1<<400))
 def test_rounding_and_integer_feedback(self):
  self.assertEqual([rounded(n,1) for n in [-5,-3,-1,1,3,5]],[-2,-2,0,0,2,2]);self.assertEqual(mul((0,Q),(0,Q)),(-Q,0))
 def test_source_and_instrument_thresholds_differ(self):
  self.assertLess(F(1034,10**13),F(1,1<<24));self.assertLess(F(1,1<<24),F(1,1000));self.assertGreater(F(1,100),F(1,1<<24))
if __name__=='__main__':unittest.main()
