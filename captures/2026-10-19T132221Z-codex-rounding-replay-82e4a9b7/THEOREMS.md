# Projection rounding and actual full-factor SVD admission

Status: DERIVED / validated exact-dyadic numerical output. Physical promotion0. Development — no registry entry. External nonconstructor replay PENDING.

## Frozen domain and lineage

The domain is the ENCODED signed-int64 record ball: each preparation/time 62-vector differs from the encoded PR195 ramp-clock-stress baseline by Euclidean norm at most one integer quantum (2^-48 in model units). This permits one ±1 coordinate, or zero, per vector with arbitrary dependence. It is not a prequantization real-valued error model or the original instrument-noise contract. All source cutoffs remain2^-24. The 321-column sketch A has column ordering c*37+a and scale1/128. The exact projected matrix is N/2^55 with N=XA, 8191×321. No full Hankel matrix is constructed.

## Uniform exact integer backend (new implementation)

All raw inputs have |X|≤30100665057351. Every product/partial sum in an int64 dot is safe because max column absolute sum is4588 and their product is138101851283126388<2^63. Integer multiplication/addition therefore computes N exactly.

Let Xc be the replay-verified cyclic-unit member. For each column j set Lj=sum_a max_c |A[c*37+a,j]|. Two encoded-ball members differ in each62-vector by l1 at most2, hence |(X-Xc)A|≤2Lj elementwise. Exact raw replay establishes max|XcA|=2504646576089788 and max Lj=520. Thus every numerator in this encoded ball is bounded by2504646576090828<2^53. Integer-to-binary64 conversion and division by2^55 are exact, with no underflow. This proves uniform exactness of the NEW integer backend's projection only.

## Conditional legacy GEMM bound

For correctly rounded binary64 conventional dot reductions, no reduced precision, and at most2294 rounding steps per term, the standard gamma bound gives |Bhat-B|≤gamma2294 |D||S|. Conversion of X and dyadic scalings are exact. The range-only bound is

    gamma2294 * 30100665057351 / 2^55 * sqrt(8191*(320*4588^2+1634^2)) < 1.580822e-9.

This is a conditional implementation theorem; installed vendor/thread metadata alone does not qualify an opaque BLAS reduction. It is larger than the inherited approximately3.209e-12 sketch-fit admission envelope, so it cannot transport the prior ideal phase guarantee uniformly. This is proof insufficiency, not an observed estimator failure. The present actual legacy GEMM projection is separately shown exactly equal to N/2^55; that record-specific equality is not extrapolated over the ball.

## A posteriori full-factor SVD theorem

Treat every returned floating factor as an exact dyadic. Use U8191×321, all321 singular values s, and Vt321×321. Verify finite entries, nonnegative descending s, and etaU=||U' U-I||F<1, etaV=||Vt Vt'-I||F<1. Form C=diag(s)Vt in EXACT dyadic integer arithmetic, not a floating product. With G=U'U, H=U'Z,

    r²=||Z||F² - 2 tr(C' H) + tr(C' G C).

All cancellation is exact; a negative exact numerator rejects. Let p(eta)=eta/(1+sqrt(1-eta)). Polar normalization and the Frobenius-to-operator inequality yield

    epsilonSVD = r + smax*(p(etaU)*sqrt(1+etaV)+p(etaV)).

Weyl's inequality then encloses each singular value of the exact projected matrix by the corresponding reported s±(epsilonProjection+epsilonSVD). No DGESDD backward-error constant is assumed. Every one of321 intervals is checked against the fixed cutoff, including the discarded values. Both fresh outputs certify exactly209 values above2^-24. This is retained sketch order, not algebraic record/Hankel rank or the nominal1893 native-observer count.

Both outputs have projection error0 and epsilonSVD<2.555e-13. sigma209>0.002880430080778 and sigma210<3.621e-13. The duplicate paired factors are retained to show the actual paths agree; they are not independent replications.

## Remaining limitations

Uniform integer projection exactness plus two admitted actual SVD outputs does not prove uniform SVD convergence, uniformly small returned defects, phase matching, optimizer convergence, full-Hankel acceptance, source frequency/SI identification or hidden-state recovery. The new phase proposals are retained as actual emissions but this SVD certificate does not newly certify their phase error. The complete U/V factors omitted by old archives cannot be reconstructed retroactively from retained U alone. Old archives and HOLDs remain immutable.

Frozen certify.py covers the present finite, int64-delta, order209 witness format. Unsupported order0/321 would error rather than issue a certificate; the unused string-delta fallback in run.py is not supported by this verifier. No general-purpose hostile-intake certification is claimed. New package integrity and exact projection hashes are checked before portable replay.

## Primary mathematical/implementation references

- N.J.Higham, The Accuracy of Floating Point Summation, SIAM J.Sci.Comput.14(4),1993: https://nhigham.com/wp-content/uploads/2023/10/high93s.pdf
- SciPy1.17.0 SVD API (returned U,s,Vh and gesdd default): https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.linalg.svd.html
- Netlib DGESDD: https://netlib.org/lapack/explore-html/df/d22/group__gesdd_ga8941e5ff50de36580dae8940015e9cb0.html

The numerical enclosures above are independently derived from retained dyadic factors, not asserted by those API references.
