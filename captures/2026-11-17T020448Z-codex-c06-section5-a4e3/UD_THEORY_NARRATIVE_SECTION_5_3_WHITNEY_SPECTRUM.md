# 5.3 Regular simplex geometry and the Whitney edge spectrum

*Proposed insertion after §5.2 of the UD Theory Narrative Manuscript v0.15.*

Consider a regular Euclidean \(d\)-simplex of side length \(\ell\), with \(d\ge2\). Give its oriented edge coefficients the Euclidean inner product and use the Whitney one-forms \(w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i\), each normalized by its integral on its own oriented edge. The field inner product is averaged over the volume of the simplex. Write \(n=d+1\), \(D_0=B_1^\mathsf T\), and let \(P_g,P_c\) be the coefficient-space orthogonal projections onto the cut and cycle spaces. The regular geometry makes these two spaces invariant while assigning them different weights.

**Regular-simplex spectrum.** The Whitney one-form mass is
\[
M_1=\frac{2}{n\ell^2}P_g+\frac{4}{n(n+1)\ell^2}P_c .
\]
The multiplicities are \(d\) and \(d(d-1)/2\), respectively. To see the cut weight, take \(j=D_0u\) with \(u\) mean-zero. Its Whitney field is the constant gradient of \(\sum_i u_i\lambda_i\). The gradients satisfy \(g_i\cdot g_k=(2/\ell^2)(\delta_{ik}-1/n)\), so the squared norm of the field is \(2\|u\|^2/\ell^2\). The complete-graph incidence gives \(\|D_0u\|^2=n\|u\|^2\), yielding the stated cut eigenvalue.

The mean field of a cycle vanishes. Indeed, the average of \(\lambda_i\) is \(1/n\), so the mean Whitney field is \(n^{-1}\sum_i(B_1j)_i g_i\). Its remaining affine part is \(A(x-c)\), where \(c\) is the centroid and \(A\) is skew. The constant exterior derivative has squared norm \(2\|A\|_F^2\) in the ordinary Euclidean two-form inner product. Uniform barycentric moments give
\[
\Sigma_d=\overline{(x-c)(x-c)^\mathsf T}
=\frac{\sum_i(v_i-c)(v_i-c)^\mathsf T}{n(n+1)}
=\frac{\ell^2}{2n(n+1)}I_d.
\]
Thus \(\overline{\|A(x-c)\|^2}=\ell^2\|dw\|^2/[4n(n+1)]\). For the curl energy \(Q=\overline{\|dw\|^2}\), the Gram entries follow from \(dw_{ij}=2d\lambda_i\wedge d\lambda_j\). They equal \((16/(n\ell^4))(B_2B_2^\mathsf T)_{ij,kl}\): substitution of the gradient products gives diagonal \(16(n-2)/(n\ell^4)\), signed adjacent entries of magnitude \(16/(n\ell^4)\), and zero entries for disjoint edges. In the full simplex, \(B_2B_2^\mathsf T=nP_c\). Hence \(Q=(16/\ell^4)P_c\), and multiplying by the geometric rotational coefficient gives the cycle eigenvalue above. Constant fields and centered rotations are orthogonal under volume averaging.

**Radial and axial moments.** The mean squared distance from the centroid is the trace of \(\Sigma_d\). On the tetrahedron this is \(3\ell^2/40\). A rotation about a centroidal axis samples squared distance in the two perpendicular directions. Its mean squared distance from the axis is therefore \(2\ell^2/40=\ell^2/20\). Writing the centered field as \(\tfrac12(\nabla\times w)\times(x-c)\) gives the tetrahedral rotational coefficient \(\ell^2/80\). On an equilateral triangle the entire plane is the rotation plane, so the mean squared radial distance is \(\ell^2/12\), and the corresponding coefficient is \(\ell^2/48\).

**Equalization and its scope.** The cut-to-cycle ratio is \((d+2)/2\). Holding the cut mass fixed and selecting a scalar mass therefore requires adding \(d/2\) copies of the centered rotational energy. For \(d=2\), one copy makes each equilateral face block scalar, and summing the four individual face averages then gives the equalized tetrahedral boundary edge form. For \(d=3\), the volume average requires \(3/2\) added copies. The required augmentation answers an equalization problem. Geometry supplies the resident rotational weight and the spectrum, while a constitutive principle must specify whether the interaction adds any rotational energy. Reflection of the field preserves its squared rotational norm.

The accompanying exact rational replay checks direct mass and curl assembly for \(d=2,\ldots,7\) at two side lengths. The statistical and physical meanings of any measured response are outside this geometric calculation. The boundary and bulk conventions are fixed by the [C06 gyration proof](https://github.com/ud-tetra/UD-Physics/pull/405) and [its UD capture](https://github.com/ud-tetra/UD/pull/529).

**Claim boundary footer:** Physical Promotion = 0.
