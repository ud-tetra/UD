# Branch-aware graphite derivative qualification v0.1

RESULT / STATUS: 2/4 cases pass the separately frozen branch-aware numerical suite. Physical promotion 0. Development — no registry entry. Constructor integrity checks are separate from non-constructor review.

The retained stationary coordinates, force model, affine constraints and numerical tolerances are unchanged. The prior primary and refined suites retain their own recorded failures; the earlier refined result remains 2/4 under its original protocol. This new protocol was selected after exposed-data diagnosis and is numerical calibration, not a physical preregistration or experimental result.

The rule numerically locates affine-bond angular crossings at all three internal carbon gC domain knots. Each column uses the largest declared fine step below 90% of the nearest crossing distance, capped at 6.25e-6 Angstrom; coarse and audit steps are twice and half that step. Fine and audit stencils are guarded; coarse may cross. Both adjacent derivative discrepancies must satisfy the original absolute 1e-6 eV/Angstrom^2 and relative 1e-5 limits. Matrix antisymmetry remains below 1e-6 relative; stationarity remains below 1e-7 eV/Angstrom. Per-column relative checks are also required. Failure cannot trigger response-adaptive step reselection.

The selection reduces six columns: one in 21_dir_10024 and five in 31_dir_10084, including both previously diagnosed REBO-sensitive columns. All other columns keep the larger fine step. The guard is a floating-point quartic-root calculation with sign and residual checks, supplemented by an independently recomputed nine-point branch test. It is not an interval proof or certification of every possible REBO branch. The corrected periodic-image gauge is used throughout.

Three old sine directions serve as regression probes. Three previously unused cosine directions use frequencies sqrt(2), sqrt(3), sqrt(5), normalized in the affine basis. All six use fixed coarse/fine/audit steps 2.5e-5, 1.25e-5, 6.25e-6 Angstrom. Directional stencils may cross angular branches but must independently satisfy both neighboring step-stability checks and agree with the symmetrized retained matrix under the same absolute and relative thresholds. No coordinate-rounding correction or target-dependent step selection is applied.

| Case | Full suite | Worst adjacent matrix entry change | Worst directional error | Minimum stiffness |
|---|---|---:|---:|---:|
| 21_dir_0 | NUMERICAL_PASS | 5.0947213e-07 | 1.676374e-07 | 0.2805211 |
| 21_dir_10024 | NUMERICAL_PASS | 4.4921347e-07 | 1.4967149e-07 | 0.28059775 |
| 31_dir_10084 | HOLD | 2.40591e-05 | 1.1759634e-07 | 0.28094583 |
| 31_dir_10134 | HOLD | 1.5641498e-05 | 1.0603147e-07 | 0.2810367 |

Hessian changes, directional errors and minimum stiffness have units eV/Angstrom^2. Detailed gates, worst entries and all direction residuals are in RESULTS.json; every force vector is retained in the package. A positive spectrum is insufficient to qualify a case that fails another gate.

## Remaining failures

All four retained fine/audit matrix pairs pass, and all24 fine directional comparisons pass. The full suite remains2/4 because its coarse comparisons are part of the frozen contract. In31_dir_10084 entry(91,91), the coarse/fine change is2.4059100e-5; in31_dir_10134 entry(84,84), it is1.5641498e-5 eV/Angstrom^2. Their nearest angular crossings lie at7.581725e-6 and8.552198e-6 Angstrom, between fine6.25e-6 and coarse1.25e-5. Each coarse stencil crosses25 -0.5 angle triples; fine and audit cross none. The fresh cos(sqrt(3)*index) direction in31_dir_10084 changes1.0974207e-6 between coarse2.5e-5 and fine1.25e-5, but only2.1289343e-7 between fine and audit. Its angular crossing is at1.4279540e-5 and again only the coarse stencil crosses25 triples. This is source/geometry correlation, not newly isolated proof of the responsible force term. FAILURE_LOCALIZATION.json preserves the post-result diagnostic.

Guarding only the retained stencil is insufficient to guarantee a three-stencil convergence window. The protocol deliberately permits coarse crossings and correctly reports their failures. No failed coarse comparison is discarded, no thresholds change, and no full-family promotion follows from the passing fine/audit pairs.

## Interpretation and limits

The new suite qualifies 2/4 members of the fixed-cell, primitive-periodic, affine-constrained stationary family at cutoff24 Angstrom and imposed width2 Angstrom smooth KCz. It does not requalify the old 36-member family at these stationary coordinates. The model retains fixed normals, ideal constraint reactions and restricted spatial sectors. Minimum eigenvalues and coarse/fine spectral discrepancies are local numerical diagnostics, not certified nonlinear, full-cell or Bloch stability.

Lateral/vertical coupling is conservative. A qualified positive finite stiffness can support exact finite-memory elimination within that model, but does not supply a physical reservoir, dissipation/noise relation, native clock, UD-to-material correspondence or measured friction. Conventional matched models remain available. No observed headline establishes friction exactly zero or a UD-specific mechanism.

The historical v0.39 ledger cannot overrule the recovered v0.85 retirement of universal G05 or the still-open Q162/Q163 protected-mode and clock gates. No 4/3 quantity is interpreted as kg/s damping. The six source attachments remain placeholders; Gap2_FINAL_Finite_Genesis.png remains unavailable.

## Verification

Constructor checks reproduce input and executable hashes, the isometric basis, geometry-selected steps, raw-force derivatives, spectra and directional errors. The executable hash record was emitted after worker launch but before any full matrix result existed; per-case geometry selection was written before that worker sampled forces. This is a transparent process record, not a stronger chronology claim. Independent non-constructor review remains OPEN. Raw arrays and source inputs are supplied for replay.

A — NUMERICAL: four stationary geometries preserved; full three-step matrix and six-direction suite evaluated.
B — RESULT: 2/4 pass this new protocol; prior protocol records unchanged.
C — OPEN/HOLD: independent review, broader stability and physical/native bath.
D — Physical promotion 0; Development — no registry entry.

1. Next: freeze a convergence contract that guards every acceptance stencil and controls roundoff; check the three failing probes before another full run. Priority97/100.
