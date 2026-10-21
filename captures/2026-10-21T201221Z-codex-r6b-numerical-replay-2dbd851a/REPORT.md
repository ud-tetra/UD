# Bounded R6b numerical replay

RESULT — PASS_NUMERICAL_SCOPED. A fresh, source-faithful L=4 reconstruction verifies the exact Theta spectrum, the unchanged clean coupled operator and the frozen component-aware diagnostics. Source inputs, numerical settings, runtime versions, starting vector, matrix hashes and implementation hashes were frozen before eigensolver execution. Physical promotion0; constructor execution only; no independent review or blind particle target run.

This is a new implementation of the recovered clean R6b equations. The archived scripts were read but not imported or executed. It is not authentication of a historical run or a replay of the VersionB disorder ensemble. Source main is c6b66d68a25b655627d6eb6f1bf6f96a13e2121b. The prior modular contract remains pinned by SHA256 75942451ae44fc907450f72500ac27db4b81e8e0cd27e5d8a5023cd6622a6e10.

## 1. Frozen execution

L=4,N=256; Theta and rho have256 coordinates each; the coupled matrix has512. The four64-site components and identity metric are unchanged. We retain eta=185/192, rho sibling weight eta^2, Theta cousin/second-cousin weights eta^4/eta^6, original depth potentials and parity cross coupling. No new edges, disorder or coefficient fit was introduced.

PRE_RUN_RECEIPT.json binds SETTINGS.json, INPUTS.npz, the two new implementation files and original source scripts. The runtime is Python3.12.14, NumPy2.3.5 and SciPy1.17.0. The supplied initial vector is generated from recorded PCG64 state and seed20261021 and stored in the payload. Scientific runtime versions and allowed thread settings are recorded; no account or credential data are included.

Dense eigh uses driver evd. Global and component-by-component decompositions retain all eigenpairs. Sparse eigsh uses k10,ncv64,tol1e-12,maxiter12800, explicit v0 and the source's exposed probe positions0.00133 and1e-8. Numerical clusters are defined by span from the first eigenvalue with absolute tolerance1e-10 and relative tolerance1e-12; these are numerical groupings, not exact-degeneracy theorems. Six-decimal deduplication is not used. Partial cluster coverage is reported, not interpreted as a complete spectral projector.

Residual tolerance is5e-12 after scaling by max(1,||H||_infinity+|lambda|); orthogonality Frobenius tolerance1e-10. Exact-Theta projector tolerance is1e-10; the coupled global-versus-blockwise relative projector tolerance is1e-4. These settings were fixed before the run and are mathematical computation checks, not experimental localization thresholds.

## 2. Exact-spectrum comparison

| Theta eigenvalue | Expected global rank | Returned rank | Maximum absolute eigenvalue error |
|---|---:|---:|---:|
| 0 | 4 | 4 | 6.58e-14 |
| 12 eta^4+48 eta^6 | 192 | 192 | 1.42e-13 |
| 64 eta^6 | 12 | 12 | 6.39e-14 |
| 16 eta^4+48 eta^6 | 48 | 48 | 1.42e-13 |

The numerical projectors agree with the known rational block projectors within1.31e-13 Frobenius norm. The global Theta null projector has rank4. Returned component-uniform zero modes have global F about4 and conditioned within-component F about1, as the prior exact controls predict.

## 3. Coupled low modes and component conditioning

The clean coupled matrix has28 numerical clusters at the frozen resolution. The four lowest Theta-dominated modes separate into one root-prefix-zero mode and a three-dimensional numerical cluster supported on the other three modules.

| Diagnostic | Fresh result |
|---|---|
| Lowest Theta-dominated eigenvalue | approximately -1.61452e-8 |
| Next three Theta-dominated eigenvalues | approximately -5.0584e-10 |
| Theta channel weight of these modes | greater than0.99999999 |
| Conditioned within-module F | numerically1, at reported floating precision |
| Global F for sparse returned low Theta vectors | approximately3.15 to4.00 |
| Complete rank3 cluster's normalized Theta projector density | global F=4/3; within-module F=1 |

These results show no resolved within-module concentration for these four low Theta modes at this level. They do not show that every coupled mode is delocalized or that the exact coupled eigenvectors are perfectly uniform. Differences below floating resolution are not exact equalities. The sampled higher-level historical outputs and the VersionB disorder ensemble remain outside this execution.

Global scores change with component occupancy and the solver's basis within a repeated eigenspace. The complete rank3 projector density occupies three modules, whereas a component-resolved basis can occupy one per vector. Both descriptions are consistent with the same subspace. Normalized IPR is always accompanied by the actual channel weight; tiny-weight channels are flagged as numerically sensitive.

## 4. Probe coverage is incomplete

| Probe | Returned coverage of reference numerical clusters |
|---|---|
| 0.00133 | 10 directions from one rank48 cluster |
| 1e-8 | Complete ranks1 and3 low clusters, plus6 directions from that rank48 cluster |

All returned vectors have valid residuals at the frozen tolerance, but the rank48 space is incomplete in both probes. The rho-near probe contains no Theta-dominated vector in its returned set. A missing candidate in a truncated probe is not proof that the mode is absent from the operator. In particular, selecting the first returned mode or comparing individual F values does not compare complete physical sectors.

The completed rank1/rank3 sparse projectors agree with the dense reference to relative Frobenius errors approximately7.84e-13 and8.29e-12. Partial rank48 vectors lie within the reference space to about1.03e-12, but they do not span it. We retain all eigenpairs and label that coverage INCOMPLETE_EIGENSPACE.

## 5. Numerical conditioning and limits

Maximum dense coupled scaled residual is8.33e-16. The largest scaled residual across the two sparse probes is1.02e-13. No solver exceptions or warnings were returned in this run. The saved payload verifier independently recomputes residuals and orthogonality from serialized arrays and checks all hashes.

A high-energy, rho-dominated rank2 cluster around3.71749418593 has a neighboring gap about1.79e-10. Its global-versus-blockwise relative projector difference is6.34e-5, the largest observed, inside the predeclared1e-4 tolerance. Small residuals do not remove subspace sensitivity near such narrow separations. That cluster is not a high-precision spectral-identification result. We did not adjust cluster or projector tolerances after seeing it.

The matrix is reconstructed from the source equations rather than a hash-bound historical matrix payload. Floating accumulation order may differ from the archived implementation while preserving the equations. PRE_RUN_RECEIPT.json makes the new matrix bytes explicit. No fundamental particle, mass, action unit or localization threshold is inferred from this finite replay.

## 6. Reproducibility and next action

INPUTS.npz stores the actual matrices, source address depth/parity arrays and initial vector. NUMERICAL_PAYLOAD.npz adds every dense, componentwise and sparse eigenpair. RESULTS.json records clusters, projectors, residuals, probe coverage, channel/component diagnostics and the empty failure log. VERIFICATION.json checks serialized evidence. The new scripts are provided; no imported archived code is required to inspect the payload.

Official SciPy1.17.0 contracts were checked for shift-invert semantics, explicit starting vectors, partial ARPACK returns and the symmetric dense solver. See DOCUMENTATION.json for exact URLs and scope. The documented API is implementation context, not evidence for the UD model.

Priority100 next: derive the coupled low-mode reduction and certify the component-conditioned conclusion analytically, beginning with the three equal depth1 modules. That separates genuine within-module structure from degenerate module mixing without adding a new global interaction. Close high-energy cluster separation can be addressed as a distinct numerical-conditioning task if it becomes relevant to a proposed observable.

Generated and executed: a new bounded numerical implementation under frozen settings. Checked: exact Theta spectra, coupled residuals, numerical projectors, component diagnostics and serialized custody. Constructor only; independent review pending; no registry or physical promotion. Gap2_FINAL_Finite_Genesis.png remained unavailable and was not used.
