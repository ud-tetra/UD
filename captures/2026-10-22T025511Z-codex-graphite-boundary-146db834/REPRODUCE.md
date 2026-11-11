# Reproduction

Use a fresh output directory and retain all original files. Runtime: Python with NumPy; force calculations use LAMMPS2025.7.22.4.0 with the declared smooth-width2 KCz plugin, REBO potential, MPI libraries and one thread per worker. The binary runtime installation is an external dependency. The archive contains the plugin and potential input bytes.

The active directory is graphite-boundary-stencil-v02. graphite-boundary-stencil contains the failed v0.1 geometry protocol and assertion logs, with no force outputs.

1. Validate FREEZE.json input hashes, CODE_FREEZE.json and PRECHECK_SEAL.json.
2. In a fresh output tree, run prepare.py and boundary_join.py; compare geometry plans and exact scalar coefficients to the archived records.
3. Run run.py. Four local subprocesses handle two disjoint probe ranges per case; each has its own LAMMPS instance and raw-force archive. They are computational workers, not independent reviewers.
4. Run analyze.py, verify.py, verify_geometry.py and report.py with OPENBLAS_NUM_THREADS=1.

The three estimator h values are2e-5,1e-5,5e-6Å. Unique force radii are4e-5,2e-5,1e-5,5e-6Å; both signs are evaluated. Four middle-estimator force samples are repeated in reverse order. A common baseline is allowed only if all worker baselines reproduce within1e-12 eV/Å.

The retained matrix is the symmetrized average of the positive and negative one-sided estimators at h=1e-5Å. Symmetrization occurs only after reporting the unsymmetrized discrepancy. Positive local stability is a numerical diagnostic using the frozen tenfold spectral step difference, not an interval certificate.

All source, derivative and status claims are limited to the declared potential, coordinates and thresholds. No data-dependent retry or estimator choice is performed after force collection. Constructor verification does not satisfy the non-constructor review gate.
