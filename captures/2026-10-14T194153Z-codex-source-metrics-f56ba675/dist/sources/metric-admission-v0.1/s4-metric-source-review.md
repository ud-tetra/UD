# S4 metric and clock admission — source-scope review v0.1

Date: 2026-10-14. Lane: development — no registry entry. Reviewer: constructor-team AI source/scope thread. This is neither independent human review nor CRL promotion. Physical promotion: 0.

## Disposition

The proposed three-frequency obstruction is correctly source-bound for the filled tetrahedron's **real S4-equivariant skew family**. The degree-isotropic positive-metric specialization is a consistent conditional construction when its adjoint convention is stated. The sources do not select new coefficient values or a native metric law. The default ten-gate clock has five positive generator frequencies, so no choice in the identical-copy three-frequency class gives exact full-generator admission.

The relaxed best relative spectral distance is exactly 1, attained by positive centers 3, 7, 10 against targets 2, 4, 6, 8, 10. Those centers are optimization witnesses, never adopted UD coefficients. Consequently a Duhamel budget based on that generator residual cannot establish a small endpoint-error guarantee. It does **not** establish an endpoint-error lower bound.

## Read scope and provenance

The source text inspected is the imported `content` field of `dist/assets/sources.json`, restored from the Site source repository. Hashes below identify those exact UTF-8 text fields, not original manuscript/PDF bytes. Archive labels remain dated source assertions.

| Catalog ID | Source and inspected part | Role |
|---|---|---|
| C0258 | Paper III review draft 1.1.1, §§2.1–2.3 | Full signed-chain decomposition; commutant dimensions 13/10/3; coefficients not selected by symmetry |
| C0769 | Paper I review draft 1.1.1, §§2 and 4.1–4.3 | Orthonormal simplex baseline; correct-adjoint requirement under metric change |
| C0190 | Exact S4 chain projectors, §§1–6 | Explicit projectors, adjacent channels, complete skew-family classification and characteristic polynomial |
| C0200 | Carrier symmetry: full versus skew commutant | Separates associative commutant from three-dimensional skew part |
| C0187 | PSR incidence-sign certificate — exact results, S4 object | Constructor receipt: isotypic ranks 1/6/6/2, grade ranks and symbolic family |
| C0173 | Geometric inner-product interface, §§1–6 | Fixed-boundary weighted-adjoint construction; geometric Rule A/B candidates; underdetermination |
| C0176 | Chain semantics and weighted receipts, §§3–5 | Ratio normalization and independent-stock semantics |
| C0473 | Pachner 2↔3 Hodge Dirac Move Response, §8 | Historical positive block-control family and inverse-product parameterization |
| C0496 | Tagged Load, Response Capacity and Pachner Spectral Change, §9 | Explicit repair distinguishing inverse-product whitening from fixed-boundary adjoints |

The attached coefficient ledger v0.39 header and governance CRL2 subdivision were inspected locally. The ledger is a historical August baseline, not authority to silently select newer metric parameters. The subdivision document identifies itself as a proposal; constructor-team AI review satisfies no independent-review rung. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read or used.

## Exact source classification and coefficient order

Write B for the degree-lowering boundary, with increasing-vertex orientation, and A0=Bᵀ−B. Source C0190 defines Ak to have −Bk in the upper block from Ck to C(k−1), and +Bkᵀ in the lower block. Thus A0=A1+A2+A3. The ordering is explicit:

| Coefficient | Degree channel | C0190 label | Paper III label | Signed eigenvalue multiplicity |
|---|---|---|---|---:|
| a | C0 ↔ C1 | V | T2 | 3 for each sign |
| b | C1 ↔ C2 | V⊗ε | T1 | 3 for each sign |
| c | C2 ↔ C3 | ε | A2 | 1 for each sign |

The harmonic vertex line is the trivial representation A1 (the representation label A1 is distinct from the matrix named A1). The isotypic projectors have ranks 6,6,2, and the harmonic projector has rank 1. Source identities are:

\[
A_iA_j=0\quad(i\ne j),\qquad
A(a,b,c)^2=-4(a^2P_V+b^2P_{V\otimes\varepsilon}+c^2P_\varepsilon),
\]
\[
\chi_{A(a,b,c)}(\lambda)=\lambda(\lambda^2+4a^2)^3
(\lambda^2+4b^2)^3(\lambda^2+4c^2).
\]

Every real skew-symmetric equivariant endomorphism is in this family because each nontrivial irreducible has a two-dimensional multiplicity space, whose skew part has dimension one. The factor 2 in the positive frequencies 2|a|,2|b|,2|c| is correct. The factor 4 in squared frequencies is correct. A coefficient equal to zero adds zero modes rather than adding a band. Coincident absolute values merge bands.

The canonical a=b=c=1 is selected by the specified boundary/adjoint generator and unit metric, not by symmetry or the unit metric alone. Source witness (1,2,3) has squared frequencies 4,16,36 but is explicitly not an adopted dynamics.

## Two distinct metric conventions

For fixed degree metrics Gk=gk I, gk>0, retain the numerical boundaries Bk. The consistent adjoint is
\[
B_k^{\dagger_G}=G_k^{-1}B_k^\top G_{k-1}.
\]
With AG=B†G−B and normalized coordinates y=G^(1/2)c, the Euclidean skew operator is
\[
\widehat A_G=G^{1/2}A_GG^{-1/2}
=\sum_{k=1}^3 t_kA_k,\qquad
t_k=\sqrt{g_{k-1}/g_k}.
\]
It has positive frequencies 2t1 (multiplicity 3), 2t2 (multiplicity 3), and 2t3 (multiplicity 1). The metric isometry, residual and norms must be evaluated after this normalization or with the equivalent G pairing. Raw AG is generally not Euclidean skew.

Any prescribed positive triple is algebraically realizable in this specialization: choose g0>0 and recursively gk=g(k−1)/tk². This is a parameterization, not a source-selected metric. Multiplying all gk by the same positive scalar leaves the tk unchanged.

Historical C0473 instead gives tk=(g(k−1)gk)^(-1/2). C0496§9 already states the convention under which that formula is valid: start from **G ċ=A0c**, and whiten to G^(-1/2)A0G^(-1/2). That is a different operator from the fixed-boundary adjoint construction. The two formulas must not be interchanged merely because both use a symbol G. The sign of C0473's A is the opposite of C0190's; this changes directed evolution but not paired frequency spectra.

The degree-isotropic class is a subset of positive diagonal chain metrics. Nonuniform simplex weights need not respect the fixed signed S4 action and can split the threefold degeneracies. C0173 supplies two source-authored geometric assignments, Rule A and Rule B, but explicitly treats both as candidates and proves the sufficiency conditions do not select between them. Their five distinct generic factors do not contradict the three-band classification because a stretched geometry is not invariant under all permutations of the fixed regular carrier.

More generally, a fixed positive **S4-invariant** metric can mix the two equivalent copies inside an isotypic component. Its positive square root commutes with the group action. Normalizing a G-skew equivariant operator therefore again gives a real Euclidean-skew equivariant operator, with at most one positive frequency per two-copy isotypic component. The three-band limit persists. This observation does not authorize arbitrary metrics or relax the source-selection requirement.

## Full-generator obstruction and residual scope

For an even padded clock length n=2M, the programme spectrum is κ{-n,-n+2,…,n}, hence positive targets 2κ,4κ,…,2Mκ. Assume the literal generator comparison uses Hnative=iÂG, fixed energy origin, a common rate adjustment and any number of **identical-parameter uncoupled copies**, with an isometry E and exact Hnative E=E Hprogramme.

Each programme eigenvector must map to a native eigenvector with the same eigenvalue. Identical copies increase multiplicities but never add positive frequencies. Thus M≥4, equivalently n≥8, is impossible in this class. For the default n=10 there are five positive targets and at most three positive centers. This is a scoped NO-GO for exact full-generator intertwining; it is not a no-go for endpoint matching, prepared-state-only matching, different complexes or all UD models.

For any programme eigenvalue λ and unit eigenvector v,
\[
\|(H_{\rm native}E-EH_{\rm programme})v\|
=\|(H_{\rm native}-\lambda I)Ev\|
\ge \operatorname{dist}(\lambda,\operatorname{spec}H_{\rm native}).
\]
The relative residual η/κ is therefore at least the worst nearest-spectrum distance. In the relaxed n=10 three-free-positive-center comparison, a radius below 1 can cover at most one positive target per center because adjacent targets differ by 2; zero covers no positive target at that radius. Three centers cannot cover five targets. Radius 1 is attained with centers 3,7,10, giving positive distances (1,1,1,1,0). With sufficient multiplicity and unrestricted spectral encoding, this bound is sharp for the relaxed operator comparison. It is not a prediction that native couplings take these values.

At T=π/(2κ), Tη≥π/2. Duhamel provides an **upper** estimate of evolution mismatch by Tη. A floor on this upper-budget quantity does not imply actual mismatch is at least π/2, and cannot supply an endpoint error lower bound. The already published endpoint counterexample remains applicable. No source-selected encoding, uncertainty, locality or acquisition model follows from the optimization.

## Exclusions and next source gate

The proof does not exclude heterogeneous uncoupled copies, copy-to-copy coupling, a different/refined complex, S4-breaking metric assignment, non-skew Hermitian equivariant Hamiltonians, or approximate/state-restricted/endpoint-only admission. These require new declared operators and fresh tests. The entire self-adjoint commutant is not the three-dimensional skew family; allowing it would change this contract. Adding an arbitrary scalar energy shift also changes the literal generator comparison and must be declared explicitly.

The next lawful bridge input remains a source-authored choice of complex, metric/coupling rule, conserved pairing, encoding and rate law. A target-blind choice may then be tested using the complete residual and separate endpoint/export errors. Merely choosing parameters to attain the optimized centers closes no native source gate. Protected export and complete clock/restart supply remain separate OPEN obligations.

## Exact text-field hashes

| Catalog ID | SHA-256 |
|---|---|
| C0258 | d4f8931ac5843205459e48c666d9c9319288261f3c678c7341120fae54a5f073 |
| C0769 | 039244bbe9e685801035d2d1cbe9f6ad58c92e9fc5a6f068ba9a658da8df2b19 |
| C0190 | f8043eb1183a97f89b7a1c3f9e12ba37b96d3b0e411222a38130d39808d327dd |
| C0200 | 79e5812b88ba89c96830db9adee87ba1f54d545ba34d49a799d1962acb1b4a79 |
| C0187 | b162b8c0f7535ce90de6f420d9237d4132bb645e1d1baca1071eb1a75e53e449 |
| C0173 | a1e338c059bdb0aa426ba97a5e2d4436c6ca931eefa0f4d2ad1d9e49c0699d4f |
| C0176 | 42132ec1235cb30837c68d94c6adf41ef37a79e1d48ae5f302e432a4acc2474d |
| C0473 | d979a0e5d77e78eee5ea996045e9cc9acaf02ecb0c03ddc24c01533e0db7140a |
| C0496 | 05200f695017e1e4a381af0eac824df7410c6b570e856b94fe0c92b12e4567ac |

This report contains direct source reading and written algebraic scope checks. It reports no hardware data, external peer review or registry promotion.
