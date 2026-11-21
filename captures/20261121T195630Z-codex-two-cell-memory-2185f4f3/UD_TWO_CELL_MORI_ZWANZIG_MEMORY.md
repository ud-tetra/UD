# Exact two-cell memory for overlapping tetrahedral averages

**Scope.** Finite chain model with the coefficient Euclidean metric and the specified Whitney sinks. **Physical Promotion = 0.**

## Carrier and projection

Use the unique-simplex carrier of \([0123]\cup[0124]\), with increasing orientations and \(A=\partial-\partial^\mathsf T\). It has \(5+9+7+2=23\) coordinates. Each cell average uses \(1/2\) on its four vertex coordinates and zero elsewhere. The two average vectors have inner product \(3/4\) because the cells share three vertices. Use the orthogonal projector onto their span, \(P=U(U^\mathsf T U)^{-1}U^\mathsf T\), where \(U\) has the two average vectors as columns. Put \(Q=I-P\). An orthonormal resolved basis consists of the vertex vectors
\[
 u_+=(2,2,2,1,1)^\mathsf T/\sqrt{14},
 \qquad u_-=(0,0,0,1,-1)^\mathsf T/\sqrt2 ,
\]
extended by zero on edges, faces and volumes. Pole exchange fixes \(u_+\) and negates \(u_-\).

Let \(R_F\) restrict to the three oriented edges of a triangle \(F\), and \(W=(6I-bb^\mathsf T)/9\), with \(b=(1,-1,1)^\mathsf T\) in increasing edge order. The internal two-sided sink is \(D_{\rm seam}=2R_{012}^\mathsf T W R_{012}\). For \(G=A-\gamma D_{\rm seam}\) with \(\gamma\ge0\), the resolved memory operator in the orthonormal two-channel basis is
\[
 {\cal K}(\tau)_{ij}=u_i^\mathsf T GQ\, e^{\tau QGQ}\,QG u_j .
\]

## Internal seam result

The permutations of the three shared vertices preserve \(A\), \(P\), and both resolved vectors. Their action on the three oriented seam edges has no invariant vector. A transposition reversing either endpoint pair fixes its edge as an unoriented simplex and negates its oriented basis vector. Therefore the unresolved modes reached by either resolved source have zero seam-edge trace. The sink vanishes on those modes regardless of \(\gamma\).

The exact Krylov calculation produces a two-dimensional even block with poles \(s=\pm i\sqrt{32/7}\) and a one-dimensional odd block with pole \(s=0\). The two channels do not mix. The Laplace transforms and time kernels are
\[
 \widehat{\cal K}_+(s)=-\frac{3}{7}\frac{s}{s^2+32/7},
 \quad \widehat{\cal K}_-(s)=-\frac3s,
 \qquad
 {\cal K}(\tau)=\operatorname{diag}\!\left[
   -\frac37\cos\!\left(\sqrt{32/7}\,\tau\right),-3\right].
\]
Thus the observable **memory decay rate is zero**. The odd component is constant and the even component oscillates. The projected equation remains nonlocal in time. Removing the initial unresolved forcing by preparing \(Qc(0)=0\) still leaves the convolution. The constant odd contribution is a property of the compressed unresolved dynamics and need not be a zero mode of the full generator.

## Exterior sink control

As a separate absorbed-boundary model, let \(D_\partial=\sum_{F\ne012}R_F^\mathsf T W R_F\), summing the six exterior faces. On the memory-active subspaces it damps the resolved-to-unresolved edge directions at \(4\gamma/3\). It vanishes on the remaining even coordinate. Adding the internal seam sink to this exterior control gives the same memory kernel because the active directions have zero seam trace.

Write \(d=4\gamma/3\), \(\omega=\sqrt{32/7}\). The exterior transforms are
\[
 \widehat{\cal K}_{\partial,+}(s)=-\frac37\frac{s}{s^2+ds+\omega^2},
 \qquad
 \widehat{\cal K}_{\partial,-}(s)=-\frac3{s+d}.
\]
The odd decay rate is \(d\). The even exponential rate is \(d/2\) for \(0<d\le2\omega\) and \((d-\sqrt{d^2-4\omega^2})/2\) for \(d>2\omega\). At critical damping the even kernel has a linear prefactor multiplying \(e^{-d\tau/2}\). For positive \(\gamma\), the slower even rate governs the full kernel. Increasing large \(d\) eventually slows even relaxation. A Markov approximation requires its own comparison with packet timescales and a closure error estimate. The positive rate here follows from the expressly supplied exterior absorption.

## Scope of the two-tier calculations

The piecewise-constant \(L^2\) interpolation in UD #588 is an isometry on the resolved amplitude coordinates. Its norm squared on arbitrary microscopic input is \(\|Pc\|^2\). Fast relaxation is one route to an approximate local closure. An invariant resolved subspace can give an exact local closure with identically zero memory. The two-cell result above concerns overlapping cell averages, for which the closed generator is coupled to the unresolved space.

Use one energy convention when matching the cubic coefficient. The complex vertex energy \(g_v|c_v|^4/2\) used by #588 gives the cell energy \(g_v|a|^4/8\) and then \(\Lambda_{\rm nl}=g_v h^3/4\). If one instead takes the input \(g_v|c_v|^4/4\) literally while keeping the same complex Hamiltonian derivative and continuum energy convention, the cell energy is \(g_v|a|^4/16\) and \(\Lambda_{\rm nl}=g_v h^3/8\). The uniform-mode overlap \(1/4\) is identical in both conventions.

The companion symbolic replay verifies the active Krylov subspaces, all four transfer functions, and the seam and exterior damping restrictions. It is constructor evidence.

- [UD #588, master equation architecture](https://github.com/ud-tetra/UD/pull/588)
- [Signed Whitney face mass, UD #528](https://github.com/ud-tetra/UD/pull/528)
