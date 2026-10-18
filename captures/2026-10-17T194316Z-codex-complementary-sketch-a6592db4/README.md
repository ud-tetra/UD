# UD complementary-sketch return v0.1

This targeted engineering return appends `v/128` to the existing160-column
record-only discovery sketch, where `v` is the exact old blind witness. It
removes that direction from the sketch kernel:2134→2133. It uses existing
readings, leaves the original160 columns intact, and changes no full-Hankel
selection threshold, target1893 or condition cap2029. Physical promotion0;
development lane; constructor work; independent review pending.

The nominal62-channel dynamical observer's747-dimensional kernel is unchanged.
This sketch kernel is a different vector space. The new sketch still has2133
blind directions, and exposing a perturbation algebraically is distinct from
placing it above a discovery cutoff.

## Executed controls and uniform theorem

Five known constructor records were frozen before the new runs: clean,
bounded null impulse, bounded null alternating, oversized null alternating,
and dense signs. All are pinned by source hash. The new exact small-Gram
checker resolves105 components in four cases and106 in the oversized case.
The latter returns HOLD at the current proposer's model/order check; no
physical interpretation or true full-record spectrum failure follows.

The baseline exact-Gram certificate also proves a uniform statement: throughout
the declared per-vector2^-20 error ball, exactly105 temporal singular values
exceed the new discovery cutoff, with retained condition number<29.246.
This is the161-column temporal sketch's condition bound, not the1893-value
Hankel condition bound. THEOREMS.md gives the exact perturbation proof.

One new proposal (bounded impulse) is separately passed through the unchanged
full record-only verifier, with all18,790,154 readings checked. Its actual
spectral bounds and timing are in CAMPAIGN_RESULTS.json. No dense286.75-GiB
Hankel is allocated.

## Replay and limits

Python3.12; NumPy2.3.5; SciPy1.17.0; python-flint0.9.0.
Set `OPENBLAS_NUM_THREADS=1` for the recorded execution convention.
Run `python validate_campaign.py` for a portable replay of five supplied exact
161-by-161 Grams and their dyadic eigensystem proofs, hostile tests, source-freeze
checks and the full-certificate receipt checks. This does not regenerate raw
record-to-Gram products or repeat the large full spectral proof.

To repeat the raw calculations, regenerate the pinned records using the recipes
and baseline binding from the prior noisy and sketch-blind captures. Then use:

```
python certify_sketch.py RECORD.i64le NEW_SKETCH_OUTPUT
python propose_complementary.py RECORD.i64le inputs/FROZEN_CONTRACT.json NEW_PROPOSAL_OUTPUT
python certify_record.py RECORD.i64le inputs/FROZEN_CONTRACT.json NEW_PROPOSAL_OUTPUT/PROPOSAL.npz NEW_FULL_OUTPUT
```

Each output directory must be new. `run_campaign.py` records the sequential
campaign and preserves HOLD; it expects the original sibling record directories.
Raw records and the38-MB full factor Grams are omitted with exact hashes/sizes;
the five small exact sketch Grams, untrusted eigensystems and four generated
proposals are included. The full verifier regenerates its large factor Grams.

The witness stores only its320-coordinate prefix; the remaining1974 coordinates
are zero. A pre-freeze setup mistake assumed a full-length stored vector and was
corrected before record processing; the setup log and freeze note are retained.
No fitting retries or post-freeze algorithm changes occur in this campaign.
All these records and the old blind witness were previously known. This is not
independent data, blinded preregistration, independent review or full acquisition
admission. Universal fitting convergence, acquisition/metrology and independent
replay remain open under issues178,144,136,130; review HOLD177 is unchanged.

## Measured return

| Quantity | Result |
| --- | --- |
| Original → augmented sketch kernel | 2134 → 2133 |
| Uniform retained sketch count / condition | 105 / <29.246 |
| Known oversized control | 106 certified sketch components; proposer HOLD |
| Oversized proposal + exact discovery proof | 5.851 s observed, including subprocess overhead |
| Fresh positive full Hankel signature | 1893 above threshold; condition <706.635 |
| Full positive proof time | 108.563 s observed |
| Extra trajectory storage | 65528 bytes |
| Hostile proof checks | 4 pass |

Wall timings describe this development runtime, not a guaranteed speed ratio.
The full positive spectral bounds differ slightly because the new sketch yields
new fitted phases/coefficients; its frozen acceptance criteria are unchanged.
