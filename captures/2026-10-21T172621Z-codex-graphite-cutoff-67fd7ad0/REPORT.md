# Graphite cutoff and energy–force qualification v0.1

21 October2026. Development — no registry entry. Constructor numerical checks; non-constructor review pending. Physical promotion0.

## Result: HOLD_SCOPED_FAILURE

The prescribed combined qualification fails. All four20-to24Angstrom endpoint differences lie below the declared Frobenius thresholds, and retained stiffness stays numerically positive. However, three local sliding-coupling step checks fail at the larger cutoffs, and three of96fine-step directional energy–force controls fail at the original16Angstrom cutoff. No threshold was loosened, case replaced or failure discarded. Do not import a bath or claim a converged friction prediction on this evidence.

## Source and frozen workload

Uses the same four exposed source registries as the preceding PR334 vertical-sector capture:21/dir_0,21/dir_10024,31/dir_10084,31/dir_10134. Baseline16Angstrom arrays are inherited from UD_GRAPHITE_VERTICAL_SECTOR_v0.1.zip, SHA256aa94fd1c3518a014f2106755f57f433177b1a84e2f9827dbcdbecf84a29f1592, Library identitylibfile_bd38429a229481918f0eb3bd1368be5a. Source structures come from checksum-verified Zenodo14283098archives. Same LAMMPS20250722wheel, CC.KC and CH.rebo bytes, fixed normals, z-only relaxation, fixed lateral registry, periodic source supercells. No native UD coefficient enters.

FREEZE.json precedes the new outcomes. It fixes cutoff comparison16,20,24Angstrom, inherited force steps1e-4and5e-5Angstrom, energy steps0.002,0.001,0.0005Angstrom, deterministic test directions and tolerances. The20and24Angstrom computations each re-relax their own equilibria. Comparisons therefore include both cutoff change and its equilibrium shift. The same group indexing is explicitly checked. This is source-exposed numerical qualification, not target-blind empirical scoring.

The28or52coordinate primitive-periodic vertical blocks are retained; one global vertical translation is removed. Omitted Bloch sectors remain outside scope. Eight new cutoff/case jobs and four energy jobs completed with exit0. A successful process exit is not a scientific PASS.

## Cutoff endpoint comparison — finite numerical differences

Relative differences are ||A24-A20||F/||A24||F.

| Registry | K relative difference | g relative difference | Endpoint threshold test |
|---|---:|---:|---|
|21/dir_0|4.45330e-7|3.17981e-5|PASS|
|21/dir_10024|4.44237e-7|7.17422e-4|PASS|
|31/dir_10084|4.88874e-7|3.49227e-5|PASS|
|31/dir_10134|4.45489e-7|3.17093e-5|PASS|

Frozen endpoint thresholds are K<=1e-4andg<=1e-3. This endpoint diagnostic is insufficient because its input g estimates fail local step convergence at three points. No infinite-cutoff proof is supplied; retained positive spectra do not repair derivative failures. Absolute energies and full matrices are preserved in the package.

## Local derivative failures at enlarged cutoffs

The inherited local maximum-entry tolerance for g between h=1e-4and5e-5 is1e-7eV/Angstrom^2. Failures:

| Cutoff | Registry | max entry difference(eV/Angstrom^2) |
|---|---|---:|
|20Angstrom|21/dir_10024|3.4558166084e-4|
|24Angstrom|21/dir_0|1.6074943773e-4|
|24Angstrom|21/dir_10024|8.0590583183e-5|

Other inherited local gates, including K step stability, symmetry, uniform-translation null and sector leakage, pass. The prior16Angstrom force-difference gates still pass as originally reported. This new result prevents extrapolating that local success to other cutoffs or to a smoothly qualified sliding path.

## Energy–force checks at16Angstrom

Use saved equilibrium coordinates, without new minimization during each perturbation. Direction vectors are the first and last Helmert columns and the normalized layer-opposition breathing vector in orthonormal sector coordinates. This is a finite directional check, not every Hessian entry. Lab xand yare rigid translations of layer2. Evalues are ordinary total-cell eV; collective displacement variables have Angstrom units.

For a sector direction v and its full coordinate image Pv, evaluate curvature by [E(q+hv)-2E(q)+E(q-hv)]/h^2 and compare to v^T Kv. Evaluate each mixed derivative by the four-corner central energy stencil divided by4h^2 and compare to v^T g_axis. Also compare first energy difference to minus the projected vertical force. Raw corner energies are retained, permitting independent arithmetic checking without rerunning LAMMPS.

Fine acceptance requires BOTH h=0.001and0.0005Angstrom to pass. Ktolerance is1e-5+1e-4*abs(reference); gtolerance is2e-5+1e-3*abs(reference); first-derivative tolerance is2e-7eV/Angstrom. All96fine controls are counted:24curvatures,24first derivatives,48mixed derivatives.93pass;3fail. Every finest-step0.0005control passes, but this does not supersede the two-step rule.

| Registry | Direction/axis | h(Angstrom) | mixed absolute error(eV/Angstrom^2) |
|---|---|---:|---:|
|21/dir_10024|breathing/x|0.001|7.8214959235e-5|
|31/dir_10084|breathing/y|0.001|4.7538958851e-5|
|31/dir_10134|breathing/y|0.001|4.8924037208e-5|

No energy curvature or first-derivative fine control fails. The fine mixed discrepancies are non-monotone across some larger steps. A finite-stencil failure does not itself prove the LAMMPS force implementation is incorrect; truncation error, cutoff crossings and cancellation require separate diagnosis. Cause remains OPEN. Finer-step agreement alone is not selected after exposure as a replacement acceptance criterion.

## Verification, amendments and claim disposition

summarize.py compares complete saved matrices/hashes and records negative local outcomes. Its initial all-local-checks-pass assertion stopped upon the new failed gstep check; the aggregator was corrected to classify and preserve failed checks. No calculation output or frozen scientific tolerance changed. verify.py recomputes energy stencil values and pass/fail decisions from raw saved energies and checks log hashes. VERIFICATION.json says VERIFICATION_PASS__SCIENTIFIC_GATE_HOLD: correct recording of a failure is not a scientific PASS. No interval arithmetic, independent reviewer or full-repository integrity certification is claimed.

Preserve the earlier force-derived16Angstrom matrices as scoped numerical results. Freeze their use as generally cutoff-stable, energy-qualified coupling inputs until this gate reopens. Conservative positivity remains numerically supported only in retained sectors. No physical Gamma, phase-averaged friction, load independence, full-supercell stability or extra UD mechanism is established. Physical promotion remains0.

## Next discriminating step

Perform a source-bound cutoff-crossing audit: enumerate interlayer pair distances at the affected equilibria and all stencil corners; determine whether interactions cross the hard cutoff, and account for their energy/force contributions using the actual KCz implementation. Compare against predicted numerical cancellation or smooth truncation errors. Declare the diagnostic before evaluating new outcomes. Do not choose a smoother or different potential silently: that would be a separately versioned model branch with fresh qualification. No further bath work on this branch is recommended before this discrepancy is explained.

## Artifacts and reproduction

The package preserves source code, freezes, eight matrix sets, force and energy logs, all raw energy controls, summaries and verification. It depends on the preceding package/source archives for the inherited16Angstrom baseline and original structures. Model/runtime parameters are unchanged. Runtime binaries, credentials and unrelated files are excluded. The compact GitHub capture records text evidence plus package identity/hash. Repository verification remains sparse-checkout capture validation only. Missing Gap2_FINAL_Finite_Genesis.png was not used.
