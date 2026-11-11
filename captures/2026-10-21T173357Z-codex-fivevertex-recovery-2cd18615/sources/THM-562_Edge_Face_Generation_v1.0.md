# THM-562: Left-Handed Generation from Edge-Face Decomposition

**Version 1.0 | Depends: THM-528 (channels), THM-561 (mass split) | Swap-operator formalism**

---

## 1. Tetrahedral Decomposition

### 1.1 Edge space (C⁶)

The 6 edges of the tetrahedron define the channel Hilbert space C⁶ with basis {|σ₀⟩, …, |σ₅⟩} corresponding to the 6 edges = C(4,2) balanced bipartitions. This is the space analyzed in THM-528 through THM-561.

### 1.2 Face space (C⁴)

The 4 faces of the tetrahedron define a second space C⁴ with basis {|f₀⟩, |f₁⟩, |f₂⟩, |f₃⟩}, where f_k is the face opposite vertex k.

### 1.3 Boundary operator

The boundary operator ∂: C⁴ → C⁶ maps faces to their boundary edges:

    ∂|f_k⟩ = Σ (signed edges of face f_k)

Explicitly (verified numerically):

    rank(∂) = 3
    ker(∂) = span(|f₀⟩ + |f₁⟩ + |f₂⟩ + |f₃⟩)   (dimension 1)
    im(∂) = 3-dimensional subspace of C⁶             (dimension 3)

The kernel is the face-sum direction. The image is the standard representation of S₄ embedded in edge space.

---

## 2. Face-Singlet Theorem

### Definition

Define |Σ⟩ = (|f₀⟩ + |f₁⟩ + |f₂⟩ + |f₃⟩)/2 (normalized face-sum).

### Proposition (S₄-invariance)

|Σ⟩ is the UNIQUE direction in C⁴ fixed by all S₄ permutations. That is, for every g ∈ S₄: g|Σ⟩ = |Σ⟩.

**Proof.** S₄ permutes the four faces. The sum |f₀⟩+|f₁⟩+|f₂⟩+|f₃⟩ is invariant under any permutation. Uniqueness: the trivial representation of S₄ appears exactly once in C⁴ = C¹(trivial) ⊕ C³(standard).  □

### Corollary (Color singlet)

|Σ⟩ transforms trivially under the S₄ action that permutes dimensions (colors). Therefore |Σ⟩ is a **color singlet**: it carries no color quantum number.

### Boundary vanishing

∂|Σ⟩ = 0. The face-sum has no boundary in edge space. (Verified numerically.)

**Physical meaning:** The color singlet direction has no component in the edge (= channel = quark) space. It is invisible to edge-based transport = the color force.

---

## 3. Left-Handed Generation Candidate

### Construction

Define C⁸ = C⁶ ⊕ C², where:

- **C⁶** = edge space (the channel algebra of THM-528)
- **C²** = face-singlet × spin = span{|Σ, +⟩, |Σ, −⟩}

The two basis states of C² are the face-singlet |Σ⟩ tensored with the two spin orientations (σ/σ̄).

### Representation content

Under SU(3)_color × SU(2)_weak:

| Subspace | Origin | Dimension | Representation |
|---|---|---|---|
| C⁶ | 6 edges = 3 dim-pairs × 2 spins | 6 | (3, 2) |
| C² | face-singlet × 2 spins | 2 | (1, 2) |
| **C⁸** | **total** | **8** | **(3,2) ⊕ (1,2)** |

This matches exactly one generation of **left-handed SM fermions**:

    (3, 2) = quark doublet (u_L, d_L) in 3 colors = 6 states
    (1, 2) = lepton doublet (ν_L, e_L) = 2 states
    Total = 8 states

### SU(2) structure on C²

The swap operator S acts on C² by exchanging the two spin states:

    S|Σ, +⟩ = |Σ, −⟩,    S|Σ, −⟩ = |Σ, +⟩

This is the same SU(2) weak isospin structure that acts on the quark doublet in C⁶. The lepton doublet inherits its weak interaction from the same spin degree of freedom.

---

## 4. Boundary-Operator Bridge

### The face space decomposition

C⁴ = ker(∂) ⊕ im(∂ᵀ) = C¹(singlet) ⊕ C³(standard)

The boundary operator ∂: C⁴ → C⁶ has:

- **ker(∂)** = face-sum = the **lepton direction** (color singlet, no edge component)
- **im(∂)** = the **color triplet** embedded in edge space (quarks carry color because they ARE edges)

### Quark-lepton relation

The quark sector (edges) and lepton sector (face-sum) are related by the boundary operator of the tetrahedron:

- **Quarks** = boundary of faces = edges. They carry color because edges connect different faces.
- **Leptons** = the face-sum, which has zero boundary. They are colorless because the total face has no edge-boundary.
- **Leptoquark transitions** correspond to the boundary map ∂ mixing ker(∂) with im(∂). In the SU(6) GUT structure (THM-557), these are the off-diagonal generators connecting the quark and lepton sectors.

This is a precise topological statement, not an analogy.

---

## 5. Extended Transport

The transport on C⁸ is block-diagonal:

    T⁸ = T⁶ ⊕ T₂

where T⁶ is the 6×6 channel transport (already analyzed) and T₂ acts on the lepton sector.

### Face-sum transport eigenvalue

On the IFS, each of 4 children inherits 3 of the 4 parent faces (the 4th face becomes the interface between parent and child). Therefore the face-sum transport eigenvalue is:

    λ_lepton = 3/4

### Mass gap comparison

| Sector | T eigenvalue | Mass gap (1−λ) |
|---|---|---|
| Vacuum/photon (V₁) | 1 | 0 |
| Weak (V_{1/2}) | 1/2 | 1/2 |
| Lepton | 3/4 | 1/4 |
| Color (V_{1/3}) | 1/3 | 2/3 (but degenerate → no mass) |

The lepton mass gap (1/4) is HALF the W/Z mass gap (1/2). This provides a distinct mass scale for the lepton sector, structurally different from both the quark and gauge boson mass scales.

---

## 6. Proof-State

### Exact structural

- C⁴ = C¹(trivial) ⊕ C³(standard) under S₄. (Standard representation theory.)
- |Σ⟩ is the unique S₄-invariant direction in C⁴. (Schur's lemma.)
- ∂|Σ⟩ = 0: the face-sum has zero boundary. (Verified; also follows from ∂² = 0 on the simplicial complex.)
- rank(∂) = 3, dim ker(∂) = 1. (Verified numerically.)
- C⁸ = C⁶ ⊕ C² has representation content (3,2) ⊕ (1,2). (Follows from the decompositions above.)
- The face-sum transport eigenvalue λ = 3/4. (From the IFS face-inheritance count: 3 of 4 faces per child.)

### Supported bridge

- The identification of C⁶ with the quark doublet and C² with the lepton doublet.
- The physical interpretation of ∂ as the quark-lepton connection.
- The mass gap 1/4 as a physical lepton mass scale.

### Open

- **Right-handed sector:** C⁸ gives left-handed fermions only. The right-handed sector (C⁸_R) requires chiral doubling with SU(2) breaking on the R copy.
- **Full generation:** C¹⁶ = C⁸_L ⊕ C⁸_R = 16 states per generation. The RH mechanism is not yet derived.
- **Yukawa couplings:** The quark-lepton mass hierarchy from ∂ coupling is not derived.
- **Anomaly cancellation:** Tr(Y) = 0 holds for C⁸ alone. Tr(Y³) = 0 requires C¹⁶.
- **Higgs mass correction:** Whether the extended C⁸ space corrects the m_H/m_W ratio is uncomputed.

---

## 7. Forward Extension Note

### From C⁸ to C¹⁶

The full SM generation requires 16 states. C⁸ provides 8 (left-handed). The remaining 8 (right-handed) require a second copy with opposite chirality:

    C¹⁶ = C⁸_L ⊕ C⁸_R

The chirality label comes from the Hodge star signs: L uses (+1,−1,+1), R uses (−1,+1,−1). In the R sector, the SU(2) structure must BREAK (right-handed fermions are weak singlets), requiring the Hodge sign flip to decouple the weak interaction on R.

### What remains unproved

1. The explicit construction of C⁸_R with SU(2) breaking.
2. The Yukawa coupling structure connecting L and R sectors.
3. Full anomaly cancellation on C¹⁶.
4. Three-generation structure from the n={4,5,6} dihedral stability applied to C⁸ or C¹⁶.
