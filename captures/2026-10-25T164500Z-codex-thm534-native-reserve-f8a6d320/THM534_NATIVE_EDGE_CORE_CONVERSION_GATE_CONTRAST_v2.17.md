# THM-534 v2.17: native edge–core conversion and face-gate contrast

Development — no registry entry. Exact conditional transfer on the original full tetrahedral carrier. Supplied mathematical permissions and preparation; native gate readiness remains open. Constructor checked; independent review pending. Physical promotion 0.

## 1. Source and purpose

The v2.16 receipt audit requires a concrete support donor and exchange contacts before calling a circulation diagnostic a consumed resource. The original tetrahedron already contains lower-grade coordinates and edge–face–core contacts. This note tests that native donor rather than adding a reserve amplitude or cotangent register. The result is conditional: uniform face permission blocks edge-to-core conversion by the chain identity, while nonuniform supplied face permission can open it.

Retain the full 15-dimensional real carrier of one filled tetrahedron, the unit metric, original signed boundaries and Q169 global skew Hodge–Dirac structure. Q170 supplies support on any declared control volume; Q171–Q173 supply core/face continuity and whole-face gating. Q177–Q179 ownership is unchanged. All proper simplices belong to the single cell, so the full owned-cell stock is the total norm. No frozen particle operator is revised. The active controlled generator differs from the all-open operator only by the supplied Q173 face mask.

Interpreting the edge-grade control volume as an available support donor is an explicit semantic choice. It does not identify this stock with physical energy or a consumable event cost. Q153/Q156/G05 still leave predictive source, gate-readiness, cost and renewal laws open. The supplied CRL-2 subdivision remains a governance proposal.

## 2. Full native controlled generator

Order vertices, edges, faces and the core by increasing simplex dimension, lexicographically within each grade. Let

\[
B_1\in\mathbb R^{4\times6},\quad B_2\in\mathbb R^{6\times4},
\quad b=B_3\in\mathbb R^4,
\]

with the ascending orientation convention. The exact tetrahedral identities are

\[
B_1B_2=0,\quad B_2b=0,\quad b^{\mathsf T}b=4,
\quad B_2^{\mathsf T}B_2=4I-bb^{\mathsf T}.
\tag{1}
\]

For a supplied binary face mask \(h\in\{0,1\}^4\), put \(D_h=\operatorname{diag}(h)\), \(w=D_hb\). On \(x=(v,e,f,c)\), define the original hard-gated native generator

\[
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-w\\
0&0&w^{\mathsf T}&0
\end{pmatrix},\qquad A_h^{\mathsf T}=-A_h.
\tag{2}
\]

Every edge–face incidence is retained. No lower-grade contact is artificially isolated. Face–core permissions act at the whole-face level, as Q173 requires. Binary masks are mathematical inputs; realizability under a future geometric readiness law is not assumed for all 16 controls.

The original boundaries still satisfy (1). The controlled block \(D_hb\) is not being declared a replacement chain boundary. Its failure to satisfy \(B_2D_hb=0\) under a nonuniform mask is a property of the controlled dynamics, not a violation of the original chain complex.

## 3. Uniform-gate obstruction and a native conversion signal

**Theorem N1 (uniform permission blocks lower-grade conversion).** With \(D_h=\lambda I\), \(\lambda\in\{0,1\}\), and initially \(f=c=0\), the core remains zero under the continuous native evolution. The same edge-only input produces zero core output in every finite Cayley event of \(A_h\).

**Proof.** Let \(y=b^{\mathsf T}f\). The continuous equations give \(\dot y=-4\lambda c\), \(\dot c=\lambda y\), because \(B_2b=0\). Both start at zero and remain zero. This invariant linear subspace is also preserved by the Cayley rational map, since its defining resolvent is invertible and restricts to the same subspace. \(\square\)

For arbitrary supplied masks, define

\[
u_h=B_2D_hb,\qquad
\gamma_h(e)=u_h^{\mathsf T}e.
\tag{3}
\]

Starting with \((v,e,f,c)=(0,e_0,0,0)\), one has

\[
\dot c(0)=0,\qquad \ddot c(0)=\gamma_h(e_0).
\tag{4}
\]

This is a prospective conversion signal using existing fields and supplied permissions, not an instantaneous nonzero-current requirement. All incidence currents can vanish at the initial state while \(A_hx\ne0\).

**Theorem N2 (gate-contrast strength).** Write \(k=\sum_fh_f\). Then

\[
\boxed{q_h:=\|u_h\|^2=k(4-k)
=\sum_{f<g}(h_f-h_g)^2.}
\tag{5}
\]

Exactly the two uniform masks have zero conversion stencil; the other 14 have a nonzero stencil. This is operator capability, not a guarantee for every reserve preparation: conversion also needs \(\gamma_h(e_0)\ne0\).

**Proof.** Since \(\|D_hb\|^2=k\) and \(b^{\mathsf T}D_hb=k\), (1) gives \(q_h=4k-k^2\). Expanding the pairwise difference sum for four binary entries gives the same expression. Each face pair in one tetrahedron shares an edge; (5) therefore measures face-permission contrast across that local face graph. \(\square\)

For the continuous evolution, parity of the grade couplings gives \(c(t)=\gamma_h(e_0)t^2/2+O(t^4)\). Consequently nonzero \(\gamma_h\) creates positive core stock to leading order \(\gamma_h^2t^4/4\), despite zero initial core stock and zero initial core current. This result does not choose the mask or an event duration.

## 4. Exact finite-event transfer from native edge support

Consider an edge-cycle preparation \(e_0\in\ker B_1\), with vertices, faces and core initially zero. Vertex amplitudes stay zero. For the native Cayley event

\[
x^+=\left(I-\frac t2A_h\right)^{-1}
\left(I+\frac t2A_h\right)x,
\tag{6}
\]

the event parameter \(t\) is supplied and dimensionless.

**Theorem N3 (exact core output).** For every real finite \(t\),

\[
\boxed{c^+(t)=
\frac{8\gamma_h(e_0)t^2}
{16+(16+4k)t^2+k^2t^4}.}
\tag{7}
\]

Thus every nonuniform mask admits an existing edge-cycle donor preparation that fills the core without adding a coordinate. No transfer is guaranteed when the preparation is orthogonal to \(u_h\).

**Proof.** The pair \(v=0\), \(B_1e=0\) is invariant because \(B_1B_2=0\). It is invariant under (6) as well. Eliminate the edge and core outputs from the Cayley midpoint equations:

\[
\left[I+\frac{t^2}{4}(B_2^{\mathsf T}B_2+ww^{\mathsf T})\right]f^+
=tB_2^{\mathsf T}e_0,
\qquad c^+=\frac t2w^{\mathsf T}f^+.
\tag{8}
\]

Decompose \(w=a+(k/4)b\), where \(a\perp b\), \(\|a\|^2=q_h/4\). The operator \(I+t^2B_2^{\mathsf T}B_2/4\) acts by \(1+t^2\) on \(b^\perp\) and by one on \(b\). Solving its single rank-one update by \(ww^{\mathsf T}\) yields

\[
w^{\mathsf T}f^+=
\frac{t\gamma_h(e_0)}
{(1+t^2)(1+k^2t^2/16)+q_ht^2/16}.
\tag{9}
\]

Use \(q_h+k^2=4k\) and substitute into (8) to obtain (7). The denominator is strictly positive. Finally, \(e_0=u_h\) belongs to \(\operatorname{im}B_2\subset\ker B_1\) and has \(\gamma_h=q_h>0\) for each nonuniform mask. \(\square\)

At the declared model step \(t=1\), the matched preparation \(e_0=u_h\) has initial edge stock \(q_h\). The exact outputs are

| Open faces \(k\) | Initial edge stock \(q_h\) | Core amplitude \(c^+(1)\) |
|---|---:|---:|
| 1 | 3 | \(24/37\) |
| 2 | 4 | \(8/11\) |
| 3 | 3 | \(24/53\) |

These preparations do not have equal initial stock. The table is not an optimization ranking or a preferred-gate selection principle. Unit edge amplitudes and unit model step are not physical reserve or action units.

The conversion signal has a robust nonzero sector within the edge-cycle preparation space. At \(e_0=u_h\), a cycle-space perturbation \(\delta e\) satisfies

\[
\gamma_h(u_h+\delta e)\ge q_h-\sqrt{q_h}\|\delta e\|>0
\quad\text{if }\|\delta e\|<\sqrt{q_h}.
\tag{10}
\]

Equation (7) then gives nonzero core output for every fixed nonzero \(t\). This is robustness of transfer under fixed supplied permissions and restricted empty-face/core preparations. It is not a proof of a continuous global binary selector, nor robustness to erroneous mask bits.

## 5. Explicit donor and interface receipts

Declare the existing grade-one support control volume as donor stock \(R=\|e\|^2\), the face interface stock \(F=\|f\|^2\), and core stock \(C=c^2\). For the cycle-space sector the vertices remain zero, so native continuity gives

\[
\dot R=-\sum_{e,f}j^{12}_{ef},\quad
\dot F=\sum_{e,f}j^{12}_{ef}-\sum_fj^{23}_f,\quad
\dot C=\sum_fj^{23}_f,
\tag{11}
\]

\[
j^{12}_{ef}=2(B_2)_{ef}e_ef_f,
\qquad j^{23}_f=2h_fb_ff_fc,
\qquad R+F+C=\|e_0\|^2.
\tag{12}
\]

The same balances hold exactly for (6) when currents are replaced by native midpoint receipts \(J^{12}_{ef}=2t(B_2)_{ef}\bar e_e\bar f_f\), \(J^{23}_f=2th_fb_f\bar f_f\bar c\). Each unique coordinate's squared-amplitude change is checked, not merely the total norm. On a single tetrahedron the complete owned-cell stock remains constant.

This supplies explicit exchange contacts for a donor interpretation using only existing native coordinates. It is redistribution: no source term, consumed circulation cost or dissipative energy is identified. General preparations permit signed backflow. Calling \(R\) a resource does not assign an event debit equal to the v2.16 absolute receipt variation.

## 6. Renewal and selection remain distinct obligations

Reversing the supplied event parameter in (6) exactly restores the field. It also returns any support delivered to the face/core sector. That mathematical inverse is not a renewal cycle retaining an extracted output, deleting an outgoing record or paying an external event cost. Such a cycle needs specified output and replenishment contacts and complete support/record receipts.

The uniform-mask obstruction is an important limit: a lower-grade donor alone does not overcome chain orthogonality. A supplied nonuniform mask and a nonorthogonal preparation open a lawful channel, but no native rule choosing or restoring that mask has been derived. Choosing the largest \(q_h\), a particular conversion fraction or a unit step would add an objective or termination convention. Symmetry-related masks can still tie.

This is a one-tetrahedron construction. In a larger complex, shared-face Q173 stars couple every incident core. Extending it requires all cofaces and consistent unique-simplex ownership; a single local incidence must not be silently isolated. No bounded bulk selector, physical action/clock map or particle/quark/lepton identification follows.

The next source test is a complete support-and-record cycle that explicitly names what leaves the native subsystem, which incoming contacts replenish it, and what predictive gate condition opens and restores. The present donor balances constrain such a proposal without supplying it. Independent review remains pending.

## 7. Reproducibility

The fresh `verify_native_reserve.py` constructs the full original 15-coordinate tetrahedral incidence generator, verifies (1), all 16 supplied masks and the gate-contrast identity, 320 exact finite-event norm/coordinate/grade-receipt/inverse controls, 384 signed \(S_4\) generator-covariance controls, all 14 matched nonuniform preparations and four cycle-space perturbations. The two uniform masks are tested on nonzero edge-cycle inputs. Exact standard-library `Fraction` arithmetic is used throughout. No archived scripts are executed. These are constructor controls supplementing the proofs, not independent replication, physical preparation or empirical validation.
