---
title: "Antisymmetry, Support Continuity and Invisible Circulation in UD"
subtitle: "Exploratory current/curl audit 0.1"
author: "Benjamin Walker Mayes / Codex constructor"
date: "5 October 2026"
---

**Development — no registry entry. Independent review pending. Physical promotion 0.** This investigates whether the antisymmetric-tensor snippet supplies a useful UD closure. It yields an exact representation and identifiability audit, not a Maxwell derivation or a solution of open-system recursive support. Anchors Q169–Q179 are taken from the attached v0.39 ledger; that attachment is preserved rather than treated as a replacement for later portal records. The ledger, controller WBS and manuscript papers are not revised by this branch.

# 1. Correct the continuum identity and type the proposed correspondence

For a sufficiently differentiable antisymmetric tensor $F^{\mu\nu}=-F^{\nu\mu}$ and commuting coordinate partial derivatives,
\[
\partial_\nu\partial_\mu F^{\mu\nu}=0.
\]
The single divergence $J^\nu=\partial_\mu F^{\mu\nu}$ need not vanish. For example $F^{01}=x^0$, $F^{10}=-x^0$ and all other entries zero give $J^1=1$. The double-divergence identity holds in any coordinate dimension, not only four. It cannot select physical four-dimensional spacetime from UD's chain counts.

| Object | Index/domain | Identity | What it does not establish |
|---|---|---|---|
| Continuum antisymmetric field F | Two spacetime coordinate indices | Double partial divergence is zero | Single divergence zero, field equations, metric or physical charge |
| Original simplicial boundaries B_k | Oriented UD simplices of adjacent degree | $B_1B_2=B_2B_3=0$ | Physical currents or calibrated spacetime |
| UD skew generator A | All chain-register basis addresses | $A^T=-A$, conserved quadratic support | Zero local stock derivative |
| Hasse graph boundary D | Incidence currents to simplex-address stocks | Column sums zero | Actual current is divergence-free |
| Diamond boundary C | Oriented Hasse squares to incidence currents | $DC=0$ | Every actual current is a curl |

These are different typed maps. In particular, $A_{\sigma\eta}$ has simplex-address indices, not spacetime indices. Calling A antisymmetric does not turn it into an electromagnetic tensor. Discrete exterior calculus is prior mathematical context, not a native UD source law: see Desbrun, Hirani, Leok and Marsden, [Discrete Exterior Calculus](https://arxiv.org/abs/math/0508341). The specific matrices and claims here are independently rederived below.

# 2. Retained skew dynamics give local throughput, not zero divergence

Use the unit-incidence convention with $A_{\eta\sigma}=B_{\sigma\eta}$ and $A_{\sigma\eta}=-B_{\sigma\eta}$ for adjacent degrees, where sigma is a facet of eta. Orient each Hasse edge from lower sigma to upper eta. D has -1 at sigma and +1 at eta. For real amplitudes evolving under $\dot c=Ac$, define
\[
\rho_\sigma=c_\sigma^2,\qquad
j_{\sigma\to\eta}=2B_{\sigma\eta}c_\sigma c_\eta.
\]
Then direct differentiation gives
\[
\dot\rho=Dj,\qquad \mathbf1^TDj=0.
\]
This is the retained Q170–Q172 throughput convention: local stocks may change while their total stays fixed. For complex amplitudes and the same real skew A, use $\rho_\sigma=|c_\sigma|^2$ and $j=2B_{\sigma\eta}\operatorname{Re}(\overline c_\eta c_\sigma)$. This is the real part of the complex PSR bilinear receipt; the full complex receipt's phase is a separate datum, not silently identified with a real support flux.

**Exact dynamic counterexample.** On the filled tetrahedron put equal normalized amplitude $1/\sqrt2$ on vertex 1 and edge 01, with all others zero. Since $B_{1,01}=+1$, the only nonzero current is one unit along $1\to01$. Thus $\dot\rho_1=-1$, $\dot\rho_{01}=+1$. The generator is skew and total support is conserved, yet $Dj\ne0$.

Likewise, equal normalized amplitudes on face 013 and tetrahedron 0123 give unit current $013\to0123$, with face-stock derivative -1 and core-stock derivative +1. Antisymmetry cannot eliminate Q172's interface reservoir. Its elimination would require an additional approximation and debit.

**Pure-curl exclusion.** If one imposed $j=Cq$ with $DC=0$ as the entire closed-system current law, then $\dot\rho=0$ at every address. Both legitimate witnesses above would be excluded. This forces stationary stocks, not necessarily stationary amplitudes or phases. A continuum conservation identity therefore cannot be imported as a universal zero-throughput constraint.

# 3. Construct the correctly typed discrete curl

The auxiliary Hasse complex has one vertex for each nonempty simplex of K, an edge for every cover incidence, and a square for every interval $\sigma\subset\tau$ differing by two vertices a,b. With $a<b$, its oriented square boundary is
\[
\sigma\to\sigma a\to\sigma ab\to\sigma b\to\sigma.
\]
C is the matrix of these four-edge boundaries. Every square has two incoming and two outgoing endpoints, so $DC=0$ exactly. There are also cubes for intervals differing by three vertices; their boundary matrix Q obeys $CQ=0$ by cancellation of paired square faces. Q here is a matrix name, not a ledger coefficient identifier.

The Hasse squares are not the original triangular C_2 faces. For one filled tetrahedron the original f-vector is (4,6,4,1), while the auxiliary current complex has counts (15,28,18,4). It is used to represent transport on the incidence graph; it does not replace the carrier or add physical dimensions.

Exact integer ranks give the following finite audit:

| Carrier / control | Hasse vertices, edges, squares, cubes | rank D | rank C | Current directions invisible to divergence | Noncurl cycle directions | Potential ambiguity dim ker C |
|---|---|---:|---:|---:|---:|---:|
| Filled tetrahedron | 15,28,18,4 | 14 | 14 | 14 | 0 | 4 |
| Two tetrahedra sharing face | 23,47,33,8 | 22 | 25 | 25 | 0 | 8 |
| Three tetrahedra sharing edge | 27,59,45,12 | 26 | 33 | 33 | 0 | 12 |
| Pentachoron boundary U | 30,70,60,20 | 29 | 41 | 41 | 0 | 19 |
| Hollow tetrahedron boundary | 14,24,12,0 | 13 | 11 | 11 | 0 | 1 |
| Unfilled triangle loop | 6,6,0,0 | 5 | 0 | 1 | 1 | 0 |

For the first five rows, equality $\operatorname{rank}C=\dim\ker D$ together with $DC=0$ proves $\ker D=\operatorname{im}C$ over the real or rational field. Smith normal form strengthens this result: every nonzero invariant of C is 1 in all six cases. Therefore its image is a primitive integer sublattice of the full current lattice. For the five rows with no noncurl directions, every integer graph cycle consequently has an integer square potential; rational and real cycles also have rational and real potentials. To see the integer conclusion, equal rank and DC=0 give equality of rational spans; saturation then places every integer vector in that span inside the integer image of C. In the loop control there is no square potential and a nonzero divergence-free circulation remains. Thus topology can obstruct a global curl representation; antisymmetry alone does not remove that obstruction.

For the filled tetrahedron, two-tet and three-tet cases, the square-potential ambiguity equals the cube-boundary image dimensions 4,8,12. For U the cube image has dimension 19 despite 20 cubes. Nonzero cube-boundary Smith invariants are likewise all 1; where its rank exhausts ker C, the cube image accounts for the integer potential ambiguity as well. The hollow tetrahedron has a one-dimensional closed-square ambiguity without any cubes. No statement about arbitrary larger carriers is inferred just from these six replays.

# 4. Decompose dynamic currents and expose the transport gap

**Theorem (continuity identifiability on the audited connected graphs).** Let $s=Dj$ be the complete stock derivative. Because $\mathbf1^Ts=0$, the graph Laplacian equation $DD^T\phi=s$ has a solution, unique after imposing $\mathbf1^T\phi=0$. Set $j_{\mathrm{grad}}=D^T\phi$. Then
\[
j=j_{\mathrm{grad}}+z,\qquad Dz=0,
\qquad j_{\mathrm{grad}}^Tz=0.
\]
For the rows with no noncurl cycle directions, write $z=Cq$; q is nonunique by ker C. For the loop control a noncurl residual may remain.

*Proof.* Connected graph incidence has rank V-1 and image equal to the zero-sum vectors. The Laplacian has the same image and only the constant kernel. Subtracting the constructed gradient gives a zero-divergence residual. Orthogonality follows from $\phi^TDz=0$. The rank equality in the table supplies the square-potential assertion. $\square$

The replay gives an explicit rational decomposition of the unit-edge dynamic witness. Its circulation residual is nonzero: even that simple stock-changing current is not equal to the Euclidean minimum-norm gradient current.

This construction does not select a native transport law. With a chosen symmetric positive-definite edge metric R, a different minimum-norm representative is
\[
j_R=R^{-1}D^T(DR^{-1}D^T)^+s,
\]
where plus denotes the Moore–Penrose inverse. The metric is a declared reconstruction choice, not a newly derived UD coupling. Actual j is fixed when A and the full admitted c are supplied; the ambiguity concerns inference from stock continuity alone.

On a filled tetrahedron, complete node-stock derivatives leave **14** independent circulation directions undetermined. The glued two- and three-tet cases leave **25** and **33**. Currents $j$ and $j+Cq$ produce identical s. If only fixed owned stocks $S=W\rho$ are observed, they also produce identical $\dot S=WDj$.

For the retained equal-top-star weights of Q177–Q179,
\[
w_{\sigma,\tau}=1/n_3(\sigma)\quad(\sigma\subset\tau),
\qquad
\dot S_\tau=\sum_{\sigma\to\eta}
(w_{\eta,\tau}-w_{\sigma,\tau})j_{\sigma\to\eta}.
\]
The replay rederives this formula and verifies column ownership sums to one on the four filled 3D carriers. Added square circulation is invisible to every such fixed owned-stock derivative. Time-dependent ownership has the additional $\dot W\rho$ term and requires its own reassignment receipt.

The useful closure is therefore a **conditional identifiability result**: at a fixed instant, continuity by itself cannot determine an otherwise unrestricted incidence-current vector. Closing recursive transport requires an admitted generator/current law or additional current-sensitive observations; further fixed owned-stock equations at that instant cannot resolve the circulation kernel. A known constitutive law or additional temporal dynamics can restrict the unknown class and must be audited separately. This does not reopen or demote the retained exact micro-continuity results.

**Theorem (minimal additional linear current probes).** Suppose the only initial information at an instant is $s=Dj$, with no additional constitutive constraint on the real current vector. Let Z have independent columns spanning ker D. Exactly $\dim\ker D$ additional linear probes suffice: observe $Z^Tj$. They are also the minimum possible count for uniform current identifiability. If two currents share both sets of data, their difference z lies in ker D and is orthogonal to its entire basis, so z=0. Fewer probes cannot injectively map a vector space of that dimension. On rows with no noncurl cycles, independent square-curl columns can serve as the probes; the loop control requires its nonlocal cycle direction too. These are mathematical observables, not a claim of an available measurement channel.

If only equal-share cell-stock derivatives are available, let m be the number of tetrahedra. Their derivative map WD has rank m-1 on the four filled carriers. Rows of W are independent because each top simplex is owned only by its own cell. A combination of rows annihilates D only when it is constant over the connected Hasse graph; the top-simplex entries then force all coefficients equal. Unrestricted current reconstruction consequently requires E-(m-1) additional independent linear probes, potentially including missing stock-changing directions as well as circulation.

| Available stock derivative data | Filled tetrahedron | Two tetrahedra | Three tetrahedra | U boundary |
|---|---:|---:|---:|---:|
| All simplex-address derivatives: minimum extra probes | 14 | 25 | 33 | 41 |
| Equal-share cell derivatives only: map rank | 0 | 1 | 2 | 4 |
| Equal-share cell derivatives only: minimum extra probes | 28 | 46 | 57 | 66 |

One cell's owned total is constant and reveals none of its 28 individual incidence currents. Replay verifies the displayed ranks and supplies exact reconstruction-rank witnesses modulo prime 101. A full modular column-rank witness certifies full rational column rank; the proven rational upper bound supplies equality where needed. The modulus is a computational check, not a physical coefficient. This gives an exact, scoped requirement for additional transport observations.

# 5. Weighted divergence and open-system bookkeeping

For the auxiliary cochain maps $d_0=D^T$ and $d_1=C^T$, choose positive diagonal inner-product matrices $M_0,M_1,M_2$. Their matched adjoints are
\[
\delta_1=M_0^{-1}DM_1,\qquad
\delta_2=M_1^{-1}CM_2,
\qquad \delta_1\delta_2=M_0^{-1}DCM_2=0.
\]
The intermediate metric cancels. Mixing a weighted divergence with an unmatched raw curl can instead give a nonzero result. Replay includes a rational positive-metric counterexample to that mismatch. An apparent failure of double divergence may therefore be a typing or metric inconsistency, rather than a broken topology.

For an explicitly supplied amplitude source $\dot c=Ac+r$, the complete local relation is
\[
\dot\rho=Dj+q_{\mathrm{src}},\qquad
(q_{\mathrm{src}})_\sigma=2\operatorname{Re}(\overline c_\sigma r_\sigma),
\qquad \frac{d}{dt}\sum_\sigma\rho_\sigma=\sum_\sigma(q_{\mathrm{src}})_\sigma.
\]
The internal incidence cut still cancels globally; the source is not cancelled by it. This is bookkeeping for an admitted r, not a derivation of native r, environmental dissipation, donor renewal or coarse breathing stocks. Those source laws remain open. No four-dimensional spacetime, electromagnetic field identification, calibration or experimental conservation claim is obtained.

# 6. Gap dispositions and next evidence

| Question | Result of this exploration | Remaining gate |
|---|---|---|
| Does antisymmetry force zero local UD flow? | No; two exact normalized dynamic witnesses reject it | None for the stated counterexamples |
| Is there a typed divergence-of-curl identity? | Yes, DC=0 on the explicitly constructed Hasse squares | Larger complexes and any physical interpretation |
| Can conservative residual currents be represented locally? | All graph cycles are square curls on five audited carriers | Arbitrary topology beyond the six exact rank/Smith audits |
| Does continuity determine native transport? | No; exact undetermined dimensions, rational decomposition and minimum linear-probe counts are supplied | Current law or current-sensitive evidence |
| Can weighted continuity be checked consistently? | Matched adjoint cancellation and mismatch witness supplied | Independently sourced metric/physical units |
| Are Q168/open-system support gaps closed? | No; admitted source bookkeeping only | Native environment, source/sink, renewal and coarse-stock laws |

Next useful effort: source a candidate current law or an implementable version of the minimal cycle probes, then test it against the supplied generator and finite preparation/observation defects; extend the exact rank and Smith-form audit to a named larger or nontrivial-topology carrier. Neither a zero-divergence slogan nor a metric chosen for convenient reconstruction can replace that work.

All replay checks use exact rational/Gaussian-integer algebra. The archive includes complete matrices, the dynamic witnesses and their rational decomposition, attached source copies and a hash manifest. Constructor checking is not independent review. Placeholder packet-field/seam attachments supply no usable field equation and were not filled in by guesswork. Missing Gap2_FINAL_Finite_Genesis.png was unavailable and not used.
