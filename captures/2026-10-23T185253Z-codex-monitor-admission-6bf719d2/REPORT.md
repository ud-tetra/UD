# Sampled-monitor receipt graph v0.1

**RESULT: PASS_SCOPED — constructor software controls.** Nine reviewed evidence roles now connect the sampled-monitor design to an unsigned tail-bound proposal. One author-controlled positive fixture and 56 rejection controls passed (57 cases). This is a structural contract and reproducible computation, not independent review or empirical admission. **Physical Promotion = 0; EXIT-03 HOLD; independent review pending.**

## What is bound

Every evidence node binds one frozen apparatus/run, source preparation, acquisition profile, channel mapping, monitor epoch, units, residual reference, kernel and source-contract hash. Receipts bind exact node bytes, witness bytes, role and fixture designation. Config and receipt allowlist must be controlled outside the submitting packet. The bundled allowlist and reviewer labels are entirely synthetic and author controlled; they confer no review authority.

| Evidence role | Required witness and scope |
|---|---|
| Samples | 1024 ordered signed complex residual samples in V; canonical finite binary64 hex words; original bytes included and reviewed |
| Clock | Timestamp bytes plus metrology supporting **true physical times**; affine error ≤10 ppb and total sample residual ≤10 ns, including timestamp/metrology uncertainty |
| I/Q path | Complete residual measurement/extraction path, applicable frequency/voltage range, loading and conditioning; matrix error ≤1/10⁶ at raw two-vector norm ≤5 V |
| Error budget | Deterministic complex sample RMS shares ≤10 µV acquisition/quantization, 5 µV quadrature, 3 µV baseline, 2 µV numerical; matrix charge cannot be omitted |
| Source class | Fixed coefficients/frequencies across both intervals, modes100–199, 1 s grid span, ≤5 mHz mode errors; independent preparation/completeness evidence |
| Outside-model TV | Independently supported complex spectral-measure variation ≤10 µV; same monitor FFT, assumptions or standard deviation do not establish this |
| Transfer | Same residual complex spectral measure, simultaneous preparation and common epoch across monitor and acquisition intervals |
| Computation | Source hashes; recomputed exact digital energy/RMS, rational sampled-Gram floor and tail calculation |
| Tail TV | Unsigned deterministic upper-bound proposal carrying graph/config/profile hashes and dependency roles |

The clock contract is distinct from the original acquisition's 0.2 ns error requirement. Timestamp residual checks verify the submitted numerical list; the reviewed calibration must establish its relationship to actual sampling events. A correctly formatted list alone supplies no time calibration.

The prototype coverage is [−1/10⁸,100000001/10⁸] seconds, containing the 1024 nominal monitor samples at j/1024 and the acquisition interval [0,16183/1953125] seconds. This is a **synthetic prospective acquisition profile**, separate from the unresolved historical profile. A source must maintain the reviewed preparation and residual decomposition over that entire interval. The transfer receipt must account for any primary-signal subtraction, reference conversion and loading. Their errors must fit the stated allocations; matching apparatus names is insufficient.

## Exact arithmetic and output boundary

The inherited theorem gives, conditionally,

\[
T_{\rm tail}\le\frac{211}{20}(r_d+\epsilon_d+T_{\rm out})+T_{\rm out}.
\]

At the frozen ceilings r_d=11/200000 V, epsilon_d=1/50000 V and T_out=1/100000 V, the design upper bound is

\[
T_{\rm tail}\le\frac{3627}{4000000}\,\mathrm V
=0.00090675\,\mathrm V<\frac1{1000}\,\mathrm V.
\]

The new checker replays the rational sampled-Gram lower bound and computes the mean squared complex norm of the exact serialized binary64 sample values. An integer ceiling square root produces its rational RMS upper bound. The design uses the 55 µV ceiling, not an unproved continuous-time RMS interpolation. The synthetic waveform and its copied bytes are inherited from the prior fixture; they are not measured I/Q data.

`TAIL_BOUND_PROPOSAL_FIXTURE.json` is **UD_UNSIGNED_MONITOR_TAIL_PROPOSAL_1**, not a v0.1 acquisition evidence packet or an approved receipt. Importing it requires independent review of the graph and an explicit reviewed bridge/policy integration. The v0.1 checker is unchanged; there is no automatic twelve-role admission. The other eleven acquisition roles, including full amplitude and tail absolute frequency, remain required. A TV bound alone does not discharge absolute bandwidth, energy, native support or an action bridge. No new mathematical theorem is asserted in this software milestone.

## Adversarial verification

The suite checks run/channel/epoch/unit/kernel/source mismatches; stale coverage; clock bounds and actual submitted timestamp deviations; I/Q multiplication and undercharging; invalid, excessive or statistical bounds; unsupported source/FFT roots; stationary-mode requirements and alias intrusion; unproved historical transfer; changed computation source, energy, Gram constants and tail export; missing, duplicate, unknown and cyclic references; corrupted sample/method bytes; nonfinite and short sample records; unapproved receipts, constructor labels, fixture laundering, unsafe paths and duplicate JSON keys.

Semantic mutations rebind their author-controlled node and receipt hashes so rejection occurs at the intended semantic gate. A transitive cycle reaches outside-TV → tail-TV → computation → outside-TV. Changing a sample while preserving a low RMS still fails against a stale computation certificate. Exact expected rejection reasons are asserted in `build_and_test.py`; this is stronger than accepting any arbitrary HOLD.

These controls verify implementation behavior under the chosen schema. They cannot authenticate a reviewer, prove the truth of a witness report, establish statistical coverage as deterministic support, or demonstrate physical independence. No packet can provide that authority merely through labels or hashes. The CLI is a scoped research checker, not a hardened network upload service.

## Historical candidate and review work remaining

The original circuit packet and empty trust catalog were replayed with the unchanged v0.1 checker. Result: **HOLD — apparatus/run binding unresolved**, with twelve acquisition roles still lacking reviewed evidence. No monitor measurements, calibration reports, source preparation records or reviewed transfer to file6385 have been supplied in the scoped record. This milestone neither reanalyzes raw experimental data nor claims such records cannot exist elsewhere.

Next obtain a review-ready source-preparation and full-path calibration specification with a concrete method for the independent 10 µV outside-TV bound. That evidence must address the exact alias counterexample and simultaneous residual transfer before a real run could be admitted. Freeze its acceptance criteria and negative controls before measurement; no experiment is performed here.

A. **CURRENT MISSION TRAJECTORY** — Establish a target-blind apparatus-to-model evidence path through mathematical certificates and independently reviewed measurement conditions.

B. **WHAT WAS DONE** — Added nine-role monitor graph, exact arithmetic replay, source/witness/receipt bindings, unsigned tail proposal and 57 constructor controls; preserved prior artifacts and acquisition checker.

C. **FINDING** — Structural integration is reproducible. The 3627/4000000 V ceiling remains conditional; no physical evidence or independent receipt is admitted.

D. **UD GAP IMPACT** — Makes the tail role's missing monitor prerequisites explicit. Does not close action normalization, EXIT-03, empirical validation or grand-unification goals.

**NEXT TRAJECTORY STEP** — Specify the independent source-completeness/outside-TV witness and full-path calibration procedure for premeasurement review. Physical Promotion = 0.
