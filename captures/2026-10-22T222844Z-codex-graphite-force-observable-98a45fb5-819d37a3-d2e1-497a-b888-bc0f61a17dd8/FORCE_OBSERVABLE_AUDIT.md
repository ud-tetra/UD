# From barrier to measured force: model-dependent bridge

Status: EXACT_CONDITIONAL 1D driven model with NUMERICAL illustrations; development — no registry entry; physical promotion 0.

Derivation: For U=Delta/2*(1-cos kx), Fc=kDelta/2=pi Delta/ell. At F>Fc, gamma dx/dt=F-Fc sin kx. The period integral equals gamma ell/sqrt(F^2-Fc^2), yielding F_drive=sqrt(Fc^2+(gamma v)^2). Its derivative at fixed v includes both Fc' and gamma'. The excess estimator subtracts gamma v and has a different derivative when gamma depends on P. Locally, positive gamma laws with specified derivatives can cancel either force slope, demonstrating a force-observable identifiability obstruction.

The 75.18 μeV/atom barrier and 0.033228 μeV/atom/MPa slope are rounded numerical inputs from the conditional 16 Å two-shell KC reconstruction in preceding draft PR #428. The 0.929608 Å period comes from a 2023 conventional deposited-grid nearest translation. A sinusoid with these inputs has a force shape distinct from the actual two-shell PES. The model contains arbitrary illustrative gamma and v; it is not calibrated to Chen et al. (2026). The APS article and supplement are marked subscription required, so no experimental force trace or estimator was ingested.

Checked: numerical quadrature for all three reduced speeds reproduces the exact velocity; centered pressure differences reproduce analytic slopes; both drag-slope cancellations have zero first derivative by algebra. Inputs and outputs are recorded in FORCE_OBSERVABLE_RESULTS.json. No dataset program was executed in this turn.

To turn this into a physical comparison, obtain the measured lateral force estimator, load range and uncertainty, angular contact geometry, rate and temperature series, and independently calibrated damping; simulate the corresponding conventional force model, then evaluate a source-derived UD residual without fitting it to the target traces. The supplied UD coefficient ledger's normalized event-time and damping coefficients cannot be directly used as physical graphite drag without a time and material map.
