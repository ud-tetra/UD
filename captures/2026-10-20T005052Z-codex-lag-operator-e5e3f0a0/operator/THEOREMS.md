# Exact saved residual operator certificate

Let L=X-YT, with finite saved binary64 entries interpreted as exact dyadics, and G=L^T L. Then G is positive semidefinite and ||L||2^2=lambda_max(G). Consequently

||L||2 <= min{ sqrt(trG), sqrt(max_i sum_j |Gij|), (sum_ij Gij^2)^(1/4) }.

Proof: G=L^TL is PSD, so its largest eigenvalue is at most its trace. For an eigenvector choose a coordinate of maximal absolute value; the eigenvalue modulus is at most its corresponding absolute row sum. Finally, orthogonal diagonalization gives lambda_max(G)^2<=sum eigenvalues^2=tr(G^2)=sum_ij Gij^2. Taking nonnegative roots proves the three bounds. Exact integer accumulation and positive scale preserve equality and PSD. An arbitrary symmetric or even positive-diagonal supplied matrix is not enough; it must equal the bound residual Gram.

If one declared rational squared-cap test passes, the original operator-norm premise ||L||2<=2^-34 holds for these saved factors. A Frobenius upper exceeding this cap does not contradict that result: trace(G) sums all squared singular values, whereas the operator norm uses only the largest. This separation is mathematical, not a new estimator execution or a change to the previous protocol.

All conditional source phase theorem dependencies remain. No unseen-record, all-input solver, unaliased/SI frequency, native observer or physical correspondence claim follows.
