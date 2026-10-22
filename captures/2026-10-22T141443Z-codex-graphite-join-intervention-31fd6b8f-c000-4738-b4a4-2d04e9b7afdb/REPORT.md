# Reconstructed graphite probe and carbon angular join intervention

22 October 2026. Development — no registry entry. Physical promotion **0**. This append-only capture extends draft PR #386 with fresh force evaluations; it does not alter the released PR #334 or PR #381 records. The original full 81-coordinate Hessian remains **HOLD**.

## Identity and numerical fingerprint

The original Zenodo `lammps_21.tar.gz` SHA-256 `d19342e8bec227a99a167930c4ca25972e79f7410f47b036959262a7af838b08` supplied the two byte-verified `struct.inp.data` members. `reconstruct_21.py` uses their periodic 28-group/81-coordinate basis and source model, relaxes vertical coordinates, then solves projected stationarity including two relative-slide coordinates. This is an independent numerical reconstruction, not a recovered byte-identical `RELAXED.npz`. Its rebuilt KCz plugin has different bytes from the original plugin. Candidate positions and basis are captured in the two `candidate.npz` files, which are outputs of the constructor, not independent certified source data.

The reconstructed relative slides equal the released values to about 1e-14 Å in both cases; projected stationary forces are at most 1.93e-12 eV/Å. For each case, `compare_reconstruction.py` ran the original potential and compared **all 81 projected force components** at the archived baseline and eight `±h` probe points (`h` 4e-5, 2e-5, 1e-5, 5e-6 Å). Maximum differences are 4.04e-12 eV/Å for first-layer REBO, 7.87e-15 eV/Å for KCz, and 4.04e-12 eV/Å for the total. These numerical checks support use of the reconstructed geometry for the held probe diagnostic, but do not prove byte identity or replace an independent Hessian review.

## Geometry at the C2 join

The actual held probe vectors are basis columns 34 and 30, as specified by the PR #334 preparation code (`np.eye(81)` precedes its nine directional probes). `trace_angular_geometry.py` independently finds three same-layer nearest neighbors with periodic images. It finds 432 angles per case within 1e-12 of cos(theta)=-0.5 at the baseline. The main nonzero crossing-offset clusters in Å are:

| Case | Offset clusters from baseline (count each) |
| --- | --- |
| `21_dir_0` | -1.5029e-5 (36), -3.002e-6 (36), +2.502e-6 (36), approximately zero (144) |
| `21_dir_10024` | -3.468e-5 (36), -1.7357e-5 (36), -2.889e-6 (36), +2.477e-6 (36), +3.468e-5 (36) |

Near-zero branch counts can change with roundoff and the precise LAMMPS bond image convention: the first case's independently reconstructed 80 µÅ count is 252 versus PR #381's 254; the second case's 180 agrees. These geometric counts are **not** a source-level log of `gSpline` calls or projected term-level forces.

## Controlled potential intervention

The original `CH.rebo` SHA-256 is `70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4`. In copies only, `diagnose_join_counterfactual.py` continues either the right-hand or left-hand carbon `gC` polynomial across its cos(theta)=-0.5 join, replacing just the six coefficients of the adjacent interval in **both** `gC1` and `gC2`. It reruns first-layer REBO at the **same** reconstructed reference positions and the same unmodified probe displacements. This is a changed-potential control; its baseline is not re-equilibrated and it is not a new physical reference.

At `h=2e-5` Å, with `S=Qplus-Qminus` and `Q=-dF/dx`:

| Case | Original S (eV/Å²) | Right continuation S | Left continuation S |
| --- | ---: | ---: | ---: |
| `21_dir_0`, probe 34, component 8 | -7.26499955e-5 | +1.25053527e-7 | +1.24741623e-7 |
| `21_dir_10024`, probe 30, component 4 | -7.78065808e-5 | -6.36558823e-8 | -6.64646143e-8 |

The absolute discrepancy falls by 99.83% and 99.92% under right continuation at this step. Both continuation directions give the same order of suppression. Across 80, 40, 20, 10 and 5 µÅ, the right-continuation target-component differences are below 3.11e-7 eV/Å². At the smallest steps numerical force subtraction has appreciable error; the counterfactual side **maxima over all 81 components** can still exceed the original 1e-6 qualification threshold. `RESULTS.json` and the per-case JSON files give every step, full-vector maxima and numerical fingerprints.

This intervention strongly ties the held target-component mismatch to the carbon angular spline join **within this specific REBO simulation**. It does not identify each contributing atom triple or isolate its `g`, `dgdc`, coordination and bond-order prefactors in the original unmodified runtime. Copying a segment also changes the model over its whole angular interval, including its baseline force and stiffness. It is not evidence for a UD-specific residual friction term or a numerical load-response coefficient. PR #386's single-hinge fitted offsets remain descriptive only; the multiple geometric crossing clusters show why a single fitted offset is not an observed crossing.

## Reproduction and gate

Run the scripts on verified source members with the version-matched LAMMPS 2025-07-22 Python runtime, `CH.rebo`, `CC.KC`, a KCz width-2 plugin and NumPy/SciPy; `reconstruct_21.py` also requires the source archive extracted into `graphite-target-replay/selected/21/`. Replaying force comparisons requires PR #381's `*_projected.npz` arrays. The copied potential hashes and all captured output hashes are recorded. This constructor check is not independent review. The original 81-coordinate qualification remains **HOLD**, and physical promotion remains **0**. Any quantitative friction/load prediction still needs a sourced mechanical loading protocol, dynamical dissipation parameters and experimental residual series.
