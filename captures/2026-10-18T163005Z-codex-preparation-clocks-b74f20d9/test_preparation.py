import unittest
from fractions import Fraction as F
import numpy as np
from flint import arb,ctx
from source_model import rotate
from controls import controls
from prep_math import budget
ctx.prec=512
class PreparationTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c={'time_rows':4,'temporal_order':3,'frame_Gram_lower':[1,1],'frame_Gram_upper':[1,1],'minimum_chord_separation_lower':[1,1],'noise_transfer_squared':[1,1],'reference_model_sketch_residual_upper':[0,1]};cls.m={'baseline_gamma_lower':[1,1],'sketch_norm_upper':[1,1],'Omega_upper':[2,1],'offset_multiplier_upper':[1,1],'per_preparation_Lipschitz_upper':[[1,1]]*37}
 def test_rotation_sign_and_channel_preparation_interleaving(self):
  t=np.full(52,2**60,np.int64);B=np.zeros((105,2294),np.int64);B[1,[0,1,37]]=2**60;offsets=[[0,1]]*37;offsets[0]=[1,1];Bo,c,s=rotate(t,B,offsets)
  self.assertEqual(Bo[1,0],int(c[0,0])*2**60);self.assertEqual(Bo[2,0],-int(s[0,0])*2**60);self.assertEqual(Bo[1,37],Bo[1,0]);self.assertEqual(Bo[1,1],2**120);self.assertEqual(Bo[2,1],0)
 def test_common_origin_control(self):self.assertEqual(controls()['families'][0]['exact_joint_rank'],3)
 def test_differential_rank_loss(self):self.assertEqual(controls()['families'][1]['exact_temporal_rank'],2)
 def test_global_operator_norm_can_increase(self):self.assertEqual(controls()['families'][2]['squared_operator_norm_after'],2)
 def test_zero_error_with_offset_margin_certifies(self):self.assertTrue(budget(self.c,self.m,F(1,16),F(1,4),0,0,0,model_floor=False)['unique_phase_matching'])
 def test_large_box_refuses(self):self.assertEqual(budget(self.c,self.m,1,F(1,4),0,0,0)['status'],'HOLD_EXCITATION_MARGIN')
 def test_case_specific_margin_separate_from_box(self):self.assertTrue(budget(self.c,self.m,1,F(1,4),0,0,0,profile_gamma=[1,1],model_floor=False)['unique_phase_matching'])
 def test_preparation_slope_aggregation(self):
  a=budget(self.c,self.m,0,0,F(1,1000000),0,0);m={**self.m,'per_preparation_Lipschitz_upper':[[1,1]]+[[0,1]]*36};b=budget(self.c,m,0,0,F(1,1000000),0,0);self.assertGreater(F(*a['timing_sketch_error_upper']),F(*b['timing_sketch_error_upper']))
 def test_strict_preparation_fraction_refuses(self):self.assertEqual(budget(self.c,self.m,0,1,0,0,0)['status'],'HOLD_EXCITATION_MARGIN')
 def test_negative_clock_input_refuses(self):
  with self.assertRaises(AssertionError):budget(self.c,self.m,0,0,-F(1,10),0,0)
if __name__=='__main__':unittest.main()
