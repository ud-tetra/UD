# Centered octahedron from tetrahedral edge midpoints: an exact UD carrier test

22 October 2026. **Development; exact finite geometry and unweighted incidence only. Independent review: no. Physical promotion: 0.** This is an additive candidate following the icosahedral T=7 exploration in draft PR #405. It does not revise that capture or release the graphite (2,1) full-Hessian HOLD.

## Question and result

Can a center-coned triangular shell encode UD's six tetrahedral edges as three opposite pairs and its eight three-bit configurations without imposing a foreign polyhedron? **Yes, structurally.** The regular tetrahedron's six edge midpoints form a regular octahedron. Its eight triangular shell faces, coned to the tetrahedron's centroid, give eight congruent tetrahedral *inner* cells. One selected midpoint from each opposite pair labels each cell. Two cells share a radial triangle exactly when one selection changes. This is an exact cube adjacency, not a derivation of a physical bit-flip process.

There is an important volume qualification: the midpoint octahedron occupies **half** the volume of the original regular tetrahedron. Four additional corner tetrahedra are required to subdivide the *whole* original tetrahedron. The eight inner tetrahedra and four corner tetrahedra have different volumes and shapes. A theory of equivalent material cells therefore cannot adopt equal geometric masses by fiat.

## 1. Intrinsic relation to the UD tetrahedron

Choose a regular tetrahedron with vertices

\[
q_1=(1,1,1),\quad q_2=(1,-1,-1),\quad
q_3=(-1,1,-1),\quad q_4=(-1,-1,1).\tag{1}
\]

Its centroid is \(o=(0,0,0)\). The six edge midpoints are precisely

\[
\left\{\frac{q_i+q_j}{2}:1\leq i<j\leq4\right\}
=\{\pm e_1,\pm e_2,\pm e_3\}.\tag{2}
\]

An antipodal midpoint pair corresponds to two disjoint edges of the original tetrahedron. Thus the vertex space of this octahedral shell is exactly the six-coordinate permutation module on tetrahedral edges. As an inherited \(S_4\) module it has the same \(1\oplus2\oplus3\) decomposition as that *tetrahedral edge representation*. This does not equate the octahedron's own edge-space representation under its full symmetry group with the UD seed's edge representation; the repository's THM-568 concerns a different module.

The octahedral shell's faces are indexed by \(s=(s_1,s_2,s_3)\in\{-1,+1\}^3\):

\[
f_s=[s_1e_1,s_2e_2,s_3e_3],\qquad
T_s=[o,s_1e_1,s_2e_2,s_3e_3].\tag{3}
\]

Each \(T_s\) has volume \(1/6\), three radial edges of length 1, three base edges of length \(\sqrt2\), and a base triangle of area \(\sqrt3/2\). The inner cells are congruent **right** tetrahedra, not regular tetrahedra. The original tetrahedron has volume \(8/3\), while the midpoint octahedron has volume \(8(1/6)=4/3\).

The old vertices \(q_i\) each connect to their three incident edge midpoints, making four corner tetrahedra of edge length \(\sqrt2\) and volume \(1/3\) each. The twelve-cell union fills the original tetrahedron exactly: \(8(1/6)+4(1/3)=8/3\). This is a partition of the entire seed into two metric classes, with inner-to-corner volume ratio \(1:2\).

## 2. Exact complexes and incidence tests

| Carrier | \((V,E,F,C)\) | Chain dimension | \((\operatorname{rank}B_1,\operatorname{rank}B_2,\operatorname{rank}B_3)\) | Betti numbers |
|---|---:|---:|---:|---:|
| Octahedral boundary | \((6,12,8,0)\) | 26 | \((5,7,0)\) | \((1,0,1)\) |
| Center-coned octahedral ball | \((7,18,20,8)\) | 53 | \((6,12,8)\) | \((1,0,0,0)\) |
| Full tetrahedral midpoint subdivision | \((11,30,32,12)\) | 85 | \((10,20,12)\) | \((1,0,0,0)\) |

All oriented boundaries use the sorted-vertex alternating-sign convention. The bundled verifier constructs every simplex from Eq. (3), checks \(B_1B_2=B_2B_3=0\) exactly and computes ranks over \(\mathbb Q\) for the full subdivision. The octahedral ball has eight outer triangles (one incident 3-cell), twelve radial internal triangles (two incident cells), and Euler characteristic 1. The full subdivision has sixteen outer and sixteen internal triangles. Its four original boundary faces are each cut into four triangles. Determinants certify the volumes and their exact sum. The verifier constructs signed actions for all 24 tetrahedral vertex permutations and checks \(B_kT_k=T_{k-1}B_k\) on every chain grade; the two four-cell orbits below are preserved.

## 3. Three-bit cells and a symmetry distinction

Define \(\theta_i=(1-s_i)/2\), so \(\theta\in\{0,1\}^3\). Two inner cells share a radial triangle if and only if their words differ at exactly one coordinate. The cell adjacency graph is the 3-cube \(Q_3\). This geometry realizes *a candidate carrier* for the previously declared UD opposite-pair configuration space; it does not determine which cells are occupied or when transitions occur.

The parity \(s_1s_2s_3=(-1)^{w_H(\theta)}\) separates the eight inner cells into two orbits of four under the original tetrahedral \(S_4\): one orbit's shell faces point toward its original vertices, and the other lies within its original faces. A one-bit neighboring-cell step exchanges the orbits. This vertex/face distinction is inherited from the tetrahedron, while the full octahedral symmetry would permit transformations that forget which tetrahedron supplied the midpoints.

With the consistent physical orientation of the 3-cells, the cell incidence Gram matrix is exactly

\[
B_3^{\mathsf T}B_3=4I-A(Q_3),\qquad
\operatorname{spec}(B_3^{\mathsf T}B_3)
=\{1^{(1)},3^{(3)},5^{(3)},7^{(1)}\}.\tag{4}
\]

Thus the cube graph is present *inside the native simplicial incidence*, without adding a cube as a separate spatial cell. Eq. (4) is a statement about unit incidence weights; interpreting it as a transition-rate matrix would require a new rule.

## 4. Unit-incidence UD dynamics

Let \(A\) be the unweighted real skew Hodge–Dirac operator on \(C_0\oplus C_1\oplus C_2\oplus C_3\), with upper blocks \(B_k\) and lower blocks \(-B_k^{\mathsf T}\). Exact integer characteristic polynomials of \(B_1B_1^{\mathsf T}\), \(B_2^{\mathsf T}B_2\), and \(B_3^{\mathsf T}B_3\) factor as

\[
\begin{aligned}
\chi_{B_1B_1^{\mathsf T}}(x)&=x(x-5)^3(x-7)^3,\\
\chi_{B_2^{\mathsf T}B_2}(x)&=x^8(x-3)^3(x-5)^6(x-7)^3,\\
\chi_{B_3^{\mathsf T}B_3}(x)&=(x-1)(x-3)^3(x-5)^3(x-7).
\end{aligned}\tag{5}
\]

Because \(B_kB_{k+1}=0\), the nonzero singular sectors are orthogonal, giving

\[
\boxed{\chi_A(\lambda)
=\lambda(\lambda^2+1)(\lambda^2+3)^6
(\lambda^2+5)^{12}(\lambda^2+7)^7.}\tag{6}
\]

The dimension is \(1+2(1+6+12+7)=53\): **one constant zero mode and 26 reversible oscillator pairs**. The exact unit-incidence frequencies are \(1,\sqrt3,\sqrt5,\sqrt7\) with pair multiplicities \(1,6,12,7\). Full-block skew symmetry and the first three exact trace moments of \(-A^2\) check this factorization separately. In particular the coned octahedron does *not* have only the seed tetrahedron's unit frequency 2. The shell by itself has two zero modes and twelve oscillator pairs, with squared frequencies \(2^{(3)},4^{(6)},6^{(3)}\). The full twelve-cell subdivision's topological count is one zero and 42 oscillator pairs; its nonzero frequencies were not computed here.

No physical frequency follows from Eq. (6): it lacks an experimentally specified clock and energy scale, simplex metric/Hodge weights, contacts and bath. An arbitrary positive material metric can alter these dimensionless frequencies. Finite closed skew dynamics also supply no irreversible friction coefficient.

## 5. Relevance and next gate

This is a better **native geometry candidate** than a chosen icosahedral closure for UD's specific three opposite tetrahedral edge pairs, since the octahedral shell is an exact midpoint transform of the seed and the three-bit cube follows from its face adjacency. It is not a theorem that UD must choose the midpoint map in a physical material. The local triangular bipyramid remains the separate native carrier for the 2↔3 Pachner move. No identification with the flat graphite interface or its measured 21.8°/38.2° response is inferred from this three-dimensional shell.

To turn this into a physical hypothesis, specify a source-selected midpoint/refinement rule, an invariant material metric and readout, and a mapping from atomistic degrees of freedom to the selected subspace. Then compare a held-out response against the conventional honeycomb and moiré baseline; use an independently characterized open-system bath for damping. The coefficient provenance ledger v0.39(2) does not close the relevant time/energy normalization or dissipation ports. The supplied CRL-2 subdivision remains a governance proposal, and this constructor check is not independent review. **Physical promotion stays 0.**

## Sources and reproducibility

- S. Reid, *Rectifications of Convex Polyhedra* (2016), https://arxiv.org/abs/1604.00580, documents the tetrahedron-to-octahedron rectification. Eqs. (1)–(6) and the full subdivision are reproduced directly by the local verifier rather than borrowed as a physical model.
- Existing UD `docs/THM-568_Tetrahedral_Uniqueness_v1.0.md` establishes the scope of the tetrahedral edge-space representation; draft PR #405 treats the icosahedral T=7 lattice comparison separately.
- `verify_centered_octahedron.py` uses standard-library exact integers, rationals and determinant checks; `RESULTS.json` records the computed incidence and spectrum. No experimental data, archived scripts, or unavailable image were used.
