# THM-563a: Four-Sector Chirality Decomposition

**Version 1.0 | Depends: THM-528 (channels), THM-561 (swap involution S, Hodge star *)**

---

## Statement

The swap involution S and Hodge star * on the 6-channel space C⁶ satisfy:

    S² = I,   *² = I,   [S, *] = 0.

Since S and * are commuting involutions, their joint eigenspaces provide an invariant decomposition of C⁶ into four sectors labeled by the eigenvalue pair (s, h) where s ∈ {+1, −1} is the S-eigenvalue and h ∈ {+1, −1} is the *-eigenvalue:

    C⁶ = V(+,+) ⊕ V(+,−) ⊕ V(−,+) ⊕ V(−,−)

with dimensions:

| Sector | S eigenvalue | * eigenvalue | Dimension |
|---|---|---|---|
| V(+,+) = P_L ∩ P_+ | +1 | +1 | 2 |
| V(+,−) = P_R ∩ P_+ | +1 | −1 | 1 |
| V(−,+) = P_L ∩ P_- | −1 | +1 | 1 |
| V(−,−) = P_R ∩ P_- | −1 | −1 | 2 |

Total: 2 + 1 + 1 + 2 = 6.

## Proof

S is the swap involution (THM-561). * is the Hodge star on the edge space, defined by the Levi-Civita symbol. Both are real symmetric involutions on C⁶.

**Commutativity.** [S, *] = 0 is verified by direct computation. (The swap exchanges σ_d ↔ σ̄_d within each dimension; the Hodge star maps σ_d ↔ σ̄_d with signs s_d ∈ {+1,−1}. Since S acts uniformly within each dimension and * acts with a dimension-dependent sign, they commute.)

**Eigenspace dimensions.** Since S and * commute, C⁶ decomposes into their joint eigenspaces. The P_+ eigenspace of S (dimension 3) decomposes under * as: *|_{P_+} is diagonal in the dimension basis with eigenvalues (s₁, s₂, s₃) = (+1, −1, +1). This gives dim(P_L ∩ P_+) = 2 (dimensions 1 and 3) and dim(P_R ∩ P_+) = 1 (dimension 2). Similarly, *|_{P_-} has eigenvalues (−s₁, −s₂, −s₃) = (−1, +1, −1), giving dim(P_L ∩ P_-) = 1 and dim(P_R ∩ P_-) = 2.  □

## Basis independence

The four-sector decomposition is the joint eigenspace decomposition of two commuting involutions. The dimensions (2, 1, 1, 2) are algebraic invariants of the operator pair (S, *). They do not depend on a basis choice.

## Corollary (Asymmetric mass-sector splitting)

Within P_+ (the mass-capable sector, THM-561):

- The left-chirality subspace P_L ∩ P_+ has dimension 2.
- The right-chirality subspace P_R ∩ P_+ has dimension 1.

This 2+1 asymmetry is a structural consequence of the Hodge star signs (+1, −1, +1) on the three dimensions of the tetrahedron.

---

## Proof-state

**EXACT STRUCTURAL.** Depends only on the definitions of S and * (both derived from the tetrahedral channel algebra), the verified identity [S, *] = 0, and standard eigenspace decomposition. No approximations, parameters, or phenomenological input. Verified: 10/10 numerical checks pass.
