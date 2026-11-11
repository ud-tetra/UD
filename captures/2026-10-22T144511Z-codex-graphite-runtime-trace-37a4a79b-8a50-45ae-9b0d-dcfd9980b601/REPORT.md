# Runtime REBO angular-force trace at the held graphite stencils

22 October 2026. Development capture extending draft PRs #381, #389 and #392; physical promotion **0**. The original full 81-coordinate Hessian qualification remains **HOLD**. This is a constructor diagnostic, pending independent review. No coefficient for residual friction or its load dependence is inferred here.

## Method and source

The original LAMMPS `stable_22Jul2025_update4` source commit `611ca3b7f8525ba802373b04f9e3d632d515f7e3`, `src/MANYBODY/pair_airebo.cpp` SHA-256 `cbe2b802e554212d2a2244d30ecd26f4d48c1fcebe5a9cb20610b643c12b0a58`, was copied and instrumented with a per-call log after the direct `gSpline` angle-gradient force vectors are formed in both bond-order loops. `source.patch` records every edit; `register.cpp` wraps the original `PairREBO`. The fixed potential `CH.rebo` has SHA-256 `70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4`. The compiled diagnostic plugin SHA-256 is `80b511dd88cfa6db9d15705709f36d6b37a40892a6d703248a3b86ab098402bf`. The original built-in style was run alongside this instrumented source copy, with identical first-layer-only `rebo` settings, cell and coordinates. The archived PR #381 reference was compared only to its matching first-layer REBO projections; its separate seven-step raw vector includes both layers.

The replay samples the baseline and four offsets for each of seven steps (29 positions per case), using the frozen candidate coordinates and probe directions, `34/8` for `21_dir_0` and `30/4` for `21_dir_10024`. For a projected force `F`, the signed side stiffness difference is

`S(h) = -[(-3F(0)+4F(h)-F(2h))-(3F(0)-4F(-h)+F(-2h))]/(2h)`.

Per-call vectors are projected on the same probe and passed through the same stencil. The middle-step NPZ files retain ordered atom triples, cosine, coordination, segment label, `g`, `dg/dcos`, five projected forces and each call's side response. They contain 3,024 first-layer ordered calls, with carbon coordination 2. The paired Python source-equation record comes from the PR #392 approach restricted to this same first layer. It is a cross-check of the logged term, not an independent experimental observation.

## Checks and result

At **all 29 positions in each case**, every raw plugin force component equals the built-in first-layer REBO force component exactly in the recorded binary64 arrays (maximum absolute difference 0.0 eV/Å). Archived first-layer projected samples agree within 4.039e-12 and 2.959e-12 eV/Å, respectively. In the five middle-step positions, the runtime and Python records have identical ordered atom triples; maximum cosine discrepancies are 2.19e-14 and 2.29e-14; maximum individual projected direct-angle force discrepancies are 1.06e-14 and 9.80e-15 eV/Å. Segment labels disagree in 152 and 430 record entries only where cosine is within 1e-12 of -0.5, a floating-point boundary; the corresponding force values still agree to those bounds.

At `h=2e-5 Å`:

| Case / probe | Full first-layer runtime S | Logged direct angle S | Full minus logged direct angle | Segment-changing call contribution |
| --- | ---: | ---: | ---: | ---: |
| `21_dir_0` / 34,8 | -7.253824451e-5 | -7.266073379e-5 | +1.224892854e-7 | -7.265363217e-5 (536 calls) |
| `21_dir_10024` / 30,4 | -7.782659914e-5 | -7.775294678e-5 | -7.365236350e-8 | -7.775989809e-5 (360 calls) |

All response columns use eV/Å². Remaining unchanged-segment direct-angle sums are -7.10e-9 and +6.95e-9 eV/Å². `runtime_trace_verification.json` checks ID ordering, per-call/stencil closure and partitions. The seven-step ladders are in each `*_runtime_trace.json` and show shrinking-step numerical instability. This calculation uses a reconstructed candidate geometry: its first-layer force differs from PR #381's archived first-layer projection by several 1e-12 eV/Å. Division by `h` makes the last displayed remainders sensitive to that difference. They do **not** represent a stable remaining physical stiffness, unique torsional contribution, UD coefficient, or load response.

The first-layer logged direct angle term explains the dominant side discrepancy in this numerical model. This upgrades PR #392's source-equation reconstruction to an instrumented-source term trace with whole-force equality to the unmodified runtime. The source edit does not prove a decomposition of *all* REBO force paths, and the spline-join segment labels near 120° are roundoff sensitive. PR #392's 6,048-call Python record included both layers; the present comparison is deliberately 3,024 first-layer calls and has its own reported numbers. The prior 0.14–0.18 eV/Å provisional whole-force mismatch from omitted torsional bond-order terms remains rejected.

## Reproduction and status

`build_rebo_trace.py` applies the exact edit after checking the source hash. It expects the pinned LAMMPS checkout at `lammps-source`, headers from that checkout staged in `graphite-trace/include`, and the 22 Jul 2025 LAMMPS runtime and MPI headers/libraries. The reference build command is:

```sh
g++ -std=c++17 -O2 -fPIC -shared -Wl,-Bsymbolic -I graphite-trace/include -I lammps-runtime/lammps/include/lammps -I mpi-runtime/include -I lammps-source/src/MANYBODY -I graphite-width/plugin graphite-trace/pair_airebo_trace.cpp lammps-source/src/MANYBODY/pair_rebo.cpp graphite-trace/register.cpp -L lammps-runtime/lammps -llammps -o graphite-trace/rebo_udtrace.so
```

`replay_rebo_trace.py` expects the copied `candidate.npz`, frozen `struct.inp.data`, archived PR #381 `*_projected.npz` / `*_ladder_raw.npz`, and source `CH.rebo` placed at the paths visible in the script; these inputs and dependencies are pinned by hash or named source. Copy the two data files into `graphite-target-replay/selected/21/dir_0` and `.../dir_10024` under their original `struct.inp.data` name. The plugin binary and GPL-2.0 license are retained for exact artifact comparison; loading this binary requires a compatible runtime. The verifier can independently check the captured records and receipts after placing them together in a directory with NumPy. The separate seven-step and middle-step receipts were constructor checked, not independently reviewed.

Next scientific gate: obtain an independent term-level replication and error budget for the full Hessian; then, if a stable remainder exists, test a preregistered load and twist protocol against conventional REBO/KC and moiré baselines. A residual dissipation law cannot be derived from this conservative static-force trace alone. `Gap2_FINAL_Finite_Genesis.png` was unavailable in this workspace and was not used.
