# Boundary-aware derivative qualification

Development — no registry entry. Physical promotion0. Constructor: Codex. Non-constructor review pending.

RESULT: 0/2 cases pass the revised frozen numerical protocol. The earlier same-branch and v0.1 preflight failures retain their original status.

| Case | one-sided difference (eV/Å²) | largest side step change (eV/Å²) | min stiffness (eV/Å²) | result |
|---|---:|---:|---:|---|
| 21_dir_0 | 7.265e-05 | 1.99988e-05 | 0.00349665853 | HOLD |
| 21_dir_10024 | 7.78066e-05 | 2.08734e-05 | 0.00349665861 | HOLD |

Each case uses81 columns plus9 normalized directions; every probe has three fixed step sizes. Independent one-sided formulas, adjacent-step comparisons, reverse sample repeats, matrix symmetry, directional checks, stationarity and a spectral stability diagnostic govern acceptance. All stored raw force samples and failed flags remain in the archive.

21_dir_0 failed checks: one_sided_agreement, one_sided_step_stability, averaged_step_stability, directional.

21_dir_10024 failed checks: one_sided_agreement, one_sided_step_stability, averaged_step_stability, directional.

The first new protocol allowed only baseline-near triples to cross-1/2; it failed geometry and all four worker assertions stopped before force collection. v0.2 permits all crossings of the same source-verified C2 join, adds one-sided coordinate diagnostics and keeps the derivative thresholds unchanged. Both active preflights pass. A supplementary cosine-displacement bound leaves more than0.166 separation from the other two angular knots. This is floating-point geometry verification, not a directed-rounding interval proof.

Exact rational source checks show scalar angular continuity through second derivative. They do not establish analytic smoothness of every force term or identify UD-native coefficients. One-sided second-order accuracy is conditional on the local Taylor regime; the protocol imposes observed agreement and does not assume that regime across interior crossings.

All results refer to the unchanged released stationary references, fixed cell and primitive-periodic81-coordinate family. No global-minimum or full-supercell stability claim, physical bath, clock, friction or UD identification follows. Different source labels need not identify different final minima.

A — EXACT CONDITIONAL: one-sided stencil identities and source-polynomial C2 joins.

B — NUMERICAL: case-specific qualification and independently recomputed constructor integrity.

C — OPEN: non-constructor review and physical correspondence; physical promotion0.

D — NEXT: isolate REBO versus KCz for columns34 and30 (zero-based), then test a targeted step ladder with branch tracing before repeating any full matrix. Priority98/100.

Post-run localization: the worst fixed probes are column34/component8 for21_dir_0 and column30/component4 for21_dir_10024. Side disagreement decreases only modestly across the tested halving ladder and remains above5e-5 eV/Å² at the finest step. The three levels do not establish an asymptotic convergence regime or unique cause. LOCALIZATION.json includes every probe failing any absolute or relative side/step test.
