import copy
import unittest
from compare_replay import compare
class ComparatorTests(unittest.TestCase):
    def setUp(self):
        self.a={'carrier':{'betti':[1,1,0,0],'readout':'3'},'preparation':{'states':[1,2,3]},
                'relaxation':{'lambda2_graph':0.16125498724045675,'sampled':[{'step':1000,'residual':0.0022513920946935465}]},'physics_promotion':0}
    def test_identical(self):
        stats=compare(self.a,copy.deepcopy(self.a))
        self.assertEqual(stats['numerical_fields'],2)
    def test_numerical_drift_admitted(self):
        b=copy.deepcopy(self.a);b['relaxation']['lambda2_graph']+=1e-12
        b['relaxation']['sampled'][0]['residual']+=1e-12
        self.assertEqual(compare(self.a,b)['numerical_fields'],2)
    def test_large_numeric_drift_rejected(self):
        b=copy.deepcopy(self.a);b['relaxation']['lambda2_graph']+=1e-3
        with self.assertRaises(AssertionError):compare(self.a,b)
    def test_exact_betti_mismatch_rejected(self):
        b=copy.deepcopy(self.a);b['carrier']['betti'][1]=0
        with self.assertRaises(AssertionError):compare(self.a,b)
    def test_reordered_schedule_rejected(self):
        b=copy.deepcopy(self.a);b['preparation']['states']=[1,3,2]
        with self.assertRaises(AssertionError):compare(self.a,b)
    def test_type_mismatch_rejected(self):
        b=copy.deepcopy(self.a);b['carrier']['readout']=3
        with self.assertRaises(AssertionError):compare(self.a,b)
    def test_nan_rejected(self):
        b=copy.deepcopy(self.a);b['relaxation']['lambda2_graph']=float('nan')
        with self.assertRaises(AssertionError):compare(self.a,b)
    def test_extra_field_rejected(self):
        b=copy.deepcopy(self.a);b['relaxation']['new']=1
        with self.assertRaises(AssertionError):compare(self.a,b)
if __name__=='__main__':unittest.main(verbosity=2)
