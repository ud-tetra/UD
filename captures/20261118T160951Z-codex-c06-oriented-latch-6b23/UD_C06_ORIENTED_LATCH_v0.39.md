# C06 oriented incidence and zero-donor latch v0.39

**EXACT / CONDITIONAL** for the shared-face sign, representation and endpoint tests. **CANDIDATE** for an oriented coefficient lift and capture-side latch. **OPEN** for source-defined lift and actuation. **Physical Promotion = 0.**

## Source-defined sign and carrier scope

In Ledger v0.39 Q169, Q171 and Q173, \(B_3\) is the signed face-to-cell incidence in the skew \(C_2\leftrightarrow C_3\) dynamics. Here \(B_3:C_3\to C_2\); the face-to-cell part is \(B_3^\mathsf T\). Give the two tetrahedra compatible orientations across their shared face \(f\). Then their \(B_3\) entries at \(f\) have opposite signs. Taking the positive cell first, the normalized row of \(B_3^\mathsf T\) from this face injects a scalar as \((1,-1)/\sqrt2\). This is a genuine instance of signed incidence in coherent coordinates. Reorienting a cell changes its coordinate convention and all its incident maps together.

Its source and target are scalar face and cell amplitudes. For fixed scalar incidence one face provides rank one into the cell pair. It does not implement a rank-three map into the two \(C_1\) gradient copies of C06 v0.38. An auxiliary \(W\)-valued seam and two compatible identifications by \(L:W=T_2\to\operatorname{im}B_1^\mathsf T\) would lift the signed pair to \(Jw=(Lw,-Lw)/\sqrt2\). This reproduces the needed model map, conditional on adding those registers, couplings and identification maps. A basis flip on one destination alone cannot replace an incidence coupling whose relative sign differs from that of the shared vertex block: simultaneous basis changes preserve the image–kernel relation.

An ordinary tetrahedral relabeling cannot act as \(-I\) on all of \(W\simeq\mathbf1_4^\perp\). Its trace is the number of fixed vertices minus one, hence at least \(-1\), while \(\operatorname{tr}(-I_3)=-3\). Also \(S_4\) has no outer automorphism: an automorphism preserves transpositions, which are the size-six conjugacy class of involutions, and permutes their four vertex stars. These stars are characterized among triples of pairwise noncommuting transpositions by generating \(S_4\), with triangular triples generating \(S_3\). After composing with a vertex relabeling to fix each star, the automorphism fixes every transposition by star intersection, so it is the identity. This does not rule out a distinct representation with an explicit orientation sign, or a term that is odd under swap of the copies.

## Directed zero-donor completion test

Under the v0.38 loader use \(s\in W\) for the donor and \(d=J^\mathsf T y\in W\) for the antisymmetric archive coordinate. Assume \(s(0)=s_0\ne0,\ d(0)=0\), \(g(t)>0\) until the first completion, and enough accumulated angle to reach \(\pi/2\). The equations are \(\dot s=-g d,\ \dot d=g s\); \(N=\|s\|^2+\|d\|^2\) is conserved. Let \(r=\|s\|^2/N,\ c=\langle s,d\rangle/N\). Then
\[
r=\cos^2\theta,\qquad c=\tfrac12\sin(2\theta),\qquad
\dot c=g(2r-1),\qquad \dot r=-2gc .
\]
The donor stock has a tangential zero at the first quarter turn, while \(c=0\) there with incoming slope \(-g<0\). An armed first downward zero of \(c\), requiring \(r<1/2\), singles out the desired crossing in this aligned model. At the initial zero, \(r=1\) and \(\dot c>0\). Continued unlatched flow returns to downward zeros at later odd quarter turns, so persistence and first-event selection are separate requirements. With unaligned initial data, \(c=0\) and \(r<1/2\) alone do not imply zero donor. The normalized Gram determinant \(\Delta=r(1-r)-c^2\) is invariant under the two-register rotation. At a downward zero the residue is \((1-\sqrt{1-4\Delta})/2\). For \(s=(1,0,0),d=(0,2,0)\), this is \(1/5\), even though the directed correlation guard passes. Thus an initial alignment certificate is essential if the guard is used to certify full transfer.

Declare a one-shot identity reset at this crossing that sets the loader and its adjoint to zero. The shared vertex generator remains live, and the archive remains in its kernel. Stage 2 reads \(N/2\). If an imperfect crossing has \(|c|\le\varepsilon\) on the aligned \(r\le1/2\) branch, the donor residue satisfies \(r(1-r)=c^2\), hence \(r\le2\varepsilon^2\). This compares a tangential stock detector with a transversal correlation observable, without importing a clock. Absolute normalization of \(c\) is unnecessary for its zero, but sourcing the paired inner product and authority to latch the loader remains open. Q173's scalar face gate is a different state and does not establish this event.

## Intake scope and replay

At the exact endpoint an active loader immediately regenerates donor amplitude for positive rate, while donor stock grows at second order in the elapsed angle. In the shared block the antisymmetric payload contributes zero vertex divergence. Other live symmetric or vertex amplitudes retain their own evolution. In a copy-symmetric equation with identical self-action \(A(t)\), the difference evolves homogeneously via \(A(t)\); only the common forcing cancels.

The adjacent replay checks signed gluing under coherent orientation choices, all tetrahedral relabeling traces, rational aligned phase curves and an unaligned false-positive guard.
