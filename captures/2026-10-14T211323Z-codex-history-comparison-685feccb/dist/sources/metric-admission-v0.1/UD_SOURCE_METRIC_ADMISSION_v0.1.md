# Source metric families and full clock admission v0.1

Date: 2026-10-14. Public reading edition 0.10. Lane: development — no registry entry. Physical promotion **0**. Constructor-team AI verification is not independent human review. Native parameter selection, preparation, encoding, readout and protected export remain OPEN.

## 1. Contract and source provenance

The retained finite programme has even padded clock length n=10 and positive generator frequencies κ{2,4,6,8,10}, each with full retained payload multiplicity Q. The exact contract is Hnative E=E Hprogramme for a complete isometry E, including clock, work, history, receipts and donor/outgoing bank. Native operators use a fixed energy origin and Hnative=iγA after metric normalization. A positive common rate γ and arbitrarily many identical uncoupled copies are allowed as a mathematical relaxation. Copies share the same metric, geometry and coefficients. They increase multiplicities, not the set of frequencies.

The candidate programme, its finite window and reset accounting remain as published in joint-carrier v0.1 and programmed-clock v0.1. No full default-sized matrix is materialized here. The spectral obstruction applies to the entire encoded domain regardless of dimension because every target eigenvector must map to a native eigenvector of the same eigenvalue. It also holds after the prefix-word conjugation, which preserves the target spectrum.

Source text is recovered from the existing public atlas catalog, not from unexported GPT memory. Exact UTF-8 content snapshots and SHA-256 provenance accompany this release. They identify extracted catalog text; they do not claim recovery of original manuscript/PDF bytes. Imported source programmes were not executed. The unavailable Gap2 image was not used.

| Source | Role |
|---|---|
| C0258, Paper III review 1.1.1 §§2.1–2.3 | Signed S4 chain decomposition and commutant dimensions |
| C0769, Paper I review 1.1.1 | Unit-metric baseline; correct adjoint under metric change |
| C0190, Exact S4 chain projectors | Complete real equivariant skew family and factor 2 |
| C0173, Geometric inner-product interface | Fixed-boundary metric adjoint; coordinate-defined Gram Rules A/B |
| C0176, Chain semantics and weighted receipts | Conserved pairing and coefficient/stock distinction |
| C0473, Pachner 2↔3 Hodge Dirac Move Response | Degree-coupled Kminus/Kplus spectral polynomials |
| C0496, Tagged Load, Response Capacity and Pachner Spectral Change §9 | Repair of inverse-product versus metric-adjoint conventions |

The source/scope review also reads C0187 and C0200. No source selects numerical couplings to fit this clock. Rules A and B are alternative source-authored candidates; their consistency does not select one physical metric. Historical ledger and CRL proposal are provenance, not new parameter authority.

## 2. Metric conventions must remain distinct

Let Bk:Ck→C(k−1) be the fixed increasing-orientation boundary. With positive degree metrics Gk=gk I, the fixed-boundary adjoint is Bk†=Gk⁻¹ Bkᵀ G(k−1). Set L=B†−B. The conserved quadratic pairing is cᵀGc, and y=G½c gives a Euclidean skew generator:

**Fixed-boundary metric-adjoint convention:** Â=G½LG⁻½=Σ tk Ak, tk=√(g(k−1)/gk).

Here Ak has −Bk in the degree-lowering block and +Bkᵀ in the reverse block. A1 connects C0/C1 (standard V or T2); A2 connects C1/C2 (V⊗ε or T1); A3 connects C2/C3 (ε or A2). Representation names and generator names are distinct. The unit-metric A0=A1+A2+A3 has positive frequency 2, not 1.

**Mass-equation convention:** G ċ=A0c normalizes to G⁻½A0G⁻½, with tk=1/√(g(k−1)gk).

The inverse-product formula in historical C0473 is valid under the latter convention, as repaired in C0496§9. It is not the adjoint of the unchanged Bk with the changed metric. The historical opposite overall sign reverses evolution direction but preserves paired frequencies. Multiplying every gk by s leaves the ratio-convention rates unchanged and scales the mass-convention rates by 1/s. Both conserve their declared pairing; neither licenses a physical norm/energy identification.

## 3. Full S4-invariant skew family

Theorem MF.1. On the filled tetrahedron's real signed chain carrier, every Euclidean-skew S4-equivariant generator is A=aA1+bA2+cA3. Its characteristic polynomial is

λ(λ²+4a²)³(λ²+4b²)³(λ²+4c²).

Source projectors satisfy AiAj=0 for i≠j and Ai²=−4Pi. Their ranks are 6,6,2; the harmonic projector has rank1. The full commutant has dimension13, its self-adjoint part10 and its skew part3. Each repeated irreducible has a two-dimensional real multiplicity space, whose skew endomorphisms have one parameter. Symmetry does not choose a=b=c=1: that value follows from the separately declared unit-boundary/adjoint operator.

Any fixed positive S4-invariant metric G commutes with the signed action, as does G½. Normalizing any real G-skew equivariant generator by G½ therefore puts it back in this same three-dimensional skew commutant. Thus at most three positive bands persist, even when an invariant metric mixes equivalent representation copies. This statement concerns real skew generators and H=iA; it does not classify every complex Hermitian equivariant Hamiltonian.

Corollary MF.2. For even n≥8, exact full-generator admission into any number of identical-parameter copies in this class is impossible: n/2≥4 distinct positive clock frequencies cannot fit in at most three native bands. Zero coefficients or coincident magnitudes reduce the number of bands. The conclusion does not extend to arbitrary symmetry-breaking metrics or larger S4 carrier multiplicities.

For degree-isotropic fixed-boundary metrics the bands are explicitly 2√(g0/g1), 2√(g1/g2), 2√(g2/g3), with signed multiplicities3,3,1. The ability to realize an arbitrary positive triple algebraically is a parameterization, not source selection.

## 4. Three-band residual relaxation

Theorem MF.3. Against positive targets {2,4,…,2M}, fixed zero and three free positive centers, the exact nearest-spectrum cover radius is the least integer r≥0 satisfying

M≤floor(r/2)+3(r+1).

For real radius R, zero covers floor(R/2) initial positive targets. Any other center can cover at most floor(R)+1 targets because the grid spacing is2. The achievable capacity changes only at integer radii. Conversely partition the remaining targets into at most three consecutive blocks of length r+1, place each center at its block midpoint and cover the initial floor(r/2) targets by zero. This proves necessity and attainability. Negative target frequencies mirror the positive cover; the target zero is already matched.

Default M=5 gives r=1. Centers 3,7,10 have nearest distances (1,1,1,1,0). A radius below1 covers at most one target per positive center and none by zero. The residual η=‖Hnative E−E Hprogramme‖ is therefore at least κ in this relaxed three-band class. With sufficient copies and unrestricted eigenbasis encoding the relaxed floor is attainable: the native skew family permits these three centers and every required eigenspace has arbitrarily expandable multiplicity. No minimal-copy, local, source-acquired or target-blind encoding claim follows. These centers are comparison witnesses, not adopted UD coefficients.

At T=π/(2κ), the sufficient Duhamel budget has Tη≥π/2. **A lower floor on an upper error budget is not a lower bound on actual endpoint error.** The retained exact endpoint alias remains a counterexample to that inference. Slowing both generators by the same factor does not change this integrated budget.

## 5. Coordinate-defined geometric Gram family

C0173 declares the fixed tetrahedron coordinates p0=(1,1,r), p1=(1,−1,−r), p2=(−1,1,−r), p3=(−1,−1,r), with r>0 and q=r². Reference regular-simplex Gram determinants are8,48,256 in degrees1,2,3. Rule A uses normalized Gram determinants; Rule B squares them. These are fixed candidate rules p=1 or2, not an adjustable fitted exponent.

Write a=((1+q)/2)^p, b=((2q+1)/3)^p, c=q^p. In increasing simplex order the positive metric is H0=I, H1=diag(a,a,1,1,a,a), H2=bI, H3=c. Keep the boundary numerical entries fixed and use its H-adjoint. Its squared positive frequencies are

u=4/a, v=2+2/a, x=4a/b, y=2(a+1)/b, z=4b/c,

with characteristic polynomial λ(λ²+u)(λ²+v)²(λ²+x)(λ²+y)²(λ²+z). This is generally five bands. The Gram variable a is a metric entry, not the skew coefficient a of §3. At q=1 all squared frequencies are4. At q=4, Rule A gives (8/5,14/5,10/3,7/3,3), and Rule B gives (16/25,58/25,25/9,29/18,9/4).

Nonregular geometry breaks full S4 invariance of a fixed operator. Covariance when both labels and geometry are relabeled is not invariance under all permutations of the fixed stretched tetrahedron. Hence these five bands do not contradict MF.1. A metric change here changes the operator; a mere basis change would preserve its old spectrum. A time-varying metric needs a separate evolution/conservation law and is outside this construction.

Theorem MF.4. For every q>0 and either Rule A/B, identical fixed-rule fixed-q copies with any common positive rate cannot exactly admit the full default n=10 clock generator.

Proof. If the native bands coincide there are fewer than five, so admission fails by counting. Otherwise all five positive target frequencies must occupy the five distinct native bands. Their squared values, after a common factor, are a bijection with {1,4,9,16,25}. But the source formulas impose the exact scale-invariant identity

u/v+x/y=2/(a+1)+2a/(a+1)=2.

All 5P4=120 assignments of four distinct squared targets to U,V,X,Y violate U/V+X/Y=2. The replay records every rational difference. The smallest absolute difference is1/144, attained by (4,9,25,16) and its pair swap. Thus no such bijection exists. This exhaustive elimination adopts no fitted geometry. The identity would also exclude a more permissive positive a,b,c family of this diagonal form.

The finite relation gap is a certificate of exact inequality, **not** an operator residual or endpoint-error lower bound. Even n≥12 is separately excluded by the five-band count. This argument leaves n=8 unresolved; it does not declare admission or failure for that shorter clock. Heterogeneous q/rules/rates across copies and coupling between copies change the spectral class.

## 6. Source degree-weighted glued carriers

Theorem MF.5. The source C0473 positive degree-coupling families Kminus/Kplus also exclude exact full clock admission for even n≥8 under identical same-coefficient copies and a common scale.

Kminus has per-degree paired bands a{√3,√5}, b{√3,√5}, c{√3,√5}. Kplus has degree1 a√5, degree2 b{√2,√5}, degree3 c{√2,√5}; source signed multiplicities are respectively (1,3;2,3;1,1) and (4;1,5;1,2). Coincident bands can only reduce the distinct set. Each pair has irrational frequency ratio, while any two positive clock-grid frequencies have rational ratio. A single degree group therefore matches at most one grid frequency, regardless of its positive coefficient. Across three groups at most three distinct positive clock frequencies can match. Having six or five available bands does not evade this commensurability obstruction.

This applies to the declared degree-scalar weighted source families and to either correctly stated metric convention producing those coefficients. Arbitrary simplex-dependent metrics or new operators on glued carriers are not covered. No new coefficients are selected here; C0473 explicitly freezes their adoption without a source law.

## 7. Verification and next frontier

Root replay regenerates the increasing-orientation boundary and weighted adjoint using exact rational arithmetic, proves G-skew identities and compares all15 characteristic coefficients for eight Gram samples and two degree-metric samples. A separate freshly generated checker derives Gram determinants from coordinates and tests eight additional exact rule/geometry cases. The S4 checker reconstructs all24 signed actions, projector ranks, commutant dimensions and four degree metrics. Its 722,864 ordered partitions for M=1…64 agree with the exact three-center formula. The finite120-assignment Gram proof is exhaustive rather than a parameter sweep. Samples corroborate source formulas; the universal no-go follows from the written classification/counting and ratio arguments, not numerical extrapolation.

The source/scope thread checked the coefficient order, adjoint convention, five-band exception and limits. These are constructor-team AI checks. Independent human review, native source selection and physical calibration remain pending. Interface arithmetic/static checks do not certify rendered browser behavior.

The revised frontier is a source-defined heterogeneous/coupled carrier or different/refined complex; a broader declared operator; or an explicitly weaker prepared-window/endpoint contract. Any such route must retain complete encoding, clock/bank supply, acquisition, outgoing records and restart costs. It is an OPEN development route, not a recommendation to fit coefficients to clock eigenvalues. The earlier closed-factor, finite-window, odd-path and unit-metric results retain their own assumptions. Nothing here closes the global proof DAG or changes the registry.
