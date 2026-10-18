import unittest
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,ctx,fmpq
from make_records import phase_matrix,timing,mul,Q,SHAPE,evaluation_bounds,rounded
ctx.prec=512
class TimingTests(unittest.TestCase):
 def test_recurrence_waveform_sign_scale_and_layout(self):
  e={'origin':'alternating_quarter','rate':[1,1<<20],'jitter':[1,16]};theta=np.arange(1,53,dtype=np.int64)*(1<<52)
  for a in [0,1,18,36]:
   ph=phase_matrix(theta,e,a,count=23)
   for k in [0,1,2,22]:
    o,eps,u=timing(e,a,k);t=o+(1+eps)*k+u
    for j in [0,17,51]:
     ang=arb(int(theta[j]))*arb(fmpq(t.numerator,t.denominator))/(1<<60);z=acb(0,ang).exp()
     self.assertTrue(abs(z.real-arb(int(ph[k,2*j+1]))/(1<<60))<arb(1)/(1<<60));self.assertTrue(abs(z.imag-arb(int(ph[k,2*j+2]))/(1<<60))<arb(1)/(1<<60))
 def test_long_recurrence_endpoint(self):
  e={'origin':'ramp_half','rate':[1,1<<20],'jitter':[1,16]};theta=np.array([731*(1<<49)],np.int64);a=36;ph=phase_matrix(theta,e,a);k=8190;o,eps,u=timing(e,a,k);t=o+(1+eps)*k+u;z=acb(0,arb(int(theta[0]))*arb(fmpq(t.numerator,t.denominator))/(1<<60)).exp()
  self.assertTrue(abs(z.real-arb(int(ph[k,1]))/(1<<60))<arb(1)/(1<<60));self.assertTrue(abs(z.imag-arb(int(ph[k,2]))/(1<<60))<arb(1)/(1<<60))
 def test_rounding_ties_even_negative(self):
  self.assertEqual([rounded(n,1) for n in [-5,-3,-1,1,3,5]],[-2,-2,0,0,2,2])
 def test_timing_budget_and_dependence(self):
  e={'origin':'ramp_half','rate':[1,1<<48],'jitter':[1,1<<34]}
  for a in range(37):
   for k in [0,1,8190]:
    o,eps,u=timing(e,a,k);self.assertLessEqual(abs(o),F(1,2));self.assertEqual(abs(eps),F(1,1<<48));self.assertEqual(abs(u),F(1,1<<34))
 def test_complex_product_and_quantization(self):
  self.assertEqual(mul((0,Q),(0,Q)),(-Q,0));self.assertEqual(mul((Q,0),(Q,0)),(Q,0));self.assertEqual(int(np.prod(SHAPE))*8,150321232)
 def test_uniform_phase_error_analytic_bound(self):
  # Anchor complex error<=2^-95; per-step error<=2^-94.
  # (1+2^-95)^8191 <2 by binomial/geometric series since8191*2^-95<1/2.
  e=F(2*(2*8191+1),1<<95);self.assertLess(e,F(1,1<<79))
  # One jitter multiplication adds at most(2+e)*2^-95+round2^-95.
  total=e+(3+e)*F(1,1<<95)+F(1,1<<61);self.assertLess(total,F(1,1<<60))
if __name__=='__main__':unittest.main()
