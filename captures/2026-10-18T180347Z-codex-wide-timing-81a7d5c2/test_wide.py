import unittest,json
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,ctx,fmpq
from model import sketch,rules,source_tail
from bindings import P
ctx.prec=512
class WideTests(unittest.TestCase):
 def test_original_prefix_and_nested_norms(self):
  A=sketch();old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
  self.assertTrue(np.array_equal(A[:,:160],2*old));self.assertEqual(rules(161)['sketch_Frobenius_squared'],F(371097,4096));self.assertLess(rules(161)['sketch_Frobenius_squared'],rules(257)['sketch_Frobenius_squared']);self.assertLess(rules(257)['scaled'],rules(321)['scaled'])
 def test_scaled_threshold_noise_ratio_preserved(self):
  old=rules(161)
  for m in [161,257,321]:self.assertEqual(rules(m)['scaled']/rules(m)['additive_vector_noise_squared'],old['scaled']/old['additive_vector_noise_squared'])
 def test_sideband_identity_and_two_step(self):
  theta=arb(fmpq(3,7));mu=arb(1)/(1<<20);j=arb(1)/16
  for s in [-1,1]:
   w=(1+s*mu)*theta
   for k in [0,1,7,18]:
    sign=(-1)**k;g=acb(0,w*k+s*theta*j*sign).exp();main=acb(0,w*k).exp();side=main*sign
    decomposed=(theta*j).cos()*main+acb(0,s*(theta*j).sin())*side
    self.assertTrue(abs(g-decomposed)<arb(1)/(1<<400));nextg=acb(0,w*(k+2)+s*theta*j*sign).exp();self.assertTrue(abs(nextg-acb(0,2*w).exp()*g)<arb(1)/(1<<400))
 def test_source_error_floor_small(self):
  self.assertEqual(1+2*52*2,209);self.assertEqual(1+2*52*4,417)
  for m in [161,257,321]:self.assertLess(source_tail(m),rules(m)['common'])
 def test_polar_residual_bound_on_exact_model(self):
  # Exact orthogonal proposal gives zero correction; corruption is detectable.
  from proof_math import fm,arr,norm_exact
  q=np.eye(3,dtype=object)*(1<<60);eta=norm_exact(arr(fm(q).transpose()*fm(q))-np.eye(3,dtype=object)*(1<<120),120);self.assertTrue(eta==0)
  q[0,0]*=2;bad=norm_exact(arr(fm(q).transpose()*fm(q))-np.eye(3,dtype=object)*(1<<120),120);self.assertTrue(bad>=1)
if __name__=='__main__':unittest.main()
