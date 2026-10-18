import unittest,json
from pathlib import Path
from fractions import Fraction as F
from phase_math import bound
P=Path(__file__).resolve().parent
class PhaseTests(unittest.TestCase):
 def setUp(self):self.c=json.loads((P/'PHASE_STABILITY_CERTIFICATE.json').read_text())['constants']
 def test_full_ball_has_no_matching_certificate(self):
  self.assertFalse(bound(F(1,2**20),self.c)['unique_phase_matching'])
 def test_certified_grid_transition(self):
  self.assertTrue(bound(F(1,2**27),self.c)['unique_phase_matching'])
  self.assertFalse(bound(F(1,2**26),self.c)['unique_phase_matching'])
 def test_zero_perturbation_is_matching(self):
  self.assertTrue(bound(F(0),self.c)['unique_phase_matching'])
 def test_unresolved_subspace_is_hold(self):
  self.assertEqual(bound(F(1),self.c)['status'],'HOLD_SUBSPACE_BOUND')
 def test_no_separation_cannot_claim_matching(self):
  c=self.c.copy();c['minimum_chord_separation_lower']=[0,1]
  self.assertFalse(bound(F(1,2**27),c)['unique_phase_matching'])
 def test_invalid_delta_is_rejected(self):
  with self.assertRaises(AssertionError):bound(F(-1),self.c)
if __name__=='__main__':unittest.main()
