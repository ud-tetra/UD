# Whole-ball shift bound: same-team mathematical design review

Design PASS with the norm and quantifier conditions below. No numerical constants or case outcomes were evaluated for this review. This is development, not externally independent review; physical promotion0.

## Frobenius upgrade requires the actual certificate construction

For full-column-rank U, set G=U^T U and Q=polar(U). If etaF>=||G-I||F and etaF<1, singular values give

||U-Q||F <= ||G-I||F/[1+sqrt(1-etaF)] <= p(etaF),

where p(x)=x/[1+sqrt(1-x)]. The same holds for the right factor V. Consequently an exact full-factor reconstruction residual rF, full Gram Frobenius defects etaUF,etaVF, and largest reported singular value smax yield

||Btilde-B||F <= rF+smax*[p(etaUF)*sqrt(1+etaVF)+p(etaVF)].

Add a Frobenius projection-error bound when the projection is not exact. This is the same numerical expression used by the parent certifier, whose reconstruction, Gram and projection-difference helpers are Frobenius sums of squares. Thus this specifically bound construction supports the stronger norm interpretation. A merely abstract operator-error certificate cannot be relabeled Frobenius; retain a separate generic lane with projected error sqrt(q)*epsilon2.

The parent baseline shift metric also uses exact sum-of-entry-squares diffnorm. Its normalized sigma0 may therefore be used as sigma0F in this argument; M0 remains an operator norm bound.

## One common alignment supports both norms

Write B0=L0+F0, rank(L0)=q209, ||F0||F<=r and sigmaq(L0)>=alpha=s0-r. Let Btilde have its full normalized SVD, with retained right factor Vq and left factor Qtop. With e2=r+Cdelta+epsilon2 and alpha>2e2,

||(I-P0)Qtop||2 <= t2=e2/(alpha-e2)<1.

For the Frobenius counterpart, multiply the residual singular equations by Vq. If a full Frobenius error epsilonF is certified, use eF=r+Cdelta+epsilonF. If only operator error epsilon2 is certified, use eF=r+Cdelta+sqrt(q)*epsilon2, since Vq has q orthonormal columns. Then

||(I-P0)Qtop||F <= tF=eF/(alpha-e2).

The canonical principal-angle Procrustes alignment simultaneously obeys

distance2<=c*t2, distanceF<=c*tF,
c=sqrt(2/[1+sqrt(1-t2^2)]).

Use this one alignment, rather than unrelated alignments in the two bounds. Full/retained polar discrepancy adds at most2p(etaF) in both norms because the retained Gram is a principal compression and the full Gram defect bound is Frobenius. Therefore the proposed d2,dF are safe.

## Comparator residual and exact least squares

Let Ua=Qa S be the returned retained basis, S=(Ua^T Ua)^(1/2). Choose O so Qa is aligned to Q0 O. Then

Tcmp=S^(-1) O^T Tbar0 O S

has the proposed orientation. The raw comparator shift residual satisfies

||Ua_plus-Ua_minus*Tcmp||F
 <= J=sqrt(1+etaF)*[sigma0F+dF*(1+M0)].

For A=Ua_minus, betaA=sqrt(1-etaF)*(beta-d2)>0 bounds sigmamin(A). These positivity conditions must be validated. The exact least-squares minimizer Tstar exists uniquely and its residual Estar has norm at most J.

For any finite returned real T, define Esh=Ua_plus-A*T and N=A^T Esh in exact saved-array arithmetic. Then

Esh=Estar+(A_dagger)^T N,
||Esh||F^2=||Estar||F^2+||(A_dagger)^T N||F^2.

The cross term vanishes because A^T Estar=0. Hence a Frobenius normal-residual ceiling nu implies

||Esh||F <= sqrt(J^2+(nu/betaA)^2).

This is conditional on full-factor quality and the normal-residual ceiling. It does not prove uniform BLAS/SVD/least-squares convergence, that every execution meets the quality gates, or uniform phase admission. If this sufficient bound exceeds a policy allowance, report proof HOLD, not actual algorithm failure.

## Fixed-basis diagnostic and strict lower-bound direction

On one saved basis, the same identity gives

||Estar||F >= sqrt(max(0,s_lower_squared-nu_upper^2/betaA_lower^2)).

Use exact raw-residual squared values or a certified LOWER; squaring a residual upper bound would invalidate this lower bound. Use a certified UPPER for the normal-residual norm and a positive LOWER for betaA. The max(0,...) is a valid nonnegative lower-bound construction, not permission to clip inconsistent exact squared residuals.

A strict lower bound above a fixed old shift gate proves that replacing T by exact least squares on THIS saved basis cannot meet THAT gate. It proves nothing about alternative bases, noise families, other algorithms, true phase accuracy, v2 admission or physical interpretation. Equality or an unresolved comparison is inconclusive.

All formulas here use real transposes, as do the saved U and T arrays. A complex extension would require adjoints and separate verification; it is not silently claimed.

## Recommended bounded controls

Verify symbolic or exact-arithmetic normal-equation/Pythagoras identities on a small full-rank fixture; retain existing actual data and engineering gates unchanged. Test nu=0 reduces the upper bound to J. An orthogonal normal-space residual gives the fixed-basis lower bound direction; invalid betaA<=0 must HOLD before division. Distinguish operator-only and Frobenius-certified lanes explicitly. Do not tune a new nu or quality budget after observing passage.

External request transmission does not establish external acceptance or a completed review receipt. Public evidence should preserve external review PENDING and omit private account identifiers.
