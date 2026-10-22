# Sliding-port memory: results

RESULT: 4/4 port extensions and 8/8 prescribed-motion checks PASS. Development — no registry entry. Physical promotion 0.

The two relative-layer lateral coordinates are now explicit. Internal reference H remains unchanged. New force derivatives satisfy every-stencil branch/representation controls, adjacent-step agreement and nine-direction reciprocity per case.

| Case | min relaxed port stiffness (eV/Å², normalized r) | max reciprocity error (eV/Å²) |
|---|---:|---:|
| 21_dir_0 | -0.00221120322 | 9.58e-08 |
| 21_dir_10024 | -0.00243896018 | 4.7e-08 |
| 31_dir_10084 | -0.0011210128 | 2.37e-08 |
| 31_dir_10134 | 0.000397463976 | 5.25e-08 |

Maximum reduced versus full required-force error: 1.1858569681777453e-14 in normalized units. Eight preparations: zero internal state and nonzero internal displacement/velocity for each reference. Direct 192-node quadrature supplies an additional constructor cross-check.

Three references have a negative relaxed sliding-stiffness direction; only 31_dir_10134 has positive relaxed port stiffness, and it still has a nonzero baseline port force. Internal stationarity must not be confused with free sliding equilibrium. Clamp bias is retained explicitly. Negative eigenvalues are numerical harmonic diagnostics, not an interval-certified nonlinear instability theorem.

All middle derivatives and baseline repeats reproduced bit-identically. Largest adjacent derivative change: 3.3833991119891493e-07. Largest port relative change: 3.4012111563341015e-06.

A — EXACT CONDITIONAL: orthogonal port construction, unit conversion and finite harmonic memory identity.

B — NUMERICAL: four force extensions, eight driven linear checks, retained raw forces/trajectories and constructor quadrature.

C — OPEN: full entrywise reciprocal remeasurement, nonlinear driven validation, physical bath/clock, UD correspondence and non-constructor review. No steady friction claim.

D — NEXT: release the lateral clamps and locate genuinely stationary sliding registries; requalify their stiffness before a free-response or bath interpretation. Priority 97/100.
