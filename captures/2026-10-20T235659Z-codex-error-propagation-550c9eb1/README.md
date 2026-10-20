# Error propagation needs decoder conformance and source bounds

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

For the unchanged PR307 weighted4096 half-step map, this capture propagates deterministic preparation, generator, readout, clock, noise, encoding and implementation errors. Rank1999/kernel641 and inverse amplification C=27648/61 are inherited and hash-pinned.

The normalized data envelope is

    D <= p + (X+p)b + nu + encoding,
    b <= rho_RMS + T_RMS*xi + (5+xi)*eta_RMS.

Here X bounds the full state amplitude, p the fixed preparation error, xi the skew generator perturbation, rho the readout operator error and eta the model-time error. T_RMS²=11180715/8. No independent or zero-mean noise is assumed. Coherent noise does not gain a1/sqrt4096 reduction. The preparation/readout and clock/generator mixed terms remain.

The ideal nominal inverse has observable-state error<=C*D. An implemented decoder instead needs independent operator bounds ||B||<=beta and ||BF−P||<=alpha over the full2640-state space, plus a numerical implementation bound. Its error is at most alphaX+betaD+algorithmerror. The good condition number alone does not establish those premises.

An exact two-coordinate counterexample has a unit trial frame, zero dynamics residual and a perfect forward right inverse, but its decoder adds a hidden component4/3 to a noiseless state. Thus the PR307 arbitrary-frame conditioning proof remains valid, while a decoder built from that frame still needs separate conformance to the orthogonal observable projection.

## Conditional arithmetic example — not admitted data

The explicitly declared control bounds in CONDITIONAL_ERROR_CONTRACT.json imply observable-chain error<2^-40<2^-39 by exact Fraction arithmetic. Every input-evidence receipt is missing and marked HOLD. No measured precision, noise tolerance, fresh acquisition or actual floating-estimator pass is claimed. The target is observable-chain Euclidean error, distinct from the older six-ratio q, port-residual and Hankel contracts.

Source calibration is made concrete: the selected ten tetrahedron boundary columns have Gram4I, so absolute weight errors supported there give exactly ||DeltaK||=2max|delta d|. Relative errors need the selected nominal weight3/2. The gain is a conditional mathematical identity; no physical weight law or measured weight uncertainty is supplied.

Small map error preserves conditioning on the nominal observable subspace when b<s. It does not preserve the entire actual kernel or full-positive condition number: tiny perturbations can expose very weak extra modes. The641 nominal hidden dimensions remain unreconstructable from nominal records.

## Checks and replay

```bash
python /absolute/UD/captures/CAPTURE_ID/compute.py --repo /absolute/UD --out /absolute/new-output
```

Replace CAPTURE_ID with this directory. The checker uses only the Python standard library, reads pinned parent files and source-complex JSON as data, checks all100 selected Gram entries, finite clock moments, a declared exact profile and eight logical countermodels. It outputs four byte-identical scientific JSON files on replay. It does not execute archived scripts or call an estimator/eigensolver/acquisition pipeline.

Separate same-team review independently derives the error lemmas, profile fractions, clock moments, source weight gains, decoder countermodel and continuity limitations. Final source/theorem hashes and replay are bound. This is not external promotion authority. Optional reviewer analysis is labeled separately from the root protocol and does not admit unsupported premises.

The next concrete implementation task is a nominal decoder with a verified full-space BF−P bound and arithmetic error, using matrix-free observation actions. Independently justified amplitude, preparation, timing, readout, generator, noise and encoding bounds remain necessary before physical use. No public-site/Project-board deployment or outreach is asserted.

Ledger v0.39/CRL-2; O03 controls are not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable and unused—please re-upload if needed. Notes/ASTER available unused. CI/merge/tracking receipts are reported separately.
