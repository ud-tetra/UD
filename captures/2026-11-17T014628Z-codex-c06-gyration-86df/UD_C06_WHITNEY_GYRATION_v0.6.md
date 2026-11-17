# C06 Whitney gyration and integration domains

**EXACT / CONDITIONAL** on regular Euclidean simplex geometry and the stated integration convention. **Physical Promotion = 0.**

## Centroidal derivation

Identify the lowest-order Euclidean Whitney one-form with its vector field. A linear combination of terms \(\lambda_i\nabla\lambda_j-\lambda_j\nabla\lambda_i\) is affine with a skew linear part, since each term has derivative \(\nabla\lambda_j\nabla\lambda_i^\mathsf T-\nabla\lambda_i\nabla\lambda_j^\mathsf T\). On a simplex with centroid \(c\) write the field as its constant mean plus a centered rigid rotation. Their squared norms add under averaging because the centered displacement has mean zero. In two dimensions the rotational field is \(\tfrac12(\operatorname{curl} w)J(x-c)\), with \(J\) the oriented quarter turn. In three dimensions it is \(\tfrac12(\nabla\times w)\times(x-c)\).

For a \(d\)-simplex with vertices \(v_i\), the uniform barycentric moments give the covariance
\[
\Sigma=\overline{(x-c)(x-c)^\mathsf T}
=\frac{\sum_{i=0}^{d}(v_i-c)(v_i-c)^\mathsf T}{(d+1)(d+2)}.
\]
On a regular simplex of side \(\ell\) the numerator is \((\ell^2/2)I_d\). Thus an equilateral face has \(\Sigma=(\ell^2/24)I_2\), and a regular tetrahedral bulk has \(\Sigma=(\ell^2/40)I_3\).

The face-averaged rotational mass is \(\tfrac14\operatorname{tr}(\Sigma)|\operatorname{curl}w|^2=(\ell^2/48)|\operatorname{curl}w|^2\). In the bulk it is \(\tfrac14(\|\omega\|^2\operatorname{tr}(\Sigma)-\omega^\mathsf T\Sigma\omega)=(\ell^2/80)\|\omega\|^2\) for \(\omega=\nabla\times w\). The face coefficient follows from geometry before any scalar target is posed. The interaction that adds an extra copy of this rotational energy is a separate choice. A group order alone carries no side-length dependence.

## Face sum and volume average

Use the same oriented edge coefficients throughout, with Whitney forms normalized by unit integral on their own edges. Let \(P_g,P_c\) project onto cuts and cycles. On the boundary, \(Q_f\) denotes the **sum of the four individual area-averaged face curl forms**. There is no factor \(1/4\) across the four faces in this convention. Each face has area \(\sqrt3\,\ell^2/4\), and Stokes' formula gives the constant curl of its Whitney trace as the signed boundary circulation divided by that area. Therefore \(Q_f=(16/3\ell^4)B_2B_2^\mathsf T=(64/3\ell^4)P_c\). The average across four faces would instead have cycle eigenvalue \(16/(3\ell^4)\).

For the whole solid tetrahedron let \(Q_v\) denote the **volume-averaged** squared curl. Write \(g_i=\nabla\lambda_i\) and use \(g_i\cdot g_j=(2/\ell^2)(\delta_{ij}-1/4)\). The curl of edge form \(ij\) is \(2g_i\times g_j\); the induced Gram matrix is \((4/\ell^4)B_2B_2^\mathsf T=(16/\ell^4)P_c\). Both forms use the same coefficient-space projectors. Their \(4/3\) ratio under the stated norms does not establish a connection to other tetrahedral response factors.

## Bulk doubling test

The volume-averaged edge mass is
\[
M_v=\frac{1}{2\ell^2}P_g+\frac{1}{5\ell^2}P_c.
\]
For cuts \(j=D_0u\), with \(u\) mean-zero, Whitney interpolation gives the constant \(\nabla\sum_i u_i\lambda_i\), with squared norm \(2\|u\|^2/\ell^2\), while \(\|j\|^2=4\|u\|^2\). Cycles have zero mean field and their mass is exactly \((\ell^2/80)Q_v\). Adding one copy of this native bulk rotational mass leaves eigenvalues \(1/(2\ell^2)\) and \(2/(5\ell^2)\), so the bulk remains split. Equalization at the cut eigenvalue instead requires
\[
M_v+\frac{3\ell^2}{160}Q_v=\frac{1}{2\ell^2}I_6 .
\]
This is an added \(3/2\) copies of the existing bulk rotational mass, selected by the equalization condition. At unit side length, an additional overall factor eight would give the combinatorial \(4I_6\). Under the face-sum convention, one extra copy of the local face rotational energy supplies the exact cycle deficit on the assembled edge matrix and gives \((4/3\ell^2)I_6\).

The exact replay independently assembles the full bulk Whitney mass from degree-two barycentric moments and checks it against the cut–cycle formula. Both geometries are kinematic results, with no physical interaction or coefficient promotion implied.

**Claim boundary footer:** Physical Promotion = 0.
