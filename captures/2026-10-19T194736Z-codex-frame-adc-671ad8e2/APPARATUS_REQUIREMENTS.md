# Actual-byte apparatus evidence adapter

Development — no registry entry. Physical Promotion=0; external review PENDING. This is a numerical evidence adapter, not hardware metrology or an external review certificate.

The command requires a caller-pinned CONTRACT.json hash, PACKET.json, calibration JSON and three binary files. Raw ADC and saved prediction use signed little-endian64-bit entries in preparation/time/channel order; timestamps use one signed64-bit tick per62-vector. Exact file lengths, hashes and frozen dimensions are enforced. Hashes of the actual bytes consumed by the numerical loop are checked, as are file snapshots and metadata. The saved prediction has one fixed positive integer denominator. No supplied residual value is trusted.

The contract pins the calibration/prediction hashes, cap, model-coordinate/time units, source IDs and declared raw ancestors, nominal tick schedule, clock-error treatment and chronology before acquisition. The calibration supplies a bijective62-channel map, sign, positive applied decoder gain, offset, ADC rails, independently justified amplitude/derivative envelopes, deterministic gain/offset/ADC/processing/nonlinearity/crosstalk/filter-tail bounds, timebase bounds and validity interval. Calibrator and constructor identities must be declared distinct. This does not authenticate either identity or the calibration's truth. Declared lineage IDs and raw ancestor hashes are checked for overlap; completeness/independence of that lineage is NOT_CERTIFIED.

For z=g*y+b+n and decoder yhat=sign*(z−bhat)/ghat, the deterministic scalar error is

base_c=(dg_c*A_c+db_c+adc_c)/ghat_c+processing_c+nonlinearity_c+crosstalk_c+filtertail_c.

All terms require independent validity over the stated run domain. An observed amplitude/domain consistency check cannot prove that calibration premise. The common vector timing error is |tick−nominaltick|*scale+originerror+|tick|*rateerror+jitter+timestampquantization+channelskew, with the calibration origin at tick0 and scale>rateerror>=0. Strict timestamp order is required within each preparation. The clock may be preparation specific through the nominal origins; unmodeled per-channel timing differences require the skew allowance.

If timing is declared acquisition uncertainty, e_c(v)=base_c+L_c*dt_v. Otherwise timing departures remain in the tested model mismatch and are not subtracted as acquisition noise. With nonnegative terms,

alpha_F²=Nvec*sum_c base_c²+2(sum_c base_c*L_c)*sum_v dt_v+(sum_c L_c²)*sum_v dt_v².

This polynomial is evaluated exactly as rational arithmetic. Disjoint deterministic components add, without an independence or quadrature assumption. Euclidean aggregation is only across coordinates/vectors of the displayed pointwise error bound. Preparation implementation deviations are part of model mismatch in this adapter; no extra preparation-noise credit is silently granted.

For each channel, the exact affine decoder and saved predictor are put over a common integer denominator. Python integers accumulate squared residual numerators without64-bit overflow. Only62 sums and one vector at a time are retained. The raw Frobenius residual squared and alpha² are exact fractions;512-bit Arb gives outward norm/mismatch bounds. Upper<=the predata cap means CONDITIONAL_CONSISTENCY; lower>cap means CONTRACT_CONTRADICTION for the collection of declared assumptions; overlap gives HOLD. Missing/malformed/invalid evidence gives HOLD_INPUT_EVIDENCE before acceptance.

The mismatch target is the frozen saved predictor artifact. A separately justified analytic prediction/truncation error is needed to transfer that result to an ideal continuous source. No such transfer is made. There is no2^-49 residual gate, no reassignment of the2^-38 shape gate, no1893-rank/747-hidden-state inference and no full Hankel allocation.

An optional declared frequency band with width<pi is mathematically injective for the two-step phase map, but evidence IDs alone do not establish actual signal membership, filter rejection or SI frequency identification. The adapter therefore returns unaliased_identification=NOT_CERTIFIED even when its raw-residual arithmetic is consistent. It also returns heldout_independence=NOT_CERTIFIED and physical_verdict=HOLD_UNQUALIFIED for ALL inputs, including an invented complete apparatus packet. These outcomes cannot be changed by a checked boolean or a receipt hash.

All included byte bundles are tiny synthetic controls, including one deliberately labeled apparatus_submission to test refusal of physical promotion. No actual instrument record or independent calibration was provided. Real use requires the explicitly frozen actual cap, independently authenticated calibration/source/timing/lineage evidence and the external-review/custodian process. Blank real templates remain HOLD; no source-family209 membership or physical precision is claimed.
