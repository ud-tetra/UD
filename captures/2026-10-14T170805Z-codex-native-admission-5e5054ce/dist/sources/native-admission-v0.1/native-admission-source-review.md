# Native spectral admission: independent constructor-team scope audit

14 October 2026. Review of the proposed native admission extension to programmed-clock0.1. This is a separate AI audit within the construction team. It supplies neither independent human review nor CRL promotion. Physical promotion remains0.

## Frozen primary premises

Read the public `programmed-clock-v0.1/UD_PROGRAMMED_WEIGHTED_PATH_CLOCK_v0.1.md` in full, SHA256 `45b69deefe6f370ece8dc7e010e9df21796ffa7f9beee34217d8d708334627a3`, and its frozen Paper I `PI.txt`, SHA256 `23a62d17d88076589e4904973c166e086c03352629e620913e4bb3897eb275ab` (especially §§4,6 and Appendix C).

PC.1 fixes the complete programme spectrum as kappa(n−2j), j=0,…,n, each repeated Q times. Its exact endpoint is T=pi/(2 kappa). Prefix dressing preserves this spectrum. Paper I fixes the Hermitian native operator iA in unit chain metric: filled tetrahedron spectrum0,±2; two-cell face-sharing Kminus spectrum0,±sqrt(3),±sqrt(5); three-cell edge-sharing Kplus spectrum0,±sqrt(2),±sqrt(5). Their respective dimensions are15,23,27. Original skew spectra must be multiplied by i to discuss a Hermitian Hamiltonian; frequency magnitudes agree, but the objects must stay typed separately.

The declared comparison class is one such fixed native carrier, or identical direct copies, with one common positive overall rate gamma. No source fixes gamma/kappa. Changing the chain metric, choosing different rates on different copies, adding interactions, adding an offset, replacing the complex, restricting a target subspace, or changing the programme creates a different comparison contract. The following results do not silently cover those alternatives.

## Residual necessity

Let Hp and Hn be finite-dimensional Hermitian operators, and let E be an isometry from the **complete** programme carrier into the declared native carrier. Define eta=||Hn E−E Hp|| in the ordinary operator norm with the declared metrics already absorbed into normalized coordinates.

For every programme eigenvalue lambda, choose a normalized eigenvector psi. Then

    (Hn E−E Hp)psi=(Hn−lambda I)Epsi,
    eta >= dist(lambda,spec(Hn)).

The second inequality follows by expanding the normalized Epsi in an orthonormal native eigenbasis and bounding its squared norm by the smallest squared eigenvalue gap. Thus

    eta >= max_lambda dist(lambda,spec(Hn)).

No invariance of the encoded image is assumed. Exact eta0 does imply invariance and operator intertwining. Passing the spectral test alone does not produce E, native preparation, gate locality, decoder, output readout or protected records.

If lambda has multiplicity r, the sharper safe bound is eta at least the r-th smallest value of |nu−lambda|, counting all native eigenvalue multiplicities. Apply Courant–Fischer to (Hn−lambda I)^2 on the r-dimensional image of that programme eigenspace. Full cross-eigenvalue assignment refinements require their own stated theorem; nearest-frequency tests should not be advertised as complete encoding admission.

If the native dimension is less than (n+1)Q, E does not exist at all. A residual optimization over an empty encoding set is a capacity failure, not a finite residual certificate. Taking sufficiently many identical native copies removes this dimension obstruction, but it never adds a frequency to the set.

## Exact free-rate relaxation for the padded default n10

Set x=gamma/kappa, and for native positive frequencies S define

    b10(x)=max_(a in {0,2,4,6,8,10}) min_(s in {0} union S) |a−xs|.

For positive targets, negative native frequencies are no closer than0, so this half-spectrum formula is exactly the full symmetric nearest-spectrum bound. It gives eta/kappa >= b10(x) for every isometry. Optimization over all x>=0 is an optimistic relaxation of the actual native-rate problem; it does not identify or calibrate any physical rate.

| Declared native class | Minimum b10 | Rate ratio attaining minimum |
|---|---:|---|
| Unit-metric filled tetrahedron and identical copies | 3 | x=7/2 |
| Unit-metric Kminus and identical copies | 7sqrt(15)−25 | x=7(sqrt(5)−sqrt(3)) |
| Unit-metric Kplus and identical copies | 2 | x in [8/sqrt(5),6/sqrt(2)] |

These are exact algebraic results, not fitted constants. Proofs:

* Filled tetrahedron: if epsilon<3, targets4 and10 cannot use0 and cannot both lie within epsilon of the single positive center2x, since their separation is6. Center7 attains3, with target2 using0.
* Either two-frequency class: epsilon<2 leaves target2 outside the zero-center interval. A positive interval of radius less than2 covers at most two of the five positive targets, since three span4. Two such intervals cannot cover five targets. Hence epsilon>=2.
* Kplus: at epsilon2, target2 uses0; targets4,6 use lower center xsqrt(2) in [4,6]; targets8,10 use upper center xsqrt(5) in [8,10]. The displayed interval of x satisfies both conditions, proving the lower bound attained.
* Kminus: the candidate c=7sqrt(15)−25 is strictly between2 and3. If epsilon<c, targets4 and10 cannot use0; their separation6 is more than2epsilon, so they cannot use the same positive center. The lower center must serve4 and the upper center10. Thus xsqrt(3)<=4+epsilon and xsqrt(5)>=10−epsilon, which imply epsilon>=(10sqrt(3)−4sqrt(5))/(sqrt(3)+sqrt(5))=c. At x=14/(sqrt(3)+sqrt(5)), the lower and upper centers are4+c and10−c. Target2 uses0, targets4,6 use the lower center, and8,10 use the upper center. All errors are at most c.

The optimization has no hidden escape at infinite scale: for x>=2n/min(S), each native positive center is at least2n, so0 is nearest to every target and b_n(x)=n. The minimum can be searched on a compact interval. The zero-rate endpoint also gives n and cannot evade these bounds.

### Sharpness under unrestricted copies and free encoding

The displayed spectral floors are also the exact minimum operator residuals in the optimistic relaxation that permits sufficiently many identical copies, arbitrary complex isometries and the freely chosen common rate. A sufficient construction uses r=3Q native copies. No minimal-copy assertion is needed.

Choose orthonormal eigenbases of Hp and Hn. Map each Q-fold target eigenspace at lambda0,+2kappa,−2kappa to separate native zero modes; these require3Q vectors and every declared class supplies r=3Q harmonic modes. Map each remaining signed target eigenspace to distinct native eigenvectors with the same sign, as follows:

| Native class and rate x | Target magnitudes mapped to lower positive native frequency | Target magnitudes mapped to higher positive native frequency |
|---|---|---|
| Filled tetrahedron, x=7/2 | 4,6,8,10 all map to7 | Only one positive frequency |
| Kminus, x=7(sqrt(5)−sqrt(3)) | 4,6 map to4+c | 8,10 map to10−c, where c=7sqrt(15)−25 |
| Kplus, x=8/sqrt(5) | 4,6 map to8sqrt(2/5) | 8,10 map to8 |

All entries in this table are in units of kappa. Negative target eigenvalues use the opposite signed native eigenvalue. The filled tetrahedron supplies7r positive and7r negative active eigenvectors;4Q per sign are required. Kminus supplies4r per sign at the lower frequency and7r per sign at the higher;2Q at each sign/frequency are required. Kplus supplies2r and11r per sign at its lower/higher frequencies; again2Q are required. All capacity inequalities hold.

This defines E with E†E=I on the complete programme domain. In these eigenbases the residual sends each target vector to its own orthogonal native eigenvector times the corresponding eigenvalue difference. Consequently its operator norm is exactly the largest absolute difference. The zero-mode assignments have error at most2kappa. The active assignments attain respectively3kappa, ckappa and2kappa. For Kplus, 8sqrt(2/5) lies between4 and6, so its distances from4 and6 are both below2; the10-to8 assignment attains2. These constructions meet the necessary spectral floors, establishing sharpness in this relaxed class.

They are engineered eigenbasis encodings. They need not preserve chain degree, a native coordinate dictionary, geometric locality, original preparation or output observables. Dressing the programme changes its eigenvectors but not this existence argument: E is chosen on the actual dressed eigenbasis. Fixed copy count, source-selected E and any additional encoding constraints may yield a larger residual or no admissible E.

For even n>=4, exact embedding into any of these three fixed unit-metric classes is impossible at every common scale. The programme includes positive frequencies2kappa and4kappa, ratio2. The tetrahedron has only one positive frequency. Each glued class has two positive frequencies, with irrational ratio sqrt(5/3) or sqrt(5/2), so they cannot match that pair. Additional programme frequencies only strengthen the obstruction. This exact statement is about the complete programme operator, not endpoint transfer alone.

## Clock slowdown and the error-budget distinction

The spectral certificate implies

    T eta >= (pi/2) min_x b_n(x).

For n10 these bounds are respectively3pi/2, (pi/2)(7sqrt(15)−25), and pi. Lowering kappa and gamma together can make eta small in rate units while increasing T inversely; this particular integrated residual requirement remains unchanged.

The Duhamel estimate ||exp(−itHn)E−Eexp(−itHp)|| <= |t|eta is an **upper bound** on error. A lower bound on its right-hand side is never a lower bound on actual channel error. If Teta exceeds1, this particular sufficient trace-distance certificate is uninformative after capping; it does not establish failure probability, forbid exact endpoint aliasing, or prove a prepared transfer fails.

### Explicit endpoint alias: zero endpoint error with eta8kappa

Take n10 and gamma=kappa, with5Q direct copies of the filled tetrahedron. At T=pi/(2kappa), native eigenvalue0 has phase+1 and native eigenvalues±2kappa have phase−1. Programme eigenvalues0,±4kappa,±8kappa have phase+1 (5Q vectors); ±2kappa,±6kappa,±10kappa have phase−1 (6Q vectors).

Choose an isometry E mapping the5Q programme phase+1 eigenvectors to the5Q native harmonic vectors. Map the3Q programme positive phase−1 eigenvectors to distinct native +2kappa eigenvectors and the3Q negative ones to distinct native −2kappa eigenvectors. Each sign has35Q available native active eigenvectors, so capacity is ample. This E is an arbitrary engineered global encoding, not source-selected.

The complete endpoint operators intertwine exactly:

    exp(−iT Hn)E = E exp(−iT Hp).

Yet the eigenvalue mismatch is8kappa on lambda±10kappa and±8kappa, so eta=8kappa and Teta=4pi. Actual endpoint channel error is zero. At intermediate times the generators disagree. This constructive counterexample is the clearest regression test against converting an upper-budget obstruction into a dynamical error lower bound.

## Admission disposition

EXACT CONDITIONAL: residual necessity and the n10 algebraic minima, within the frozen operator/metric/rate class.

SCOPED NO-GO: exact full-operator embedding into the three specified unit-metric carrier classes and arbitrary identical common-rate copies, for even n>=4.

OPEN: source-selected enlarged complex, non-unit chain metric, coupling/source selection, complete isometry, preparation, locality, native clock calibration, physical energy accounting and protected export. Engineered weighted-path metrics remain a constructed representation, not native source evidence. Endpoint aliases, selected prepared transfers and source-authored new operators are separate contracts.

HUMAN REVIEW PENDING. PHYSICAL PROMOTION0. No automatic ledger or CRL promotion follows from this AI audit.

## Audit of the implemented report and exact solver

Read the actual root report `UD_NATIVE_SPECTRAL_ADMISSION_v0.1.md` in full and `native_admission.py` in full. Audited content hashes at this check:

* Report SHA256 `c83efb28a57904d0e019bd3c0ad29535993e9a0eb9484a3739a85e6c4c73231d`.
* Solver SHA256 `3e2093db96c8066019da6296050b2c18cff47f8d547c5c6e4bb875b2db1e5989`.

The report's n10 exact minima, rate choices, complete Kplus optimizer interval, eigenvalue multiplicities,3Q direct-copy sharpness construction and5Q endpoint alias agree with the derivations above. The compressed alias basis (v±i u)/2 is orthonormal with iA eigenvalues±2 because ||v||²=||u||²=2, v⊥u, Av=2u and Au=−2v. Five copies have75 native dimensions, sufficient for the11-dimensional Q1 clock block. This numerical witness is an operator comparison, not a source-acquired physical E.

The solver performs exact ordering in the quadratic fields D15 and D10, enumerates all ordered partitions, and merges only overlapping optimal intervals. Replayed n2 and n10 for all three classes. The n2 glued classes correctly yield two isolated optimizer high-centres: {2,2sqrt(15)/3} for Kminus and {2,sqrt(10)} for Kplus, rather than an invalid convex hull. At n10 it returns high centre7 for Delta3,35−7sqrt(15) for Kminus, and interval[8,3sqrt(10)] for Kplus. Dividing the latter by sqrt(5) gives the report's x interval[8/sqrt(5),3sqrt(2)].

One non-winning certificate detail was flagged to the root: when every target is assigned the0 centre, the partition has no finite upper constraint on y, but the reviewed solver sets hi=lo=0. This represents a sufficient finite witness, not the full feasible interval[0,infinity). It never wins for the admitted n>=2, so it does not change the residual minima or optimal-interval unions. Its interval semantics should be corrected or explicitly labeled witness-only before treating every partition's printed endpoints as a full feasible interval certificate.

No Site edits or publication were made by this reviewer. This remains a constructor-team AI audit, not independent human review; physical promotion0.

### Final correction audit: partition interval issue resolved

Re-read the corrected solver interval/serialization logic. Final solver SHA256 is `546ac7ad5db929898158dd2d9365528ebd9dc68eaec95e86e5def3f26e8b39d5`. The report is unchanged at SHA256 `c83efb28a57904d0e019bd3c0ad29535993e9a0eb9484a3739a85e6c4c73231d`.

The all-zero partition now records `high_centre_min=0`, `high_centre_max=null`, and `high_centre_unbounded=true`, correctly representing the full feasible interval[0,infinity). Replayed all three classes at n2,4,6,8,10,12:18 such partition checks pass. Their bound is n, and the winning bound is always smaller. The exclusion from optimal finite-interval merging is valid for every admitted n: assigning all positive targets2,…,n to the higher centre (n+2)/2 yields error(n−2)/2<n, so the all-zero partition cannot win. Exact n2 disconnected optimizer points and n10 minima/intervals are unchanged.

The previously flagged certificate semantics issue is resolved. Final substantive disposition: PASS within the stated unrestricted identical-copy/free-isometry comparison scope. Source-selected native admission remains OPEN; independent human review pending; physical promotion0.
