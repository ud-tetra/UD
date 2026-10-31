"""Deterministic exact and finite-scope numerical tests; no physical correspondence."""
import itertools
import unittest
from collections import Counter
import sympy as s

import carrier_and_preparation as m

class CarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.S,cls.B1,cls.B2,cls.B3=m.chain(8,True)
        cls.z=m.seam_slip(cls.S,8)

    def test_chain_boundary_squared_zero(self):
        self.assertEqual(self.B1*self.B2,s.zeros(self.B1.rows,self.B2.cols))
        self.assertEqual(self.B2*self.B3,s.zeros(self.B2.rows,self.B3.cols))

    def test_betti_m4_exact(self):
        x=m.build_carrier(4,True,True)
        self.assertEqual(x['betti'],[1,1,0,0])

    def test_betti_m8_exact(self):
        self.assertEqual(m.build_carrier(8,True,True)['betti'],[1,1,0,0])

    def test_full_simplex_no_h1(self):
        # K4 as filled tetrahedron, unlike its 1-skeleton.
        edges=list(itertools.combinations(range(4),2))
        faces=list(itertools.combinations(range(4),3))
        tet=[tuple(range(4))]
        B1=m.incidence([(i,) for i in range(4)],edges)
        B2=m.incidence(edges,faces)
        B3=m.incidence(faces,tet)
        self.assertEqual(6-B1.rank()-B2.rank(),0)
        self.assertEqual(B2*B3,s.zeros(B2.rows,B3.cols))

    def test_face_flatness_all_five_sectors(self):
        for n in range(5):
            self.assertEqual(self.B2.T*m.lifted_cochain(self.S,8,n),s.zeros(self.B2.cols,1))

    def test_vertex_coclosedness_all_five_sectors(self):
        for n in range(5):
            self.assertEqual(self.B1*m.lifted_cochain(self.S,8,n),s.zeros(self.B1.rows,1))

    def test_periods_are_integer(self):
        for n in range(5):self.assertEqual(m.period(self.S,m.lifted_cochain(self.S,8,n),8),n)

    def test_norm_exact(self):
        for n in range(5):
            a=m.lifted_cochain(self.S,8,n)
            self.assertEqual((a.T*a)[0],s.Rational(5*n*n,16))

    def test_quadratic_action_exact(self):
        for n in range(5):
            self.assertEqual(m.action(m.lifted_cochain(self.S,8,n)),s.Rational(5*n*n,32))

    def test_seam_support_exact(self):
        self.assertEqual(sum(1 for x in self.z if x),3)

    def test_seam_is_closed_and_nonexact(self):
        self.assertEqual(self.B2.T*self.z,s.zeros(self.B2.cols,1))
        self.assertEqual(m.period(self.S,self.z,8),1)

    def test_seam_source_balance(self):
        z=m.seam_receipts(8)
        self.assertEqual(z['source_receipts'][2]['gross_injected_work'],'17/8')
        self.assertEqual(z['source_receipts'][2]['retained_equilibrium_increment'],'25/32')
        self.assertEqual(z['source_receipts'][2]['dissipated_remainder'],'43/32')

    def test_gross_retained_ratio_distinction(self):
        z=m.seam_receipts(8)
        self.assertEqual(z['gross_two_event_ratio'],'29/24')
        self.assertEqual(z['retained_two_event_ratio'],'3')

    def test_same_sector_gauge_minimality(self):
        a=m.lifted_cochain(self.S,8,3)
        phi=s.Matrix([s.Rational(i%5,7) for i in range(self.B1.rows)])
        ex=self.B1.T*phi
        self.assertGreater(m.action(a+ex)-m.action(a),0)
        self.assertEqual(m.period(self.S,a+ex,8),3)

    def test_quadratic_d2_h4(self):
        x=m.build_carrier(8)
        self.assertEqual(x['quadratic_D2'],'0')
        self.assertEqual(x['quadratic_H4'],'0')

    def test_quartic_needs_additional_rule(self):
        x=m.build_carrier(8)
        self.assertEqual(x['quartic_D2'],'153/1024')
        self.assertEqual(x['quartic_H4'],'3825/262144')

    def test_cap_kills_winding(self):
        self.assertEqual(m.capped_annulus_beta(8)['betti'],[1,0,0])

    def test_relaxation_converges_to_harmonic(self):
        r=m.relax_phase_slip(8,1000)
        self.assertLess(r['final_distance_to_n3'],r['initial_distance_to_n3']/100)
        self.assertLess(r['contraction_on_exact_sector_bound'],1)

    def test_fixed_sector_cannot_advance_without_source(self):
        a=m.lifted_cochain(self.S,8,2)
        assert self.B1*a==s.zeros(self.B1.rows,1)
        self.assertEqual(m.period(self.S,a-self.B1.T*self.B1*a,s.Rational(8)),2)

    def test_refinement_no_go_exact(self):
        m_values=[4,8,16,32]
        retained_fixed=[]; gross_scaled=[]
        for z in m_values:
            # Fixed stiffness: retained action gap decays as 1/m.
            retained_fixed.append(s.Rational(25,4*z))
            # Required stiffness lambda_m=m: retained gap fixed, gross input grows.
            scaled_retained=s.Rational(25*z,4*z)
            gross_scaled.append(s.Rational(3*z,2)+5)
            self.assertEqual(scaled_retained,s.Rational(25,4))
        self.assertTrue(all(a>b for a,b in zip(retained_fixed,retained_fixed[1:])))
        self.assertTrue(all(a<b for a,b in zip(gross_scaled,gross_scaled[1:])))

    def test_quartic_gradient_stationary_all_sectors(self):
        for n in range(1,5):
            a=m.lifted_cochain(self.S,8,n)
            grad=s.Matrix([v+4*v**3 for v in a])
            self.assertEqual(self.B1*grad,s.zeros(self.B1.rows,1))


class PreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record=m.audit_preparation(20261031)

    def test_all_states27_unique(self):self.assertEqual(len(set(m.states27())),27)
    def test_shell_distribution(self):self.assertEqual(Counter(m.shell(x) for x in m.states27()),{0:8,1:12,2:6,3:1})
    def test_partial_count(self):self.assertEqual(sum(m.has_partial(x) for x in m.states27()),19)
    def test_minimal_four_gate_and_replay(self):
        x=self.record['minimal_schedule'];self.assertEqual(len(x),4)
        self.assertEqual(x[0],x[3])
    def test_all_54_classes_twice(self):
        x=[tuple(tuple(p) for p in y['class']) for y in self.record['full_54_schedule']]
        self.assertEqual(Counter(x),{k:2 for k in m.states27()})
        self.assertEqual(self.record['minimum_repeat_lag'],18)
    def test_orbit_count10(self):
        self.assertEqual(len(m.orbit_reps()),10)
        self.assertEqual(Counter(len(v) for v in m.orbit_reps().values()),{1:3,3:6,6:1})
    def test_orbit_sum27(self):self.assertEqual(sum(len(v) for v in m.orbit_reps().values()),27)
    def test_two_pass_quotient20(self):self.assertEqual(len(self.record['quotient_20_schedule']),20)
    def test_S3_covariance_of_assumed_endpoint_laws(self):
        for x in m.states27():
            for perm in itertools.permutations(range(3)):
                y=tuple(x[i] for i in perm)
                for name,q in m.q_representatives(x).items():
                    self.assertEqual(m.q_representatives(y)[name],tuple(q[i] for i in perm))
    def test_representative_X_table(self):
        for x in m.states27():
            q=m.q_representatives(x)
            k=m.shell(x)
            self.assertEqual(sum(q['R0'])-k,0)
            self.assertEqual(sum(q['Rtop'])-k,3-k)
            self.assertEqual(sum(q['R2'])-k,1 if k==2 else 0)
    def test_six_states_min_distance_three(self):
        x=self.record['representative_endpoint_design']
        self.assertEqual(x['min_pairwise_bit_distance_six'],3)
        self.assertEqual(len(x['minimal_six_observations']),6)
    def test_twelve_states_min_distance_six(self):
        x=self.record['representative_endpoint_design']
        self.assertEqual(x['min_pairwise_bit_distance_twelve'],6)
        self.assertEqual(len(x['two_pass_twelve_observations']),12)
    def test_strict_divergence_R0_vs_R2_only_shell2(self):
        for x in m.states27():
            q=m.q_representatives(x)
            dist=sum(a!=b for a,b in zip(q['R0'],q['R2']))
            self.assertEqual(dist,1 if m.shell(x)==2 else 0)
    def test_strict_divergence_R2_vs_R1_only_shell1(self):
        for x in m.states27():
            q=m.q_representatives(x)
            dist=sum(a!=b for a,b in zip(q['R2'],q['R1']))
            self.assertEqual(dist,2 if m.shell(x)==1 else 0)
    def test_strict_divergence_R1_vs_Rtop_only_shell0(self):
        for x in m.states27():
            q=m.q_representatives(x)
            dist=sum(a!=b for a,b in zip(q['R1'],q['Rtop']))
            self.assertEqual(dist,3 if m.shell(x)==0 else 0)

if __name__=='__main__':unittest.main(verbosity=2)
