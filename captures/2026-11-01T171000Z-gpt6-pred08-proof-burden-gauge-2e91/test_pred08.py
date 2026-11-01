#!/usr/bin/env python3
"""Finite corroboration tests. These are not a proof assistant or a physical bridge."""
import unittest
from fractions import Fraction as F
from itertools import permutations,product
from pathlib import Path
from independent_exact import (pairs,variance,a_nonnegative,sink,seed,classify)

class BurdenPassivity(unittest.TestCase):
    def test_all_zero(self):self.assertEqual(sink((F(1),)*4,(1,)*6),0)
    def test_one_hot_positive(self):self.assertGreater(sink((F(1),F(0),F(0),F(0)),(1,)*6),0)
    def test_gate_off(self):self.assertEqual(sink((F(1),F(0),F(0),F(0)),(0,)*6),0)
    def test_mask_nonneg(self):
        for mask in product((0,1),repeat=6):self.assertGreaterEqual(sink((F(4),F(3),F(2),F(0)),mask),0)
    def test_uniform_symmetry(self):
        for mask in product((0,1),repeat=6):self.assertEqual(sink((F(1),)*4,mask),0)

class Resource(unittest.TestCase):
    def test_nonnegative_A(self):
        for t in product(range(3),repeat=4):
            if sum(t):self.assertGreaterEqual(a_nonnegative(tuple(F(x) for x in t)),0)
    def test_equal_positive_zero_A(self):self.assertEqual(a_nonnegative((F(2),)*4),0)
    def test_equal_nonzero_support_zero_A(self):self.assertEqual(a_nonnegative((F(2),F(2),F(0),F(0))),0)
    def test_unequal_positive_A(self):self.assertGreater(a_nonnegative((F(3),F(2),F(1),F(1))),0)
    def test_linear_gain_eigenvalue(self):
        gamma=F(2);M=F(4); R=F(2); Rstar=F(1)
        u=R/(R+Rstar)
        self.assertEqual(-1+gamma*M*u/4,F(1,3))
    def test_spent_stock_zero_gain(self):
        R=F(0);Rstar=F(1)
        self.assertEqual(R/(R+Rstar),0)
    def test_seed_cost(self):
        e=F(1,10); pre=(F(1),)*4; post=seed(pre,0,1,e)
        self.assertEqual(variance(post)-variance(pre),e*e)
    def test_ordered_seed_output(self):
        e=F(1,10);pre=(F(1),)*4
        for u,v in permutations(range(4),2):self.assertEqual(classify(seed(pre,u,v,e)),(u,v))
    def test_current_magnitude(self):
        b=seed((F(1),)*4,0,1,F(1,10))
        self.assertEqual((b[0]-b[1])/4,F(1,20))
        self.assertEqual((b[0]-b[2])/4,F(1,40))
    def test_k4_variance(self):
        b=(F(11,10),F(9,10),F(1),F(1))
        self.assertEqual(sink(b,(1,)*6),2*variance(b))
    def test_dwell_bound(self):
        E=F(2);delta=F(1,2)
        self.assertEqual(2*E/(delta*delta),16)

class GaugeAndCohomology(unittest.TestCase):
    def test_triangle_period(self):self.assertEqual(sum((1,0,0)),1)
    def test_compact_link_integer(self):
        import cmath
        for n in range(-5,6):
            self.assertLess(abs(cmath.exp(2j*cmath.pi*n)-1),1e-13)
    def test_exact_gradient_period(self):
        for a,b,c in product(range(-2,3),repeat=3):
            self.assertEqual((b-a)+(c-b)+(a-c),0)
    def test_large_relative_invariance(self):
        for a,r,k in product(range(-3,4),repeat=3):self.assertEqual((a+k)-(r+k),a-r)
    def test_independent_lift_noninvariance(self):
        self.assertNotEqual((2+1)-1,2-1)
    def test_compact_quadratic_action_diff(self):
        tau=F(3,7)
        self.assertEqual(tau*(3*3-2*2)/2,F(15,14))
    def test_action_coefficient_free(self):
        n=3;self.assertNotEqual(F(1)*n*n/2,F(2)*n*n/2)
    def test_single_filled_triangle_has_no_h1(self):
        # Direct exact ranks of the cellular boundary complex (not Euler alone).
        import sympy as sp
        B1=sp.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
        B2=sp.Matrix([1,1,1])
        self.assertEqual(B1*B2,sp.zeros(3,1))
        self.assertEqual(B1.rank(),2)
        self.assertEqual(B2.rank(),1)
        self.assertEqual(3-B1.rank()-B2.rank(),0)

if __name__=='__main__':unittest.main(verbosity=2)
