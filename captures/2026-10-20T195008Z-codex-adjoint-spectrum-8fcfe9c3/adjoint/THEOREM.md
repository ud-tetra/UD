# Two-sided retained singular-value certification from two partial equations

Development — no registry entry. Physical Promotion=0. External promotion review PENDING.

For a real m×n matrix Z and saved retained factors U (m×q), V (n×q), descending positive S=diag(s1,…,sq), suppose actual operator bounds are

    ||UᵀU−I||≤a<1, ||VᵀV−I||≤b<1,
    ||ZV−US||≤f, ||ZᵀU−VS||≤g.

The existing per-case exact forward and Gram norm certificates are inherited premises. This turn reconstructs the original projected integer matrix (checked against original raw and projection identities) and computes the new adjoint equation exactly. It is a zero-fit replay of existing data, not a new preparation, perturbation or acquisition.

Let QL=U(UᵀU)^(-1/2) and QR=V(VᵀV)^(-1/2), and let C=QLᵀ Z QR. Complete QL and QR to orthogonal bases only for the proof, obtaining blocks

    Z ~ [[C,X],[Y,D]].

Forward equation implies ||Y||≤f/sqrt(1−b); adjoint implies ||X||≤g/sqrt(1−a). Thus deleting both off-diagonal blocks changes operator norm by at most

    e=max(f/(1−b),g/(1−a)).

The maximum is valid because the rectangular operator [[0,X],[Y,0]] has norm max(||X||,||Y||); it is not necessary to sum both bounds.

Writing GL=UᵀU and GR=VᵀV, the forward equation gives

    C=GL^(1/2) S GR^(-1/2) + QLᵀ(ZV−US) GR^(-1/2).

For 0≤x<1, sqrt(1−x)≥1−x and

    ||GL^(1/2)−I||≤a/(2−a),
    ||GR^(-1/2)||≤1/(1−b),
    ||GR^(-1/2)−I||≤b/[(1−b)(2−b)].

The first inequality follows from the extremal Gram eigenvalues and rationalizing the square-root deviation; the inverse bound follows by the same rationalization. Therefore a conservative exact rational compression bound is

    c={s1[a/(2−a)+b/(2−b)]+f}/(1−b),
    ||C−S||≤c.

Suppose a separately supported actual tail enclosure sigma_(q+1)(Z)≤t holds, and the strict matching gap

    sq−c > t+e

is positive. Let B=diag(C,D). Weyl gives sigma_(q+1)(B)≤t+e. All q singular values of C are at least sq−c>t+e. If ||D||>t+e then B would have q+1 singular values above t+e, a contradiction. Hence ||D||≤t+e<sigma_q(C), so the leading q singular values of B are exactly the singular values of C, with order and multiplicity. Applying Weyl to Z,B and C,S yields

    |sigma_j(Z)−sj|≤c+e for every j=1,…,q.

This is an ordered two-sided retained-spectrum bound. A full321-column left factor or reconstruction residual is not required. The proof uses singular values, not eigenvalues of the saved shift T, and gives no exact-spectrum(T) statement.

If epsilon=c+e<sq, the ambient LEADING q-spectrum condition is at most (s1+epsilon)/(sq−epsilon). This bounds sigma1(Z)/sigma_q(Z); it is not the full condition down to sigma_n(Z). It is distinct from PR283's restricted right-span condition and from native1893-dimensional/full-Hankel conditioning.

For j>q, descending nonnegative proposals and the actual tail enclosure give

    |sigma_j(Z)−sj|≤max(t,s_(q+1)).

Thus a mixed full-list bound is max(epsilon,t,s_(q+1)). Retained209 error can be below2^-41 while the full321 mixed bound is only below2^-25. Do not transfer the retained budget to the discarded112 values. The inherited original-radius source floor sigma209(Z)≥L together with retained epsilon≤2^-41 implies the original lower proposal-floor condition s209≥L−2^-41. The mixed full-list error≤2^-25 supplies the previously derived strict rank/no-tie sufficient budget. These are finite implications for the validated saved cases, not all-input backend conformance.

The source-tail/forward/Gram statements remain inherited, hash-bound premises. Hashes alone do not prove these statements. The new adjoint integer witness is independently checked entrywise by a deterministic modular/CRT audit with an explicit difference bound; finite random probes are not used as a proof. Protocol tolerances are O03 controls, not theory constants. No source H/full-factor/frame/target proof, all-input termination or numerical-library correctness, physical freshness, SI calibration or six-ratio accuracy is established here. Earlier HOLD/NO-GO verdicts remain unchanged.
