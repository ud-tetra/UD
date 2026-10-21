# Conservative lateral-memory verification v0.1

RESULT / STATUS: 4/4 qualified stationary models and 16/16 preparations pass the frozen memory checks. Exact block-elimination proposition is conditional on the stated matrix assumptions; its numerical application is constructor-checked. Physical promotion0. Development — no registry entry. Non-constructor review pending.

DERIVATION.md provides the full proof. In normalized mathematical time, partition the qualified matrix as D=[[A,C],[C.T,V]], with52/100 lateral coordinates and27/51 vertical coordinates. The eliminated vertical equation is

\[\ddot z+Sz+\int_0^\tau K(\tau-s)\dot z(s)\,ds=f(\tau),\qquad S=V-C^{\mathsf T}A^{-1}C,\]
\[K(\tau)=C^{\mathsf T}A^{-1}\cos(A^{1/2}\tau)C,\]
\[f(\tau)=-C^{\mathsf T}\cos(A^{1/2}\tau)(\ell_0+A^{-1}Cz_0)-C^{\mathsf T}A^{-1/2}\sin(A^{1/2}\tau)\dot\ell_0.\]

The specific initial-slip contribution is -K(tau)z0; the remaining initial force comes from hidden lateral displacement/velocity. Grouping them through eta0=ell0+A^-1 C z0 makes conditional equilibrium explicit. Deleting all initial forcing is permissible for ell0=-A^-1 C z0, elldot0=0, but not for arbitrary hidden preparation. The tests do not conflate these cases.

Four preparations are tested per model: vertical displacement with unrelaxed lateral coordinates; conditional lateral equilibrium at that same vertical displacement; hidden lateral displacement only; hidden lateral velocity only. The full reference uses an exact modal propagator of D. The memory solve uses an independently assembled auxiliary ODE with zero initial history and explicit initial-state forcing. Both conserve the same finite Hamiltonian energy after hidden-state reconstruction. The auxiliary realization carries2m total state coordinates; no computational state-size reduction is claimed.

| Check | Worst result | Frozen limit |
|---|---:|---:|
|Vertical position error|1.2566004e-11|1e-8 absolute;1e-7 relative|
|Reconstructed full position error|1.2566004e-11|1e-8|
|Reconstructed full velocity error|5.6940147e-12|1e-8|
|Direct history residual|2.1809743e-16|1e-9|
|96/192-node quadrature change|3.868823e-19|1e-10|
|Relative energy drift|3.7071997e-11|1e-8|
|Relative transfer identity error|9.2777521e-16|1e-10|

Time, probe amplitudes and these errors are normalized mathematical quantities, not laboratory seconds, measured dissipation or nonlinear atomistic accuracy. D is H divided by its largest eigenvalue; a common mass is absorbed into time. No native UD clock conversion is inferred. Unit-amplitude tests exploit linearity and have no large-displacement molecular claim.

## Initial-source ablation and reversibility

Omitting initial forcing produces maximum-component vertical errors from1.1123216e-05 to0.008075843 across all12 nonconditional preparations, exceeding the predeclared1e-6 visibility floor. All four conditional-equilibrium preparations still agree, with largest error1.2566004e-11. The ablation thus checks both when the source is necessary and when it vanishes.

Separate direct-history integration uses96/192 Gauss-Legendre nodes at17 times over tau0..80. Resolvent Schur identities are tested at four complex Laplace arguments per model. Spectral kernel weights are positive semidefinite, and a discrete positive-type identity is checked. Pointwise K(tau) need not be positive semidefinite. An independent first-order matrix exponential also checks the full modal reference at selected times. All are constructor tests, not non-constructor review.

The finite cosine kernel represents reversible energy exchange. Its zero-frequency Abel integral is zero because all hidden frequencies are positive; this is not a physical friction coefficient. No reservoir, dissipation/noise law, continuum limit, native material map or experimental prediction is introduced. These results are conventional consequences of the chosen harmonic matrix, rather than UD-specific discrimination.

## Numerical execution record

The first run passed all four first-case preparations, then stopped while serializing a NumPy Boolean. Original code, freeze and raw first-case arrays remain untouched. CODE_AMENDMENT.json records a writer-only scalar conversion and unique active v02 executable/output paths, with no numerical-rule change. SERIALIZATION_REPLAY_CHECK.json confirms all first-case arrays in the original and amended runs are bit-identical. Active results are RESULTS_v02.json and run_v02/; active verification is VERIFICATION_v02.json.

The attached historical v0.39 ledger does not reverse later v0.85 repairs; no universal G05 or4/3 damping identification enters this model. The CRL-2 governance allows labeled development but does not turn constructor checking into promotion. Gap2_FINAL_Finite_Genesis.png remains unavailable.

## Consequence for the graphite question

The omitted internal lateral coordinates can be represented exactly as finite vertical memory in this declared harmonic model. This completes that reduction, while the mean relative-layer x/y sliding coordinates are still held fixed by the existing preparation constraints. Therefore this vertical-memory calculation is not yet the force response of a driven sliding port. The next material-model step is to introduce the two relative-layer mean sliding coordinates as explicit controlled ports and derive their coupling to the qualified internal modes. Physical dissipation and a native UD correspondence remain additional gates.

![Memory verification](MEMORY_CHECK.png)

A — DERIVED:exact conditional lateral-memory, initial-source and storage identities.
B — NUMERICAL:4/4 models,16/16 preparations pass;12 source-omission controls visibly fail and4 conditional controls match.
C — OPEN/HOLD:sliding-force port, physical bath/clock, native correspondence and non-constructor review.
D — Physical promotion0; Development — no registry entry.

1. Next: construct the relative-layer sliding port and derive its internal-mode memory, with physical dissipation kept as a separate gate. Priority97/100.
