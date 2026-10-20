# Exact trial-response obstruction lemma

Let B=B3D, H=B-transpose B, C=R2B, and the top-channel skew generator be K=[0,-B; B-transpose,0]. Let v be a nonzero exact real vector in Q=W intersect (D-inverse h)-perpendicular. Under the inherited rank443 result, its grade3 embedding is perpendicular to the complete new hidden space. Let lambda>0 and r=(H-lambda I)v, delta=norm(r).

Define the trial trajectory

    p(t)=(-Bv sin(sqrt(lambda)t)/sqrt(lambda), v cos(sqrt(lambda)t)).

Its initial state is (0,v). Its equation residual p-prime-Kp is

    (0, r sin(sqrt(lambda)t)/sqrt(lambda)).

Since the true generator is skew, its propagator is isometric. Duhamel therefore gives

    norm(exp(tK)(0,v)-p(t)) <= t delta/sqrt(lambda), t>=0.

The actual full observer has norm1 and no grade3 entries. On the finite grid t_j=j/2, j0..M-1, put L²=mean(t_j²)=(M-1)(2M-1)/24. The normalized sample response obeys

    norm(F_M(0,v))/norm(v)
       <= [norm(Cv)+L delta]/[sqrt(lambda) norm(v)].

This uses Minkowski for the two finite time-block vectors and |sin|<=1. It makes no assumption that an individual trial eigenmode exhausts a frequency block and does not discard cross-channel terms: it bounds the actual response of an exact state under the complete generator. It is an upper bound on a weak trial response, not a lower bound on the smallest singular value.

The unchanged normalized uniform grade0 harmonic u has norm(F_M u)=1/sqrt10. Hence, on the complete positive singular quotient,

    kappa_positive(F_M) >= sqrt(lambda norm(v)²/10)/[norm(Cv)+L delta].

A strict obstruction to2029 follows if an exact upper B on the squared response satisfies B<1/(10*2029²). No upper condition bound or practical gate pass follows if this test does not close. Exact Q membership is necessary to infer sigma_min_positive<=the trial response; a small response of a vector containing hidden mass is insufficient.

For an exact rational candidate, a checker can compute norm(v)², norm(Cv)² and norm(r)² as rational values, then enclose positive square roots with predeclared dyadic integer ceilings. Choosing L as an exact rational upper of its root is sufficient. Zero residual is allowed; lambda must remain strictly positive. No sine/cosine implementation or sampled exponential is required.

Development — no registry entry. Same-team development review, external review PENDING, Physical Promotion=0.
