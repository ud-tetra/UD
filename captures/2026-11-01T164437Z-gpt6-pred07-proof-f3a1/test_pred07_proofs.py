"""Scoped exact mathematical regression tests for PRED07. Not empirical validation."""
import unittest
from pathlib import Path
from itertools import permutations
from fractions import Fraction as F
import sys
import sympy as S
sys.path.insert(0,str(Path(__file__).parent))
from pred07_exact_audit import audit
from pred07_numerical_controls import solve,rhs
import numpy as np

class ExactProofChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results=audit()
    def test_source_conserves_mass(self): self.assertTrue(self.results['exact_mass_conservation'])
    def test_source_has_internal_flux_representation(self): self.assertIn('s=B',self.results['source_is_an_internal_conservative_flux'])
    def test_uniform_threshold(self): self.assertEqual(self.results['instability_threshold'],'gamma*M>4')
    def test_order_preserved_equation(self): self.assertTrue(self.results['difference_sign_preserved'])
    def test_instability_exact_root(self):
        self.assertEqual(self.results['M4_gamma2_delta_star'],'4/3 + 2*sqrt(10)/3')
    def test_symmetry_all_24(self): self.assertEqual(self.results['S4_exact_permutation_cases'],24)
    def test_metric_projector_gradient_rank(self): self.assertEqual(self.results['K4_grad_projector_rank'],3)
    def test_metric_projector_cycle_rank(self): self.assertEqual(self.results['K4_cycle_projector_rank'],3)
    def test_metric_cross_edge_difference(self): self.assertEqual(self.results['explicit_metric_correlation_G1_edge01_edge02'],'-1/4')
    def test_sector_action_gap(self): self.assertEqual(self.results['sector_gap_2_to_3'],'5*tau/2')
    def test_physical_promotion_is_zero(self): self.assertEqual(self.results['physical_promotion'],0)
    def test_threshold_under_uniform(self):
        self.assertTrue(float((4+2*S.sqrt(10))/3)>3.)
        self.assertLess(float((4+2*S.sqrt(10))/3),4.)
    def test_k4_source_q162_baseline(self):
        from itertools import combinations
        B=S.zeros(4,6)
        for j,(u,v) in enumerate(combinations(range(4),2)):
            B[u,j]=-1;B[v,j]=1
        b=S.Matrix([2,2,2,2]);self.assertEqual(-B*B.T*b/4,S.zeros(4,1))
    def test_linear_threshold_zero_case_is_not_promoted(self):
        self.assertIn('REVIEW',self.results['review_status'].replace('DEFERRED','REVIEW_DEFERRED'))

class NumericalControls(unittest.TestCase):
    def test_uniform_fixed_point(self):
        y=solve(np.array([1.,1.,1.,1.]),2.)
        self.assertLess(float(np.max(abs(y.y-1.))),1e-10)
    def test_instability_crosses_chosen_threshold(self):
        y=solve(np.array([1.03,1.01,.99,.97]),2.)
        self.assertTrue(np.any(y.y[0]-y.y[3]>=1.))
    def test_stable_gain_decay(self):
        y=solve(np.array([1.03,1.01,.99,.97]),.5)
        self.assertLess(float(np.max(y.y[:,-1])-np.min(y.y[:,-1])),.06)
    def test_mass_positive_bounds(self):
        y=solve(np.array([1.03,1.01,.99,.97]),2.)
        self.assertLess(float(np.max(abs(y.y.sum(axis=0)-4))),1e-9)
        self.assertGreaterEqual(float(y.y.min()),0)
    def test_strict_initial_order_before_numerical_collapse(self):
        y=solve(np.array([1.03,1.01,.99,.97]),2.)
        self.assertGreater(min(float(np.min(y.y[i,:201]-y.y[i+1,:201])) for i in range(3)),0)

if __name__=='__main__':unittest.main()
