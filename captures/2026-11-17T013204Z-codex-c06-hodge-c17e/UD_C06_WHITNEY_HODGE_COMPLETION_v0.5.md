# C06 Whitney Hodge energy and cycle correction

**EXACT / CONDITIONAL** on the declared face Whitney masses. **Physical Promotion = 0.**

Let \(D_0=B_1^\mathsf T\), \(D_1=B_2^\mathsf T\) on the oriented boundary of the regular Euclidean unit tetrahedron, with signed simplicial bases and area-normalized tangential integration summed over its four faces. Let \(P_g\) and \(P_c\) be the Euclidean projections of the six edge cochains onto cuts and cycles. The merged Whitney trace result gives
\[
M_1=\tfrac43P_g+\tfrac89P_c,\qquad
\tfrac43 I_6-M_1=\tfrac49P_c.
\]
The required increment is \(4/9\), obtained by subtracting the two eigenvalues. \(M_1\) is an edge form and its flag lift lies outside the affine pullback fiber over a scalar edge form. The 57-dimensional kernel consists of flag-form perturbations with zero pullback.

## Whitney masses and adjoints

Assemble \(M_0\) from the boundary traces of the vertex barycentric basis. The local averaged products are \(1/6\) on the diagonal and \(1/12\) off it. Each vertex lies in three faces and each pair of vertices lies in two, giving \(M_0=\tfrac13 I_4+\tfrac16\mathbf1\mathbf1^\mathsf T\). This has eigenvalues \(1/3\) on mean-zero vertex cochains and \(1\) on constants.

A face Whitney two-form has unit integral on its oriented face and constant signed density \(1/A_f\), with \(A_f=\sqrt3/4\). The consistent area-averaged two-form mass is therefore \(M_2=\tfrac{16}{3}I_4\). These are masses for the boundary complex and the same face integration convention as \(M_1\).

The degree-one codifferential is \(\delta_1=M_0^{-1}D_0^\mathsf T M_1\). It vanishes on cycles because \(M_1\) preserves them and \(D_0^\mathsf T\) annihilates them. Its energy and the exterior derivative energy, expressed as symmetric forms in the edge coefficients, are
\[
\begin{aligned}
Q_{\rm down}&=M_1D_0M_0^{-1}D_0^\mathsf T M_1
             =\tfrac{64}{3}P_g,\\
Q_{\rm up}&=D_1^\mathsf T M_2D_1=\tfrac{64}{3}P_c.
\end{aligned}
\]
The identities use \(B_1^\mathsf T B_1=4P_g\), \(B_2B_2^\mathsf T=4P_c\), and the mean-zero vertex mass. Equivalently \(Q_{\rm up}=M_1\delta_2D_1\) for the adjoint \(\delta_2=M_1^{-1}D_1^\mathsf T M_2\). Its cycle contribution arises from the exterior derivative paired with its adjoint.

## Equalization test

The full Whitney Hodge **energy matrix** is \((64/3)I_6\) in these coefficients. Adding any multiple of that full energy to \(M_1\) leaves the cut–cycle gap at \(4/9\). The mass-raised Hodge **operator** \(M_1^{-1}(Q_{\rm down}+Q_{\rm up})\) has eigenvalues \(16\) on cuts and \(24\) on cycles.

For independent nonnegative weights \(x,y\), the augmented metric \(M_1+xQ_{\rm down}+yQ_{\rm up}\) is scalar exactly when \(y-x=1/48\). Requiring the scalar to stay \(4/3\) gives \(x=0,\ y=1/48\). Hence
\[
M_1+\tfrac{1}{48}Q_{\rm up}=\tfrac43I_6.
\]
At the flag level the term adds \(b_fb_f^\mathsf T/9\) to each face block, giving \((2/3)I_3\) per face. The factor \(1/48\) is fixed **by the specified equalization target** in this unit-length convention. The Whitney complex and its adjoints supply the operators; a constitutive rule selecting that relative weight remains open.

The rational replay assembles the Whitney masses on the four faces and multiplies the signed coboundary matrices. It checks the two energy forms, eigenvalue assignments, equalizing mass, and unchanged gap under a full-energy addition. Sources are the [merged Whitney derivation](https://github.com/ud-tetra/UD-Physics/pull/404) and [UD capture](https://github.com/ud-tetra/UD/pull/528).

**Claim boundary footer:** Physical Promotion = 0. This result uses the declared regular Euclidean duality and does not establish a midpoint gain or physical response allocation.
