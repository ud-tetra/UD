# Carbon angular join: source-bound stencil signature

22 October 2026. Development — no registry entry. Physical promotion 0. This is a **source and archived-force diagnostic**, not a new force evaluation, atom-resolved trace, graphite friction fit or UD coefficient. Draft PRs [#334](https://github.com/ud-tetra/UD/pull/334), [#378](https://github.com/ud-tetra/UD/pull/378) and [#381](https://github.com/ud-tetra/UD/pull/381) remain distinct and unmerged at this capture.

## Source result

The LAMMPS `stable_22Jul2025_update4` source at commit `611ca3b7f8525ba802373b04f9e3d632d515f7e3`, `pair_airebo.cpp` SHA-256 `cbe2b802e554212d2a2244d30ecd26f4d48c1fcebe5a9cb20610b643c12b0a58`, evaluates `gSpline(cosjik, NijC+NijH, ...)` inside REBO bond order, and evaluates it again along a `dgdc` force path. Its carbon spline selects `gC1` at coordination `Nij<=NCmin` and `gC2` at `Nij>=NCmax` (`NCmin=3.2`, `NCmax=3.7` in the parameter file). This source inspection does **not** establish which path or exact neighbor triples the held geometries actually traverse. `PairREBO` inherits this implementation.

Exact decimal arithmetic on the version-matched `CH.rebo` SHA-256 `70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4` shows that both `gC1` and `gC2` have identical first three polynomial segments, through `cos=-1/3`. At their `cos=-1/2` join, right minus left derivatives of order 0, 1 and 2 are exactly zero under the printed decimal coefficients. The third derivative jump is `24.334074`. Thus merely changing the `gC1/gC2` coordination selection cannot distinguish the two scalar angular polynomials at this join. Other coordination contributions or bond-order paths may still matter in the full force.

## Why a broad side-difference plateau is possible

Let `x` be a physical displacement in Å along a held probe and let a *hypothetical* contribution to its projected force be `F_join(x)=B(x-t)_+^2` in eV/Å. Here `t` is the displacement at which one angular triple crosses the join; this is a local surrogate for the C2 angular spline composed with its force prefactor, not a fitted physical law. For the two second-order one-sided derivative formulas used by PR #381, its side difference is exactly

`S(h)=B[-6p(0)+4p(h)+4p(-h)-p(2h)-p(-2h)]/(2h)`, where `p(x)=(x-t)_+^2`.

At `t=0`, `S(h)=0` for every `h` in this leading-order model. At `0<|t|<h`, it is `B[-2t+(3/2)sign(t)t²/h]`. Hence a *shifted* join can give an almost constant discrepancy for `h>>|t|` and a collapse after the stencil stops crossing it (`h<|t|/2`). The side-difference kernel alone is invariant under jointly reversing `B,t`; it cannot determine the sign of the offset. An ordinary smooth force contribution has a leading side-difference term proportional to `h³` if it has four local derivatives. These are mathematical conditional statements, not proof that this join causes the observed mismatch.

## Archived array check

`analyze.py` validates exact hashes for the potential, source, published `LADDER.json` and both PR #381 raw projected-force arrays. It independently reconstructs the seven side differences from raw baseline and four sampled forces at each step. The observed `|S(80 µÅ)|/|S(1.25 µÅ)|` is `47.67` for `21_dir_0` and `96.69` for `21_dir_10024`. A descriptive single-hinge plus cubic-in-`h` fit over all seven *exposed* points gives effective `|t|` values `2.63e-6` and `2.58e-6` Å, but maximum residuals remain `4.12e-6` and `3.66e-6` eV/Å². These fitted offsets are **not measured angle offsets or predictions**: many triples can contribute, all seven points were used, the assumed remainder is only illustrative, and the residuals exceed the original `1e-6` side-agreement scale. The coefficient `B` is a descriptive projected-force coefficient in eV/Å³ and is not a UD parameter.

## Actual next discriminating experiment

Reacquire the previously hash-identified `RELAXED.npz`, `PLAN.npz`, selected original data files and matching LAMMPS runtime from PR #334's external source chain. Instrument the version-matched `gSpline` calls at the frozen `(34,8)` and `(30,4)` probes, recording atom triple IDs, `cosjik`, `Nij`, selected segment, `g`, `dgdc`, relevant prefactors and **projected angular/coordination force contributions** at `x0, ±h, ±2h` for each declared step. Compare the sum of term-level forces to the unmodified REBO values within a prespecified tolerance before attributing the side difference. A source patch or altered potential must be distinguished from the original physical run. The source data and binary runtime are not included in the compact GitHub capture, so the term-level check remains **OPEN**.

The full 81-coordinate derivative qualification remains **HOLD** for both `21` references. Neither a converged Hessian nor a residual friction or load response follows. PR #378's conditional dissipative-mode equation remains a hypothesis awaiting material/UD coupling, bath and experimental series.

Reproduction: `python3 analyze.py --potential <verified CH.rebo> --source <verified pair_airebo.cpp> --ladder <PR381 LADDER.json> --raw-dir <PR381 array directory> --output <fresh RESULTS.json>`. The script rejects hash mismatches; `RESULTS.json` is this constructor's output.
