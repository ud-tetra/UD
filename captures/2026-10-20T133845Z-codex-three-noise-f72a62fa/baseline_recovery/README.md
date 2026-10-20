# Baseline-only deterministic recovery

Development — no registry entry. Physical Promotion=0; external promotion review PENDING.

The scratch reset removed the previously shared nominal baseline. `recover_baseline.py` reconstructs exactly one existing computational record, `ramp_clock_stress.i64le`, using the reviewed PR195 timing-waveform formulas and a data-only NPZ member from the pinned source archive. It imports no estimator or proposer and makes zero fit calls. This is raw recovery, not a fresh measurement or a new benchmark case.

`RECOVERY_FREEZE.json` pins the script, source files and archive, reference data, and expected original generation row before execution. `FORMULA_IDENTITY_REVIEW.json` checks the phase/timing/recurrence/evaluation functions and rounding function are byte-identical to their reviewed sources; `STATIC_SCOPE_REVIEW.json` records the limited code scope. `RECOVERY_RECEIPT.json` is emitted only after the full 150321232-byte record, all18790154 scalar ranges and original generation row agree. Source-aware reconstruction does not independently establish physical source premises.

The raw file is made read-only after success and may remain external to Git capture; its exact expected SHA256 is25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59. Replay in a new directory using Python/NumPy/python-flint versions recorded in the receipt, the pinned `REFERENCE_PROPOSAL.npz`, and the same repository sources. Never overwrite an earlier record or re-use one-shot benchmark invocation files.
