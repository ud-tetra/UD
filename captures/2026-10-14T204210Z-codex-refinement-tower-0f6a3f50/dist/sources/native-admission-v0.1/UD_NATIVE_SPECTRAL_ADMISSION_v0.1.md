# Native spectral admission: residual floors and endpoint aliases

Development v0.1 · 14 October 2026 · public reading edition0.9

**RESULT.** The complete n=10 programmed clock has a positive generator-residual floor against each of the three declared unit-metric UD carrier classes, even with arbitrarily many identical copies and a free common rate. Exact full-operator embedding fails in all three classes for every even n≥4. These statements do not exclude exact endpoint agreement: an explicit phase alias has zero endpoint error with generator residual8 kappa. Native source selection and protected export remain open.

EXACT CONDITIONAL / SCOPED NO-GO / OPEN NATIVE ADMISSION. Development — no registry entry. Constructor-team AI verification and source review; independent human review pending; physical promotion0. The supplied clock and its metrics remain authored candidate apparatus. Comparison optimization does not turn a control into a theory coefficient or acquire a native encoding.

## 1. Frozen operators, domains and preliminary dimension gate

The programme from clock0.1 has Hermitian H_p on its complete retained domain. Its eigenvalues are kappa(n−2j), j=0,…,n, each with multiplicity Q. kappa>0 is an internal comparison rate. Clock, all payload/history/receipt/donor factors and every spectator remain accounted. Unitary prefix dressing does not change these eigenvalues.

Paper I's declared unit-metric carriers give H_c=i A_c, with the following signed eigenvalues. These are fresh-reconstructed simplicial boundary spectra as well as primary source statements.

| Carrier class | Chain dimension | Zero multiplicity | Positive eigenvalues and multiplicities |
|---|---:|---:|---|
| Filled tetrahedron Delta3 |15|1|2, multiplicity7|
| K-minus: two tetrahedra sharing a face |23|1|sqrt(3), multiplicity4; sqrt(5), multiplicity7|
| K-plus: three tetrahedra sharing an edge |27|1|sqrt(2), multiplicity2; sqrt(5), multiplicity11|

Negative frequencies have matching multiplicities. The orientations are increasing-order simplex bases; changing orientation only conjugates the operator. Use r identical disconnected copies at one common rate gamma>0, H_native=gamma directsum A_c times i. This is a narrowly declared class. Coupled copies, different rates per copy, additive nontrivial environments, different metrics or new complexes have different spectra and are not excluded by this comparison.

A complete isometry E requires native dimension at least(n+1)Q. In the default programme Q=3,869,835,264 and total dimension42,568,187,904; a single15-,23- or27-dimensional carrier already fails this gate. Even one prefix-frame clock component has dimension11. Enlarging copies removes a dimension obstruction but does not automatically remove spectral mismatch, source selection or encoding cost.

## 2. Exact necessary residual bound

Define eta=norm(H_native E−E H_p), with E†E=I on the entire programme domain.

**Theorem NA.1.**

    eta >= max_(lambda in spectrum H_p) distance(lambda, spectrum H_native).

*Proof.* For a normalized target eigenvector u, E u has norm1. The residual applied to u is (H_native−lambda I)E u. The finite Hermitian spectral theorem gives its norm at least the nearest eigenvalue distance. Maximize over target eigenvalues. No invariant-image assumption is needed. □

Let x=gamma/kappa and let S_c be the signed unit-rate native spectrum including0. Define

    b_(n,c)(x)=max_(j=0,…,n) min_(s in S_c) abs(n−2j−x s).

Then eta/kappa≥b_(n,c)(x). For positive target values and gamma≥0, negative native centres cannot improve on0, so only ordered centres0, x a, x b need be considered. Allowing x=0 in the relaxation does not improve the minima below; their witnesses use positive rates.

If a target eigenvalue has multiplicity Q, a safe stronger bound is its Q-th nearest native eigenvalue distance, counted with multiplicity. Indeed the squared residual on that eigenspace is the compression of (H_native−lambda I)^2 to a Q-dimensional isometric image; the maximum Rayleigh quotient is at least its Q-th lowest eigenvalue. Insufficient fixed-copy multiplicity can raise the residual. The nearest-spectrum floor is not automatically sharp under a fixed source encoding or restricted register map.

## 3. Exact free-scale optimization and its limited meaning

For n=10, target positive frequencies in units of kappa are {2,4,6,8,10}. Optimizing the lower certificate over x is a deliberate relaxation in favour of the native class. It selects no native rate, physical clock, metric or output fit.

| Declared class | Minimum nearest-spectrum floor | Optimizing comparison x=gamma/kappa |
|---|---|---|
| Delta3 |3|7/2|
| K-minus |7 sqrt(15)−25|7(sqrt(5)−sqrt(3))|
| K-plus |2|interval[8/sqrt(5),3 sqrt(2)]|

Decimals appear only in the inspector. The expressions and interval certificates are exact.

**Theorem NA.2 (the three minima).** These values are global minima of b_(10,c).

*Delta3 proof.* If a proposed error epsilon<3, target4 cannot use the0 centre, so it must use the sole positive centre z. Target10 must also use z. Their distance6 requires epsilon≥3, contradiction. At z=7, assign2 to0 and4,6,8,10 to7; the maximum error is3.

*K-plus universal lower proof.* If epsilon<2, none of the five targets can use0. One interval of radius epsilon has width<4 and cannot cover three targets spaced2 apart. Two positive centres therefore cover at most four targets, contradiction. At epsilon=2, centres sqrt(2)x and sqrt(5)x cover4/6 and8/10 while2 uses0 precisely for x in[8/sqrt(5),3 sqrt(2)]. The exact enumerator certifies that this is the complete optimizer set.

*K-minus proof.* It suffices to consider epsilon<3 because the claimed witness is below3. Then4 and10 cannot use0. They cannot both use one centre because their separation6 exceeds2 epsilon. They also cannot use the centres in reversed order: the higher centre would have to be at most4+epsilon<7 while the lower centre would have to be at least10−epsilon>7. Hence4 uses sqrt(3)x and10 uses sqrt(5)x, implying

    (10−epsilon)/sqrt(5) <= x <= (4+epsilon)/sqrt(3),
    epsilon >= (10 sqrt(3)−4 sqrt(5))/(sqrt(3)+sqrt(5)) = 7 sqrt(15)−25.

At x=7(sqrt(5)−sqrt(3)), the lower centre is7(sqrt(15)−3) and the higher is7(5−sqrt(15)). Assign2 to0,4/6 to the lower,8/10 to the higher; all gaps satisfy the bound and4/10 attain it. □

### Replay certificate for other even lengths

The exact solver uses the native lower/high ratio rho=a/b and high centre y=b x. Choose an ordered partition of the positive targets into0, lower and higher centre blocks. Such a partition always exists when any assignment is feasible, since nearest-centre Voronoi intervals are ordered. Each nonempty block with minimum u and maximum v imposes a centre interval[v−epsilon,u+epsilon]. A block assigned0 imposes epsilon≥its maximum.

For lower block[u_1,v_1] and higher block[u_2,v_2], the minimal partition error is the maximum of

    zero_block_maximum,
    (v_1−u_1)/2, (v_2−u_2)/2,
    (v_1−rho u_2)/(1+rho), (rho v_2−u_1)/(1+rho),

omitting terms belonging to empty blocks. The feasible y intervals follow directly from centre containment and y≥0. Native ratios are sqrt(15)/5 for K-minus and sqrt(10)/5 for K-plus, so all comparisons use exact quadratic-field arithmetic. All partitions are inventoried, not merely the winning fit.

Optimal intervals are retained as a **union**, not automatically their convex hull. For n=2 and a two-frequency native class, exact spectral agreement is possible at either y=2 or y=2/rho; intermediate y values generally do not have zero error. This negative control guards against turning isolated feasible scales into an unsupported continuous family.

## 4. Sharpness with unconstrained copies and eigenbasis encodings

These minima can be attained as actual residual norms in the **unrestricted identical-copy/free-isometry relaxation**, with sufficiently many copies. This is distinct from source-selected E or an acquired native apparatus.

For n=10 take r=3Q copies. All three native classes then supply3Q zero modes. Map the programme eigenvalues0,+2 kappa,−2 kappa (eachQ) to distinct native zero modes. Map the remaining positive target modes4/6/8/10 and their negatives as follows:

| Class |4/6 target modes|8/10 target modes|Common comparison rate|
|---|---|---|---|
| Delta3 |positive centre7 kappa|same centre7 kappa|gamma/kappa=7/2|
| K-minus |gamma sqrt(3)|gamma sqrt(5)|gamma/kappa=7(sqrt(5)−sqrt(3))|
| K-plus |gamma sqrt(2)|gamma sqrt(5)|gamma/kappa=8/sqrt(5)|

Use sign-matched negative eigenvectors for negative targets. Native positive/negative capacities are at least4Q for Delta3 and2Q at each glued frequency, because the source multiplicities multiplied by3Q exceed these demands. Choose orthogonal native eigenvectors for every target vector. E is isometric and each residual column is its assigned eigenvalue difference times an orthogonal native vector. Its norm is therefore exactly the maximum gap. This realizes respectively3 kappa,(7 sqrt(15)−25)kappa and2 kappa.

The chosen target basis is the actual dressed programme eigenbasis. Dressing changes no capacity or spectral argument. These E can mix chain degrees, sites and register identities; they need not be local or source-derived. The construction claims only that3Q copies suffice, not that this copy count is minimal. Per-programme dimensions in these witnesses are45Q,69Q,81Q; their excess coordinates remain retained in the native domain, not discarded as free resources.

## 5. Exact full-generator no-go and clock slowdown

**Theorem NA.3.** For even n≥4 and every positive common rate, none of the three stated unit-metric classes or arbitrary identical copies admits exact isometric intertwining of the full programmed operator.

*Proof.* The programme has positive frequencies2 kappa and4 kappa. Delta3 has only one positive native frequency. K-minus and K-plus have two with irrational ratios sqrt(5/3) and sqrt(5/2), so neither ratio can equal2. An exact intertwiner must preserve both distinct eigenvalues. □

For T=pi/(2 kappa), the residual floors imply

    T eta >= (pi/2) times {3, 7 sqrt(15)−25, 2}.

All three default floors exceed1. Lowering kappa and gamma together reduces eta in rate units and increases T inversely; this dimensionless requirement does not decrease. Letting both source and programme collapse into a harmonic limit is not a small full-word propagation certificate.

Crucial type distinction: the Duhamel estimate is an **upper bound** on propagation/channel discrepancy. A lower floor on its upper-budget quantity T eta cannot be read as an actual error or failure-probability lower bound. It only prevents this particular sufficient certificate from establishing small endpoint error. Sharper trajectory comparisons, endpoint phase matching and constrained prepared subspaces have different contracts.

## 6. Explicit endpoint alias with zero endpoint error

**Theorem NA.4 (alias negative control).** With n=10, gamma=kappa and5Q copies of Delta3, an engineered isometry has

    exp(−iT H_native)E = E exp(−iT H_p),
    eta = 8 kappa,       T eta = 4 pi.

*Construction.* At T, native harmonic eigenvalues have phase+1 and active eigenvalues±2 kappa have phase−1. Programme eigenvalues0,±4 kappa,±8 kappa have phase+1 (5Q vectors); ±2 kappa,±6 kappa,±10 kappa have phase−1 (6Q vectors). Map the first group to distinct native harmonic vectors. Map positive/negative modes in the second group to distinct native±2 kappa eigenvectors. The source provides enough vectors at5Q copies. All eigenphases agree at T, and the largest generator gap is8 kappa. □

A compressed one-component numeric witness uses five native tetrahedra (dimension75) and the eleven-dimensional clock block. Its exact ingredients are a source harmonic vector h=(1,1,1,1)/2 and the active plane v=(1,−1,0,0), u=A v/2; (v±i u)/2 are normalized eigenvectors of iA with eigenvalues±2. The complete E is constructed from orthogonal programme and native eigenvectors. The full-Q proof repeats these assignments and composes with the inverse prefix dressing; the huge default matrix is not numerically built.

This proves zero **complete endpoint channel** discrepancy for any encoded input and spectator, not merely agreement of one response bit. Intermediate propagation differs. The encoding and input admission are supplied, so this is not a physical realization or a source-selected prediction. It also leaves the full generator no-go intact.

## 7. Admission disposition and next gate

The mathematical comparison now distinguishes dimension, eigenvalue multiplicity, residual, elapsed time and endpoint eigenphase. The fixed unit-metric classes fail exact full-clock admission. Their free-scale residual relaxation has explicit, sharp floors. Endpoint aliasing is possible under supplied global encoding and cannot promote the candidate to native dynamics.

The next native target must therefore name a different source-authored geometry/metric/coupling or explicitly adopt a weaker prepared-window/endpoint contract. It must provide the complete E and its provenance, admitted state/bank, clock definition, output readout and retention mechanism. Optimizing a comparison variable is not that source law. A failure of one fixed class does not authorize adjustable weights or distinct rates without their own typed constitutive definition.

Primary basis: Paper I review1.1.1 §§4,6.3–6.4 and exact simplex deletion rule; programmed clock0.1 PC.1/PC.4/native-isometry contract; fresh native matrix/field/partition checks and separate AI audit. Ledger0.39 remains a historical235-object attachment, while the public ledger has448 rows. CRL2 subdivision remains a proposal. No empirical run, source-acquired E, physical scale or human review is supplied.

Reproduction: `python native_admission.py`, `python verify_native_admission.py`, `python verify_dependencies_v09.py`, `node verify_native_admission_ui.mjs`. Root exact certificates use Python standard library. Small dense alias diagnostics additionally use NumPy/SciPy; the independent generated checker uses NumPy/SciPy/SymPy. Numerical tolerances are recorded separately. No archived source program is executed for ingestion.

Disposition: EXACT CONDITIONAL residual minima and alias; SCOPED NO-GO for complete generator intertwining in the three declared classes; OPEN new native source, constrained encoding, preparation, locality, physical units and protected export. Development — no registry entry; independent human review pending; physical promotion0.
