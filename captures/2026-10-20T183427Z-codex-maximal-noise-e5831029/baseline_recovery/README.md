# Exact nominal baseline recovery for boundary campaign

Development — no registry entry; Physical Promotion=0; external promotion review PENDING.

This is one fresh execution of the byte-identical reviewed PR269 standalone recovery source, after scratch maintenance removed the prior raw baseline. It reconstructs the same computational nominal record, not new physical measurements. RECOVERY_PRECHECK.json freshly verifies every original repository/source/reference pin, exact formula and rounding identity, and absence of estimator or dynamic-code execution. The original source freeze is retained unchanged as source authority; its source_main field is the historical source anchor, not a claim about the current execution.

Only recover_baseline.py, RECOVERY_FREEZE.json and REFERENCE_PROPOSAL.npz were copied before execution. No old execution receipt was copied. The new RECOVERY_RECEIPT.json will be emitted exclusively by this new run. The raw is 150321232 bytes of little-endian int64, shape37x8191x62, made read-only after its SHA exactly matches25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59. Zero estimator calls, no archived code executed.

Repeat only in a new external directory with its parent containing ud-repo and the pinned repository sources. Run `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python recover_baseline.py`. Never overwrite prior evidence. The raw may remain external to Git capture; the explicit output inventory excludes it.
