# UD first closure package: finite observation, five-cell dynamics and transfer

14 October 2026. Development — no registry entry. Physical promotion: 0.

## Execution result

The first package is executed as a scoped mathematical programme. Source reconciliation, declared comparison contracts, Gaussian readout formulas, five-cell spectra, and an orthogonal interface with retained residuals are established. Native source and configuration selection remain OPEN: the reconciled sources explicitly underidentify them. No missing source was replaced by a fitted coefficient or a candidate silently promoted to native law.

## 1. Reconciled source baseline

Repository `ud-tetra/UD` was inspected and cloned at commit `4b9c1f7ba03f76324b792f389517161d2bc47e05`. The recursive tree was complete, with 673 entries. Each of the four M5 manuscript sources matches the current repository paper blob exactly:

| Paper | Git blob SHA-1 |
|:--|:--|
| I | `248a9e33dd0c459b154383c336d980b0ab4e6b4e` |
| II | `d618031eb252ae6334ac30298e5b9c948658125e` |
| III | `6cd972467c98eedcee106d93fee65d7c4c7153f0` |
| IV | `0c33d4e8d774f3d53afc1fc0cb643b88a26eeb51` |

The portal's current visible paper edition also lists I–III 1.1.1 and IV 0.1. Later repository captures add results without rewriting those four texts. Nine selected source reports were recovered and their bytes checked against the pinned tree. Additional local captures on predictive records and record entropy were inspected for scope.

Important amendments for this package are: exact conditional Theta-to-closure pushforward; a native pre-event factorization obstruction; action/proposal underdetermination; candidate balance-trigger subdivision; bounded subdivision with residual completion; strict interface incompatibility; and the polarity-pipeline counterexamples. The record-entropy session already contains candidate write and thermal mechanisms but leaves complete resource renewal and native parameter sources open. Thus the manuscript gap list represents integration gaps as well as genuinely unresolved source mechanisms.

This is a targeted reconciliation of the first package, not proof that every later result has been absorbed into the manuscript.

## 2. Frozen comparison contracts

**C1 — noisy two-cell observation.** Carrier is `0123,0124`, with increasing-order simplex orientations and unit-metric skew incidence flow. Source label Z is equiprobable L/R, prepared in the two unit cell states with every other coordinate zero. Observe either the two cell amplitudes, or the four coordinates `(q,q'/sqrt(3))`. Measurement time is known. Add independent Gaussian noise of covariance `sigma² I` in the declared observation coordinates. This is a mathematical readout model, not measured/native noise. Units are model amplitude units; derivative normalization fixes an observation scale, not a free physical sensor.

**C2 — five-cell architecture comparison.** Compare the core-star cells `0123,1234,0235,0136,0127` with the chain `0123,1234,2345,3456,4567`. Both have 47 coordinates and 12 boundary faces. Use the same scale `A/sqrt(8)`, admitted operator-norm ceiling 1, initial norm 1, equal-prior alternatives in the first and last listed cells, cell-only readout, sigma=1/4, and horizon `[0,pi]` in the scaled model parameter. Exact rational LDL proves `8I-L` positive definite for both, so both satisfy the ceiling. Their actual norms differ; the comparison matches a resource ceiling, not identical expenditure. Their preparation sites have different structural roles, so this single preparation does not establish architecture-wide superiority.

The reported 129-point comparison is NUMERICAL under C2. The finite horizon, noise and scale are protocol choices, not theory constants. A general worst-time or preference theorem needs additional certification or preparation averaging.

## 3. Exact Gaussian readout and uncertainty

For two Gaussian output laws with known means mu_L, mu_R, common positive-definite covariance Sigma and equal priors, let delta=mu_L-mu_R. The likelihood-ratio statistic is linear, and its exact Bayes error is

\[
P_e=\Phi\!\left(-\tfrac12\sqrt{\delta^T\Sigma^{-1}\delta}\right).
\]

Proof: center at `(mu_L+mu_R)/2` and project with `Sigma^{-1}delta`. The score has means `±delta^T Sigma^{-1}delta/2` and variance `delta^T Sigma^{-1}delta`; threshold zero gives the expression. At delta=0 the outputs coincide and error is 1/2. Singular covariance requires a different support-sensitive statement.

For C1 cell-only observation,

\[
\delta_q=\cos(\sqrt3s)(1,-1),\qquad
P_e(s)=\Phi\!\left(-\frac{|\cos(\sqrt3s)|}{\sqrt2\sigma}\right).
\]

For the augmented observation, `delta_{q'/sqrt(3)}=-sin(sqrt(3)s)(1,-1)`. Consequently its separation squared is exactly 2 for every s, and

\[
P_e^{\mathrm{aug}}=\Phi(-1/(\sqrt2\sigma)).
\]

At sigma=1/4 this is approximately 0.00233886749, while the cell-only error is 1/2 at its blind instants. The augmented receiver observes four channels rather than two, and this gain cannot be called free. No physical derivative-acquisition or retained-memory cost is closed here.

The symmetric optimal hard decision defines a binary channel with `I(Z:Zhat)=ln2-h(P_e)`. This is decision information, not the full continuous-output mutual information, irreversible record entropy or information already stored in a memory. Data processing bounds it above by the full analog information.

For correlated multiple observations, stack the entire mean difference and use the complete Sigma. An exact stipulated witness `delta=(1,1)`, `Sigma=[[1,1/2],[1/2,1]]` gives squared Mahalanobis distance 4/3 rather than the incorrect independent value 2. Repeated observations with shared noise are not independent confirmations.

For m declared Gaussian residual coordinates with known marginal deviations sigma_i, Bonferroni gives simultaneous residual coverage at least `1-alpha` using thresholds `sigma_i Phi^{-1}(1-alpha/(2m))`, without independence. This is coverage under the declared Gaussian law, not coverage inferred from covariance alone. Unknown covariance estimation needs its own uncertainty contract. Uncertain measurement time can mix the output laws and invalidate the known-time formula; no jitter law is assumed here.

## 4. Exact five-cell core-star spectrum

The core-star has `f=(8,18,16,5)`, chain dimension 47 and 12 exposed faces. Exact signed incidence construction, boundary cancellation and characteristic-polynomial factorization give

\[
\begin{aligned}
\chi_{\star}(x)={}&x(x^2+2)(x^2+3)^2(x^2+4)^3(x^2+5)^3(x^2+6)^2\\
&\times(x^4+9x^2+16)^3(x^4+10x^2+20)^3.
\end{aligned}
\]

The positive squared frequencies and each sign's multiplicities are

| Squared frequency | Multiplicity of each ±i frequency |
|:--|--:|
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 3 |
| 6 | 2 |
| `(9-sqrt(17))/2`, `(9+sqrt(17))/2` | 3 each |
| `5-sqrt(5)`, `5+sqrt(5)` | 3 each |

There is one zero mode. The exact norm is `sqrt(5+sqrt(5))`. The squared-frequency multiplicities sum to 23, accounting for 46 active dimensions plus the zero mode.

With the stated cell ordering, the top-cell Gram matrix is

\[
H_3=\begin{pmatrix}
4&1&-1&1&-1\\1&4&0&0&0\\-1&0&4&0&0\\1&0&0&4&0\\-1&0&0&0&4
\end{pmatrix}.
\]

Let b=(1,-1,1,-1) in the four leaf coordinates. Every leaf vector orthogonal to b has eigenvalue 4; this is a three-dimensional cell sector. On the core and normalized collective leaf b/2, the matrix is `[[4,2],[2,4]]`, giving eigenvalues 2 and 6. Thus cell motion splits into three frequency-2 modes and two collective modes of frequencies sqrt(2), sqrt(6). This is an invariant top-cell oscillator decomposition, not a complete claim that all full-chain modes live on cells.

The chain's top-cell squared frequencies are `4-sqrt(3),3,4,5,4+sqrt(3)`. Its full characteristic polynomial is recorded exactly in `results.json`; it differs from the core-star despite identical f-vectors. The full norm is approximately 2.69936488629, compared with approximately 2.68999404786 for the star before common scaling.

No complete exact period exists for the core-star because it includes frequencies sqrt(2) and sqrt(3) with irrational ratio. The frequency-2 cell sector can be periodic. Lack of a global period is not dissipation, stability or formation preference.

The numerical C2 comparison is illustrative only. A distance grid can be supplemented by the analytic Lipschitz estimate: since the generator ceiling is 1 and the initial difference norm is sqrt(2), the cell distance changes at most sqrt(2) per unit time. A nearest-grid cover gives a whole-interval error envelope from the sampled minimum. Floating evaluations have not been interval-certified, so the recorded envelope is not an exact numerical certificate. It cannot establish universal shape preference.

## 5. Interface transfer with a retained residual

Two independent tetrahedron carriers have 30 coordinates. The unique-simplex face-glued carrier has 23; the shared face contributes seven duplicate coordinates (three vertices, three edges, one face). For every consistently oriented pair of shared coordinates x,y, define

\[
z=(x+y)/\sqrt2,\qquad r=(x-y)/\sqrt2.
\]

Carry unshared coordinates unchanged. This defines Q: R30→R23 and R: R30→R7 with orthogonal completion U=(Q;R), so

\[
\|Qv\|^2+\|Rv\|^2=\|v\|^2.
\]

The transfer is invertible when residuals are retained. Agreement x=y sets r=0 but gives z=sqrt(2)x. A decoder z/sqrt(2) restores the shared amplitude convention. Simply calling z the old amplitude silently changes calibration.

This is a conditional linear interface/state-transfer contract. It does not claim chain-map compatibility or native move admission. For the direct-sum old generator, `G=U(A_tet direct-sum A_tet)U^T`, exact arithmetic gives visible/residual coupling rank 7. The visible block differs from the native glued generator with rank 14; `Q A_old-A_glued Q` has rank 21. Keeping residuals closes the transformed old dynamics; discarding them does not create the native glued flow.

Choosing post-event generator `A_glued direct-sum A_residual` is an additional intervention, even though it preserves total norm when both blocks are skew. Its source, locality and physical cost are unclosed. This exposes the event-local generator obligation rather than hiding it inside geometric identification.

The existing subdivision results give a second contract: `T=S/sqrt(24)` is a bounded chain map with residual `(I-T^T T)^{1/2}`, but attenuates vertex readout and fails unweighted flow intertwining. The stricter requirement of contraction, unit singleton vertex coefficient and unweighted intertwining is already excluded by the exact 7-versus-3 incidence norm witness. These are different contracts; neither selects native geometry change.

## 6. Native selection: established boundary and remaining positive task

Later sources already provide

\[
\Theta^+=P_g\Theta^-\oplus\xi
\]

and an exact closure/hard-mask pushforward when the receipt xi and relevant local transport gates are supplied. The package rechecks 24,576 fixed-gate cases. This closes a conditional map, not the source of xi, gate updates or event occurrence.

At identical native pre-state, formal receipt completions xi=000 and xi=111 give different endpoints. Both identity and complementation commute with pair permutations. Hence symmetry and the fixed pre-event chain trajectory do not uniquely select the endpoint under that interface. The positive repair must make the set of admitted next outputs a singleton, or specify a complete normalized stochastic kernel with receipt availability, null windows and timing separately typed.

The balance observable `E3-E2` supplies a pre-event signal; treating its crossing as a subdivision command is a candidate constitutive rule. The historical action/Metropolis acceptance likewise fails to select proposal frequency or admissible moves. The later polarity audit shows that universal signed-flux/index agreement and simultaneous nontrivial burden selection under binding saturation fail on stated counterexamples.

Therefore G05/G06/G09 remain source-open. The next positive task is an explicit joint state `(K,c,Theta,transport,source,reservoir)` with lawful pre-event generator, move eligibility, transfer, generator change and resource update. Supplying one such rule establishes a candidate model; a uniqueness or native-source theorem needs additional justified restrictions. There is no derivation of that rule from the reconciled fixed-flow equations alone.

## 7. Gap dispositions

| Gap | Outcome |
|:--|:--|
| E01 | Four paper bytes reconciled; targeted later source results integrated; broader project reconciliation remains partial. |
| G01 | Closed for C1/C2, not universal across UD. |
| G02/G04 | Exact conditional Gaussian readout and dependence-aware decision formulas; physical noise/acquisition remains open. |
| G03 | Exact core-star and chain spectra and top-cell sectors; one numerical comparison; robustness/formation ranking remains open. |
| G08/G10 | Conditional orthogonal copy-to-interface transfer and exact dynamic defects; native gluing/source selection remains open. |
| G05/G06/G09 | Source underidentification reconciled and tested; no native law promoted. |

`verify_first_package.py` regenerates exact certificates and separately labeled numerical fixtures. Constructor checks are not independent review. All protocol choices and source hashes are retained. No physical experiment, outside review, or autonomous apparatus is claimed.
