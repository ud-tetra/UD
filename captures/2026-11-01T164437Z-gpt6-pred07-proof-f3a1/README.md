# UD PRED07 — Proof-first burden and sector-action development v1.0

This reproducible **mathematical** package answers two authorized workloads: an added conservative K4 burden instability and a metric/sector-action source audit. It contains three scoped theorem proofs. Software and CI are supporting verification only.

## Proof milestones

- `UD-PM-PRED07-BUR-001`: K4 nonlinear conservative burden amplifier, exact instability threshold, strict ordering and no endogenous selection from exact symmetry.
- `UD-PM-PRED07-MET-002`: independent S4-invariant cochain metric family even at unit edge-basis norms.
- `UD-PM-PRED07-ACT-003`: a gauge-invariant period-squared sector term exists; its coefficient and integer lift are unprovided assumptions.

## Replay

```bash
python pred07_exact_audit.py
python independent_exact_check.py
python pred07_numerical_controls.py
python -m unittest discover -v -p 'test_pred07_proofs.py'
```

Uses SymPy, NumPy and SciPy. Exact proofs are contained in the milestone `.md` files and do **not** depend on the numerical simulator. Tests cover their finite algebraic witnesses, not the validity of their physical interpretation.

## Governance

D0 development; review deferred; physical promotion 0. Source references: dated UD coefficient ledger v0.39 Q153/Q162/Q169/G05, PRED06 source audit PR #490 and PRED05 scaling PR #487. Revisions and hashes recorded in MANIFEST.json and RECEIPT.json. This package is not a source-complete law, not a measured physical prediction and not an accepted mainline theorem until applicable review/integration gates are satisfied.
