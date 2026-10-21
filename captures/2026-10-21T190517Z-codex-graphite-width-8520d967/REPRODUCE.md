# Reproduction

The archive contains the24 new width1/3 matrices, logs and raw energy controls, the12 unchanged width2 configurations from v0.1, source structures and CC.KC/CH.rebo parameters. LAMMPS and MPI runtimes must be installed separately. The inherited source folder includes its earlier report and scripts: those remain v0.1 evidence and are not overwritten by this audit.

Use a separate extracted directory for any rerun. Install a compatible LAMMPS wheel and matching MPI development libraries under the preserved lammps-runtime and mpi-runtime paths. The original runtime is20250722 from wheel2025.7.22.4.0. Supply its Python path and shared libraries. The provided Linux binaries should be rebuilt for another environment.

setup.py writes the frozen protocol and inherited hash receipt, emits width-specific calculation scripts from v0.1 and compiles three fixed-width plugins. It uses only known local research source, not archive-supplied execution scripts. It requires g++ and the included upstream headers plus runtime development headers. pair_check.py W checks each compiled width W in1,2,3. run.py requires those three controls to pass, then runs all24 new jobs using4 subprocesses with1 numerical thread each. Each job performs fresh z relaxation, the full retained-sector force derivatives, then the directional energy controls.

After all24 jobs finish, run summarize.py and verify.py. Width2 outcomes are read directly from the inherited graphite-smooth folder and checked against INHERITED_INPUTS.json. The report uses the larger-width matrix norm in width comparisons. Parameter and result hashes are retained in the inventory. Rerunning setup.py in the original evidence directory is not preservation: use a copy.

The width2 compiled source has the same switching algebra as v0.1 when w=2: (rc-w)=(rc-2), the interval divisor equals2, and -30/w=-15. Its isolated-pair control checks this parameterized implementation; it is not a new graphite run or independent replication.

The GPL source and license are included. These models contain no physical bath. Numerical width robustness does not identify a UD dissipative coupling or predict friction.
