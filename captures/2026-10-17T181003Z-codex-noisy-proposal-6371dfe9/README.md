# Noisy-record proposal campaign — four full certificates passed

**Development — no registry entry. Constructor verification only. Independent review pending. Physical promotion 0.**

The frozen threshold is `9093197064441289377 / 604462909807314587353088`; the rank target1893 and condition cap2029 are unchanged. Exact outward dyadic bounds are preserved in each record certificate.

| Fresh noisy-record certificate | Count above threshold | Condition upper | Projection-tail upper |
|---|---:|---:|---:|
| Dense signs | 1893 | <747.128 | <6.470×10^-6 |
| Coherent DC offset | 1893 | <752.797 | <7.320×10^-6 |
| Rational ramp | 1893 | <724.387 | <2.932×10^-6 |
| Single-vector impulse | 1893 | <706.664 | <1.582×10^-8 |

All **75,160,616 readings** across these four records were checked by fresh exact/interval proofs. Two concurrent jobs completed the four proof stages in235.57seconds, with maximum worker RSS2091972KiB. The dense286.75-GiB Hankel matrix was not allocated. Timings are schedule-specific.

The revised proposer discovers105 temporal components in all five bounded-noise cases and the clean control. The strong out-of-budget control returns HOLD. The old proposer succeeds only on clean and coherent-DC discovery; its old spatial cutoff then inflates the DC candidate to1929directions.

An exact sketch-Gram theorem gives105 components above the noise-aware temporal cutoff throughout the entire additive vector-error ball. This is stronger than a finite campaign for temporal order alone; frequency fitting and final spectral certification retain separate checks.

The independent-review packet and unsigned template are in `noise-campaign/REVIEW_PACKET.md` and `REVIEW_TEMPLATE.json`. They record no completed independent review or CRL advancement.

# Noise-aware record-only extraction campaign

**Development — no registry entry. Physical promotion: 0. Independent review: pending.**

This version tests numerical proposal generation under exact, constructed additive noise. It preserves the original rank target 1893, exact selection threshold and condition cap 2029. It does not promote acquisition controls to theory constants, identify a physical generator or re-certify six-ratio/shape diagnostics.

## Construction and scope

The campaign specification was fixed by the constructor before generating its noise records. It is not independently reviewed preregistration. The baseline was already known constructed nominal data. Five bounded noise recipes are tested: a single-vector impulse, dense signs, coherent DC offsets, a rational ramp and an integer period-127 triangular clock. A clean control and an out-of-budget strong impulse complete the seven discovery cases.

Each bounded recipe satisfies the exact global62-vector ceiling `delta=1/1048576`. The dense, DC, ramp and periodic coordinate amplitudes are at most `1/8388608`. The single-vector impulse tests the global vector bound alone and exceeds the sufficient coordinate ceiling; full acquisition-sub-budget membership is not claimed. All records contain 18,790,154 encoded readings and are reproducible from fixed seeds and exact integer recipes.

The old relative temporal cutoff fails on several bounded records. It also exposes an indexing error in a diagnostic print when all160 sketch singular values exceed the cutoff. Coherent DC noise separately raises its proposed stationary rank from1 to37 and total real rank from1893 to1929. These are proposal failures; none establishes a spectral signature failure or hidden-state leakage.

## Repair

The new160-column sketch has entries `±1/64`. Its temporal cutoff is twice a deterministic noise envelope derived from the vector budget and the sketch Frobenius norm. An exact sketch Gram and validated160-dimensional eigensystem prove a uniform separation of105 temporal components over the complete additive vector-error ball. This is not a claim that the finite quantized record has exact algebraic temporal rank105.

A separate global real-rank allocation shares the frozen1893-dimensional approximation budget among modal blocks. Positive-frequency directions cost two real dimensions each. The allocation is an untrusted optimizer choice; acceptance still requires a complete record residual, both actual factor Grams and exact/interval spectral validation. Discarded nonzero modes remain included in the full temporal-frame error bound.

Four predeclared noisy records receive fresh proposals and complete proofs: dense signs, coherent DC offsets, ramp and single-vector impulse. The periodic-clock record is tested at discovery only; no fresh full certificate for its proposal is claimed here. Existing baseline perturbation bounds independently preserve its numeric signature when its exact vector-budget premise is applied.

## Reproduction and independent review

The package restores the baseline losslessly, regenerates the complete noise records, compares the old and new proposers, certifies uniform temporal separation, runs four fresh full-record proofs and executes regression fixtures. At most two full proof jobs run concurrently. Reported per-case times depend on this schedule and machine; they are not isolated performance comparisons.

Run `python replay.py NEW_DIRECTORY` at the package root. The directory must not exist. Raw records and large Gram intermediates are regenerated; their hashes and compact recipes are preserved in the archive. The learner and verifier load no nominal operator, preparation vectors, spectral roots or frozen modal data.

`REVIEW_PACKET.md` states the reviewer actions; `REVIEW_TEMPLATE.json` is unsigned and unassigned. Independent non-constructor review, custodian ruling, physical acquisition evidence and broader native-family proposal convergence remain open. Nothing was sent to an external reviewer.
