# Reproduction
Use the supplied source/reference tree and the LAMMPS runtime described in the preceding full-safe qualification package. Python requires NumPy and SciPy. The imported smooth KCz shared library requires a compatible LAMMPS runtime and MPI libraries; those installed runtime dependencies are not bundled here.

1. In a fresh output tree run prepare.py (generates geometry plans); compare to sealed plans.
2. Verify CODE_FREEZE and PRECHECK_SEAL before running calculate.py for each case, using the runtime environment in run.py.
3. Run analyze.py with OPENBLAS_NUM_THREADS=1, then verify.py.

The archive preserves the inputs, raw force outputs and reduced/full trajectories. Existing outputs must be copied to a new directory before rerunning; keep immutable originals. Repository capture contains text/code and the archive digest; binary arrays are in the companion ZIP.

FREEZE.json inherited older descriptive fields matrix_rule/direction_rule/stability/directions/roundoff_rule from the full-internal family. The explicit new purpose, numerical_rule, dynamics_rule and scope fields override those descriptions for this port extension. Only two port columns and nine internal directions were measured; no extended-SPD gate or port-zero-baseline requirement was applied. This metadata ambiguity is documented after execution, not silently edited. Governing numerical thresholds are unchanged.
