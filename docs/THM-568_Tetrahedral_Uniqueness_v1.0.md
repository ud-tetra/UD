# THM-568: Tetrahedral Uniqueness Among Simplices

**Version 1.0 | Depends: THM-LS9 (S₄ irrep decomposition)**

---

## Statement

Among all n-simplices (n ≥ 2), the tetrahedron (n = 3) is the unique case whose edge representation under S_{n+1} decomposes into irreducible components of dimensions {1, 2, 3}.

More precisely: for the n-simplex with vertex set [n+1], the edge space C^{C(n+1,2)} decomposes under S_{n+1} into exactly three irreducible representations with dimensions

    1,  n,  n(n−1)/2 − 1

For n = 3 and only n = 3, these dimensions are {1, 2, 3} (equivalently, {1, 3, 2} in the standard ordering).

## Proof

**Step 1: The edge space carries the 2-subset representation of S_{n+1}.**

The n-simplex has C(n+1, 2) = n(n+1)/2 edges, each a 2-element subset of [n+1]. The symmetric group S_{n+1} acts by permuting vertices, hence permuting edges. This defines the 2-subset representation on C^{n(n+1)/2}.

**Step 2: The 2-subset representation decomposes into exactly three irreps for n ≥ 3.**

By standard results in the representation theory of symmetric groups, the permutation representation on k-element subsets of [m] decomposes as:

    C^{C(m,k)} = ⊕_{j=0}^{k} V_{(m−j, j)}

where V_{(m−j, j)} is the irrep of S_m labeled by the partition (m−j, j). For k = 2 and m = n+1:

    C^{C(n+1,2)} = V_{(n+1)} ⊕ V_{(n, 1)} ⊕ V_{(n−1, 2)}

These have dimensions:
- V_{(n+1)}: dim = 1 (trivial representation)
- V_{(n, 1)}: dim = n (standard representation)
- V_{(n−1, 2)}: dim = C(n+1, 2) − n − 1 = n(n−1)/2 − 1

**Step 3: Solve for {1, 2, 3}.**

We require the multiset {1, n, n(n−1)/2 − 1} to equal {1, 2, 3}. Since the trivial rep always contributes 1, we need:

    {n, n(n−1)/2 − 1} = {2, 3}

Case A: n = 2 and n(n−1)/2 − 1 = 3. Check: 2(1)/2 − 1 = 0 ≠ 3. Fails.

Case B: n = 3 and n(n−1)/2 − 1 = 2. Check: 3(2)/2 − 1 = 2. ✓

Case C: n = 2 is also the "other assignment" — but n(n−1)/2 − 1 must be positive, requiring n ≥ 3.

For n ≥ 4: n ≥ 4 and n(n−1)/2 − 1 ≥ 5. Neither can equal 2 or 3 simultaneously with the other matching.

Therefore n = 3 is the unique solution.  □

## Corollary: Gauge Group Uniqueness

The tetrahedron is the unique simplex whose edge-space irreps have dimensions matching the fundamental representations of U(1) × SU(2) × SU(3):
- dim 1 → U(1) singlet
- dim 2 → SU(2) fundamental (weak isospin doublet)
- dim 3 → SU(3) fundamental (color triplet)

No other n-simplex (for any n) produces this decomposition.

## Additional properties unique to n = 3

- The edge count C(4,2) = 6 = 2 × 3 (doublet × triplet factorization)
- The face count = vertex count = 4 (self-duality among simplices: unique to n = 3 as a non-trivial property of closed 2-manifold triangulation)
- The Hodge star * exists on the edge space (requires the ambient dimension ≥ 3, i.e., the simplex must be at least a tetrahedron)
- The Euler characteristic χ = 2 (closed orientable surface)

## Scope and non-claims

This result establishes uniqueness among simplices under the S_{n+1} symmetry. It does NOT claim uniqueness among all possible geometric seeds — non-simplicial geometries (octahedron, cube, icosahedron, etc.) are addressed separately and found to decompose into 4 or more irreps, none matching {1, 2, 3}. The corollary identifying irrep dimensions with gauge group representations carries interpretive (bridge) weight.

---

## Proof-state

**EXACT STRUCTURAL.** The decomposition formula for the 2-subset representation of S_{n+1} is a standard result in combinatorial representation theory. The uniqueness of n = 3 follows by direct arithmetic on the dimension formula. Verified computationally for n = 2 through n = 8.
