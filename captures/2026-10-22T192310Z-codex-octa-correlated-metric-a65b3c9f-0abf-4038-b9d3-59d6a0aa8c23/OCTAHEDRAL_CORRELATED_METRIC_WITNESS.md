# An equivariant correlated metric that preserves the octahedral subdivision's seed modes

22 October 2026. **EXACT, conditional finite-chain existence; constructor verified; no independent review; physical promotion 0.** This capture is stacked on draft PR #408 (positive diagonal metric no-go), #407 (subdivision and retraction), and #406 (octahedral cell construction). It answers the diagonal no-go's immediate mathematical question without selecting a material law.

## Fixed ingredients and construction

Let \(C_k\) be the old tetrahedral chain groups of dimensions \((4,6,4,1)\), and let \(\widetilde C_k\) be the 12-cell refinement's groups of dimensions \((11,30,32,12)\). Keep the *same geometric subdivision* \(S_k:C_k\to\widetilde C_k\) and the rational, \(S_4\)-equivariant chain retraction \(D_k:\widetilde C_k\to C_k\) from PR #407. Thus

\[
D_kS_k=I,\quad \widetilde B_k S_k=S_{k-1}B_k,\quad
D_{k-1}\widetilde B_k=B_kD_k. \tag{1}
\]

Set \(P_k=S_kD_k\), \(N_k=I-P_k\), and choose the grade-wise metric

\[
\boxed{H_k=D_k^{\mathsf T}D_k+N_k^{\mathsf T}N_k.}\tag{2}
\]

This is an existence witness, not a parameter inferred from graphite. It is generally *off-diagonal* in the fine simplex basis. It is positive definite: \(y^{\mathsf T}H_ky=\|D_ky\|^2+\|N_ky\|^2\); if both terms vanish, \(y=S_kD_ky+N_ky=0\). Equivariance of \(S,D\) and the signed-permutation, Euclidean-orthogonal group actions imply \(S_4\)-invariance. Moreover \(H_kS_k=D_k^{\mathsf T}\), \(S_k^{\mathsf T}H_kS_k=I\), and \(P_k\) is \(H_k\)-orthogonal. Other positive scales on the complement are possible, so Eq. (2) is not uniquely selected.

## Exact dynamical intertwining

Use the metric-skew incidence generator with down block \(\widetilde B_k\) and up block \(-H_k^{-1}\widetilde B_k^{\mathsf T}H_{k-1}\). The old generator has down block \(B_k\) and up block \(-B_k^{\mathsf T}\), with unit coarse metric. Eq. (1) gives the down intertwiner. For the up block,

\[
\begin{aligned}
\widetilde B_k^{\mathsf T}H_{k-1}S_{k-1}
&=\widetilde B_k^{\mathsf T}D_{k-1}^{\mathsf T}\\
&=(D_{k-1}\widetilde B_k)^{\mathsf T}\\
&=D_k^{\mathsf T}B_k^{\mathsf T}\\
&=H_kS_kB_k^{\mathsf T}.
\end{aligned}\tag{3}
\]

Since \(H_k\) is invertible, \(A_HS=SA_{\rm seed}\) exactly. The 15 seed modes are invariant; the \(H\)-orthogonal complement is invariant too because \(A_H\) is metric-skew. The seed characteristic polynomial \(\lambda(\lambda^2+4)^7\) is inherited on \(\operatorname{im}S\), **not asserted for all 85 refined coordinates**. Geometric coarse-to-fine leakage is exactly zero for this constructed metric. Its finite closed dynamics conserves the \(H\)-norm; the construction yields no positive damping or friction.

## Measured cost of the witness

Exact rational reconstruction and all 24 inherited \(S_4\) actions check Eqs. (1)–(3). Every down/up block residual has zero nonzero entries. The metric's off-diagonal support (one triangle of each symmetric grade block) is:

| Grade | Dimension | Nonzero off-diagonal entries | Possible pairs |
|:--:|--:|--:|--:|
| 0 | 11 | 34 | 55 |
| 1 | 30 | 243 | 435 |
| 2 | 32 | 340 | 496 |
| 3 | 12 | 38 | 66 |

Thus rescuing exact tetrahedral motion under the **fixed** subdivision requires correlations beyond positive diagonal simplex weights. This witness was reverse-engineered from a retraction and couples many simplex coordinates; the counts do not establish a microscopic range, energy, or contact mechanism. The infinitely many choices of complement metric further block a numerical material prediction.

## Graphite and next gate

The observed complementary angle pair is already accounted for by the conventional hexagonal symmetry and moiré baseline. Eq. (2) adds no twist-angle dependence and predicts neither a residual friction coefficient nor a load slope. To turn this into a UD graphite hypothesis, independently derive a physical coupling kernel and bath/contact response, project it to the same fine-chain basis, then compare its residual load and angle dependence against the conventional model on held-out measurements. A metric fitted to preserve the seed modes cannot count as an independent prediction. The coefficient ledger v0.39(2) and CRL-2 subdivision proposal do not promote this construction. Physical promotion remains 0.

## Reproduce

Run `python3 verify_correlated_metric.py` in this capture. `RESULTS.json` reports exact zero residuals and support. The verifier carries forward the geometric and equivariant constructors of the parent capture, then evaluates Eq. (2) with rational arithmetic. No material data or image was used.
