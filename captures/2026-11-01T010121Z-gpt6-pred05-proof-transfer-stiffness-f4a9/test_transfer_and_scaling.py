import unittest
from verify_transfer_and_scaling import trial, scaling
from check_angular_cochain import check

class ProofAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials={n:trial(n) for n in (4,6,8,10)}
        cls.angular={n:check(n) for n in (4,6,8,10)}
    def test_tetrahedral_counts(self):
        for n,r in self.trials.items():
            self.assertEqual(r['states'][0]['tetrahedra'],12*n*n)
            self.assertEqual(r['states'][-1]['tetrahedra'],12*n*n-36)
    def test_token_plus_sink_conservation(self):
        for r in self.trials.values():
            self.assertEqual([s['control_stock'] for s in r['states']],[1]*4)
    def test_ordering_liveness(self):
        for r in self.trials.values():self.assertTrue(r['excision_first_is_blocked'])
    def test_final_homology(self):
        for r in self.trials.values():self.assertEqual(r['states'][-1]['betti_F2'],[1,1,0,0])
    def test_partial_homology(self):
        for r in self.trials.values():self.assertEqual(r['states'][2]['betti_F2'],[1,1,0,0])
    def test_radial_cut_counterexample(self):
        for r in self.trials.values():self.assertEqual(r['radial_cut_betti_F2'],[1,0,0,0])
    def test_chain_boundary_composition(self):
        for r in self.trials.values():self.assertEqual(r['states'][0]['betti_F2'],[1,0,0,0])
    def test_harmonic_number(self):self.assertEqual(scaling(8)['H_m'],'25/12')
    def test_lower_cochain_norm(self):self.assertEqual(scaling(8)['norm_h_sq_lower'],'25/32')
    def test_constant_lambda_gap_lower(self):self.assertEqual(scaling(8)['delta_lower_lambda1'],'125/64')
    def test_lambda_unit_gap_bound(self):self.assertEqual(scaling(8)['lambda_for_unit_gap_upper'],'64/125')
    def test_retained_work_ratio(self):self.assertEqual(scaling(8)['work_ratio_upper_with_mu_equals_lambda_n2'],'9/5')
    def test_angular_closedness_periods(self):
        for n,r in self.angular.items():
            self.assertEqual(len(r['ring_periods']),3*n//2)
            self.assertTrue(all(abs(abs(x)-1)<1e-12 for x in r['ring_periods']))
    def test_angular_energy_upper(self):
        for r in self.angular.values():self.assertLess(r['cochain_norm_sq'],r['analytical_upper'])
    def test_angular_ring_count(self):
        for n,r in self.angular.items():self.assertEqual(set(map(int,r['edges_by_min_radius'].keys())),set(range(1,n//2+1)))

if __name__=='__main__': unittest.main(verbosity=2)
