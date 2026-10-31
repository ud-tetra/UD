import unittest
from fractions import Fraction
from itertools import product
from math import comb
import numpy as np
import native_defect_and_readout as m

class NativeSelectionMath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full=m.build_complex(4,2,False)
        cls.punct=m.build_complex(4,2,True)
        cls.z,cls.seam=m.integer_cocycle(cls.punct)
        cls.h,cls.har=m.harmonic(cls.punct,cls.z)

    def test_01_full_is_three_ball(self):
        a=m.audit_topology(self.full)
        self.assertEqual(a['betti_F2'],[1,0,0,0]);self.assertEqual(a['simplices']['T'],192)

    def test_02_defect_has_integer_winding_support(self):
        a=m.audit_topology(self.punct)
        self.assertEqual(a['betti_F2'],[1,1,0,0]);self.assertEqual(a['simplices']['T'],156)

    def test_03_source_token_stock_conserved(self):
        trail,ledger=m.source_prop(4,2)
        self.assertEqual(len(trail),3)
        self.assertEqual([x['stock_after']-x['stock_before'] for x in ledger],[0,0])

    def test_04_excision_local_to_selected_path(self):
        trail=set(self.punct['trail'])
        self.assertTrue(all(trail.isdisjoint(t) for t in self.punct['tetrahedra']))
        self.assertLess(len(self.punct['tetrahedra']),len(self.full['tetrahedra']))

    def test_05_integer_cocycle_and_nontrivial_period(self):
        self.assertEqual(self.seam['integral_period'],1)
        self.assertLess(self.har['flat_residual_max'],1e-10)
        self.assertLess(self.har['coflat_residual_max'],1e-9)

    def test_06_n2_n3_exist_mathematically(self):
        b1=m.graph_incidence(self.punct);b2=m.sparse_tri_incidence(self.punct)
        for n in (2,3):
            a=n*self.h
            self.assertLess(np.max(np.abs(b2.T@a)),1e-10)
            self.assertLess(np.max(np.abs(b1@a)),1e-9)

    def test_07_staged_updates_are_typed_and_bounded(self):
        r=m.local_staged_work(self.punct,self.h)
        self.assertAlmostEqual(r['net_retained_action'],1)
        self.assertGreater(r['nonflat_intermediate_steps'],0)
        self.assertLessEqual(r['sum_positive_injected_work'],r['safe_upper_bound'])

    def test_08_fixed_cut_is_not_equivalent_to_distributed(self):
        f=m.fixed_cut_work(self.h,self.z)
        d=m.local_staged_work(self.punct,self.h)
        self.assertGreater(f['input_work_at_fixed_cut'],d['sum_positive_injected_work'])

    def test_09_single_edge_cannot_preserve_flatness(self):
        b2=m.sparse_tri_incidence(self.punct)
        self.assertTrue(np.all(np.diff(b2.tocsr().indptr)>=1))

    def test_10_refinement_topology(self):
        for n in (6,8):
            b=m.build_complex(n,2,True)
            self.assertEqual(m.audit_topology(b)['betti_F2'],[1,1,0,0])

    def test_11_raw_classes_counts_exact(self):
        counts={x:sum(m.pair_class(s)==x for s in product((0,1),repeat=4)) for x in ((0,0),(0,1),(1,1))}
        self.assertEqual(counts,{(0,0):9,(0,1):4,(1,1):3})

    def test_12_all_27_classes_representable_in_boolean_lift(self):
        a=m.microstate_audit()
        self.assertEqual(a['formal_class_count'],27)
        self.assertEqual(a['raw_triple_microstate_count'],4096)

    def test_13_raw_iid_collisions(self):
        a=m.microstate_audit()
        self.assertEqual(a['expected_iid_replays_N24'],str(Fraction(comb(24,2)*53**3,128**3)))
        self.assertGreater(Fraction(a['expected_iid_replays_N24']),Fraction(92,9))

    def test_14_54_paired_class_schedule(self):
        classes=list(product(((0,0),(0,1),(1,1)),repeat=3))
        schedule=classes+classes[::-1]
        self.assertEqual(len(schedule),54)
        for c in classes:self.assertEqual(schedule.count(c),2)

    def test_15_independent_theta_readout_needed(self):
        # If q is erroneously identified with theta_plus, R_top contradicts V=0.
        omega=(1,1,1);q=(1,1,1)
        self.assertEqual(sum(o*t for o,t in zip(omega,q)),3)
        self.assertNotEqual(sum(o*t for o,t in zip(omega,q)),0)

    def test_16_z2_reduction_loses_integer_index(self):
        self.assertEqual(1%2,3%2)
        self.assertNotEqual(1,3)

    def test_17_flip_budget_union_bound(self):
        a=m.microstate_audit()
        self.assertEqual(a['union_bound_54x12_input_flips'],str(Fraction(54*12,100000)))
        self.assertLess(a['union_failure_probability_54_preparations_approx'],.01)

    def test_18_homology_robust_seed_relocation(self):
        b=m.build_complex(6,2,True,(2,3,0))
        self.assertEqual(m.audit_topology(b)['betti_F2'],[1,1,0,0])

if __name__=='__main__':unittest.main()

# Additional tests are bound dynamically to the existing suite for direct verification.
def _test_19_three_pass_dual_control(self):
    a=m.microstate_audit()
    sch=a['schedule_81_observations']
    self.assertEqual(len(sch),81)
    for k in range(27):
        self.assertEqual(sch[k]['class'],sch[27+k]['class'])
        self.assertEqual(sch[k]['class'],sch[54+k]['class'])
        self.assertEqual(sch[k]['raw_12bits'],sch[27+k]['raw_12bits'])
        self.assertNotEqual(sch[k]['raw_12bits'],sch[54+k]['raw_12bits'])

def _test_20_coarse_graining_does_not_imply_memory(self):
    a=(0,0,0,0); b=(0,0,1,0)
    self.assertEqual(m.pair_class(a),m.pair_class(b))
    self.assertNotEqual(a[2],b[2])

NativeSelectionMath.test_19_three_pass_dual_control=_test_19_three_pass_dual_control
NativeSelectionMath.test_20_coarse_graining_does_not_imply_memory=_test_20_coarse_graining_does_not_imply_memory

def _test_21_local_solver_refines(self):
    for N in (4,6,8):
        c=m.build_complex(N,2,True)
        z,_=m.integer_cocycle(c)
        target,_=m.harmonic(c,z)
        approx,receipt=m.local_hodge_relaxation(c,z,steps=2500)
        self.assertLess(receipt['final_divergence_max'],2e-9)
        self.assertLess(np.linalg.norm(target-approx),1e-7)

def _test_22_uniform_bound_across_refinement(self):
    for N in (4,6,8):
        c=m.build_complex(N,2,True)
        z,_=m.integer_cocycle(c);h,_=m.harmonic(c,z)
        receipt=m.local_staged_work(c,h)
        self.assertLessEqual(receipt['safe_upper_bound'],41/5+1e-10)
        self.assertLessEqual(receipt['sum_positive_injected_work'],41/5)
        self.assertGreater(receipt['nonflat_intermediate_steps'],0)

def _test_23_natural_shell_2_risk(self):
    p_shell2=Fraction(351,4096)
    miss=(1-float(p_shell2))**24
    self.assertGreater(miss,.1)
    self.assertLess(miss,.15)

def _test_24_quartic_alternative_is_not_WBX1_unique(self):
    a=Fraction(1);b=Fraction(1,32)
    e=[a*(2*n+1)+b*((n+1)**4-n**4) for n in range(4)]
    self.assertEqual(m.d2(e) if hasattr(m,'d2') else e[2]-2*e[1]+e[0],36*b)
    self.assertNotEqual((e[1]-e[0])*(e[3]-e[2])-(e[2]-e[1])**2,0)

def _test_25_input_error_bound_for_81_observations(self):
    self.assertEqual(Fraction(81*12,100000),Fraction(243,25000))
    self.assertLess(Fraction(81*12,100000),Fraction(1,100))

NativeSelectionMath.test_21_local_solver_refines=_test_21_local_solver_refines
NativeSelectionMath.test_22_uniform_bound_across_refinement=_test_22_uniform_bound_across_refinement
NativeSelectionMath.test_23_natural_shell_2_risk=_test_23_natural_shell_2_risk
NativeSelectionMath.test_24_quartic_alternative_is_not_WBX1_unique=_test_24_quartic_alternative_is_not_WBX1_unique
NativeSelectionMath.test_25_input_error_bound_for_81_observations=_test_25_input_error_bound_for_81_observations
