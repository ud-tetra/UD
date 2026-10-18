# Wider-sketch diagnosis of the preparation-clock HOLD

Development — no registry entry. Physical promotion **0**; independent review pending.

The larger PR195 timing record saturated the 161-column sketch. A frozen nested
extension now certifies additional signal directions without changing those
old columns or rewriting the original HOLD.

| Existing record | Width | Count at common cutoff | Count at noise-scaled cutoff |
| --- | ---: | ---: | ---: |
| Small joint clocks | 161 | 105 | 105 |
| Small joint clocks | 257 | 105 | 105 |
| Small joint clocks | 321 | 105 | 105 |
| Larger clock control | 161 | 161 (saturated) | 161 (saturated) |
| Larger clock control | 257 | 202 | 200 |
| Larger clock control | 321 | **205** | **204** |

The common cutoff is the exact parent dyadic, approximately 0.0099945479322.
The scaled cutoffs are approximately 0.0126162731959 at width 257 and
0.0140957413193 at width 321; their squared values are exact rational controls.
Scaling preserves the parent's threshold/noise-envelope ratio for the wider
sketch. It does not admit this stress record into the original acquisition
contract. Both rules were frozen before these executions; no outcomes were
used to choose widths, seeds or thresholds.

At width 321, the larger control has retained condition <421.439 for 205 values
at the common cutoff, or <378.019 for 204 values at the scaled cutoff. The small
clock record's 105-value condition improves from <27.968 to <15.687 in these
particular sketches. These are bounds for the mathematical encoded sketch,
not full-Hankel conditioning or an optimal sketch comparison.

## Structural finding

Two rate classes with alternating jitter have a comparison waveform span of
at most 209 real dimensions. Their tied sidebands can require a one-step shift
closure of at most 417 dimensions. These are upper bounds, not proven exact
dimensions. Two-step shifts preserve the smaller waveform family exactly.

The 205-value lower certificate and source evaluation bound place the comparison
model rank in **[205,209]**. Encoded rounding can add tiny algebraic directions:
at width 321, sigma210 of the encoded sketch is **<1.034e-10** by the source
model tail bound. This does not assert exact encoded rank 209 or all 209 signal
coordinates being recoverable.

## Checks completed

- Exact integer projections read all 37,580,308 coordinates of the two existing
  records. Separate full raw-projection replays reproduce both 321-by321 Grams.
- Validated eigenvalue enclosures classify every value for all six case/width
  combinations and both frozen cutoff rules. Untrusted floating eigensystems
  are checked through exact integer orthogonality and eigenpair residuals.
- Complete small-Gram replays agree; five tests pass. No full Hankel allocated.

The result concerns the EXACT mathematical sketch of encoded bytes. It does
not certify a separate floating BLAS sketch or new actual phase outputs.
The PR195 phase certificates and stress model/order HOLD retain their scope.

## Portable replay

Extract the ZIP into an empty folder, install requirements.txt, then run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

This checks all package hashes, recomputes the six small-Gram spectral proofs
and source-tail bounds, preserves all count/HOLD outcomes and runs five tests.
It does not regenerate raw records, reproject them or rerun a phase estimator.

For separate full raw projection replay, first regenerate the source records
using the PR195 package's make_records.py --destination option. Check the raw
hashes in WIDE_FREEZE.json, then from this package run:

```bash
OPENBLAS_NUM_THREADS=1 python project.py ramp_joint_clocks --records /path/to/regenerated/records --replay
OPENBLAS_NUM_THREADS=1 python project.py ramp_clock_stress --records /path/to/regenerated/records --replay
```

Use a fresh extracted copy without existing PROJECTION_REPLAY.json receipts;
never overwrite evidence. Both exact projections were separately rerun in
this return. THEOREMS.md proves the mode/threshold/Gram bounds; RESULT_SUMMARY.json
and per-case certificates provide rational values.

Next bounded work is a separately frozen stride-two phase adapter with sampled
collision, excitation, finite-conditioning and actual-output checks. This
return closes a sketch-saturation diagnostic, not independent review, global
fitter convergence, full acquisition qualification, SI clocks, the native
observer/metric source, full-Hankel acceptance or hidden-state recovery.
The nominal 747-dimensional dynamical observer kernel is unchanged.
