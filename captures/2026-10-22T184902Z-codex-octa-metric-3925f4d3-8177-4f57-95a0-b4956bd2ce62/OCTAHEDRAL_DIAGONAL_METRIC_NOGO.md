# Positive diagonal Hodge weights cannot remove vertex leakage from the midpoint-octahedron refinement

22 October 2026. **Exact conditional finite-chain no-go. Development; no independent review; physical promotion 0.** This capture extends draft PR #407, itself stacked on the centered-octahedron construction in draft PR #406. It tests a specific, common class of local material metrics; it does not claim a no-go for every positive operator or every UD carrier.

## Claim and scope

For the *fixed geometric subdivision* \(S:C_\bullet(\Delta^3)\to C_\bullet(\widetilde\Delta^3)\) in PR #407 and **any strictly positive diagonal simplex inner products** \(H_0,H_1,H_2,H_3\), the old vertex subspace cannot be invariant under the weighted, metric-skew incidence generator with nonzero \(0\leftrightarrow1\) coupling. This failure occurs on one subdivided old edge before any choice of face/cell weights matters. For an inherited \(S_4\)-symmetric diagonal metric, precisely **one half of the instantaneous squared generator action** of each normalized old vertex leaves the geometrically embedded coarse subspace. This is reversible amplitude mixing, not a friction coefficient or entropy production.

## 1. Weighted operator and geometric coarse subspace

Use the complete 12-cell midpoint/centroid refinement: four old tetrahedral vertices, six old-edge midpoints, one centroid, thirty fine edges, thirty-two faces and twelve 3-cells. Let \(\widetilde B_1\) map oriented fine edges to vertices and let each \(H_k\) be diagonal with strictly positive entries. On adjacent chain grades, define the metric-skew generator with blocks

\[
(A_H)_{k-1,k}=\widetilde B_k,\qquad
(A_H)_{k,k-1}=-H_k^{-1}\widetilde B_k^{\mathsf T}H_{k-1}.\tag{1}
\]

It obeys \(A_H^{\mathsf T}H+HA_H=0\), where \(H=\operatorname{diag}(H_0,H_1,H_2,H_3)\), so the finite weighted norm is conserved. The fixed subdivision \(S_0\) embeds each old vertex as itself, and \(S_1\) sends an old oriented edge \(i\!\to\!j\) to its two oriented halves \(i\!\to\!m_{ij}\!\to\!j\). The chain identity \(\widetilde B_kS_k=S_{k-1}B_k\) still holds regardless of \(H\). Invariance also requires the weighted *adjoint* to preserve the image of \(S\); chain identity alone does not supply this.

## 2. One-edge proof for every positive diagonal metric

Take an old vertex \(i\) incident to old edge \(\{i,j\}\). Its normalized coordinate state is \(v_i=e_i/\sqrt{a_i}\), where \(a_i=(H_0)_{ii}>0\). Write \(m=m_{ij}\), \(b_{ij,i}>0\) for the weight of the near half-edge \(im\), and \(b_{ij,j}>0\) for the far half-edge \(mj\). Apart from orientation signs, Eq. (1) produces the edge amplitudes

\[
\left. (A_Hv_i)_{C_1}\right|_{(im,mj)}
=\left(\frac{\sqrt{a_i}}{b_{ij,i}},\;0\right).\tag{2}
\]

Every vector in the *fixed* old-edge image of \(S_1\) has equal-magnitude oriented coefficients on its two halves, \((t,t)\). The far component in Eq. (2) forces \(t=0\), contradicting its nonzero near component. Different old-edge images have disjoint supports, so a combination of them cannot repair the mismatch. Since \(b_{ij,i}\) is finite and positive, Eq. (2) proves \(A_H\operatorname{im}S\not\subseteq\operatorname{im}S\) for **all** positive diagonal \(H\). The negative sign of the adjoint block has no effect on the argument.

This result does **not** exclude an off-diagonal positive metric, a different or nonlocal embedding, a revised incidence/contact rule, or the degenerate choice of zero vertex-edge coupling. Any of those requires its own selector and audit.

## 3. Exact leakage formula and robust lower bound

In the weighted edge norm the best approximation of Eq. (2) in its old-edge image has coefficient \(t=\sqrt{a_i}/(b_{ij,i}+b_{ij,j})\) (up to orientation). Its squared orthogonal residual is

\[
\ell_{ij\mid i}^2
=\frac{a_i b_{ij,j}}
       {b_{ij,i}(b_{ij,i}+b_{ij,j})}.\tag{3}
\]

Summing the three incident edges gives the exact normalized vertex leakage and full squared action,

\[
\ell_i^2=\sum_{j\ne i}
 \frac{a_i b_{ij,j}}
 {b_{ij,i}(b_{ij,i}+b_{ij,j})},\qquad
\|A_Hv_i\|_H^2=\sum_{j\ne i}\frac{a_i}{b_{ij,i}}.\tag{4}
\]

If the within-edge weight contrast satisfies \(\max(b_{ij,i}/b_{ij,j},b_{ij,j}/b_{ij,i})\leq\kappa\) for every original edge, then Eq. (4), as a positive weighted average, yields

\[
\boxed{\frac{\ell_i^2}{\|A_Hv_i\|_H^2}
\geq\frac{1}{1+\kappa}>0.}\tag{5}
\]

For the regular tetrahedron and any **inherited \(S_4\)-invariant diagonal metric**, all twelve vertex-to-midpoint half-edges form one symmetry orbit and have common weight \(b\); the four old vertices have common weight \(a\). Thus \(\kappa=1\) and equality holds:

\[
\ell_i^2=\frac{3a}{2b},\qquad
\|A_Hv_i\|_H^2=\frac{3a}{b},\qquad
\frac{\ell_i^2}{\|A_Hv_i\|_H^2}=\frac12.\tag{6}
\]

The half is a dimensionless geometric ratio for initial **vertex** states. It is not the PR #407 all-grade Frobenius ratio \(11/31\): that earlier number averages squared action across the entire 15-dimensional embedded seed for the unit metric. Scaling \(b\) can make the absolute frequency and \(\ell_i^2\) arbitrarily small, but it scales the total vertex action too and leaves the \(1/2\) ratio intact. Without independently selected \(a/b\) and a physical clock, Eq. (6) gives no rate in seconds or dissipated power.

## 4. Exact checks and next physical gate

The bundled standard-library verifier reconstructs all 30 fine edges from the 12 tetrahedra, the six two-half-edge subdivision columns and the fine vertex incidence matrix. It evaluates the weighted orthogonal residual with rational arithmetic, independently comparing it with Eqs. (3)–(4). Controls include the unit metric (\(\ell_i^2=3/2\), ratio \(1/2\)), a different \(S_4\)-symmetric positive metric (\(a=2,b=3\), ratio \(1/2\)), and anisotropic positive rational weights satisfying the bounded-contrast inequality. These controls test the formula; the universal statement follows from the support proof in §2, not a finite parameter sweep.

For the original graphite goal, the next admissible branch must specify a physically justified off-diagonal metric or altered embedding/contact and then compare its held-out prediction with the conventional honeycomb and moiré baseline. Alternatively this is evidence that the octahedral refinement is a bookkeeping geometry while material motion lives in a different carrier. In either case, a finite metric-skew generator remains reversible; a material friction law requires an independently sourced open-system bath and time normalization. The coefficient ledger v0.39(2) keeps those bridges open, and the supplied CRL-2 subdivision is a governance proposal. Constructor verification is not independent review. **Physical promotion stays 0.**

## Reproduction

Run `python verify_diagonal_metric_nogo.py`. `RESULTS.json` contains the rational controls, exact formulas, contrast bound, and claim scope. Parent capture: `2026-10-22T184127Z-codex-octa-coarse-3ddfe996-c702-4694-9e18-0b84add389f1`. No unavailable image, archived research script, material dataset or fitted coefficient was used.
