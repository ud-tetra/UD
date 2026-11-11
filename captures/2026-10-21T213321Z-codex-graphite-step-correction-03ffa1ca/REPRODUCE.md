# Reproduction

The package preserves raw force ladders, actual tangent-direction diagnostics, stationary inputs, version-tagged source/parameter bytes, correction provenance, all corrected36 geometry maps and72 closure records, original36 material matrices, source graph arrays and necessary plugin/structure inputs. A compatible LAMMPS/Python/MPI runtime is required only for fresh force evaluations; it is not bundled.

Array-level checks use NumPy/SciPy: run verify.py. It recomputes force windows/errors and independently enumerates periodic images for all corrected bonds. summarize.py rebuilds the force-ladder summary. branch_audit.py performs the source-parameter polynomial and corrected geometry crossing audit. gauge_replay.py regenerates the corrected maps and closure records from preserved inputs; it writes to this new directory and never modifies original geometric archives.

Force-level repetition uses calculate.py with indices0..3 into FREEZE.json. component.py2 is the REBO-only31_dir_10084 comparison, with cross-layer interactions explicitly none. Use a separate evidence copy/output root when repeating. Runtime version was LAMMPS20250722; compiled plugin provenance is retained but may require rebuilding for another platform. The smooth source is compiled with UD_SWITCH_WIDTH=2. Do not substitute force parameters or source geometry silently.

This release retains initial setup/guard failures under development_failure. The branch geometry guard failed because earlier graph shifts were in the raw source image gauge; corrected branch_audit.py explicitly converts those shifts. The REBO-only configuration initially omitted a cross-pair none directive and failed before producing forces. Neither setup failure changed a scientific threshold.

The existing stationary stiffness qualification remains2/4. Diagnostic plateau choices and approximate actual-direction correction are not substitute acceptance tests. All conclusions are constructor work, not independent review or physical identification.
