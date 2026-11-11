# Reproduction scope

This is numerical qualification of an imposed REBO + smooth-KCz stationary family, not experimental validation or a native UD material model.

1. Use the four original struct.inp.data inputs, stationary RELAXED.npz and HESSIAN.npz basis files and source hashes in FREEZE.json. Restore the directory relationships shown in the package.
2. Use LAMMPS Python distribution 2025.7.22.4.0 (runtime20250722), NumPy, one BLAS/OpenMP thread. Build the bundled width2 smooth-KCz plugin with build_plugin.py and LAMMPS/MPI development headers. Rebuilding may change binary hashes; an independent replay must record its new binary identity separately rather than silently editing the frozen original. Binary identity to the audited official source tag was not independently verified.
3. FREEZE.json is the fixed numerical rule. prepare.py creates that record and is preserved for provenance; do not regenerate a new timestamp or modify the frozen record during replay. run.py launches the four local force workers, followed by analyze.py and verify.py. The submitted code hashes are in CODE_FREEZE.json; it was recorded after job launch but before any matrix result was available. Selection records are emitted before force collection in each worker.
4. New output directories are required for independent replay. Do not overwrite the supplied records. Inputs, branches, gates and prior failures remain immutable.

Geometry selection uses corrected periodic image gauges, affine bond vectors and quartic cosine-crossing roots. It numerically guards the three internal gC knots; it does not certify every REBO branch or constitute an interval proof. Fine and audit steps lie inside the numerical clearance; the coarse stencil may cross. Both neighboring differences must pass the original absolute and relative tolerances. No response-adaptive step reselection is permitted.

Directions use three old sine probes and three previously unused cosine probes at fixed steps. Directional crossings are not forbidden: these probes must demonstrate step stability directly. Relative/absolute agreement is evaluated against the symmetrized retained matrix, without coordinate-rounding correction.

All quantities use LAMMPS metal units: positions/steps Angstrom, energy eV, forces eV/Angstrom, Hessians eV/Angstrom^2. No physical time or friction coefficient is inferred.
