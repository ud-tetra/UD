# Independent review of the frozen C26 weighted model

PASS for the stated finite mathematical conclusions. The reviewed member is epsilon=1/2 on the specified ten-tetrahedron C10 orbit, in unit Euclidean chain coordinates, with the unchanged 62-coordinate vertex-link observer. This is same-team development review, not a blinded or external validation. No physical constitutive law, acquisition or estimator fit is supplied.

| Quantity | Certified value | Basis |
|---|---:|---|
| Nominal top second-order observation rank | 390 | Exact rational factor ranks and a nonzero prime minor |
| Augmented nominal cyclic space dimension | 444 | Exact rational factor ranks and a nonzero prime minor |
| Weighted top second-order observation rank | 443 | Explicit upper proof and nonzero prime minor |
| Full weighted continuous-history rank / kernel | 1999 / 641 | Top-channel delta plus inherited nominal 1893 and channel separation |
| Old/new hidden-space intersection | 640 | Exact subspace argument |
| New observation rank restricted to the old 747-dimensional kernel | 107 | Rank-nullity on that intersection |
| Frozen 4096-sample rank / kernel | 1999 / 641 | Nonaliasing and modal Vandermonde |

The net full rank gain is 106. The kernels are not nested: a new stationary hidden line replaces the old one, so “106 old coordinates recovered with the rest unchanged” would be incorrect. Character-resolved weighted ranks have not been computed.

## Independent calculations and payload replay

The reviewer reconstructed G from signed dual-face adjacency, rather than importing the producer's B-transpose-B matrix, and reconstructed the observed boundary rows directly from the pinned JSON. Exact factor calculations give nominal390 and augmented444. All 30 factor profiles agree with the final producer output. The independent weighted prime-field calculation supplies lower443. A finite-field lower bound alone is not used to assert a deficient rational rank.

A separate final replay verifies all 60 compact rational upper payloads: the pivot identities and denominator-cleared memberships contain 1,590,000 matrix entries. The three nonzero minors over the trial-division-verified prime1009 have determinants103,66,1005, for dimensions390,443,444. There are312 final payload checks. The final witness hashes agree with the scientific source-binding file; input endpoint hashes agree during replay. This assumes stable intended inputs, and is not a universal concurrent-mutation guarantee.

The exact upper proof is substantive. The augmented G-cyclic space W is G- and P-invariant, hence invariant under D2 and M. Connected signed dual-graph Laplacian structure shows kerG=span(h), and the zero spectral projection of a selected coordinate puts h in W. The nonzero vector D2-inverse h is in W and is annihilated by both M and C. The weighted cyclic row space therefore has dimension at most444−1. The443 minor saturates this bound.

## Kernel geometry and channel scope

Let F=W-perpendicular, dimension156. It is G-invariant, P annihilates it, and it is perpendicular to h. The weighted C3 dark space is precisely F plus the moved stationary line span(D-inverse h). On F, D is identity, and B3 is injective. The oscillatory dark partners F in C3 and B3F in C2 therefore provide312 shared top hidden dimensions. The moved stationary line is nominally visible at the named face, so it adds no intersection dimension. The unchanged lower hidden space has328 dimensions, yielding640 in the intersection and107 on restriction of the new observation map to the old kernel. The full proof is in INTERSECTION_PROOF.md.

This uses the inherited downward-closed channel-separation theorem, rather than an unsupported inference from commutation. The old full1893/747 result and observed frequency count105 are inherited. There is no fresh dense2640-dimensional full-rank calculation.

## Finite conditioning: formal and practical conclusions differ

Independent exact row/column sums give squared channel norm bounds24,15,15. Pairwise channel annihilation implies norm(K)≤sqrt24<5. Half-step phases have diameter<5<2pi; the frozen4096 samples thus have the continuous kernel by a distinct-node Vandermonde argument.

The final analytic conditioning argument is valid but deliberately extremely weak. For the integer normal generator S=2K, the observable quotient is rational. Its monic rational minimal polynomial divides the integer characteristic polynomial, so Gauss's lemma makes it integral. Normality makes it squarefree. These rational-module facts are necessary: an arbitrary subset of algebraic eigenvalues would not suffice. The nonzero integer discriminant supplies a gap-product lower bound. The sine chord bound, Vandermonde determinant bound, integer-jet positive pseudodeterminant, and modal-jet norm then give

- smallest positive singular value of the normalized4096-sample map greater than 2^-10394665;
- positive-quotient condition number less than 2^10394665;
- full2640-domain condition number infinite, because641 directions remain hidden.

CONDITION_CHECKS.json independently verifies the exact Taylor fraction, binary exponents and their sum. BOUND_CHECKS.json is the earlier norm/nonaliasing-only stage: its “NOT_CERTIFIED” quantitative fields are superseded only by this formal analytic bound, not by a useful numerical enclosure. No numerical singular-value calculation is claimed. Practical2029 conditioning, accuracy, calibration, shape and noise-tolerance gates remain HOLD. Neither a trial response nor the maximum of isolated channel condition numbers certifies the full quotient.

## Final bindings and review history

FINAL_BINDING.json pins the final checker, theorem, sign-normalized witness archive, three scientific outputs and their byte-identical producer replay. It confirms the documented60-membership/3-minor counts. The final source and theorem have no unresolved mathematical review blocker.

The frozen first reviewer payload checker stopped at an unnecessarily positive-denominator predicate: a negative common FLINT denominator can represent the same exact rational rows. Its source and failure receipt are preserved, and no false complete PASS was issued. The second checker accepted mathematically nonzero denominators; the final producer archive normalizes row signs and passes the separate final positive-format replay. This is a witness-format correction, not a mathematical retraction. A draft norm checker also replaced equality to a conservative cap18 by the intended upper-bound comparison; the actual exact value is15. No contrary theorem result was published.

No source/archived executable, floating estimator, acquisition, full Hankel or numerical eigensolver was run by this review. All conclusions are conditional on the explicit inherited premises and the declared mathematical model. No physical promotion or external review authority is supplied.

Development — no registry entry. External review PENDING. Practical conditioning HOLD. Physical Promotion=0.
