# Structural exclusivity and the single-cell U(1) boundary

**EXACT_INTERNAL / CONDITIONAL / NO-GO. Physical Promotion = 0.**

This constructor draft addresses the first two actions in the supplied theory roadmap. It uses the filled oriented tetrahedron on four vertices, the three opposite-edge pairs, and the unit simplex inner products. Independent review is open. No measured target enters either derivation.

## 1. What fixes the 192 = 185 + 7 split

Let \(P=\{\{01,23\},\{02,13\},\{03,12\}\}\) be the set of unordered opposite-edge pairs of \(K_4\). Define \(\Theta=\mathbb F_2^P\) and the exposure set \(X=\operatorname{Aut}(K_4)\times\Theta\). The fiber model makes one independent binary assignment per pair. Since every permutation of the vertices is an automorphism, \(|X|=4!\,2^3=192\). The four chain grades of the filled tetrahedron have dimensions \(4,6,4,1\), so their total dimension is 15. The alternating Euler characteristic is \(4-6+4-1=1\).

**Conditional exclusivity.** Fix the reference exposure \(g_*=e\) and impose two conditions.

1. Every defect has exposure coordinate \(e\).
2. Within that fiber the zero assignment is active and every nonzero assignment is defective.

There is exactly one subset satisfying these conditions, \(D=\{e\}\times(\Theta\setminus\{0\})\). Thus \(|D|=7\) and \(|X\setminus D|=185\). The distinguished identity is intrinsic to a group model for the exposure coordinate. If exposures are instead a torsor of frames, choosing a reference frame supplies that coordinate. The proof depends on the defect law as well as on the exposure carrier.

The count is compatible with the natural relabeling action \((g,\theta)\mapsto (hgh^{-1},h\cdot\theta)\). Vertex permutations act on the three pairs through \(S_4\to S_3\), and the fiber orbits are the four Hamming-weight classes, of sizes \(1,3,3,1\). Using the induced semidirect product law gives the same cardinality as the Cartesian product. This count alone leaves the group law and its physical relevance undetermined.

**Carrier-only no-go.** Symmetry does not force the defect law. Even with the reference fiber fixed and zero active, retaining only the weight-one assignments as defects gives an invariant three-element set and \(192=189+3\). If invariance is taken under transitive left translation on the full exposure group, the only invariant subsets are the empty set and the full set. A proper seven-element defect therefore needs an action and a selection rule stated explicitly. A replacement for the conditional theorem would need to derive that selection rule from additional native axioms and rule out the weight-one alternative.

**Coupling scope.** For the real three-dimensional standard \(S_4\) representation \(V\) and an invariant inner product, \(\dim\operatorname{Sym}^2_0(V)=3(3+1)/2-1=5\). Consequently \(5|X|/|D|=960/7\) under the stated defect rule. The factor is a dimension. To identify this expression with an inverse coupling, derive the choice of sector, the scalar observable, its normalization, and the coupling map independently of the target. The available invariant inner product also admits a scalar multiple, so equivariance alone cannot fix the normalization of a quadratic observable.

## 2. Which continuous U(1) the skew Hodge–Dirac flow supplies

Orient simplices by increasing vertex order and let \(B_k:C_k\to C_{k-1}\) be their signed boundaries. Write \(B\) for the total boundary and \(A=B^\mathsf{T}-B\). Set \(Z_1=\ker B_1=\operatorname{im}B_2\) and \(Y_2=\operatorname{im}B_2^\mathsf{T}\). Each has dimension three.

In the exterior-algebra realization of the full simplex, the boundary is contraction by \(u=(1,1,1,1)\), and the adjoint is exterior multiplication by \(u\). Their anticommutator is \(\|u\|^2 I=4I\). In edge degree this gives \(B_1^\mathsf{T}B_1+B_2B_2^\mathsf{T}=4I\). Therefore \(U=B_2^\mathsf{T}/2:Z_1\to Y_2\) is an isometric isomorphism. The boundary identities give \(B_3^\mathsf{T}U=0\) and
\[
Ax=2Ux,\qquad A(Ux)=-2x,\qquad x\in Z_1.
\]
On \(Z_1\oplus Y_2\), identification \(x+Uy\leftrightarrow x+iy\) makes \(A\) multiplication by \(2i\). Hence \(e^{sA}\) gives the faithful common phase action \(x+iy\mapsto e^{2is}(x+iy)\), with \(s\) modulo \(\pi\). This is an exact \(U(1)\) dynamical symmetry of the paired sector.

A nonzero pure edge cycle moves into face degree under \(A\), so the pure edge cycle space fails invariance under the flow. On the graph alone, omitting the 2-simplices gives \(Ax=0\) for every \(x\in\ker B_1\). These two cases delimit what the generator forces.

### Local gauge transformations and Wilson loops

A compact edge-connection model has a separate construction. Specify edge phases in \(\mathbb R/2\pi\mathbb Z\) and vertex gauge transformations \(a\mapsto a+B_1^\mathsf{T}\chi\) modulo \(2\pi\). For an integer cycle \(z\), \(W_z(a)=\exp(i z^\mathsf{T}a)\) is gauge invariant by \(B_1z=0\). A spanning tree removes three edge phases by gauge choice, leaving three independent loop phases. Equivalently, the graph orbit space is \(\operatorname{Hom}(\ker_{\mathbb Z}B_1,U(1))\cong U(1)^3\). In the filled tetrahedron the integer face boundaries generate the integer cycle lattice, so a flat compact connection has trivial loop holonomy and is gauge-equivalent to zero.

**Gap 4 disposition.** The paired-sector circle action is derived exactly. The compact edge gauge model is conditional on declaring the compact connection variables and their local symmetry. The Hodge–Dirac action by itself supplies one evolution parameter, whereas vertex-dependent gauge transformations and independently variable Wilson loops require additional structure. The next proof obligation is an explicit map from native UD states and transport rules to compact edge connections that intertwines vertex gauge transformations and yields a nontrivial gauge-invariant loop phase. Non-Abelian forcing and continuum coupling flow remain open.

## Verification

An independent exact-arithmetic replay assembled the signed incidence matrices from lexicographically ordered simplices. It checked boundary nilpotency, ranks of \(B_1\) and \(B_2\), the degree-one Laplacian identity, the paired rotation on a cycle basis, the isometry, and the unimodular chord coordinates of the fundamental integer cycles. Enumerating the 24 vertex permutations independently recovered six induced permutations and four fiber orbits of sizes \(1,3,3,1\). These are constructor checks.
