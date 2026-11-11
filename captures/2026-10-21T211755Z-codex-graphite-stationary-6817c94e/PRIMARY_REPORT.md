# Stationary graphite preparation and constrained stability v0.1

RESULT / STATUS: Numerical qualification HOLD_DERIVATIVE_QUALIFICATION for four frozen baseline configurations. Stability classifications: {'POSITIVE_RESOLVED': 4}. Vertical/lateral coupling classifications: {'RESOLVED_NONZERO': 4}. These are raw spectral/coupling diagnostics; the full stiffness qualification has not passed. Physical/native reservoir identification remains HOLD; physical promotion0. Development — no registry entry. Constructor checks only; independent review pending.

## New preparation and scope

The prior full-force audit found vertical-to-lateral tangent coupling at references that were only equilibrated with lateral coordinates fixed. This calculation supplies a new stationary preparation on an explicit affine mechanical constraint space. It preserves the prior arrays and outcomes.

The four source cases are run at the previously qualified24 Angstrom cutoff and2 Angstrom smoothing width. The supercell, layer membership and each layer's mean lateral position remain fixed; global mean height remains fixed, while interlayer separation and internal primitive-periodic x/y/z coordinates may relax. No external normal load, temperature, thermostat or sliding drive is added. Local atoms may reconstruct; registry here fixes means rather than every atom.

The orthonormal displacement basis has3d-5 coordinates:79 for primitive dimension28 and151 for primitive dimension52. These are material preparation dimensions, not identifications with a UD carrier. Lateral and vertical coordinate blocks have dimensions52/27 or100/51. The conservative force law remains the imposed smooth fixed-normal KCz plus REBO model. It is not a full uncertainty assessment of real graphite, the legacy hard-cutoff model or a cutoff/width robustness sweep at these new relaxed references.

## Stationarity, stability and coupling

| Source case | Constrained dimension | Max projected force, eV/Angstrom | Minimum stiffness eigenvalue, eV/Angstrom^2 | Spectral diagnostic only | Relative lateral/vertical block norm |
|---|---:|---:|---:|---|---:|
| 21_dir_0 | 79 | 2.285e-12 | 0.2805211 | POSITIVE_RESOLVED | 0.008549217 |
| 21_dir_10024 | 79 | 1.847e-11 | 0.2805977 | POSITIVE_RESOLVED | 0.00865029 |
| 31_dir_10084 | 151 | 4.249e-10 | 0.2809458 | POSITIVE_RESOLVED | 0.006962642 |
| 31_dir_10134 | 151 | 1.242e-10 | 0.2810367 | POSITIVE_RESOLVED | 0.007027206 |

Maximum constraint drift is 2.686e-16 Angstrom. Maximum atom displacement ranges from 0.00034411 to 0.00049813 Angstrom. The extensive supercell energy changes range from -0.001855545 to -0.001744224 eV. Because the source supercells contain different atom counts, those extensive energy changes are not an angle ranking or evidence of a favored geometry.

Stationarity means B^T F=0 within the prescribed coordinate space. Individual forces can remain as constraint reactions or components outside this sector; the result does not assert a completely free3D equilibrium. The layer-mean restrictions are time-independent ideal constraints, not a specified physical controller. Future externally driven registry changes would require their own work accounting.

The stiffness is the central derivative of projected conservative forces at each new stationary reference. A positive classification requires its smallest symmetric eigenvalue to exceed both1e-7 eV/Angstrom^2 and ten times the coarse/fine spectral discrepancy. This is numerical local stability within the declared affine space, not a rigorous eigenvalue interval, a global minimum or full-supercell/Bloch stability.

All four cases fail the frozen absolute Hessian-step and directional-error checks;31_dir_10084 also fails relative symmetry. The largest entry-level coarse/fine discrepancy is8.71e-4 eV/Angstrom^2 against the1e-6 criterion. All four relative Frobenius step checks pass, which does not erase those absolute failures. Zero of four cases is fully stiffness-qualified. The positive spectral diagnostics therefore remain conditional numerical evidence, not an accepted stationary-bath stability result. No tolerance has been loosened.

The coupling statistic is ||H_lateral,vertical||F/||H[:,vertical]||F. It is an operator norm ratio under a fixed mass-compatible orthonormal basis, not an energy fraction, damping rate or measured friction. It tests whether allowing internal lateral relaxation removes the material coupling route found in the earlier constrained-reference audit. It does not use the earlier responses to construct a dark projector or tune a bath.

## Numerical controls and provenance

The protocol was frozen before this relaxation, using already exposed source geometries. It is not target-blind physical preregistration. All four original source hashes match. L-BFGS-B minimizes the shifted potential using exact projected forces; the independent force tolerance decides stationarity. Its terminal success flag is recorded but does not substitute for that test. Where extensive-energy precision stopped the initial optimizer early, the registered Newton refinement required a reduction in projected-force norm, retained every stage and respected its step/halving limits. OPTIMIZER.json and PRE_POLISH arrays preserve these stages.

Coarse/fine Hessians use1e-4 and5e-5 Angstrom normalized-coordinate steps. Maximum relative step discrepancy is 3.5413e-06; maximum entry discrepancy 0.00087095 eV/Angstrom^2; maximum relative antisymmetry 1.0617e-06. Three fresh deterministic directional force differences at2.5e-5 Angstrom per case check Hessian-vector predictions against the frozen criteria. The data include every directional residual.

A separate constructor script independently gathers forces by primitive group, reconstructs coordinate constraints/displacements, reproduces the eigenvalue classification and coupling block, and hashes the retained arrays. This is additional constructor verification, not review by a non-constructor. All evidence belongs to the development lane. The attached historical ledger v0.39 does not supersede the recovered current ledger repairs, and no burden coefficient or7/768 threshold is imported into these atomistic equations.

## What this closes and what remains

This baseline replaces the previously nonstationary released-coordinate reference with a specified stationary constrained preparation, and tests the candidate coupling there. The finite constrained lateral block is exposed as a candidate additional material coordinate set, but its full derivative qualification remains blocked. A positive stiffness and nonzero cross block are not a source-selected reservoir or proof of irreversible dissipation.

After derivative qualification, a natural next reduction would eliminate the finite lateral block into its exact frequency-dependent memory, with the actual coupling fixed by the relaxed stiffness. That would replace arbitrary damping controls with a conservative material-derived kernel. Any irreversible export, thermal noise, experimental friction or native UD protection still requires an independently sourced bath/preparation and material dictionary. Full spatial-wavevector sectors and new physical data remain additional gates.

A — NUMERICAL: stationary constrained preparation passes4/4.
B — HOLD: full stiffness qualification passes0/4; data integrity checks pass.
C — OPEN/HOLD: wider stability, bath identification, native map and independent review.
D — Physical promotion0; Development — no registry entry.

1. Next: use the selected-column step diagnostic to freeze a finer full-Hessian calculation, then rerun every original absolute, symmetry and directional gate before deriving a qualified memory kernel. Priority97/100.

## Post-primary selected-column diagnostic

DIAGNOSTIC_FREEZE.json was written after the primary failures, before the new probes. It selects two columns per case by the exposed maximum absolute step discrepancy and freezes seven steps from1e-4 through1.5625e-6 Angstrom. This is response-adapted numerical diagnosis, not held-out validation or a replacement gate. The table compares successive full-column max changes at the original pair and the finest pair. It does not qualify untested columns or establish a convergence order.

| Case | Selected column | Original-pair change | Finest-pair change |
|---|---:|---:|---:|
| 21_dir_0 | 49 | 0.000506946 | 3.70172e-07 |
| 21_dir_0 | 23 | 0.000491786 | 5.01899e-07 |
| 21_dir_10024 | 17 | 0.000691281 | 2.91918e-07 |
| 21_dir_10024 | 25 | 0.000363728 | 5.68881e-07 |
| 31_dir_10084 | 7 | 0.000870943 | 5.58366e-07 |
| 31_dir_10084 | 91 | 0.000843046 | 2.50326e-07 |
| 31_dir_10134 | 84 | 0.000619205 | 3.63992e-07 |
| 31_dir_10134 | 65 | 0.000570041 | 4.26171e-07 |

Raw probe columns and all step values are retained. The original coarse/fine matrices and failed flags remain unchanged. A finer full-matrix calculation must rerun all gates; selected-column improvement alone cannot close them.
