# Issue draft · Alpha-specific nuclear bridge acceptance criteria

**Physical Promotion = 0.** The PB4 identification remains a candidate structural analogue. This issue records the acceptance criteria before target-facing nuclear modeling resumes.

## Decision sought

Does the pinned framework select an alpha-specific state and produce a discriminating nuclear observable from its native operators? The baseline includes the even-ring rank defect and exterior memory benchmark in [PR #607](https://github.com/ud-tetra/UD/pull/607). Both parity and threshold outcomes occur in comparison carriers.

## Acceptance criteria

- [ ] **Endogenous state selection.** Freeze the state space, inner product, admissible carriers, symmetries, and algebraic selection rule. Show which orbit of states it selects on PB4 and compare the same rule on PB3, PB5, PB6, and a size-matched admissible four-cell control. Document degeneracies and tie handling. Define the candidate proton and neutron inputs separately.
- [ ] **Endogenous binding functional.** Derive the native Hamiltonian or energy functional with the same conventions for bound and separated states. Show a positive defect $2E_p+2E_n-E_{\rm PB4}$ against the registered breakup channels and verify that the result depends on the endogenous generator. Record the reference energy and any unit or dimensionless observable map. The known helium-4 binding-energy figure is exposed and cannot serve as a target-blind test.
- [ ] **Frozen discriminating prediction.** Before inspecting the holdout, record the observable, preparation and selection rule, reference controls, map to measurement, uncertainties, tolerance, and rejection condition. Use a holdout whose relevant values are masked during derivation. Freeze the source commit, data split, replay, and prediction. Require an independent reviewer to replay the native result and evaluate the discriminating test against the registered alternatives.

## Disposition

An ambiguous selection, an energy that depends on target-based calibration, or a prediction shared by the controls keeps the correspondence open. Any future physical promotion requires a separate governance decision with the recorded test result.
