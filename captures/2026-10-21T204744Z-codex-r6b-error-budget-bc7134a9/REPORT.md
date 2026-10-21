# R6b low modes: source assembly and solver error budget

**PASS_SCOPED — EXACT CONDITIONAL bounds on the rational source and the stored replay bytes.** Development — no registry entry. Constructor: Codex; non-constructor reviewers: none. Physical promotion: 0.

The audit closes the eigenvalue error decomposition for the four negative low modes of the clean L=4 R6b replay. It does not promote a physical interpretation, replace the original thresholds, or certify new channel weights for the floating matrix.

## Result

Let lambda_src be a source-model eigenvalue, lambda_IEEE the corresponding exact eigenvalue of the stored IEEE matrix considered as a rational matrix, and lambda_returned the stored solver return. Exactly,

\[
\lambda_{\rm returned}-\lambda_{\rm src}
=(\lambda_{\rm IEEE}-\lambda_{\rm src})
 +(\lambda_{\rm returned}-\lambda_{\rm IEEE}).
\]

The first term is source-to-stored assembly error. The second is the error in the stored eigenvalue returned by the solver.

| Module first digit | Rational source ground eigenvalue, approximately | Stored matrix ground eigenvalue, approximately | Assembly shift, approximately |
|---|---:|---:|---:|
| 0: varying depth | -1.6145247540177632e-8 | -1.6145203575346149e-8 | +4.3964831483e-14 |
| 1 | -5.058799395853153e-10 | -5.058359747535502e-10 | +4.3964831765e-14 |
| 2 | -5.058799395853153e-10 | -5.058359747535502e-10 | +4.3964831765e-14 |
| 3 | -5.058799395853153e-10 | -5.058359747535502e-10 | +4.3964831765e-14 |

Every stored-matrix interval has width less than 1e-23; actual widths are approximately 2.32e-25 for module 0 and 4.56e-25 for the three other modules. Rounded table values are displays, not interval endpoints. AUDIT.json contains outward rational enclosures.

| Stored solver output | Negative modes covered | Largest absolute solver eigenvalue error, approximately |
|---|---:|---:|
| Full dense solve | 4 | 2.89337e-14 |
| Blockwise dense solve | 4 | 1.27534e-15 |
| Sparse probe sigma=1e-8 | 4 | 4.58270e-15 |
| Sparse probe sigma=0.00133 | 0 | Not applicable to these low modes |

The three stored depth-1 modules are exactly related by a rho sign gauge, checked entry by entry. Their stored spectra are identical. Consequently a sparse solver may mix these modules without changing the eigenvalue being compared; the audit checks membership in the three-module family rather than requiring localization within a single module.

The assembly shift is about 2.72e-6 of the varying-depth source eigenvalue magnitude and 8.69e-5 of the depth-1 magnitude. Small absolute residuals do not by themselves establish many correct relative digits for these eigenvalues.

## Provenance and exact arithmetic

The replay is the fresh reconstruction captured in PR352, commit `524f180d3f903267925d48599add52acb9301d6b`, not an execution of historical recovered code. Payload SHA-256 is `fa6f6c4fa3dc9d1c13d0a9d0418cef93d1fd6d03cdfa0370055796164767fd3f`. The audit checks this hash, the prior results-to-payload link, receipt hash, stored matrix hash, and frozen settings hash before analysis. It checks matrix symmetry and every off-module entry is zero.

The six-coordinate certificate and its fresh verifier are copied byte-for-byte from PR356's checked local tree, with hashes recorded. Calling that verifier's run function regenerates its exact result and must equal the imported certificate. The depth-1 source root is independently bisected for 160 steps using its exact quadratic. Both source anchors are then used to construct rational trial vectors in the full 128-coordinate modules. No eigensolver is invoked in this audit.

Each stored binary64 matrix entry and eigenvector coordinate is read exactly as a Fraction. All matrix differences, trial Rayleigh quotients, residual variances, gap bounds, solver residuals, and interval subtractions use rational arithmetic. Report intervals are enlarged outward onto the rational grid 10^(-65). Decimal strings are readable displays only. NumPy is used for safe NPZ loading and byte/shape checks, with pickle disabled.

## Why the stored-matrix bounds are valid

For each source module H, let E be the maximum absolute row sum of H_IEEE-H, computed exactly. Both matrices are symmetric, so their spectral norm difference is at most E. The measured bounds are approximately 5.818e-14.

Let v_min be the minimum rho potential, c_max the maximum coupling magnitude, and g0=12 eta^4+48 eta^6. On the codimension-one subspace in which the Theta coordinates sum to zero, the source quadratic form is at least

\[
\frac{v_{\min}}2\|x\|^2+
\left(g_0-\frac{2c_{\max}^2}{v_{\min}}\right)\|y\|^2.
\]

The second coefficient exceeds alpha=v_min/2, verified rationally. The min-max principle gives source lambda_2 >= alpha. The symmetric perturbation bound gives stored lambda_2 >= beta=alpha-E>0.

For any nonzero rational trial vector v, compute exactly

\[
\mu=\frac{v^T H_{\rm IEEE}v}{v^T v},\qquad
s^2=\frac{\|(H_{\rm IEEE}-\mu I)v\|^2}{v^T v}.
\]

The trial vectors here satisfy mu<0<beta. Their variances are approximately 3.02923e-28. The ground eigenvalue obeys

\[
\boxed{\mu-\frac{s^2}{\beta-\mu}\le\lambda_{1,\rm IEEE}\le\mu}.
\]

For completeness, the lower bound follows by averaging (t-lambda_1)(t-beta) over the trial vector's spectral measure. The product is zero at the ground eigenvalue and nonnegative at every other eigenvalue because t>=beta. Therefore s^2+(mu-lambda_1)(mu-beta)>=0. The upper bound is the Rayleigh principle. Since beta>0 and mu<0, the negative stored eigenvalue is unique. This argument does not assume the source reduction stays invariant after floating assembly.

Subtract the exact source enclosures from these stored-matrix enclosures to bound assembly error. Subtract the stored-matrix enclosures from each exact stored solver return to bound solver error. The identity in the first section then gives the source error budget without fitting any coefficient or tolerance.

## Original acceptance rule retained

For all 12 negative low-mode returns (four dense, four blockwise, four sparse), the audit recomputes residuals over all 512 coordinates, including module mixtures, using the original rule

\[
\frac{\|Av-\lambda v\|}{\max(1,\|A\|_\infty+|\lambda|)}\le5\times10^{-12}.
\]

It checks the squared inequality exactly, without changing normalization or threshold. All pass. Prior orthogonality, clustering and projector checks are preserved as prior receipts; they are not rerun here. The sigma=0.00133 probe did not return these low modes, so it supplies no low-mode coverage. No new relative-error acceptance threshold has been introduced.

## Reproduction and remaining gates

Run `audit_replay.py --payload <PR352 NUMERICAL_PAYLOAD.npz> --results <PR352 RESULTS.json> --receipt <PR352 PRE_RUN_RECEIPT.json>`. The needed source receipts are identified by commit and hashes in PROVENANCE.json; upstream binary evidence is not duplicated. Output is AUDIT.json.

This closes the scoped eigenvalue error budget. Floating eigenvector/channel-profile errors and all particle/action-unit correspondences remain open. A next useful step is to assemble the exact reductions and this audit into one non-constructor review packet. Independent review is not supplied by constructor rechecks. No CRL promotion or registry entry is made. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used.
