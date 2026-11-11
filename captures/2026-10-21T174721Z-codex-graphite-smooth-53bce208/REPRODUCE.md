# Reproduction

The package preserves source, generated calculations, all new matrices/logs/energy controls, same-cutoff legacy matrices, four original structures and parameter bytes. Imported source inputs remain read-only. LAMMPS runtime and MPI libraries must be installed separately.

For the original directory layout, install the compatible LAMMPS Python wheel (2025.7.22.4.0; runtime version20250722) under lammps-runtime and matching MPI under mpi-runtime, including development headers. The included binary was built for this session's x86 Linux environment; rebuild plugin/kcz_smooth.so with build_plugin.sh for another installation. Inspect the source before compiling. Its GPL license and upstream header sources are included.

After setting PYTHONPATH to the local LAMMPS installation and LD_LIBRARY_PATH to matching MPI libraries, run pair_check.py, then run.py (which supplies the environment paths in the preserved layout). Run summarize.py and verify.py after all12 jobs finish. run.py uses4 concurrent subprocesses, each with1 numerical thread. Reproduction creates new run outputs: use a separate extracted directory to preserve the included evidence.

The model is a quintic switch on the unshifted full KCz pair energy. It is not an official upstream pair style and is not the historical Zenodo model. The switch width2A is a design choice. The plugin subclasses the installed fixed-normal KCz implementation for parameter parsing and neighbor setup, while replacing its compute routine. Pair checks validate the compiled force and energy, including the product-rule term. No dynamical bath or dissipation is present.
