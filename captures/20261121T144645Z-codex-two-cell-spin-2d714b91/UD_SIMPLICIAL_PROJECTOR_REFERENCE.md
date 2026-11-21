# Simplicial incidence projectors

**Scope:** Orthogonal projection in the Euclidean coefficient metric. **Physical Promotion = 0.**

For an edge-by-face matrix \(M\), form the orthogonal projector onto the image of its columns:
\[
P=MM^+=M(M^\mathsf{T}M)^+M^\mathsf{T}.
\]
The Gram pseudoinverse reduces to the ordinary inverse when \(M\) has full column rank. An exact rational replay may choose independent columns \(C\) of \(M\) and compute \(C(C^\mathsf{T}C)^{-1}C^\mathsf{T}\). Both methods project to the same subspace. Check symmetry, idempotence, and \(PM=M\). For complex coefficients replace transpose with adjoint. For a declared positive coefficient metric \(W\), use \(C(C^\ast WC)^{-1}C^\ast W\) and test \(W\)-self-adjointness.

## Unsigned tetrahedral face overlaps

Each face has three edges and distinct faces in one tetrahedron overlap along one edge. Hence \(M^\mathsf{T}M=2I_4+J_4\) and its inverse is \(I_4/2-J_4/12\). The image projector has diagonal \(2/3\). The spectrum of \(MM^\mathsf{T}/3\) is \(2,2/3,2/3,2/3,0,0\). The diagonal alone cannot certify a projector. In the two-cell assembly with unique faces, the Gram entry is \(3\) on the diagonal and \(1\) or \(0\) according to shared-edge incidence. With cell-owned copies of the seam face, the Gram matrix also has a duplicated column and requires the pseudoinverse or the independent-column formula.

| Fixture | Matrix size | Rank | Projector trace |
| --- | --- | ---: | ---: |
| Unsigned single tetrahedron | \(6\times4\) | 4 | 4 |
| Unsigned two cells, unique faces | \(9\times7\) | 7 | 7 |
| Unsigned two cells, seam copied | \(9\times8\) | 7 | 7 |
| Signed two-cell simplicial boundary | \(9\times7\) | 5 | 5 |

The signed boundary fixture uses a different image from the unsigned incidence fixture. Each assembled projector is checked independently. The unique-face and copied-seam unsigned fixtures give exactly the same projector.

## Relationship to existing UD operators

For the single-cell unsigned face-edge map \(H=M^\mathsf T\), the full \(H^\mathsf TH\) has eigenvalue \(6\) on the constant edge vector and \(2\) on the three-dimensional mean-zero image. On the **mean-zero** edge space, \(H^\mathsf TH/2\) therefore gives the odd projector used by C06 v0.23. Its three-face formula also uses an inverse overlap Gram. Those formulas are valid in their declared subspaces. The Whitney face mass and two-cell additive dissipation Grams are quadratic forms, and their use does not require idempotence.

This reference applies to code that constructs an image projector from simplicial incidence. The companion replay uses the same rank-safe formula on all four fixtures.

- [UD C06 face projector cut v0.23](https://github.com/ud-tetra/UD/blob/d0fb71f1d0829d13cef851edbcccd2a0eb77e45d/captures/20261117T200440Z-codex-c06-face-projector-7bc4/UD_C06_FACE_PROJECTOR_CUT_v0.23.md)
