# UD 600-cell and Hopf-sector assessment

15 October 2026 UTC | Development; no registry entry | Physical promotion 0

## Result and scope

The proposal contains a useful finite symmetry-reduction problem, mixed with incorrect dimension/group statements and unsupported physical identifications. A declared order-ten right-quaternion symmetry of the regular 600-cell boundary commutes with the unit-incidence UD skew generator. Its complexified 2640-dimensional chain space therefore splits into ten orthogonal invariant 264-dimensional character sectors. On the original real carrier the decomposition has dimensions 264, 264 and four times 528. These are Fourier sectors across the fibre bundle, not independent spatial fibres or identified gauge sectors.

The companion replay independently builds the exact vertices over Q(phi), all simplices, signed boundary maps and the chosen symmetry action. Twenty-four exact finite check families pass. General Fourier-projector and perturbation statements below have written proofs. Constructor checks are not non-constructor review. The full 600-cell eigenvalue list and renormalization dynamics have not been calculated here.

The supplied historical ledger already mentions 600-cell structural diagnostics: Q32, Q33, Q39, Q59 and Q60. Thus the 600-cell is not being introduced into UD for the first time. Its G05 action weighting and G06 physical action normalization remain source-open in that document. Its date is 22 August 2026; it is historical input rather than a replacement for current repository state. The supplied governance proposal distinguishes development from registry promotion and does not authorize upgrading a physical claim from construction alone.

## Corrections to the proposed extension

| Proposed assertion | Assessment |
| --- | --- |
| A filled pentachoron has chain dimension 31 | Correct with nonempty simplices in degrees 0 through 4: f=(5,10,10,5,1). Its boundary has dimension 30. A tetrahedral facet is a 15-dimensional subcomplex, not automatically an invariant dynamical subspace. |
| The 600-cell boundary has f=(120,720,1200,600) and dimension 2640 | Correct. It is a three-dimensional simplicial sphere embedded in R4. Its 600 cells are tetrahedra, not four-dimensional hypervolumes. |
| B3 is a new layer beyond tetrahedral dynamics | Incorrect. B3 already maps tetrahedra to triangles. A four-dimensional filling introduces B4; its state space must be declared. |
| Ambient embedding upgrades Pachner moves to dimension four | Incorrect. The boundary uses 1↔4 and 2↔3 moves in dimension three. A declared four-dimensional bulk uses 1↔5, 2↔4 and 3↔3 moves. These moves preserve PL topology; they change triangulation. |
| The rotational group of the 600-cell is 2I of order 120 | Incorrect. It is (2I_L×2I_R)/{(1,1),(-1,-1)}, of order 7200. The full reflection group W(H4) has order 14400. A left or right copy of 2I is a subgroup. |
| The local automorphism group changes from S4 to S5 | Correct for replacement of an abstract tetrahedron by a 4-simplex; not for every retained tetrahedral cell. Oriented/geometric restrictions can select subgroups. |
| The 192-element exposure carrier grows exponentially | Unsupported. The supplied ledger's 192 is the typed product 24×8. A new global group requires a declared configuration fibre and action; its order is not obtained by extrapolating that product. The three opposite-edge pairs belong to a tetrahedron, and no replacement five-vertex fibre has been supplied. |
| H4/E8 relations yield Standard Model gauge modes | Unsupported. Root-system constructions and the McKay graph are genuine mathematics [1,2]. They do not supply local gauge transformations, gauge fields, matter representations, an action or running couplings for UD. |
| Z13 or D13 follows from the 600-cell's symmetry | Unsupported. 14400=2^6·3^2·5^2 has no factor 13, so W(H4) has no element of order 13 and no C13 subgroup. A separately supplied internal C13 structure remains possible; it needs its own source. |

The icosahedron is the vertex figure of the 600-cell, while its three-dimensional facets are tetrahedra. Embedding an arbitrary icosahedral cluster into this fixed triangulation is a separate incidence/metric test, not automatic from its name.

There is also a distinction between a flat tetrahedral facet in R4 and its radially projected spherical cell on S3. Both provide the same simplicial incidence here; they give different metric descriptions. No Lorentzian spacetime metric follows from either construction.

## Declared carriers, topology and small spectral controls

All chain bases below use one sorted oriented simplex, unit simplex metric, and no augmented empty-simplex register. Define B_k:C_k→C_(k−1), B_(k−1)B_k=0, and the real skew generator A with upper off-diagonal blocks −B_k and lower blocks B_k^T. For nonzero degree weights, replace each pair of blocks by −a_k B_k and a_k B_k^T.

| Carrier | f-vector | Total dimension | Betti numbers |
| --- | --- | --- | --- |
| Filled Δ4 | (5,10,10,5,1) | 31 | (1,0,0,0,0) |
| Boundary ∂Δ4 | (5,10,10,5) | 30 | (1,0,0,1) |
| Boundary of regular 600-cell | (120,720,1200,600) | 2640 | (1,0,0,1) |
| Cone from a new interior vertex over that boundary | (121,840,1920,1800,600) | 5281 | (1,0,0,0,0) |

The last row is one explicit simplicial four-ball filling, not an extra claim that the polytope selects this dynamics. Each boundary simplex is retained and coned; hence the total dimension is 2·2640+1. Another cellular filling can have one four-cell but is a different chain convention. Neither choice can be silently identified with the boundary-only carrier.

The exact unweighted pentachoron controls are

\[
\det(\lambda I-A_{\Delta^4})=\lambda(\lambda^2+5)^{15},
\qquad
\det(\lambda I-A_{\partial\Delta^4})=\lambda^2(\lambda^2+5)^{14}.
\]

These follow from exact incidence matrices in the replay. Merely extending a state on one tetrahedral facet by zeros does not isolate it under the larger generator: incidence into simplices outside that facet can produce amplitudes there. Embedding and dynamical invariance are separate claims.

For the 600-cell boundary the exact boundary ranks are

\[
\operatorname{rank}B_1=119,\quad
\operatorname{rank}B_2=601,\quad
\operatorname{rank}B_3=599.
\]

The replay obtains matching lower bounds modulo 1009. Constants give rank B1≤119; a nonzero consistently oriented fundamental cycle gives rank B3≤599. The chain identities and the modular lower bounds bound rank B2 above by both 720−119 and 1200−599, namely 601. Thus the ranks over Q and R are exactly the displayed values, not just modular or numerical guesses. Finite Hodge decomposition then gives

\[
\dim\ker A=2,\qquad \operatorname{rank}A=2638.
\]

One harmonic witness is constant on vertices and the other is the oriented fundamental three-cycle. The extra top harmonic mode is a consequence of a closed three-sphere, not a fourth spacetime degree. For nonzero degree weights the kernel remains the same by orthogonality of exact/coexact images. A zero weight can enlarge it.

Full unit-incidence spectra are not general PL invariants. For example, a 3D 1→4 subdivision changes a tetrahedral ball's f-vector from (4,6,4,1), dimension 15, to (5,10,10,4), dimension 29. Its full characteristic polynomial cannot remain equal with the state convention fixed. Betti numbers survive. A reduced spectral comparison would need an explicit state-transfer or coarse-graining map and is a different question. Neither invariance nor failure of spectral invariance by itself identifies physical gauge equivalence.

## Quaternionic Hopf construction

Set phi=(1+sqrt(5))/2. Use the standard unit-quaternion vertex set V of the 600-cell [1, §3; 2, §6]:

\[
(\pm1,0,0,0)\text{ and permutations},\quad
\tfrac12(\pm1,\pm1,\pm1,\pm1),\quad
\tfrac12\,\mathrm{EvenPerm}(0,\pm1,\pm\phi,\pm(\phi-1)).
\]

This gives 8+16+96=120 vertices. Join nearest neighbours, whose unit-quaternion inner product is phi/2. The resulting clique complex through tetrahedra has the stated f-vector, no five-vertex cliques, two tetrahedra per triangular face, and five tetrahedra per edge. The construction is an exact reconstruction of the declared standard complex; imported research scripts are not executed.

Choose g∈V with scalar part phi/2=cos(pi/5). Its quaternion order is ten and g^5=−1. Write g=cos(pi/5)+u sin(pi/5) with u a unit imaginary quaternion. The Hopf map

\[
h_u(q)=q u q^{-1}\in S^2
\]

obeys h_u(qg)=h_u(q). On V its fibres are the right cosets q⟨g⟩. The replay verifies this without approximate trigonometry by using the equivalent conjugacy map q↦qgq^(-1): it finds twelve distinct images, each with ten preimages, and an icosahedral nearest-neighbour graph on the images. Rescaling their imaginary parts gives the unit S2 base. Each coset lies on a great circle and is a regular decagon, since right multiplication is an isoclinic unit-quaternion rotation by pi/5 along that circle.

Choosing u or g chooses a Hopf structure. Full polytope symmetry need not preserve this one choice; it can carry it into another. A native law selecting the axis/fibration has not been supplied. Linked rings in a drawing are also not by themselves an algebraic decomposition of the full chain complex. Related 600-cell tetrahelix/Hopf constructions occur in the non-Euclidean nanoparticle literature [3]; no experimental validation of UD is imported from that work.

## Invariant-sector theorem

Let T_k be the signed simplex action induced by q↦qg on C_k. The sorting parity is essential; unsigned simplex permutations generally fail the oriented boundary identity. Naturality of simplicial boundary gives

\[
T_{k-1}B_k=B_kT_k,\quad T_k^{10}=I.
\]

These actions are orthogonal for the declared unit metric. Consequently T=diag(T0,T1,T2,T3) commutes with A. The same holds for arbitrary uniform degree weights a,b,c, without choosing their values.

After mathematical complexification define zeta=exp(2 pi i/10) and

\[
P_m=\frac1{10}\sum_{r=0}^9\zeta^{-mr}T^r,
\qquad m=0,\ldots,9.
\]

Finite geometric-series identities and T*=T^(-1) give P_m*=P_m, P_m P_n=delta_mn P_m, and sum_m P_m=I. Since [A,T]=0, [A,P_m]=0. Thus V_m=im(P_m) are mutually orthogonal invariant subspaces and

\[
C_\bullet(K;\mathbb C)=\bigoplus_{m=0}^9 V_m,
\qquad A=\bigoplus_m A|_{V_m}.
\]

The complexification is a representation-theoretic calculation, not the quantum amplitude encoding supplied in the acquisition instrument. No physical Hilbert-space interpretation is assumed by this theorem.

The dimensions can be found exactly without a 2640-dimensional eigenvalue calculation. Right multiplication acts freely on vertices. If a nonidentity element of C10 preserved a simplex, its induced vertex permutation would have order dividing that element's order. An element of order five or ten cannot act faithfully on at most four vertices; some nonidentity power would then fix a vertex, contradicting freeness. The remaining element of order two is antipodal and cannot preserve a simplex with all pairwise edges. Therefore all simplex orbits have length ten. The replay also checks every signed orbit and verifies total orientation sign +1 around each full orbit.

Each orbit affords one signed regular representation, equivalent to the ordinary regular representation because its sign product is +1. Hence every character occurs once per orbit:

| Degree | Number of simplices | C10 orbits | Dimension in each V_m |
| --- | --- | --- | --- |
| 0 | 120 | 12 | 12 |
| 1 | 720 | 72 | 72 |
| 2 | 1200 | 120 | 120 |
| 3 | 600 | 60 | 60 |
| Total | 2640 | 264 | 264 |

Equivalently Tr(T^r) vanishes for 1≤r≤9 and Tr(I)=2640, so Tr(P_m)=264. This trace certificate is exact.

For real amplitudes, V_m and V_(10−m) are conjugate. The real invariant dimensions are therefore

\[
264\ (m=0),\quad264\ (m=5),\quad
528\ (\{1,9\}),\quad528\ (\{2,8\}),\quad
528\ (\{3,7\}),\quad528\ (\{4,6\}).
\]

The two harmonic witnesses lie in m=0; its restricted generator has rank 262. Every other complex sector has rank 264, by the total kernel calculation. The four paired real sectors have rank 528 and m=5 has rank 264. These rank statements assume all three exchange weights are nonzero. They do not give the nonzero eigenfrequencies.

## What does and does not decouple

The projector onto one spatial vertex fibre does not commute with the full incidence dynamics. Acting on a fibre-supported vertex vector generates edges, including edges joining fibres. Those connections are part of the global triangulation. The invariant V_m instead takes a common Fourier character along every simplex orbit, with all orbit amplitudes included. Within a V_m, incidence still exchanges degree 0,1,2,3 components and couples different simplex orbits.

Thus the exact statement is sector decoupling for a specified symmetry, not independent dynamics of twelve spatial decagons. A fixed fibration is not a unique decomposition selected by full W(H4) symmetry, and its ten characters are not three selected physical coupling channels.

For a perturbation A=A0+E, with A0 and A real skew and [A0,P_m]=0, Duhamel's identity and unitary/orthogonal norm preservation imply

\[
\|(I-P_m)e^{t(A_0+E)}P_m\|
\le\min\{1,|t|\|E\|\}.
\]

Proof: the same quantity with e^(tA0) vanishes; subtract that propagator, integrate e^((t−s)(A0+E)) E e^(sA0), and use norm one for both evolution factors. Exact block separation survives if E also commutes with P_m. Unequal local metric weights, gates, seams, attachments or matter contacts can break the chosen symmetry and must be tested. The bound is a worst-case sufficient leakage bound, not a measured decoherence rate.

## Gauge and physical bridge limits

The finite group action above supplies neither a local gauge group at vertices nor parallel-transport variables on edges. A gauge comparison first needs a fibre, group-valued links with declared orientation laws, gauge transformations, field/matter state and an action or response functional. The ordinary identity B²=0 does not force a supplied connection to have zero curvature.

The 600-cell boundary is S3, with trivial fundamental group. For an ordinary globally flat lattice connection on the filled simplicial boundary, all graph loops become contractible through its faces and holonomy is gauge-trivial. Its graph alone has 720−120+1=601 independent cycle coordinates, but treating those graph cycles as topologically protected after restoring the triangular faces is an error. Curved connections, defects or omitted faces define other contracts. Hopf linking is not a nontrivial element of pi1(S3).

The H4/E8 relation is specifically a relation between root systems/Clifford constructions and, separately, the affine E8 McKay diagram [1,2]. It does not imply E8 Lie gauge symmetry on this state space, nor SU(3)×SU(2)×U(1), charge assignments, chiral matter, action normalization or coupling unification. A finite symmetry has no continuous Lie algebra of local infinitesimal gauge transformations of its own. Continuous emergent symmetry requires a separate limit and dynamical argument.

Running requires a scale-dependent family and a specified coarse-graining/renormalization map. This single finite complex and its invariant blocks supply neither. Uniform symbolic exchange coefficients remain model parameters; changing their labels to g1,g2,g3 would not derive physical couplings. The two unresolved action/normalization entries in the supplied ledger are not closed by these dimension or symmetry counts.

## Manuscript disposition and next tasks

Retain the corrected geometry as context and the conditional C10 sector theorem as a finite-model development result. Exclude the proposed claims of automatic exposure growth, four-dimensional boundary Pachner dynamics and emergent Standard Model modes. A short manuscript-facing formulation is:

> The regular 600-cell boundary provides a finite closed tetrahedral test carrier. For a declared tenfold right-quaternion symmetry and an invariant chain metric, its incidence dynamics admits an orthogonal character decomposition. This reduces a specified dynamical calculation while retaining couplings between spatial fibres. It does not identify a gauge sector or a renormalization flow; those require separately defined fields, interactions and coarse-graining.

The next productive computations are: construct the ten reduced boundary matrices from orbit representatives and their signed transport phases; calculate their spectra with exact/algebraic certificates where feasible; determine the commutant and metric assumptions relevant to any proposed interaction; test the actual gate/seam perturbations through [A,P_m] and the leakage bound; and only then define a physically motivated gauge/renormalization problem. Choosing this new carrier does not derive the current manuscript's preparation bank or blank supply.

This assessment is a separate development note. It does not revise the narrative manuscript or promote the registry. Current repository main was refreshed to 786cf65 before construction; the source register pins the full commit and the two supplied historical documents. The current upload `Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used.

## Exact sources and reproducibility

1. Koca, M., Al-Ajmi, M. and Koca, N. O. *Quaternionic Representation of Snub 24-Cell and its Dual Polytope Derived From E8 Root System*. arXiv:0906.2109v2 (2009), especially §3, equations (6)-(9), and the vertex conjugacy classes. https://arxiv.org/pdf/0906.2109 . Inspected for quaternion vertices, full symmetry action and H4/E8 scope. The rotation order 7200 also follows from the pair action's two-element kernel.
2. Dechant, P.-P. *The Birth of E8 out of the Spinors of the Icosahedron*. Proceedings of the Royal Society A 472, 20150504 (2016). DOI:10.1098/rspa.2015.0504. arXiv:1602.05985, §§5-6. https://arxiv.org/pdf/1602.05985 . Inspected for the explicit 120-vertex coordinate set, McKay diagram and the extra Clifford/reduced-inner-product construction needed for E8.
3. Serafin, F., Lu, J., Kotov, N., Sun, K. and Mao, X. *Frustrated Self-Assembly of Non-Euclidean Crystals of Nanoparticles*. Nature Communications 12, 4925 (2021), DOI:10.1038/s41467-021-25139-9; arXiv:2010.03087. https://www.nature.com/articles/s41467-021-25139-9 . Article/search metadata identifies related Hopf/tetrahelix geometry; no theorem from its inaccessible full-text passage is imported. The finite Hopf construction above is proved and checked independently. Authorship and publication details were checked against arXiv:2010.03087v2 and PubMed:34389712.
4. Kashaev, R. *On realizations of Pachner moves in 4D*. arXiv:1504.01979 (2015). https://arxiv.org/abs/1504.01979 . Dimension-specific Pachner background; abstract inspected, no uninspected identity imported.

Run `python verify_hopf_sectors.py` with Python, NumPy, SciPy and SymPy. It reconstructs all finite data and writes HOPF_SECTOR_CHECKS.json plus COMPLEX_AND_ACTION.json. The latter records vertices in the exact field, all simplices and the signed symmetry permutations. Fourier projectors are specified algebraically in this note; no floating-point eigenvalue claim is used as proof. Earlier UD source or manuscript replays are not all rerun.
