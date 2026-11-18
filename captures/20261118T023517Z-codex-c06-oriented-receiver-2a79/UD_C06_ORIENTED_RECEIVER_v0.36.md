# C06 signed gradient receiver and archive readout v0.36

**EXACT / CONDITIONAL** for the regular \(K_4\) with Euclidean vertex and edge coordinates. **CANDIDATE** for an isolated archive and half-stock readback. **OPEN** for a native transfer and isolation law. **Physical Promotion = 0.**

## Correct the v0.35 intake

Use ordinary unsigned edge relabeling on the polarized input \(W=T_2\), and signed relabeling on oriented chains. The \(V_4\) action on \(W\) flips zero or two of the three pair-difference coordinates. An axis vector can meet its antipode in the orbit. A vector with three nonzero coordinates cannot, since the product of the coordinates is unchanged. The matching-register obstruction needs only an orbit collision, which occurs for every nonzero input and was proved in v0.35.

## The signed gradient is a faithful receiver

Let \(A:\mathbb R^6_{\rm ordinary}\to\mathbb R^4\) be unsigned endpoint incidence, and \(B_1:\mathbb R^6_{\rm signed}\to\mathbb R^4\) oriented endpoint incidence with columns \(v_j-v_i\) for \(i<j\). Write \(V_0=\mathbf1_4^\perp\). Both maps intertwine their respective edge actions with vertex relabeling. One has \(A A^\mathsf{T}=2I_4+J_4\) and \(B_1 B_1^\mathsf{T}=4I_4-J_4\), with \(J_4\) the all-ones matrix. The image of \(A^\mathsf{T}|_{V_0}\) is precisely \(W\): opposite edge entries sum to zero, and the map has rank three.

The normalized map
\[
L=\frac{B_1^\mathsf{T}A}{2\sqrt2}\bigg|_{W}:W\longrightarrow \operatorname{im}B_1^\mathsf{T}
\]
is an \(S_4\)-equivariant isometry. The two factors \(A/\sqrt2\) and \(B_1^\mathsf{T}/2\) are isometries on \(W\) and \(V_0\), respectively. These normalizations follow from the incidence identities. This realizes the correct action on the signed gradient subspace using the incidence audited in v0.31. The signed cycle space gives a different result.

To see the cycle action, identify signed edges with \(\bigwedge^2\mathbb R^4\). The gradient component is \(\mathbf1_4\wedge V_0\), and the cycle component is \(\bigwedge^2 V_0\simeq V_0\otimes\mathrm{sgn}\) by the orientation-dependent Hodge isomorphism on \(V_0\). The action on \(V_0\) is irreducible: differences of a nonconstant vector and a transposition of it generate a vertex contrast, whose orbit spans \(V_0\). A transposition has trace \(+1\) on \(W\simeq V_0\) and \(-1\) on the cycle space, so there is no nonzero linear equivariant map from \(W\) into that space. Even a nonlinear norm-preserving equivariant injection fails: the unit circle in the transposition-fixed plane of \(W\) would have to map to the two unit points in the cycle fixed line. This argument uses full \(S_4\) and does not rule out a reduced orientation-preserving model.

## Stock transfer and readback

For an aligned held pair \((a,a)\in W\oplus W\), an isolated gradient receiver holding \(h=L(\sqrt2a)\) preserves all old stock and recovers each half as \(L^\dagger h/\sqrt2\). In the v0.34 orthogonal handoff, identify its archive coordinate with the gradient copy through \(L\). A separate fresh epoch still needs donor stock if the old stock is fully retained. If the donor is absent, the candidate can archive without restarting or consider a different operation consuming old stock. Stage 2 continues to transfer only retained even stock.

If this archive replaces the old direct odd register in the Stage 2 record observable, the preserved direct odd contribution is \(\|h\|^2/2\). Including the full archive norm would double that contribution. This half weight is fixed by the readback, with no empirical normalization. The active Hodge chain does not by itself provide an isolated bank: \(B_1Lw=\sqrt2Aw\ne0\) for \(w\ne0\), while \(B_2^\mathsf{T}Lw=0\) by boundary nilpotency. A nonzero vertex-edge coupling therefore moves a bare gradient state out of its edge block. The incidence proves availability of the representation and its readback. A native reserved receiver, stock-moving event and persistent isolation remain open.

## Verification

The adjacent replay checks the integer numerator of \(L\) against all 24 relabelings on 27 odd preparations. It checks norm and archive readback, triangular circulation, active vertex coupling, and the transposition trace split. The proof extends beyond the bounded replay.
