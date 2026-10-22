# The icosahedron and the graphite (2,1) lattice: an exact geometric bridge with a dynamical boundary

22 October 2026. **Development — no registry entry; physical promotion 0.** Constructor calculations only. This note follows the graphite working paper (draft PR #402) and material-port analysis (draft PR #404) without editing them.

## 1. Three distinct carriers

1. The *regular icosahedron boundary* is a triangulated sphere with \((V,E,F)=(12,30,20)\), chain dimension 62 and homology \((b_0,b_1,b_2)=(1,0,1)\). Five equilateral triangular faces meet at every vertex. Its dual is the dodecahedron.
2. The *600-cell boundary* is a triangulated three-sphere with \((120,720,1200,600)\). The link of each 600-cell vertex is precisely an icosahedral two-sphere, and the closed star is a cone over that link. The link is a two-dimensional subcomplex; it is not the whole 600-cell or an automatically invariant subspace of its incidence generator. The existing UD link readout has 62 channels and an ideal history rank of 1893 on the declared 2640-dimensional ambient chain space; that older result is not recomputed here.
3. The *flat graphite bilayer* has a honeycomb atomic graph over a triangular Bravais lattice. Its (2,1) moiré cell is an area-seven planar lattice construction. A flat sheet has none of the icosahedron's twelve fivefold curvature defects. The graphite angles must first be explained by the ordinary Bravais construction.

Keeping these carriers separate prevents a shared integer or face shape from becoming a physical identification.

## 2. Exact icosahedron incidence and spectrum

Represent \(\phi=(1+\sqrt5)/2\) symbolically by the ring \(\mathbb Z[\phi]\) with \(\phi^2=\phi+1\). From the twelve coordinate permutations \((0,\pm1,\pm\phi)\), \((\pm1,\pm\phi,0)\), \((\pm\phi,0,\pm1)\), connect pairs at squared distance four and take all three-cliques as oriented faces. The bundled standard-library verifier reconstructs exactly 30 edges and 20 faces, checks degree five at all twelve vertices, edge incidence two, and the oriented relation \(B_1B_2=0\). In this connected sphere, \(\operatorname{rank}B_1=11\) and \(\operatorname{rank}B_2=19\).

For the unit-simplex metric, let \(L_0=B_1B_1^T\) and \(L_2=B_2^TB_2\). Exact integer characteristic-polynomial computation and independent multiplication of the displayed factors give

\[
\begin{aligned}
\chi_{L_0}(x)&=x(x-6)^5(x^2-10x+20)^3,\\
\chi_{L_2}(x)&=x(x-2)^5(x-3)^4(x-5)^4(x^2-6x+4)^3.
\end{aligned}\tag{1}
\]

The zeros are the constant vertex state and oriented fundamental face cycle. For the UD-style unweighted skew incidence generator \(A\) on \(C_0\oplus C_1\oplus C_2\), orthogonality of gradient and face-boundary images gives

\[
\boxed{\begin{aligned}
\chi_A(\lambda)={}&\lambda^2(\lambda^2+6)^5
\,(\lambda^4+10\lambda^2+20)^3\\
&\times(\lambda^2+2)^5(\lambda^2+3)^4(\lambda^2+5)^4
\,(\lambda^4+6\lambda^2+4)^3.
\end{aligned}}\tag{2}
\]

Its degree is 62: **two harmonic zero modes and thirty reversible oscillator pairs**. This is an exact finite-chain spectral result for the declared unit metric, not a graphite phonon spectrum, physical clock, or dissipative rate. Changing edge/face weights changes the spectrum; topology protects only the Betti dimensions.

## 3. Why the same seven appears in a refined icosahedron

Let \(a_1,a_2\) be unit directions of a flat triangular lattice meeting at 60°. A Coxeter/Goldberg triangular face can use the large edge \(u=2a_1+a_2\), and its 60° rotate \(v=-a_1+3a_2\). The oriented lattice determinant is \(2\cdot3-(-1)\cdot1=7\), hence each large icosahedral face has area equal to seven primitive triangular cells. Graver and Brinkmann *et al.* describe the icosahedral construction in triangular-lattice coordinates. The standard Goldberg/Caspar–Klug T=7 combinatorial object has fivefold and sixfold sites. Our local verifier does **not** construct that object; it audits the base shell and exhibits why the index seven alone does not determine it.

The straight-edged large triangle has only its three macro vertices on the boundary and three additional lattice points inside. One explicit triangulation with those six vertices has seven faces of lattice determinant one, twelve edges, and a disk Euler characteristic of one. **Those faces need not have unit edges or be equilateral.** Gluing twenty such patches along the thirty macro edges yields a spherical triangulation with the same face counts as the standard T=7 Goldberg construction:

\[
T=2^2+2\cdot1+1^2=7,
\quad F=20T=140,
\quad E=30T=210,
\quad V=10T+2=72.\tag{3}
\]

**Selection gap:** the explicit straight-edge patch has all six local vertices of degree four. When twenty copies are glued, the twelve old corners have degree fifteen and the sixty new vertices degree four. Its valence sum \(12(15)+60(4)=420=2E\), and its defect-index sum \(12(6-15)+60(6-4)=12\). It therefore fails the standard fivefold/sixfold pattern despite having exactly the same \((V,E,F)\) and area index. This is a counterexample to selecting an icosadeltahedral lattice from \(T=7\) or Euler counts alone. Applying the equilateral-triangle angular-defect formula to these non-equilateral patch faces would be invalid.

For the **standard** T=7 Goldberg/Caspar–Klug icosadeltahedron, twelve degree-five and sixty degree-six vertices give \(\sum_v(6-\deg v)=12\). In its intrinsic equilateral triangular metric, each fivefold site has defect \(2\pi-5\pi/3=\pi/3=60^\circ\), totaling \(4\pi\), whereas the flat planar lattice has no fivefold closure defects. Its trivalent dual has twelve pentagonal faces, sixty hexagonal faces and 140 vertices, a C140 fullerene *graph*. These are the literature construction's combinatorial counts, not a construction verified by the bundled script or a claim of chemical stability.

Either spherical triangulation has chain dimension \(72+210+140=422\). Sphere homology gives boundary ranks \(71,139\), two harmonic zero modes and 210 oscillator pairs for the unweighted incidence generator, though their nonzero frequencies and mode shapes depend on the actual graph and weights. A standard Goldberg T=7 link is **not** the original 62-coordinate vertex link of the unrefined 600-cell. A surjective linear coarse map 422→62 has a 360-dimensional kernel, and a chain map must additionally satisfy \(D_{k-1}B_k^{T7}=B_k^{T1}D_k\). Intertwining the skew Hodge dynamics requires compatible adjoints and metric, not merely the boundary identity. No such UD source-selected coarse map is asserted here.

## 4. The exact relation to the graphite angles, and its limit

The (2,1) *candidate macro edge* lies at angle

\[
\alpha=\arg(2a_1+a_2)=\arctan(\sqrt3/5)=19.1066053509\ldots^\circ.\tag{4}
\]

Its mirrored edge lies at \(60^\circ-\alpha=40.8933946491\ldots^\circ\). In graphite the two equal-length registry vectors are \(2a_1+a_2\) and \(a_1+2a_2\), so their *relative* twist is

\[
\theta=(60^\circ-\alpha)-\alpha=60^\circ-2\alpha
=\arccos(13/14)=21.7867892983\ldots^\circ,\quad
60^\circ-\theta=2\alpha=38.2132107017\ldots^\circ.\tag{5}
\]

This precisely relates the candidate T=7 macro-edge orientation to both paired graphite angles. The macro-edge angle is **19.1066°**, not **21.7868°**; confusing the edge with the relative twist would be a mathematical error. The common \(T=7\) is the same triangular-lattice norm used in two different constructions. The *standard Goldberg* icosadeltahedron adds twelve 60° curvature deficits when the planar triangulation is closed onto a sphere. A flat graphite interface has no such closure, and Chen *et al.* already attribute the paired twist peaks to (2,1) commensurate moiré geometry. Thus this exact bridge gives a clean UD geometric comparison but no excess friction coefficient, damping law, or evidence that an icosahedral mode participates in the experiment.

## 5. Native UD and physical next gate

The first mathematical task is to construct and audit the *standard* T=7 icosadeltahedral incidence graph (the straight patch demonstrably does not suffice), then build a refined-link chain/coarse-graining map and compare its Hodge blocks with the 600-cell link. A claim of inherited dynamics needs an explicit intertwiner and controlled discarded sector, not only matching homology. A native UD selector must then explain why such a refined link and its orientation are chosen, and how a matter contact writes/reads it. The user-supplied coefficient ledger leaves physical time/energy normalization and open-system constitutive loss unresolved. The supplied CRL-2 subdivision is a proposal; constructor checking does not satisfy its non-constructor review gate.

For graphite specifically, test a *separately specified* physical mapping from atomistic honeycomb and moiré modes into that refined link, including units, load dependence and bath export. It must predict a held-out friction or mode response beyond a conventional full atomistic baseline. The archived released (2,1) Hessian remains HOLD; the earlier conservative coupling norms and finite harmonic bath memory do not provide such a physical correspondence. **Physical promotion remains 0.**

## Sources and check scope

- Chen *et al.*, *Phys. Rev. Lett.* **137**, 166201 (2026), https://doi.org/10.1103/ly48-b4l2 — accessible abstract only, reporting small paired peaks and negligible measured load dependence.
- J. E. Graver, *Encoding Fullerenes and Geodesic Domes*, *SIAM Journal on Discrete Mathematics* **17**, 596–614 (2004), https://doi.org/10.1137/S0895480101391041 — accessible abstract explains icosahedral signatures using triangular-lattice edge coordinates; full article unavailable.
- G. Brinkmann, P. Goetschalckx and S. Schein, *Goldberg, Fuller, Caspar, Klug and Coxeter and a general approach to local symmetry-preserving operations* (2017), https://arxiv.org/abs/1705.02848 — explains the distinct literature constructions. The abstract and accessible paper inform terminology; the script does not verify a full Goldberg T=7 net.
- Existing UD `docs/UD_600Cell_Hopf_Sector_Assessment_v0.1.md`, `docs/UD_600Cell_Reduced_Dynamics_v0.1.md`, and `UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.md` in the session publication capture. They distinguish the vertex link from the full 600-cell and bound the scope of this comparison.
- `verify_icosahedron_t7.py` uses exact integer arithmetic for incidence and characteristic polynomials, \(\mathbb Z[\phi]\) for geometric adjacency, and floating point only for displayed decimal angles. `RESULTS.json` retains counts, integer characteristic coefficients, the deliberately non-Goldberg straight patch and angle displays. No standard T=7 graph, material dynamics or experimental curve was computed. `Gap2_FINAL_Finite_Genesis.png` was unavailable and unused.
