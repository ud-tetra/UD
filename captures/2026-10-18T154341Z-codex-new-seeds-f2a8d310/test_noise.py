import unittest
import numpy as np
from make_records import block_metrics
class NoiseTests(unittest.TestCase):
 def test_dense_sufficient_scalar_bound(self):
  m,s=block_metrics(np.full((2,62),2**25,dtype=np.int64));self.assertEqual(s,62*2**50);self.assertLessEqual(s,2**56);self.assertEqual(m,2**25)
 def test_vector_boundary_is_not_scalar_admission(self):
  a=np.zeros((1,62),np.int64);a[0,0]=2**28;m,s=block_metrics(a);self.assertEqual(s,2**56);self.assertGreater(m,2**25)
 def test_large_integer_square_never_wraps(self):
  m,s=block_metrics(np.full((1,62),2**40,dtype=np.int64));self.assertEqual(s,62*2**80);self.assertGreater(s,2**63)
 def test_one_integer_above_vector_boundary(self):
  a=np.zeros((1,62),np.int64);a[0,0]=2**28+1;_,s=block_metrics(a);self.assertGreater(s,2**56)
 def test_scalar_and_vector_status_distinct(self):
  m,s=block_metrics(np.full((1,62),2**25+1,dtype=np.int64));self.assertGreater(m,2**25);self.assertLess(s,2**56)
if __name__=='__main__':unittest.main()
