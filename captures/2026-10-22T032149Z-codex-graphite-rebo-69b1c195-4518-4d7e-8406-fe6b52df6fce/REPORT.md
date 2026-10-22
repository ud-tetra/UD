# Targeted graphite REBO/KCz derivative localization

**Result:** the two exposed worst-probe one-sided derivative discrepancies are
localized to the *first intralayer REBO interaction* in the declared
REBO+smooth-KCz atomistic model. The prior full-matrix `21` qualification
remains **HOLD**. This result is numerical, model-scoped, constructor-checked
and not an experimental friction measurement. Development — no registry entry;
physical promotion 0.

## Motivation and provenance

Draft [PR 334](https://github.com/ud-tetra/UD/pull/334) contains the
boundary-aware 81-coordinate qualification of two released stationary `21`
references. At its fixed $h=2\times10^{-5}$ Å, its worst probes are
column/component `(34,8)` and `(30,4)`, with one-sided differences
`7.265001257e-5` and `7.780662771e-5` eV/Å². Both cases failed multiple
frozen derivative checks. The numerical diagnostic here was selected **after
exposure to those failures**, so it is not a new blind pre-registration and
does not revise the original thresholds.

The source geometry, two stationary references, fixed neighbor construction,
plugin/potential bytes and sampled probe vectors come from the earlier
archive. `diagnose.py` checks all declared input hashes in its `FREEZE.json`
before running and uses separate LAMMPS instances at the *same* nine
Cartesian configurations per case. It measures total, intralayer REBO,
first-layer REBO, second-layer REBO, and interlayer KCz projected force. The
two component-only simulations explicitly mark unassigned pairs `none`.

## Component result

| Case and fixed worst probe | Total one-sided difference | First-layer REBO | KCz (fixed component) | Max force-additivity error |
|---|---:|---:|---:|---:|
| `21_dir_0`, `(34,8)` | $-7.265001105\times10^{-5}$ | $-7.264999548\times10^{-5}$ | $+1.82\times10^{-11}$ | $1.5821\times10^{-15}$ |
| `21_dir_10024`, `(30,4)` | $-7.780662771\times10^{-5}$ | $-7.780658083\times10^{-5}$ | $-3.37\times10^{-11}$ | $1.6376\times10^{-15}$ |

All differences have units eV/Å²; force additivity errors have units eV/Å.
The REBO-alone and two-layer sum also reconstruct at each stored point; the
largest REBO-layer force-additivity errors are $2.78\times10^{-17}$ and
$1.21\times10^{-19}$ eV/Å. The second-layer contribution to either displayed
fixed component is zero under these two selected coordinate displacements.
Across *all* projected components, the maximum KCz side difference at the
largest original stencil is $1.79\times10^{-10}$ and
$1.65\times10^{-10}$ eV/Å² respectively. This localized REBO mismatch is at
least $4.0\times10^5$ times larger than that KCz bound. The raw projected
forces are retained in the two `*_projected.npz` files; `verify.py` recomputes
the decomposition and matches the earlier total-force worst-probe results.

The original total projected force at each stationary reference is near zero
(here $8.2\times10^{-12}$ and $6.2\times10^{-12}$ eV/Å in norm), but its
separate REBO and KCz baseline forces are approximately equal and opposite,
each of norm $0.86017$ eV/Å. Their cancellation checks stationarity of the
*total* model; it must not be construed as individually stationary layers.

## Exploratory REBO-only step ladder

The separate `ladder.py` scans the fixed probes at seven $h$ values, spanning
$8\times10^{-5}$ to $1.25\times10^{-6}$ Å. Its source-traced C2 join is
$\cos\alpha=-1/2$; 432 angle triples in each reference lie within
$10^{-12}$ of the join. Branch-count classifications below use floating-point
angles at sampled geometries and are **diagnostics**, not a proof of runtime
control flow.

| $h$ (Å) | `21_dir_0` REBO side | `21_dir_10024` REBO side | plus/minus branch counts, first/second |
|---:|---:|---:|---:|
| $8\times10^{-5}$ | $-7.2914\times10^{-5}$ | $-7.8100\times10^{-5}$ | 254 / 180 |
| $2\times10^{-5}$ | $-7.2650\times10^{-5}$ | $-7.7807\times10^{-5}$ | 254 / 108 |
| $5\times10^{-6}$ | $-5.1056\times10^{-5}$ | $-5.4763\times10^{-5}$ | 218 / 72 |
| $2.5\times10^{-6}$ | $-1.5695\times10^{-5}$ | $-1.8128\times10^{-5}$ | 144 / 36 |
| $1.25\times10^{-6}$ | $+1.5296\times10^{-6}$ | $-8.0776\times10^{-7}$ | 144 / 0 |

The full seven rows, actual one-sided estimates and effective Cartesian
input-direction errors are in `LADDER.json`; raw projected forces are in
`*_ladder_raw.npz`. Even at the finest step, the first case exceeds the old
$10^{-6}$ absolute one-sided threshold, and the adjacent-step stability
check would still fail. Selecting a fine step *after seeing this ladder*
cannot qualify the full 81-column Hessian. The scalar `CH.rebo` angular
spline's C2 join and the changing branch counts are consistent with a
representation-sensitive region, but do not establish which internal REBO
term causes the discrepancy or the true limiting Hessian.

## Reproduction and next gate

The archived scripts require the original PR 334 source directory, the
matching LAMMPS runtime and `UD_GRAPHITE_ROOT` pointing at the scratch
workspace containing those inputs. With the Python LAMMPS package, NumPy,
MPI libraries, plugin and potentials present, run `diagnose.py`, then
`ladder.py`, then `verify.py`. Numerical logs are local diagnostics and are
not included; the projected arrays and script inputs needed for replay are.
No imported archived script was executed merely to ingest source material.

**Next experiment:** instrument the version-matched REBO angular and
coordination branch evaluations for these same two probes, recording each
term's force contribution and selected segment at $x_0,\pm h,\pm2h$.
Compare that term-level trace with a higher-precision scalar evaluation
without changing the physical potential. Only after a source-level cause
and a convergent estimator are identified should the *unchanged released
references* undergo full-matrix requalification. An independently sourced
material/UD coupling and a dissipative bath remain separate requirements;
this diagnosis does not yield a residual friction coefficient. The paper's
abstract contains no accessible raw load- or speed-series numbers for such
a fit (Chen *et al.*, PRL **137**, 166201 (2026),
[DOI:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2)).

A — EXACT CONDITIONAL: additivity of separately defined potential forces.

B — NUMERICAL: two selected REBO/KCz force decompositions and seven-step
exploratory ladders; raw-array constructor replay PASS.

C — OPEN/HOLD: cause within REBO, complete qualified Hessian, independent
review, experimental baseline, native UD map and physical drain.

D — NEXT: term-level REBO branch trace at the two frozen probes; priority
98/100. Physical promotion 0.
