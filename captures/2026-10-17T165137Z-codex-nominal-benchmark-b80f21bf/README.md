# Frozen nominal pipeline benchmark — completed

**PASS, constructor verification; physical promotion 0; independent review pending.**

The frozen exact threshold is `9093197064441289377 / 604462909807314587353088`. The primary spectral bounds are exact outward dyadic pairs in `BENCHMARK_RESULT.json`; readable bounds follow.

| Quantity | Verified result |
|---|---:|
| Full scalar readings generated | 18,790,154 |
| Singular values above frozen threshold | 1,893 |
| Retained condition number | <706.570 |
| Complete discarded projection tail, Frobenius | <9.615×10^-14 |
| Smallest retained singular value | >0.00011935053 |
| Largest singular value | <0.084329461 |
| Complete sequential run | 152.8455 seconds |
| Peak worker RSS | 2,857,156 KiB (2.72480 GiB) |
| Twin factor-Gram payload | 57,335,184 bytes (54.68 MiB) |
| Dense Hankel storage avoided | 286.75 GiB |

Exact source moments, all preparations, direct phase enclosures, Cholesky/SVD residuals, complete record energy, both full-size probe actions, adjoint/direct-entry checks and dense small-case regressions passed. The encoded payload SHA-256 is `812ede167804a754f1e7343cc370cdc72a231d3f255a8656080e5cc7a2753ff7`.

This completes the **known-nominal spectral benchmark**. It uses temporal factor structure to form actual factor Grams; the generic candidate-basis adapter on unknown measured records remains open. The inherited 747-dimensional hidden subspace is not identified or monitored by this run.

# Frozen nominal Hankel benchmark, v0.2

Constructor verification only. Physical promotion: **0**. Independent review: pending.

This benchmark generates the nominal observation record from the pinned integer 600-cell operator, original 62-coordinate readout and 37 pinned preparations. It does not substitute identity Gram matrices, random matrices or artificial residual noise. All thresholds come from the frozen contract; the shape gate and diagnostic outputs have no role in the spectral tail test.

## Frozen object and method

The record is `Y[a,k,c]`, with 37 preparations, 8191 times `t=k/2`, and 62 history outputs. There are **18,790,154** scalar readings. The payload consists of little-endian signed int64 numerators, quantum `2^-48`, nearest ties-even. NPY files have a header; the recorded payload hash excludes that header.

The normalized matrix is

\[
H_{(i,c),(j,a)}=Y[a,i+j,c]/(4096\,2^{48}),\qquad 0\leq i,j<4096.
\]

Its shape is 253952 by 151552. A dense float64 copy would take **307,895,468,032 bytes = 286.75 GiB**. None is constructed.

1. Recompute every exact moment `R(-A²)^k S` and `RA(-A²)^k S`, `k=0,...,52`, from the actual sparse operator and sign matrix. Check the degree-53 annihilator on all preparations, isolate its 53 distinct real roots and verify the operator is skew symmetric.
2. Use its spectral projectors to reconstruct the stationary component and 52 positive-frequency pairs, with interval arithmetic at 512 bits. Round modal coefficients and direct trigonometric phases to dyadic rationals. Generate the complete encoded record through exact integer matrix products and ties-even quantization.
3. Factor each modal observation block as `Lλ Rλ*`, with a rigorously bounded residual, retaining a total of 1893 signed-mode directions. The selected ranks are a numerical construction choice; the residual bound, not that choice, justifies the discarded tail.
4. Write `H̃=F_L F_R*`, where the temporal vectors in the left factor use `exp(+iωj/2)/sqrt(M)` and those in the right factor use its conjugate. Construct the two **actual 1893 by 1893 factor Grams** using exact integer factor inner products and enclosed geometric sums. Convert conjugate pairs to real factors by `[f++f−,−i(f+−f−)]` on the left and half that transformation on the right. These are a structured nominal alternative to the generic candidate-basis Grams in the parent verifier; they are not claimed to be the same matrices.
5. Verify Cholesky and SVD proposals using exact integer matrix products, Frobenius residual bounds and polar corrections. Independently check all 240870 coefficient entries, 851864 nonstationary phase components and 5460 temporal pairs against uniform dyadic bounds. Recompute temporal and modal frame bounds directly by Gershgorin enclosures.
6. Evaluate the exact weighted energy of the encoded record, full-size `Hx` and `Hᵀz` on deterministic dense integer probes, their exact adjoint identity and 32 direct entries in each direction. Compare the energy with the factor-Gram trace and its error bound. Small dense regression cases separately check the factor identities and their singular spectra.

## Why the enclosures hold

For dyadic factor Grams `Ĝ_L,Ĝ_R`, let `γ_L,γ_R` include both Gram construction error and exact Cholesky residuals. With verified positive lower bounds `a_L,a_R` for the true Grams, the normalized factor defects satisfy

\[
\eta_L\leq\gamma_L/(a_L-\gamma_L),\qquad
\eta_R\leq\gamma_R/(a_R-\gamma_R).
\]

For the exact core `S=L_LᵀL_R`, verified proposed singular values `s_i` have an error enclosure `e`. Consequently,

\[
\sqrt{(1-\eta_L)(1-\eta_R)}(s_i-e)
\leq\sigma_i(\widetilde H)\leq
\sqrt{(1+\eta_L)(1+\eta_R)}(s_i+e).
\]

The uniform phase and coefficient checks give a scalar trajectory error at most `210·2^-60+2^-49`. Therefore its Hankel Frobenius error is at most `sqrt(37·62)` times that quantity. If `b` bounds the temporal Gram norm and `ε_modal` is the combined modal Frobenius residual, then

\[
\|H-\widetilde H\|_2\leq\|H-\widetilde H\|_F
\leq\delta=\delta_{trajectory}+b\varepsilon_{modal}.
\]

Weyl's inequality adds `±δ` to the core enclosures and yields `σ_1894(H)≤δ`. The Frobenius discarded tail is also at most `δ`: projecting onto the exact right factor's range annihilates `H̃(I−P)`, so `||H(I−P)||F≤δ`. The final certificate uses the **exact rational** threshold from the frozen contract. Bounds are also recorded as outward dyadic rational pairs; printed decimals are for reading.

The exact full-record energy is an independent consistency check. The final tail bound comes from the complete source-bound factor residual, rather than subtracting nearly equal floating-point energies.

## Scope and corrections

**DERIVED / constructor verified:** the complete known-nominal spectral calculation, encoded record hash, count above the frozen threshold, conditioning and tail, exact full-size probe actions, total energy and recorded resource usage.

**OPEN:** the generic model-free dense-candidate adapter on an independently acquired record; apparatus and calibration receipts over the acquisition horizon; independent review. This benchmark does not establish the six-ratio calibration or source-defined shape gate anew. It uses 62 history outputs, distinct from 189 diagnostic outputs and four additional six-ratio ports. It neither evaluates the rejected `2^-49` auxiliary gate nor reassigns `2^-38` to a Borel norm.

The nominal 747-dimensional unobservable invariant subspace is inherited from the frozen model. Its invisibility is a structural observer limitation, not evidence of quarantine measured during this computation. The benchmark does not identify hidden dynamics.

The supplied parallel script is a **NO-GO benchmark**: its two `5I` matrices do not derive from the record, it never performs a Hankel action, diagonal random noise is not a discarded projection tail, and its acceptance comparison reuses the unrelated shape gate. `2028.403` was a conditional sufficient ceiling in the parent method, not a previously observed condition number.

A first local draft used interval phase recurrence and a comparison of overlapping interval balls that could understate its error envelope. That draft's phase certificate is superseded. Version 0.2 evaluates phases directly and takes maxima of outward endpoints; a separate uniform-error checker verifies every phase. The fresh rerun reproduced the same encoded payload hash. No initial-draft bound is used in the final refined certificate.

## Reproduction

Install the pinned dependencies in `requirements.txt`. From the package root, execute `python replay.py NEW_DIRECTORY`. The destination must not exist. Replay copies only sources and scripts into an isolated directory, then runs `run_all.py`; it does not trust cached output files. Large record, Gram and SVD intermediates are regenerated locally. The package preserves compact dyadic factors, phases, hashes, interval certificates and logs; it does not need the 150-MB record or a dense Hankel file to preserve its definition.

Timing values are machine-specific numerical benchmark measurements, not physical acquisition times. `PIPELINE_BENCHMARK.json` gives one sequential run, including all verification stages, and the maximum child-process RSS. Resource usage includes exact matrix-product workspaces, beyond the 54.68-MiB pair of stored int64 Grams.
