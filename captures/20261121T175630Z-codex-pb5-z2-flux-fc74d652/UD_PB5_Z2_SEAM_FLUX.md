# PB5 equatorial \(\mathbb Z_2\) flux and cyclic orientation

**Exact obstruction for the declared \(\mathbb Z_2\) edge connection. Physical Promotion = 0.**

Use the equatorial cycle \(C=(0,1,2,3,4,0)\) of PB5, with poles 5 and 6. Put a link \(u_{ij}\in\{+1,-1\}\) on each edge and impose reciprocal transport \(u_{ji}=u_{ij}^{-1}=u_{ij}\). Vertex switches \(\eta_i\in\{+1,-1\}\) act by \(u_{ij}\mapsto\eta_i u_{ij}\eta_j\). On the equator the product
\[
W(C)=\prod_{j=0}^4 u_{j,j+1}
\]
is gauge invariant, and it classifies edge connections on the ring up to switches. To prove classification, fix four consecutive links to \(+1\) by switching their endpoints in order. The remaining link then records \(W(C)\).

Reversal gives \(W(C^{-1})=W(C)^{-1}=W(C)\). The odd-flux sector even admits the manifestly symmetric representative \(u_{j,j+1}=-1\) on every rim edge. Since the ring has odd length, this gives \(W=-1\) with full equatorial dihedral symmetry. A single negative rim link is another representative on the ring in isolation. Its position is gauge dependent there.

The relevant mirror for clockwise versus counterclockwise is a **vertical** mirror through the PB5 axis. It reverses the cyclically oriented edge sum \(c\) and sends \(C\) to \(C^{-1}\). Horizontal reflection exchanges the poles, fixes the equatorial vertices pointwise, and fixes \(c\). The \(\mathbb Z_2\) holonomy is even under both. An equivariant orientation selector that receives only \(W\) must assign \(f(W)c=-f(W)c\), so \(f(W)=0\). A nonlinear function of this one scalar remains mirror-even. In particular, multiplying \(b|z|^2\) by any function of \(W\) does not supply the missing mirror-odd coefficient.

## Extension into the filled bipyramid

For a triangle \(t=[ijk]\), let \(F_t=u_{ij}u_{jk}u_{ki}\). Multiply these signs over either of the five-triangle cones from the rim to a pole. Each spoke occurs twice and cancels:
\[
\prod_{t\ \text{in north cone}}F_t=W(C)
=\prod_{t\ \text{in south cone}}F_t.
\]
Thus \(W=-1\) requires an odd number of negative triangles in each cap. A flat connection on the filled carrier forces \(W=+1\). The smallest support of a negative curvature pattern with \(W=-1\) has two triangles, achieved with one negative rim link and all other links positive. The two triangles share that rim link. Their curvature makes the chosen location observable on PB5.

A fully symmetric curved extension also exists. Take all five rim links negative and all other links positive. This has negative curvature on the ten exterior triangles and positive curvature on the five radial triangles. Changing the spine link to negative gives another fully symmetric extension, now with negative curvature on the radial triangles as well. These are admissible assignments in the finite link model, and the flux alone supplies neither a choice of assignment nor a dynamical generation rule.

The exact replay exhausts 32 ring connections, 32 ring switches, and all 1,024 gauge-fixed PB5 connections. It checks reversal, cone identities, the minimum two-triangle support, and both fully symmetric PB5 realizations of the negative flux. A model with additional mirror-odd state or asymmetric curvature data requires a separate test. Endogenous selection of an oriented axial source remains open.

- [Two-cell spin transition and projector reference, UD #582](https://github.com/ud-tetra/UD/pull/582)
- [PB5 axial and planar shear projection, UD #584](https://github.com/ud-tetra/UD/pull/584)
