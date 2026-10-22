# Full stationary graphite qualification with every-stencil branch guards v0.1

RESULT / STATUS: 4/4 full-case NUMERICAL PASS under this new frozen contract. Constructor integrity verification is separate from non-constructor review. Physical promotion0. Development — no registry entry.

The four unchanged affine-stationary references are evaluated at cutoff24 Angstrom and imposed width2 Angstrom smooth fixed-normal KCz plus REBO. Each constrained Hessian has79 or151 coordinates: each layer mean x/y and global mean z are fixed, with primitive-periodic internal Cartesian displacements admitted. This is four cases at one force-model setting, not a requalification of the earlier36-model family or a fully free supercell/Bloch calculation.

The geometry/input preflight passed all460 coordinate columns and36 directional probes before any new force sampling. For each probe, the nearest numerically located affine-bond crossing of the three internal carbon gC knots determines h_top=min(cap,0.8*clearance), with cap1.25e-5 Angstrom for columns and2.5e-5 for directions. Coarse/middle/audit steps are h_top*[1,0.8,0.6]. All three actual rounded stencils are checked at nine points. The minimum selected step is1.4170214e-6 Angstrom, above the frozen1e-6 floor; maximum Cartesian input-direction norm distortion is2.68706e-8, below1e-6. The actual positions are reconstructed deterministically from the retained source geometry and selected steps rather than storing their repeated arrays for every column.

Affine positions use extended precision followed by one rounding to float64; no approximate-H direction correction is used. Every middle derivative is repeated with reversed force-sampling order. Frozen projected baseline forces are checked before collection, every20 probes and after completion. All code hashes, input hashes and preflight plan hashes were sealed before launch. No response-adaptive step reselection or fallback occurs. This is exposed-data numerical qualification, not physical or target-blind preregistration.

Both adjacent full-matrix max-entry changes must remain below1e-6 eV/Angstrom^2; relative Frobenius and each-column changes must remain below1e-5. Retained-middle relative antisymmetry must remain below1e-6. The matrix is symmetrized only after that check. Every direction must satisfy adjacent absolute/relative step agreement and middle-derivative agreement with that newly computed symmetric matrix at unchanged1e-6/1e-5 tolerances. The nine directions comprise three old sine probes, three old cosine sqrt2/3/5 probes and three previously unused cosine sqrt7/11/13 probes in each case. They are not a substitute for non-constructor review.

Additional fixed controls require projected baseline forces<=1e-7 eV/Angstrom, baseline repeat difference<=1e-12 eV/Angstrom, reversed-order derivative difference<1e-7 eV/Angstrom^2, and geometric/representation preflight. Full qualification also requires positive local spectral resolution: lambda_min(symHmiddle)>max(1e-7,10*max spectral adjacent discrepancy), in eV/Angstrom^2. The three nonhalving steps supply a numerical stability diagnostic, not a demonstrated convergence order, extrapolation error theorem or interval bound.

| Case | Full suite | Largest matrix step change | Largest directional error | Minimum stiffness |
|---|---|---:|---:|---:|
| 21_dir_0 | NUMERICAL_PASS | 2.1922556e-07 | 1.0047092e-07 | 0.2805211 |
| 21_dir_10024 | NUMERICAL_PASS | 2.8350821e-07 | 1.037813e-07 | 0.28059775 |
| 31_dir_10084 | NUMERICAL_PASS | 5.4127399e-07 | 1.6097605e-07 | 0.28094583 |
| 31_dir_10134 | NUMERICAL_PASS | 1.9313612e-07 | 7.3147449e-08 | 0.2810367 |

Across the complete new suite, maximum directional agreement error is1.6097605e-7 and maximum directional adjacent-step change is3.3833991e-7 eV/Angstrom^2. Retained relative antisymmetry is at most2.9218911e-9. Every reversed-order middle derivative and baseline repeats bit-identically. The minimum eigenvalue across the four cases is0.28052110 eV/Angstrom^2. Conservative lateral/vertical coupling ratios remain0.00696264–0.00865029; these are matrix mixing diagnostics, not physical damping or energy fractions.

Matrix changes, directional errors and stiffness are in eV/Angstrom^2. Complete flags, every failing column/pair if present, all36 directional residuals, spectra and conservative lateral/vertical coupling diagnostics appear in RESULTS.json. A positive spectrum cannot override a failed derivative gate.

The retained force model and mechanical constraints are imposed constitutive choices. Numerical consistency establishes neither a native UD material dictionary nor physical friction, a clock conversion, bath loss/noise or experimental superlubricity. The angular guard addresses three internal gC knots with floating-point roots and samples; it is not certification of every REBO branch. Input representation and repeat diagnostics do not provide rigorous Cartesian force-error bounds.

The historical v0.39 source ledger does not supersede the later v0.85 repairs; no universal G05 or4/3 damping identification is imported. The attached CRL-2 governance separates development from registry promotion; no non-constructor review has been supplied here. Physical promotion remains0. Gap2_FINAL_Finite_Genesis.png remains unavailable.

## Evidence and prior scope

All raw projected plus/minus forces, reversed middle forces, baseline vectors, derivative arrays, selected plans and input-error metrics are retained. The constructor verifier recomputes all hashes, basis, geometry plans, actual rounded stencils, branch samples, complete force differences, matrix spectra, every qualification flag and the full failed-column register. This is constructor verification, not independent replication or adversarial review. Runtime/source build identity remains limited as recorded in prior source audits.

Earlier full-suite2/4 outcomes and the targeted5/5 audit retain their original contracts and immutable evidence. This new full run is a separate qualification; old failures are not erased or relabeled. Passing numerical checks would support conservative finite-memory elimination in this stationary model, while physical dissipation remains a separate source gate.

A — NUMERICAL:460 columns and36 directional probes fully evaluated.
B — RESULT:4/4 full-case PASS under the new frozen contract.
C — OPEN/HOLD:non-constructor review, broader stability and physical/native bath.
D — Physical promotion0; Development — no registry entry.

1. Next: derive and verify exact finite conservative lateral-memory elimination for this qualified stationary family, retaining initial-slip terms and testing against full dynamics. Priority96/100.
