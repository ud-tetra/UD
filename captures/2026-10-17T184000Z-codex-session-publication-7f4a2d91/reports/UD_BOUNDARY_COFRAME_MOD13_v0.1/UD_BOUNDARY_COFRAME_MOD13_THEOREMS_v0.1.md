# UD boundary, coframe and mod-13 theorem audit v0.1

2026-10-16 UTC. Development — no registry entry. Constructor: Codex. Non-constructor review: pending. Physical promotion: 0.

## Scope and provenance

This addendum corrects the user-supplied research in the present session; it does not attribute its unsupported claims to accepted UD theory. All new theorems below concern explicitly declared finite mathematical models. They do not supply spacetime, a physical clock, gauge identification, or an experimental bridge.

Repository source snapshot: `840e46a4f631a05f7a5992a07bcdf70c733c5dd5`. Relevant source documents: `docs/UD_600Cell_Hopf_Sector_Assessment_v0.1.md`, sections “Declared carriers”, “Invariant-sector theorem”, and “Gauge and physical bridge limits”; `docs/UD_600Cell_Reduced_Dynamics_v0.1.md`, sections 1–5 and Appendix A. The former pins its exact 600-cell construction and the latter supplies algebraic spectra; neither is replayed in full here. Uploaded ledger v0.39 (2026-08-22), Q169–Q179, is historical source input; it is not substituted for the October repository. Uploaded governance CRL-2 v1.0 labels itself a proposal. Its development/registry and independent-review distinctions are preserved without claiming adoption.

Group reference: Tim Dokchitser, GroupNames, SL(2,5), https://people.maths.bris.ac.uk/~matyd/GroupNames/97/SL(2,5).html, subgroup list and character table, retrieved 2026-10-16. This is the original database source used for the ordinary character values. The replay separately enumerates SL(2,5), verifies perfectness and computes the Q8 character inner products.

`Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used. No definition of the proposed UD-specific M_e, its actual frame/link data, or a new C13 constitutive source was supplied. Here E denotes a newly declared edge coframe; it is not silently identified with an existing M_e.

## T1 — Carrier and boundary bookkeeping (EXACT, conditional on declared triangulation)

Let K triangulate the boundary of the regular 600-cell, with nonaugmented chains over a field F and f=(120,720,1200,600). Then dim C_*(K)=2640 and K is a closed 3-sphere: its manifold boundary is empty. A shell L must be separately chosen, for example L=boundary P for an embedded triangulated 3-ball P. The identity boundary squared=0 does not produce an S2 boundary of S3.

If L is a triangulated S2, triangle-edge incidence gives 3F=2E; Euler gives V-E+F=2. Consequently E=3V-6, F=2V-4 and dim C_*(L)=6V-10=2E+2. The supplied formula 2V+2E-2 is incorrect (already 18 rather than 14 for V=4).

For the canonical signed coordinate inclusion i:C_*(L;F)→C_*(K;F), i^T i=I, so R=i^T is surjective, rank R=dim C_*(L), and nullity R=2640-dim C_*(L). This conclusion uses the inclusion, not just an upper bound on rank. A different transfer map requires its own rank calculation. A metric adjoint has the same rank for nonsingular metrics but is not necessarily the coordinate projection.

| Declared shell | f | Chain dimension | Nullity in the fixed 2640 carrier |
|---|---|---:|---:|
| Single tetrahedron boundary | (4,6,4) | 14 | 2626 |
| Boundary of a 2↔3 ball | (5,9,6) | 20 | 2620 |
| Icosahedral shell | (12,30,20) | 62 | 2578 |

The icosahedral row is realized by a vertex link in K. A link is a subcomplex, not the manifold boundary of K. These examples do not bound all possible embedded shells. The fractions 2626/2640=1313/1320 and 2578/2640=1289/1320 count instantaneous linear invisibility in those examples, not physical information destruction. If K itself is replaced by a 2→3 move, its total dimension increases by four; holding 2640 fixed then needs an explicit ambient-carrier convention.

Proof: the incidence and Euler equations above, followed by rank-nullity and the displayed inclusion identity.

## T2 — Reconstruction obstruction and admissibility criterion (EXACT / NO-GO)

Let R:X→Y be a surjective linear map with dim X=n>m=dim Y. Every right-inverse J:Y→X satisfies RJ=I_Y and rank J=m. No such J can satisfy JR=I_X: rank(JR)≤m<n. Every datum y has affine solution fibre Jy+ker R. Calling ker R gauge is an additional physical/model equivalence declaration, not a consequence of projection.

For a declared admissible linear subspace W⊆X, unique recovery holds exactly when W∩ker R={0}; thus dim W≤m. For constraints Cx=0, uniqueness is equivalent to ker R∩ker C={0}, or rank [R;C]=n, and any y still requires consistency with C. Side measurements Qx allow recovery exactly when [R;Q] has full column rank; rank Q must be at least n-m. Geometric compatibility may select a smaller W, but cannot recover arbitrary discarded states without further data. An edge coframe E:C1→F^4 also cannot satisfy E^T E=I on a nondegenerate chain space of dimension greater than four: rank(E^T E)≤4. Isometry on a smaller declared subspace is a separate possible contract.

Proof: compare x and x+z, z∈ker R, and apply the rank test to their difference. No injective group homomorphism from the additive F13-chain space into additive R4 exists: 13x=0 implies 13M(x)=0 and hence M(x)=0. Thus “linear mod-13 coframe into real geometry” is ill-typed without a separate lifting/encoding contract.

## T3 — Correct flat-coframe equations and Pachner extension (EXACT)

For a finite complex P, take B1:C1→C0 and B2:C2→C1 in sorted oriented simplex bases. Declare a trivial fibre F^d and an edge coframe E:C1→F^d, a d×n1 matrix. Its untwisted face closure, here called torsion, is T=EB2. The statement B1B2=0 implies T=0 only when E factors through B1, not for arbitrary E. The supplied expression B1^T M_e(f)-M_e(B2 f) is undefined for a map M_e:C1→F^4: it applies the edge map to a face and mismatches matrix types.

Let P_-={0123,0124}, P_+={0134,0234,1234}, with all faces included. Their f-vectors are (5,9,7,2) and (5,10,9,3); the shared outer sphere has (5,9,6). Both are contractible. Hence every E_-B2,-=0 is E_-=XB1,- for a vertex potential X, unique up to a constant vector. Retain the nine old edges and define

    E_34=X_4-X_3=E_04-E_03.

Then E_+=XB1,+ is flat on every new face. Conversely, the new face 034 forces exactly that value, so the extension is unique. For a prescribed new value v, the three sorted faces 034,134,234 each have defect v-(X_4-X_3). Choosing v incorrectly creates a nonzero defect; retriangulation itself does not force one. If v is unspecified return UNDEFINED_NEW_EDGE, not FLATNESS_VIOLATED.

The flat scalar coframe dimension is 4 on either ball and on their common sphere; for d=4 it is 16. Without flatness, edge coframe dimensions are 36 and 40. If a different patch has H^1≠0, closed need not mean exact and period data must be checked.

Incidence algorithm:
1. Enumerate sorted simplices and construct Bk by deleting vertex r with sign (-1)^r.
2. Verify B1B2=0 and B2B3=0 independently of coframe flatness.
3. Check input E_-B2,-=0; otherwise return INPUT_NONFLAT.
4. Solve E_-=XB1,- with X_0=0. Preserve all old edge values.
5. If new edge is unspecified, either return UNDEFINED_NEW_EDGE or explicitly invoke the flat extension rule above.
6. Construct E_+, evaluate E_+B2,+ over the declared field, and verify common boundary columns in common edge coordinates.
7. Return FLATNESS_PRESERVED, INCONSISTENT_EXTENSION, or SOURCE_BLOCKED_CONNECTION as appropriate.

The replay checks all 13^4=28,561 scalar potential classes over F13. Vector-valued results follow componentwise by the proof.

For a nontrivial connection, declare G_ab transporting fibre b to a, G_ba=G_ab^-1, and e_ab in fibre a with e_ba=-G_ba e_ab. The typed triangular torsion and curvature are

    T_abc=e_ab+G_ab e_bc-e_ac,
    H_abc=G_ab G_bc G_ca.

Under frame changes h_a, use G'_ab=h_a G_ab h_b^-1 and e'_ab=h_a e_ab; then T'_abc=h_a T_abc and H'_abc=h_a H_abc h_a^-1. T=0 and H=I are separate conditions. A pure-gauge flat construction G_ab=U_a U_b^-1, e_ab=U_a(x_b-x_a) satisfies both. No actual UD source for these links is asserted.

## T4 — Snapshot kernel versus dynamical observability (EXACT)

For real x'=Ax and y=Rx, define O=[R;RA;...;RA^(n-1)]. Two initial states have identical continuous output histories exactly when their difference lies in N=ker O. N is the largest A-invariant subspace contained in ker R. Proof: differentiate Re^(tA)z at t=0; Cayley-Hamilton reduces all higher powers to the displayed stack, and the exponential series gives the converse. For a sampling protocol, use its actual sampled observability matrix instead; continuous observability does not guarantee well-conditioned finite sampling.

Thus a boundary-hidden snapshot may become visible later through coupling. A=A_osc=[[0,-w],[w,0]], R=[1,0], w≠0 is a two-dimensional counterexample to automatic clock extinction: ker R is one-dimensional but O has rank two. The frequency is recovered from output history. The full 600-cell boundary observer is NOT computed in this audit. The local sqrt(2),sqrt(3),sqrt(5) controls cannot be assigned wholesale to a 600-cell kernel; the repository already has a richer exact 600-cell spectrum.

If A is skew and i is coordinate inclusion, ||Rx||²+||(I-iR)x||²=||x||². Projection conserves the entire norm only on im i. A right-inverse does not change this. Norm preservation on a declared reduced admissible subspace requires a metric/isometry theorem. Over F13 the dot form is not positive: (1,5) has squared value 1+25=0 while nonzero. It is not real positive support or a derived Lorentzian metric.

## T5 — Character sectors require equivariant observation (EXACT, conditional)

Use the repository's complex C10 sectors V_m of dimension 264, not ten real sectors. For R with target dimension m_B, dim(V_m∩ker R)=264-rank(R|V_m)≥264-m_B. Hence shells of dimensions 14,20,62 give lower bounds 250,244,202 per complex sector. These are bounds, not computed sector ranks. A general kernel need not be the direct sum of these intersections: cancellation between sector images is possible.

A boundary action T_L with RT=T_L R exists precisely when ker R is T-invariant, for surjective R. Proof: define T_L(Rx)=RTx and test independence of representative. If the shell is a T-invariant subcomplex, the natural signed action supplies this relation and ordinary character restriction is meaningful. An arbitrary patch need not preserve C10. The real source decomposition is 264+264+4×528. No assertion of all-sector destruction or exact boundary branching follows from dimension counting alone.

## T6 — Mod-13 arithmetic does not supply synchronized phase clocks (EXACT / NO-GO)

Distinguish the additive group C13=(F13,+), the multiplicative group F13^× of order 12, and complex phase roots μ13. Because x^13-1=(x-1)^13 in characteristic 13, F13 and its algebraic closure contain no nontrivial 13th root of unity. For a linear C13 action U over F13, (U-I)^13=0. Nontrivial actions are unipotent, e.g. [[1,1],[0,1]] has order 13; they are not a semisimple 13-phase Fourier clock. A complex phase encoding r↦exp(2πir/13) is instead a representation of the additive group in U(1); it does not preserve field addition and multiplication as a map of scalar fields.

The nonzero square residues are {1,3,4,9,10,12}. They create no forbidden transition unless a source-selected admissibility law actually uses the quadratic character. Neither parity Θ nor synchronized updates follows from this list. F13 has cube and fourth roots in its multiplicative group, but no fifth or tenth roots since 5 does not divide 12.

For additive edge connections a_ab∈F13, face flatness is a_ab+a_bc-a_ac=0. On S2 or S3, H1(-;F13)=0, so every cycle has zero holonomy for a flat connection. Nonzero holonomy requires curvature, defects or a different topology. Discrete values alone imply neither flatness, synchrony nor absence of drift under an unspecified update law.

## T7 — Binary icosahedral obstruction and legitimate restriction (EXACT / NO-GO)

SL(2,F13) has order (13²-1)13=2184=2³·3·7·13. Since 2I≅SL(2,F5) has order 120=2³·3·5, Lagrange forbids the proposed injection 2I→SL(2,F13). The ratio is 91/5, not an integer. No C13 or D13 of order 26 is a subgroup of 2I. More strongly every homomorphism 2I→C13 is trivial by the image-order divisor test; every homomorphism into D13 has image order at most 2 and is trivial because 2I is perfect. The replay verifies perfectness by enumerating commutators in SL(2,F5).

This does NOT forbid higher-dimensional F13 representations: the regular representation exists, and 13 does not divide 120, so Maschke semisimplicity applies to F13[2I]. A chosen integral model can be reduced at a declared prime; it is not restriction to a nonexistent C13 subgroup. Gold-ratio coordinates require an extension because 5 is a non-residue mod 13; F169 accommodates a root of t²-t-1. Scalar reduction is not a canonical ring map R→F13. In fact no unital ring map R→F13 exists. For the free C10 chain action, x^10-1=(x-1)(x+1)Φ5(x)Φ10(x), where both quartics are irreducible over F13 since 13 has multiplicative order four modulo five and ten. Consequently the F13 carrier decomposes into isotypic dimensions 264+264+1056+1056, rather than ten one-dimensional-character blocks. A splitting field needs degree four. These are representation blocks, not physical boundary modes.

The full 600-cell rotational group is (2I_L×2I_R)/{±(1,1)}, order 7200, as already established in the repository source. A single 2I is a subgroup, not that whole rotation group. No “fragmentation over the boundary field” follows without an actual group action preserving the chosen shell.

There IS a legitimate ordinary complex restriction to a chosen Q8 subgroup. Denote its four one-dimensional characters 1,χ1,χ2,χ3 and its unique two-dimensional irrep σ. For irreps of 2I, with central parity indicated for the two inequivalent four-dimensional irreps:

| 2I irrep | Restriction to Q8 |
|---|---|
| 1 | 1 |
| 2,2′ | σ (each) |
| 3,3′ | χ1+χ2+χ3 (each) |
| 4, central +1 | 1+χ1+χ2+χ3 |
| 4, central -1 | 2σ |
| 5 | 2·1+χ1+χ2+χ3 |
| 6 | 3σ |

Proof: use Q8 class sizes (1,1,2,2,2). The character restrictions are (d,z,t,t,t), with (d,z,t)=(1,1,1),(2,-2,0),(3,3,-1),(4,4,0),(4,-4,0),(5,5,1),(6,-6,0). Take character inner products divided by 8. This table is ordinary complex branching; it does not assume all 2I irreps split over F13, and does not calculate the actual shell carrier multiplicities.

## T8 — Explicit Q8 over F13 (EXACT)

The supplied eight matrices are correct:

    1=[[1,0],[0,1]]       -1=[[12,0],[0,12]]
    i=[[5,0],[0,8]]       -i=[[8,0],[0,5]]
    j=[[0,1],[12,0]]      -j=[[0,12],[1,0]]
    k=[[0,5],[5,0]]       -k=[[0,8],[8,0]]

They are distinct, have determinant one, satisfy i²=j²=k²=ijk=-I, and close under all 64 products. They faithfully realize Q8 in SL(2,F13). With J=j they obey g^T J g=J. They do not preserve the standard dot product: i^T i=-I. Indeed any symmetric 2×2 matrix H invariant under i has zero diagonal; invariance under j then forces its off-diagonal entry to vanish. Thus no nondegenerate symmetric invariant form exists in this particular 2D module, although its alternating form is nondegenerate. This distinguishes symplectic from orthogonal framing.

This exact finite representation supplies neither a map from the three-bit Θ fibre nor error correction for measurements. Those need explicit actions, encoding/decoding and fault contracts.

## Corrections register and next gate

Rejected as stated: boundary(S3)=S2; erroneous Euler dimension formula; generic norm conservation by projection; gauge status of a projection kernel; full kernel reconstruction by a right-inverse; mandatory Pachner torsion violation; nilpotence implying connection flatness; real/F13 scalar mixing; SL2(F13) embedding of 2I; C13/D13 subgroup fragmentation; automatic parity sieve/synchrony; all microfrequencies confined to the snapshot kernel. Valid narrower statements and their assumptions are T1–T8 above. These corrections address the supplied proposal, not retractions of accepted UD results.

Highest-value next task: choose an actual 600-cell shell, its real/complex readout R, generator A and any admissibility constraints; compute its dynamical unobservable subspace and sector-resolved observation ranks, then test finite-sample conditioning. Track under existing project issue #136 (REF01, metrics/observables); a measurement implementation also depends on #144 (APP05). Do not inject C13 as a source-free repair.

## Reproduction

Run `python verify.py` with Python and SymPy. `results.json` records exact finite checks, the Q8 matrices and the ordinary branching multiplicities. No floating-point tolerances are used. Written proofs establish the general results; finite replay checks cover only the local complexes and listed arithmetic. Full 600-cell observability and independent non-constructor review remain OPEN. No registry or physical promotion, site publication or main-branch merge is claimed.
