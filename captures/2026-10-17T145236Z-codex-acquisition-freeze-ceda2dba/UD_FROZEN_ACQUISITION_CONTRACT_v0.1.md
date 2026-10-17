# UD frozen acquisition contract v0.1

RESULT / STATUS: **CONSTRUCTOR-FROZEN PROPOSAL**, conditional mathematics checked. Development — no registry entry. Independent review pending; physical promotion **0**. No apparatus experiment, independent review or empirical pass is claimed.

The 4,096-axis-sample acquisition option now has an exact machine-readable contract, fixed preparations and channel order, separate precision formats for history and diagnostics, an empty run-receipt template, a record auditor and adversarial checks. This is a concrete review packet. It is not a declaration that the experiment is ready to execute on hardware.

## Frozen primary operating point

| Item | Contract |
|---|---|
| Observer | Original real 62-channel vertex-link coordinate selector |
| Preparations | Frozen 37 columns of ±1/52; each norm squared 165/169 |
| Axis window M | 4,096 |
| Raw timestamps per preparation | 8,191 |
| Total 62-vector records | 303,067 |
| History scalar readings | 18,790,154 |
| Normalized sample interval | 1/2 |
| Normalized final time | 4,095 |
| Additive error per complete 62-vector | At most 2^-20 |
| Sufficient additive error per scalar | At most 2^-23 |
| Target retained signal count | 1,893 |
| Retained condition-number strict upper bound | 2,029, including the declared numerical reserve |
| Original nominal dynamical kernel | 747 dimensions; unchanged |

The contract hash is recorded in `FREEZE_CERTIFICATE.json` and binds the canonical bytes of `FROZEN_CONTRACT.json`. Every run must cite that exact hash. Changing its window, rank target, tolerances, ordering or processing rules creates a new protocol version and a new run. The smaller-count options from the parent noise staircase are not permitted as post hoc fallbacks for this run.

## Coordinate and ordering closure

The proposed reference centre is the previously declared candidate

\[
Q=\operatorname{diag}_{\rm grade}(1,65/64,33/32,67/64),
\quad c=33/32,\quad K_*=cQ^{-1}AQ.
\]

Use raw preparations Q^-1 X, correct each selected raw readout by its grade-Q factor, and sample at raw model interval 1/(2c) = 16/33. The last raw model time is 43680/11. These are model-coordinate conversions, not a derivation of seconds or volts. A hardware/SI transfer remains OPEN.

`CHANNEL_ORDER.csv` lists each zero-based readout coordinate, grade and correction factor. The 62 selected coordinates contain 12 vertices, 30 edges and 20 faces. `PREPARATION_ORDER.csv` hashes each signed preparation column. `BASE_PREPARATIONS.npz` and `OPERATORS.npz` are included as frozen source inputs. The builder re-derives the SHAKE256 signs from the recorded domain and checks all 14,880 sparse generator entries are ±1 with A+A^T = 0. It does not regenerate the 600-cell topology or independently repeat its modal projector proof.

The six-ratio protocol uses the labeled order **D1,U1,D2,U2,D3,U3**. At the reference centre the ratios are

\[
(2145/2048,\;66/65,\;1089/1040,\;65/64,\;67/64,\;1089/1072).
\]

These are checked against the six-ratio source. The parent fitted-family certificate stores its directed-ratio array in a different order. Arrays must therefore be joined by their labels, not by position. The six-ratio protocol also needs four auxiliary ports beyond the original shell: coordinates 1,133,878,2040. The diagnostic phase uses its larger 189-channel readout. Neither phase is silently supplied by the later 62-channel history observer.

## Three distinct measurement stages

| Stage | Known scalar readings | Precision/control |
|---|---:|---|
| Six-ratio calibration | 12 | Original source preparation, gain, logger and feature-computation bounds; final ratio-vector error strictly below 2^-39 |
| Restricted-family diagnostics | 493,290 | Recommended m4 protocol, h=1/256, total response error at most 2^-58, source shape gate retained |
| History acquisition | 18,790,154 | Per-62-vector additive error at most 2^-20, plus separate preparation, model, readout and timing budgets |
| Known total | **19,283,456** | Excludes extra metrology, independent held-out validation, additional drift tracking, repeats and rejected runs |

The order in the physical campaign must preserve the inherited dependency requirements. A review should check whether six-ratio and diagnostic processing need an iterative preflight schedule; this packet does not infer missing model membership from either stage alone. Their bounds and final receipts must be established before interpreting the history result. Two diagnostic epochs do not certify arbitrary later stability.

The six-ratio source contains a stronger historical intermediate margin. The recommended diagnostic variant has already relaxed that extra margin; this contract retains the **2^-39 final ratio gate**, not an unproved promise of 2^-40 under the revised diagnostic budget. `PARENT_TRADEOFF_CERTIFICATE.json` supplies the applicable composite bound. The source six-ratio document remains evidence for its finite design and primitive precision requirements.

## Concrete additive-error allocation

Each history scalar has the following normalized absolute-error allowance:

| Contribution | Ceiling |
|---|---:|
| Instrument acquisition | 2^-24 |
| Blank/drift correction | 2^-25 |
| Processing and unit conversion | 2^-26 |
| Fixed-point quantization | 2^-49 |

The sum is exactly 58720257/562949953421312, below 2^-23. Multiplying that sum by sqrt(62) stays below 2^-20. This is deterministic triangle-inequality accounting: no independent noise, Gaussian tail or statistical averaging assumption is used. Quantization does not establish the instrument, correction or processing bounds; those need separate evidence.

History preparation error remains at most 2^-25 in normalized state norm. Origin error and jitter are each at most 2^-29 in normalized time. The raw sufficient preparation allowance is (64/67)2^-25 and each raw timing allowance is (32/33)2^-29. Metric, native-rate and readout bounds are the exact outward dyadic ceilings inherited from the recommended restricted-pass model certificate. J=0 remains a fault-family assumption. A constant common scale within 1±1/1024 is allowed; arbitrary time-varying clock/rate error is not.

Every bound is typed by its norm and coordinate units in the contract. The run template preserves those types. The auditor rejects replacing a per-scalar bound with the much larger vector allowance, even if the same number appears elsewhere in the project. These tolerances remain protocol controls under ledger O03.

## Precision formats

**History:** `normalized_history.i64le` contains exactly 150,321,232 bytes: signed little-endian 64-bit integers in C-order shape [37,8191,62], scaled by 2^-48. Round to nearest with ties to even; retain the raw source. Do not clip, fill missing data or delete rejected samples. The one-scalar quantization error is at most 2^-49. This is about 143.36 MiB, excluding indexes and raw data.

**Diagnostic and calibration precision:** the history format is too coarse for diagnostics at 2^-58. Their proposed transport format uses arbitrary-precision integer numerator strings at denominator 2^64; its quantization contribution is at most 2^-65. Include that contribution inside the total computation allowance, rather than adding it beyond an already exhausted budget. Do not convert the scaled numerator through binary64 or signed int64: even the value 1 has scaled numerator 2^64. The original six-ratio solver and primitive precision contract remain binding. `exact_encoding.py` implements exact rational rounding for both formats.

**Coverage:** `sample_index.csv` has 303,067 rows with zero-based preparation index, time index and globally unique raw record ID, in the same order as the binary record. Actual timestamps stay in the raw record, covered by separate clock receipts. Hashes bind the normalized file, index, raw source and processing implementation. Hash consistency detects byte changes; it does not authenticate an instrument, reviewer or claimed error bound.

## Numerical analysis reserve and finite signature

The parent modal and temporal certificates imply nominal smallest-positive squared singular bound s² and largest bound S². Let β² be the inherited total model-plus-history-error bound for this operating point. The builder rounds B ≥ sqrt(β²) upward to an exact 80-bit dyadic and freezes

\[
T=2B,\qquad \epsilon_{\rm alg}=B/4096.
\]

Display values are B ≈ 7.5217163×10^-6, T ≈ 1.5043433×10^-5 and ε_alg ≈ 1.8363565×10^-9. Gates use the exact fractions in JSON, not these decimals. This ε_alg is the operator-norm error of the later numerical matrix/solver approximation. It is additional to data-value processing and quantization errors already counted in the observation record.

For a computed matrix Htilde with ||Htilde−H_data|| ≤ ε_alg, Weyl's inequality and the source bounds give

\[
\sigma_{1893}(\widetilde H)\ge s-B-\epsilon_{\rm alg},\qquad
\sigma_{1894}(\widetilde H)\le B+\epsilon_{\rm alg},\qquad
\sigma_1(\widetilde H)\le S+B+\epsilon_{\rm alg}.
\]

The frozen outward rational bounds put the first of these strictly above T, the second strictly below T, and bound the ratio of largest to retained-smallest singular values below 2,029. The calculated rational ratio is about 2028.27294. Thus the numerical reserve preserves the earlier target. These are conditional predictions of the finite observer contract, not independent evidence that the plant belongs to the declared family.

The Hankel shape is 253952×151552. Storing it densely in binary64 would require exactly 307,895,468,032 bytes, or **286.75 GiB**, before SVD workspace. This packet does not implement a validated full-size spectral solver. It requires either an implementation that applies the matrix without storing it in full and certifies the operator/solver error, or directly verified singular-value enclosures. An ordinary SVD tolerance, convergence flag or randomized rank estimate does not fill that proof slot.

`evaluate_declared_intervals` checks the arithmetic consequences of externally valid enclosures for σ1,σ1893,σ1894. It reports conditional consistency, conditional contradiction or inconclusive. The function does not validate the enclosures themselves. A tie with the selection threshold is inconclusive; no rounding or tolerance override is allowed after looking at the outcome.

## Execution and review states

The empty template intentionally returns **NOT_EXECUTED**, with missing receipts listed. Structural completeness can establish that declared fields, units, hashes and record coverage are consistent. It cannot establish the truth of referenced evidence. Even a completely filled synthetic receipt with a forged proof hash remains **HOLD_PENDING_EVIDENCE_AND_PROOF_REVIEW**, never an empirical pass. A failed integrity or budget gate rejects the corresponding record contract. A trustworthy spectral contradiction would reject at least one declared model or error assumption; it would not uniquely diagnose hidden bulk phase leakage.

Independent review must examine the inherited modal and diagnostic dependencies, reference transfer, clock/gain identification, full-run stability, bounded-error metrology and the numerical certificate. `INDEPENDENT_REVIEW_FORM.md` is blank and keyed to the frozen hash. There has been no reviewer outreach or simulated review. Constructor freezing does not qualify as pre-registration under the attached CRL2 governance proposal, which is retained as a proposal rather than silently adopted.

## Verification and remaining boundary

Fresh-directory replay reproduces the contract, proof certificate, receipt template and two order files byte for byte. Thirteen adversarial checks cover frozen-hash/target changes, unit and scalar/vector substitution, strict ratio equality, incomplete/reused indexes, altered/truncated data, signed-integer range overflow, fake evidence references, spectral boundary ambiguity, conditional tail contradiction, exact quantization and the reserved numerical gap. All pass. The inherited modal diagonalizations and diagnostic campaigns were not rerun. No physical data were generated or evaluated.

The primary open analysis task is a validated large-matrix spectral computation that meets ε_alg without dense allocation. Hardware/SI mapping, instrument receipts and non-constructor review also remain open. No result here reconstructs the 747-dimensional nominal unobservable space, transfers the proof to F13, identifies the full plant, derives a physical clock or promotes a physical law.

Next recommended step — priority **98/100**: implement and certify the computation needed to evaluate the frozen spectral signature without materializing the full Hankel matrix, then submit this exact version for non-constructor review. Do not change the threshold to accommodate the eventual data.
