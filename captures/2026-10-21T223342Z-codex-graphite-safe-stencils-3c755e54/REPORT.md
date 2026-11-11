# Every-stencil angular-branch contract: five-probe audit v0.1

RESULT / STATUS: 5/5 previously failing probes pass the newly frozen scoped numerical contract. Full-family qualification remains HOLD; the prior full suite remains2/4 under its own rule. Physical promotion0. Development — no registry entry. Non-constructor review pending.

The previous complete register contains columns12,60,91 in31_dir_10084, column84 in31_dir_10134, and the cos(sqrt(3)*index) direction in31_dir_10084. This audit collects new force vectors at unchanged stationary geometries and with the unchanged REBO + imposed width2 smooth-KCz model at cutoff24 Angstrom. It does not assemble or replace any full matrix. All earlier passing and failed records remain immutable.

The numerical contract is frozen before fresh force collection, with executable hashes also recorded before launch. For each exposed probe, numerically locate its nearest affine-bond crossing c of the three internal gC knots. Set h_top=min(cap,0.8c), with cap1.25e-5 Angstrom for columns and2.5e-5 for the direction. The three centered acceptance stencils are h_top,0.8h_top,0.6h_top. This nonhalving window keeps all three steps below the crossing and avoids forcing the smallest step unnecessarily toward coordinate roundoff. It is a finite-step stability test, not a demonstrated convergence order or extrapolation error bound. No force-response-dependent reselection or fallback is permitted.

The original absolute1e-6 eV/Angstrom^2 and relative1e-5 gates apply to both adjacent differences and to the middle derivative versus the frozen prior symmetrized H times the nominal probe. Additional controls require all nine sampled points of every actual rounded stencil to keep their angular branch; minimum step1e-6 Angstrom; actual Cartesian central-direction norm error <=1e-6; reversed-order middle-derivative repeat difference <1e-7 eV/Angstrom^2; stationarity <=1e-7 eV/Angstrom; and baseline repeat difference <=1e-12 eV/Angstrom.

Affine positions are constructed in numpy.longdouble, then rounded once to native float64; this runtime has63 explicit mantissa bits for longdouble. The nominal derivative is used without coordinate correction. Actual tangent and orthogonal rounding components are recorded. These representation diagnostics and repeat controls are not a rigorous force-error bound. The angular guard is a floating-point root calculation plus sampling, not interval certification or a guard of every possible REBO branch.

| Probe | Adjacent max change | Prior-H agreement max error | Pass |
|---|---:|---:|---|
| 31_dir_10084_column_12 | 3.6198453e-07 | 2.7630503e-07 | True |
| 31_dir_10084_column_60 | 3.2943345e-07 | 2.2776066e-07 | True |
| 31_dir_10084_column_91 | 2.6483185e-07 | 1.1406174e-07 | True |
| 31_dir_10084_direction_4 | 2.2060539e-07 | 1.5002394e-07 | True |
| 31_dir_10134_column_84 | 1.089799e-07 | 7.9685599e-08 | True |

Derivative changes/errors have units eV/Angstrom^2. Every raw force, repeated middle force, actual rounded coordinate array, nominal vector, step, branch/input diagnostic and result gate is retained. The constructor verifier recomputes hashes, basis, geometry-selected windows, actual stencils, branch samples, derivatives, baseline identity and error metrics. This is constructor checking, not non-constructor review.

This is targeted numerical calibration on already exposed geometries/probes. It is not blinded physical validation or CRL-2b/2c advancement. The attached CRL-2 governance permits development work without registry entry and still requires non-constructor review for promotion. The historical v0.39 coefficient ledger is source history, not authority to reverse later v0.85 repairs; no coefficient or4/3 quantity enters this derivative calculation. Physical clock, material map and source-selected bath remain OPEN/HOLD. No friction or UD-specific prediction follows. Gap2_FINAL_Finite_Genesis.png remains unavailable.

The earlier2/4 full-suite outcome cannot be upgraded using these five tests: other columns/directions and whole-matrix symmetry/spectral checks have not been recomputed under this new contract. A positive scoped result supports freezing and testing a new full-family protocol; a failed result requires diagnosing that gate first.

A — NUMERICAL:five exposed failures retested under an every-stencil branch rule.
B — RESULT:5/5 scoped PASS; prior full suite2/4 unchanged.
C — HOLD:full-family qualification, non-constructor review and physical/native bath.
D — Physical promotion0; Development — no registry entry.

1. Next: freeze this every-stencil contract for all four full matrices and directional probes, test its geometric/roundoff feasibility before launch, then run full qualification. Priority97/100.
