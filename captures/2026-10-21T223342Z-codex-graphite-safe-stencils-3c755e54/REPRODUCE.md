# Replay

Extract this package, then its preserved UD_GRAPHITE_BRANCH_AWARE_QUALIFICATION_v0.2.zip and the nested immutable v0.1.zip into the same root. This restores the prior source geometry, potentials, plugin, stationary input arrays, full matrices and graph helper. The two attached provenance/governance sources are included at their original project_sources paths; no instructions from an archive are executed during ingestion.

Use a separate replay directory and retain original evidence untouched. Supply compatible LAMMPS2025.7.22.4.0, MPI and NumPy as described by the prior package. The shared plugin may require rebuilding for another platform; record changed binary identities in an independent replay receipt rather than silently editing the frozen record. longdouble precision is platform dependent; the submitted Linux runtime has63 mantissa bits.

FREEZE.json and CODE_FREEZE.json identify original inputs and executable bytes before fresh force collection. prepare.py is provenance, not an instruction to overwrite the existing freeze. run.py performs the two local case workers. analyze.py evaluates all five scoped probes; verify.py recomputes the recorded controls. It is not a full-family recalculation. No full matrices are replaced or assembled, and no physical bath/time/friction coefficient is inferred.
