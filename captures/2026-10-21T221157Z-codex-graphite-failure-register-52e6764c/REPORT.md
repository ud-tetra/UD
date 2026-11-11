# Complete failure register — qualification v0.2

RESULT / STATUS: full branch-aware suite remains 2/4 PASS, with 21_dir_0 and 21_dir_10024 passing. Full-family qualification remains HOLD. All four fine/audit matrix pairs and all24 fine directional comparisons pass. Independent review and physical/native bath remain OPEN/HOLD. Physical promotion0. Development — no registry entry.

The v0.1 localization selected the worst entry of each failed matrix. It did not enumerate every failed column. The earlier three-probe recommendation is superseded by the complete five-probe register below. No raw arrays, numerical flags, thresholds or case outcomes change; all prior bytes remain preserved.

| Case | Failed probe | Largest adjacent change, eV/Angstrom^2 |
|---|---|---:|
|31_dir_10084|column12|1.9625011e-6|
|31_dir_10084|column60|1.9944872e-6|
|31_dir_10084|column91|2.4059100e-5|
|31_dir_10134|column84|1.5641498e-5|
|31_dir_10084|fresh cos(sqrt(3)*index) direction|1.0974207e-6|

Indices are zero-based. These are all columns/directions failing the absolute adjacent-step gate. Relative, symmetry, stationarity and fine directional-agreement gates pass. Each listed coarse stencil crosses25 angle triples at the -0.5 carbon gC knot; its fine and audit stencils cross none. This is numerical/source-geometry correlation; no new component isolation establishes unique term attribution. Every retained fine stencil passed the separate nine-point branch guard.

Guarding the retained step alone did not ensure branch-safe coarse comparisons. The frozen protocol explicitly allowed coarse crossings, and its resulting failures are retained. Do not discard them to claim four-case qualification. A positive spectrum and passing finer pair cannot overrule the full declared suite.

The package contains the immutable v0.1 archive, which holds the frozen protocol, all raw force data, matrices, potentials, source geometry, scripts and constructor checks, plus this correction and complete register. The complete scan recomputes failed sets directly from all raw matrix and directional arrays. Constructor verification is not non-constructor review.

A — NUMERICAL: full matrices and24 directional comparisons evaluated.
B — RESULT:2/4 full-suite PASS; complete register4 columns plus1 direction.
C — HOLD: full-family qualification, independent review and physical/native bath.
D — Physical promotion0; Development — no registry entry.

1. Next: freeze a convergence contract that guards every acceptance stencil and controls roundoff; check these five probes before another full run. Priority97/100.
