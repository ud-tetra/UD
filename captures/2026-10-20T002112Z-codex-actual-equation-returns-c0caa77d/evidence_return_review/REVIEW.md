# Separate same-team review of the evidence-return requirements

**Disposition: PASS_REQUEST_STRUCTURE_AND_CONTENT_SCOPE_ONLY.** The packet is a concrete, UNSENT request and blank external-return form. It is not evidence, a calibration certificate, external attestation, authorization or physical admission. All128 original metadata paths remain unresolved; external scientific review is PENDING and Physical Promotion = 0.

This review concerns `/workspace/scratch/f3d1c2f040c9/evidence-return-20261020`. The reviewer is a separate agent on the same team, not the independent calibration authority, external scientific reviewer or custodian requested by the packet. Prior PR250/252/254 outcomes and source exposure were known. The16-check review plan was frozen before the packet existed; the inventory logic and exact producer inputs were frozen before its first execution. This is a disclosed, retrospective requirements review, not a blinded experiment or scientific preregistration.

## Coverage and meaningful content

The independent inventory audit matches all128 original blocker strings, in source order and without duplicate paths, to14 requested artifact roles. All10 original source bindings match their bytes and SHA-256. Every channel-index mapping is correct. The170 candidate null leaves are distinct bookkeeping and do not become170 scientific gates; the original128 paths are not claimed to be128 independent gates.

| Requirement | Finding and packet location |
|---|---|
| Authority and custody | R01/R02/R14 require actual accepted authority, identity/conflicts, devices/configuration, acquisition/domain and independent custody. Hashes establish byte identity rather than scientific truth. |
| Amplitude calibration | R03 requests actual gain/offset intervals, nonlinear/noise/quantization errors, covered input range and source-bound sample coverage for each real channel. |
| Timing | R04 and the guide require actual rate/origin/skew/jitter/crop conventions plus a derivative/band proof before translating time warp into voltage-vector error. Shared triggers are not shared clocks. |
| Transfer and aliasing | R05 requires actual passband/transfer/domain and in-band/out-of-band allowances. Nominal Nyquist labels and averaging flags do not supply these. |
| Joint coverage | R06 explicitly offers deterministic simultaneous enclosure OR justified statistical simultaneous coverage. Four common, one deterministic-only and three statistical-only paths are mapped accordingly; inactive-route N/A needs reviewed justification. |
| Computation | R07 distinguishes FFT/window/normalization/rounding and prediction-solver debits from acquisition, state and model uncertainty. Bin spacing is not frequency confidence. |
| Physical model | R08–R11 require equations/domains/units, complex link-amplitude dependence, physical realization and state/action/readout/quadratures, preparations, drive/feedback/loss, source-work/discrepancy and a justified comparator in the same observation coordinates. |
| Prospective analysis | R12 requires source/model/comparator/solver/precision/ties/failures/scores/margin rationale fixed before new fits or relevant outcome access, with retained HOLDs and no outcome-selected repair. |
| Fresh source | R13 preserves existing05-21/05-28 exposure and current05-28 retrospective scope. A filename, new hash or local lack of raw access does not establish independence. A genuinely unseen source needs independent custody/exposure review, its own domain and calibration coverage, and a pre-outcome freeze. |
| Blank return | Actual review identities, content hashes, commands/logs, verdict and custodian ruling remain null. R01–R13 are reviewed content; R14 is the completed statement, separately pinned after completion without self-hash or self-review recursion. |

The guide keeps the synthetic209-temporal/internal quantum, native62×37/1893 observable/747 hidden/189 diagnostic outputs, and published10-channel component lanes separate. It supplies no10→62 padding, kernel recovery or automatic physical realization. No internal2^-48 quantum, six-ratio2^-39 accuracy, native2^-38 shape statistic or rejected2^-49 residual gate becomes a voltage/SI tolerance.

The conditional propagation equations use triangle inequalities within error components and Euclidean geometry for disjoint coordinate blocks, without inventing stochastic independence. The clock inverse allocation includes its positivity conditions and avoids division by a zero derivative. Comparison-score intervals preserve separate observation, prediction/state/model and numerical debits. Both declared aggregateL2 and globalmax interval separation are required beyond an independently justified frozen margin; overlap means HOLD.

## Draft corrections and appended clarification

Three drafting issues were corrected before the producer's original freeze: joint-route applicability, compound-path secondary references, and the circular R14 receipt interpretation. Compound-path references now include feedback/loss, energy discrepancy and prediction/state/solver/error allocation rather than pointing only to one part of a combined requirement.

A later content question concerned the guide's spectral factor. The frozen guide did not spell out its FFT scaling. The producer preserved its frozen bytes and added `SPECTRAL_OPERATOR_ADDENDUM.md`, a separate source pin and addendum freeze. The pinned upstream lemma uses

\[
p_j=d_j|\operatorname{FFT}(WPv)_j|^2/(N\sum_nw_n^2),\quad
T=DRFWP,\quad F=\operatorname{FFT}/\sqrt N.
\]

Thus \(\|T\|_2\le\sqrt{2/\sum w_n^2}\max|w_n|\) follows by submultiplicativity. The addendum explicitly rejects applying this factor to an unscaled FFT amplitude and requires a new operator norm/debit for another convention. Its two file hashes and upstream source pin match; the original frozen files are unchanged. This resolves the presentation ambiguity without providing any missing physical calibration or validated numerical bound.

## Executed checks and limits

The independently frozen `audit_inventory.py` passed twice with byte-identical output. Its10 negative controls reject an omitted path, duplicate path, wrong channel, wrong role, wrong section, incorrect route applicability, premature content-verification flag, fabricated receipt identity, physical-promotion flag and omitted prediction crossreference. These are metadata mutations testing this inventory audit, not metrology, scientific estimator or actual apparatus tests. The packet's12 examples are hypothetical review dispositions, not received evidence.

`CONTENT_REVIEW.json` records all16 planned content checks and their specific locations. `ADDENDUM_REVIEW.json` records the operator/source review. No raw records, author code, new fits, external evidence URIs, outreach or hardware were accessed or executed. Neither same-team review nor successful inventory checks satisfy external nonconstructor scientific review, independent authority acceptance or a custodian ruling.
