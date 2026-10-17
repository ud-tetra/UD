# UD 600-cell vertex-link observability theorem v0.1

Date: 2026-10-16 UTC. Lane: development — no registry entry. Constructor verification: exact. Non-constructor review: pending. Physical promotion: 0.

## Result

For the regular 600-cell boundary, unit simplex metric and unweighted real skew Hodge–Dirac generator A=A(1,1,1), observe every vertex, edge and face amplitude of one icosahedral vertex link. The readout has 62 scalar channels. Its snapshot rank is 62; its ideal continuous-history observation rank is **1893**. The dynamical unobservable subspace has real dimension **747**, comprising one stationary dimension and 746 nonzero-frequency dimensions.

Each complex C10 character sector has dimension 264 and snapshot observation rank 51. Its continuous-history ranks are 255 (m=0), 220 (m=5), 254 (m=1,3,7,9) and 258 (m=2,4,6,8). These isolated-sector ranks do not add to the full observation rank because the chosen readout does not intertwine C10 actions.

These are ideal mathematical observability results. They are not finite-sampling conditioning, experimental noise robustness, native observer selection, physical clock calibration or evidence for a physical tetrahedral substrate.

## 1. Source selection and carrier

The connection supplied by the user motivates an **icosahedral vertex link**, not a recursively branching fractal. The link is the actual two-dimensional subcomplex L=lk_K(v). Its simplices are precisely those disjoint from v for which adjoining v gives a simplex of K. Its twenty triangles correspond bijectively to the twenty tetrahedra incident to v. The closed star st_K(v)=v*L is a three-ball whose boundary is L; K itself remains a closed S3 with empty manifold boundary.

Use vertex index v=0 in the pinned finite dataset; its exact quaternion coordinates are (-1,0,0,0). The link has f=(12,30,20), chain dimension 62, Euler characteristic two and boundary ranks (11,19). All edges belong to two link triangles. The replay checks these facts and reconstructs the global adjacency from exact golden-ratio coordinates rather than trusting a picture.

Choosing one vertex is a computational convention. Left multiplication by 2I acts transitively on vertices and commutes with the declared right C10 action. Consequently the full and isolated-sector ranks are identical for every vertex-link shell with the same all-simplex readout. This is a symmetry equivalence, not a native law selecting a physical observer.

The global carrier is X=C0⊕C1⊕C2⊕C3 over R, with dimensions (120,720,1200,600), total 2640. One sorted oriented simplex supplies each coordinate, with no empty-simplex register and no added four-cell. Bk:Ck→C(k−1) are signed incidence maps. Declare

    A = [[0,-B1,0,0],
         [B1^T,0,-B2,0],
         [0,B2^T,0,-B3],
         [0,0,B3^T,0]],    x'(t)=A x(t).

The metric is identity on these chains. The parameter t is an internal continuous evolution parameter, not calibrated seconds. No drives, gates, dissipation or topology changes are included. x(0) is unrestricted. The signed incidences are generated from simplex data; the scripts check B1B2=B2B3=0 and A^T=-A.

Let R be the 62×2640 coordinate-selection matrix in RESULTS and modular_results. It observes the twelve link vertices, thirty link edges and twenty link faces, in that order. No tetrahedral coordinate is directly observed. R R^T=I62. The retained support is ||Rx||²; it is not the full conserved support ||x||².

## 2. Theorem VL1 — Snapshot versus dynamical kernel

Define the finite observation matrix

    O_104 = [ R ; R A ; ... ; R A^104 ].

Then, for this model and shell,

    rank_R(R)=62,          dim_R ker R=2578,
    rank_R(O_104)=1893,    dim_R ker O_104=747.

Moreover

    N = ker O_104 = {x : R exp(tA)x=0 for every real t}

is the largest A-invariant subspace contained in ker R. Therefore all its 747 dimensions remain invisible even with an arbitrarily long ideal noiseless history. This is a dynamical restriction, not data destruction by the evolution. Conversely every nonzero coset in X/N changes the continuous output history. The kernel invisible at the snapshot but not for the full history is measured by

    dim(ker R / N)=2578-747=1831.

Thus time dependence exposes 1831 additional dimensions beyond the snapshot's 62, while 747 remain hidden. A concrete recovered example is unit amplitude on the central vertex v: Rx=RAx=0, but RA²x equals one on each of the twelve observed link vertices. It first appears in the second output derivative. This exact example is recorded in MEMBERSHIP_EXAMPLES.json.

Proof of the all-time statement: A is skew and finite-dimensional. Let L=-A². The exact squarefree polynomial q below satisfies **R q(L)=0**, checked with integer arithmetic on the reconstructed incidence matrices. Its degree is 53 and it has a simple factor x. Writing q(x)=x q1(x), R A² q1(-A²)=0. For real skew A, a row w with wA²=0 also has wA=0 because ||wA||²=-wA²w^T=0. Hence the degree-105 polynomial z q1(-z²) annihilates the rows of R. All higher derivatives reduce to powers 0 through 104. Vanishing of the finite stack is consequently equivalent to vanishing of R exp(tA)x. A-invariance follows from the polynomial recurrence. This supplies an upper/saturation certificate, not merely agreement of ranks modulo primes.

The polynomial q is the product, once each, of the following monic factors:

    x, x-3, x-4, x-5, x-6, x-7, x-8, x-9, x-12, x-14, x-15,
    x²-20x+80, x²-18x+36, x²-15x+55, x²-14x+44,
    x²-11x+23, x²-11x+27, x²-11x+29,
    x²-10x+5, x²-10x+23, x²-9x+9, x²-9x+15,
    x²-8x+11, x²-7x+1, x²-7x+11, x²-5x+3, x²-3x+1,
    x³-11x²+33x-28, x³-11x²+33x-24,
    x⁴-22x³+165x²-484x+464.

The stored coefficient array is authoritative for the replay. Candidate factors came from the pinned source spectrum; the observer annihilator identity is rechecked independently and does not assume that spectrum is correct.

## 3. Exact computable representation of N

This release represents the full N by exact matrix constraints and spectral-component dimensions, rather than listing a dense 2640×747 basis. It additionally exports explicit basis vectors for the entire 48-dimensional hidden sqrt(14) component and a stationary harmonic witness.

For each factor f of q, let d_f=deg f and h_f=q/f. Form the integer matrix

    V_f = stack over j=0,...,d_f-1 of
          R L^j h_f(L) and R A L^j h_f(L).

Then

    N = intersection over f of ker V_f.

The rows are specified completely by the stored simplex list, shell indices, q coefficients and the displayed recurrence. The replay constructs each matrix with Python arbitrary-precision integers and calculates its rank over Q using FLINT fmpz_mat.rank. Because the factors are coprime and Rq(L)=0, their row modules form a direct sum; their ranks sum to 1893. This is also a compact exact membership test for any rational candidate hidden state. It defines the real subspace by scalar extension, without numerical thresholds.

For the full Laplacian spectral component X_f=ker f(L), define N_f=X_f∩ker V_f. Then N=direct_sum_f N_f. Ambient component dimensions in the following table use the pinned source's complete ten-sector characteristic multiplicities; those full characteristic polynomials are not replayed here. The observation ranks and their sum are newly verified exactly.

| Factor f of L | Ambient dimension | Observed-history rank | Hidden dimension |
|---|---:|---:|---:|
| x | 2 | 1 | 1 |
| x-3 | 80 | 30 | 50 |
| x-4 | 108 | 74 | 34 |
| x-5 | 48 | 38 | 10 |
| x-6 | 16 | 16 | 0 |
| x-7 | 144 | 60 | 84 |
| x-8 | 50 | 38 | 12 |
| x-9 | 64 | 54 | 10 |
| x-12 | 50 | 22 | 28 |
| x-14 | 72 | 24 | 48 |
| x-15 | 32 | 24 | 8 |
| x²-20x+80 | 36 | 36 | 0 |
| x²-18x+36 | 16 | 16 | 0 |
| x²-15x+55 | 96 | 96 | 0 |
| x²-14x+44 | 96 | 96 | 0 |
| x²-11x+23 | 192 | 120 | 72 |
| x²-11x+27 | 160 | 120 | 40 |
| x²-11x+29 | 120 | 76 | 44 |
| x²-10x+5 | 24 | 24 | 0 |
| x²-10x+23 | 192 | 76 | 116 |
| x²-9x+9 | 64 | 64 | 0 |
| x²-9x+15 | 64 | 64 | 0 |
| x²-8x+11 | 96 | 64 | 32 |
| x²-7x+1 | 16 | 16 | 0 |
| x²-7x+11 | 96 | 64 | 32 |
| x²-5x+3 | 64 | 64 | 0 |
| x²-3x+1 | 36 | 36 | 0 |
| x³-11x²+33x-28 | 216 | 120 | 96 |
| x³-11x²+33x-24 | 150 | 120 | 30 |
| x⁴-22x³+165x²-484x+464 | 240 | 240 | 0 |
| **Total** | **2640** | **1893** | **747** |

A concrete stationary hidden vector is the consistently oriented fundamental three-cycle, with all other degrees zero: A annihilates it and R observes no C3 coordinate. The other harmonic vector, uniform on vertices, is visible. Hence one of the 747 hidden dimensions is stationary and 746 are oscillatory. In particular sqrt(3) and sqrt(5) are both visible frequencies here, with observation ranks 30 and 38 on their real frequency subspaces; they are not wholly trapped in a boundary kernel. This unit 600-cell source does not have a sqrt(2) frequency factor in q.

The file HIDDEN_WITNESSES.json supplies an explicit oscillatory witness pair x,y with x supported on vertices and y on edges:

    y=Ax, Ay=-14x, Rx=Ry=0,
    exp(tA)x=cos(sqrt(14)t)x+sin(sqrt(14)t)y/sqrt(14).

The displayed example has 16 nonzero vertex coordinates and 176 nonzero edge coordinates. Its time dependence is nontrivial but exactly invisible on the selected shell. The replay also computes all 24 independent graph eigenvectors at eigenvalue 14 that vanish on the link vertices. Their A-images give 24 independent partners, supplying a full 48-vector basis for this hidden frequency component; the two degrees have disjoint support, and A is injective on this nonzero-frequency space. Their link-edge gradients vanish because both endpoints lie in the zero-valued link. This is a constructive example of hidden dynamics, rather than an inference from large dimension counts.

## 4. Theorem VL2 — Character-resolved ranks

Let T be the pinned signed right-quaternion action of order ten; [A,T]=0. Work over C and set zeta=exp(2πi/10). For V_m=ker(T-zeta^m I), dim_C V_m=264. Let Q_m be its signed-orbit Fourier basis, unnormalized by a nonzero common factor. Define the isolated-sector observation matrix by O_m=stack(R Q_m A_m^j), j=0,...,104, where A Q_m=Q_m A_m.

| Characters m | Number of sectors | Dimension of each | Snapshot rank of each | History rank of each | Hidden within each |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 264 | 51 | 255 | 9 |
| 1,3,7,9 | 4 | 264 | 51 | 254 | 10 |
| 2,4,6,8 | 4 | 264 | 51 | 258 | 6 |
| 5 | 1 | 264 | 51 | 220 | 44 |

Snapshot proof: the twelve link vertices meet six C10 vertex orbits; thirty link edges meet twenty-five edge orbits; twenty link faces meet twenty face orbits. Each touched orbit contributes exactly one independent Fourier column, for every m. Thus rank RQ_m=6+25+20=51 exactly.

Dynamic proof/certificate: m=0 and m=5 use rational matrices directly. For m=1 and m=2, use K=Q(zeta), phi10(zeta)=zeta⁴-zeta³+zeta²-zeta+1=0. Every V_f Q_m has four exact integer coefficient matrices. Replace each scalar coefficient by its 4×4 regular multiplication matrix on K. The resulting rational matrix has rank exactly four times its K-rank; compute that integer rank and divide by four. Sum over the thirty coprime f components. Galois conjugation supplies m=3,7,9 from m=1 and m=4,6,8 from m=2. This is an exact number-field rank certificate, not an inference from finite-field values. Independent split-prime checks at p=2011 and p=3011 agree for all ten characters, and the full ranks also agree with preliminary checks at p=1009 and p=1013.

A real state in a conjugate character pair has twice the corresponding complex rank and dimension: pairs {1,9},{3,7} each have dimension 528 and rank 508; pairs {2,8},{4,6} each have dimension 528 and rank 516. The real m=0 and m=5 results are unchanged.

## 5. Theorem VL3 — Cross-sector ambiguity

The shell does not preserve the chosen right C10 action: T carries lk(v) to lk(vg), rather than leaving this single shell fixed. The output therefore has no inherited boundary C10 action under which R automatically intertwines the bulk action. Observation ranks on sectors are restrictions to individually prepared sectors, not ten independently available readout channels.

The sum of the isolated-sector history ranks is 2523, whereas the full observation rank is 1893. Equivalently,

    dim_C [direct_sum_m (N_C ∩ V_m)] = 117,
    dim_C N_C = 747,
    dim_C [N_C / direct_sum_m (N_C ∩ V_m)] = 630.

Here N_C denotes complexification of the real N. The quotient measures additional mixed-sector hidden combinations; it is not a new canonical physical sector. Shared eigenfrequencies permit outputs from distinct characters to cancel for all time. No cancellation between distinct frequencies is needed for this obstruction. Assuming that sector ranks add would overstate recoverability by 630 dimensions. The explicit field-rank computation above avoids this error.

## 6. Geometry claims considered in making the choice

The triangle→tetrahedron→pentachoron sequence is the simplex sequence. The 600-cell instead supplies a closed tetrahedral three-sphere embedded in four-dimensional Euclidean space. Five tetrahedra meet per edge and twenty per vertex; the icosahedral link uses this incidence directly. Banchoff's original exposition confirms the five-around-an-edge and twenty-at-a-vertex constructions: https://www.math.brown.edu/tbanchof/Beyond3d/chapter5/section08.html . MathWorld's Pentatope page identifies the four-simplex: https://mathworld.wolfram.com/Pentatope.html . Retrieved 2026-10-16. Linked video/third-party claims are not used as theorem premises.

The proposed value log(20)/log(phi), approximately 6.225, is a formal branching ratio, not an established Hausdorff dimension of the 600-cell. A finite polytope boundary is not an iterated function system. Twenty incident tetrahedra are not twenty smaller copies of the whole polytope. Any subset of R4 has Hausdorff dimension at most four (and a subset of a smooth S3 at most three), so that ratio cannot describe a nonoverlapping similarity construction of this embedded carrier. A recursive contraction family, its invariant set and a separation/overlap analysis would be needed. The Sierpinski tetrahedron's Hausdorff dimension two also does not make it a smooth two-dimensional surface.

For flat regular tetrahedral facets, the intrinsic edge angle deficit is

    delta = 2π - 5 arccos(1/3) > 0.

It is about 7.356 degrees. Embedding the closed polyhedral boundary in R4 does not erase this piecewise-flat intrinsic curvature. Radially projecting onto a round S3 supplies a different metric with spherical tetrahedra whose five dihedral angles close around an edge. Neither metric supplies a fractal law or selects the unit chain metric used here. “Maximum regular packing” is unnecessary for this computation and is not treated as a general packing theorem.

## 7. Verification, reproducibility and limits

Sources are immutable data, not executed imported research code:

- Main snapshot at source selection: 840e46a4f631a05f7a5992a07bcdf70c733c5dd5; refreshed main: 3b4ccc26a65b5deef0e917fa8bbadf045649695d. Relevant two 600-cell notes and AGENTS.md have no diff between these snapshots.
- PR105 source head: 40d56f5f8a54b1ed7b6125209903504f66e9a2a4; data path captures/2026-10-15T034434Z-codex-hopf-sectors-92216026/COMPLEX_AND_ACTION.json.
- PR106 source head: 2c4e4c89d25817cb0120916e28014c8b77a5527f; data paths captures/2026-10-15T040218Z-codex-reduced-dynamics-627a281a/{EXACT_SPECTRA.json,REDUCED_GENERATORS.json}.
- Existing repository reports: docs/UD_600Cell_Hopf_Sector_Assessment_v0.1.md, “Invariant-sector theorem”; docs/UD_600Cell_Reduced_Dynamics_v0.1.md, sections 1–2 and Appendix A. Their development status is retained. Reading an open PR source is not promotion or merger.
- The preceding local boundary/coframe audit v0.1 supplies the general observation criterion; this release computes the named carrier/shell. The attached historical ledger and governance proposal are not copied into this release or modified. The unavailable Genesis PNG remains unread and unused.

Run the scripts in this order in a clean directory with the bundled sources:

    python compute_sectors.py
    python exact_complex_rank.py
    python summarize.py
    python validate_geometry.py
    python build_witnesses.py
    python check_hidden_state.py

The module check_hidden_state.py additionally provides an exact integer-state membership test using output derivatives 0 through 104; its three examples include two persistently hidden states and the dynamically exposed central vertex. The exact replay uses NumPy, SciPy, SymPy and python-flint. No approximate eigensolver or tolerance is used for the rank conclusions. Finite-field checks are separately identified. The geometry validator records 26 check families, including exact golden-ratio adjacency, clique reconstruction, incidence counts, signed symmetry, chain symmetry, shell homology, snapshot orbit counts and agreement between exact and modular ranks. results files give all thirty exact component ranks and per-character certificates. The code and source hashes are recorded in the manifest.

Implementation correction during development: an initial extraction command used a wrong relative output directory and was rerouted before data use. A preliminary rational grouping by cyclotomic isotypic blocks was not used as isolated character ranks: because R is not equivariant, grouped image ranks need not be multiples of the field degree. The final computation instead expands BOTH source and output scalars through the regular number-field representation. Final exact ranks match two split-prime character calculations. This distinction is mathematically consequential and is recorded to prevent reuse of the grouped-rank shortcut.

The kernel is supplied as exact constraints and component dimensions, not a printed basis list. Whole source characteristic polynomials are used for ambient multiplicities but not rerun; the central total observability rank is independently saturated by the exact observer annihilator and component rank calculation. Finite sampling times, noise, conditioning, derivative estimation, finite bandwidth and realistic readout costs remain OPEN. Changing metric, rates, readout or interactions creates a new observation problem. Physical promotion remains 0.

## Next gate

Select extra observations that reduce the 747-dimensional kernel and certify their finite-sample conditioning. A two-dimensional-only shell observer necessarily misses the stationary fundamental C3 cycle under this generator; removing that last obstruction requires a readout with nonzero pairing against it, such as a declared tetrahedral-coordinate port. Additional boundary histories may address oscillatory hidden modes, but their gain must be calculated rather than inferred by adding isolated ranks. This is related to project REF01 (#136, observer/metric selection) and APP05 (#144, finite acquisition); neither task is declared closed by this conditional ideal readout.
