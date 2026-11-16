# AW5 Gap 4 — Time-dependent additive local gauge covariance

**Status:** EXACT_INTERNAL / CONDITIONAL for the covariant realization. NO-GO for the requested homogeneous linear generator with a shifting connection. **Physical Promotion = 0.**

## Transformations and obstruction

Use the unit simplex inner product to identify real edge cochains with edge coordinates. Let \(A=B^\mathsf T-B\) on \(C=\bigoplus_{k=0}^3C_k\), let \(E:C_1\to C\) insert an edge vector, and define \(J=EB_1^\mathsf T\). The prescribed transformation is \(c'=c+J\chi(t)\). Introduce an edge connection \(\alpha'=\alpha+B_1^\mathsf T\chi\).

There is no family of homogeneous linear generators \(A_\alpha\) satisfying the requested covariance for arbitrary time-dependent \(\chi\) under these transformation laws. Start with \(c\equiv0\). Choose \(\chi(t_0)=0\) and \(J\dot\chi(t_0)\ne0\). At \(t_0\), the transformed state is zero while its derivative is nonzero. Every homogeneous linear right-hand side vanishes at zero. This obstruction also applies to homogeneous linear formulas whose coefficients depend on \(\dot\alpha\) or on a temporal potential.

## Exact compensated dynamics

The invariant state \(u=c-E\alpha\) can be evolved by the native equation \(\dot u=Au\). In the original variables this is the affine system
\[
\dot c=A(c-E\alpha)+E\dot\alpha .
\]
With the stated transformation of \(\alpha\), its right-hand side changes by exactly \(J\dot\chi\), matching the derivative of \(c'\). This prescription fixes the affine source uniquely once the invariant-state evolution \(\dot u=Au\) is specified. In grades,
\[
\begin{aligned}
\dot\rho&=-B_1(j-\alpha),\\
\dot j&=B_1^\mathsf T\rho-B_2q+\dot\alpha,\\
\dot q&=B_2^\mathsf T(j-\alpha)-B_3\sigma,\\
\dot\sigma&=B_3^\mathsf Tq.
\end{aligned}
\]
If \(\alpha=B_1^\mathsf T\phi\) is restricted to pure gauge, the added source has only vertex and edge components, \(+B_1B_1^\mathsf T\phi\) and \(+B_1^\mathsf T\dot\phi\). This suffices for all prescribed gauge shifts. It leaves the cycle–face observables invariant and recovers the original system in the gauge \(\phi=0\).

For a temporal-potential version, introduce \(a_0'=a_0+\dot\chi\) and
\[
\mathcal D_t c=\dot c-Ja_0,\qquad
\mathcal D_t c=A(c-E\alpha).
\]
The invariant combination \(\mathcal E=\dot\alpha-B_1^\mathsf T a_0\) gives \(\dot u=Au-E\mathcal E\). The compensated native dynamics correspond to \(\mathcal E=0\), including the pure-gauge choice \(a_0=\dot\phi\).

## Loop observables and remaining scope

For \(B_1z=0\), the real loop coordinate \(z^\mathsf Tj\) is gauge invariant, as is \(z^\mathsf T\alpha\). The real curvature \(B_2^\mathsf T\alpha\) is gauge invariant by \(B_1B_2=0\). The pure-gauge construction supplies zero spatial curvature. A general \(\alpha\) can carry invariant curvature. A dynamical theory of that curvature still requires an equation or constitutive rule for the connection and a specified interaction with native state. Under \(\dot u=Au\), \(\alpha\) enters only as a compensator. This local symmetry is an additive real vertex action, with constant vertex parameters acting trivially on a connected carrier.

An exact integer replay checked the affine covariance and the result of dropping the compensating terms on the tetrahedron, shared-face bipyramid, filled AW5, and hollow AW5.

**Claim boundary footer:** Physical Promotion = 0. The theorem establishes covariance of a declared finite real-chain evolution.
