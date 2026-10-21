# Reproduction scope

The ZIP retains the original36 MATRICES.npz files at the paths frozen in FREEZE.json, all new derivative columns and result files, the four source structure files, smooth plugin source/license and compiled plugins, and the exact potential files. The compatible Python/LAMMPS/MPI runtime is not bundled. This run used LAMMPS20250722 with NumPy/SciPy, equal carbon masses and no trajectory integration.

For array-level constructor verification, run `python3 graphite-mode-coupling/verify.py` from the extracted root. It needs NumPy and the preserved source/new arrays. Run summarize.py and make_report.py in that order to regenerate the aggregate report from individual records.

For force-level repetition, calculate.py accepts an index0..35 into FREEZE.json. It recreates the conservative force setup, scatters the already frozen equilibrium coordinates, evaluates full forces at the declared perturbations and writes a per-case archive. It does not run a minimizer. Use a separate copy/output root so the original evidence is preserved. A compatible LAMMPS runtime must support REBO and the retained smooth KCz plugin. The build uses pair_kcz_width.cpp with UD_SWITCH_WIDTH=1,2 or3, the retained header files and matching LAMMPS/MPI headers/libraries. Compiled .so files are retained as provenance and may require rebuilding on another platform. Scientific results must not rely on silently substituting force parameters.

run.py is the constructor driver used for36 cases. Its initial four JSON export failures are retained separately; recover_exports.py reuses their already saved columns and repeats only reciprocal controls. EXPORT_RECOVERY.json verifies all36 array entries across the four failed exports exactly. A full repeat may simply use the corrected calculate.py; the `reuse` argument exists only to reproduce the recorded recovery with its preserved development_failure inputs.

Reference forces are deliberately observed without the original lateral lineforce filter. This is an explicit released-coordinate derivative audit at a constrained reference. No free3D stationary equilibrium, full Hessian spectrum, damping rate or physical reservoir is claimed.
