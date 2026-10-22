# Held graphite stencil: pointwise transfer and residual resolution audit

22 October 2026. Development — no registry entry, independent review pending, physical promotion **0**. This append-only capture extends draft PR #394's source-copy angular trace and the frozen PR #381 first-layer force projections. The full 81-coordinate Hessian remains **HOLD**. Nothing below is an experimental friction or load response.

## Question and exact stencil sensitivity

Can the small `full REBO minus direct carbon angular` side-stencil response from PR #394 be transferred from its reconstructed geometry to PR #381's archived first-layer force samples with a sign or magnitude certificate? For projected force `F` at `0, +h, +2h, -h, -2h`, the signed side stiffness difference is

\[S_h(F)=\frac{6F(0)-4F(h)+F(2h)-4F(-h)+F(-2h)}{2h}.\]

If two sampled force arrays differ by at most `epsilon` eV/Å at each of those **five points**, the triangle inequality gives `|S_h(F)-S_h(G)| <= 8 epsilon/h` eV/Å². This coefficient is the operator norm under a pointwise infinity-norm error model. It is exact algebra, conditional on the stated per-point bound. The observed maxima here are differences between two recorded numerical preparations, **not** certified solver error bounds for all geometries or a physical uncertainty distribution. Common-mode correlations can make the actual shift smaller; the pointwise receipts record that shift too.

`point_error_budget.py` replays built-in first-layer REBO on the reconstructed candidate coordinates at the nine archived offsets per case using the pinned LAMMPS/Potential setup from PR #394. Its signed replay-minus-archive differences and all nine projected pairs are in `point_error_budget.json`. `audit_residual_transfer.py` independently reapplies the coefficient vector to those stored differences and checks the archived NPZ values and retained PR #394 middle-step term records. The two archive NPZs, candidate coordinates, and source data are copied byte-for-byte here; the original potential is public LAMMPS `CH.rebo` SHA-256 `70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4`.

## Results at the middle step

At `h=2e-5 Å`:

| Case / held probe | PR #394 full-minus-direct S | Actual replay-minus-archive S | Max observed point difference epsilon | Conditional 8 epsilon / h | Needed epsilon for this bound < absolute remainder |
| --- | ---: | ---: | ---: | ---: | ---: |
| `21_dir_0` / 34,8 | +1.22489e-7 | +1.11751e-7 | 1.80703e-12 | 7.22813e-7 | <3.06223e-13 |
| `21_dir_10024` / 30,4 | -7.36524e-8 | -2.00183e-8 | 2.19795e-12 | 8.79180e-7 | <1.84131e-13 |

Force-point entries use eV/Å; all S and bounds use eV/Å². The conditional bounds are **5.90 and 11.94 times** the magnitudes of the corresponding runtime remainders. They do not certify either remainder's transfer to the archived calculation. The actual replay shifts are about 91% and 27% of the respective runtime remainders, with signs shown. A tempting subtraction of PR #394's direct term from PR #381's full S would mix two coordinate preparations and is not a valid isolated physical response.

At `h=1e-5 Å`, the pointwise bounds rise to 1.446e-6 and 1.758e-6 eV/Å². At `h=5e-6 Å`, they are 1.420e-6 and 3.155e-6 eV/Å². The PR #394 runtime full-minus-direct ladder does not stabilize across these steps: case 0 goes `+1.225e-7, +1.057e-7, +3.223e-9`; case 10024 goes `-7.365e-8, +1.101e-8, -2.639e-7` eV/Å². The smaller steps in the seven-step source trace are noisier still. At the middle step, summing the C++ versus Python per-call angular force values before applying the stencil changes the direct angular side by `-4.79e-9` and `+8.94e-9` eV/Å², respectively. This is another numerical cross-evaluation diagnostic, not an independent force experiment.

## Decision and next gate

**NO-GO for a numerical residual-friction or load-slope claim from this stencil.** The direct carbon angular contribution remains a strong explanation of the dominant *conventional model* discrepancy, but the remainder is below the present archive-to-replay pointwise transfer resolution and has no stable step plateau. It cannot be assigned a UD amplitude. Moreover, these are conservative static force derivatives; dissipation and load dependence require an explicit dynamics/observable protocol and actual load-series data. A two-angle sum of 60° supplies a symmetry pairing, not an independent dissipative coefficient.

The next computational gate is a single pinned coordinate/force preparation that logs the remaining REBO bond-order paths and reports a residual across at least three steps with a verified numerical error envelope below the putative signal. Only then should a pre-registered friction experiment compare load slopes at both complementary angles against a conventional honeycomb/moiré/REBO/KC baseline. Any UD excess coefficient requires a source law and held-out observations, with non-constructor adversarial review before promotion. `Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used.

Reproduction: place the captured files together, then run `python3 audit_residual_transfer.py` with NumPy. The fresh LAMMPS replay script additionally expects the runtime/source layout of PR #394 and the copied `struct.inp.data` files staged at its indicated paths. It is constructor verification only.
