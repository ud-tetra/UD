import unittest
from fractions import Fraction as F
import numpy as np
from flint import arb,ctx
from controls import controls
from calibration_math import budget
from operator_bounds import gram_norm
from proof_math import fm,arr
ctx.prec=512
class CalibrationTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c={'time_rows':4,'temporal_order':3,'frame_Gram_lower':[1,1],'frame_Gram_upper':[1,1],'minimum_chord_separation_lower':[1,1],'noise_transfer_squared':[1,1],'reference_model_sketch_residual_upper':[0,1]};cls.m={'coefficient_sigma_lower':[1,1],'coefficient_norm_upper':[1,1],'Omega_upper':[2,1]}
 def test_no_error_preserves_phase(self):self.assertTrue(budget(self.c,self.m,F(1,2),0,0,0)['unique_phase_matching'])
 def test_strict_preparation_margin(self):self.assertEqual(budget(self.c,self.m,1,0,0,0)['status'],'HOLD_EXCITATION_MARGIN')
 def test_large_jitter_refuses(self):self.assertFalse(budget(self.c,self.m,0,1,0,0)['unique_phase_matching'])
 def test_clock_rate_accumulates_in_time(self):
  a=budget(self.c,self.m,0,0,F(1,100000),0);b=budget(self.c,self.m,0,F(1,100000),0,0)
  self.assertGreater(F(*a['clock_error_vector_norm_upper']),F(*b['clock_error_vector_norm_upper']))
 def test_bad_inverse_residual_is_detected_exactly(self):
  C=np.array([[1,0,0],[0,1,0]],dtype=object);H=np.array([[1,0],[0,2],[0,0]],dtype=object);r=arr(fm(C)*fm(H)-fm(np.eye(2,dtype=object)));rho,_=gram_norm(r,0);self.assertTrue(rho>=1)
 def test_valid_inverse_margin(self):
  C=np.array([[2,0,0],[0,2,0]],dtype=object);H=np.array([[1,0],[0,1],[0,0]],dtype=object);r=arr(fm(C)*fm(H)-2*fm(np.eye(2,dtype=object)));rho,_=gram_norm(r,1);h,_=gram_norm(H,1);self.assertTrue(rho==0);self.assertTrue((1-rho)/h==2)
 def test_exact_controls(self):self.assertEqual(controls()['status'],'PASS')
 def test_negative_protocol_input_refuses(self):
  with self.assertRaises(AssertionError):budget(self.c,self.m,0,-F(1,1000),0,0)
if __name__=='__main__':unittest.main()
