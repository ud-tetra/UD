# Released sliding constraints: stationary references

Development — no registry entry. Physical promotion 0. Constructor: Codex; non-constructor reviewers: none.

All four searches satisfy stationarity after releasing relative-layer lateral motion. Four lower-energy endpoints were found from one declared positive0.05Å relative-x seed per reference. This is a local search, not a global-minimum claim. Two endpoints fail the frozen derivative preflight at the carbon angular knot cos(theta)=-1/2; they remain HOLD and received no force stencils. A scheduler-only amendment permits the independently eligible two cases to proceed under unchanged thresholds.

| Reference | max projected force (eV/Å) | energy change (eV/supercell) | min full stiffness (eV/Å²) | status |
|---|---:|---:|---:|---|
| 21_dir_0 | 2.83e-12 | -0.047283193 | unqualified | HOLD_PREFLIGHT |
| 21_dir_10024 | 2.015e-12 | -0.0403121868 | unqualified | HOLD_PREFLIGHT |
| 31_dir_10084 | 1.34e-08 | -0.00890791909 | 0.0007699493169587982 | PASS |
| 31_dir_10134 | 1.428e-12 | -0.0003045091 | 0.0007699495678066568 | PASS |

The frozen same-branch criterion has zero numerical clearance in the two21 references:432 angular triples per reference lie within1e-12 of-1/2. Zero steps produce NaNs in preflight input-direction quotients, never in force evaluations. Original FEASIBILITY.json retains these NaN diagnostic values; PREFLIGHT_DIAGNOSIS.json gives strict-JSON counts and interpretation. This proves the chosen preflight is inapplicable there, not that a Hessian cannot exist.

Eligible endpoints receive a new full153-coordinate Hessian, three guarded step sizes per column, reverse-order repeats and nine directions. Positive stability requires lambda_min>max(1e-7,10 times adjacent spectral discrepancy). This is a numerical diagnostic, not an interval theorem. The old held-registry matrices and memories are not transferred to new reference positions.

Coordinates cover the fixed-cell primitive-periodic family with global translations removed. They do not cover all supercell/Bloch perturbations. Different source labels do not imply different final minima; equivalence under periodicity and symmetry is unclassified. Optimizer messages and pre-polish states are retained; explicit force tolerances govern acceptance.

A — DERIVED: Schur complement positivity equivalence for symmetric harmonic block matrices.

B — NUMERICAL: four stationary endpoints; derivative qualification remains case-specific, with failed preflight preserved.

C — OPEN: non-constructor review, global/supercell stability, bath, native UD map and friction discrimination.

D — NEXT: formulate and freeze a C2-aware boundary-stencil rule at cos(theta)=-1/2, using source polynomial continuity and independent one-sided derivative limits before requalifying the held21 references. Priority98/100.
