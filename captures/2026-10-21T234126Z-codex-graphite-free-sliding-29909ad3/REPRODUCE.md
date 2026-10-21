# Reproduction and scope

Use a fresh directory tree, retaining immutable original outputs. The companion ZIP carries frozen inputs and results. Python requires NumPy/SciPy; force evaluation uses the previously installed LAMMPS2025.7.22.4.0 runtime, MPI and smooth-width2 KCz plugin. The binary runtime itself is not bundled. run_relax.py and run_hessian.py specify the runtime environment.

1. Validate FREEZE input SHA256 values and RELAX_CODE_FREEZE.
2. Run run_relax.py. Each local search uses the same declared0.05Å relative-x seed. Preserve optimizer status, pre-polish state, force/energy evaluation history and final positions.
3. Run prepare_hessian.py. Check all four preflight results. Any failure yields HOLD without changing steps or thresholds.
4. Preserve relaxation log files under relaxation-specific names before starting the Hessian evaluator, which uses its own lammps.log and case.log outputs.
5. Run run_hessian.py, then analyze.py, verify.py and summarize.py with OPENBLAS_NUM_THREADS=1.

The Hessian uses centered negative force derivatives in the full81/153-dimensional primitive-periodic basis. It excludes only global translation in that family; it does not include all supercell fluctuations. Three carbon gC knots are guarded using numerical roots and nine rounded-position samples; this is not an interval certificate for every potential branch.

The minimizer’s energy stopping message is never sufficient for acceptance. The explicit maximum projected force must be <=1e-7 eV/Å, including both newly released sliding coordinates. A deterministic force-root polish is permitted only by the frozen rule and accepted only if it reduces that force. Hessian qualification separately decides local positive stability; a root can still be a saddle.

Full source force logs, optimizer history and raw three-step Hessian forces remain in the archive. Repository text capture references the archive SHA256. All checks are constructor checks; physical promotion0 and non-constructor review pending.

## Active selective execution

The original all-family preflight failed for the two21 cases. No force evaluation was attempted for those failed plans. ELIGIBILITY_AMENDMENT.json freezes a scheduler-only change before any fresh endpoint Hessian forces: run_eligible.py invokes calculate_eligible.py only for individually eligible cases; analyze_eligible.py and verify_eligible.py cover those executed cases. Original scripts remain for provenance and are not the active route after this amendment. Run verify_relaxation.py for all four endpoints, diagnose_preflight.py for the branch boundary failure, and summarize_eligible.py for the combined PASS/HOLD report.

The original FEASIBILITY.json uses Python's NaN serialization for the undefined zero-step diagnostics. Keep its bytes because its digest was sealed. PREFLIGHT_DIAGNOSIS.json is a strict-JSON companion explaining the nonfinite values and failed steps. They must never be interpreted as successful input guards.

BOUNDARY_NOTE.md and boundary_join.py supply a post-run source-polynomial explanation using exact rational arithmetic. This does not retroactively qualify the held matrices or replace the frozen derivative rule.
