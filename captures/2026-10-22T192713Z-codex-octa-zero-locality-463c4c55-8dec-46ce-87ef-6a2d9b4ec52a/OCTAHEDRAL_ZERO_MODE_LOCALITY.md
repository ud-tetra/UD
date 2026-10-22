# Zero-mode obstruction to one-hop octahedral vertex metrics

22 October 2026. **EXACT conditional locality no-go and sharp residual bound; constructor verified; physical promotion 0.** This result extends draft PR #409. It tests the *fixed* geometric embedding of the four old tetrahedral vertices into the 11-vertex, 30-edge midpoint/centroid refinement and the weighted incidence generator. It does not derive a graphite material Hessian.

## Theorem: exact seed dynamics requires a two-hop vertex coupling

Let \(S_0:\mathbb R^4\to\mathbb R^{11}\) insert the four original vertices. Write \(u=(1,1,1,1)^\mathsf T\). The seed incidence has \(B_1^{\mathsf T}u=0\), so the seed skew generator annihilates the grade-zero state \(u\). Let \(H_0,H_1\) be arbitrary symmetric positive definite vertex/edge metrics. The fine generator's vertex-to-edge block is \(-H_1^{-1}\widetilde B_1^{\mathsf T}H_0\).

If exact dynamical intertwining \(A_H S=S A_{\rm seed}\) holds, then

\[
\widetilde B_1^{\mathsf T}H_0S_0u=0.\tag{1}
\]

The 30-edge fine graph is connected. Its incidence transpose has only constant vertex vectors in its kernel, so \(H_0S_0u=c\mathbf 1_{11}\). Since \(H_0\) is positive definite,
\(4c=(S_0u)^{\mathsf T}H_0(S_0u)>0\). At the centroid \(o\), Eq. (1) therefore requires

\[
\boxed{\sum_{i=1}^4(H_0)_{o,v_i}=c>0.}\tag{2}
\]

The centroid is not adjacent to any old vertex; its shortest graph path to each old vertex uses a midpoint and has length **two**. Hence **no positive vertex metric supported only on the diagonal and one-hop edges of the fine graph** can preserve the seed zero mode. This obstruction is independent of face/cell weights, \(S_4\) symmetry, and the choice of \(H_1\), provided \(H_1\) is invertible.

Under the additional normalization \(S_0^{\mathsf T}H_0S_0=I_4\), \(c=1\). If \(H_0\) is inherited \(S_4\)-invariant, all four entries in Eq. (2) are equal, forcing

\[
(H_0)_{o,v_i}=1/4\quad(i=1,\ldots,4).\tag{3}
\]

This is a **necessary algebraic coupling in this normalized model**, not a measured force constant or a uniquely selected metric.

## Sharp one-hop residual

Assume the unit coarse pullback \(S_0^{\mathsf T}H_0S_0=I_4\) and no centroid-to-old entries. For \(z=H_0S_0u\), the four old vertex values equal 1 and the centroid value equals 0; the six midpoint values \(m_a\) are arbitrary. The fine graph consists of twelve old-to-midpoint edges, six centroid-to-midpoint edges, and twelve octahedral midpoint-to-midpoint edges. Therefore

\[
\begin{aligned}
\|\widetilde B_1^{\mathsf T}z\|_2^2
&=\sum_{a=1}^6\left[2(1-m_a)^2+m_a^2\right]
  +\sum_{\{a,b\}\in E_{\rm oct}}(m_a-m_b)^2\\
&=4+3\sum_{a=1}^6(m_a-2/3)^2
  +\sum_{\{a,b\}\in E_{\rm oct}}(m_a-m_b)^2
\geq\boxed{4}.\tag{4}
\end{aligned}
\]

Equality is achieved by \(m_a=2/3\) for all six midpoints. It is compatible with a positive, \(S_4\)-invariant one-hop metric: take unit diagonal on old vertices and centroid, diagonal 10 on midpoints, and value \(1/3\) on every old-to-incident-midpoint pair, with all other off-diagonals zero. The quadratic form is \(\sum_{\rm old-mid}(x_{\rm old}+x_{\rm mid})^2/3+(10-2/3)\sum_{\rm mid}x_{\rm mid}^2+x_o^2>0\) for nonzero \(x\), and it attains Eq. (4). Thus 4 is a sharp lower bound in the stated class, not a numerical fit.

For the normalized seed mode \(u/2\), the *incidence covector* squared residual is at least 1. If in addition \(H_1\preceq M I\) with \(M>0\), its instantaneous weighted dynamic action obeys

\[
\|A_H S_0(u/2)\|_{H_1}^2
=\tfrac14(\widetilde B_1^{\mathsf T}z)^{\mathsf T}
H_1^{-1}(\widetilde B_1^{\mathsf T}z)
\geq 1/M.\tag{5}
\]

The scale bound on \(H_1\) must be independently sourced before Eq. (5) has physical units. The result is an *instantaneous reversible mode-mixing* bound, not a decay rate, friction coefficient, or load slope.

## Relation to the correlated witness and graphite

Draft PR #409 gives a complete all-grade positive metric with exact seed intertwining. Its centroid-to-old entries equal \(1/4\), meeting Eq. (3). This theorem explains one minimal nonlocal ingredient of that witness; it does **not** show that a two-hop restriction suffices for all 85 coordinates, nor that the witness is a microscopic material Hessian. The diagonal no-go in #408 is a special case of the qualitative zero-mode obstruction, but its \(1/2\) vertex leakage fraction concerns a different state and metric class.

The 21.8°/38.2° graphite pair has a conventional hexagonal/moiré account. This finite zero-mode constraint has no twist-angle or load variable, so it cannot explain a residual friction signal. The next material gate is an independently justified interfacial Hessian or response kernel, with explicit spatial mapping and bath/contact terms, tested against held-out residuals. The coefficient ledger v0.39(2) and proposed CRL-2 scheme leave this at construction level. Physical promotion stays 0.

## Reproduction

`python3 verify_zero_mode_locality.py` reconstructs the 30-edge graph, checks centroid-old graph distance two, the sharp rational minimum, an attaining SPD local vertex metric, and a two-hop grade-zero witness. `RESULTS.json` records the exact claims. The universal no-go and Eq. (5) follow algebraically above; the verifier is constructor validation, not independent review.
