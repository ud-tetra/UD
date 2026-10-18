# UD exact residual-preflight return v0.1

An append-only optimization of the record-only numeric spectral verifier.
The frozen target 1893, threshold T and condition cap 2029 are unchanged.
The original spectral proof module is byte-identical. Physical promotion 0;
constructor execution, independent review pending; no registry entry.

The gate stops a particular proposal's proof attempt only when an exact
reverse-triangle residual lower bound exceeds T. It does not decide the true
record spectrum or exclude successful alternative proposals. See THEOREMS.md.

## Replay

Python 3.12, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0; one BLAS thread.
Run `python -m unittest -v test_preflight` and `python validate_return.py`.
The archived residual comparison in RECEIPT_REPLAY.json covers eight existing
certificates; this is explicitly not eight fresh all-readings executions.
`replay_receipts.py` regenerates it against the original sibling work directories.
`validate_return.py` rechecks its exact gates portably from the included receipts.

Two new completed all-readings execution classes are included: the oversized
sketch-blind alternating control (early HOLD) and the bounded impulse control
(full positive spectral proof). Exact source records/proposals are pinned by hash.
Reuse the previous sketch-blind audit's `make_records.py`, frozen baseline and
proposer to regenerate these binary inputs; both proposals are also included in
this package. No nominal dynamical operator or modes enter this verifier.

Example, replacing paths with regenerated inputs and choosing a new output dir:

```
OPENBLAS_NUM_THREADS=1 python certify_record.py RECORD.i64le inputs/FROZEN_CONTRACT.json inputs/PROPOSAL.npz OUTPUT
```

Raw record files and the large full factor Grams are omitted; omission hashes and
sizes are retained. The new full positive proof regenerates its factor Grams.
The dense 286.75-GiB Hankel is never allocated.

The old/new timing comparison is an observed development benchmark, not a
hardware-independent performance guarantee. All attempts, including the first
briefly overlapping control execution, are recorded in BENCHMARK_COMPARISON.json.
Frozen acquisition, calibration, metrology and independent-replay obligations
remain open under issues #178, #144, #136 and #130; review HOLD #177 is unchanged.

## Executed return

| Check | Result |
| --- | --- |
| Exact boundary/invalid-input tests | 7 pass |
| Archived exact residual comparisons | 8 preserve composed status; receipt-only replay |
| Fresh full positive proof | Certificate and residual byte-identical to parent |
| Fresh early-HOLD executions | 3 completed, all HOLD; repeated controls retained |
| Isolated optimized oversized control | 29.871 s; 439,948 KiB peak RSS |
| Historical full oversized control | 108.517 s; 2,090,928 KiB peak RSS |
| Observed difference | 78.646 s saved, 72.47% wall reduction |
| Dense Hankel allocation | None |

The isolated negative run's exact proposal-residual lower bound is approximately
0.0216354, above T approximately 0.0000150434. Its spectrum was not computed.
The positive run took 107.852 s; its retained condition bound remains <706.635.
All four new completed runs checked 75,160,616 scalar readings including repeats.
The output directory with suffix `_serial` is a retained historical attempt name:
it briefly overlapped the end of the positive control and is not the isolated
comparison. The `_isolated` run began after both other workers completed.
