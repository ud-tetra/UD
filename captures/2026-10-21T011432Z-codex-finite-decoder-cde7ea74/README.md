# Finite matrix-free decoding with verified projection and error bounds

Development — no registry entry. External promotion review PENDING; Physical Promotion=0.

For the unchanged PR307 weighted4096 half-step observation map F, the inherited singular interval is [61/27648,1], with rank1999/kernel641. This capture constructs B=h(F^T F)F^T using a finite8192-degree Chebyshev residual polynomial. It proves the whole-state bound ||BF−P||<2^-51 and ||B||<512, where P is the nominal orthogonal observable projection. The earlier arbitrary-frame inverse counterexample remains valid; this construction uses the exact adjoint range instead.

The recurrence requires one adjoint and8191 normal actions, or16383 forward/adjoint calls when normal actions are composed. It stores vectors and coefficient enclosures rather than F, F^TF, P or a full Hankel matrix. Actual600-cell runtime has not been benchmarked.

The full-space error proof includes hidden-direction arithmetic and action errors. Under the declared absolute action contracts and whole-update error budget2^-67, the implementation error is below11*2^-46<2^-42. Sufficient factored forward/adjoint errors are2^-68 absolute on state ball2048 and data ball2049 respectively. These are explicit obligations, not certified facts about an actual600-cell implementation.

## Executed checks

The standard-library checker verifies30 exact scalar identities, zero-mode limits, constants and the8192-degree integer-power inequality. The executable reference uses Arb192 coefficient balls, exact dyadic96 vectors and certified whole-coordinate rounding. Three full8192-step rational four-state proxy cases pass, including a rotated hidden subspace, inconsistent data and coherent hidden oracle errors. Independent exact action audits and adversarial rejection controls pass. Separate same-team review independently reproduces all three outputs with an algebraically regrouped recurrence. Five scientific JSON files replay byte-identically.

The generic weak-mode proxy has state amplitude about453; it validates the declared data-ball2 domain. It is distinct from the earlier illustrative X<=1 profile. Substituting that profile's D<2^-50 and the new obligations implies observable-chain error<2^-40. All physical/input premises and actual600-cell action contracts remain UNSUPPLIED/HOLD. The641 hidden components are not recovered.

## Replay

```bash
python /absolute/capture/certify.py --repo /absolute/UD --out /absolute/new-math-output
python /absolute/capture/reference_tests.py --decoder /absolute/capture/decoder.py --out /absolute/new-reference-output
```

The first command uses the Python standard library and reads pinned parent JSON/theorem bytes as data. The second explicitly runs the new reference module and requires python-flint. Neither command runs the actual600-cell decoder or executes archived acquisition scripts. Reference output binds decoder bytes, so use the captured decoder unchanged.

Next: implement and certify true weighted600-cell F/F^T actions on the required domains, then run this decoder on the frozen full problem. An opaque callback or successful small proxy cannot establish that certificate. No physical experiment, fresh preparation, calibration gate, public-site deployment or Project-board update is asserted here.

Ledger v0.39/CRL-2; O03 controls are not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable and unused—please re-upload if needed. Notes/ASTER available unused. CI/merge/tracking receipts reported separately.
