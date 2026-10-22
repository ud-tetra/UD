# Reproduction

This package directly supplies the four qualified HESSIANS.npz inputs, prior qualification summaries, frozen memory protocol, derivation, active amended executable, numerical outputs and verifier. No molecular-force rerun is needed for the finite harmonic-memory calculation. The prior force qualification remains its own dependency and scope.

Use NumPy/SciPy/Matplotlib with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. All time is dimensionless tau and all initial vectors are mathematical unit-amplitude linear probes; no physical clock or nonlinear trajectory accuracy is asserted.

The original calculate.py and CODE_FREEZE.json are immutable first-execution evidence. That run completed the first case's four numerical preparations and stopped at JSON serialization of a NumPy Boolean. Its raw outputs remain in21_dir_0/. CODE_AMENDMENT.json records the writer-only scalar conversion, separate active calculate_v02.py/verify_v02.py and new output namespace run_v02/. No equation, test preparation, solver setting or threshold changed. SERIALIZATION_REPLAY_CHECK.json confirms that every first-case array in the original and amended runs is bit-identical.

The active calculation is calculate_v02.py; the active aggregate and verifier output are RESULTS_v02.json and VERIFICATION_v02.json. In a separate replay directory, retain original files and supply a new output destination; do not overwrite captured results. prepare.py is provenance and must not regenerate the original frozen timestamp. verify_v02.py verifies both executable records, reconstructs analytical references and hidden positions/velocities from retained memory states, recomputes energy/history residuals, and checks an independent first-order matrix exponential at selected times.

Raw retained arrays are memory auxiliary ODE states, omitted-source vertical trajectories, initial conditions, dimensionless grids, energies and two direct-history quadrature arrays. Full-reference and reconstructed position/velocity arrays are deterministically derived from MODEL.npz and the raw initial/memory states, and are regenerated rather than duplicated in the package. The auxiliary ODE has2m coordinates and is an exact finite realization of the memory equation; no reduced total state-size claim is made.

DERIVATION.md contains the exact conditional theorem, all initial-source signs, reconstruction, positive-type identity, energy storage, transfer identity and the zero Abel-limit distinction. REPORT.md states the numerical scope and open physical/native gates.
