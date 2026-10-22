# Exact coarse transfer and dynamical leakage of the centered octahedral refinement

22 October 2026. **Development; exact finite-chain unit-metric result. Independent review: no. Physical promotion: 0.** This is a new additive capture extending the centered-octahedron test in draft PR #406. Its parent branch is that draft PR, so the new pull request is stacked and does not claim merger into `main`.

## Result in one paragraph

The original tetrahedron embeds by an explicit geometric subdivision chain map \(S\) into its full 12-cell, 85-coordinate edge-midpoint/center subdivision. An exact \(S_4\)-equivariant rational chain retraction exists. But with the unit simplex inner product and native skew-incidence generator, the embedded 15-coordinate space is **not dynamically invariant**. The orthonormal projected generator has characteristic polynomial \(\lambda(\lambda^2+4/3)(\lambda^2+2)^6\), instead of the seed's \(\lambda(\lambda^2+4)^7\). Its coupling to the discarded modes has squared Frobenius norm \(44/3\), or \(11/31\) of the squared action on an orthonormal coarse basis. This is reversible finite-chain leakage, not physical friction.

## 1. Explicit subdivision and its chain property

Write the old filled tetrahedral complex as \(C_\bullet\), with \(f=(4,6,4,1)\), and the complete refinement as \(\widetilde C_\bullet\), with \(f=(11,30,32,12)\). The six edge midpoints form the octahedral core, the centroid cones its eight shell faces, and four corner tetrahedra complete the original volume. Orient every simplex by increasing vertex index. The subdivision \(S_k:C_k\to\widetilde C_k\) assigns:

| Old generator | Fine chain | Number of supported simplices |
|---|---|---:|
| Vertex | Same vertex | 1 |
| Edge | Two oriented half-edges through its midpoint | 2 |
| Face | Three corner triangles plus the central midpoint triangle | 4 |
| Tetrahedral volume | All eight inner cells plus four corner cells with oriented signs | 12 |

The verifier computes every column and checks, over exact integers,

\[
\widetilde B_kS_k=S_{k-1}B_k\quad(k=1,2,3),\qquad
S_k^{\mathsf T}S_k=g_k I,
\quad(g_0,g_1,g_2,g_3)=(1,2,4,12).\tag{1}
\]

The Gram identity uses the declared *unit simplex coordinate* metric; it does not assign physical mass or area to a face. Assigning each edge midpoint to its lower-index old endpoint and the center to old vertex 0 yields a simplicial chain retraction \(D\) satisfying \(DS=I\). Such a deterministic vertex retraction cannot be \(S_4\)-equivariant: the stabilizer of an old edge midpoint swaps both its endpoint pair and the complementary pair, leaving no old vertex fixed. Averaging conjugates of \(D\) over the 24 tetrahedral permutations gives an **exact rational, equivariant chain retraction** \(D_{\rm sym}\) with \(D_{\rm sym}S=I\), verified grade by grade. Its rational signed coefficients are algebraic; a positive probabilistic readout is not thereby selected.

## 2. Metric projection fails as a chain retraction

The unit-metric least-squares left inverse on each grade is

\[
D_{\perp,k}=g_k^{-1}S_k^{\mathsf T},\qquad
P=SD_\perp.\tag{2}
\]

Although \(D_\perp S=I\) and \(P\) is an orthogonal projection, \(D_\perp\) does **not** commute with the boundaries. The exact defect \(B_kD_{\perp,k}-D_{\perp,k-1}\widetilde B_k\) has respectively 24, 48 and 48 nonzero matrix entries for \(k=1,2,3\). Existence of a topological coarse chain map therefore does not identify it with the unit-metric readout. A physical observable/metric choice must resolve this split.

## 3. Exact projected generator and leakage

Let \(A\) and \(\widetilde A\) be the old and fine skew Hodge–Dirac incidence generators with upper boundary blocks \(B_k\) and \(\widetilde B_k\) and negative transposed lower blocks. Let \(G=S^{\mathsf T}S\) (block scalars in Eq. (1)) and \(Q=SG^{-1/2}\), so \(Q^{\mathsf T}Q=I_{15}\). The orthonormal compression \(A_{\rm eff}=Q^{\mathsf T}\widetilde A Q\) has between-grade couplings

\[
\widehat B_k=\sqrt{\frac{g_{k-1}}{g_k}}B_k,
\qquad
(\widehat B_1,\widehat B_2,\widehat B_3)
=\left(\frac{B_1}{\sqrt2},\frac{B_2}{\sqrt2},\frac{B_3}{\sqrt3}\right).\tag{3}
\]

The verifier computes the exact rational characteristic polynomial using the similar coordinate operator \(G^{-1}S^{\mathsf T}\widetilde A S\):

\[
\boxed{\chi_{A_{\rm eff}}(\lambda)
=\lambda(\lambda^2+4/3)(\lambda^2+2)^6,}
\qquad
\chi_A(\lambda)=\lambda(\lambda^2+4)^7.\tag{4}
\]

No single global clock rescaling maps the two distinct projected frequencies \(2/\sqrt3\) and \(\sqrt2\) back to the old frequency 2. More decisively, the fine operator does not intertwine \(Q\). Define the high-sector leakage map

\[
L=(I-QQ^{\mathsf T})\widetilde A Q.\tag{5}
\]

The verifier evaluates Eq. (5) entirely in rational arithmetic by using \(S\), \(G^{-1}\), and the equivalent unnormalized residual \(\widetilde A S-SG^{-1}S^{\mathsf T}\widetilde A S\):

| Original chain grade | Basis count | \(\lVert L\rVert_F^2\) from that grade | Each basis direction |
|---|---:|---:|---:|
| \(C_0\) vertices | 4 | 6 | \(3/2\) |
| \(C_1\) edges | 6 | 6 | 1 |
| \(C_2\) faces | 4 | \(8/3\) | \(2/3\) |
| \(C_3\) volume | 1 | 0 | 0 |
| **Total** | **15** | **\(44/3\)** | |

Since \(\lVert A_{\rm eff}\rVert_F^2=80/3\) and \(\lVert\widetilde A Q\rVert_F^2=124/3\), the unit-metric ensemble fraction of **squared generator action** leaving the embedded coarse space is \((44/3)/(124/3)=11/31\). This is a basis-independent Frobenius ratio for *this specified coarse subspace and metric*, not a per-state loss fraction, entropy production, damping rate or graphite measurement. A particular state in the volume grade has zero instantaneous leakage, whereas generic vertex/edge/face states do not. The finite closed skew generator can return that amplitude later.

## 4. Interpretation and physical gate

The midpoint octahedron is a native combinatorial/geometric construction from UD's tetrahedron and provides an exact three-pair, eight-cell carrier. It does **not** preserve the seed's unit-weight dynamics under naïve refinement. Topological functoriality, an equivariant rational retraction, orthogonal metric readout and dynamical invariance are four separate requirements. The exact \(44/3\) leakage makes the choice of Hodge weights and contacts a concrete gate rather than a verbal concern.

For a physical graphite hypothesis, select a metric, time normalization and atomistic coupling from independently specified material data; evaluate whether an appropriate observable subspace remains robust when the continuum sheet is flat; then predict a held-out residual beyond honeycomb and moiré friction. The finite-chain transfer result by itself does not explain the 21.8°/38.2° peaks or dissipate energy. The released (2,1) full Hessian remains HOLD. The supplied coefficient ledger v0.39(2) retains the physical clock and open-system ports; CRL-2 is a governance proposal, and this constructor audit is not independent review. **Physical promotion: 0.**

## Reproduction

Run `python verify_coarse_transfer.py`. Standard-library integer and rational calculations build all coarse and fine simplex lists, exact boundary maps, the 24 signed symmetry actions, both retractions, and the full-block leakage. `RESULTS.json` stores the exact fractions, characteristic coefficients, and claim boundary. The parent capture is `2026-10-22T183342Z-codex-centered-octahedron-03df6bff-dcf6-4dee-b364-9b170b4885c5`. No archived research scripts, external experimental dataset, or unavailable image was executed or used.
