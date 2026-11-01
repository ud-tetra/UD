#!/usr/bin/env python3
"""Supporting exact finite tests; mathematical proofs are in the milestone papers."""
import unittest
from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
from independent_topology_work_audit import (
    tetra_mesh, cut_center, closure, betti, triangle_incidence, face_bound_check
)

class ProofAudit(unittest.TestCase):
    def test_intact_and_cut_integral_homology_mod2_check(self):
        for N in (4,6,8):
            f=tetra_mesh(N,N,2)
            x=cut_center(f,N,N,2)
            self.assertEqual(betti(closure(f))['betti_f2'],(1,0,0,0))
            self.assertEqual(betti(closure(x))['betti_f2'],(1,1,0,0))
    def test_local_star_incomplete_is_not_winding(self):
        for N in (4,6,8):
            f=tetra_mesh(N,N,2)
            seed=(N//2,N//2,0)
            x={t for t in f if seed not in t}
            v,e,_,_=closure(x)
            self.assertNotIn(seed,v)
            self.assertNotIn(tuple(sorted((seed,(N//2,N//2,1)))),e)
            self.assertEqual(betti(closure(x))['betti_f2'],(1,0,0,0))
    def test_exact_tetra_and_star_counts(self):
        for N in (4,6,8):
            f=betti(closure(tetra_mesh(N,N,2)))
            x=betti(closure(cut_center(tetra_mesh(N,N,2),N,N,2)))
            self.assertEqual(tuple(f[k]-x[k] for k in ['V','E','F','T']),(3,32,66,36))
    def test_staged_source_inequality_exact_rational(self):
        r=face_bound_check()
        self.assertEqual(r['sharp_face_ratio'],'2/3')
        self.assertEqual(r['exact_closed_face_cases'],1008)
        self.assertEqual(r['exact_action_sequences'],1728)
    def test_freudenthal_face_incidence_uniform(self):
        for N in (4,6,8):
            _,_,f,_=closure(cut_center(tetra_mesh(N,N,2),N,N,2))
            self.assertEqual(triangle_incidence(f)[1],6)
    def test_repeated_toggles_exceed_one_pass_bound(self):
        # Exact finite witness: 1 edge changes repeatedly while final state unchanged.
        h=[F(1),F(-1,2),F(-1,2)]
        lam=F(4,15);mu=lam;n=2
        a=[n*v for v in h]
        def action(): return lam*sum(x*x for x in a)/2+mu*sum(a)**2/2
        base=action();old=base;work=F(0)
        # Add/subtract h[0] five times, then perform each final addition once.
        for _ in range(8):
            a[0]+=h[0]
            new=action();work+=max(new-old,F(0));old=new
            a[0]-=h[0]
            new=action();work+=max(new-old,F(0));old=new
        for j in range(3):
            a[j]+=h[j]
            new=action();work+=max(new-old,F(0));old=new
        self.assertEqual(action()-base,F(1))
        self.assertGreater(work,F(9,5))
    def test_pure_gauge_sign_loop_no_holonomy(self):
        for bits in range(1<<5):
            g=[1 if (bits>>i)&1 else -1 for i in range(5)]
            edges=[g[i]*g[(i+1)%5] for i in range(5)]
            holonomy=1
            for s in edges:holonomy*=s
            self.assertEqual(holonomy,1)

if __name__=='__main__':unittest.main(verbosity=2)
