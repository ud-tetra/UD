# C06 support of an exact incidence cut v0.31

**EXACT / CONDITIONAL** for fixed-coordinate single-simplex row support. **CANDIDATE** for the event-triggered pair-copy port. **OPEN** for native event authority and persistence. **Physical Promotion = 0.**

## Scope correction to the v0.30 intake summary

Use edge order 01,02,03,12,13,23 and signed vertex-edge boundary \(B_1 e_{ij}=v_j-v_i\). The v0.30 blind witness \(w=(1,1,0,0,-1,-1)\) is the exact gradient \(B_1^\mathsf{T}(0,1,1,0)\). Its divergence is \(B_1w=(-2,2,2,-2)\). Thus the intake's assertion that it is a cycle is false. Its zero signed face circulation follows from \(B_2^\mathsf{T}B_1^\mathsf{T}=0\). The v0.30 rank and blindness results stand. The signing replay classifies fixed coordinate embeddings only and makes no claim about \(A_4\) compatibility.

## Row-support obstruction

Let \(X=\mathbf{1}^{\perp}\subset\mathbb{R}^6= \mathbb{R}\mathbf{1}\oplus E\oplus T_2\) with ordinary edge coordinates and the Euclidean carrier metric. Write \(\bar e\) for the edge opposite \(e\). For each linear output row \(r\) of a post-event map \(K\), the condition \(KT_2=0\) is exactly \(r_e=r_{\bar e}\) on all three pairs, by testing \(e_e-e_{\bar e}\) as an input. The support of each row must therefore be a union of complete opposite pairs. This characterization is pointwise for any post-event linear operator chosen as a function of state or event data.

A triangular face and a vertex star each contain one edge from each opposite pair. If every output row of \(K\) is confined to either kind of support, \(KT_2=0\) forces \(K=0\) and removes all even exchange. This rules out every \(K=B_1+\Delta B_1\) retaining the original endpoint support in each column, even with arbitrary signed coefficients. It also rules out arbitrary face-local reassignment of each Whitney flag output within the original face. The theorem allows coordination in choosing the coefficients. It concerns their input supports, so it also applies if the choice is instantaneous and shared. Routing from multiple simplices into the same output can change the support and lies outside the obstruction.

There is an additional obstruction specific to the signed boundary port under the fixed embedding. The images of \(e_{01}-e_{23}\) and \(e_{02}-e_{13}\) under \(B_1\) coincide, and the image of \(e_{03}-e_{12}\) is independent of them. Hence the original \(B_1|_{T_2}\) has rank two and cannot serve as a rank-three pre-event port in these coordinates.

## Smallest support for a selective flag cut

Use the v0.20 flag-copy port \(G\) with \((Gx)_{f,e}=x_e\). On \(X\) the unique target map killing \(T_2\) and agreeing with \(G\) on \(E\) is \(K=G(I_X-P_-)\). The exact row is \((Kx)_{f,e}=(x_e+x_{\bar e})/2\). Every ambient row inducing this same functional on \(X\) differs by a multiple of \(\mathbf{1}^\mathsf{T}\). Its possible support sizes are 2, 4, and 6, with the two-edge row unique. Thus one opposite edge per flag is sufficient and minimal in these fixed coordinates. The twelve-flag output is retained. The v0.23 unsigned face aggregation implements the same operator, with cancellation furnishing the opposite-edge weights.

Assume the v0.20 flag metric and its orthogonal record ranges, injective \(G\) on \(T_2\), positive odd stock, and an incoming aligned common odd phase with empty odd record. At the first \(B=0\) with \(dB(F_{\rm in})>0\), a declared persistent mode change to \(K\), with identity amplitude reset and reverse map \(K^\dagger\), removes exactly three forward coupling directions and freezes both odd registers. The even map and its reverse on the even record range are unchanged. The derivative of total quadratic stock vanishes on both sides by adjoint reciprocity. The trajectory stays continuous and odd stock stays fixed for the duration of the declared mode. Keeping the original mode at the same event also satisfies fixed incidence and stock conservation. A source rule selecting and persisting the new mode remains open, as do Stage 2 and deficit allocation.

## Verification

Run the adjacent Python replay. It checks the signed gradient witness, exact ranks, row support possibilities and all 64 support masks, including every single-face and vertex-star support.
