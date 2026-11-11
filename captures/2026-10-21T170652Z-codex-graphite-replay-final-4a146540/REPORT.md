# Target-cell archive inspection and compatibility replay v0.1

21 October2026. Development — no registry entry. Constructor numerical reproduction only. Non-constructor review pending. Physical promotion0. Extends graphite captures on PR334; no earlier evidence overwritten.

## Result

Four original target-cell minimization energies reproduce in LAMMPS22July2025 within the frozen1e-7eV/cell tolerance. Maximum absolute difference is2.1827872842550278e-11eV/cell. This qualifies a small compatibility subset, not all source calculations, force derivatives, a physical friction prediction or an extra UD mechanism.

## Sources and custody

Minkin, Lebedeva, Popov, Vyrko, Poklonski and Lozovik, Zenodo v1 DOI10.5281/zenodo.14283098, https://zenodo.org/records/14283098; supplement to Phys.Rev.Materials9,024002. Downloaded lammps_21.tar.gz and lammps_31.tar.gz, matching published MD5 values. Complete size and SHA256 records are in CUSTODY_AND_GRID.json. Source archives remain local; their identities and reacquisition code are captured, rather than duplicating1.24GB in GitHub.

LAMMPS wheel lammps2025.7.22.4.0, runtime version20250722, plus MPICH5.0.2. Historical archived logs identify LAMMPS3November2022. The wheel's CC.KC and CH.rebo files were used with recorded hashes. The archives contain no files ending .KC or .rebo; therefore original parameter byte identity remains unavailable. Matching potential filenames and dated headers alone do not prove byte identity. Version compatibility is tested numerically for these cases only. No claim of an exact historical executable replay.

Two redundant sequential downloads were stopped after a range-based transfer supplied complete checksum-verified archives. Initial runtime loading failed on missing MPI libraries; after installing dependencies, its default transport initialization failed under the environment's socket restrictions. A single-process self-only transport succeeded without permission escalation. These setup failures are not scientific model failures. No acquired shell submission script or Mathematica source was executed. Original input content was read as data and a bounded command list was transcribed in replay.py.

## Actual source model and constraints

All four selected PES inputs use units metal; periodic boundaries in all three axes; atom_style full; a100Angstrom-high box; pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z16.0. Two REBO substyles isolate the two atom types/layers, and CC.KC couples types1and2. No taper flag is passed to this z-style command. The exact legacy cutoff/shift behavior belongs to its implementation; the full-style taper result from the prior capture must not be imported into it.

The constraint fix lineforce0,0,1 restricts motion to z. Conjugate-gradient minimization uses dmax0.005Angstrom and minimize1e-15,1e-15,30000,30000. These calculations permit out-of-plane relaxation at fixed lateral registry, not unconstrained full-coordinate or constant-normal-load evolution. Initial layer separation is3.46Angstrom in selected input structures. No fixed-load bath/damping is implied.

(2,1) selected cells have1008atoms=36*28; (3,1) selected cells have1300atoms=25*52. Primitive commensurate bilayers contain28and52atoms respectively. The finite periodic boxes and their exact original coordinates are retained through source-member hashes and re-extraction code; arbitrary minimum-image replacement is not asserted.

Full archive input inspection found10 distinct input texts among24246input members for(2,1), and4 among23518for(3,1). ARCHIVE21_INPUTS.json and ARCHIVE31_INPUTS.json record those variants. These counts include other constraint/relaxation families; success of the four selected PES cases does not certify those other families.

## Frozen compatibility cases and outcome

Four complete cases were selected by lexicographic order among complete records in the then-downloaded prefixes, before executing the replay:21/dir_0,21/dir_10024,31/dir_10084,31/dir_10134. This availability-conditioned selection is disclosed; it is not a random or adversarial sample. The raw four energy targets were already exposed. REPLAY_FREEZE.json fixes cases, runtime parameter hashes and absolute1e-7eV/cell comparison tolerance before execution. This is reproducibility, not blind confirmation.

| Pattern/case | Archived final E_pair (eV/cell) | Replay minus archive (eV/cell) |
|---|---:|---:|
|21/dir_0|-7474.05107924262|1.8189894035458565e-12|
|21/dir_10024|-7474.05807169058|-1.000444171950221e-11|
|31/dir_10084|-9639.16387419045|2.1827872842550278e-11|
|31/dir_10134|-9639.17245097659|2.000888343900442e-11|

Original and replay logs retain their stop conditions. Matching energies does not certify each Hessian entry or minimizer convergence in all directions. The force constraint can hide lateral residuals, as intended by this source family.

## Mapping to the exposed PES tables — exploratory reconciliation

The directory index is not the row index of the deposited plotting table. For a151-by151grid, directory i corresponds to x=0.02(i mod151), y=0.02 floor(i/151)Angstrom. The plotting file uses the opposite nesting order. This mapping was established after the energy replay and is not a newly preregistered target test.

Independently verify the mapping from input top-layer displacement: rotate Cartesian displacement relative to dir_0 by phi=30degrees-theta/2; it yields the stated x,y. check_and_map.py checks both coordinates rather than choosing whichever grid energy agrees. Subtract the two replayed energies per pattern, divide by atoms in one layer and convert eV to microeV. Compare this difference against the corresponding deposited PES difference. CUSTODY_AND_GRID.json preserves errors and classifications. No numerical grid acceptance threshold is asserted after exposure. Absolute energy offsets cancel; no fit to friction or to a new physical target occurs.

## Consequence for the UD hypothesis

The historical fixed-normal conservative model is now numerically reproducible in four selected cases. It does not establish a graphite dissipative nullspace. Its constrained out-of-plane Hessian and mixed sliding derivative can next be computed in this declared legacy model. That would be a conventional baseline. Full-normal deformations, intralayer freedom, fixed-load elimination and bath response must be separate branches, not silent upgrades.

Hessians were not calculated during this workload. No experiment, whole-grid rerun, friction law, native UD coefficient or fundamental physical correspondence is inferred. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused. Supplied historical ledger and proposed CRL-2 rules provide no graphite parameters.

## Reproduction

range_download.py recovers checksum-verified source archives. check_and_map.py extracts selected members and establishes their geometry-to-grid mapping; it also needs the already verified data.zip from the preceding capture. replay.py records the exact command list used and the installed potential path. A portable rerun must provide the same wheel parameter bytes and set its parameter path explicitly; no claim of a turnkey container. SELECTED_FILES.json hashes recovered members and replay logs. The compact capture includes code, records and logs, with source IDs/hashes for large data. Runtime packages, credentials and unrelated files are excluded. Repository verification covers only materialized captures in the sparse checkout.

## Pre-publication receipt correction

The first receipt check failed because replay.py recorded log hashes before l.close(), which appends exactly25bytes: the Total wall time line. The original pre-close hash is preserved in REPLAY_RESULTS.json. FINAL_LOG_RECEIPTS.json proves that each original hash matches the exact final-file prefix and records the appended text and final-file hash. verify_receipts_final.py checks both, as well as source energies, cases and frozen energy tolerance. VERIFICATION_FINAL.json is the operative check. The earlier verifier and its empty redirected output remain preserved as failure evidence; no result array, energy, case or scientific threshold was changed. This was a constructor bookkeeping correction, not independent review. A preliminary local capture was made before this check completed; it is not the remote release capture.
