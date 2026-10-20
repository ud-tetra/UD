# Full-quotient lower singular bound using an arbitrary approximate basis

This is a separate route from RESPONSE_LEMMA.md. The latter proves only a weak-response obstruction and requires an observable trial vector. This route proves a LOWER singular bound; it does not require an exact observable projector.

Let F be the fixed normalized sampling map, rank r=1999, and norm(F)<=1. Take any real Q of size2640-by-r and a real skew r-by-r matrix J. Let K be the real skew model generator and E=KQ-QJ. Put Y=4096^-1/2 stack_j RQ exp(t_j J), with t_j=j/2. Duhamel and orthogonality of both propagators imply

    norm(exp(tK)Q-Q exp(tJ)) <= t norm(E).

The norm is spectral. Summing squared block norm bounds gives

    norm(FQ-Y) <= T_rms norm(E),
    T_rms²=(4095*8191)/24=11180715/8.

Consequently, if sigma_min(Y)>=sY and norm(E)<=e with sY>T_rms e, then

    sigma_min(FQ)>=sY-T_rms e>0.

The product inequality sigma_r(FQ)<=sigma_r(F) norm(Q) now yields

    sigma_min_positive(F)>=(sY-T_rms e)/norm(Q).

The rank r premise is essential to identify sigma_r(F) with its smallest positive singular value. Q need not initially be certified injective: the strict positive FQ lower bound proves its injectivity. If etaQ>=norm(Q-transpose Q-I), then norm(Q)<=sqrt(1+etaQ). A conservative rational upper may replace the square root.

For the complete Y Gram G=Y-transpose Y, take an r-by-r approximate eigenvector matrix V and a nonnegative real diagonal d. Certify etaV>=norm(V-transpose V-I)<1 and rho>=norm(G-V d V-transpose). Then

    lambda_min(G)>=min(d)*(1-etaV)-rho.

Indeed, V is square invertible, sigma_min(V)²>=1-etaV, and Weyl applies to the symmetric residual. A positive right side gives sY as its square-root lower bound. Merely reporting computed eigenvalues, Cholesky success, isolated channel condition numbers, or entrywise errors without an operator-norm conversion does not prove the result. Frobenius enclosures are sufficient for etaQ, etaV, e and rho, although conservative.

All cross-channel terms must be retained in G. When J is block rotation, analytic finite sine/cosine sums may construct G, but the sums and their roundoff/cancellation errors need validated enclosures. A saved numerical factorization is a proposal, not an exact Gram identity. The Gram dimension alone is unrelated to the older321-column Hankel estimator certificate.

If the lower bound l=(sY-T_rms e)/norm(Q) is strictly above1/2029, norm(F)<=1 implies kappa_positive(F)<2029. If it is positive but smaller, only the corresponding weaker upper condition bound is certified. The full2640-domain condition remains infinite from the641-dimensional kernel.

Same-team development only. No measured source, acquisition, estimator or physical weight law is introduced. External review PENDING; Physical Promotion=0.
