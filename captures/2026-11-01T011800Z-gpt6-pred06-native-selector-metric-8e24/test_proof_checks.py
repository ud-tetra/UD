"""Exact scoped regression tests for PRED06 mathematical proof witnesses.
Passing software checks corroborate, but cannot elevate assumptions or peer-review status.
"""
import unittest
import sympy as sp
from independent_proof_checks import (
    s4_checks, selector_checks, parity_checks, diffusion_checks,
    flux_selector, annulus_exact, harmonic_bounds_checks, E,
)

class ProofChecks(unittest.TestCase):
    def test_s4_order(self): self.assertEqual(s4_checks()['s4_order'],24)
    def test_s4_no_fixed_vertex(self): self.assertEqual(s4_checks()['common_fixed_vertices'],[])
    def test_s4_no_fixed_edge(self): self.assertEqual(s4_checks()['common_fixed_unoriented_edges'],[])
    def test_vertex_stabilizer_transitive(self): self.assertEqual(s4_checks()['neighbor_orbit_after_vertex_seed'],[1,2,3])
    def test_selector_equivariance(self): self.assertTrue(selector_checks()['s4_equivariant_24_actions'])
    def test_selector_unique(self): self.assertEqual(flux_selector((4,3,2,0)),(0,3,sp.Rational(1)))
    def test_selector_uniform_hold(self): self.assertIsNone(flux_selector((1,1,1,1)))
    def test_selector_port_tie_hold(self): self.assertIsNone(flux_selector((4,1,1,1)))
    def test_selector_closed_hold(self): self.assertIsNone(flux_selector((4,3,2,0),gates={e:0 for e in E}))
    def test_parity_no_integer_additive_lift(self): self.assertEqual(parity_checks()['additive_integer_homomorphisms_in_range'],[[0,0,0]])
    def test_diffusion_homogeneous_stationary(self): self.assertTrue(diffusion_checks()['homogeneous_stationary'])
    def test_diffusion_energy_decay(self): self.assertEqual(diffusion_checks()['contrast_energy_derivative'],'-35/4')
    def test_annulus_homology(self): self.assertEqual(annulus_exact()['betti_1'],1)
    def test_annulus_unweighted_harmonic(self): self.assertEqual(annulus_exact()['unweighted_harmonic_norm_sq'],'5/8')
    def test_incidence_metric_harmonic(self): self.assertEqual(annulus_exact()['weighted_harmonic_norm_sq'],'3/4')
    def test_hodge_harmonic_zero(self): self.assertTrue(annulus_exact()['unit_metric_hodge_zero'])
    def test_metric_action_scale_pair(self): self.assertTrue(annulus_exact()['quadratic_scale_pair_invariant'])
    def test_elliptic_metric_exact_bounds(self):
        r=harmonic_bounds_checks()
        self.assertEqual(r['rows'][0]['H_halfN'],'3/2')
        self.assertEqual(r['rows'][0]['gap_lower'],'15/32')
        self.assertEqual(r['rows'][-1]['gap_upper'],'2520')
    def test_source_promotion_zero(self):
        import json
        from pathlib import Path
        r=json.loads(Path(__file__).with_name('EXACT_AUDIT.json').read_text())
        self.assertEqual(r['physical_promotion'],0)
        self.assertEqual(r['review'],'DEFERRED')

if __name__=='__main__':unittest.main()
