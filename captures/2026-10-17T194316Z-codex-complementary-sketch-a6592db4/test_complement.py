import unittest
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np
from flint import fmpz_mat
from replay_sketch import load_case,replay_arrays
P=Path(__file__).resolve().parent
class ComplementTests(unittest.TestCase):
 def test_exact_rank_increment_and_response(self):
  v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],dtype=np.int64),(0,1974))
  W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
  self.assertTrue(np.all(v@W==0));self.assertEqual(int(v@v),16228)
  self.assertNotEqual(int(fmpz_mat(W[:160].tolist()).det()),0)
  self.assertEqual(F(int(v@v),128),F(4057,32))
 def test_nonorthogonal_factor_is_refused(self):
  gg,q,d,c,r=load_case(P/'results/sketch-clean-v1');q=q.copy();q[:,0]=0
  with self.assertRaises(AssertionError):replay_arrays(gg,q,d,c,r)
 def test_false_eigenvalue_is_refused(self):
  gg,q,d,c,r=load_case(P/'results/sketch-clean-v1');d=d.copy();d+=2**38
  with self.assertRaises(AssertionError):replay_arrays(gg,q,d,c,r)
 def test_altered_gram_is_refused(self):
  gg,q,d,c,r=load_case(P/'results/sketch-clean-v1');gg=gg.copy();gg[0,0]+=2**110
  with self.assertRaises(AssertionError):replay_arrays(gg,q,d,c,r)
if __name__=='__main__':unittest.main()
