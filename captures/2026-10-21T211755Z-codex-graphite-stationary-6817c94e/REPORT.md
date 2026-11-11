# Stationary graphite preparation and refined stiffness audit v0.1

RESULT / STATUS: HOLD_REFINED_DERIVATIVE_QUALIFICATION; stationary preparations pass4/4; refined full stiffness checks pass2/4. Primary coarse-step qualification remains HOLD and is preserved separately. Constructor integrity checks pass; non-constructor review pending. Physical promotion0. Development — no registry entry.

## Preparation achieved

The previous omitted-mode audit detected lateral coupling at geometries with nonzero lateral residual forces. This new baseline allows internal primitive-periodic x/y/z relaxation while fixing each layer's mean lateral position, the unchanged periodic box and global mean height. Relative height can relax, with no imposed normal load or thermostat. Four original cases use the previously qualified24 Angstrom cutoff and2 Angstrom imposed smoothing width in the same REBO plus fixed-normal KCz force model.

The affine displacement space has79 or151 orthonormal equal-mass-compatible coordinates. Stationarity requires zero force projected into this space, rather than zero individual Cartesian force. Ideal constraint reactions and omitted spatial sectors remain outside that claim. Maximum projected-force residual ranges from2.285e-12 to4.249e-10 eV/Angstrom, below the frozen1e-7 limit. Layer/global mean drift stays below2.686e-16 Angstrom.

Maximum atom displacement is0.00034411–0.00049813 Angstrom. Energy decreases by0.001744–0.001856 eV per source supercell. Different supercell atom counts prevent treating those extensive changes as an angle ranking. The optimizer iterations are not a physical dissipative trajectory. Registered Newton stationarity refinement followed the initial optimizer when necessary, retaining every stage and independently measuring the resulting force.

## Primary failure and separate refinement

All four primary matrices at1e-4/5e-5 Angstrom fail the absolute step and directional checks;31_dir_10084 also fails relative symmetry. Their relative Frobenius step checks pass, and their spectral diagnostics are positive, but those facts do not erase the absolute failures. The worst absolute entry discrepancy is8.71e-4 eV/Angstrom^2 against1e-6. PRIMARY_REPORT.md, RESULTS.json and original HESSIAN.npz files preserve the HOLD result.

A post-primary diagnostic selected the two worst columns in each case by exposed error and evaluated seven finer steps. It is adaptive numerical diagnosis, not held-out validation. The selected columns supported a separate full refinement at6.25e-6/3.125e-6 Angstrom, frozen in REFINEMENT_FREEZE.json before computing those full matrices. Fresh directional force differences use1.5625e-6 Angstrom. Sampling steps changed; every original numerical tolerance remains unchanged. The stationarity positions and constraints were not altered.

| Case | All refined checks pass | Minimum stiffness, eV/Angstrom^2 | Lateral/vertical derivative ratio |
|---|---|---:|---:|
| 21_dir_0 | False | 0.2805211 | 0.008549217 |
| 21_dir_10024 | True | 0.28059775 | 0.0086502897 |
| 31_dir_10084 | False | 0.28094583 | 0.0069626412 |
| 31_dir_10134 | True | 0.2810367 | 0.007027206 |

Maximum refined absolute step discrepancy is9.52533e-06 eV/Angstrom^2; maximum relative step discrepancy2.69183e-08; relative antisymmetry6.15568e-09; fresh directional absolute error1.04061e-06 eV/Angstrom^2. The remaining failures are21_dir_0 directional absolute error1.0406079e-6 and31_dir_10084 full-matrix absolute step discrepancy9.5253262e-6 eV/Angstrom^2. The passing cases are21_dir_10024 and31_dir_10134. Refined classifications and all per-case flags are in REFINEMENT_RESULTS.json. A positive spectrum counts as qualified here only together with that case's complete refined checks.

## What the stiffness means

The projected stiffness is the symmetric force derivative at the stationary affine reference. The positivity test compares its minimum eigenvalue with1e-7 eV/Angstrom^2 and ten times the spectral coarse/fine discrepancy. This is finite-step numerical local stability within the prescribed coordinate space, not a rigorous interval bound, global minimum or full Bloch/full-supercell result.

The coupling ratio is ||H_lateral,vertical||F/||H[:,vertical]||F. It measures conservative Cartesian mixing at fixed mean layer registry. It is not an energy fraction, damping rate, heat flux or measured friction. A finite positive conservative lateral block produces reversible memory after elimination. No physical reservoir, native UD-to-material map, loss/noise law or physical-friction identification is supplied by stationarity or a nonzero cross block.

The baseline is four cases at one cutoff/width, not the earlier36-case smooth-model family requalified at new geometries. The fixed-normal force model and imposed mechanical constraints retain their stated scope. Physical/native correspondence and independent review remain OPEN/HOLD. The historical v0.39 ledger cannot replace later repaired scope; no burden constant, capacity threshold or master scalar was imported into these material equations.

## Verification and evidence

All original source hashes match. The independent constructor verifier gathers force by primitive group, checks affine means and displacement recovery, and reproduces primary classification without suppressing failures. The refinement verifier reproduces every numerical flag and directional residual from retained arrays and verifies unchanged relaxed-position hashes. Both are constructor work, not non-constructor review. The original arrays, optimizer histories, selected-column probe arrays, both full Hessian pairs, three fresh directional-force columns per refined case, source potential/plugin bytes and frozen protocols are packaged.

A — NUMERICAL: stationary constrained preparation passes4/4.
B — NUMERICAL: refined stiffness checks pass2/4; primary HOLD preserved.
C — OPEN/HOLD: broader stability, physical/native bath and independent review.
D — Physical promotion0; Development — no registry entry.

1. Next: audit the force-law derivative and failing matrix entries before any further memory/stability promotion. Priority97/100.
