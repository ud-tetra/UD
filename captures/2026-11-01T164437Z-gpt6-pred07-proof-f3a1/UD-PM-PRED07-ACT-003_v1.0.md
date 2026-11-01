# UD-PM-PRED07-ACT-003 v1.0 — A gauge-invariant winding-period action exists, but its coefficient is unsourced

**Proof kind:** THEOREM / constructive sector-sensitive action and coefficient NO-GO. **Status:** PROVED_CONDITIONAL. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## 1. Typed state, sources and explicit new premises

- Source: `UD-PM-PRED06-ACT-005` establishes that divergence/curvature-only Hodge actions are blind to harmonic winding; `UD-PM-PRED06-MET-006` separates cochain metric from stiffness; `UD-PM-PRED05-SCALE-002` gives the logarithmic norm theorem on the punctured K4 carrier. These sources are in unmerged stacked PRs #487/#490; they are conditional research mathematics, not accepted physical mechanisms.
- **New assumption A1:** A finite connected oriented simplicial carrier \(K\) has \(H_1(K;\mathbb Z)\cong\mathbb Z\), with a chosen primitive cycle \(\Gamma\in Z_1(K;\mathbb Z)\) defined up to orientation. Use real closed cochains \(a\in Z^1(K;\mathbb R)\) with an **externally declared noncompact integer lift**, \(\langle a,\Gamma\rangle=n\in\mathbb Z\). This integer cannot be recovered solely as an additive homomorphism of the native \(\mathbb Z_2^3\) parity fiber.
- **New assumption A2:** Introduce a positive scalar \(\tau\) with native-action units. No value or microscopic source for \(\tau\) is supplied by G05, Q169, the native event clock or loop-curvature counting.

## 2. Theorem — explicit gauge-invariant sector term

Define
\[\mathcal A_{\rm per}(a)=\frac\tau2\big\langle a,\Gamma\big\rangle^2.\]

Then for every exact (gauge) shift \(a\mapsto a+d_0\phi\), \(\mathcal A_{\rm per}\) is unchanged. On a closed cochain, replacing \(\Gamma\) by a homologous cycle does not change the value; reversing the primitive cycle does not change the squared action. For the declared integer sectors \(\langle a_n,\Gamma\rangle=n\),
\[\mathcal A_{\rm per}(a_n)=\frac\tau2 n^2,\qquad \mathcal A_{\rm per}(a_3)-\mathcal A_{\rm per}(a_2)=\frac{5\tau}{2}>0.\]

This is a **sector-sensitive, nonlocal** mathematical action despite \(d_1a_n=\delta_1a_n=0\) on harmonic representatives, so it lies outside the PRED06 curvature-only no-go hypotheses. The theorem does not show that the term is admitted by the native UD action; it exhibits an explicitly added possibility.

## 3. Proof

If \(\Gamma\) is a cycle, then \(\langle d_0\phi,\Gamma\rangle=\langle\phi,\partial_1\Gamma\rangle=0\). Thus the period and its square are gauge invariant. If \(a\) is closed and \(\Gamma' = \Gamma+\partial_2\Sigma\), then \(\langle a,\Gamma'-\Gamma\rangle=\langle d_1a,\Sigma\rangle=0\). Because \(H_1\cong\mathbb Z\), every primitive generator differs by sign plus boundary, so its square is orientation independent. Substituting integral periods gives the action and exact gap. QED.

## 4. Coefficient-identifiability obstruction and refinement comparison

The topological and gauge requirements above admit \(\tau\) and \(2\tau\) equally. They induce different sector gaps \(5\tau/2\) and \(5\tau\) on the same complex. Therefore those premises alone cannot **derive a unique nonzero action coefficient**. Nor do they fix the cochain inner product \(G_N\), because \(\mathcal A_{\rm per}\) depends only on the period pairing and never uses \(G_N\).

If one **additionally demands** exact agreement between this new period term and a separately postulated quadratic harmonic-norm action \(\mathcal A_{\rm kin}(n h_N)=\frac{\kappa_N}{2}n^2 P_N(G)\), then and only then \(\kappa_N=\tau/P_N(G)\). If \(P_N(G)=\Theta(\log N)\) as in the *uniformly elliptic* PRED06 theorem, this matching entails \(\kappa_N=\Theta(1/\log N)\) for fixed positive \(\tau\). **This is inverse matching between two assumed actions, not an independently derived stiffness from frozen UD.**

The compact Wilson readout \(\exp(2\pi i\langle a,\Gamma\rangle)=1\) is the same for all integer \(n\). A noncompact/unwrapped period reader or other additional carrier would be required to distinguish these sectors observationally. **Critical gauge-scope caveat:** This theorem proves invariance only under single-valued real exact shifts \(a\mapsto a+d_0\phi\). If a compact U(1) gauge convention identifies periods \(n\sim n+1\) through large gauge transformations, the quadratic term is **not** invariant (its values at \(n=0\) and \(n=1\) differ). Hence the proposed action requires an independently justified unwrapped/noncompact sector or a new observable that is not quotiented by large gauge equivalence.

## 5. Exact witness, counterexamples, open gates

For an unfilled oriented triangle graph with \(H_1=\mathbb Z\), the cochain \(h=(1/3,1/3,1/3)\) is divergence-free and has period one. The proposed topological action splits \(2h\) from \(3h\) while all incidence-derived derivative terms vanish. Exact SymPy checks confirm gauge invariance under arbitrary vertex potentials and \(\Delta=5\tau/2\). This is a *toy witness* of a general theorem, not a proof that a single filled K4 packet has winding.

**OPEN_GATED:** selection of a native integral cycle and noncompact lift, a microscopic mechanism for the global period term, action units and \(\tau\), actual defect dynamics and readout, uncertainty and independent physical verification. Non-constructor review DEFERRED. **Physical promotion 0.**
