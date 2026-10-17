# UD parallel research reconciliation

**RESULT — Relevant mathematical ingredients, but the claimed frozen gauge bridge fails exact checks.** Preserve the existing observability results, repair the finite arithmetic in a separate development module, and quarantine the index, anomaly, continuum and coupling claims. Physical promotion remains **0**. This is constructor verification, with independent review pending and no registry entry.

The reviewed source is the supplied 4106-line conversation, identified by its SHA-256 in `PROVENANCE.json`. Line numbers below refer to that exact export. The review targets its major dependency chain, monograph, appendix and final code. It is not a formal verification of every sentence or a review of an unseen original package. The literal attachment was inspected statically; none of its code or deployment commands was executed.

## What transfers to the current research

| Ingredient | Decision | Scope |
|---|---|---|
| 600-cell chain dimension 2640 and Betti numbers (1,0,0,1) | ADOPT existing result | The tetrahedral boundary is a 3-sphere. A selected vertex link is a 2-sphere; the 3-sphere itself has no manifold boundary. |
| Icosahedral link with 62 chain coordinates | ADOPT existing result | Snapshot rank 62, kernel 2578 for coordinate restriction. |
| History rank 1893, hidden dimension 747, derivatives through order 104 | ADOPT existing result | Specific unit-metric, unit-rate generator and single-link observer. Repetition in the parallel conversation supplies no independent replication. |
| Ten complex 264-dimensional character sectors | ADOPT with coefficient field specified | Over the reals: two 264-dimensional blocks and four 528-dimensional conjugate-pair blocks. Observation ranks cannot be summed because the selected observer is not equivariant. |
| Quaternion generators over the base field | REPAIR final code | The earlier generators are valid. Correct the final negative-k matrix to `[[0,8],[8,0]]`. All 64 products close in the repaired group. |
| Quadratic/cubic subfields and sextic compositum | ADOPT conditional algebra | For genuine fields inside a common algebraic closure, intersection is F13 and compositum is F_(13^6). Trace transitivity is valid. The proposed cubic polynomial is not. |
| Norm-one subgroup of order 183 | REPAIR construction | Valid in a genuine cubic extension. It supplies neither an error-correcting code nor a physical clock without further definitions. |
| Gauge groups, anomaly cancellation, invariant 1146-plane, physical running couplings | QUARANTINE | The necessary representations, operators, identities, limiting maps and operational correspondence are not established; several stated supporting equations are false. |

## Decisive exact failures

**1. The declared cubic field is not a field** (source line 3058):

\[
x^3-x-2=(x-6)(x+3)^2\quad\text{in }\mathbb F_{13}[x].
\]

The quotient has a nonzero square-zero element, represented by `(x-6)(x+3)`. Field inverses and Frobenius-orbit conclusions cannot be applied to it as written. A concrete repair is `F13[a]/(a^3-2)`: the cubic has no base-field root, hence is irreducible. The audit constructs a primitive multiplicative generator `a+a^2`, and

\[
\beta=7+2a+11a^2,
\qquad \operatorname{ord}(\beta)=183,
\qquad \operatorname{Norm}(\beta)=1.
\]

Its Frobenius orbit is `(7,2,11)`, `(7,6,8)`, `(7,5,7)` in the basis `(1,a,a^2)`. This repairs an arithmetic example; it does not repair the gauge interpretation.

**2. Integer reduction modulo 13^6 does not implement F_(13^6)** (lines 3791–3794). The integer residue ring has characteristic 13^6, a nonunit 13 and nilpotents. The field has characteristic 13 and requires polynomial-extension arithmetic. Even source notation `mod 13^6` is incorrect when intended to mean field arithmetic.

**3. The inter-sector constraint is impossible** (lines 3060–3063). For a 3-by-2 matrix over any field,

\[
\operatorname{rank}(KK^\dagger)\le2<3
=\operatorname{rank}(2I_3).
\]

This holds for transpose or a well-defined conjugate transpose. The code's specific K gives `K K^T = [[0,10,0],[10,0,0],[0,0,0]]` modulo 13. Its assembled 5-by-5 transport matrix Omega has **integer determinant zero and modular rank four**. Therefore Omega inverse does not exist over the base field or any extension; the proposed transport cannot execute even after the syntax is repaired. The final negative-k matrix is separately singular.

**4. The alleged octet simulation cannot produce its claimed result** (lines 2002–2067). It replaces the actual incidence generator and selected observer with random dense matrices, and stacks one trajectory into a **6510-by-1 column**. Its SVD rank is at most one. At rank one every sampled skew generator is the zero 1-by-1 matrix. More generally, `trace(S J)=0` whenever S is real symmetric and J is real skew, so the proposed trace projection is zero in exact arithmetic. The prose assertion of nonzero octet coefficients contradicts the supplied algorithm. Constructing O by stacking the matrices `R A^k` is different from constructing the single vector `O x`.

**5. 1146 is a rank-minus-nullity arithmetic difference, not the stated index theorem** (lines 2543–2558 and 3088–3095). Here O is 6510-by-2640 with rank 1893, so

\[
\dim\ker O=747,\quad
\dim\ker O^T=4617,\quad
\operatorname{ind}(O)=-3870.
\]

For the square real Gram operator `H=O O^T`, the Fredholm index is **0**, since H is symmetric. The difference `1893-747=1146` does not identify a subspace, a topological invariant, or an anomaly count. O is an observability matrix; its Gram matrix is not by definition a system-identification Hankel matrix.

**6. The central-cover argument is false** (lines 3043–3049). Steinberg's central-extension theorem states that `SL_n(F_q)` is centrally closed for finite fields and n at least five. Thus `H_2(SL_5(F_(13^6)), Z)=0`, rather than Z2. Independently, `det(-I5)=-1`, so the proposed parity element is not in SL5 in characteristic 13. The centre of this particular SL5 has order `gcd(5,13^6-1)=1`. See Steinberg, *Lectures on Chevalley Groups*, central extensions, Corollary 2:
https://math.soimeme.org/~arunram/Resources/LOCGS7CentralExtensions.html

**7. The subdivision counts mix dimensions** (lines 3114–3122). For unaugmented full chains, a 4D 1-to-5 move changes the f-vector by `(1,5,10,10,4)`, increasing total dimension by **30**, not 15. On the original tetrahedral 3-complex, the applicable moves include 1-to-4 with increase **14**, and 2-to-3 with increase **4**. Applying 4D bistellar moves requires a new 4D carrier and source matrices; the 2640-dimensional boundary carrier does not contain 4-simplices.

**8. Nilpotency does not imply orthogonality or torsion freedom.** For `N=[[0,1],[0,0]]`, N squared is zero, but `(I+2N)^T(I+2N)=[[1,2],[2,5]]` modulo 13. The coframe closure condition is a separate equation. Over finite fields, preservation of `c^T c` is also not preservation of a positive real norm: the nonzero vector `(5,1)` has modular squared length zero.

**9. The final fraction and baseline disagree with the claimed 3/8** (lines 3142–3150 and 3803–3804, 3914–3917):

\[
\frac1{1+3/5}=\frac58\ne\frac38.
\]

The final code's initial inverse couplings `(3,2,1)` give its plotted ratio `1/(2+1)=1/3`; the 3/8 annotation is a reference string. The beta coefficients are assigned as literals rather than computed from the complex or character matrices. Standard SU(5) normalization can conditionally yield 3/8: choose `Y=diag(-1/3,-1/3,-1/3,1/2,1/2)` and `T3=diag(0,0,0,1/2,-1/2)`; then `Tr(Y^2)=5/6`, `Tr(T3^2)=1/2`, and a common normalized coupling yields `(3/5)/(1+3/5)=3/8`. Those are extra embedding and coupling assumptions. Block sizes alone do not select the hypercharge generator. The historical SU(5) proposal is Georgi–Glashow, DOI 10.1103/PhysRevLett.32.438; the accessible publisher abstract supports its SU(5) premise, not a UD derivation.

**10. Universal recurrence and group fragmentation are unsupported.** The identity has period one; a quaternion generator has order four; `I+E12` in SL3 has order 13 in characteristic 13. Neither 2196 nor 114924 is even divisible by 13, so neither can be a universal period for the stated unrestricted groups. A time-varying sequence of transitions needs its own update law and state-space proof. Also, `120` does not divide `2184=|SL2(F13)|`; an order-120 group cannot embed there. Any homomorphism from 2I to C13 is trivial, and D13 of order 26 cannot be a subgroup of 2I. Changing coefficients does not furnish these branching maps.

The final class also fails static parsing at source line 3823 (`for m in:`). Missing iterables could be an export defect; the independent algebraic contradictions remain. The package section supplies a build recipe and a placeholder for core.py, not a wheel, verified build transcript, committed repository state or reproducibility certificate.

## New compatibility result for our sectors

To split C10 into all ten one-dimensional characters over F_(13^d), the field must contain a primitive tenth root:

\[
10\mid13^d-1,\qquad \operatorname{ord}_{10}(13)=4.
\]

Over F13, Frobenius sends m to 3m modulo 10, producing orbits `{0}`, `{5}`, `{1,3,9,7}`, `{2,6,8,4}`. The factor degrees of `x^10-1` are **1,1,4,4**. Over F_(13^6), Frobenius on characters sends m to minus m, so there are two fixed characters and four conjugate pairs, rather than ten separate character lines. The sextic field is therefore compatible with an **unsplit paired-block description**, but not with ten independently scalar-valued character projectors.

If both the full character splitting and the proposed sextic coefficient arithmetic are required, their smallest common extension is F_(13^12). This is a coefficient-field requirement, with no gauge-group implication. It does not assert that the real spectral or conditioning certificates survive reduction modulo 13.

Trace maps are another useful warning: `Tr_(13^6/13)` is a surjective F13-linear map of rank one and kernel dimension five, since `Tr(1)=6`. Correct trace identities do not imply information preservation or a nondegenerate mixing map. Frobenius powers commute because they belong to one cyclic Galois group; extension-degree mismatch does not by itself generate a nonabelian braid.

## Impact on our observer and validation program

| Observer | History rank | Dynamical kernel | Status |
|---|---:|---:|---|
| One vertex link, 62 channels | 1893 | 747 | Existing exact result for the frozen nominal model |
| Two vertex links and tetrahedral port, 125 channels | 2498 | 142 | Existing exact result; reduction by 605 from the original kernel |
| Three links, tetrahedral port and face/edge/vertex ports, 189 channels | 2640 | 0 | Existing exact full-state result |

The parallel text repeatedly treats 747 as a permanent intrinsic stock. Our augmented observers already disprove that interpretation: it is a property of the pair `(R,A)`. With no dynamics changed, additional readouts remove that dynamical kernel. A right inverse of R still cannot reconstruct arbitrary hidden states from one snapshot; history and extra observations provide additional information.

Our latest compressed validation uses **260 preparations**, 295974 scalar outputs and a declared family of local readout errors and matching same-grade metric defects. Its conditional later-history condition bounds remain **less than 783, 391 and 328** for the three frozen sample lengths. These are inherited results, not rerun or enlarged by this audit. They require the specified real dynamics, preparation errors, time jitter, background uncertainty and temporal stability contracts. Finite arithmetic supplies no instrument-error bound and no extension to excluded faults.

There is no specified additional noncommuting generator in the proposed Lie-algebra extraction. A alone generates a Lie algebra of dimension at most one, because `[A,A]=0`. A large observable space can support many representations, but observing its dimension does not select SU3, SU2 or U1. Vanishing intermediate simplicial homology also does not prove quantum anomaly cancellation.

## Recommended integration contract

Use the repaired finite arithmetic as an **algebraic verification module and source of candidate challenge transformations**. Keep the existing real observer, calibration and conditioning certificates as separate typed objects. The immediate work item is a compatibility test, not deployment of the supplied automaton.

For each proposed finite symmetry or coframe transition, supply explicit matrices and require:

1. A genuine field construction, invertible group elements and the intended bilinear or Hermitian form. Choose either paired C10 blocks over the sextic field or full splitting over a compatible field.
2. Degree-correct chain maps with `B' S = S B`. For an edge-valued coframe E, ordinary closure is the dimensionally valid `E B2=0`. With connection matrices G, torsion and curvature are separate constraints; for example `e_ij + G_ij e_jk - e_ik=0` and `G_ij G_jk G_ki=I` under stated frame conventions. Incidence nilpotency alone proves neither.
3. An explicit observation intertwiner `R S = S_out R` whenever sectorwise observation claims are made. If it fails, preserve the mixed-sector analysis rather than adding sector ranks.
4. A defined mapping to real model parameters or real fault matrices. For real transport K and metric H, test `H>0` and `K^T H+H K=0`, then recompute the observation bounds or check the frozen robustness hypotheses. There is no nonzero additive homomorphism from a finite-field vector space into a real vector space, so a real-linear geometric reconstruction is not supplied by field notation.
5. For each candidate fault, test whether it lies inside the frozen local family and whether the 260-code schedule detects it. A passing modular checksum cannot certify finite-sample conditioning, real norm conservation or excluded-fault coverage.

No previous capture is overwritten. The parallel conversation's internal freeze declaration is source content, not authority over this reconciliation. Failed parent claims leave their dependents pending re-derivation. Physical promotion stays zero; independent review is still required for stronger status.
