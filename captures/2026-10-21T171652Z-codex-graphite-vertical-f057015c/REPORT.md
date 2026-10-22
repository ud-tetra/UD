# Graphite constrained vertical stiffness and sliding coupling v0.1

21 October2026. Development — no registry entry. NUMERICAL / constructor verification only; non-constructor review pending. Physical promotion0. Extends draft PR334's legacy KCz+REBO compatibility baseline.

## Result and scope

PASS_SCOPED for the primitive-periodic vertical sector of four reproduced registries. The28-coordinate(2,1)and52-coordinate(3,1)stiffness blocks are numerically positive after removing their single uniform vertical translation, leaving27and51coordinates. Their rigid lateral sliding couplings are nonzero. This does not establish full-supercell stability, a phase-averaged friction coefficient or an extra UD mechanism.

| Registry | Sector dimension | Null-removed minimum eigenvalue(eV/Angstrom^2) | Norm gx(eV/Angstrom^2) | Norm gy(eV/Angstrom^2) |
|---|---:|---:|---:|---:|
|21/dir_0|28|0.280583180778|1.367611813952|1.367611813929|
|21/dir_10024|28|0.280661471640|1.390462148702|1.365452550480|
|31/dir_10084|52|0.280978997743|1.555353293861|1.548968711735|
|31/dir_10134|52|0.281070560958|1.580200447252|1.569769725486|

Numbers describe orthonormal collective coordinates on the actual1008/1300-atom source supercells. Raw gx,gy norms therefore include replication normalization; divide by6or5 respectively for a per-primitive-cell comparison. The table must not be interpreted as an experimentally calibrated cross-angle friction ranking.

## Source and implementation

Source structures and inputs: Zenodo DOI10.5281/zenodo.14283098, complete archives lammps_21.tar.gz and lammps_31.tar.gz, previously checksum-verified in the target-replay capture. Atom/case selection and energy compatibility were fixed there. Runtime LAMMPS20250722, package lammps2025.7.22.4.0. Potential parameter bytes are those hashed in that replay's REPLAY_FREEZE.json. Historical source logs use20221103; original parameter bytes were absent. This remains a modern compatibility model, not a recovery of the original executable.

Physical law imported for this computation is the original fixed-normal kolmogorov/crespi/z16.0 plus separate REBO terms, fixed lateral coordinates and z-only relaxation. The initial3.46Angstrom separation is allowed to relax under this specified energy law, not prescribed as a maintained normal load. No full-normal KC substitution or bath model is introduced. No coefficient from the historical UD ledger is used. Missing Gap2_FINAL_Finite_Genesis.png remains unused.

## Object, coordinates and reduction

Let q consist of all vertical Cartesian displacements, x,y be rigid displacement of layer2 in the laboratory lateral axes, and E be the declared total cell energy. At each reproduced stationary configuration, K_full=-partial Fz/partial q, gx_full=-partial Fz/partial x, and gy_full=-partial Fz/partial y. Matrix units are eV/Angstrom^2; multiplying by16.02176634 converts to N/m.

The supercells contain6by6or5by5identical moire cells. Group atoms by layer and lateral fractional coordinate modulo a primitive moire cell. P has one indicator column per group normalized by the square root of group size, so P^T P=I. The computed block is K_s=P^T K_full P, and g_s=P^T g_full. A vertical perturbation h in collective coordinate j moves each atom in that group by h/sqrt(group size), not by h. These conventions fix all factors of cell count.

If the equilibrium and conservative law possess the exact cell-translation symmetry, K_full preserves this invariant sector and rigid sliding forcing lies in it. Our matrices check this numerically by retaining the full n-by28or n-by52force-response columns. They do not prove the symmetry exactly in floating arithmetic. Nonzero-Bloch sectors remain uncomputed; positivity of K_s alone does not establish positivity of K_full. Nonlinear or thermally activated motion can excite omitted sectors even where a linear pointwise reduction is accurate.

Uniform vertical translation is a null mode. The calculation removes it through a Householder orthonormal complement. verify.py separately uses a Helmert complement and compares all retained eigenvalues. The reported eigenvalues are ordinary stiffness eigenvalues, not mass-weighted frequencies.

## Executed numerical gates

Central force differences use h=1e-4and5e-5Angstrom in normalized collective coordinates. The fine step is the reported value. Before reduced-run outcomes, the contract fixes relative Frobenius step tolerance1e-5, absolute max-entry K step tolerance1e-6eV/Angstrom^2, absolute g step tolerance1e-7, symmetry relative tolerance1e-6and uniform-translation residual1e-6. Sector invariance is checked at both steps with relative leakage threshold1e-5. All four cases pass. Positivity is a numerical eigenvalue test, not an interval lower-bound certificate. Inversion is restricted to the null-removed retained block and is attempted only after the gates pass.

The first full-supercell derivative attempt was stopped for computational cost before producing a complete matrix. That original plan/source and its progress log are retained. Scope was then explicitly narrowed to the primitive-periodic sector before its computation. A mapping test and raw-column leakage checks control this reduction; full Hessian completion is not claimed.

The first reduced numerical run completed its matrices but failed JSON export because NumPy booleans were not serializable. Its arrays and logs remain in serialization_failure/. The exporter was repaired without changing finite-difference steps, model parameters or thresholds; saving coarse raw columns was also added. All four cases were rerun and exited0. Independent constructor verification finds exactly zero difference in every common retained array between attempts. This is a bookkeeping correction and reproducibility check, not independent review. Final log hashes are computed after closing LAMMPS, avoiding the prior turn's pre-close hash problem.

verify.py checks both-step projections, sector leakage, orthonormality, all independent-complement eigenvalues, repeated arrays, final log hashes and frozen gate status. Full raw matrices and position data are preserved in MATRICES.npz. JSON/log timing and ZIP timestamps are not claimed byte-reproducible across execution environments.

## What this says about the hypothesis

Sliding visibly drives vertical internal deformation in this conventional model. A strict claim g=0for these registries is numerically contradicted. This does not alone falsify a bath-selective nullspace: its condition is Gamma^(1/2)K^(-1)g=0, and no physical Gamma has been acquired here. For an assumed strictly positive damping on the whole retained response space, nonzero g and positive K give nonzero dissipation. That is conditional algebra, not a measured graphite friction result.

The geometric low-corrugation account survives. No independent native UD law selecting a special bath-coupling constraint is established. Do not promote these ordinary material stiffness matrices into a UD microscopic identification. A pointwise derivative at two phases is not a full-cycle loss integral.

## Remaining numerical and physical gates

The checks establish step stability at the fixed source cutoff, not cutoff convergence. Neighbor-cutoff smoothness, alternate cutoff values, energy-versus-force mixed-derivative controls and fixed-normal versus local-normal model sensitivity remain untested. Normal-load elimination and full lateral relaxation are different branches. A physical bath response, temperature, boundary conditions, uncertainty budget and independently sourced UD constraint remain required before testing added dissipation protection.

Recommended next action: check cutoff and energy-force consistency of the retained blocks before importing a bath coefficient. Raw publication targets remain exposed; future fits/reanalyses must retain exploratory status until a new independent test is frozen.

## Files and reproduction

calculate_reduced.py and run_reduced.py execute the accepted workload with the source structures and parameter paths recorded above. verify.py is the independent constructor check. REDUCED_FREEZE.json, per-case RESULTS.json, MATRICES.npz and final logs retain scientific outputs. The full attempted plan and failed-export evidence are retained alongside them. Runtime libraries/packages are excluded from the deliverable. Source structures remain reacquirable by the previous archive hashes and selected member paths. A saved package holds complete matrix arrays; GitHub capture stores compact text evidence and its package identity/hash. No claim of a turnkey container or full historical-repository integrity pass.
