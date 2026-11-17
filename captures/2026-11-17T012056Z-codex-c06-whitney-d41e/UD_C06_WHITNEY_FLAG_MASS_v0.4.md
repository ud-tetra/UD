# C06 Whitney tangential-trace flag mass

**EXACT / CONDITIONAL** for the Euclidean Whitney construction on a regular tetrahedron. **NO-GO** for isotropy or agreement with the scalar edge form under positive rescaling of this mass. **Physical Promotion = 0.**

## Construction

Use a filled regular Euclidean tetrahedron of side length one, increasing vertex order, ordinary unoriented area measure and tangential restriction to each triangular face. For edge \(ij\), take the Whitney one-form \(w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i\), normalized to have integral one on its own oriented edge. For each face, use the area-normalized \(L^2\) inner product of the three tangential traces belonging to that face. Edges off the face have zero tangential trace. With independent edge–face flags the resulting metric \(M_W\) has one \(3\times3\) block per face.

For a unit equilateral face the tangential gradients satisfy \(d\lambda_i\cdot d\lambda_j=2(\delta_{ij}-1/3)\). The face averages of \(\lambda_i^2\) and \(\lambda_i\lambda_j\) for \(i\ne j\) are \(1/6\) and \(1/12\). Let \(b_f\) be the signed local triangle boundary column in the chosen edge order. Expanding the Whitney products gives
\[
M_f=\frac{6I_3-b_fb_f^\mathsf T}{9}.
\]
The diagonal is \(5/9\), and the off-diagonal entries are \(-[e:f][e':f]/9\). The eigenvalues are \(1/3\) on \(b_f\) and \(2/3\) on its orthogonal complement. The full flag spectrum is therefore \(1/3\) with multiplicity four and \(2/3\) with multiplicity eight. The construction respects signed tetrahedral relabeling and distinguishes two flag sectors.

## Edge pullback and the C06 constraint

For the duplication map \(S\), \(S^\mathsf TS=2I_6\), each edge occurs twice, and
\[
S^\mathsf T M_W S=\frac{12I_6-B_2B_2^\mathsf T}{9}
 =\frac89 I_6+\frac19 B_1^\mathsf T B_1.
\]
Here the final equality uses the single-cell identity \(B_1^\mathsf T B_1+B_2B_2^\mathsf T=4I_6\). The pulled-back eigenvalues are \(4/3\) on \(\operatorname{im}B_1^\mathsf T\) and \(8/9\) on \(\operatorname{im}B_2\), each of dimension three. The coexact-to-exact weight ratio is \(2/3\); no positive scalar rescaling makes this matrix equal to \(4I_6\). For raw \(L^2\) integration without area normalization the matrices acquire the common face area \( \sqrt3/4\), with the same ratios. With side length \(\ell\), the area-normalized matrix also scales by \(1/\ell^2\).

The 57-dimensional kernel of \(M\mapsto S^\mathsf T M S\) consists of perturbations preserving a prescribed edge form. The Whitney trace construction chooses a particular positive flag metric whose pullback lies outside the affine fiber over \(4I_6\). More generally, in any face-block-diagonal flag metric the same-face coefficient between distinct edges survives directly in the corresponding edge matrix entry, since their shared face is unique. Consequently, a face-block-diagonal extension of a diagonal edge form must have diagonal face blocks. The Whitney blocks violate this condition. The exact and coexact edge spaces used here are not the \(E\) and \(T_2\) summands of the five-dimensional spatial shear representation.

The exact replay uses a degree-two triangle quadrature, rational barycentric gradients and signed incidence assembly. It verifies both spectra and the distinct pulled-back eigenvalues. The result uses the declared tangential face mass. Volume integration, diagonal mass lumping and integration of the one-forms along individual edges are different constructions. Neither a midpoint gain law nor the \(7/192\) defect-to-response allocation follows from this calculation.

**Claim boundary footer:** Physical Promotion = 0. The regular Euclidean coframe and the face-readout rule are declared model choices.
