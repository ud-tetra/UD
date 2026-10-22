# Evidence admission structure and circuit disposition v0.1

21 October 2026 America/Chicago (capture UTC22October). SOFTWARE CHECKED / EMPIRICAL HOLD. Constructor verification only; independent scientific review pending. Development —no registry entry. Physical promotion0; EXIT-03 HOLD.

## Result

A portable evidence-packet contract and executable checker now connect the leakage theorem to twelve measurement prerequisites. All27 software controls pass: one complete synthetic packet reaches STRUCTURALLY_READY_FIXTURE, and26 corrupted or deficient cases return HOLD. Synthetic constructors/reviewers are fictional test labels, not independent reviews.

The Riechert circuit candidate returns **HOLD**. Its apparatus/run binding is unresolved, and the prior scoped audit supplies none of the twelve reviewed bound records required here. This means not established in the inspected material; it does not prove that additional author or laboratory records do not exist. No dataset is newly downloaded or reanalyzed, and no author is contacted.

A structurally complete packet can reach only STRUCTURALLY_READY_FOR_REVIEW. Every result retains empirical_admission=false and physical_promotion=0. The checker does not decide that a bound is scientifically true, that a reviewer is authentic, or that claimed independence exists.

## Twelve prerequisites

| Role | Bound | Expected evidence |
|---|---:|---|
| In-band spectral-measure TV | <=1 V | Independent source/model norm certificate |
| Envelope support | within±50 Hz | Source-class or calibrated transfer evidence |
| Tail spectral-measure TV | <=1/1000 V | Independent tail/leakage certificate, not same-output FFT |
| True full-envelope amplitude at phase centers | >=1/2 V | Independently supported amplitude lower bound |
| Physical tail absolute frequency | <=200000 Hz | Source/anti-alias evidence for the timing-slope allocation |
| Constant baseline magnitude | <=3 V | Instrument/baseline calibration |
| Additive noise and quantization | <=1/10000 V | Uniform acquisition bound covering the run |
| Relative gain error | <=1/100000 | Calibrated gain uncertainty over applicable range |
| Sample-time error | <=1/5000000000 s | Common-epoch clock/skew bound over displaced intervals |
| Clean voltage derivative | <=250000 V/s | Reviewed derivation or source/metrology bound |
| Baseline variation | <=1/20000 V | Residual variation after local constant baseline |
| Input magnitude | <=5 V | Applicable voltage/range bound |

These are deterministic worst-case bounds. A standard deviation, expectation, typical specification or confidence interval does not automatically satisfy them. One-channel readiness also does not establish cross-device phase skew; any channel set change requires a new profile and applicable evidence.

## Binding and review rules

PROFILE.json freezes the waveform/kernel hashes, dataset, channel set, nominal sample rate, digital carrier, window, temporal coverage, target and spectral-measure meaning. The physical apparatus/run identifier is explicitly UNRESOLVED and blocks real readiness. Gain/skew/clock errors must fit the timing and input-error assumptions, including every displaced sample interval; matching sample-rate metadata alone is insufficient.

An evidence index points to UTF-8 JSON bound records stored inside the packet. Exact SHA-256 checks bind their bytes. Each record has one typed deterministic bound, exact rational value, validity interval, origin, dependencies and a review-receipt path. Units are strict: seconds are not silently accepted as milliseconds. Duplicate identities/roles, unresolved references, cycles, same-output-derived or model-assumption origins, insufficient bounds, missing bytes and unknown schema fields fail closed.

Review receipts bind the bound-record hash, profile, role, reviewer and scoped verdict. Their hashes must be present in a separately supplied trusted catalog. Different constructor/reviewer labels are necessary structural checks; they are not proof of independence. The catalog must be maintained by an external review authority after inspecting methods and underlying witness bytes. A caller who can invent both the packet and its trusted catalog can fabricate apparent structural readiness. This trust boundary is explicit; the checker supplies no cryptographic identity service or scientific verification.

Artifacts are embedded strings, not fetched or executed. Canonical relative paths reject traversal. The packet never executes evidence code. A receipt's claim that witness bytes were inspected must be authenticated by the external review process; the software does not retrieve or independently inspect those raw witness files.

## Software validation

The27 controls cover a complete synthetic packet; missing/duplicate records; wrong channels and kernel; changed artifact bytes; unapproved and constructor-only receipts; malformed rational/nonfinite/float/negative values; excessive tail and insufficient amplitude; wrong units/direction; incomplete time coverage; mismatched profile; same-output or model-only source; unknown/unanchored dependencies; self/two-node cycles; circular ancestor; statistical-only bounds; unsafe path; duplicate JSON keys. Tests rebind selected synthetic hashes/receipts where needed to exercise semantic gates beyond an easy hash mismatch. These are software tests, not physical trials or nonconstructor review.

Run `python3 build_and_test.py` to regenerate the fixtures, circuit disposition and TEST_RESULTS.json. Run `python3 admit.py CIRCUIT_PACKET.json EMPTY_TRUST_CATALOG.json` for the real-candidate structural check; HOLD intentionally exits2. The synthetic packet and catalog are visibly marked and must never be relabeled as empirical evidence.

## Circuit mapping and next step

The prior signed-trace content audit supports waveform availability and the nominal acquisition format. It does not establish the source TV bounds, global bandwidth, absolute amplitude floor, voltage-range calibration, deterministic noise/gain/baseline ceilings or0.2ns clock/skew requirement. The static notebook's nominal capacitor formula does not satisfy full energy or native support requirements. CIRCUIT_DISPOSITION.json records twelve missing reviewed roles and the unresolved apparatus binding.

Next prepare a concrete calibration/preparation protocol and blank receipt templates for these roles, with independent reference measurements, epoch/channel binding and uncertainty propagation. Prioritize feasibility of timing and tail-TV evidence before treating the existing dataset as admissible for this certificate. The evidence schema itself is a proposed review aid. No experiment is executed. Full energy, native support, primitive state clock, action anchor and EXIT-03 remain open.

A. CURRENT MISSION TRAJECTORY — Turn theorem assumptions into auditable experiment prerequisites.

B. WHAT WAS DONE — Portable evidence contract, fail-closed checker,27 software controls and scoped circuit HOLD disposition.

C. FINDING — Software can reject deficient records; physical truth and independent source/calibration evidence remain external gates.

D. UD GAP IMPACT — Requirements are operationally reviewable, without empirical admission or physical promotion.
