import unittest
from fractions import Fraction as F
from math import isqrt
from residual_preflight import residual_preflight

class ExactGateTests(unittest.TestCase):
    def test_strict_boundary(self):
        self.assertEqual(residual_preflight(F(1,4),0,F(1,2))['status'],'CONTINUE_FULL_VERIFIER')
        self.assertEqual(residual_preflight(F(1,4)+F(1,2**20),0,F(1,2))['status'],'EARLY_HOLD')
        self.assertEqual(residual_preflight(F(1,4)-F(1,2**20),0,F(1,2))['status'],'CONTINUE_FULL_VERIFIER')
    def test_phase_correction_and_equality(self):
        # e=48/2^120; dyadic residual=1/2. True residual lower=1/2-e.
        e=F(48,2**120)
        self.assertEqual(residual_preflight(F(1,4),1,F(1,2)-e)['status'],'CONTINUE_FULL_VERIFIER')
        self.assertEqual(residual_preflight(F(1,4),1,F(1,2)-2*e)['status'],'EARLY_HOLD')
    def test_sqrt_floor_bracket(self):
        for x in [F(0),F(1,3),F(2),F(10**80+17,2**200)]:
            r=residual_preflight(x,0,F(1),bits=100)
            l=F(*r['dyadic_phase_residual_lower']);h=l+F(1,2**100)
            self.assertLessEqual(l*l,x);self.assertGreater(h*h,x)
    def test_conservative_near_boundary(self):
        # An increment below sqrt-floor resolution continues, never false HOLD.
        self.assertEqual(residual_preflight(F(1,4)+F(1,2**250),0,F(1,2))['status'],'CONTINUE_FULL_VERIFIER')
    def test_large_phase_error_continues(self):
        self.assertEqual(residual_preflight(F(1,4),2**120,F(1,4))['status'],'CONTINUE_FULL_VERIFIER')
    def test_invalid_inputs(self):
        for args in [(F(-1),0,F(1)),(F(0),-1,F(1)),(F(0),0,F(0))]:
            with self.assertRaises(ValueError):residual_preflight(*args)
    def test_exact_phase_dimension_bound(self):
        self.assertLess(37*62,48**2)

if __name__=='__main__':unittest.main()
