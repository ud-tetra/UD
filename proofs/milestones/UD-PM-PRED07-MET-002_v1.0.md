# UD-PM-PRED07-MET-002 v1.0 — K4 symmetry does not fix a cochain action metric

**Proof kind:** NO-GO / exact metric ambiguity. **Status:** PROVED_CONDITIONAL. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## Source, domain and hypotheses

Source: UD coefficient ledger v0.39 Q169 (global skew Hodge–Dirac on fixed incidence, unit-simplex support norm) and G05 (action weighting open); prior source-bound proof `UD-PM-PRED06-MET-006` in PR #490 (separate cochain-metric/stiffness ambiguity). **Do not identify** Q169's explicit support norm with a newly introduced physical sector action metric without a further equality axiom.

Take the **oriented** six-dimensional real edge-cochain space \(C^1(K_4;\mathbb R)\), with Euclidean orientation basis, and its signed \(S_4\) permutation representation. Let \(B_1:C_1\to C_0\) be the ordinary K4 incidence map, \(B_1B_1^T=4I-J\). Define

\[P_{\nabla}=\frac14 B_1^TB_1,\qquad P_{\rm cyc}=I-P_{\nabla}.\]

## Theorem — non-uniqueness even with fixed edge norms

Both \(P_{\nabla}\) and \(P_{\rm cyc}\) are orthogonal projectors of rank three, and are equivariant under the signed \(S_4\) edge representation. For **every** \(g,c>0\),

\[G_{g,c}=gP_{\nabla}+cP_{\rm cyc}\]

is an \(S_4\)-invariant symmetric positive-definite edge-cochain metric. The metrics \(G_{1,1}=I\) and \(G_{1/2,3/2}\ne I\) both have trace six and satisfy \((G_{g,c})_{ee}=1\) for every oriented edge, yet assign distinct inner products to pairs of different edges. Therefore **K4 permutation symmetry, total trace, and unit norms of each edge basis vector do not determine a unique general cochain metric.**

This is an existence proof of non-uniqueness, not a classification of *all* possible invariant forms. Imposing the **additional assumption** that the metric be diagonal in the oriented edge basis, with each diagonal equal to one, does select \(G=I\); that diagonal assumption is stronger than symmetry and cannot silently be transferred from Q169's support-norm convention to a physical sector action.

## Proof

Since \(B_1B_1^T=4I-J\) and \(JB_1=0\),
\[(B_1^TB_1)^2=B_1^T(4I-J)B_1=4B_1^TB_1.\]
Thus \(P_{\nabla}^2=P_{\nabla}\), \(P_{\rm cyc}^2=P_{\rm cyc}\), they are symmetric orthogonal complements, and their ranks are three by the K4 incidence rank. Relabeling vertices and changing each edge orientation in the induced way preserves the signed incidence equation; hence both projectors commute with the signed edge action of \(S_4\). Their positive weighted sum \(G_{g,c}\) is positive definite for \(g,c>0\) with eigenvalues \(g\) and \(c\), each of multiplicity three.

Each K4 edge column in \(B_1\) has squared norm two, so \((P_{\nabla})_{ee}=1/2\), and similarly \((P_{\rm cyc})_{ee}=1/2\). Hence every diagonal entry is \((g+c)/2\). Choosing \(g+c=2\) fixes every edge norm to one and the trace to six, but leaves a positive one-parameter family \(0<g<2\), \(c=2-g\). For instance \(g=1/2,c=3/2\) yields \((G_{g,c})_{(01),(02)}=-1/4\) whereas the unit metric has zero there. This is a genuine metric difference under identical stated normalization and symmetry constraints. QED.

## Limits and physical correspondence

The K4 **filled tetrahedron** has \(H^1=0\). This finite metric theorem does not assert a nontrivial winding harmonic cochain on a single packet; those appear only in later glued/topology-changed complexes under their separate assumptions. An edge-local diagonal action on a glued complex may choose a particular metric; its derivation must identify a native measure and gluing map. The family above neither derives G05 nor selects a physical stiffness coefficient, and it does not invalidate Q169's fixed unit-support convention.

A SymPy exact checker constructs the projectors and verifies covariance for all 24 signed permutations. **Proof status:** EXACT_CONDITIONAL; **physical promotion:** 0; review deferred.
